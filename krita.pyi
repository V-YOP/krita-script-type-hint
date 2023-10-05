from typing import Protocol, List
from PyQt5.QtCore import QObject, QUuid, QByteArray, QRect, QVariant, QPointF, QRectF, QPoint
from PyQt5.QtGui import QColor, QImage, QTransform, QIcon
from PyQt5.QtWidgets import QDockWidget, QMainWindow, QWidget, QAction

# TODO an enum in /libs/flake/KoDockFactoryBase.h
class Shape(QObject):
    """
    The Shape class The shape class is a wrapper around Krita's vector objects.Some example code to parse through interesting information in a given vector layer with shapes. importsys
fromkritaimport*
doc=Application.activeDocument()
root=doc.rootNode()
forlayerinroot.childNodes():
print(str(layer.type())+""+str(layer.name()))
if(str(layer.type())=="vectorlayer"):
forshapeinlayer.shapes():
print(shape.name())
print(shape.toSvg())
    """
    def name (self  )  -> "str" :
        """
    namethe name of the shape
        """
        pass
    def setName (self,  name: "str" )  :
        """
    setNamename

which name the shape should have.
        """
        pass
    def type (self  )  -> "str" :
        """
    typethe type of shape.
        """
        pass
    def zIndex (self  )  -> "int" :
        """
    zIndexthe zindex of the shape.
        """
        pass
    def setZIndex (self,  zindex: "int" )  :
        """
    setZIndexzindex

set the shape zindex value.
        """
        pass
    def selectable (self  )  -> "bool" :
        """
    selectablewhether the shape is user selectable.
        """
        pass
    def setSelectable (self,  selectable: "bool" )  :
        """
    setSelectableselectable

whether the shape should be user selectable.
        """
        pass
    def geometryProtected (self  )  -> "bool" :
        """
    geometryProtectedwhether the shape is protected from user changing the shape geometry.
        """
        pass
    def setGeometryProtected (self,  protect: "bool" )  :
        """
    setGeometryProtectedprotect

whether the shape should be geometry protected from the user.
        """
        pass
    def visible (self  )  -> "bool" :
        """
    visiblewhether the shape is visible.
        """
        pass
    def setVisible (self,  visible: "bool" )  :
        """
    setVisiblevisible

whether the shape should be visible.
        """
        pass
    def boundingBox (self  )  -> "QRectF" :
        """
    boundingBox the bounding box of the shape in pointsRectF containing the bounding box.
        """
        pass
    def position (self  )  -> "QPointF" :
        """
    position the position of the shape in points.the position of the shape in points.
        """
        pass
    def setPosition (self,  point: "QPointF" )  :
        """
    setPosition set the position of the shape.point

the new position in points
        """
        pass
    def transformation (self  )  -> "QTransform" :
        """
    transformation the 2D transformation matrix of the shape.the 2D transformation matrix.
        """
        pass
    def setTransformation (self,  matrix: "QTransform" )  :
        """
    setTransformation set the 2D transformation matrix of the shape.matrix

the new 2D transformation matrix.
        """
        pass
    def absoluteTransformation (self  )  -> "QTransform" :
        """
    transformation the 2D transformation matrix of the shape including all grandparent transforms.the 2D transformation matrix.
        """
        pass
    def remove (self  )  -> "bool" :
        """
    remove delete the shape.
        """
        pass
    def update (self  )  :
        """
    update queue the shape update.
        """
        pass
    def updateAbsolute (self,  box: "QRectF" )  :
        """
    updateAbsolute queue the shape update in the specified rectangle.box

the RectF rectangle to update.
        """
        pass
    def toSvg (self,  prependStyles: "bool" = False, stripTextMode: "bool" = True )  -> "str" :
        """
    toSvg convert the shape to svg, will not include style definitions.prependStyles

prepend the style data. Default: false 


stripTextMode

enable strip text mode. Default: true 

the svg in a string.
        """
        pass
    def select (self  )  :
        """
    select selects the shape.
        """
        pass
    def deselect (self  )  :
        """
    deselect deselects the shape.
        """
        pass
    def isSelected (self  )  -> "bool" :
        """
    isSelectedwhether the shape is selected.
        """
        pass
    def parentShape (self  )  -> "Shape" :
        """
    parentShapethe parent GroupShape of the current shape.
        """
        pass
class Node(QObject):
    """
    Node represents a layer or mask in a Krita image's Node hierarchy. Group layers can contain other layers and masks; layers can contain masks.
    """
    def clone (self  )  -> "Node" :
        """
    clone clone the current node. The node is not associated with any image.
        """
        pass
    def alphaLocked (self  )  -> "bool" :
        """
    alphaLocked checks whether the node is a paint layer and returns whether it is alpha lockedwhether the paint layer is alpha locked, or false if the node is not a paint layer
        """
        pass
    def setAlphaLocked (self,  value: "bool" )  :
        """
    setAlphaLocked set the layer to value if the node is paint layer.
        """
        pass
    def blendingMode (self  )  -> "str" :
        """
    the blending mode of the layer. The values of the blending modes are defined in 
KoCompositeOpRegistry.h
        """
        pass
    def setBlendingMode (self,  value: "str" )  :
        """
    setBlendingMode set the blending mode of the node to the given valuevalue

one of the string values from 

KoCompositeOpRegistry.h
        """
        pass
    def channels (self  )  -> "List[ Channel  ]" :
        """
    channels creates a list of Channel objects that can be used individually to show or hide certain channels, and to retrieve the contents of each channel in a node separately.Only layers have channels, masks do not, and calling channels on a Node that is a mask will return an empty list.
the list of channels ordered in by position of the channels in pixel position
        """
        pass
    def childNodes (self  )  -> "List[ Node  ]" :
        """
    childNodesreturns a list of child nodes of the current node. The nodes are ordered from the bottommost up. The function is not recursive.
        """
        pass
    def findChildNodes (self,  name: "str" = '', recursive: "bool" = False, partialMatch: "bool" = False, type: "str" = '', colorLabelIndex: "int" = 0 )  -> "List[ Node  ]" :
        """
    findChildNodesname

name of the child node to search for. Leaving this blank will return all nodes. 


recursive

whether or not to search recursively. Defaults to false. 


partialMatch

return if the name partially contains the string (case insensitive). Defaults to false. 


type

filter returned nodes based on type 


colorLabelIndex

filter returned nodes based on color label index 

returns a list of child nodes and grand child nodes of the current node that match the search criteria.
        """
        pass
    def addChildNode (self,  child: "Node", above: "Node" )  -> "bool" :
        """
    addChildNode adds the given node in the list of children.child

the node to be added 


above

the node above which this node will be placed 

false if adding the node failed
        """
        pass
    def removeChildNode (self,  child: "Node" )  -> "bool" :
        """
    removeChildNode removes the given node from the list of children.child

the node to be removed
        """
        pass
    def setChildNodes (self,  nodes: "List[ Node  ]" )  :
        """
    setChildNodes this replaces the existing set of child nodes with the new set.nodes

The list of nodes that will become children, bottom-up  the first node, is the bottom-most node in the stack.
        """
        pass
    def colorDepth (self  )  -> "str" :
        """
    colorDepth A string describing the color depth of the image: 
U8: unsigned 8 bits integer, the most common type 

U16: unsigned 16 bits integer 

F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 

F32: 32 bits floating point 

the color depth.
        """
        pass
    def colorModel (self  )  -> "str" :
        """
    colorModel retrieve the current color model of this document:A: Alpha mask 

RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 

XYZA: XYZ with alpha channel 

LABA: LAB with alpha channel 

CMYKA: CMYK with alpha channel 

GRAYA: Gray with alpha channel 

YCbCrA: YCbCr with alpha channel 

the internal color model string.
        """
        pass
    def colorProfile (self  )  -> "str" :
        """
    the name of the current color profile
        """
        pass
    def setColorProfile (self,  colorProfile: "str" )  -> "bool" :
        """
    setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is not converted.colorProfile



if assigning the color profile worked
        """
        pass
    def setColorSpace (self,  colorModel: "str", colorDepth: "str", colorProfile: "str" )  -> "bool" :
        """
    setColorSpace convert the node to the given colorspacecolorModel

A string describing the color model of the node: 
A: Alpha mask 

RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 

XYZA: XYZ with alpha channel 

LABA: LAB with alpha channel 

CMYKA: CMYK with alpha channel 

GRAYA: Gray with alpha channel 

YCbCrA: YCbCr with alpha channel 



colorDepth

A string describing the color depth of the image: 
U8: unsigned 8 bits integer, the most common type 

U16: unsigned 16 bits integer 

F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 

F32: 32 bits floating point 



colorProfile

a valid color profile for this color model and color depth combination.
        """
        pass
    def animated (self  )  -> "bool" :
        """
    Krita layers can be animated, i.e., have frames.return true if the layer has frames. Currently, the scripting framework does not give access to the animation features.
        """
        pass
    def enableAnimation (self  )  :
        """
    enableAnimation make the current layer animated, so it can have frames.
        """
        pass
    def setPinnedToTimeline (self,  pinned: "bool" )  :
        """
    Sets whether or not node should be pinned to the Timeline Docker, regardless of selection activity.
        """
        pass
    def isPinnedToTimeline (self  )  -> "bool" :
        """
    Returns true if node is pinned to the Timeline Docker or false if it is not.
        """
        pass
    def setCollapsed (self,  collapsed: "bool" )  :
        """
    Sets the state of the node to the value of
collapsed
        """
        pass
    def collapsed (self  )  -> "bool" :
        """
    returns the collapsed state of this node
        """
        pass
    def colorLabel (self  )  -> "int" :
        """
    Sets a color label index associated to the layer. The actual color of the label and the number of available colors is defined by Krita GUI configuration.
        """
        pass
    def setColorLabel (self,  index: "int" )  :
        """
    setColorLabel sets a color label index associated to the layer. The actual color of the label and the number of available colors is defined by Krita GUI configuration.index

an integer corresponding to the set of available color labels.
        """
        pass
    def inheritAlpha (self  )  -> "bool" :
        """
    inheritAlpha checks whether this node has the inherits alpha flag settrue if the Inherit Alpha is set
        """
        pass
    def setInheritAlpha (self,  value: "bool" )  :
        """
    set the Inherit Alpha flag to the given value
        """
        pass
    def locked (self  )  -> "bool" :
        """
    locked checks whether the Node is locked. A locked node cannot be changed.true if the Node is locked, false if it hasn't been locked.
        """
        pass
    def setLocked (self,  value: "bool" )  :
        """
    set the Locked flag to the give value
        """
        pass
    def hasExtents (self  )  -> "bool" :
        """
    does the node have any content in it?if node has any content in it
        """
        pass
    def name (self  )  -> "str" :
        """
    the user-visible name of this node.
        """
        pass
    def setName (self,  name: "str" )  :
        """
    rename the Node to the given name
        """
        pass
    def opacity (self  )  -> "int" :
        """
    return the opacity of the Node. The opacity is a value between 0 and 255.
        """
        pass
    def setOpacity (self,  value: "int" )  :
        """
    set the opacity of the Node to the given value. The opacity is a value between 0 and 255.
        """
        pass
    def parentNode (self  )  -> "Node" :
        """
    return the Node that is the parent of the current Node, or 0 if this is the root Node.
        """
        pass
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.The type of the node. Valid types are: 
paintlayer 

grouplayer 

filelayer 

filterlayer 

filllayer 

clonelayer 

vectorlayer 

transparencymask 

filtermask 

transformmask 

selectionmask 

colorizemask 


If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def icon (self  )  -> "QIcon" :
        """
    iconthe icon associated with the layer.
        """
        pass
    def visible (self  )  -> "bool" :
        """
    Check whether the current Node is visible in the layer stack
        """
        pass
    def hasKeyframeAtTime (self,  frameNumber: "int" )  -> "bool" :
        """
    Check to see if frame number on layer is a keyframe
        """
        pass
    def setVisible (self,  visible: "bool" )  :
        """
    Set the visibility of the current node to
visible
        """
        pass
    def pixelData (self,  x: "int", y: "int", w: "int", h: "int" )  -> "QByteArray" :
        """
    pixelData reads the given rectangle from the Node's paintable pixels, if those exist, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float.
You can read outside the node boundaries; those pixels will be transparent black.
The order of channels is:

Integer RGBA: Blue, Green, Red, Alpha 

Float RGBA: Red, Green, Blue, Alpha 

GrayA: Gray, Alpha 

Selection: selectedness 

LabA: L, a, b, Alpha 

CMYKA: Cyan, Magenta, Yellow, Key, Alpha 

XYZA: X, Y, Z, A 

YCbCrA: Y, Cb, Cr, Alpha 

The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
If you read the pixeldata of a mask, a filter or generator layer, you get the selection bytes, which is one channel with values in the range from 0..255.
If you want to change the pixels of a node you can write the pixels back after manipulation with setPixelData(). This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.

x

x position from where to start reading 


y

y position from where to start reading 


w

row length to read 


h

number of rows to read 

a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def pixelDataAtTime (self,  x: "int", y: "int", w: "int", h: "int", time: "int" )  -> "QByteArray" :
        """
    pixelDataAtTime a basic function to get pixeldata from an animated node at a given time.x

the position from the left to start reading. 


y

the position from the top to start reader 


w

the row length to read 


h

the number of rows to read 


time

the frame number 

a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def projectionPixelData (self,  x: "int", y: "int", w: "int", h: "int" )  -> "QByteArray" :
        """
    projectionPixelData reads the given rectangle from the Node's projection (that is, what the node looks like after all sub-Nodes (like layers in a group or masks on a layer) have been applied, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float.
You can read outside the node boundaries; those pixels will be transparent black.
The order of channels is:

Integer RGBA: Blue, Green, Red, Alpha 

Float RGBA: Red, Green, Blue, Alpha 

GrayA: Gray, Alpha 

Selection: selectedness 

LabA: L, a, b, Alpha 

CMYKA: Cyan, Magenta, Yellow, Key, Alpha 

XYZA: X, Y, Z, A 

YCbCrA: Y, Cb, Cr, Alpha 

The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
If you read the projection of a mask, you get the selection bytes, which is one channel with values in the range from 0..255.
If you want to change the pixels of a node you can write the pixels back after manipulation with setPixelData(). This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.

x

x position from where to start reading 


y

y position from where to start reading 


w

row length to read 


h

number of rows to read 

a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def setPixelData (self,  value: "QByteArray", x: "int", y: "int", w: "int", h: "int" )  -> "bool" :
        """
    setPixelData writes the given bytes, of which there must be enough, into the Node, if the Node has writable pixel data:paint layer: the layer's original pixels are overwritten 

filter layer, generator layer, any mask: the embedded selection's pixels are overwritten. Note: for these 

File layers, Group layers, Clone layers cannot be written to. Calling setPixelData on those layer types will silently do nothing.

value

the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.


x

the x position to start writing from 


y

the y position to start writing from 


w

the width of each row 


h

the number of rows to write 

true if writing the pixeldata worked
        """
        pass
    def bounds (self  )  -> "QRect" :
        """
    bounds return the exact bounds of the node's paint devicethe bounds, or an empty QRect if the node has no paint device or is empty.
        """
        pass
    def move (self,  x: "int", y: "int" )  :
        """
    move the pixels to the given x, y location in the image coordinate space.
        """
        pass
    def position (self  )  -> "QPoint" :
        """
    position returns the position of the paint device of this node. The position is always 0,0 unless the layer has been moved. If you want to know the topleft position of the rectangle around the actual non-transparent pixels in the node, use bounds().the top-left position of the node
        """
        pass
    def remove (self  )  -> "bool" :
        """
    remove removes this node from its parent image.
        """
        pass
    def duplicate (self  )  -> "Node" :
        """
    duplicate returns a full copy of the current node. The node is not inserted in the graphica valid Node object or 0 if the node couldn't be duplicated.
        """
        pass
    def save (self,  filename: "str", xRes: "float", yRes: "float", exportConfiguration: "InfoObject", exportRect: "QRect" = QRect )  -> "bool" :
        """
    save exports the given node with this filename. The extension of the filename determines the filetype.filename

the filename including extension 


xRes

the horizontal resolution in pixels per pt (there are 72 pts in an inch) 


yRes

the horizontal resolution in pixels per pt (there are 72 pts in an inch) 


exportConfiguration

a configuration object appropriate to the file format. 


exportRect

the export bounds for saving a node as a QRect If exportRect is empty, then save exactBounds() of the node. If you'd like to save the image- aligned area of the node, just pass image->bounds() there. See Document->exportImage for InfoObject details. 

true if saving succeeded, false if it failed.
        """
        pass
    def mergeDown (self  )  -> "Node" :
        """
    mergeDown merges the given node with the first visible node underneath this node in the layerstack. This will drop all per-layer metadata.
        """
        pass
    def scaleNode (self,  origin: "QPointF", width: "int", height: "int", strategy: "str" )  :
        """
    scaleNodeorigin

the origin point 


width

the width 


height

the height 


strategy

the scaling strategy. There's several ones amongst these that aren't available in the regular UI. 
Hermite 

Bicubic - Adds pixels using the color of surrounding pixels. Produces smoother tonal gradations than Bilinear. 

Box - Replicate pixels in the image. Preserves all the original detail, but can produce jagged effects. 

Bilinear - Adds pixels averaging the color values of surrounding pixels. Produces medium quality results when the image is scaled from half to two times the original size. 

Bell 

BSpline 

Lanczos3 - Offers similar results than Bicubic, but maybe a little bit sharper. Can produce light and dark halos along strong edges. 

Mitchell
        """
        pass
    def rotateNode (self,  radians: "float" )  :
        """
    rotateNode rotate this layer by the given radians.radians

amount the layer should be rotated in, in radians.
        """
        pass
    def cropNode (self,  x: "int", y: "int", w: "int", h: "int" )  :
        """
    cropNode crop this layer.x

the left edge of the cropping rectangle. 


y

the top edge of the cropping rectangle 


w

the right edge of the cropping rectangle 


h

the bottom edge of the cropping rectangle
        """
        pass
    def shearNode (self,  angleX: "float", angleY: "float" )  :
        """
    shearNode perform a shear operation on this node.angleX

the X-angle in degrees to shear by 


angleY

the Y-angle in degrees to shear by
        """
        pass
    def thumbnail (self,  w: "int", h: "int" )  -> "QImage" :
        """
    thumbnail create a thumbnail of the given dimensions. The thumbnail is sized according to the layer dimensions, not the image dimensions. If the requested size is too big a null QImage is created. If the current node cannot generate a thumbnail, a transparent QImage of the requested size is generated.a QImage representing the layer contents.
        """
        pass
    def layerStyleToAsl (self  )  -> "str" :
        """
    layerStyleToAsl retrieve the current layer's style in ASL format.a QString in ASL format representing the layer style.
        """
        pass
    def setLayerStyleFromAsl (self,  asl: "str" )  -> "bool" :
        """
    setLayerStyleFromAsl set a new layer style for this node.aslContent

a string formatted in ASL format containing the layer style 

true if layer style was set, false if failed.
        """
        pass
    def index (self  )  -> "int" :
        """
    index the index of the node inside the parentan integer representing the node's index inside the parent
        """
        pass
    def uniqueId (self  )  -> "QUuid" :
        """
    uniqueId uniqueId of the nodea QUuid representing a unique id to identify the node
        """
        pass
class Document(QObject):
    """
    The Document class encapsulates a Krita Document/Image. A Krita document is an Image with a filename.
      Libkis does not differentiate between a document and an image, like Krita does internally.
    """
    def horizontalGuides (self  )  -> "List[ float ]" :
        """
    horizontalGuides The horizontal guides.a list of the horizontal positions of guides.
        """
        pass
    def verticalGuides (self  )  -> "List[ float ]" :
        """
    verticalGuides The vertical guide lines.a list of vertical guides.
        """
        pass
    def guidesVisible (self  )  -> "bool" :
        """
    guidesVisible Returns guide visibility.whether the guides are visible.
        """
        pass
    def guidesLocked (self  )  -> "bool" :
        """
    guidesLocked Returns guide lockedness.whether the guides are locked.
        """
        pass
    def clone (self  )  -> "Document" :
        """
    clone create a shallow clone of this document.a new Document that should
          be identical to this one in every respect.
        """
        pass
    def batchmode (self  )  -> "bool" :
        """
    Batchmode means that no actions on the document should show dialogs or popups. 
              true if the document is in batchmode.
        """
        pass
    def setBatchmode (self,  value: "bool" )  :
        """
    Set batchmode to value. If batchmode is true, then
          there should be no popups or dialogs shown to the user.
        """
        pass
    def activeNode (self  )  -> "Node" :
        """
    activeNode retrieve the node that is currently active in the currently active windowthe active node. If there is no active window, the first child node is returned.
        """
        pass
    def setActiveNode (self,  value: "Node" )  :
        """
    setActiveNode make the given node active in the currently active view and windowvalue
                
                
                  the node to make active.
        """
        pass
    def topLevelNodes (self  )  -> "List[ Node  ]" :
        """
    toplevelNodes return a list with all top level nodes in the image graph
        """
        pass
    def nodeByName (self,  name: "str" )  -> "Node" :
        """
    nodeByName searches the node tree for a node with the given name and returns itname
                
                
                  the name of the node 
                
              
            
              the first node with the given name or 0 if no node is found
        """
        pass
    def nodeByUniqueID (self,  id: "QUuid" )  -> "Node" :
        """
    nodeByUniqueID searches the node tree for a node with the given name and returns it.uuid
                
                
                  the unique id of the node 
                
              
            
              the node with the given unique id, or 0 if no node is found.
        """
        pass
    def colorDepth (self  )  -> "str" :
        """
    colorDepth A string describing the color depth of the image: 
              
                U8: unsigned 8 bits integer, the most common type 
              
              
                U16: unsigned 16 bits integer 
              
              
                F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 
              
              
                F32: 32 bits floating point 
              
            
              the color depth.
        """
        pass
    def colorModel (self  )  -> "str" :
        """
    colorModel retrieve the current color model of this document:A: Alpha mask 
              
              
                RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 
              
              
                XYZA: XYZ with alpha channel 
              
              
                LABA: LAB with alpha channel 
              
              
                CMYKA: CMYK with alpha channel 
              
              
                GRAYA: Gray with alpha channel 
              
              
                YCbCrA: YCbCr with alpha channel 
              
            
              the internal color model string.
        """
        pass
    def colorProfile (self  )  -> "str" :
        """
    the name of the current color profile
        """
        pass
    def setColorProfile (self,  colorProfile: "str" )  -> "bool" :
        """
    setColorProfile set the color profile of the image to the given profile. The profile
          has to be registered with krita and be compatible with the current color model and depth;
          the image data is not converted.colorProfile
                
                
                  
                
              
            
              false if the colorProfile name does not correspond to to a registered profile or
          if assigning the profile failed.
        """
        pass
    def setColorSpace (self,  colorModel: "str", colorDepth: "str", colorProfile: "str" )  -> "bool" :
        """
    setColorSpace convert the nodes and the image to the given colorspace. The
          conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as
          flags and no blackpoint compensation.colorModel
                
                
                  A string describing the color model of the image: 
                      
                        A: Alpha mask 
                      
                      
                        RGBA: RGB with alpha channel (The actual order of channels is most
          often BGR!) 
                      
                      
                        XYZA: XYZ with alpha channel 
                      
                      
                        LABA: LAB with alpha channel 
                      
                      
                        CMYKA: CMYK with alpha channel 
                      
                      
                        GRAYA: Gray with alpha channel 
                      
                      
                        YCbCrA: YCbCr with alpha channel 
                      
                    
                  
                
              
              
                
                  colorDepth
                
                
                  A string describing the color depth of the image: 
                      
                        U8: unsigned 8 bits integer, the most common type 
                      
                      
                        U16: unsigned 16 bits integer 
                      
                      
                        F16: half, 16 bits floating point. Only available if Krita was built with
          OpenEXR 
                      
                      
                        F32: 32 bits floating point 
                      
                    
                  
                
              
              
                
                  colorProfile
                
                
                  a valid color profile for this color model and color depth combination. 
                
              
            
              false the combination of these arguments does not correspond to a colorspace.
        """
        pass
    def backgroundColor (self  )  -> "QColor" :
        """
    backgroundColor returns the current background color of the document. The color will
          also include the opacity.QColor
        """
        pass
    def setBackgroundColor (self,  color: "QColor" )  -> "bool" :
        """
    setBackgroundColor sets the background color of the document. It will trigger a
          projection update.color
                
                
                  A QColor. The color will be converted from sRGB. 
                
              
            
              bool
        """
        pass
    def documentInfo (self  )  -> "str" :
        """
    documentInfo creates and XML document representing document and author information.a string containing a valid XML document with the right information about the
          document and author. The DTD can be found here:
            
          https://phabricator.kde.org/source/krita/browse/master/krita/dtd/
          <?xmlversion="1.0"
          encoding="UTF-8"
          ?>
<!DOCTYPE
          document-infoPUBLIC'-//KDE//DTD
          document-info1.1//EN'
          'http://www.calligra.org/DTD/document-info-1.1.dtd'
          >
<document-info
          xmlns=
          "http://www.calligra.org/DTD/document-info">
          <about>
          <title>MyDocument</title>
          <description></description>
          <subject></subject>
          <abstract><![CDATA[]]></abstract>
          <keyword></keyword>
          <initial-creator>Unknown</initial-creator>
          <editing-cycles>1</editing-cycles>
          <editing-time>35</editing-time>
          <date>2017-02-27T20:15:09</date>
          <creation-date>2017-02-27T20:14:33</creation-date>
          <language></language>
          </about>
          <author>
          <full-name
          >BoudewijnRempt</full-name
          >
          <initial></initial>
          <author-title></author-title>
          <email></email>
          <telephone></telephone>
          <telephone-work></telephone-work>
          <fax></fax>
          <country></country>
          <postal-code></postal-code>
          <city></city>
          <street></street>
          <position></position>
          <company></company>
          </author>
          </document-info>
        """
        pass
    def setDocumentInfo (self,  document: "str" )  :
        """
    setDocumentInfo set the Document
          information to the information contained in documentdocument
                
                
                  A string containing a valid XML document that conforms to the document-info
          DTD that can be found here:
                
              
            
          https://phabricator.kde.org/source/krita/browse/master/krita/dtd/
        """
        pass
    def fileName (self  )  -> "str" :
        """
    the full path to the document, if it has been set.
        """
        pass
    def setFileName (self,  value: "str" )  :
        """
    setFileName set the full path of the document tovalue
        """
        pass
    def height (self  )  -> "int" :
        """
    the height of the image in pixels
        """
        pass
    def setHeight (self,  value: "int" )  :
        """
    setHeight resize the document tovalue
                
                
                  height. This is a canvas resize, not a scale.
        """
        pass
    def name (self  )  -> "str" :
        """
    the name of the document. This is the title field in the 
          documentInfo
        """
        pass
    def setName (self,  value: "str" )  :
        """
    setName sets the name of the document to value.
          This is the title field in the 
          documentInfo
        """
        pass
    def resolution (self  )  -> "int" :
        """
    the resolution in pixels per inch
        """
        pass
    def setResolution (self,  value: "int" )  :
        """
    setResolution set the resolution of the image; this does not scale the imagevalue
                
                
                  the resolution in pixels per inch
        """
        pass
    def rootNode (self  )  -> "Node" :
        """
    rootNode the root node is the invisible group layer that contains the entire node
          hierarchy.the root of the image
        """
        pass
    def selection (self  )  -> "Selection" :
        """
    selection Create a Selection
          object around the global selection, if there is one.the global selection or None if there is no global selection.
        """
        pass
    def setSelection (self,  value: "Selection" )  :
        """
    setSelection set or replace the global selectionvalue
                
                
                  a valid selection object.
        """
        pass
    def width (self  )  -> "int" :
        """
    the width of the image in pixels.
        """
        pass
    def setWidth (self,  value: "int" )  :
        """
    setWidth resize the document tovalue
                
                
                  width. This is a canvas resize, not a scale.
        """
        pass
    def xOffset (self  )  -> "int" :
        """
    the left edge of the canvas in pixels.
        """
        pass
    def setXOffset (self,  x: "int" )  :
        """
    setXOffset sets the left edge of the canvas to x.
        """
        pass
    def yOffset (self  )  -> "int" :
        """
    the top edge of the canvas in pixels.
        """
        pass
    def setYOffset (self,  y: "int" )  :
        """
    setYOffset sets the top edge of the canvas to y.
        """
        pass
    def xRes (self  )  -> "float" :
        """
    xRes the horizontal resolution of the image in pixels per inch
        """
        pass
    def setXRes (self,  xRes: "float" )  :
        """
    setXRes set the horizontal resolution of the image to xRes in pixels per inch
        """
        pass
    def yRes (self  )  -> "float" :
        """
    yRes the vertical resolution of the image in pixels per inch
        """
        pass
    def setYRes (self,  yRes: "float" )  :
        """
    setYRes set the vertical resolution of the image to yRes in pixels per inch
        """
        pass
    def pixelData (self,  x: "int", y: "int", w: "int", h: "int" )  -> "QByteArray" :
        """
    pixelData reads the given rectangle from the image projection and returns it as a
          byte array. The pixel data starts top-left, and is ordered row-first.The byte array can be interpreted as follows: 8 bits images have one byte per
          channel, and as many bytes as there are channels. 16 bits integer images have two bytes
          per channel, representing an unsigned short. 16 bits float images have two bytes per
          channel, representing a half, or 16 bits float. 32 bits float images have four bytes per
          channel, representing a float.
You can read outside the image boundaries;
          those pixels will be transparent black.
The order of channels is:
              
                Integer RGBA: Blue, Green, Red, Alpha 
              
              
                Float RGBA: Red, Green, Blue, Alpha 
              
              
                LabA: L, a, b, Alpha 
              
              
                CMYKA: Cyan, Magenta, Yellow, Key, Alpha 
              
              
                XYZA: X, Y, Z, A 
              
              
                YCbCrA: Y, Cb, Cr, Alpha 
              
            
          
The
          byte array is a copy of the original image data. In Python, you can use bytes, bytearray
          and the struct module to interpret the data and construct, for instance, a Pillow Image
          object.
              
                
                  x
                
                
                  x position from where to start reading 
                
              
              
                
                  y
                
                
                  y position from where to start reading 
                
              
              
                
                  w
                
                
                  row length to read 
                
              
              
                
                  h
                
                
                  number of rows to read 
                
              
            
              a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def close (self  )  -> "bool" :
        """
    close Close the document: remove it from 
          Krita's internal list of documents and close all views. If the document is
          modified, you should save it first. There will be no prompt for saving.After closing the document it becomes invalid.
              true if the document is closed.
        """
        pass
    def crop (self,  x: "int", y: "int", w: "int", h: "int" )  :
        """
    crop the image to rectangle described by x, 
          y, w and hx
                
                
                  x coordinate of the top left corner 
                
              
              
                
                  y
                
                
                  y coordinate of the top left corner 
                
              
              
                
                  w
                
                
                  width 
                
              
              
                
                  h
                
                
                  height
        """
        pass
    def exportImage (self,  filename: "str", exportConfiguration: "InfoObject" )  -> "bool" :
        """
    exportImage export the image, without changing its URL to the given path.filename
                
                
                  the full path to which the image is to be saved 
                
              
              
                
                  exportConfiguration
                
                
                  a configuration object appropriate to the file format. An InfoObject will used to
          that configuration.
                
              
            
          The supported formats have specific configurations that must be used when in batchmode.
          They are described below:
png 
              
                alpha: bool (True or False) 
              
              
                compression: int (1 to 9) 
              
              
                forceSRGB: bool (True or False) 
              
              
                indexed: bool (True or False) 
              
              
                interlaced: bool (True or False) 
              
              
                saveSRGBProfile: bool (True or False) 
              
              
                transparencyFillcolor: rgb (Ex:[255,255,255]) 
              
            
          
          jpeg 
              
                baseline: bool (True or False) 
              
              
                exif: bool (True or False) 
              
              
                filters: bool (['ToolInfo', 'Anonymizer']) 
              
              
                forceSRGB: bool (True or False) 
              
              
                iptc: bool (True or False) 
              
              
                is_sRGB: bool (True or False) 
              
              
                optimize: bool (True or False) 
              
              
                progressive: bool (True or False) 
              
              
                quality: int (0 to 100) 
              
              
                saveProfile: bool (True or False) 
              
              
                smoothing: int (0 to 100) 
              
              
                subsampling: int (0 to 3) 
              
              
                transparencyFillcolor: rgb (Ex:[255,255,255]) 
              
              
                xmp: bool (True or False) 
              
            
              true if the export succeeded, false if it failed.
        """
        pass
    def flatten (self  )  :
        """
    flatten all layers in the image
        """
        pass
    def resizeImage (self,  x: "int", y: "int", w: "int", h: "int" )  :
        """
    resizeImage resizes the canvas to the given left edge, top edge, width and height.
          Note: This doesn't scale, use scale image for that.x
                
                
                  the new left edge 
                
              
              
                
                  y
                
                
                  the new top edge 
                
              
              
                
                  w
                
                
                  the new width 
                
              
              
                
                  h
                
                
                  the new height
        """
        pass
    def scaleImage (self,  w: "int", h: "int", xres: "int", yres: "int", strategy: "str" )  :
        """
    scaleImagew
                
                
                  the new width 
                
              
              
                
                  h
                
                
                  the new height 
                
              
              
                
                  xres
                
                
                  the new xres 
                
              
              
                
                  yres
                
                
                  the new yres 
                
              
              
                
                  strategy
                
                
                  the scaling strategy. There's several ones amongst these that
          aren't available in the regular UI. The list of filters is extensible and can be
          retrieved with Krita::filter 
                      
                        Hermite 
                      
                      
                        Bicubic - Adds pixels using the color of surrounding pixels. Produces
          smoother tonal gradations than Bilinear. 
                      
                      
                        Box - Replicate pixels in the image. Preserves all the original
          detail, but can produce jagged effects. 
                      
                      
                        Bilinear - Adds pixels averaging the color values of surrounding
          pixels. Produces medium quality results when the image is scaled from half to two times
          the original size. 
                      
                      
                        Bell 
                      
                      
                        BSpline 
                      
                      
                        Kanczos3 - Offers similar results than Bicubic, but maybe a little bit
          sharper. Can produce light and dark halos along strong edges. 
                      
                      
                        Mitchell
        """
        pass
    def rotateImage (self,  radians: "float" )  :
        """
    rotateImage Rotate the image by the given radians.radians
                
                
                  the amount you wish to rotate the image in radians
        """
        pass
    def shearImage (self,  angleX: "float", angleY: "float" )  :
        """
    shearImage shear the whole image.angleX
                
                
                  the X-angle in degrees to shear by 
                
              
              
                
                  angleY
                
                
                  the Y-angle in degrees to shear by
        """
        pass
    def save (self  )  -> "bool" :
        """
    save the image to its currently set path. The modified flag of the document will be
          resettrue if saving succeeded, false otherwise.
        """
        pass
    def saveAs (self,  filename: "str" )  -> "bool" :
        """
    saveAs save the document under the filename. The
          document's filename will be reset to filename.filename
                
                
                  the new filename (full path) for the document 
                
              
            
              true if saving succeeded, false otherwise.
        """
        pass
    def createNode (self,  name: "str", nodeType: "str" )  -> "Node" :
        """
    @brief createNode create a new node of the given type. The node is not added
   to the node hierarchy; you need to do that by finding the right parent node,
   getting its list of child nodes and adding the node in the right place, then
   calling Node::SetChildNodes
   @param name The name of the node
   @param nodeType The type of the node. Valid types are:
   <ul>
    <li>paintlayer
    <li>grouplayer
    <li>filelayer
    <li>filterlayer
    <li>filllayer
    <li>clonelayer
    <li>vectorlayer
    <li>transparencymask
    <li>filtermask
    <li>transformmask
    <li>selectionmask
   </ul>
   When relevant, the new Node will have the colorspace of the image by default;
   that can be changed with Node::setColorSpace.
   The settings and selections for relevant layer and mask types can also be set
   after the Node has been created.
 d=
          Application.createDocument(1000,1000,
          "Test",
          "RGBA",
          "U8",
          "",120.0)
          root=d.rootNode();
          print(root.childNodes())
l2
          =d.createNode
          ("layer2","paintLayer")
          print(l2)
          root.addChildNode(l2,None)
          print(root.childNodes())

              the new Node.
        """
        pass
    def createGroupLayer (self,  name: "str" )  -> "GroupLayer" :
        """
    createGroupLayer Returns a grouplayer object. Grouplayers are nodes that can have
          other layers as children and have the passthrough mode.name
                
                
                  the name of the layer. 
                
              
            
              a GroupLayer object.
        """
        pass
    def createFileLayer (self,  name: "str", fileName: "str", scalingMethod: "str", scalingFilter: "str" = "Bicubic" )  -> "FileLayer" :
        """
    createFileLayer returns a layer that shows an external image.name
                
                
                  name of the file layer. 
                
              
              
                
                  fileName
                
                
                  the absolute filename of the file referenced. Symlinks will be resolved. 
                
              
              
                
                  scalingMethod
                
                
                  how the dimensions of the file are interpreted can be either
          "None", "ImageToSize" or "ImageToPPI" 
                
              
              
                
                  scalingFilter
                
                
                  filter used to scale the file can be "Bicubic",
          "Hermite", "NearestNeighbor", "Bilinear", "Bell",
          "BSpline", "Lanczos3", "Mitchell" 
                
              
            
              a FileLayer
        """
        pass
    def createFilterLayer (self,  name: "str", filter: "Filter", selection: "Selection" )  -> "FilterLayer" :
        """
    createFilterLayer creates a filter layer, which is a layer that represents a filter
          applied non-destructively.name
                
                
                  name of the filterLayer 
                
              
              
                
                  filter
                
                
                  the filter that this filter layer will us. 
                
              
              
                
                  selection
                
                
                  the selection. 
                
              
            
              a filter layer object.
        """
        pass
    def createFillLayer (self,  name: "str", generatorName: "str", configuration: "InfoObject", selection: "Selection" )  -> "FillLayer" :
        """
    createFillLayer creates a fill layer object, which is a layername
                
                
                  
                
              
              
                
                  generatorName
                
                
                  - name of the generation filter. 
                
              
              
                
                  configuration
                
                
                  - the configuration for the generation filter. 
                
              
              
                
                  selection
                
                
                  - the selection. 
                
              
            
              a filllayer object.
            
          fromkritaimport
          *
d=
          Krita.instance().activeDocument()
          i=InfoObject();
          i.setProperty("pattern"
          ,"Cross01.pat"
          )
s=Selection();
          s.select(0,0,d.width(),d.height(),255)
          n=d.createFillLayer("test"
          ,"pattern"
          ,i,s)
r=
          d.rootNode();
c=
          r.childNodes();
          r.addChildNode(n,c[0])
          d.refreshProjection()
        """
        pass
    def createCloneLayer (self,  name: "str", source: "Node" )  -> "CloneLayer" :
        """
    createCloneLayername
                
                
                  
                
              
              
                
                  source
        """
        pass
    def createVectorLayer (self,  name: "str" )  -> "VectorLayer" :
        """
    createVectorLayer Creates a vector layer that can contain vector shapes.name
                
                
                  the name of this layer. 
                
              
            
              a VectorLayer.
        """
        pass
    def createFilterMask (self,  name: "str", filter: "Filter", selection: "Selection" )  -> "FilterMask" :
        """
    createFilterMask Creates a filter mask object that much like a filterlayer can apply
          a filter non-destructively.name
                
                
                  the name of the layer. 
                
              
              
                
                  filter
                
                
                  the filter assigned. 
                
              
              
                
                  selection
                
                
                  the selection to be used by the filter mask 
                
              
            
              a FilterMask
        """
        pass
    def createFilterMask (self,  name: "str", filter: "Filter", selection_source: "Node" )  -> "FilterMask" :
        """
    createFilterMask Creates a filter mask object that much like a filterlayer can apply
          a filter non-destructively.name
                
                
                  the name of the layer. 
                
              
              
                
                  filter
                
                
                  the filter assigned. 
                
              
              
                
                  selection_source
                
                
                  a node from which the selection should be initialized 
                
              
            
              a FilterMask
        """
        pass
    def createSelectionMask (self,  name: "str" )  -> "SelectionMask" :
        """
    createSelectionMask Creates a selection mask, which can be used to store selections.name
                
                
                  - the name of the layer. 
                
              
            
              a SelectionMask
        """
        pass
    def createTransparencyMask (self,  name: "str" )  -> "TransparencyMask" :
        """
    createTransparencyMask Creates a transparency mask, which can be used to assign
          transparency to regions.name
                
                
                  - the name of the layer. 
                
              
            
              a TransparencyMask
        """
        pass
    def createTransformMask (self,  name: "str" )  -> "TransformMask" :
        """
    createTransformMask Creates a transform mask, which can be used to apply a
          transformation non-destructively.name
                
                
                  - the name of the layer mask. 
                
              
            
              a TransformMask
        """
        pass
    def createColorizeMask (self,  name: "str" )  -> "ColorizeMask" :
        """
    createColorizeMask Creates a colorize mask, which can be used to color fill via
          keystrokes.name
                
                
                  - the name of the layer. 
                
              
            
              a TransparencyMask
        """
        pass
    def projection (self,  x: "int" = 0, y: "int" = 0, w: "int" = 0, h: "int" = 0 )  -> "QImage" :
        """
    projection creates a QImage from the rendered image or a cutout rectangle.
        """
        pass
    def thumbnail (self,  w: "int", h: "int" )  -> "QImage" :
        """
    thumbnail create a thumbnail of the given dimensions.If the requested size is too big a null QImage is created.
              a QImage representing the layer contents.
        """
        pass
    def lock (self  )  :
        """
    [low-level] Lock the image without waiting for all the internal job queues are
          processed
WARNING: Don't use it unless you really know what you are
          doing! Use barrierLock() instead!
Waits for all the currently running
          internal jobs to complete and locks the image for writing. Please note that this function
          does not wait for all the internal queues to process, so there might be some
          non-finished actions pending. It means that you just postpone these actions until you unlock()
          the image back. Until then, then image might easily be frozen in some inconsistent state.
The
          only sane usage for this function is to lock the image for emergency
          processing, when some internal action or scheduler got hung up, and you just want to fetch
          some data from the image without races.
In all other cases, please use
          barrierLock() instead!
        """
        pass
    def unlock (self  )  :
        """
    Unlocks the image and starts/resumes all the pending internal jobs. If the image has
          been locked for a non-readOnly access, then all the internal caches of the image (e.g.
          lod-planes) are reset and regeneration jobs are scheduled.
        """
        pass
    def waitForDone (self  )  :
        """
    Wait for all the internal image jobs to complete and return without locking the
          image. This function is handy for tests or other synchronous actions, when one needs to
          wait for the result of his actions.
        """
        pass
    def tryBarrierLock (self  )  -> "bool" :
        """
    Tries to lock the image without waiting for the jobs to finish.Same as barrierLock(), but doesn't block execution of the calling thread until
          all the background jobs are finished. Instead, in case of presence of unfinished jobs in
          the queue, it just returns false
              whether the lock has been acquired
        """
        pass
    def refreshProjection (self  )  :
        """
    Starts a synchronous recomposition of the projection: everything will wait until the
          image is fully recomputed.
        """
        pass
    def setHorizontalGuides (self,  lines: "List[ float ]" )  :
        """
    setHorizontalGuides replace all existing horizontal guides with the entries in the
          list.lines
                
                
                  a list of floats containing the new guides.
        """
        pass
    def setVerticalGuides (self,  lines: "List[ float ]" )  :
        """
    setVerticalGuides replace all existing horizontal guides with the entries in the
          list.lines
                
                
                  a list of floats containing the new guides.
        """
        pass
    def setGuidesVisible (self,  visible: "bool" )  :
        """
    setGuidesVisible set guides visible on this document.visible
                
                
                  whether or not the guides are visible.
        """
        pass
    def setGuidesLocked (self,  locked: "bool" )  :
        """
    setGuidesLocked set guides locked on this documentlocked
                
                
                  whether or not to lock the guides on this document.
        """
        pass
    def modified (self  )  -> "bool" :
        """
    modified returns true if the document has unsaved modifications.
        """
        pass
    def setModified (self,  modified: "bool" )  :
        """
    setModified sets the modified status of the documentmodified
                
                
                  if true, the document is considered modified and closing it will ask for
          saving.
        """
        pass
    def bounds (self  )  -> "QRect" :
        """
    bounds return the bounds of the imagethe bounds
        """
        pass
    def importAnimation (self,  files: "List[ str ]", firstFrame: "int", step: "int" )  -> "bool" :
        """
    Import an image sequence of files from a directory. This will grab all images from
          the directory and import them with a potential offset (firstFrame) and step (images on 2s,
          3s, etc)whether the animation import was successful
        """
        pass
    def framesPerSecond (self  )  -> "int" :
        """
    frames per second of documentthe fps of the document
        """
        pass
    def setFramesPerSecond (self,  fps: "int" )  :
        """
    set frames per second of document
        """
        pass
    def setFullClipRangeStartTime (self,  startTime: "int" )  :
        """
    set start time of animation
        """
        pass
    def fullClipRangeStartTime (self  )  -> "int" :
        """
    get the full clip range start timefull clip range start time
        """
        pass
    def setFullClipRangeEndTime (self,  endTime: "int" )  :
        """
    set full clip range end time
        """
        pass
    def fullClipRangeEndTime (self  )  -> "int" :
        """
    get the full clip range end timefull clip range end time
        """
        pass
    def animationLength (self  )  -> "int" :
        """
    get total frame range for animationtotal frame range for animation
        """
        pass
    def setPlayBackRange (self,  start: "int", stop: "int" )  :
        """
    set temporary playback range of document
        """
        pass
    def playBackStartTime (self  )  -> "int" :
        """
    get start time of current playbackstart time of current playback
        """
        pass
    def playBackEndTime (self  )  -> "int" :
        """
    get end time of current playbackend time of current playback
        """
        pass
    def currentTime (self  )  -> "int" :
        """
    get current frame selected of animationcurrent frame selected of animation
        """
        pass
    def setCurrentTime (self,  time: "int" )  :
        """
    set current time of document's animation
        """
        pass
    def annotationTypes (self  )  -> "List[str]" :
        """
    annotationTypes returns the list of annotations present in the document. Each
          annotation type is unique.
        """
        pass
    def annotationDescription (self,  type: "str" )  -> "str" :
        """
    annotationDescription gets the pretty description for the current annotationtype
                
                
                  the type of the annotation 
                
              
            
              a string that can be presented to the user
        """
        pass
    def annotation (self,  type: "str" )  -> "QByteArray" :
        """
    annotation the actual data for the annotation for this type. It's a simple
          QByteArray, what's in it depends on the type of the annotationtype
                
                
                  the type of the annotation 
                
              
            
              a bytearray, possibly empty if this type of annotation doesn't exist
        """
        pass
    def setAnnotation (self,  type: "str", description: "str", annotation: "QByteArray" )  :
        """
    setAnnotation Add the given annotation to the documenttype
                
                
                  the unique type of the annotation 
                
              
              
                
                  description
                
                
                  the user-visible description of the annotation 
                
              
              
                
                  annotation
                
                
                  the annotation itself
        """
        pass
    def removeAnnotation (self,  type: "str" )  :
        """
    removeAnnotation remove the specified annotation from the imagetype
                
                
                  the type defining the annotation
        """
        pass
class Selection(QObject):
    """
    Selection represents a selection on Krita. A selection is not necessarily associated with a particular Node or Image.
fromkritaimport*
d=Application.activeDocument()
n=d.activeNode()
r=n.bounds()
s=Selection()
s.select(r.width()/3,r.height()/3,r.width()/3,r.height()/3,255)
s.cut(n)
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    Create a new, empty selection object.
        """
        pass
    def duplicate (self  )  -> "Selection" :
        """
    a duplicate of the selection
        """
        pass
    def width (self  )  -> "int" :
        """
    the width of the selection
        """
        pass
    def height (self  )  -> "int" :
        """
    the height of the selection
        """
        pass
    def x (self  )  -> "int" :
        """
    the left-hand position of the selection.
        """
        pass
    def y (self  )  -> "int" :
        """
    the top position of the selection.
        """
        pass
    def move (self,  x: "int", y: "int" )  :
        """
    Move the selection's top-left corner to the given coordinates.
        """
        pass
    def clear (self  )  :
        """
    Make the selection entirely unselected.
        """
        pass
    def contract (self,  value: "int" )  :
        """
    Make the selection's width and height smaller by the given value. This will not move the selection's top-left position.
        """
        pass
    def copy (self,  node: "Node" )  :
        """
    copy copies the area defined by the selection from the node to the clipboard.node

the node from where the pixels will be copied.
        """
        pass
    def cut (self,  node: "Node" )  :
        """
    cut erases the area defined by the selection from the node and puts a copy on the clipboard.node

the node from which the selection will be cut.
        """
        pass
    def paste (self,  destination: "Node", x: "int", y: "int" )  :
        """
    paste pastes the content of the clipboard to the given node, limited by the area of the current selection.destination

the node where the pixels will be written 


x

the x position at which the clip will be written 


y

the y position at which the clip will be written
        """
        pass
    def erode (self  )  :
        """
    Erode the selection with a radius of 1 pixel.
        """
        pass
    def dilate (self  )  :
        """
    Dilate the selection with a radius of 1 pixel.
        """
        pass
    def border (self,  xRadius: "int", yRadius: "int" )  :
        """
    Border the selection with the given radius.
        """
        pass
    def feather (self,  radius: "int" )  :
        """
    Feather the selection with the given radius.
        """
        pass
    def grow (self,  xradius: "int", yradius: "int" )  :
        """
    Grow the selection with the given radius.
        """
        pass
    def shrink (self,  xRadius: "int", yRadius: "int", edgeLock: "bool" )  :
        """
    Shrink the selection with the given radius.
        """
        pass
    def smooth (self  )  :
        """
    Smooth the selection.
        """
        pass
    def invert (self  )  :
        """
    Invert the selection.
        """
        pass
    def resize (self,  w: "int", h: "int" )  :
        """
    Resize the selection to the given width and height. The top-left position will not be moved.
        """
        pass
    def select (self,  x: "int", y: "int", w: "int", h: "int", value: "int" )  :
        """
    Select the given area. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected.
        """
        pass
    def selectAll (self,  node: "Node", value: "int" )  :
        """
    Select all pixels in the given node. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected.
        """
        pass
    def replace (self,  selection: "Selection" )  :
        """
    Replace the current selection's selection with the one of the given selection.
        """
        pass
    def add (self,  selection: "Selection" )  :
        """
    Add the given selection's selected pixels to the current selection.
        """
        pass
    def subtract (self,  selection: "Selection" )  :
        """
    Subtract the given selection's selected pixels from the current selection.
        """
        pass
    def intersect (self,  selection: "Selection" )  :
        """
    Intersect the given selection with this selection.
        """
        pass
    def symmetricdifference (self,  selection: "Selection" )  :
        """
    Intersect with the inverse of the given selection with this selection.
        """
        pass
    def pixelData (self,  x: "int", y: "int", w: "int", h: "int" )  -> "QByteArray" :
        """
    pixelData reads the given rectangle from the Selection's mask and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.The byte array will contain one byte for every pixel, representing the selectedness. 0 is totally unselected, 255 is fully selected.
You can read outside the Selection's boundaries; those pixels will be unselected.
The byte array is a copy of the original selection data. 
x

x position from where to start reading 


y

y position from where to start reading 


w

row length to read 


h

number of rows to read 

a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def setPixelData (self,  value: "QByteArray", x: "int", y: "int", w: "int", h: "int" )  :
        """
    setPixelData writes the given bytes, of which there must be enough, into the Selection.value

the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (w * h) bytes are read.


x

the x position to start writing from 


y

the y position to start writing from 


w

the width of each row 


h

the number of rows to write
        """
        pass
class VectorLayer(Node):
    """
    The VectorLayer class A vector layer is a special layer that stores and shows vector shapes.Vector shapes all have their coordinates in points, which is a unit that represents 1/72th of an inch. Keep this in mind wen parsing the bounding box and position data.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.vectorlayer
        """
        pass
    def shapes (self  )  -> "List[ Shape  ]" :
        """
    shapesthe list of top-level shapes in this vector layer.
        """
        pass
    def toSvg (self  )  -> "str" :
        """
    toSvg convert the shapes in the layer to svg.the svg in a string.
        """
        pass
    def addShapesFromSvg (self,  svg: "str" )  -> "List[ Shape  ]" :
        """
    addShapesFromSvg add shapes to the layer from a valid svg.svg

valid svg string. 

the list of shapes added to the layer from the svg.
        """
        pass
    def shapeAtPosition (self,  position: "QPointF" )  -> "Shape" :
        """
    shapeAtPoint check if the position is located within any non-group shape's boundingBox() on the current layer.position

a QPointF of the position. 

the shape at the position, or None if no shape is found.
        """
        pass
    def shapesInRect (self,  rect: "QRectF", omitHiddenShapes: "bool" = True, containedMode: "bool" = False )  -> "List[ Shape  ]" :
        """
    shapeInRect get all non-group shapes that the shape's boundingBox() intersects or is contained within a given rectangle on the current layer.rect

a QRectF 


omitHiddenShapes

true if non-visible() shapes should be omitted, false if they should be included. omitHiddenShapes defaults to true. 


containedMode

false if only shapes that are within or intersect with the outline should be included, true if only shapes that are fully contained within the outline should be included. containedMode defaults to false 

returns a list of shapes.
        """
        pass
    def createGroupShape (self,  name: "str", shapes: "List[ Shape  ]" )  -> "Shape" :
        """
    createGroupShape combine a list of top level shapes into a group.name

the name of the shape. 


shapes

list of top level shapes. 

if successful, a GroupShape object will be returned.
        """
        pass
class Swatch:
    """
    The Swatch class is a thin wrapper around the KisSwatch class.A Swatch is a single color that is part of a palette, that has a name and an id. A Swatch color can be a spot color.
    """
    def __init__ (self  )  :
        """
    
        """
        pass
    def __init__ (self,  rhs: "Swatch" )  :
        """
    
        """
        pass
    def name (self  )  -> "str" :
        """
    
        """
        pass
    def setName (self,  name: "str" )  :
        """
    
        """
        pass
    def id (self  )  -> "str" :
        """
    
        """
        pass
    def setId (self,  id: "str" )  :
        """
    
        """
        pass
    def color (self  )  -> "ManagedColor" :
        """
    
        """
        pass
    def setColor (self,  color: "ManagedColor" )  :
        """
    
        """
        pass
    def spotColor (self  )  -> "bool" :
        """
    
        """
        pass
    def setSpotColor (self,  spotColor: "bool" )  :
        """
    
        """
        pass
    def isValid (self  )  -> "bool" :
        """
    
        """
        pass
class SelectionMask(Node):
    """
    The SelectionMask class A selection mask is a mask type node that can be used to store selections. In the gui, these are referred to as local selections.A selection mask can hold both raster and vector selections, though the API only supports raster selections.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.selectionmask
If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def selection (self  )  -> "Selection" :
        """
    
        """
        pass
    def setSelection (self,  selection: "Selection" )  :
        """
    
        """
        pass
class Krita(QObject):
    """
    Krita is a singleton class that offers the root access to the Krita object hierarchy.
The Krita.instance() is aliased as two builtins: Scripter and Application.
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    
        """
        pass
    def activeDocument (self  )  -> "Document" :
        """
    the currently active document, if there is one.
        """
        pass
    def setActiveDocument (self,  value: "Document" )  :
        """
    setActiveDocument activates the first view that shows the given documentvalue

the document we want to activate
        """
        pass
    def batchmode (self  )  -> "bool" :
        """
    batchmode determines whether the script is run in batch mode. If batchmode is true, scripts should now show messageboxes or dialog boxes.Note that this separate from Document.setBatchmode(), which determines whether export/save option dialogs are shown.
true if the script is run in batchmode
        """
        pass
    def setBatchmode (self,  value: "bool" )  :
        """
    setBatchmode sets the batchmode tovalue;

if true, scripts should not show dialogs or messageboxes.
        """
        pass
    def actions (self  )  -> "List[ QAction  ]" :
        """
    return a list of all actions for the currently active mainWindow.
        """
        pass
    def action (self,  name: "str" )  -> "QAction" :
        """
    the action that has been registered under the given name, or 0 if no such action exists.
        """
        pass
    def documents (self  )  -> "List[ Document  ]" :
        """
    a list of all open Documents
        """
        pass
    def dockers (self  )  -> "List[ QDockWidget  ]" :
        """
    a list of all the dockers
        """
        pass
    def filters (self  )  -> "List[str]" :
        """
    Filters are identified by an internal name. This function returns a list of all existing registered filters.a list of all registered filters
        """
        pass
    def filter (self,  name: "str" )  -> "Filter" :
        """
    filter construct a Filter object with a default configuration.name

the name of the filter. Use Krita.instance().filters() to get a list of all possible filters. 

the filter or None if there is no such filter.
        """
        pass
    def colorModels (self  )  -> "List[str]" :
        """
    colorModels creates a list with all color models id's registered.a list of all color models or a empty list if there is no such color models.
        """
        pass
    def colorDepths (self,  colorModel: "str" )  -> "List[str]" :
        """
    colorDepths creates a list with the names of all color depths compatible with the given color model.colorModel

the id of a color model. 

a list of all color depths or a empty list if there is no such color depths.
        """
        pass
    def filterStrategies (self  )  -> "List[str]" :
        """
    filterStrategies Retrieves all installed filter strategies. A filter strategy is used when transforming (scaling, shearing, rotating) an image to calculate the value of the new pixels. You can use ththe id's of all available filters.
        """
        pass
    def profiles (self,  colorModel: "str", colorDepth: "str" )  -> "List[str]" :
        """
    profiles creates a list with the names of all color profiles compatible with the given color model and color depth.colorModel

A string describing the color model of the image: 
A: Alpha mask 

RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 

XYZA: XYZ with alpha channel 

LABA: LAB with alpha channel 

CMYKA: CMYK with alpha channel 

GRAYA: Gray with alpha channel 

YCbCrA: YCbCr with alpha channel 



colorDepth

A string describing the color depth of the image: 
U8: unsigned 8 bits integer, the most common type 

U16: unsigned 16 bits integer 

F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 

F32: 32 bits floating point 



a list with valid names
        """
        pass
    def addProfile (self,  profilePath: "str" )  -> "bool" :
        """
    addProfile load the given profile into the profile registry.profilePath

the path to the profile. 

true if adding the profile succeeded.
        """
        pass
    def notifier (self  )  -> "Notifier" :
        """
    notifier the Notifier singleton emits signals when documents are opened and closed, the configuration changes, views are opened and closed or windows are opened.the notifier object
        """
        pass
    def version (self  )  -> "str" :
        """
    version Determine the version of KritaUsage: print(Application.version ())
the version string including git sha1 if Krita was built from git
        """
        pass
    def views (self  )  -> "List[ View  ]" :
        """
    a list of all views. A Document can be shown in more than one view.
        """
        pass
    def activeWindow (self  )  -> "Window" :
        """
    the currently active window or None if there is no window
        """
        pass
    def windows (self  )  -> "List[ Window  ]" :
        """
    a list of all windows
        """
        pass
    def resources (self,  type: "str" )  -> "dict[ str, Resource  ]" :
        """
    resources returns a list of Resource objects of the given typetype

Valid types are:


pattern 

gradient 

brush 

preset 

palette 

workspace
        """
        pass
    def recentDocuments (self  )  -> "List[str]" :
        """
    return all recent documents registered in the RecentFiles group of the kritarc
        """
        pass
    def createDocument (self,  width: "int", height: "int", name: "str", colorModel: "str", colorDepth: "str", profile: "str", resolution: "float" )  -> "Document" :
        """
    @brief createDocument creates a new document and image and registers
   the document with the Krita application.
   Unless you explicitly call Document::close() the document will remain
   known to the Krita document registry. The document and its image will
   only be deleted when Krita exits.
   The document will have one transparent layer.
   To create a new document and show it, do something like:
 fromKritaimport*
defadd_document_to_window():
d=Application.createDocument(100,100,"Test","RGBA","U8","",120.0)
Application.activeWindow().addView(d)
add_document_to_window()
    @param width the width in pixels
   @param height the height in pixels
   @param name the name of the image (not the filename of the document)
   @param colorModel A string describing the color model of the image:
   <ul>
   <li>A: Alpha mask</li>
   <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li>
   <li>XYZA: XYZ with alpha channel</li>
   <li>LABA: LAB with alpha channel</li>
   <li>CMYKA: CMYK with alpha channel</li>
   <li>GRAYA: Gray with alpha channel</li>
   <li>YCbCrA: YCbCr with alpha channel</li>
   </ul>
   @param colorDepth A string describing the color depth of the image:
   <ul>
   <li>U8: unsigned 8 bits integer, the most common type</li>
   <li>U16: unsigned 16 bits integer</li>
   <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li>
   <li>F32: 32 bits floating point</li>
   </ul>
   @param profile The name of an icc profile that is known to Krita. If an empty string is passed, the default is
   taken.
   @param resolution the resolution in points per inch.
   @return the created document.
        """
        pass
    def openDocument (self,  filename: "str" )  -> "Document" :
        """
    openDocument creates a new Document, registers it with the Krita application and loads the given file.filename

the file to open in the document 

the document
        """
        pass
    def openWindow (self  )  -> "Window" :
        """
    openWindow create a new main window. The window is not shown by default.
        """
        pass
    def addExtension (self,  extension: "Extension" )  :
        """
    addExtension add the given plugin to Krita. There will be a single instance of each Extension in the Krita process.extension

the extension to add.
        """
        pass
    def extensions (self  )  -> "List[ Extension  ]" :
        """
    return a list with all registered extension objects.
        """
        pass
    def addDockWidgetFactory (self,  factory: "DockWidgetFactoryBase" )  :
        """
    addDockWidgetFactory Add the given docker factory to the application. For scripts loaded on startup, this means that every window will have one of the dockers created by the factory.factory

The factory object.
        """
        pass
    def writeSetting (self,  group: "str", name: "str", value: "str" )  :
        """
    writeSetting write the given setting under the given name to the kritarc file in the given settings group.group

The group the setting belongs to. If empty, then the setting is written in the general section 


name

The name of the setting 


value

The value of the setting. Script settings are always written as strings.
        """
        pass
    def readSetting (self,  group: "str", name: "str", defaultValue: "str" )  -> "str" :
        """
    readSetting read the given setting value from the kritarc file.group

The group the setting is part of. If empty, then the setting is read from the general group. 


name

The name of the setting 


defaultValue

The default value of the setting 

a string representing the setting.
        """
        pass
    def icon (self,  iconName: "str" )  -> "QIcon" :
        """
    icon This allows you to get icons from Krita's internal icons.iconName

name of the icon. 

the icon related to this name.
        """
        pass
    @staticmethod
    def instance (  )  -> "Krita" :
        """
    instance retrieve the singleton instance of the Application object.
        """
        pass
    @staticmethod
    def fromVariant ( v: "QVariant" )  -> "QObject" :
        """
    Scripter.fromVariant(variant) variant is a QVariant returns instance of QObject-subclass
This is a helper method for PyQt because PyQt cannot cast a variant to a QObject or QWidget
        """
        pass
    @staticmethod
    def krita_i18n ( text: "str" )  -> "str" :
        """
    
        """
        pass
    @staticmethod
    def krita_i18nc ( context: "str", text: "str" )  -> "str" :
        """
    
        """
        pass
    @staticmethod
    def getAppDataLocation (  )  -> "str" :
        """
    
        """
        pass
class View(QObject):
    """
    View represents one view on a document. A document can be shown in more than one view at a time.
    """
    def window (self  )  -> "Window" :
        """
    the window this view is shown in.
        """
        pass
    def document (self  )  -> "Document" :
        """
    the document this view is showing.
        """
        pass
    def setDocument (self,  document: "Document" )  :
        """
    Reset the view to show document.
        """
        pass
    def visible (self  )  -> "bool" :
        """
    true if the current view is visible, false if not.
        """
        pass
    def setVisible (self  )  :
        """
    Make the current view visible.
        """
        pass
    def canvas (self  )  -> "Canvas" :
        """
    the canvas this view is showing. The canvas controls things like zoom and rotation.
        """
        pass
    def activateResource (self,  resource: "Resource" )  :
        """
    activateResource activates the given resource.resource

a pattern, gradient or paintop preset
        """
        pass
    def foregroundColor (self  )  -> "ManagedColor" :
        """
    @brief foregroundColor allows access to the currently active color.
   This is nominally per canvas/view, but in practice per mainwindow.
   @code
 color = Application.activeWindow().activeView().foregroundColor() components = color.components() components[0] = 1.0 components[1] = 0.6 components[2] = 0.7 color.setComponents(components) Application.activeWindow().activeView().setForeGroundColor(color)
        """
        pass
    def setForeGroundColor (self,  color: "ManagedColor" )  :
        """
    
        """
        pass
    def backgroundColor (self  )  -> "ManagedColor" :
        """
    
        """
        pass
    def setBackGroundColor (self,  color: "ManagedColor" )  :
        """
    
        """
        pass
    def currentBrushPreset (self  )  -> "Resource" :
        """
    
        """
        pass
    def setCurrentBrushPreset (self,  resource: "Resource" )  :
        """
    
        """
        pass
    def currentPattern (self  )  -> "Resource" :
        """
    
        """
        pass
    def setCurrentPattern (self,  resource: "Resource" )  :
        """
    
        """
        pass
    def currentGradient (self  )  -> "Resource" :
        """
    
        """
        pass
    def setCurrentGradient (self,  resource: "Resource" )  :
        """
    
        """
        pass
    def currentBlendingMode (self  )  -> "str" :
        """
    
        """
        pass
    def setCurrentBlendingMode (self,  blendingMode: "str" )  :
        """
    
        """
        pass
    def HDRExposure (self  )  -> "float" :
        """
    
        """
        pass
    def setHDRExposure (self,  exposure: "float" )  :
        """
    
        """
        pass
    def HDRGamma (self  )  -> "float" :
        """
    
        """
        pass
    def setHDRGamma (self,  gamma: "float" )  :
        """
    
        """
        pass
    def paintingOpacity (self  )  -> "float" :
        """
    
        """
        pass
    def setPaintingOpacity (self,  opacity: "float" )  :
        """
    
        """
        pass
    def brushSize (self  )  -> "float" :
        """
    
        """
        pass
    def setBrushSize (self,  brushSize: "float" )  :
        """
    
        """
        pass
    def paintingFlow (self  )  -> "float" :
        """
    
        """
        pass
    def setPaintingFlow (self,  flow: "float" )  :
        """
    
        """
        pass
    def showFloatingMessage (self,  message: "str", icon: "QIcon", timeout: "int", priority: "int" )  :
        """
    showFloatingMessage displays a floating message box on the top-left corner of the canvasmessage

Message to be displayed inside the floating message box 


icon

Icon to be displayed inside the message box next to the message string 


timeout

Milliseconds until the message box disappears 


priority

0 = High, 1 = Medium, 2 = Low. Higher priority messages will be displayed in place of lower priority messages
        """
        pass
    def selectedNodes (self  )  -> "List[ Node  ]" :
        """
    @brief selectedNodes returns a list of Nodes that are selected in this view.
fromkritaimport*
w=Krita.instance().activeWindow()
v=w.activeView()
selected_nodes=v.selectedNodes()
print(selected_nodes)
a list of Node objects which may be empty.
        """
        pass
    def flakeToDocumentTransform (self  )  -> "QTransform" :
        """
    flakeToDocumentTransform The transformation of the document relative to the view without rotation and mirroringQTransform
        """
        pass
    def flakeToCanvasTransform (self  )  -> "QTransform" :
        """
    flakeToCanvasTransform The transformation of the canvas relative to the view without rotation and mirroringQTransform
        """
        pass
    def flakeToImageTransform (self  )  -> "QTransform" :
        """
    flakeToImageTransform The transformation of the image relative to the view without rotation and mirroringQTransform
        """
        pass
class Canvas(QObject):
    """
    Canvas wraps the canvas inside a view on an image/document. It is responsible for the view parameters of the document: zoom, rotation, mirror, wraparound and instant preview.
    """
    def zoomLevel (self  )  -> "float" :
        """
    the current zoomlevel. 1.0 is 100%.
        """
        pass
    def setZoomLevel (self,  value: "float" )  :
        """
    setZoomLevel set the zoomlevel to the given value. 1.0 is 100%.
        """
        pass
    def resetZoom (self  )  :
        """
    resetZoom set the zoomlevel to 100%
        """
        pass
    def rotation (self  )  -> "float" :
        """
    the rotation of the canvas in degrees.
        """
        pass
    def setRotation (self,  angle: "float" )  :
        """
    setRotation set the rotation of the canvas to the givenangle

in degrees.
        """
        pass
    def resetRotation (self  )  :
        """
    resetRotation reset the canvas rotation.
        """
        pass
    def mirror (self  )  -> "bool" :
        """
    return true if the canvas is mirrored, false otherwise.
        """
        pass
    def setMirror (self,  value: "bool" )  :
        """
    setMirror turn the canvas mirroring on or off depending onvalue
        """
        pass
    def wrapAroundMode (self  )  -> "bool" :
        """
    true if the canvas is in wraparound mode, false if not. Only when OpenGL is enabled, is wraparound mode available.
        """
        pass
    def setWrapAroundMode (self,  enable: "bool" )  :
        """
    setWrapAroundMode set wraparound mode toenable
        """
        pass
    def levelOfDetailMode (self  )  -> "bool" :
        """
    true if the canvas is in Instant Preview mode, false if not. Only when OpenGL is enabled, is Instant Preview mode available.
        """
        pass
    def setLevelOfDetailMode (self,  enable: "bool" )  :
        """
    setLevelOfDetailMode sets Instant Preview toenable
        """
        pass
    def view (self  )  -> "View" :
        """
    the view that holds this canvas
        """
        pass
class Window(QObject):
    """
    Window represents one Krita mainwindow. A window can have any number of views open on any number of documents.
    """
    def qwindow (self  )  -> "QMainWindow" :
        """
    Return a handle to the QMainWindow widget. This is useful to e.g. parent dialog boxes and message box.
        """
        pass
    def dockers (self  )  -> "List[ QDockWidget  ]" :
        """
    dockersa list of all the dockers belonging to this window
        """
        pass
    def views (self  )  -> "List[ View  ]" :
        """
    a list of open views in this window
        """
        pass
    def addView (self,  document: "Document" )  -> "View" :
        """
    Open a new view on the given document in this window
        """
        pass
    def showView (self,  view: "View" )  :
        """
    Make the given view active in this window. If the view does not belong to this window, nothing happens.
        """
        pass
    def activeView (self  )  -> "View" :
        """
    the currently active view or 0 if no view is active
        """
        pass
    def activate (self  )  :
        """
    activate activates this Window.
        """
        pass
    def close (self  )  :
        """
    close the active window and all its Views. If there are no Views left for a given Document, that Document will also be closed.
        """
        pass
    def createAction (self,  id: "str", text: "str" = '', menuLocation: "str" = "tools/scripts" )  -> "QAction" :
        """
    createAction creates a QAction object and adds it to the action manager for this Window.id

The unique id for the action. This will be used to propertize the action if any .action file is present 


text

The user-visible text of the action. If empty, the text from the .action file is used. 


menuLocation

a /-separated string that describes which menu the action should be places in. Default is "tools/scripts" 

the new action.
        """
        pass
class Channel(QObject):
    """
    A Channel represents a single channel in a Node. Krita does not use channels to store local selections: these are strictly the color and alpha channels.
    """
    def visible (self  )  -> "bool" :
        """
    visible checks whether this channel is visible in the nodethe status of this channel
        """
        pass
    def setVisible (self,  value: "bool" )  :
        """
    setvisible set the visibility of the channel to the given value.
        """
        pass
    def name (self  )  -> "str" :
        """
    the name of the channel
        """
        pass
    def position (self  )  -> "int" :
        """
    the position of the first byte of the channel in the pixel
        """
        pass
    def channelSize (self  )  -> "int" :
        """
    the number of bytes this channel takes
        """
        pass
    def bounds (self  )  -> "QRect" :
        """
    the exact bounds of the channel. This can be smaller than the bounds of the Node this channel is part of.
        """
        pass
    def pixelData (self,  rect: "QRect" )  -> "QByteArray" :
        """
    Read the values of the channel into the a byte array for each pixel in the rect from the Node this channel is part of, and returns it.
Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita returns 32 bits float for every channel; the libkis scripting API does not support half.
        """
        pass
    def setPixelData (self,  value: "QByteArray", rect: "QRect" )  :
        """
    setPixelData writes the given data to the relevant channel in the Node. This is only possible for Nodes that have a paintDevice, so nothing will happen when trying to write to e.g. a group layer.Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita expects to be given a 4 byte, 32 bits float for every channel; the libkis scripting API does not support half.

value

a byte array with exactly enough bytes. 


rect

the rectangle to write the bytes into
        """
        pass
class Scratchpad(QWidget):
    """
    The Scratchpad class A scratchpad is a type of blank canvas area that can be painted on with the normal painting devices.
    """
    def __init__ (self,  view: "View", defaultColor: "QColor", parent: "QWidget" = 0 )  :
        """
    
        """
        pass
    def clear (self  )  :
        """
    Clears out scratchpad with color specified set during setup.
        """
        pass
    def setFillColor (self,  color: "QColor" )  :
        """
    Fill the entire scratchpad with a color.Color

to fill the canvas with
        """
        pass
    def setModeManually (self,  value: "bool" )  :
        """
    Switches between a GUI controlling the current mode and when mouse clicks control mode.Setting

to true allows GUI to control the mode with explicitly setting mode
        """
        pass
    def setMode (self,  modeName: "str" )  :
        """
    Manually set what mode scratchpad is in. Ignored if "setModeManually is set to false.Available

options are: "painting", "panning", and "colorsampling"
        """
        pass
    def linkCanvasZoom (self,  value: "bool" )  :
        """
    Makes a connection between the zoom of the canvas and scratchpad area so they zoom in sync.Should

the scratchpad share the zoom level. Default is true
        """
        pass
    def loadScratchpadImage (self,  image: "QImage" )  :
        """
    Load image data to the scratchpad.Image

object to load
        """
        pass
    def copyScratchpadImageData (self  )  -> "QImage" :
        """
    Take what is on the scratchpad area and grab image.the image data from the scratchpad
        """
        pass
class FillLayer(Node):
    """
    The FillLayer class A fill layer is much like a filter layer in that it takes a name and filter. It however specializes in filters that fill the whole canvas, such as a pattern or full color fill.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.The type of the node. Valid types are: 
paintlayer 

grouplayer 

filelayer 

filterlayer 

filllayer 

clonelayer 

vectorlayer 

transparencymask 

filtermask 

transformmask 

selectionmask 

colorizemask 


If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def setGenerator (self,  generatorName: "str", filterConfig: "InfoObject" )  -> "bool" :
        """
    setGenerator set the given generator for this fill layergeneratorName

"pattern" or "color" 


filterConfig

a configuration object appropriate to the given generator plugin 

true if the generator was correctly created and set on the layer
        """
        pass
    def generatorName (self  )  -> "str" :
        """
    
        """
        pass
    def filterConfig (self  )  -> "InfoObject" :
        """
    
        """
        pass
class CloneLayer(Node):
    """
    The CloneLayer class A clone layer is a layer that takes a reference inside the image and shows the exact same pixeldata.If the original is updated, the clone layer will update too.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.clonelayer
        """
        pass
    def sourceNode (self  )  -> "Node" :
        """
    sourceNodethe node the clone layer is based on.
        """
        pass
    def setSourceNode (self,  node: "Node" )  :
        """
    setSourceNodenode

the node to use as the source of the clone layer.
        """
        pass
class DockWidget(QDockWidget):
    """
    DockWidget is the base class for custom Dockers. Dockers are created by a factory class which needs to be registered by calling Application.addDockWidgetFactory:
classHelloDocker(DockWidget):
def__init__(self):
super().__init__()
label=QLabel("Hello",self)
self.setWidget(label)
self.label=label
self.setWindowTitle("HelloDocker")
defcanvasChanged(self,canvas):
self.label.setText("Hellodocker:canvaschanged");
Application.addDockWidgetFactory(DockWidgetFactory("hello",DockWidgetFactoryBase.DockRight,HelloDocker))
One docker per window will be created, not one docker per canvas or view. When the user switches between views/canvases, canvasChanged will be called. You can override that method to reset your docker's internal state, if necessary.
    """
    def __init__ (self  )  :
        """
    
        """
        pass
class GroupLayer(Node):
    """
    The GroupLayer class A group layer is a layer that can contain other layers. In Krita, layers within a group layer are composited first before they are added into the composition code for where the group is in the stack. This has a significant effect on how it is interpreted for blending modes.PassThrough changes this behaviour.
Group layer cannot be animated, but can contain animated layers or masks.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.grouplayer
        """
        pass
    def setPassThroughMode (self,  passthrough: "bool" )  :
        """
    setPassThroughMode This changes the way how compositing works. Instead of compositing all the layers before compositing it with the rest of the image, the group layer becomes a sort of formal way to organise everything.Passthrough mode is the same as it is in photoshop, and the inverse of SVG's isolation attribute(with passthrough=false being the same as isolation="isolate").

passthrough

whether or not to set the layer to passthrough.
        """
        pass
    def passThroughMode (self  )  -> "bool" :
        """
    passThroughModereturns whether or not this layer is in passthrough mode. 
setPassThroughMode
        """
        pass
class TransformMask(Node):
    """
    The TransformMask class A transform mask is a mask type node that can be used to store transformations.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.transformmask
If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def finalAffineTransform (self  )  -> "QTransform" :
        """
    
        """
        pass
    def toXML (self  )  -> "str" :
        """
    toXMLa string containing XML formated transform parameters.
        """
        pass
    def fromXML (self,  xml: "str" )  -> "bool" :
        """
    @brief fromXML set the transform of the transform mask from XML formatted data.
   The xml must have a valid id
   dumbparams - placeholder for static transform masks
   tooltransformparams - static transform mask
   animatedtransformparams - animated transform mask
 <!DOCTYPEtransform_params>
<transform_params>
<mainid="tooltransformparams"/>
<datamode="0">
<free_transform>
<transformedCentertype="pointf"x="12.3102137276208"y="11.0727768562035"/>
<originalCentertype="pointf"x="20"y="20"/>
<rotationCenterOffsettype="pointf"x="0"y="0"/>
<transformAroundRotationCentervalue="0"type="value"/>
<aXvalue="0"type="value"/>
<aYvalue="0"type="value"/>
<aZvalue="0"type="value"/>
<cameraPosz="1024"type="vector3d"x="0"y="0"/>
<scaleXvalue="1"type="value"/>
<scaleYvalue="1"type="value"/>
<shearXvalue="0"type="value"/>
<shearYvalue="0"type="value"/>
<keepAspectRatiovalue="0"type="value"/>
<flattenedPerspectiveTransformm23="0"m31="0"m32="0"type="transform"m33="1"m12="0"m13="0"m22="1"m11="1"m21="0"/>
<filterIdvalue="Bicubic"type="value"/>
</free_transform>
</data>
</transform_params>
 
xml

a valid formated XML string with proper main and data elements. 

a true response if successful, a false response if failed.
        """
        pass
class Filter(QObject):
    """
    Filter: represents a filter and its configuration. A filter is identified by an internal name. The configuration for each filter is defined as an InfoObject: a map of name and value pairs.
Currently available filters are:
'autocontrast', 'blur', 'bottom edge detections', 'brightnesscontrast', 'burn', 'colorbalance', 'colortoalpha', 'colortransfer', 'desaturate', 'dodge', 'emboss', 'emboss all directions', 'emboss horizontal and vertical', 'emboss horizontal only', 'emboss laplascian', 'emboss vertical only', 'gaussian blur', 'gaussiannoisereducer', 'gradientmap', 'halftone', 'hsvadjustment', 'indexcolors', 'invert', 'left edge detections', 'lens blur', 'levels', 'maximize', 'mean removal', 'minimize', 'motion blur', 'noise', 'normalize', 'oilpaint', 'perchannel', 'phongbumpmap', 'pixelize', 'posterize', 'raindrops', 'randompick', 'right edge detections', 'roundcorners', 'sharpen', 'smalltiles', 'sobel', 'threshold', 'top edge detections', 'unsharp', 'wave', 'waveletnoisereducer']
    """
    def __init__ (self  )  :
        """
    Filter: create an empty filter object. Until a name is set, the filter cannot be applied.
        """
        pass
    def name (self  )  -> "str" :
        """
    name the internal name of this filter.the name.
        """
        pass
    def setName (self,  name: "str" )  :
        """
    setName set the filter's name to the given name.
        """
        pass
    def configuration (self  )  -> "InfoObject" :
        """
    the configuration object for the filter
        """
        pass
    def setConfiguration (self,  value: "InfoObject" )  :
        """
    setConfiguration set the configuration object for the filter
        """
        pass
    def apply (self,  node: "Node", x: "int", y: "int", w: "int", h: "int" )  -> "bool" :
        """
    Apply the filter to the given node.node

the node to apply the filter to 


x



y



w



h

describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node. 

true if the filter was applied successfully, or false if the filter could not be applied because the node is locked or does not have an editable paint device.
        """
        pass
    def startFilter (self,  node: "Node", x: "int", y: "int", w: "int", h: "int" )  -> "bool" :
        """
    startFilter starts the given filter on the given node.node

the node to apply the filter to 


x



y



w



h

describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node.
        """
        pass
class Notifier(QObject):
    """
    The Notifier can be used to be informed of state changes in the Krita application.
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    
        """
        pass
    def active (self  )  -> "bool" :
        """
    true if the Notifier is active.
        """
        pass
    def setActive (self,  value: "bool" )  :
        """
    Enable or disable the Notifier
        """
        pass
class GroupShape(Shape):
    """
    The GroupShape class A group shape is a vector object with child shapes.
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    
        """
        pass
    def type (self  )  -> "str" :
        """
    type returns the type."groupshape"
        """
        pass
    def children (self  )  -> "List[ Shape  ]" :
        """
    childrenthe child shapes of this group shape.
        """
        pass
class PaletteView(QWidget):
    """
    The PaletteView class is a wrapper around a MVC method for handling palettes. This class shows a nice widget that can drag and drop, edit colors in a colorset and will handle adding and removing entries if you'd like it to.
    """
    def __init__ (self,  parent: "QWidget" = 0 )  :
        """
    
        """
        pass
    def setPalette (self,  palette: "Palette" )  :
        """
    setPalette Set a new palette.palette
        """
        pass
    def addEntryWithDialog (self,  color: "ManagedColor" )  -> "bool" :
        """
    addEntryWithDialog This gives a simple dialog for adding colors, with options like adding name, id, and to which group the color should be added.color

the default color to add 

whether it was successful.
        """
        pass
    def addGroupWithDialog (self  )  -> "bool" :
        """
    addGroupWithDialog gives a little dialog to ask for the desired groupname.whether this was successful.
        """
        pass
    def removeSelectedEntryWithDialog (self  )  -> "bool" :
        """
    removeSelectedEntryWithDialog removes the selected entry. If it is a group, it pop up a dialog asking whether the colors should also be removed.whether this was successful
        """
        pass
    def trySelectClosestColor (self,  color: "ManagedColor" )  :
        """
    trySelectClosestColor tries to select the closest color to the one given. It does not force a change on the active color.color

the color to compare to.
        """
        pass
class FilterMask(Node):
    """
    The FilterMask class A filter mask, unlike a filter layer, will add a non-destructive filter to the composited image of the node it is attached to.You can set grayscale pixeldata on the filter mask to adjust where the filter is applied.
Filtermasks can be animated.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.The type of the node. Valid types are: 
paintlayer 

grouplayer 

filelayer 

filterlayer 

filllayer 

clonelayer 

vectorlayer 

transparencymask 

filtermask 

transformmask 

selectionmask 

colorizemask 


If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def setFilter (self,  filter: "Filter" )  :
        """
    
        """
        pass
    def filter (self  )  -> "Filter" :
        """
    
        """
        pass
class DockWidgetFactoryBase(KoDockFactoryBase):
    """
    The DockWidgetFactoryBase class is the base class for plugins that want to add a dock widget to every window. You do not need to implement this class yourself, but create a DockWidget implementation and then add the DockWidgetFactory to the Krita instance like this:classHelloDocker(DockWidget):
def__init__(self):
super().__init__()
label=QLabel("Hello",self)
self.setWidget(label)
self.label=label
defcanvasChanged(self,canvas):
self.label.setText("Hellodocker:canvaschanged");
Application.addDockWidgetFactory(DockWidgetFactory("hello",DockWidgetFactoryBase.DockRight,HelloDocker))
    """
    def __init__ (self,  _id: "str", _dockPosition: "DockPosition" )  :
        """
    
        """
        pass
    def id (self  )  -> "str" :
        """
    
        """
        pass
    def defaultDockPosition (self  )  -> "DockPosition" :
        """
    
        """
        pass
class ColorizeMask(Node):
    """
    The ColorizeMask class A colorize mask is a mask type node that can be used to color in line art.window=Krita.instance().activeWindow()
doc=Krita.instance().createDocument(10,3,"Test","RGBA","U8","",120.0)
window.addView(doc)
root=doc.rootNode();
node=doc.createNode("layer","paintLayer")
root.addChildNode(node,None)
nodeData=QByteArray.fromBase64(b"AAAAAAAAAAAAAAAAEQYMBhEGDP8RBgz/EQYMAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARBgz5EQYM/xEGDAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQYMAhEGDAkRBgwCAAAAAAAAAAAAAAAA");
node.setPixelData(nodeData,0,0,10,3)
cols=[ManagedColor('RGBA','U8',''),ManagedColor('RGBA','U8','')]
cols[0].setComponents([0.65490198135376,0.345098048448563,0.474509805440903,1.0]);
cols[1].setComponents([0.52549022436142,0.666666686534882,1.0,1.0]);
keys=[
QByteArray.fromBase64(b"/48AAAAAAAAAAAAAAAAAAAAAAACmCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
QByteArray.fromBase64(b"AAAAAAAAAACO9ocAAAAAAAAAAAAAAAAAAAAAAMD/uQAAAAAAAAAAAAAAAAAAAAAAGoMTAAAAAAAAAAAA")
]
mask=doc.createColorizeMask('c1')
node.addChildNode(mask,None)
mask.setEditKeyStrokes(True)
mask.setUseEdgeDetection(True)
mask.setEdgeDetectionSize(4.0)
mask.setCleanUpAmount(70.0)
mask.setLimitToDeviceBounds(True)
mask.initializeKeyStrokeColors(cols)
forcol,keyinzip(cols,keys):
mask.setKeyStrokePixelData(key,col,0,0,20,3)
mask.updateMask()
mask.setEditKeyStrokes(False);
mask.setShowOutput(True);
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.colorizemask
If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def keyStrokesColors (self  )  -> "List[ ManagedColor  ]" :
        """
    keyStrokesColors Colors used in the Colorize Mask's keystrokes.a ManagedColor list containing the colors of keystrokes.
        """
        pass
    def initializeKeyStrokeColors (self,  colors: "List[ ManagedColor  ]", transparentIndex: "int" = -1 )  :
        """
    initializeKeyStrokeColors Set the colors to use for the Colorize Mask's keystrokes.colors

a list of ManagedColor to use for the keystrokes. 


transparentIndex

index of the color that should be marked as transparent.
        """
        pass
    def removeKeyStroke (self,  color: "ManagedColor" )  :
        """
    removeKeyStroke Remove a color from the Colorize Mask's keystrokes.color

a ManagedColor to be removed from the keystrokes.
        """
        pass
    def transparencyIndex (self  )  -> "int" :
        """
    transparencyIndex Index of the transparent color.an integer containing the index of the current color marked as transparent.
        """
        pass
    def keyStrokePixelData (self,  color: "ManagedColor", x: "int", y: "int", w: "int", h: "int" )  -> "QByteArray" :
        """
    keyStrokePixelData reads the given rectangle from the keystroke image data and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.color

a ManagedColor to get keystrokes pixeldata from. 


x

x position from where to start reading 


y

y position from where to start reading 


w

row length to read 


h

number of rows to read 

a QByteArray with the pixel data. The byte array may be empty.
        """
        pass
    def setKeyStrokePixelData (self,  value: "QByteArray", color: "ManagedColor", x: "int", y: "int", w: "int", h: "int" )  -> "bool" :
        """
    setKeyStrokePixelData writes the given bytes, of which there must be enough, into the keystroke, the keystroke's original pixels are overwrittenvalue

the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.


color

a ManagedColor to set keystrokes pixeldata for. 


x

the x position to start writing from 


y

the y position to start writing from 


w

the width of each row 


h

the number of rows to write 

true if writing the pixeldata worked
        """
        pass
    def setUseEdgeDetection (self,  value: "bool" )  :
        """
    setUseEdgeDetection Activate this for line art with large solid areas, for example shadows on an object.value

true to enable edge detection, false to disable.
        """
        pass
    def useEdgeDetection (self  )  -> "bool" :
        """
    useEdgeDetectiontrue if Edge detection is enabled, false if disabled.
        """
        pass
    def setEdgeDetectionSize (self,  value: "float" )  :
        """
    setEdgeDetectionSize Set the value to the thinnest line on the image.value

a float value of the edge size to detect in pixels.
        """
        pass
    def edgeDetectionSize (self  )  -> "float" :
        """
    edgeDetectionSizea float value of the edge detection size in pixels.
        """
        pass
    def setCleanUpAmount (self,  value: "float" )  :
        """
    setCleanUpAmount This will attempt to handle messy strokes that overlap the line art where they shouldn't.value

a float value from 0.0 to 100.00 where 0.0 is no cleanup is done and 100.00 is most aggressive.
        """
        pass
    def cleanUpAmount (self  )  -> "float" :
        """
    cleanUpAmounta float value of 0.0 to 100.0 representing the cleanup amount where 0.0 is no cleanup is done and 100.00 is most aggressive.
        """
        pass
    def setLimitToDeviceBounds (self,  value: "bool" )  :
        """
    setLimitToDeviceBounds Limit the colorize mask to the combined layer bounds of the strokes and the line art it is filling. This can speed up the use of the mask on complicated compositions, such as comic pages.value

set true to enabled limit bounds, false to disable.
        """
        pass
    def limitToDeviceBounds (self  )  -> "bool" :
        """
    limitToDeviceBoundstrue if limit bounds is enabled, false if disabled.
        """
        pass
    def updateMask (self,  force: "bool" = False )  :
        """
    updateMask Process the Colorize Mask's keystrokes and generate a projection of the computed colors.force

force an update
        """
        pass
    def resetCache (self  )  :
        """
    
        """
        pass
    def showOutput (self  )  -> "bool" :
        """
    showOutput Show output mode allows the user to see the result of the Colorize Mask's algorithm.true if edit show coloring mode is enabled, false if disabled.
        """
        pass
    def setShowOutput (self,  enabled: "bool" )  :
        """
    setShowOutput Toggle Colorize Mask's show output mode.enabled

set true to enable show coloring mode and false to disable it.
        """
        pass
    def editKeyStrokes (self  )  -> "bool" :
        """
    editKeyStrokes Edit keystrokes mode allows the user to modify keystrokes on the active Colorize Mask.true if edit keystrokes mode is enabled, false if disabled.
        """
        pass
    def setEditKeyStrokes (self,  enabled: "bool" )  :
        """
    setEditKeyStrokes Toggle Colorize Mask's edit keystrokes mode.enabled

set true to enable edit keystrokes mode and false to disable it.
        """
        pass
class Preset(QObject):
    """
    The Preset class Preset is a resource object that stores brush preset data.An example for printing the current brush preset and all its settings:
fromkritaimport*
view=Krita.instance().activeWindow().activeView()
preset=Preset(view.currentBrushPreset())
print(preset.toXML())
    """
    def __init__ (self,  resource: "Resource" )  :
        """
    
        """
        pass
    def toXML (self  )  -> "str" :
        """
    toXML convert the preset settings into a preset formatted xml.the xml in a string.
        """
        pass
    def fromXML (self,  xml: "str" )  :
        """
    fromXML convert the preset settings into a preset formatted xml.xml

valid xml preset string.
        """
        pass
class Palette(QObject):
    """
    The Palette class Palette is a resource object that stores organised color data. It's purpose is to allow artists to save colors and store them.An example for printing all the palettes and the entries:
importsys
fromkritaimport*
resources=Application.resources("palette")
for(k,v)inresources.items():
print(k)
palette=Palette(v)
forxinrange(palette.numberOfEntries()):
entry=palette.colorSetEntryByIndex(x)
c=palette.colorForEntry(entry);
print(x,entry.name(),entry.id(),entry.spotColor(),c.toQString())
    """
    def __init__ (self,  resource: "Resource" )  :
        """
    
        """
        pass
    def numberOfEntries (self  )  -> "int" :
        """
    numberOfEntries
        """
        pass
    def columnCount (self  )  -> "int" :
        """
    columnCountthe amount of columns this palette is set to use.
        """
        pass
    def setColumnCount (self,  columns: "int" )  :
        """
    setColumnCount Set the amount of columns this palette should use.
        """
        pass
    def comment (self  )  -> "str" :
        """
    commentthe comment or description associated with the palette.
        """
        pass
    def setComment (self,  comment: "str" )  :
        """
    setComment set the comment or description associated with the palette.comment
        """
        pass
    def groupNames (self  )  -> "List[str]" :
        """
    groupNamesthe list of group names. This is list is in the order these groups are in the file.
        """
        pass
    def addGroup (self,  name: "str" )  :
        """
    addGroupname

of the new group 

whether adding the group was successful.
        """
        pass
    def removeGroup (self,  name: "str", keepColors: "bool" = True )  :
        """
    removeGroupname

the name of the group to remove. 


keepColors

whether or not to delete all the colors inside, or to move them to the default group.
        """
        pass
    def colorsCountTotal (self  )  -> "int" :
        """
    colorsCountTotalthe total amount of entries in the whole group
        """
        pass
    def colorSetEntryByIndex (self,  index: "int" )  -> "Swatch" :
        """
    colorSetEntryByIndex get the colorsetEntry from the global index.index

the global index 

the colorset entry
        """
        pass
    def colorSetEntryFromGroup (self,  index: "int", groupName: "str" )  -> "Swatch" :
        """
    colorSetEntryFromGroupindex

index in the group. 


groupName

the name of the group to get the color from. 

the colorsetentry.
        """
        pass
    def addEntry (self,  entry: "Swatch", groupName: "str" = '' )  :
        """
    addEntry add an entry to a group. Gets appended to the end.entry

the entry 


groupName

the name of the group to add to.
        """
        pass
    def removeEntry (self,  index: "int", groupName: "str" )  :
        """
    removeEntry remove the entry at index from the group groupName.
        """
        pass
    def changeGroupName (self,  oldGroupName: "str", newGroupName: "str" )  :
        """
    changeGroupName change the group name.oldGroupName

the old groupname to change. 


newGroupName

the new name to change it into. 

whether successful. Reasons for failure include not knowing have oldGroupName
        """
        pass
    def moveGroup (self,  groupName: "str", groupNameInsertBefore: "str" = '' )  :
        """
    moveGroup move the group to before groupNameInsertBefore.groupName

group to move. 


groupNameInsertBefore

group to inset before. 

whether successful. Reasons for failure include either group not existing.
        """
        pass
    def save (self  )  -> "bool" :
        """
    save save the palettewhether it was successful.
        """
        pass
class ManagedColor(QObject):
    """
    The ManagedColor class is a class to handle colors that are color managed. A managed color is a color of which we know the model(RGB, LAB, CMYK, etc), the bitdepth and the specific properties of its colorspace, such as the whitepoint, chromaticities, trc, etc, as represented by the color profile.Krita has two color management systems. LCMS and OCIO. LCMS is the one handling the ICC profile stuff, and the major one handling that ManagedColor deals with. OCIO support is only in the display of the colors. ManagedColor has some support for it in colorForCanvas()
All colors in Krita are color managed. QColors are understood as RGB-type colors in the sRGB space.
We recommend you make a color like this:
colorYellow=ManagedColor("RGBA","U8","")
QVector<float>yellowComponents=colorYellow.components()
yellowComponents[0]=1.0
yellowComponents[1]=1.0
yellowComponents[2]=0
yellowComponents[3]=1.0
colorYellow.setComponents(yellowComponents)
QColoryellow=colorYellow.colorForCanvas(canvas)
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    ManagedColor Create a ManagedColor that is black and transparent.
        """
        pass
    def __init__ (self,  colorModel: "str", colorDepth: "str", colorProfile: "str", parent: "QObject" = None )  :
        """
    ManagedColor create a managed color with the given color space properties.setColorModel() for more details.
        """
        pass
    def colorForCanvas (self,  canvas: "Canvas" )  -> "QColor" :
        """
    colorForCanvascanvas

the canvas whose color management you'd like to use. In Krita, different views have separate canvasses, and these can have different OCIO configurations active. 

the QColor as it would be displaying on the canvas. This result can be used to draw widgets with the correct configuration applied.
        """
        pass
    def colorDepth (self  )  -> "str" :
        """
    colorDepth A string describing the color depth of the image: 
U8: unsigned 8 bits integer, the most common type 

U16: unsigned 16 bits integer 

F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 

F32: 32 bits floating point 

the color depth.
        """
        pass
    def colorModel (self  )  -> "str" :
        """
    colorModel retrieve the current color model of this document:A: Alpha mask 

RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 

XYZA: XYZ with alpha channel 

LABA: LAB with alpha channel 

CMYKA: CMYK with alpha channel 

GRAYA: Gray with alpha channel 

YCbCrA: YCbCr with alpha channel 

the internal color model string.
        """
        pass
    def colorProfile (self  )  -> "str" :
        """
    the name of the current color profile
        """
        pass
    def setColorProfile (self,  colorProfile: "str" )  -> "bool" :
        """
    setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is not converted.colorProfile



false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed.
        """
        pass
    def setColorSpace (self,  colorModel: "str", colorDepth: "str", colorProfile: "str" )  -> "bool" :
        """
    setColorSpace convert the nodes and the image to the given colorspace. The conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as flags and no blackpoint compensation.colorModel

A string describing the color model of the image: 
A: Alpha mask 

RGBA: RGB with alpha channel (The actual order of channels is most often BGR!) 

XYZA: XYZ with alpha channel 

LABA: LAB with alpha channel 

CMYKA: CMYK with alpha channel 

GRAYA: Gray with alpha channel 

YCbCrA: YCbCr with alpha channel 



colorDepth

A string describing the color depth of the image: 
U8: unsigned 8 bits integer, the most common type 

U16: unsigned 16 bits integer 

F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR 

F32: 32 bits floating point 



colorProfile

a valid color profile for this color model and color depth combination. 

false the combination of these arguments does not correspond to a colorspace.
        """
        pass
    def components (self  )  -> "List[ float ]" :
        """
    componentsa QVector containing the channel/components of this color normalized. This includes the alphachannel.
        """
        pass
    def componentsOrdered (self  )  -> "List[ float ]" :
        """
    componentsOrdered()same as Components, except the values are ordered to the display.
        """
        pass
    def setComponents (self,  values: "List[ float ]" )  :
        """
    setComponents Set the channel/components with normalized values. For integer colorspace, this obviously means the limit is between 0.0-1.0, but for floating point colorspaces, 2.4 or 103.5 are still meaningful (if bright) values.values

the QVector containing the new channel/component values. These should be normalized.
        """
        pass
    def toXML (self  )  -> "str" :
        """
    Serialize this color following Create's swatch color specification available at https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft
        """
        pass
    def fromXML (self,  xml: "str" )  :
        """
    Unserialize a color following Create's swatch color specification available at https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft

xml

an XML color

the unserialized color, or an empty color object if the function failed to unserialize the color
        """
        pass
    def toQString (self  )  -> "str" :
        """
    toQString create a user-visible string of the channel names and the channel valuesa string that can be used to display the values of this color to the user.
        """
        pass
    @staticmethod
    def fromQColor ( qcolor: "QColor", canvas: "Canvas" = 0 )  -> "ManagedColor" :
        """
    fromQColor is the (approximate) reverse of colorForCanvas()qcolor

the QColor to convert to a KoColor. 


canvas

the canvas whose color management you'd like to use. 

the approximated ManagedColor, to use for canvas resources.
        """
        pass
class TransparencyMask(Node):
    """
    The TransparencyMask class A transparency mask is a mask type node that can be used to show and hide parts of a layer.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.transparencymask
If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned.
        """
        pass
    def selection (self  )  -> "Selection" :
        """
    
        """
        pass
    def setSelection (self,  selection: "Selection" )  :
        """
    
        """
        pass
class Resource(QObject):
    """
    A Resource represents a gradient, pattern, brush tip, brush preset, palette or workspace definition.
allPresets=Application.resources("preset")
forpresetinallPresets:
print(preset.name())
Resources are identified by their type, name and filename. If you want to change the contents of a resource, you should read its data using data(), parse it and write the changed contents back.
    """
    def __init__ (self,  resourceId: "int", type: "str", name: "str", filename: "str", image: "QImage", parent: "QObject" = None )  :
        """
    
        """
        pass
    def __init__ (self,  rhs: "Resource" )  :
        """
    
        """
        pass
    def type (self  )  -> "str" :
        """
    Return the type of this resource. Valid types are: 
pattern: a raster image representing a pattern 

gradient: a gradient 

brush: a brush tip 

preset: a brush preset 

palette: a color set 

workspace: a workspace definition.
        """
        pass
    def name (self  )  -> "str" :
        """
    The user-visible name of the resource.
        """
        pass
    def setName (self,  value: "str" )  :
        """
    setName changes the user-visible name of the current resource.
        """
        pass
    def filename (self  )  -> "str" :
        """
    The filename of the resource, if present. Not all resources are loaded from files.
        """
        pass
    def image (self  )  -> "QImage" :
        """
    An image that can be used to represent the resource in the user interface. For some resources, like patterns, the image is identical to the resource, for others it's a mere icon.
        """
        pass
    def setImage (self,  image: "QImage" )  :
        """
    Change the image for this resource.
        """
        pass
class FileLayer(Node):
    """
    The FileLayer class A file layer is a layer that can reference an external image and show said reference in the layer stack.If the external image is updated, Krita will try to update the file layer image as well.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks."filelayer"
        """
        pass
    def setProperties (self,  fileName: "str", scalingMethod: "str" = "None", scalingFilter: "str" = "Bicubic" )  :
        """
    setProperties Change the properties of the file layer.fileName

- A String containing the absolute file name. 


scalingMethod

- a string with the scaling method, defaults to "None", other options are "ToImageSize" and "ToImagePPI" 


scalingFilter

- a string with the scaling filter, defaults to "Bicubic", other options are "Hermite", "NearestNeighbor", "Bilinear", "Bell", "BSpline", "Lanczos3", "Mitchell"
        """
        pass
    def resetCache (self  )  :
        """
    makes the file layer to reload the connected image from disk
        """
        pass
    def path (self  )  -> "str" :
        """
    pathA QString with the full path of the referenced image.
        """
        pass
    def scalingMethod (self  )  -> "str" :
        """
    scalingMethod returns how the file referenced is scaled.one of the following: 
None - The file is not scaled in any way. 

ToImageSize - The file is scaled to the full image size; 

ToImagePPI - The file is scaled by the PPI of the image. This keep the physical dimensions the same.
        """
        pass
    def scalingFilter (self  )  -> "str" :
        """
    scalingFilter returns the filter with which the file referenced is scaled.
        """
        pass
class Extension(QObject):
    """
    An Extension is the base for classes that extend Krita. An Extension is loaded on startup, when the setup() method will be executed.
The extension instance should be added to the Krita Application object using Krita.instance().addViewExtension or Application.addViewExtension or Scripter.addViewExtension.
Example:
importsys
fromPyQt5.QtGuiimport*
fromPyQt5.QtWidgetsimport*
fromkritaimport*
classHelloExtension(Extension):
def__init__(self,parent):
super().__init__(parent)
defhello(self):
QMessageBox.information(QWidget(),"Test","Hello!ThisisKrita"+Application.version())
defsetup(self):
qDebug("HelloSetup")
defcreateActions(self,window)
action=window.createAction("hello")
action.triggered.connect(self.hello)
Scripter.addExtension(HelloExtension(Krita.instance()))
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    Create a new extension. The extension will be owned by parent.
        """
        pass
    def setup (self  )  :
        """
    Override this function to setup your Extension. You can use it to integrate with the Krita application instance.
        """
        pass
    def createActions (self,  window: "Window" )  :
        """
    
        """
        pass
class FilterLayer(Node):
    """
    The FilterLayer class A filter layer will, when compositing, take the composited image up to the point of the location of the filter layer in the stack, create a copy and apply a filter.This means you can use blending modes on the filter layers, which will be used to blend the filtered image with the original.
Similarly, you can activate things like alpha inheritance, or you can set grayscale pixeldata on the filter layer to act as a mask.
Filter layers can be animated.
    """
    def type (self  )  -> "str" :
        """
    type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks."filterlayer"
        """
        pass
    def setFilter (self,  filter: "Filter" )  :
        """
    
        """
        pass
    def filter (self  )  -> "Filter" :
        """
    
        """
        pass
class InfoObject(QObject):
    """
    InfoObject wrap a properties map. These maps can be used to set the configuration for filters.
    """
    def __init__ (self,  parent: "QObject" = None )  :
        """
    Create a new, empty InfoObject.
        """
        pass
    def properties (self  )  -> "dict[ str, QVariant ]" :
        """
    Return all properties this InfoObject manages.
        """
        pass
    def setProperties (self,  propertyMap: "dict[ str, QVariant ]" )  :
        """
    Add all properties in the propertyMap to this InfoObject
        """
        pass
    def setProperty (self,  key: "str", value: "QVariant" )  :
        """
    set the property identified by key to value 
If you want create a property that represents a color, you can use a QColor or hex string, as defined in https://doc.qt.io/qt-5/qcolor.html#setNamedColor.
        """
        pass
    def property (self,  key: "str" )  -> "QVariant" :
        """
    return the value for the property identified by key, or None if there is no such key.
        """
        pass
class PresetChooser(KisPresetChooser):
    """
    The PresetChooser widget wraps the KisPresetChooser widget. The widget provides for selecting brush presets. It has a tagging bar and a filter field. It is not automatically synchronized with the currently selected preset in the current Windows.
    """
    def __init__ (self,  parent: "QWidget" = 0 )  :
        """
    
        """
        pass
    def setCurrentPreset (self,  resource: "Resource" )  :
        """
    Make the given preset active.
        """
        pass
    def currentPreset (self  )  -> "Resource" :
        """
    a Resource wrapper around the currently selected preset.
        """
        pass