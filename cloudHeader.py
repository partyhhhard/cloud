from ctypes import *


class cloudRequestHeader(Structure):
    _fields_: [
        ("Signature", c_uint32),
        ("ProtocolVerMinor", c_uint8),
        ("ProtocolVerMajor", c_uint8),
        ("Flags", c_uint16),
        ("CodePage", c_uint32),
        ("CPUID", c_buffer(12)),
        ("Size", c_uint32),
        ("CRC16", c_uint16),
    ]