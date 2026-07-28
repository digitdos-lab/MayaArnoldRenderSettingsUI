import os

import maya.cmds as cmds

from PySide2 import QtWidgets
from Pysode2 import QtCore

from shiboken2 import wrapInstance

cmds.SetAttr("defaultArnoldRenderOptions.AASamples", 5)
cmds.SetAttr("defaultArnoldRenderOptions.GIDiffuseSamples", 2)
cmds.SetAttr("defaultArnoldRenderOptions.GISpeculaSamples", 2)
cmds.SetAttr("defaultArnoldRenderOptions.GITransmission", 2)
cmds.SetAttr("defaultArnoldRenderOptions.GISssSamples", 5)
cmds.SetAttr("defaultArnoldRenderOptions.GIVolumeSamples", 2)
