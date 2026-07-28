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


lights = cmds.ls(light=True)

for light in lights :
  cmds.setAttr("[light].aiSamples", 2)
  cmds.setAttr("[light].exposure", 8)
