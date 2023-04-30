import ctypes
import WinApi as winapi


def FindDMAAddy(hProc, base, offsets, arch=64):
    size=8
    if (arch == 32): size = 4

    address = ctypes.c_uint64(base)

    for offset in offsets:
        winapi.ReadProcessMemory(hProc, address, ctypes.byref(address), size, 0)
        address = ctypes.c_uint64(address.value + offset)

    return(address.value)