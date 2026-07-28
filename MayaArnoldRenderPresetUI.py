from PySide2 import QtWidgets, QtCore

class ArnoldRenderSettings(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(ArnoldRenderSettings, self).__init__(parent)

        self.setWindowTitle("Arnold Render Presets")
        self.resize(420, 420)

        self.createWidgets()
        self.createLayout()
        self.createConnections()

    def createWidgets(self):

        self.lowRadio = QtWidgets.QRadioButton("Low (LightingFirstPass/IPR)")
        self.mediumRadio = QtWidgets.QRadioButton("Medium (LightingWIP)")
        self.highRadio = QtWidgets.QRadioButton("High (LightingFinal)")

        self.mediumRadio.setChecked(True)

        self.aaSpin = QtWidgets.QSpinBox()
        self.diffuseSpin = QtWidgets.QSpinBox()
        self.specularSpin = QtWidgets.QSpinBox()
        self.transSpin = QtWidgets.QSpinBox()
        self.sssSpin = QtWidgets.QSpinBox()
        self.volumeSpin = QtWidgets.QSpinBox()

        for widget in [
            self.aaSpin,
            self.diffuseSpin,
            self.specularSpin,
            self.transSpin,
            self.sssSpin,
            self.volumeSpin
        ]:
            widget.setRange(0,10)

        self.adaptiveCheck = QtWidgets.QCheckBox("Enable Adaptive Sampling")
        self.adaptiveCheck.setChecked(True)

        self.thresholdSpin = QtWidgets.QDoubleSpinBox()
        self.thresholdSpin.setDecimals(4)
        self.thresholdSpin.setRange(0.0001,1.0)
        self.thresholdSpin.setSingleStep(0.001)

        self.applyButton = QtWidgets.QPushButton("Apply Preset")
        self.closeButton = QtWidgets.QPushButton("Close")

    def createLayout(self):

        layout = QtWidgets.QVBoxLayout(self)

        presetGroup = QtWidgets.QGroupBox("Render Presets")
        presetLayout = QtWidgets.QVBoxLayout()

        presetLayout.addWidget(self.lowRadio)
        presetLayout.addWidget(self.mediumRadio)
        presetLayout.addWidget(self.highRadio)

        presetGroup.setLayout(presetLayout)

        layout.addWidget(presetGroup)

        form = QtWidgets.QFormLayout()

        form.addRow("Camera AA", self.aaSpin)
        form.addRow("Diffuse", self.diffuseSpin)
        form.addRow("Specular", self.specularSpin)
        form.addRow("Transmission", self.transSpin)
        form.addRow("SSS", self.sssSpin)
        form.addRow("Volume", self.volumeSpin)

        layout.addLayout(form)

        layout.addWidget(self.adaptiveCheck)

        layout.addWidget(QtWidgets.QLabel("Adaptive Threshold"))

        layout.addWidget(self.thresholdSpin)

        buttonLayout = QtWidgets.QHBoxLayout()

        buttonLayout.addWidget(self.applyButton)
        buttonLayout.addWidget(self.closeButton)

        layout.addLayout(buttonLayout)

    def createConnections(self):

        self.lowRadio.toggled.connect(self.loadPreset)
        self.mediumRadio.toggled.connect(self.loadPreset)
        self.highRadio.toggled.connect(self.loadPreset)

        self.applyButton.clicked.connect(self.applySettings)   # <-- Add this

        self.closeButton.clicked.connect(self.close)

        self.loadPreset()

    def loadPreset(self):

        if self.lowRadio.isChecked():

            self.aaSpin.setValue(3)
            self.diffuseSpin.setValue(1)
            self.specularSpin.setValue(1)
            self.transSpin.setValue(0)
            self.sssSpin.setValue(0)
            self.volumeSpin.setValue(0)
            self.thresholdSpin.setValue(0.05)

        elif self.mediumRadio.isChecked():

            self.aaSpin.setValue(4)
            self.diffuseSpin.setValue(2)
            self.specularSpin.setValue(2)
            self.transSpin.setValue(2)
            self.sssSpin.setValue(2)
            self.volumeSpin.setValue(0)
            self.thresholdSpin.setValue(0.015)

        elif self.highRadio.isChecked():

            self.aaSpin.setValue(5)
            self.diffuseSpin.setValue(3)
            self.specularSpin.setValue(3)
            self.transSpin.setValue(3)
            self.sssSpin.setValue(5)
            self.volumeSpin.setValue(2)
            self.thresholdSpin.setValue(0.005)

    def applySettings(self):

        cmds.setAttr("defaultArnoldRenderOptions.AASamples",
                 self.aaSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseSamples",
                 self.diffuseSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.GISpecularSamples",
                 self.specularSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.GITransmissionSamples",
                 self.transSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.GISssSamples",
                 self.sssSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.GIVolumeSamples",
                 self.volumeSpin.value())

        cmds.setAttr("defaultArnoldRenderOptions.enableAdaptiveSampling",
                 self.adaptiveCheck.isChecked())

        cmds.setAttr("defaultArnoldRenderOptions.AAAdaptiveThreshold",
                 self.thresholdSpin.value())

        cmds.inViewMessage(
            amg='<hl>Arnold Render Settings Applied</hl>',
            pos='midCenter',
            fade=True
        )        


try:
    arnoldUI.close()
    arnoldUI.deleteLater()
except:
    pass

arnoldUI = ArnoldRenderSettings()
arnoldUI.show()
