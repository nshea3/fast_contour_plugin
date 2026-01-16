"""
Fast Contour QGIS Plugin - Main Plugin Class
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsProcessingAlgorithm, QgsApplication
import os.path


class FastContourPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        from .fast_contour_provider import FastContourProvider
        self.provider = FastContourProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.initProcessing()

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        if self.provider:
            QgsApplication.processingRegistry().removeProvider(self.provider)
