import process from 'process'
import fs from 'fs'
import { DOMParser } from '@xmldom/xmldom'
import path from 'path'

process.chdir(path.join(__dirname, 'xml'))
const xmlPaths = fs.readdirSync('.', 'utf-8').filter(x => x.startsWith('class_'))


type XMLElement = {
    tag: string,
    attrs: Record<string, string>,
    text?: string,
    childs?: XMLElement[],
    parent?: XMLElement,
} 

async function toXML(xmlStr: string): Promise<XMLElement> {
    function go(xmlObj: Node): XMLElement | undefined {
        if (xmlObj.TEXT_NODE === xmlObj.nodeType) {
            if (!xmlObj.nodeValue || xmlObj.nodeValue.trim() === '') {
                return
            }
            return {
                tag: 'text',
                attrs: {},
                text: xmlObj.nodeValue!
            }
        }

        const element = xmlObj as HTMLElement
        const tag = element.tagName;
        
        const attrs: Record<string, string> = {};
        for (let i = 0; i < element.attributes.length; i++) {
            const item = element.attributes.item(i)!
            attrs[item.nodeName] = item.nodeValue ?? ''
        }
        const childs: XMLElement[] = []

        for (let i = 0; i < element.childNodes.length; i++) {
            const child = go(element.childNodes[i])
            if (child) childs.push(child)
        }
        return {
            tag, attrs, childs
        }
    }
    const parser = new DOMParser()
    const xml = parser.parseFromString(xmlStr)
    const res = go(xml.documentElement)!

    function setParent(node: XMLElement, parent?: XMLElement) {
        node.parent = parent
        for (const child of node.childs ?? []) {
            setParent(child, node)
        }
    }
    setParent(res)
    return res
}

function querySelectorsAll(xml: XMLElement, p: (xml: XMLElement) => boolean): XMLElement[] {
    function go(xml: XMLElement, p: (xml: XMLElement) => boolean): XMLElement[] {
        if (p(xml)) {
            return [xml]
        }
        if (xml.tag !== 'text') {
            const res: XMLElement[] = []
            // @ts-ignore
            for (const child of xml.childs) {
                res.push(...go(child, p))
            }
            return res
        }
        return []
    }
    return go(xml, p)
}

function querySelector(xml: XMLElement, p: (xml: XMLElement) => boolean): XMLElement {
    const res = querySelectorsAll(xml, p)
    debugger
    if (res.length === 0) {
        throw new Error('not found')
    }
    if (res.length >= 2) {
        throw new Error(`multiple result`)
    }
    return res[0]
}

function mapAndSmartConcat(xmls: XMLElement[], f: (xml: XMLElement) => string): string {
    
    if (xmls.length === 0) {
        return ''
    }
    const contents = xmls.map(f)
    for (let i = 1; i < contents.length - 1; i++) {
        if (contents[i].startsWith(' ') && contents[i - 1].endsWith(' ')) {
            contents[i] = contents[i].substring(1)
        }
        if (contents[i].endsWith(' ') && contents[i + 1].startsWith(' ')) {
            contents[i] = contents[i].substring(0, contents[i].length - 1)
        }
    }
    return contents.join('')
}

function xmlsLiteral(xmls: XMLElement[]): string {
    return mapAndSmartConcat(xmls, xmlLiteral)
}

function xmlLiteral(xml: XMLElement): string {

    if (xml.tag === 'text') {
        return xml.text ?? ''
    }
    if (xml.tag === 'ref') {
        return xmlsLiteral(xml.childs ?? [])
    }

    throw new Error(`undefined tag: ${xml.tag}`)
}

type ClassMember = ({
    type: 'function' | 'constructor_',
    isStatic: boolean,
    returnType: string,
} | {
    type: 'signal',
}) & {
    name: string,
    params: [string, string, any?][],
    briefDescription: XMLElement,
    detailedDescription: XMLElement,
}

function extractDefs(root: XMLElement): [string, ClassMember[]] {
    const className = xmlsLiteral(querySelector(root, xml => xml.tag === 'compoundname').childs ?? [])
    const defs = querySelectorsAll(root, x => x.tag === 'memberdef' && x.attrs.prot === 'public')

    // @ts-ignore
    return [className, defs.flatMap(def => {
        const nameElem = querySelector(def, xml => xml.tag === 'name')
        const name = xmlLiteral(nameElem.childs![0])
        const kind = def.attrs.kind

        if (kind === 'property' || name.startsWith('~') || name.startsWith('operator')) {
            console.log(`skip ${kind} ${name}`)
            return []
        }

        const paramElems = querySelectorsAll(def, xml => xml.tag === 'param')
        const briefDescription = querySelector(def, xml => xml.tag === 'briefdescription')
        const detailedDescription = querySelector(def, xml => xml.tag === 'detaileddescription')

        const params: [string, string, any?][] = []

        for (const paramElem of paramElems) {
            const paramType = getPyType(xmlsLiteral(querySelector(paramElem, xml => xml.tag === 'type').childs!))
            const paramName = getPyType(xmlsLiteral(querySelector(paramElem, xml => xml.tag === 'declname').childs!))
            let defval: any = undefined
            for (const valElem of querySelectorsAll(paramElem, xml => xml.tag === 'defval')) {
                const elem = xmlsLiteral(valElem.childs!)
                if (+elem === 0 && paramType !== 'int' && paramType !== 'float') {
                    defval = null
                } else {
                    defval = elem
                        .replace(/false/g, 'False')
                        .replace(/true/g, 'True')
                }
            }
            params.push([paramType, paramName, getPyValue(defval)])
        }
        
        if (kind === 'slot' || kind === 'function') {
            const retTypeElem = querySelector(def, xml => xml.tag === 'type' && xml.parent?.tag === 'memberdef')
            const retType = getPyType((retTypeElem.childs && xmlsLiteral(retTypeElem.childs)) || name)

            // console.log('F', name, `(${params.map(([t, n, v]) => `${n}: ${t}${v !== undefined ? ` = ${v}` : ''}`).join(', ')}): ${retType}`)
            return [{
                type: retType === className ? 'constructor_' : 'function',
                name,
                isStatic: def.attrs.static === 'yes',
                params,
                returnType: retType,
                briefDescription,
                detailedDescription
            }]

        } else if (kind === 'signal') {
            return [{
                type: 'signal',
                name,
                params, 
                briefDescription,
                detailedDescription
            }]
        } else {
            throw new Error(`undefined kind: ${kind}`)
        }
    })]
}

function getPyType(cppType: string): string {
    return cppType
        .replace(/const/g, '')
        .replace(/QStringList/g, 'List[str]')
        .replace(/QString/g, 'str')
        .replace(/QMap/g, 'dict')
        .replace(/QList/g, 'List')
        .replace(/qreal/g, 'float')
        .replace(/void/g, 'None')
        .replace(/QVector/g, 'List')
        .replace(/double/g, 'float')
        .replace(/[ \*&]/g, '')
        .replace(/</g, '[')
        .replace(/>/g, ']')
        .trim()
}

function getPyValue(cppValue: any): any {
    if (cppValue === undefined) {
        return undefined
    }
    if (cppValue === null) {
        return 'None'
    }
    if (!isNaN(+cppValue)) {
        return +cppValue
    }
    const value = '' + cppValue
    const QSTRING_REGEX = /QString\((?:"(.*?)")?\)/
    const qstringMatch = QSTRING_REGEX.exec(value)
    if (qstringMatch) {
        return `"${qstringMatch[1] ?? ''}"`
    }
    return value
}

function briefDescriptionToDocStr(def: ClassMember): string {
    function go(xml: XMLElement): string {
        if (xml.tag === 'text') {
            return xml.text!
        }
        if (xml.tag === 'briefdescription') {
            return gos(xml.childs ?? [])
        }
        if (xml.tag === 'para') {
            return `\n${gos(xml.childs ?? [])}\n`
        } https://api.kde.org/krita/html/classChannel.html
        if (xml.tag === 'emphasis' || xml.tag === 'computeroutput') {
            return `\`${gos(xml.childs ?? [])}\``
        }
        if (xml.tag === 'ref') {
            const className = gos(xml.childs ?? [])
            return `[${className}](https://api.kde.org/krita/html/class${className}.html)`
        }
        throw new Error(`undefined tag: ${xml.tag}`)
    }
    function gos(xml: XMLElement[]): string {
        return mapAndSmartConcat(xml, go)
    }
    return go(def.briefDescription).replace(/\n\n\n+/g, '\n\n')
}


function detailedDescriptionToDocStr(def: ClassMember) : string {
    let returnDesc = ''
    let paramDesc: Record<string, string> = {}

    function initParamList(xml: XMLElement) {
        for (const itemElem of querySelectorsAll(xml, x => x.tag === 'parameteritem')) {
            const nameElem = querySelector(itemElem, x => x.tag === 'parametername')
            const descElem = querySelector(itemElem, x => x.tag === 'parameterdescription')
            const name = gos(nameElem.childs ?? [])
            const desc = gos(descElem.childs ?? [])
            paramDesc[name] = desc
        }
    }
    
    function go(xml: XMLElement): string {
        if (xml.tag === 'itemizedlist') {
            return '\n\n' + gos(xml.childs ?? []).trimStart()
        }
        if (xml.tag === 'ndash') {
            return '-'
        }
        if (xml.tag === 'listitem') {
            const child = gos(xml.childs ?? [])
            return `- ${child.trim()}\n`
        }
        if (xml.tag === 'parameterlist') {
            initParamList(xml)
            return ''
        }
        if (xml.tag === 'ulink') {
            const url = xml.attrs.url
            const content = gos(xml.childs ?? [])
            return `[${content}](${url})`
        }
        if (xml.tag === 'programlisting') {
            let res = ''
            for (const child of xml.childs ?? []) {
                if (child.tag !== 'codeline') {
                    throw new Error('!')
                }
                res += gos(child.childs ?? []) + '\n'
            }
            return `\`\`\`\n${res.trim()}\n\`\`\`\n`
        }
        if (xml.tag === 'sp') {
            return ' '
        }
        if (xml.tag === 'simplesect') {
            if (xml.attrs.kind === 'return') {
                returnDesc = gos(xml.childs ?? [])
                return ''
            }
            if (xml.attrs.kind === 'see') {
                return gos(xml.childs ?? [])
            }
            throw new Error(`? ${xml.attrs.kind}`)
        }
        if (xml.tag === 'text') {
            return xml.text!
        }
        if (xml.tag === 'detaileddescription' || xml.tag === 'highlight' || xml.tag === 'verbatim') {
            return gos(xml.childs ?? [])
        }
        if (xml.tag === 'para') {
            const prefix = xml.parent?.tag === 'itemizedlist' ? '' : '\n';
            return `\n${gos(xml.childs ?? [])}\n`
        } 
        if (xml.tag === 'emphasis' || xml.tag === 'computeroutput' || xml.tag === 'bold') {
            return `\`${gos(xml.childs ?? [])}\``
        }
        if (xml.tag === 'ref') {
            const className = gos(xml.childs ?? [])
            if (className.endsWith(')')) {
                return `\`${className}\``
            }
            return `[${className}](https://api.kde.org/krita/html/class${className}.html)`
        }
        throw new Error(`undefined tag: ${xml.tag}`)
    }


    function gos(xml: XMLElement[]): string {
        return mapAndSmartConcat(xml, go)
    }

    const desc = go(def.detailedDescription)

    let res = ''
    if (desc.trim().length !== 0) {
        res += desc.trimEnd() + '\n\n'
    }
    if (Object.keys(paramDesc).length !== 0) {
        res += '# Parameters\n\n'
        for (const [paramName, desc] of Object.entries(paramDesc)) {
            let paramType: string = ''
            let defval: any = undefined
            try {
                [paramType, , defval] = def.params.find(([,name,]) => paramName === name)!
            } catch(e) {}
            res += `- ${paramName}${paramType ? `: ${paramType}` : ''}${defval != undefined ? ` = \`${defval}\`` : ''}\n\n  ${desc.trim()}\n\n`
        }
    }

    if (returnDesc) {
        res += '# Returns\n\n'
        res += `${returnDesc}\n\n`
    }
    return res.replace(/\n\n\n+/g, '\n\n').trimEnd()
    
}

function getDocstr(def: ClassMember): string {
    const brief = briefDescriptionToDocStr(def)
    const detail = detailedDescriptionToDocStr(def)

    let res = ''
    if (brief.trim().length !== 0) {
        res += brief.trimEnd().replace(/(^\r?\n)+/g, '')
    }
    if (detail.trim().length !== 0) {
        
        res += '\n\n' + detail.replace(/(^\r?\n)+/g, '').trimEnd()
    }
    return res
}

function addIndent(str: string, indent: number): string {
    return str.split(/\r?\n/).map(line => {
        return line.padStart(line.length + indent)
    }).join('\n')
}

function toPythonDef(def: ClassMember): string {
    const paramStrs = def.params.map(([type, name, defval]) => {
        if (defval != undefined) {
            return `${name}: ${type} = ${defval}`
        }
        return `${name}: ${type}`
    })

    const realDocStr = getDocstr(def)


    let res: string = ''
    if (def.type === 'function') {
        let docStr = ''
        if (realDocStr.trim().length !== 0) {
            docStr += addIndent('"""', 2) + '\n'
            docStr += addIndent(realDocStr, 4) + '\n'
            docStr += addIndent('"""', 2)
        }
        if (def.isStatic) {
            res += '@staticmethod\n'
        } else {
            paramStrs.unshift('self')
        }
        res += `def ${def.name}(${paramStrs.join(', ')}) -> "${def.returnType}":\n`
        res += docStr  + '\n'
        res += addIndent('...', 2) + '\n'
    } else if (def.type === 'constructor_') {
        let docStr = ''
        if (realDocStr.trim().length !== 0) {
            docStr += addIndent('"""', 2) + '\n'
            docStr += addIndent(realDocStr, 4) + '\n'
            docStr += addIndent('"""', 2)
        }

        paramStrs.unshift('self')
        res += `def __init__(${paramStrs.join(', ')}) -> None:\n`
        res += docStr  + '\n'
        res += addIndent('...', 2) + '\n'
    } else {
        let docStr = ''
        if (realDocStr.trim().length !== 0) {
            docStr += addIndent('"""', 0) + '\n'
            docStr += addIndent(realDocStr, 2) + '\n'
            docStr += addIndent('"""', 0)
        }
        return `${def.name}: pyqtSignal\n${docStr}\n`
    }
    return res
}

; (async () => {
    let result = ''
    result += 'from typing import Protocol, List, Never\n'
    result += 'from PyQt5.QtCore import QObject, QUuid, QByteArray, QRect, QVariant, QPointF, QRectF, QPoint, pyqtSignal\n'
    result += 'from PyQt5.QtGui import QColor, QImage, QTransform, QIcon\n'
    result += 'from PyQt5.QtWidgets import QDockWidget, QMainWindow, QWidget, QAction\n\n'
    
    result += `KoCanvasBase = Never
    KisNodeSP = Never
    KisLayerSP = Never
    KoChannelInfo = Never
    KisImage = Never
    KisImageSP = Never
    KisCloneLayerSP = Never
    DockPosition = Never
    KisDocument = Never
    KisFileLayerSP = Never
    KisColorizeMaskSP = Never
    KisFilterMaskSP = Never
    KisFilterConfigurationSP = Never
    KisGeneratorLayerSP = Never
    KisAdjustmentLayerSP = Never
    KisGroupLayerSP = Never
    KisShapeGroupSP = Never
    KoShapeGroup = Never
    KoColor = Never
    KoResourceSP = Never
    KisPropertiesConfigurationSP = Never
    KisSelectionSP = Never
    KisSelectionMaskSP = Never
    KoShape = Never
    KisTransformMaskSP = Never
    KisTransparencyMaskSP = Never
    KoShapeControllerBase = Never
    KisView = Never
    KisShapeLayerSP = Never
    KisMainWindow = Never
    KoCanvasObserverBase = Never
    KoDockFactoryBase = Never
    KisPresetChooser = Never`
        .split(/\r?\n/g).map(x=>x.trim()).filter(x=>x).join('\n') + '\n\n'

    for (const xmlPath of xmlPaths) {
        const xml = await toXML(fs.readFileSync(xmlPath, 'utf-8'))
        const [className, defs] = extractDefs(xml)

        const mockClassMember: ClassMember = {
            type: 'constructor_',
            isStatic: false,
            briefDescription: querySelector(xml, x => x.tag === 'briefdescription' && x.parent!.tag === 'compounddef'),
            detailedDescription:  querySelector(xml, x => x.tag === 'detaileddescription' && x.parent!.tag === 'compounddef'),
            name: '',
            params: [],
            returnType: 'None',
        }

        const parents = 
            querySelectorsAll(xml, x => x.tag === 'basecompoundref' && x.parent!.tag === 'compounddef')
                .map(elem => xmlsLiteral(elem.childs ?? []).trim())
        const classDocStr = getDocstr(mockClassMember)
        
        result += `class ${className}${parents.length === 0 ? '' : `(${parents.map(x => `${x}`).join(', ')})`}:\n\n`
        result += addIndent('"""', 2) + '\n'
        result += addIndent(classDocStr, 4) + '\n'
        result += addIndent('"""', 2) + '\n\n'

        // // 处理signal，创建一个假的__init__去绑定signal
        // result += addIndent('def __init__(self, DO_NOT_CALL_ME: Never):', 2) + '\n'
        // result += addIndent('"""', 4) + '\n'
        // result += addIndent('仅用来标识signal，不要调用它', 6) + '\n'
        // result += addIndent('"""', 4) + '\n'
        // defs.filter(def => def.type === 'signal')

        // 处理构造器和函数
        defs.map(def=> {
            result += addIndent(toPythonDef(def), 2) + '\n\n'
        })
        // const count = defs.reduce((acc, x) => {
        //     if (!acc[x.type]) {
        //         acc[x.type] = 0
        //     }
        //     acc[x.type] += 1
        //     return acc
        // }, {} as Record<string, number>)
    }
    fs.writeFileSync('../krita.pyi', result)
    // console.log(JSON.stringify(querySelectorsAll(xml, x => x.tag === 'memberdef' && x.attrs?.kind === 'function')[0], null, 4))
})();;