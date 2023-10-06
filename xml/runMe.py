#!/usr/bin/env python3

from glob import glob
import os
import xml.etree.ElementTree as ET

XML_PATH = '/Users/yuuki/aa_code/libkis/xml'
RESULT_PATH = '/Users/yuuki/code/pyqt_learn/test'

# =====================================

os.chdir(XML_PATH)
os.makedirs(RESULT_PATH, exist_ok=True)

# convert doxygen xml element to html string for python comment

def convertXmlFragment(component: ET.Element) -> str:
    return ET.tostring(component, encoding='unicode', method='text').replace("\n\n", "\n").strip()


def toPlainText(component: ET.Element) -> str:
    return ET.tostring(component, encoding='unicode', method='text').replace("\n\n", "\n").strip()


def typeReplace(str: str) -> str:
    str = str.replace('*', '').replace('&', '').replace('const', '').replace('QStringList', 'list[str]').replace(
        '<', '[').replace('>', ']').replace('QString', 'str').replace('QMap', 'dict').replace('QList', 'list').replace('qreal', 'float').replace('QVector', 'list').replace('double', 'float').strip()
    return str


def readClassComponent(classComponent: ET.Element) -> dict:
    className = classComponent.find('./compoundname').text
    superClass = classComponent.find(
        './basecompoundref').text if classComponent.find('./basecompoundref') is not None else None
    if str(superClass).strip().startswith('Kis') or str(superClass).strip().startswith('Ko'): 
        superClass = None
    classComment = convertXmlFragment(classComponent.find(
        './briefdescription')) + convertXmlFragment(classComponent.find('./detaileddescription'))

    slots = classComponent.findall(".//memberdef[@kind='slot']")
    fns = classComponent.findall(".//memberdef[@kind='function']")
    if fns is None:
        fns = []
    if slots is not None:
        fns.extend(slots)

    funDefs = []
    for funDef in fns:
        if funDef.attrib['prot'] != 'public':
            continue
        funName = funDef.find('./name').text
        if 'operator' in funName or '~' in funName or 'Q_' in funName:
            continue
        retType = typeReplace(toPlainText(funDef.find('./type')))
        isConstructor = funName == className
        isStatic = funDef.attrib['static'] == 'yes'
        params = []
        for paramElem in funDef.findall('.//param'):
            paramType = typeReplace(toPlainText(paramElem.find('./type')))
            paramName = paramElem.find('./declname').text
            paramDefault = None
            if paramElem.find('./defval') is not None:
                paramDefault = paramElem.find('./defval').text
                paramDefault = paramDefault.replace('QString()', "''").replace('QString', '').replace('(', '').replace(')', '').replace('true', 'True').replace('false', 'False')
            params.append(
                {'paramName': paramName, 'paramType': paramType, 'paramDefault': paramDefault})
        
        haveCannotFetchType = False
        for param in params:
            if haveCannotFetchType: break
            haveCannotFetchType = str(param['paramType']).startswith('Kis') or str(param['paramType']).startswith('Ko')

        if haveCannotFetchType:
            continue

        funComment = convertXmlFragment(funDef.find(
            './briefdescription')) + convertXmlFragment(funDef.find('./detaileddescription'))
        funDefs.append({'funName': funName, 'retType': retType, 'isConstructor': isConstructor,
                       'isStatic': isStatic, 'funComment': funComment, 'params': params})
    return {
        'className': className, 'superClass': superClass, 'classComment': classComment, 'funDefs': funDefs
    }


def convertToPythonDef(classMeta: dict) -> str:

    className = classMeta['className']
    superClass = classMeta['superClass']
    classComment = classMeta['classComment']
    funDefs = classMeta['funDefs']

    def funStr(funDef: dict) -> str:
        funName = funDef['funName']
        retType = funDef['retType']
        isConstructor = funDef['isConstructor']
        isStatic = funDef['isStatic']
        funComment = funDef['funComment']
        params = funDef['params']

        def paramStr(paramDef: dict) -> str:
            paramName = paramDef['paramName'].strip()
            paramType = paramDef['paramType'].strip().replace('DockWidgetFactoryBase', 'DockWidgetFactoryBase')
            paramDefault = paramDef['paramDefault']
            if paramType == 'QObject' and paramDefault == '0':
                paramDefault = 'None'
            return f'{paramName}: {paramType}{f" = {paramDefault}" if paramDefault is not None else ""}'

        return "\n".join(map(lambda x: '    ' + x, filter(lambda x: x is not None, [
            '@staticmethod' if isStatic else None,
            ' '.join(filter(lambda x: x is not None, [
                'def',
                '__init__' if isConstructor else funName,
                '(' if isStatic else '(self' + (', ' if len(params) != 0 else ''),
                ', '.join(map(paramStr, params)),
                ')',
                f' -> "{retType}"' if retType != 'void' and retType != '' else '',
                ':',
            ])),
            '    """',
            funComment,
            '    """',
            '    pass'
        ])))

    res = f'''
class {className}{"(Protocol)" if superClass is None else f"({superClass}, Protocol)"}:
    """
    {classComment}
    """
    '''.strip()
    res += '\n' + '\n'.join(map(funStr, funDefs))
    return res
    # print(res)

importStr = """
from typing import Protocol
from PyQt5.QtCore import QObject, QUuid, QByteArray, QRect, QVariant, QPointF, QRectF
from PyQt5.QtGui import QColor, QImage, QTransform, QIcon
from PyQt5.QtWidgets import QDockWidget, QMainWindow, QWidget, QAction
""".strip()

res = ""
classMetaList = []
for file in glob("class_*.xml"):
    tree = ET.parse(file)
    root = tree.getroot()
    classMetaList.extend(filter(lambda x: x is not None, map(readClassComponent, root.findall(".//compounddef[@kind='class']"))))

for classMeta in classMetaList:
    className = classMeta['className']
    print(className)
    resultStr = importStr + "\n" + "\n".join([f"from {i['className']} import {i['className']}" for i in classMetaList if i['className'] != className]) + "\n" + convertToPythonDef(classMeta)
    with open(os.path.join(RESULT_PATH, f'{className}.py'), 'w') as f:
        f.write(resultStr)

with open(os.path.join(RESULT_PATH, '__init__.py'), 'w') as f:
    f.write('\n'.join([f"from {i['className']} import {i['className']}" for i in classMetaList]))