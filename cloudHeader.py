from ctypes import *

CLOUD_HEADER_SIGNATURE = 0xA242242A

SENSORS_SEND_TIMEOUT_MS = (5 * 1000)
SETTINGS_SEND_TIMEOUT_MS = (300 * 1000)

DIRECTORY_TYPE_PROFILES = 1
DIRECTORY_TYPE_FIRMWARE = 2
DIRECTORY_TYPE_POLYGON_ONLINE_PRINT_QUEUE = 3

DIR_REQUEST_ITEMS_QTY_MAX = 8

CLOUD_PROTOCOL_VER_MAJOR = 0
CLOUD_PROTOCOL_VER_MINOR = 3
CLOUD_DOCUMENT_CURRENT_VERSION = 1
CLOUD_TASK_PORT_UDP_FROM = (5000 + TASK_ID_CLOUD_CONNECT)
CLOUD_SERVER_IP_ADDRESS = "3.124.248.139"
CLOUD_SERVER_PORT_UDP = 4000
CLOUD_SERVER_ANSWER_SIZE_MAX = 512
CODEPAGE_DEFAULT = 1251

CLOUD_HEADER_FLAG_DATA_EXIST = (1 << 2)
CLOUD_HEADER_FLAG_WAIT_ANSWER = (1 << 5)

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
    def __init__( self, sig, vermin, vermaj, fl, cp, cpuid, sz, crc ):
        Signature = sig
        ProtocolVerMinor = vermin
        ProtocolVerMajor = vermaj
        Flags = fl
        CodePage = cp
        CPUID = cpuid
        Size = sz
        CRC16 = crc