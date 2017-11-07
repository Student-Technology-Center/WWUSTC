from enum import Enum
import platform

class SystemType(Enum):
    LINUX = 1
    WINDOWS = 2

def getSystem():
    return {
        'Linux' : SystemType.LINUX,
        'Windows' : SystemType.WINDOWS,
    }.get(platform.system(), SystemType.LINUX)