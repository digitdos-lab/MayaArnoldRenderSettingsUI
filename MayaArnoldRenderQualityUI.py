import os

import maya.cmds as cmds

from maya import OpenMayaUI

from PySide2 import QtWidgets
from Pysode2 import QtCore

from shiboken2 import wrapInstance

cmds.setAttr("defaultArnoldRenderOptions.AASamples", 4)
cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseSamples", 2)
cmds.setAttr("defaultArnoldRenderOptions.GISpeculaSamples", 2)
cmds.setAttr("defaultArnoldRenderOptions.GITransmission", 2)
cmds.setAttr("defaultArnoldRenderOptions.GISssSamples", 5)
cmds.setAttr("defaultArnoldRenderOptions.GIVolumeSamples", 2)


light_shapes = cmds.ls(light=True)

for lgt in lights_shapes :
  cmds.setAttr("[lgt].aiSamples", 2)
  cmds.setAttr("[lgt].exposure", 8)
