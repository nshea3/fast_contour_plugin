"""
Fast Contour Processing Provider
"""

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon
import os
from .fast_contour_algorithm import FastContourAlgorithm


class FastContourProvider(QgsProcessingProvider):
    """Processing provider for Fast Contour algorithms."""

    def __init__(self):
        super().__init__()

    def loadAlgorithms(self):
        """Load all algorithms belonging to this provider."""
        self.addAlgorithm(FastContourAlgorithm())

    def id(self):
        """Unique provider id."""
        return 'fastcontour'

    def name(self):
        """Human-friendly provider name."""
        return 'Fast Contour'

    def icon(self):
        """Provider icon."""
        return QgsProcessingProvider.icon(self)

    def longName(self):
        """Longer version of the provider name."""
        return 'Fast Contour Generation'
