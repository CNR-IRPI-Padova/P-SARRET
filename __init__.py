from .psarret import psarretPlugin

def classFactory(iface):
    return psarretPlugin(iface)
