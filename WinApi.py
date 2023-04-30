import ctypes
import win32con #part of pywin32

# Win32 Kernel32 API
api = ctypes.windll.kernel32

# Map Functions
CreateToolhelp32Snapshot = api.CreateToolhelp32Snapshot
OpenProcess = api.OpenProcess
CloseHandle = api.CloseHandle
VirtualProtectEx = api.VirtualProtectEx
WriteProcessMemory = api.WriteProcessMemory
ReadProcessMemory = api.ReadProcessMemory
Module32First = api.Module32First
Module32Next = api.Module32Next
Process32First = api.Process32First
Process32Next = api.Process32Next

# Constants & Structures
PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS
PAGE_EXECUTE_READWRITE = win32con.PAGE_EXECUTE_READWRITE
TH32CS_SNAPPROCESS = 0x2
TH32CS_SNAPMODULE = 0x8
TH32CS_SNAPMODULE32 = 0x10
INVALID_HANDLE_VALUE = -1

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [('dwSize' , ctypes.wintypes.DWORD),
                ('cntUsage' , ctypes.wintypes.DWORD),
                ('th32ProcessID', ctypes.wintypes.DWORD),
                ('th32DefaultHeapID', ctypes.POINTER(ctypes.wintypes.ULONG)),
                ('th32ModuleID', ctypes.wintypes.DWORD),
                ('cntThreads', ctypes.wintypes.DWORD),
                ('th32ParentProcessID', ctypes.wintypes.DWORD),
                ('pcPriClassBase', ctypes.wintypes.LONG),
                ('dwFlags', ctypes.wintypes.DWORD),
                ('szExeFile', ctypes.c_char * 260)]

class MODULEENTRY32(ctypes.Structure):
    _fields_ = [('dwSize', ctypes.wintypes.DWORD),
                ('th32ModuleID', ctypes.wintypes.DWORD),
                ('th32ProcessID', ctypes.wintypes.DWORD),
                ('GlblcntUsage', ctypes.wintypes.DWORD),
                ('ProccntUsage', ctypes.wintypes.DWORD),
                ('modBaseAddr', ctypes.POINTER(ctypes.wintypes.BYTE)),
                ('modBaseSize', ctypes.wintypes.DWORD),
                ('hModule', ctypes.wintypes.HMODULE),
                ('szModule', ctypes.c_char * 256),
                ('szExePath', ctypes.c_char * 260)]