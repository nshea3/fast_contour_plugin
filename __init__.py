"""
Fast Contour QGIS Plugin
High-performance contour generation using contourpy
"""

def classFactory(iface):
    from .fast_contour_plugin import FastContourPlugin
    return FastContourPlugin(iface)
