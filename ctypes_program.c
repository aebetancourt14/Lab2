
import ctypes
_libInC = ctypes.CDLL('./libMyLib.so')
print(_libInC.myAdd(3, 5))
def addC(a,b):
    return _libInC.myAdd(a,b)
print(addC(10, 202))
def myMultiply(a,b):
    return _libInC.myMultiply(a,b)
print(myMultiply(10, 2))