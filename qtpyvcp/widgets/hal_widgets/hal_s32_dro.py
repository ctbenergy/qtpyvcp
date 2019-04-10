"""
HAL s32 DRO
-----------

Label for displaying `s32` HAL pin values.

Generated HAL Pins
++++++++++++++++++

========================= ========= =========
HAL Pin Name              Type      Direction
========================= ========= =========
qtpyvcp.s32-dro.enable    s32       in
qtpyvcp.s32-dro.in        s32       in
========================= ========= =========
"""

from qtpy.QtWidgets import QLabel
from qtpy.QtCore import Property

from qtpyvcp import hal
from qtpyvcp.widgets import HALWidget


class Hals32Dro(QLabel, HALWidget):
    """HAL s32 DRO"""
    def __init__(self, parent=None):
        super(Hals32Dro, self).__init__(parent)

        self._in_pin = None
        self._enable_pin = None
        self._format = "%6d"

        self.setValue(0)

    def setValue(self, value):
        self.setText(self._format % value)

    @Property(str)
    def numberFormat(self):
        return self._format

    @numberFormat.setter
    def numberFormat(self, fmt):
        self._format = fmt
        self.setValue(0)

    def initialize(self):
        comp = hal.COMPONENTS['qtpyvcp']
        obj_name = str(self.objectName()).replace('_', '-')

        # add s32-dro.enable HAL pin
        self._enable_pin = comp.addPin(obj_name + ".enable", "bit", "in")
        self._enable_pin.value = self.isEnabled()
        self._enable_pin.valueChanged.connect(self.setEnabled)

        # add s32-dro.in HAL pin
        self._in_pin = comp.addPin(obj_name + ".in", "s32", "in")
        self.setValue(self._in_pin.value)
        self._in_pin.valueChanged.connect(self.setValue)