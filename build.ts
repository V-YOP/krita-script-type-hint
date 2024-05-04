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

function xmlsToPlainText(xmls: XMLElement[]): string {
    if (xmls.length === 0) {
        return ''
    }
    const contents = xmls.map(xmlToPlainText)
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

function xmlToPlainText(xml: XMLElement): string {

    if (xml.tag === 'text') {
        return xml.text ?? ''
    }
    if (xml.tag === 'ref') {
        return xmlsToPlainText(xml.childs ?? [])
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
    const className = xmlsToPlainText(querySelector(root, xml => xml.tag === 'compoundname').childs ?? [])
    const defs = querySelectorsAll(root, x => x.tag === 'memberdef' && x.attrs.prot === 'public')

    // @ts-ignore
    return [className, defs.flatMap(def => {
        const nameElem = querySelector(def, xml => xml.tag === 'name')
        const name = xmlToPlainText(nameElem.childs![0])
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
            const paramType = getPyType(xmlsToPlainText(querySelector(paramElem, xml => xml.tag === 'type').childs!))
            const paramName = getPyType(xmlsToPlainText(querySelector(paramElem, xml => xml.tag === 'declname').childs!))
            let defval: any = undefined
            for (const valElem of querySelectorsAll(paramElem, xml => xml.tag === 'defval')) {
                const elem = xmlsToPlainText(valElem.childs!)
                if (+elem === 0 && paramType !== 'int' && paramType !== 'float') {
                    defval = null
                } else {
                    defval = elem
                }
            }
            params.push([paramType, paramName, getPyValue(defval)])
        }

        if (kind === 'slot' || kind === 'function') {
            const retTypeElem = querySelector(def, xml => xml.tag === 'type' && xml.parent?.tag === 'memberdef')
            const retType = getPyType((retTypeElem.childs && xmlsToPlainText(retTypeElem.childs)) || name)

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
        .replace('QString', 'str')
        .replace('QMap', 'dict')
        .replace('QList', 'List')
        .replace('qreal', 'float')
        .replace('QVector', 'List')
        .replace('double', 'float')
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

function toPythonDef(member: ClassMember): string[] {
`
def function_name(parameters):
"""
Description of the function.

# Parameters

- id : \`int\` 

    Description of parameter1.
- option : \`dict\` 

    Description of parameter2.
# Returns
\`type\`
    Description of the return value.
"""
    # Function code
`
    const args = member.params.map(([type, name, v]) => `${name}: ${type}${v ? ` = ${v}` : ''}`)
    if (member.type === 'constructor_') {
        const res = [
            `def __init__(self${args.length === 0 ? '' : `, ${args}`}) -> None:`,
            '    ...',
        ]
    }

}

; (async () => {
    // const xml = await toXML(
    //     `
    //     <ref>
    //     <ref>QList&lt; <ref refid="class_node" kindref="compound">Node</ref> * &gt;</ref>
    //     </ref>
    //     `

    // )
    // console.log(xmlToString(xml))

    for (const xmlPath of xmlPaths) {
        const xml = await toXML(fs.readFileSync(xmlPath, 'utf-8'))
        const [className, defs] = extractDefs(xml)
        const count = defs.reduce((acc, x) => {
            if (!acc[x.type]) {
                acc[x.type] = 0
            }
            acc[x.type] += 1
            return acc
        }, {} as Record<string, number>)

        console.log(className, count)
    }
    // console.log(JSON.stringify(querySelectorsAll(xml, x => x.tag === 'memberdef' && x.attrs?.kind === 'function')[0], null, 4))
})();;