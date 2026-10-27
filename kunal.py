#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PSYCO TOOL SUITE - PAK Tool
WHITE + GREY EDITION
+ BUILD NEW PAK (CSV)
+ MINI SKIN TOOL
+ ZSDIC SKIN TOOL
+ LUA TOOL
+ BLACK TOOL (UE4)
"""

# =====================================================================
# IMPORTS
# =====================================================================

from collections import Counter
import itertools as it
import math
import struct
import subprocess
import os
import shutil
import os
import sys
import uuid
import hashlib
import platform
import subprocess
import requests
import base64
import zlib
import ctypes
import re as _ptre
import marshal as _ptmarshal
import dis as _ptdis
import ast as _ptast
from io import StringIO as _ptSIO
from dataclasses import dataclass
from functools import lru_cache
from pathlib import PurePath, Path
from typing import List, Dict, Tuple, Optional, Any
import time
import json
import csv
import zipfile
import stat
import bisect
from collections import defaultdict
import tempfile
import random
import string
from datetime import datetime, timedelta
import getpass
import socket
import secrets

try:
    import pytz
except ImportError:
    os.system("pip install pytz")
    import pytz

try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

try:
    import gmalg
except ImportError:
    os.system("pip install gmalg")
    import gmalg

try:
    from Crypto.Cipher import AES
    from Crypto.Cipher.AES import MODE_CBC
    from Crypto.Hash import SHA1
    from Crypto.Util.Padding import unpad, pad
except ImportError:
    os.system("pip install pycryptodome")
    from Crypto.Cipher import AES
    from Crypto.Cipher.AES import MODE_CBC
    from Crypto.Hash import SHA1
    from Crypto.Util.Padding import unpad, pad

try:
    from zstandard import ZstdDecompressor, ZstdCompressionDict, DICT_TYPE_AUTO, ZstdCompressor
except ImportError:
    os.system("pip install zstandard")
    from zstandard import ZstdDecompressor, ZstdCompressionDict, DICT_TYPE_AUTO, ZstdCompressor

try:
    import colorama
    from termcolor import colored
    colorama.init(autoreset=True)
except ImportError:
    os.system("pip install colorama termcolor")
    import colorama
    from termcolor import colored
    colorama.init(autoreset=True)

try:
    from rich.console import Console, Group
    from rich.panel import Panel
    from rich.progress import (
        Progress, SpinnerColumn, TextColumn, BarColumn,
        TaskProgressColumn, TimeElapsedColumn, TimeRemainingColumn,
        TransferSpeedColumn,
    )
    from rich.table import Table
    from rich import print as rprint
    from rich.markup import escape
    from rich.text import Text
    from rich.align import Align
    from rich.box import HEAVY_EDGE, ROUNDED, DOUBLE_EDGE, HEAVY, SIMPLE, SQUARE
    from rich.live import Live
    from rich.layout import Layout
    from rich.columns import Columns
    from rich.style import Style
    from rich.padding import Padding
    from rich.prompt import Prompt, Confirm
except ImportError:
    os.system("pip install rich")
    from rich.console import Console, Group
    from rich.panel import Panel
    from rich.progress import (
        Progress, SpinnerColumn, TextColumn, BarColumn,
        TaskProgressColumn, TimeElapsedColumn, TimeRemainingColumn,
        TransferSpeedColumn,
    )
    from rich.table import Table
    from rich import print as rprint
    from rich.markup import escape
    from rich.text import Text
    from rich.align import Align
    from rich.box import HEAVY_EDGE, ROUNDED, DOUBLE_EDGE, HEAVY, SIMPLE, SQUARE
    from rich.live import Live
    from rich.layout import Layout
    from rich.columns import Columns
    from rich.style import Style
    from rich.padding import Padding
    from rich.prompt import Prompt, Confirm

console = Console()
zsdic_console = Console()


# =====================================================================
# UNIFIED COLOUR PALETTE (Cyber Neon Edition)
# =====================================================================

# Ensure DC_HIGHLIGHT is always available as string
DC_HIGHLIGHT = "#00FFCC"
DC_TEXT = "#FFFFFF"
DC_DIM = "#7A7A9A"
DC_BORDER = "#3A3A5A"
DC_RED = "#FF3366"
DC_ORANGE = "#FFAA00"
DC_GREEN = "#FFFFFF"
DC_CYAN = "#00FFCC"
DC_MAGENTA = "#F5F5F5"
DC_ACCENT = "#00FFCC"
SUCCESS = "#00FFCC"
ERROR = "#FF3366"
WARNING = "#FFAA00"
DC_BG = "#000000"
DC_BG_MID = "#1A1A1A"

CURRENT_SESSION_BANNER = "KUNALYT0 TOOL"
CURRENT_SESSION_COLOR = "white"

BASE_DIR_NAME = "KUNALYT0"


# =====================================================================
# CONSTANTS
# =====================================================================

ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
ZUC_IV = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

RSA_MOD_1 = bytes.fromhex('CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
RSA_MOD_2 = bytes.fromhex('7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

SIMPLE1_DECRYPT_KEY = 121
SIMPLE2_DECRYPT_KEY = bytes.fromhex('E55B4ED1')
SIMPLE2_BLOCK_SIZE = 16

SM4_SECRET_4 = 'eb691efea914241317a8'
SM4_SECRET_2 = 'Q0hVTKey$as*1ZFlQCiA'
SM4_SECRET_NEW = [
    'xG2qW5lP7lV2iN5fN5pG', 'xT1cJ6dL5wC0kK1rB4dK', 'qC4jS5bZ6fL5xE6nD4zA',
    'gD4jQ2aL3bS3lC3xT0iW', 'xU1yQ8wE9zY3gZ3bT5aE', 'uQ3cO2dX7xY4xU7gH7iS',
    'gW1fR0jK6wQ4oN0oK1kZ', 'aJ4pV7iZ7pU4wP2aC2cZ', 'cX6jT3cM2oT3vK0kJ1qN',
    'iT2vS0cS6yT6cZ1sE1lO', 'hM1pH9iY8wM9hT4lN5uJ', 'kG6bC8jK0fL0dE4sH4mL',
    'dB6lB3vE0eZ8wM8rI0aC', 'tP7sP7nI9rA2vQ4cV5yQ', 'aT0cL1yN4pT3sZ7eM2vY',
    'uV6fU8fC9zN3mP5dH8mN', 'rT6aQ6oZ1yM0gO5tO1aN', 'jU5bH7lQ0fM9hK2kI0oF',
    'iQ0eM0mJ7uT0kV6kL5zY', 'fO3kW1fE6eD0pU1kY7xK', 'rG0lR2rZ5vM6mW5lM1rR', 
]

EM_SIMPLE1 = 1
EM_SIMPLE2 = 16
EM_SM4_2 = 2
EM_SM4_4 = 4
EM_SM4_NEW_BASE = 31
EM_SM4_NEW_MASK = ~EM_SM4_NEW_BASE
EM_UNKNOWN_17 = 17

CM_NONE = 0
CM_ZLIB = 1
CM_ZSTD = 6
CM_ZSTD_DICT = 8
CM_MASK = 15

MAX_OVERFLOW_BYTES = 5

# Mini tool constants
mini_BLOCK_SIZE = 65536
zsdic_DEFAULT_MAX_NULLS = 40
zsdic_ENABLE_UTF16LE_ID_SCAN = False

# Global session variables
SESSION_USER = "VIP USER"
SESSION_KEY = "LOCAL-BYPASS"
SESSION_EXPIRY = "LIFETIME"
game_key = "BGMI"


# =====================================================================
# CSV URLs (for auto-download)
# =====================================================================

CSV_URLS = {
    "PUBG.csv": "https://raw.githubusercontent.com/sellacountvinay-creator/BGMI_CSV/main/PUBG.csv",
    "BGMI.csv": "https://raw.githubusercontent.com/sellacountvinay-creator/BGMI_CSV/main/BGMI.csv",
}


# =====================================================================
# KEYBOARD INPUT (Pause/Stop during Unpack)
# =====================================================================

def check_key_press():
    try:
        if sys.platform == 'win32':
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8', errors='ignore').lower()
        else:
            import select
            if select.select([sys.stdin], [], [], 0)[0]:
                return sys.stdin.read(1).lower()
    except Exception:
        pass
    return None


# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def to_fancy(text: str) -> str:
    """Convert to fancy unicode text (math bold)."""
    try:
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        fancy  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        trans_table = str.maketrans(normal, fancy)
        return str(text).translate(trans_table)
    except Exception:
        return str(text)


def get_banner_color() -> str:
    return DC_TEXT


def to_long_path(path) -> str:
    p = str(path)
    if os.name != "nt":
        return p
    if p.startswith("\\\\?\\"):
        return p
    p = os.path.abspath(p)
    if p.startswith("\\\\"):
        return "\\\\?\\UNC\\" + p[2:]
    return "\\\\?\\" + p


def open_long(path, mode='rb'):
    return open(to_long_path(path), mode)


def get_indian_time():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


def safe_input(prompt=''):
    clean = _ptre.sub(r'\[/?[^\[\]]*\]', '', prompt)
    try:
        return input(clean)
    except (EOFError, KeyboardInterrupt):
        return ""


def human_size(size):
    if size is None:
        return "N/A"
    size = int(size)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            if unit == 'B':
                return f'{size} B'
            return f'{size:.2f} {unit}'
        size /= 1024.0
    return f'{size:.2f} PB'


def get_real_device_model():
    try:
        if hasattr(sys, 'getandroidapilevel') or os.path.exists('/system/build.prop'):
            try:
                brand = subprocess.check_output(['getprop', 'ro.product.brand'], timeout=3).decode().strip().upper()
                model = subprocess.check_output(['getprop', 'ro.product.model'], timeout=3).decode().strip().upper()
                if brand and model:
                    return f"{brand} {model}" if brand not in model else model
            except Exception:
                pass
    except Exception:
        pass
    try:
        return socket.gethostname().upper()
    except Exception:
        return "UNKNOWN"


def get_hwid():
    try:
        android_id = subprocess.check_output(['settings', 'get', 'secure', 'android_id'], timeout=4).decode().strip()
        if android_id and android_id != "null":
            return hashlib.md5(android_id.encode()).hexdigest().upper()[:16]
    except Exception:
        pass
    try:
        hwid_file = os.path.expanduser("~/KAZUKI_hwid.key.txt")
        if os.path.exists(hwid_file):
            with open(hwid_file, "r") as f:
                return f.read().strip()
        else:
            new_hwid = hashlib.md5(uuid.uuid4().bytes).hexdigest().upper()[:16]
            with open(hwid_file, "w") as f:
                f.write(new_hwid)
            return new_hwid
    except Exception:
        return "UNKNOWN-DEVICE"


# =====================================================================
# END OF PART 1
# =====================================================================# =====================================================================
# PART 2 - SM4, READER, PAK INFO CLASSES
# =====================================================================

# =====================================================================
# SM4 ENCRYPTION
# =====================================================================

class SM4:
    _S_BOX = bytes([
        52, 102, 37, 116, 137, 120, 228, 169, 90, 65, 188, 122, 214, 22, 33, 35,
        77, 97, 218, 148, 155, 223, 19, 60, 105, 58, 49, 10, 95, 215, 153, 149,
        241, 174, 114, 61, 7, 96, 36, 182, 152, 238, 196, 162, 45, 136, 221, 141,
        4, 234, 187, 17, 202, 62, 93, 161, 246, 63, 176, 151, 128, 71, 43, 166,
        230, 247, 217, 177, 89, 192, 124, 190, 84, 40, 183, 126, 79, 248, 67, 110,
        160, 80, 14, 245, 144, 184, 251, 163, 123, 98, 25, 70, 3, 42, 185, 143,
        159, 119, 180, 91, 131, 135, 8, 235, 226, 30, 66, 240, 15, 232, 113, 106,
        117, 173, 85, 31, 181, 171, 51, 250, 127, 21, 189, 133, 216, 6, 104, 179,
        82, 48, 72, 11, 0, 237, 239, 178, 87, 142, 231, 108, 213, 229, 46, 83,
        130, 5, 249, 129, 244, 86, 191, 140, 75, 227, 219, 74, 145, 76, 44, 211,
        64, 41, 78, 32, 20, 54, 121, 9, 111, 209, 55, 224, 57, 12, 138, 146,
        56, 18, 53, 109, 225, 253, 147, 154, 23, 212, 201, 156, 107, 132, 38, 157,
        175, 118, 193, 158, 208, 150, 197, 203, 233, 115, 73, 210, 205, 100, 195, 199,
        1, 125, 243, 172, 252, 222, 164, 68, 50, 27, 194, 186, 28, 2, 198, 39,
        69, 139, 242, 24, 167, 16, 81, 29, 200, 207, 99, 255, 47, 13, 88, 206,
        101, 165, 220, 26, 59, 134, 254, 34, 92, 168, 94, 103, 170, 236, 112, 204
    ])
    _FK = [1184304796, 1270900830, 1493524870, 3164752158]
    _CK = [964907, 973793155, 2654690407, 2916866751, 2071233739, 1226140771, 3348805095, 2045549823, 388349611, 800627875, 612403927, 3721562911, 1195432523, 3150178931, 612053223, 2445162591, 67183755, 1174197155, 1393249511, 3331183455, 3822152747, 1332317203, 1804781383, 1990130463, 1282653851, 3376591251, 2910902311, 925872959, 332098219, 735840931, 396665415, 3588844719]

    @staticmethod
    def ROL32(x, n):
        return (x << n) & 0xFFFFFFFF | (x >> (32 - n))

    @staticmethod
    def _BS(X):
        return (SM4._S_BOX[X >> 24 & 255] << 24 |
                SM4._S_BOX[X >> 16 & 255] << 16 |
                SM4._S_BOX[X >> 8 & 255] << 8 |
                SM4._S_BOX[X & 255])

    @staticmethod
    def _T0(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X, 2) ^ SM4.ROL32(X, 10) ^ SM4.ROL32(X, 18) ^ SM4.ROL32(X, 24)

    @staticmethod
    def _T1(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X, 13) ^ SM4.ROL32(X, 23)

    @staticmethod
    def _key_expand(key: bytes, rkey: list):
        K0 = int.from_bytes(key[0:4], 'big') ^ SM4._FK[0]
        K1 = int.from_bytes(key[4:8], 'big') ^ SM4._FK[1]
        K2 = int.from_bytes(key[8:12], 'big') ^ SM4._FK[2]
        K3 = int.from_bytes(key[12:16], 'big') ^ SM4._FK[3]
        for i in range(0, 32, 4):
            K0 = K0 ^ SM4._T1(K1 ^ K2 ^ K3 ^ SM4._CK[i])
            rkey[i] = K0
            K1 = K1 ^ SM4._T1(K2 ^ K3 ^ K0 ^ SM4._CK[i + 1])
            rkey[i + 1] = K1
            K2 = K2 ^ SM4._T1(K3 ^ K0 ^ K1 ^ SM4._CK[i + 2])
            rkey[i + 2] = K2
            K3 = K3 ^ SM4._T1(K0 ^ K1 ^ K2 ^ SM4._CK[i + 3])
            rkey[i + 3] = K3

    @classmethod
    def key_length(cls): return 16

    @classmethod
    def block_length(cls): return 16

    def __init__(self, key: bytes):
        if len(key) != self.key_length():
            raise ValueError(f'Key must be {self.key_length()} bytes')
        self._key = key
        self._rkey = [0] * 32
        SM4._key_expand(self._key, self._rkey)
        self._block_buffer = bytearray()
        if not hasattr(SM4, '_T_TABLES'):
            SM4._T_TABLES = SM4._make_t_tables()

    def encrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f'Block must be {self.block_length()} bytes')
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], 'big')
        X1 = int.from_bytes(block[4:8], 'big')
        X2 = int.from_bytes(block[8:12], 'big')
        X3 = int.from_bytes(block[12:16], 'big')
        for i in range(0, 32, 4):
            X0 = X0 ^ SM4._T0(X1 ^ X2 ^ X3 ^ RK[i])
            X1 = X1 ^ SM4._T0(X2 ^ X3 ^ X0 ^ RK[i + 1])
            X2 = X2 ^ SM4._T0(X3 ^ X0 ^ X1 ^ RK[i + 2])
            X3 = X3 ^ SM4._T0(X0 ^ X1 ^ X2 ^ RK[i + 3])
        B = self._block_buffer; B.clear()
        B.extend(X3.to_bytes(4, 'big')); B.extend(X2.to_bytes(4, 'big'))
        B.extend(X1.to_bytes(4, 'big')); B.extend(X0.to_bytes(4, 'big'))
        return bytes(B)

    def decrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f'Block must be {self.block_length()} bytes')
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], 'big')
        X1 = int.from_bytes(block[4:8], 'big')
        X2 = int.from_bytes(block[8:12], 'big')
        X3 = int.from_bytes(block[12:16], 'big')
        for i in range(0, 32, 4):
            X0 = X0 ^ SM4._T0(X1 ^ X2 ^ X3 ^ RK[31 - i])
            X1 = X1 ^ SM4._T0(X2 ^ X3 ^ X0 ^ RK[30 - i])
            X2 = X2 ^ SM4._T0(X3 ^ X0 ^ X1 ^ RK[29 - i])
            X3 = X3 ^ SM4._T0(X0 ^ X1 ^ X2 ^ RK[28 - i])
        B = self._block_buffer; B.clear()
        B.extend(X3.to_bytes(4, 'big')); B.extend(X2.to_bytes(4, 'big'))
        B.extend(X1.to_bytes(4, 'big')); B.extend(X0.to_bytes(4, 'big'))
        return bytes(B)

    @classmethod
    def _make_t_tables(cls):
        S = cls._S_BOX
        def rol(x, n): return (x << n) & 0xFFFFFFFF | (x >> (32 - n))
        def L(y): return y ^ rol(y, 2) ^ rol(y, 10) ^ rol(y, 18) ^ rol(y, 24)
        T0 = [0] * 256
        T1 = [0] * 256
        T2 = [0] * 256
        T3 = [0] * 256
        for i in range(256):
            s = S[i]
            T0[i] = L(s << 24)
            T1[i] = L(s << 16)
            T2[i] = L(s << 8)
            T3[i] = L(s)
        return (T0, T1, T2, T3)

    def _bulk(self, data: bytes, rk) -> bytes:
        n = len(data)
        out = bytearray(n)
        T0, T1, T2, T3 = self._T_TABLES
        unpack_from = struct.unpack_from
        pack_into = struct.pack_into
        idx = 0
        while idx < n:
            X0, X1, X2, X3 = unpack_from('>IIII', data, idx)
            for i in range(0, 32, 4):
                t = X1 ^ X2 ^ X3 ^ rk[i]
                X0 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X2 ^ X3 ^ X0 ^ rk[i + 1]
                X1 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X3 ^ X0 ^ X1 ^ rk[i + 2]
                X2 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X0 ^ X1 ^ X2 ^ rk[i + 3]
                X3 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
            pack_into('>IIII', out, idx, X3, X2, X1, X0)
            idx += 16
        return bytes(out)

    def encrypt_bulk(self, data: bytes) -> bytes:
        lib = _load_fast_sm4()
        if lib is not None:
            data = bytes(data)
            n = len(data)
            inbuf = ctypes.create_string_buffer(data)
            outbuf = ctypes.create_string_buffer(n)
            lib.sm4_ecb(ctypes.create_string_buffer(self._key), inbuf, outbuf, n, 1)
            return outbuf.raw
        return self._bulk(data, self._rkey)

    def decrypt_bulk(self, data: bytes) -> bytes:
        lib = _load_fast_sm4()
        if lib is not None:
            data = bytes(data)
            n = len(data)
            inbuf = ctypes.create_string_buffer(data)
            outbuf = ctypes.create_string_buffer(n)
            lib.sm4_ecb(ctypes.create_string_buffer(self._key), inbuf, outbuf, n, 0)
            return outbuf.raw
        return self._bulk(data, self._rkey[::-1])


_FAST_SM4_LIB = None
_FAST_SM4_TRIED = False


def _sm4_c_source() -> str:
    sbox = SM4._S_BOX
    fk = SM4._FK
    ck = SM4._CK
    L = []
    L.append('// auto-generated fast SM4')
    L.append('#include <stdint.h>')
    L.append('#include <stddef.h>')
    L.append('static const uint8_t SBOX[256] = { ' + ', '.join(str(x) for x in sbox) + ' };')
    L.append('static const uint32_t FK[4] = { ' + ', '.join(hex(x) for x in fk) + ' };')
    L.append('static const uint32_t CK[32] = { ' + ', '.join(hex(x) for x in ck) + ' };')
    L.append('static inline uint32_t rotl(uint32_t x, int n){ return (x << n) | (x >> (32 - n)); }')
    L.append('static inline uint32_t load_be(const uint8_t* p){ return ((uint32_t)p[0]<<24)|((uint32_t)p[1]<<16)|((uint32_t)p[2]<<8)|(uint32_t)p[3]; }')
    L.append('static inline void store_be(uint8_t* p, uint32_t v){ p[0]=(uint8_t)(v>>24); p[1]=(uint8_t)(v>>16); p[2]=(uint8_t)(v>>8); p[3]=(uint8_t)v; }')
    L.append('static inline uint32_t sb(uint32_t x){ return ((uint32_t)SBOX[(x>>24)&0xff]<<24)|((uint32_t)SBOX[(x>>16)&0xff]<<16)|((uint32_t)SBOX[(x>>8)&0xff]<<8)|(uint32_t)SBOX[x&0xff]; }')
    L.append('static inline uint32_t t0(uint32_t x){ x = sb(x); return x ^ rotl(x,2) ^ rotl(x,10) ^ rotl(x,18) ^ rotl(x,24); }')
    L.append('static inline uint32_t t1(uint32_t x){ x = sb(x); return x ^ rotl(x,13) ^ rotl(x,23); }')
    L.append('static void expand(const uint8_t* key, uint32_t rk[32]){')
    L.append('    uint32_t k0 = load_be(key) ^ FK[0];')
    L.append('    uint32_t k1 = load_be(key+4) ^ FK[1];')
    L.append('    uint32_t k2 = load_be(key+8) ^ FK[2];')
    L.append('    uint32_t k3 = load_be(key+12) ^ FK[3];')
    L.append('    for (int i = 0; i < 32; i++){')
    L.append('        k0 ^= t1(k1 ^ k2 ^ k3 ^ CK[i]); rk[i] = k0;')
    L.append('        k1 ^= t1(k2 ^ k3 ^ k0 ^ CK[++i]); rk[i] = k1;')
    L.append('        k2 ^= t1(k3 ^ k0 ^ k1 ^ CK[++i]); rk[i] = k2;')
    L.append('        k3 ^= t1(k0 ^ k1 ^ k2 ^ CK[++i]); rk[i] = k3;')
    L.append('    }')
    L.append('}')
    L.append('static void crypt_block(const uint8_t* in, uint8_t* out, const uint32_t* rk){')
    L.append('    uint32_t x0 = load_be(in);')
    L.append('    uint32_t x1 = load_be(in+4);')
    L.append('    uint32_t x2 = load_be(in+8);')
    L.append('    uint32_t x3 = load_be(in+12);')
    L.append('    for (int i = 0; i < 32; i += 4){')
    L.append('        x0 ^= t0(x1 ^ x2 ^ x3 ^ rk[i]);')
    L.append('        x1 ^= t0(x2 ^ x3 ^ x0 ^ rk[i+1]);')
    L.append('        x2 ^= t0(x3 ^ x0 ^ x1 ^ rk[i+2]);')
    L.append('        x3 ^= t0(x0 ^ x1 ^ x2 ^ rk[i+3]);')
    L.append('    }')
    L.append('    store_be(out, x3); store_be(out+4, x2); store_be(out+8, x1); store_be(out+12, x0);')
    L.append('}')
    L.append('void sm4_ecb(const uint8_t* key, const uint8_t* in, uint8_t* out, size_t len, int encrypt){')
    L.append('    uint32_t rk[32];')
    L.append('    expand(key, rk);')
    L.append('    if (!encrypt){')
    L.append('        for (int i = 0; i < 16; i++){ uint32_t tmp = rk[i]; rk[i] = rk[31-i]; rk[31-i] = tmp; }')
    L.append('    }')
    L.append('    for (size_t off = 0; off < len; off += 16){ crypt_block(in + off, out + off, rk); }')
    L.append('}')
    return '\n'.join(L)


def _load_fast_sm4():
    global _FAST_SM4_LIB, _FAST_SM4_TRIED
    if _FAST_SM4_TRIED:
        return _FAST_SM4_LIB
    _FAST_SM4_TRIED = True
    try:
        tool_dir = Path(__file__).resolve().parent
        src_path = tool_dir / 'sm4_fast.c'
        so_path = tool_dir / 'sm4_fast.so'
        c_src = _sm4_c_source()
        if not src_path.exists() or src_path.read_text() != c_src:
            src_path.write_text(c_src)
        recompile = (not so_path.exists()) or (so_path.stat().st_mtime < src_path.stat().st_mtime)
        if recompile:
            for cc in ('gcc', 'cc', 'clang'):
                try:
                    r = subprocess.run([cc, '-O2', '-shared', '-fPIC', str(src_path), '-o', str(so_path)],
                                       capture_output=True, timeout=120)
                    if r.returncode == 0 and so_path.exists():
                        break
                except Exception:
                    continue
        if not so_path.exists():
            return None
        lib = ctypes.CDLL(str(so_path))
        lib.sm4_ecb.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
        lib.sm4_ecb.restype = None
        _FAST_SM4_LIB = lib
        return lib
    except Exception:
        return None


# =====================================================================
# MISC HELPERS
# =====================================================================

class Misc:
    @staticmethod
    def pad_to_n(data: bytes, n: int) -> bytes:
        assert n > 0
        padding = n - len(data) % n
        return data if padding == n else data + b'\x00' * padding

    @staticmethod
    def align_up(x: int, n: int) -> int:
        return (x + n - 1) // n * n


# =====================================================================
# READER
# =====================================================================

class Reader:
    def __init__(self, buffer, cursor=0):
        self._buffer = buffer
        self._cursor = cursor

    def u1(self, move_cursor=True): return self.unpack('B', move_cursor=move_cursor)[0]
    def u4(self, move_cursor=True): return self.unpack('<I', move_cursor=move_cursor)[0]
    def u8(self, move_cursor=True): return self.unpack('<Q', move_cursor=move_cursor)[0]
    def i1(self, move_cursor=True): return self.unpack('b', move_cursor=move_cursor)[0]
    def i4(self, move_cursor=True): return self.unpack('<i', move_cursor=move_cursor)[0]
    def i8(self, move_cursor=True): return self.unpack('<q', move_cursor=move_cursor)[0]
    def s(self, n: int, move_cursor=True): return self.unpack(f'{n}s', move_cursor=move_cursor)[0]

    def unpack(self, f: str, offset=0, move_cursor=True):
        x = struct.unpack_from(f, self._buffer, self._cursor + offset)
        if move_cursor:
            self._cursor += struct.calcsize(f)
        return x

    def string(self, move_cursor=True) -> str:
        length = self.i4(move_cursor=move_cursor)
        if length == 0:
            return str()
        assert length > 0
        offset = 0 if move_cursor else 4
        return self.unpack(f'{length}s', offset=offset, move_cursor=move_cursor)[0].rstrip(b'\x00').decode(errors='ignore')


# =====================================================================
# PAK INFO
# =====================================================================

class PakInfo:
    def __init__(self, buffer, keystream: List[int]):
        def decrypt_index_encrypted(x):
            return (x ^ keystream[3]) & 255

        def decrypt_magic(x):
            return x ^ keystream[2]

        def decrypt_index_hash(x):
            key = struct.pack('<5I', *keystream[4:][:5])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))

        def decrypt_index_size(x):
            return x ^ (keystream[10] << 32 | keystream[11])

        def decrypt_index_offset(x):
            return x ^ (keystream[0] << 32 | keystream[1])

        reader = Reader(buffer[-PakInfo._mem_size((-1)):])
        self.index_encrypted = decrypt_index_encrypted(reader.u1()) == 1
        self.magic = decrypt_magic(reader.u4())
        self.version = reader.u4()
        self.index_hash = decrypt_index_hash(reader.s(20)) if self.version >= 6 else bytes()
        self.index_size = decrypt_index_size(reader.u8())
        self.index_offset = decrypt_index_offset(reader.u8())
        if self.version <= 3:
            self.index_encrypted = False

    @staticmethod
    def _mem_size(_): return 45


class TencentPakInfo(PakInfo):
    def __init__(self, buffer, keystream: List[int]):
        def decrypt_unk(x):
            key = struct.pack('<8I', *keystream[7:][:8])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))

        def decrypt_stem_hash(x):
            return x ^ keystream[8]

        def decrypt_unk_hash(x):
            return x ^ keystream[9]

        super().__init__(buffer, keystream)
        reader = Reader(buffer[-TencentPakInfo._mem_size(self.version):])
        self.unk1 = decrypt_unk(reader.s(32)) if self.version >= 7 else bytes()
        self.packed_key = reader.s(256) if self.version >= 8 else bytes()
        self.packed_iv = reader.s(256) if self.version >= 8 else bytes()
        self.packed_index_hash = reader.s(256) if self.version >= 8 else bytes()
        self.stem_hash = decrypt_stem_hash(reader.u4()) if self.version >= 9 else 0
        self.unk2 = decrypt_unk_hash(reader.u4()) if self.version >= 9 else 0
        self.content_org_hash = reader.s(20) if self.version >= 12 else bytes()

    @staticmethod
    def _mem_size(version: int) -> int:
        s7 = 32 if version >= 7 else 0
        s8 = 768 if version >= 8 else 0
        s9 = 8 if version >= 9 else 0
        s12 = 20 if version >= 12 else 0
        return PakInfo._mem_size(version) + s7 + s8 + s9 + s12


# =====================================================================
# PAK COMPRESSED BLOCK & ENTRY
# =====================================================================

class PakCompressedBlock:
    def __init__(self, reader: Reader):
        self.start = reader.u8()
        self.end = reader.u8()


@dataclass
class TencentPakEntry:
    def __init__(self, reader: Reader, version: int):
        self.content_hash = reader.s(20)
        if version <= 1:
            _ = reader.u8()
        self.offset = reader.u8()
        self.uncompressed_size = reader.u8()
        self.compression_method = reader.u4() & CM_MASK
        self.size = reader.u8()
        self.unk1 = reader.u1() if version >= 5 else 0
        self.unk2 = reader.s(20) if version >= 5 else bytes()
        if self.compression_method != 0 and version >= 3:
            self.compressed_blocks = [PakCompressedBlock(reader) for _ in range(reader.u4())]
        else:
            self.compressed_blocks = []
        self.compression_block_size = reader.u4() if version >= 4 else 0
        self.encrypted = reader.u1() == 1 if version >= 4 else False
        self.encryption_method = reader.u4() if version >= 12 else 0
        self.index_new_sep = reader.u4() if version >= 12 else 0


# =====================================================================
# END OF PART 2
# =====================================================================# =====================================================================
# PART 3 - CRYPTO, COMPRESSION, TENCENT PAK FILE
# =====================================================================

# =====================================================================
# PAK CRYPTO
# =====================================================================

class PakCrypto:

    class _LCG:
        def __init__(self, seed: int):
            self.state = seed

        def next(self) -> int:
            MASK_32 = 4294967295
            MSB_1 = 2147483648

            def wrap(x):
                x &= MASK_32
                return x if not x & MSB_1 else (x + MSB_1 & MASK_32) - MSB_1

            x1 = wrap(1103515245 * self.state)
            self.state = wrap(x1 + 12345)
            x2 = wrap(x1 + 77880) if self.state < 0 else self.state
            return (x2 >> 16 & MASK_32) % 32767

    @staticmethod
    def zuc_keystream() -> List[int]:
        zuc = gmalg.ZUC(ZUC_KEY, ZUC_IV)
        return [struct.unpack('>I', zuc.generate())[0] for _ in range(16)]

    @staticmethod
    def _xorxor(buffer, x):
        return bytes((buffer[i] ^ x[i % len(x)] for i in range(len(buffer))))

    @staticmethod
    def _hashhash(buffer, n: int) -> bytes:
        result = bytes()
        for i in range(math.ceil(n / SHA1.digest_size)):
            result += SHA1.new(buffer).digest()
        if len(result) >= n:
            return result[:n]
        return result + b'\x00' * (n - len(result))

    @staticmethod
    def _meowmeow(buffer) -> bytes:
        def unpad(x):
            skip = 1 + next((i for i in range(len(x)) if x[i] != 0))
            return x[skip:]

        if len(buffer) < 43:
            return bytes()
        x1 = buffer[1:][:SHA1.digest_size]
        x2 = buffer[SHA1.digest_size + 1:]
        x1 = PakCrypto._xorxor(x1, PakCrypto._hashhash(x2, len(x1)))
        x2 = PakCrypto._xorxor(x2, PakCrypto._hashhash(x1, len(x2)))
        part1, m = (x2[:SHA1.digest_size], x2[SHA1.digest_size:])
        if part1 != SHA1.new(b'\x00' * SHA1.digest_size).digest():
            return bytes()
        return unpad(m)

    @staticmethod
    def rsa_extract(signature: bytes, modulus: bytes) -> bytes:
        c = int.from_bytes(signature, 'little')
        n = int.from_bytes(modulus, 'little')
        e = 65537
        m = pow(c, e, n).to_bytes(256, 'little').rstrip(b'\x00')
        return PakCrypto._meowmeow(Misc.pad_to_n(m, 4))

    @staticmethod
    def _decrypt_simple1(ciphertext) -> bytes:
        return bytes((x ^ SIMPLE1_DECRYPT_KEY for x in ciphertext))

    @staticmethod
    def _decrypt_simple2(ciphertext) -> bytes:
        class RollingKey:
            def __init__(self, v):
                self._value = v

            def update(self, x):
                self._value ^= x
                return self._value

        assert len(ciphertext) % SIMPLE2_BLOCK_SIZE == 0
        initial_key, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
        rk = RollingKey(initial_key)
        plaintext = (struct.pack('<I', rk.update(x)) for x in struct.unpack(f'<{len(ciphertext)//4}I', ciphertext))
        return bytes(it.chain.from_iterable(plaintext))

    @staticmethod
    @lru_cache(maxsize=128)
    def _derive_sm4_key(file_path: PurePath, encryption_method: int) -> bytes:
        part1 = file_path.stem.lower()
        if encryption_method == EM_SM4_2:
            secret = SM4_SECRET_2
        elif encryption_method == EM_SM4_4:
            secret = SM4_SECRET_4
        elif encryption_method == 52:
            # Specific override for Type 52 found in mini_obbzsdic_obb.pak
            secret = f'fO3kW1fE6eD0pU1kY7xK{encryption_method}'
        else:
            index = (encryption_method - EM_SM4_NEW_BASE) % len(SM4_SECRET_NEW)
            secret = f'{SM4_SECRET_NEW[index]}{encryption_method}'
            
        return SHA1.new(str(part1 + secret).encode()).digest()[:SM4.key_length()]

    @staticmethod
    @lru_cache(maxsize=128)
    def _sm4_context_for_key(key: bytes) -> SM4:
        return SM4(key)

    @staticmethod
    def _decrypt_sm4(ciphertext, file_path, encryption_method) -> bytes:
        assert len(ciphertext) % SM4.block_length() == 0
        key = PakCrypto._derive_sm4_key(file_path, encryption_method)
        return PakCrypto._sm4_context_for_key(key).decrypt_bulk(ciphertext)

    @staticmethod
    def decrypt_index(ciphertext, pak_info):
        if pak_info.version > 7:
            key = PakCrypto.rsa_extract(pak_info.packed_key, RSA_MOD_1)
            iv = PakCrypto.rsa_extract(pak_info.packed_iv, RSA_MOD_1)
            assert len(key) == 32 and len(iv) == 32
            aes = AES.new(key, MODE_CBC, iv[:16])
            return unpad(aes.decrypt(ciphertext), AES.block_size)
        return bytes(PakCrypto._decrypt_simple1(ciphertext))

    @staticmethod
    def _is_simple1_method(m): return m == EM_SIMPLE1

    @staticmethod
    def _is_simple2_method(m): return m == EM_SIMPLE2 or m == 17

    @staticmethod
    def _is_sm4_method(m):
        return m == EM_SM4_2 or m == EM_SM4_4 or m & EM_SM4_NEW_MASK != 0

    @staticmethod
    def align_encrypted_content_size(n, m):
        if PakCrypto._is_simple2_method(m):
            return Misc.align_up(n, SIMPLE2_BLOCK_SIZE)
        if PakCrypto._is_sm4_method(m):
            return Misc.align_up(n, SM4.block_length())
        return n

    @staticmethod
    def decrypt_block(ciphertext, file, encryption_method):
        if PakCrypto._is_simple1_method(encryption_method):
            return PakCrypto._decrypt_simple1(ciphertext)
        if PakCrypto._is_simple2_method(encryption_method):
            return PakCrypto._decrypt_simple2(ciphertext)
        if PakCrypto._is_sm4_method(encryption_method):
            return PakCrypto._decrypt_sm4(ciphertext, file, encryption_method)
        raise ValueError(f'Unknown encryption method: {encryption_method}')

    @staticmethod
    @lru_cache(maxsize=33)
    def generate_block_indices(n, encryption_method):
        if not PakCrypto._is_sm4_method(encryption_method):
            return list(range(n))
        perm = []
        lcg = PakCrypto._LCG(n)
        while len(perm) != n:
            x = lcg.next() % n
            if x not in perm:
                perm.append(x)
        inv = [0] * len(perm)
        for i, x in enumerate(perm):
            inv[x] = i
        return inv


# =====================================================================
# PAK COMPRESSION
# =====================================================================

class PakCompression:

    @staticmethod
    @lru_cache(maxsize=33)
    def _zstd_decompressor(d):
        return ZstdDecompressor(d)

    @staticmethod
    def zstd_dictionary(d):
        return ZstdCompressionDict(d, DICT_TYPE_AUTO)

    @staticmethod
    def decompress_block(block, dict, compression_method):
        if compression_method == CM_ZLIB:
            try:
                return zlib.decompress(block)
            except zlib.error:
                return block
        if compression_method in (CM_ZSTD, CM_ZSTD_DICT):
            if compression_method != CM_ZSTD_DICT:
                dict = None
            return PakCompression._zstd_decompressor(dict).decompress(block)
        raise ValueError(f'Unknown compression method: {compression_method}')


# =====================================================================
# TENCENT PAK FILE
# =====================================================================

class TencentPakFile:
    def __init__(self, file_path, is_od=False, silent=False):
        self._silent = silent
        self._file_path = file_path
        with open_long(file_path, 'rb') as f:
            self._file_content = memoryview(f.read())
        self._is_od = is_od
        self._mount_point = PurePath()
        self._is_zstd_with_dict = 'zsdic' in str(self._file_path)
        self._zstd_dict = None
        self._zstd_dict_entry = None
        self._files = []
        self._index = {}
        try:
            ks = PakCrypto.zuc_keystream()
        except Exception:
            ks = [0] * 16
        self._pak_info = TencentPakInfo(self._file_content, ks)
        self._verify_stem_hash()
        self._tencent_load_index()

    def _get_method_str(self, m, is_enc):
        if is_enc:
            if PakCrypto._is_simple1_method(m):
                return "SIMPLE1"
            if PakCrypto._is_simple2_method(m):
                return "SIMPLE2"
            if PakCrypto._is_sm4_method(m):
                return f"SM4 (Type {m})"
            return "NONE" if m == 0 else "UNKNOWN"
        if m == CM_NONE:
            return "NONE"
        if m == CM_ZLIB:
            return "ZLIB"
        if m == CM_ZSTD:
            return "ZSTD"
        if m == CM_ZSTD_DICT:
            return "ZSTD_DICT"
        return "UNKNOWN"

    def _verify_stem_hash(self):
        if not self._is_od and self._pak_info.version >= 9:
            try:
                assert self._pak_info.stem_hash == zlib.crc32(self._file_path.stem.encode('utf-32le'))
            except AssertionError:
                if not self._silent:
                    console.print(f"[bold {DC_ORANGE}]Warning: pak filename differs from original stem.[/]")

    def _tencent_load_index(self):
        raw_index = bytes(self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size])

        def _try_aes_decrypt(data, mod):
            try:
                key = PakCrypto.rsa_extract(self._pak_info.packed_key, mod)
                iv = PakCrypto.rsa_extract(self._pak_info.packed_iv, mod)
                if not key or not iv or len(key) < 16 or len(iv) < 16:
                    return None
                aes = AES.new(key, MODE_CBC, iv[:16])
                decrypted = aes.decrypt(data)
                try:
                    result = unpad(decrypted, AES.block_size)
                except Exception:
                    result = decrypted.rstrip(b'\x00')
                    if not result:
                        return None
                r = Reader(result)
                r.string()
                n = r.u4()
                if 0 <= n <= 200000:
                    return result
                return None
            except Exception:
                return None

        candidates = []

        if self._pak_info.index_encrypted:
            d = _try_aes_decrypt(raw_index, RSA_MOD_1)
            if d:
                candidates.append(d)
            d = _try_aes_decrypt(raw_index, RSA_MOD_2)
            if d:
                candidates.append(d)
            try:
                candidates.append(PakCrypto._decrypt_simple1(raw_index))
            except Exception:
                pass

        candidates.append(raw_index)

        for data in candidates:
            try:
                self._files = []
                self._index = {}
                self._load_index(data)
                if self._index:
                    return
            except Exception:
                continue

        self._files = []
        self._index = {}

    @staticmethod
    def _construct_mount_point(mp):
        result = PurePath()
        for part in PurePath(mp).parts:
            if part != '..':
                result /= part
        return result

    def _peek_content(self, offset, size, encryption_method):
        size = PakCrypto.align_encrypted_content_size(size, encryption_method)
        return self._file_content[offset:][:size]

    def _peek_block_content(self, block, encryption_method):
        size = PakCrypto.align_encrypted_content_size(block.end - block.start, encryption_method)
        return self._file_content[block.start:][:size]

    def _construct_zstd_dict(self, dict_entry):
        try:
            data = self._peek_content(dict_entry.offset, dict_entry.size, dict_entry.encryption_method)
            if dict_entry.encrypted:
                data = PakCrypto.decrypt_block(data, PurePath("zstddic"), dict_entry.encryption_method)
            reader = Reader(data)
            dict_size = reader.u8()
            _ = reader.u4()
            _ = reader.u4()
            dict_data = reader.s(dict_size)
            if ZstdCompressionDict:
                self._zstd_dict = ZstdCompressionDict(dict_data, DICT_TYPE_AUTO)
        except Exception as e:
            if not self._silent:
                console.print(f"[red]Dictionary Load Error: {e}[/red]")

    def _load_index(self, index_data):
        if self._pak_info.version <= 10:
            raise ValueError(f'Unsupported version: {self._pak_info.version}')
        reader = Reader(index_data)
        self._mount_point = self._construct_mount_point(reader.string())
        n_files = min(reader.u4(), 200000)
        self._files = [TencentPakEntry(reader, self._pak_info.version) for _ in range(n_files)]
        dirs_count = min(reader.u8(), 200000)
        for _ in range(dirs_count):
            dir_path = PurePath(reader.string())
            file_count = min(reader.u8(), 200000)
            e = {}
            for _ in range(file_count):
                name = reader.string()
                idx = reader.i4()
                mapped = ~idx
                if 0 <= mapped < len(self._files):
                    e[name] = self._files[mapped]
                else:
                    e[name] = None
            if self._is_zstd_with_dict and dir_path.name == 'zstddic':
                if e:
                    self._zstd_dict_entry = e[[*e.keys()][0]]
                    self._construct_zstd_dict(self._zstd_dict_entry)
                continue
            self._index.update({PurePath(dir_path): e})

    def _write_to_disk(self, file_path, entry):
        encryption_method = entry.encryption_method
        compression_method = entry.compression_method

        file_path = Path(*[str(p).replace('\x00', '') for p in Path(file_path).parts])
        parent_dir = file_path.parent
        os.makedirs(to_long_path(parent_dir), exist_ok=True)

        with open_long(file_path, 'wb') as file:
            if compression_method == CM_NONE:
                data = self._peek_content(entry.offset, entry.size, encryption_method)
                if entry.encrypted:
                    data = PakCrypto.decrypt_block(data, file_path, encryption_method)
                file.write(data[:entry.uncompressed_size])
                return

            if not entry.compressed_blocks:
                if entry.size:
                    data = self._peek_content(entry.offset, entry.size, encryption_method)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, file_path, encryption_method)
                    data = PakCompression.decompress_block(data, self._zstd_dict, compression_method)
                    file.write(data)
                return

            try:
                for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), encryption_method):
                    data = self._peek_block_content(entry.compressed_blocks[x], encryption_method)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, file_path, encryption_method)
                    data = PakCompression.decompress_block(data, self._zstd_dict, compression_method)
                    file.write(data)
            except Exception as exc:
                file.seek(0)
                file.truncate()
                raw = bytearray()
                for blk in entry.compressed_blocks:
                    raw += self._peek_block_content(blk, encryption_method)
                file.write(raw)

    def dump(self, out_path=None):
        """Extract with PAUSE (S) / STOP (B) live controls."""
        base_dir = Path("/storage/emulated/0/Documents/KUNALYT0/")
        base_dir.mkdir(parents=True, exist_ok=True)
        out_path = Path(out_path) if out_path else (base_dir / self._mount_point)
        out_path.mkdir(parents=True, exist_ok=True)
        total_files = sum(len(d) for d in self._index.values())
        if total_files == 0:
            console.print(Panel("[yellow]No files in PAK index.[/yellow]", border_style="yellow"))
            return False, {}

        console.print(Panel(
            Align.center(Text.from_markup(
                f"[bold {DC_TEXT}][S][/bold {DC_TEXT}] PAUSE / RESUME    "
                f"[bold {DC_DIM}]❖[/bold {DC_DIM}]    "
                f"[bold {DC_RED}][B][/bold {DC_RED}] STOP / CANCEL"
            )),
            title=f"[bold black on {DC_HIGHLIGHT}] LIVE CONTROLS [/]",
            border_style=DC_BORDER,
            box=HEAVY_EDGE,
        ))
        console.print()

        is_paused = False
        is_cancelled = False
        ext_counts = defaultdict(int)

        with Progress(
            SpinnerColumn(style=f"bold {DC_HIGHLIGHT}"),
            TextColumn("[bold white]{task.description}"),
            BarColumn(bar_width=30, complete_style=f"bold {DC_HIGHLIGHT}", finished_style=f"bold {DC_GREEN}"),
            TextColumn("[bold white]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Extracting...", total=total_files)

            for dir_path, dir_content in self._index.items():
                if is_cancelled:
                    break
                current_out_path = out_path / dir_path
                current_out_path.mkdir(parents=True, exist_ok=True)

                for file_name, entry in dir_content.items():
                    if is_cancelled:
                        break

                    while True:
                        key = check_key_press()
                        if key == 's':
                            is_paused = not is_paused
                            if is_paused:
                                progress.update(task, description=f"[blink bold {DC_ORANGE}]PAUSED - press [S] to resume[/]")
                            else:
                                progress.update(task, description="[cyan]Extracting...")
                        elif key == 'b':
                            is_cancelled = True
                            break

                        if not is_paused:
                            break
                        time.sleep(0.1)

                    if is_cancelled:
                        break

                    if entry is None:
                        progress.update(task, advance=1)
                        continue

                    short_name = file_name if len(file_name) < 30 else file_name[:15] + "..." + file_name[-15:]
                    progress.update(task, advance=1, description=f"[cyan]Extracting: [white]{short_name}[/white]")

                    try:
                        self._write_to_disk(current_out_path / file_name, entry)
                        ext = os.path.splitext(file_name)[1].lower()
                        if not ext: ext = "no_ext"
                        ext_counts[ext] += 1
                    except Exception:
                        pass

        console.print()
        if is_cancelled:
            console.print(Panel(
                f"[bold {DC_RED}]EXTRACTION CANCELLED BY USER![/bold {DC_RED}]",
                border_style=DC_RED,
                box=HEAVY_EDGE,
            ))
            return False, dict(ext_counts)
        else:
            return True, dict(ext_counts)

    def dump_single_file(self, target_file_name, out_path_base=None, single_dir_name="UNPACKED"):
        """Extract a single file from the PAK."""
        if out_path_base is None:
            out_path_base = Path("/storage/emulated/0/Documents/KUNALYT0/")

        entry_found = None
        dir_of_file = None
        for dir_path, dir_content in self._index.items():
            if target_file_name in dir_content:
                entry_found = dir_content[target_file_name]
                dir_of_file = dir_path.relative_to(self._mount_point) if dir_path.parts and dir_path.parts[0] == self._mount_point.name else dir_path
                break

        if entry_found is None:
            console.print(Panel(f"[red]Error: '{target_file_name}' not found in PAK.[/red]"))
            return

        pak_stem = Path(self._file_path).stem
        current_out_path = out_path_base / single_dir_name / pak_stem / dir_of_file
        os.makedirs(to_long_path(current_out_path), exist_ok=True)
        target_path = current_out_path / target_file_name

        console.print(f"[dim]|[/] [bold {DC_HIGHLIGHT}]SINGLE UNPACK:[/] [green]{target_file_name}[/] [dim]from {self._file_path.name}[/dim]")
        try:
            self._write_to_disk(target_path, entry_found)
            console.print(Panel(f"[green]Successfully extracted: {target_file_name}[/green]"))
        except Exception as e:
            console.print(Panel(f"[red]Error writing {target_file_name}: {e}[/red]"))


# =====================================================================
# PART 10 - PREMIUM AUTH SYSTEM (KUNALYT0)
# =====================================================================

AUTH_KEY_FILE = os.path.expanduser("~/KUNALYT0_LICENSES.json")
REMOTE_KEYS_URL = "https://gist.githubusercontent.com/pikunp909-dot/745409e249483f560314d9fe0ca92442/raw/keys.json"
SESSION_FILE = os.path.expanduser("~/.kunalyt0_session")
ADMIN_SECRET_KEY = "KUNALYT02001"
TELEGRAM_CONTACT = "@YourTelegram" # <-- Yahan apna Telegram daalo

def _encrypt_data(data_str):
    return base64.b64encode(data_str.encode('utf-8')).decode('utf-8')

def _decrypt_data(data_str):
    try:
        return base64.b64decode(data_str.encode('utf-8')).decode('utf-8')
    except:
        return "{}"

def load_licenses():
    merged_data = {}
    
    # 1. Load Local Data
    if os.path.exists(AUTH_KEY_FILE):
        try:
            with open(AUTH_KEY_FILE, "r") as f:
                encrypted = f.read()
                local_data = json.loads(_decrypt_data(encrypted))
                merged_data.update(local_data)
        except:
            pass
    
    # 2. Load Remote Data (Override local)
    if REMOTE_KEYS_URL:
        try:
            import requests
            r = requests.get(REMOTE_KEYS_URL, timeout=8, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                remote_data = r.json()
                local_trials = {
                    k: v for k, v in merged_data.items()
                    if k.startswith("KUNALYT0-TRIAL-") and isinstance(v, dict) and v.get("tier") == "TRIAL"
                }
                merged_data.update(remote_data)
                # Per-device trials live only on this device. Gist must not clobber them.
                merged_data.update(local_trials)
        except:
            pass
            
    return merged_data

def save_licenses(data):
    try:
        with open(AUTH_KEY_FILE, "w") as f:
            f.write(_encrypt_data(json.dumps(data, indent=4)))
    except Exception as e:
        console.print(f"[bold red]Failed to save keys: {e}[/]")

def generate_new_key(tier="PREMIUM", days=30):
    chars = string.ascii_uppercase + string.digits
    part1 = "".join(secrets.choice(chars) for _ in range(4))
    part2 = "".join(secrets.choice(chars) for _ in range(4))
    part3 = "".join(secrets.choice(chars) for _ in range(4))
    key = f"KUNALYT0-{part1}-{part2}-{part3}"
    
    expires = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    data = load_licenses()
    data[key] = {
        "username": "Premium User",
        "hwid": "UNBIND",
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "expires_at": expires,
        "status": "active",
        "tier": tier
    }
    save_licenses(data)
    return key

def validate_license_key(key):
    key = key.strip().upper()
    data = load_licenses()
    
    if key not in data:
        return False, None, "Invalid License Key"
        
    info = data[key]

    # Check Trial Key Strictness (1 HWID = 1 Trial)
    if info.get("tier") == "TRIAL":
        trial_log = os.path.expanduser("~/.kunalyt0_trial_used")
        current_hwid = get_hwid()
        used_hwids = []
        if os.path.exists(trial_log):
            with open(trial_log, "r") as f:
                used_hwids = f.read().splitlines()
        
        if current_hwid in used_hwids and info.get("hwid") != current_hwid:
            return False, None, "Trial key already used on this device! Please buy Premium."
        
        if info.get("hwid") == "UNBIND":
            if current_hwid not in used_hwids:
                with open(trial_log, "a") as f:
                    f.write(current_hwid + "\n")
    
    if info.get("status") != "active":
        return False, None, "Key is blocked/revoked"
        
    # Check Expiry
    try:
        expiry_date = datetime.strptime(info["expires_at"], "%Y-%m-%d")
        if datetime.now() > expiry_date:
            return False, None, f"Key expired on {info['expires_at']}"
    except:
        return False, None, "Invalid date format in key"
        
    # Check HWID
    current_hwid = get_hwid()
    if info["hwid"] == "UNBIND":
        data[key]["hwid"] = current_hwid
        save_licenses(data)
    elif info["hwid"] != current_hwid:
        return False, None, "Key is locked to another device (HWID Mismatch)"
        
    return True, info, "Success"


def auto_sync_to_gist():
    import os
    import json
    import base64
    import requests

    GIST_ID = "745409e249483f560314d9fe0ca92442"
    TOKEN_FILE = os.path.expanduser("~/.kunalyt0_gh_token")
    AUTH_FILE = os.path.expanduser("~/KUNALYT0_LICENSES.json")

    token = ""
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "r") as f:
                token = f.read().strip()
        except:
            pass

    if not token:
        return

    if not os.path.exists(AUTH_FILE):
        return

    try:
        with open(AUTH_FILE, "r") as f:
            encoded = f.read()
        decoded = base64.b64decode(encoded).decode("utf-8")
        keys_json = json.loads(decoded)
    except Exception:
        return

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    payload = {
        "files": {
            "keys.json": {
                "content": json.dumps(keys_json, indent=2)
            }
        }
    }

    with console.status("[bold #00FFCC]Auto-syncing keys to Cloud...[/]", spinner="dots"):
        try:
            r = requests.patch(f"https://api.github.com/gists/{GIST_ID}", headers=headers, json=payload, timeout=15)
            if r.status_code == 200:
                console.print("[bold #00FF00]Keys auto-synced to Cloud![/]")
            else:
                console.print(f"[bold #FF3366]Failed to sync: {r.status_code}[/]")
        except Exception as e:
            console.print(f"[bold #FF3366]Sync Error: {e}[/]")

def admin_panel():
    console.clear()
    
    while True:
        data = load_licenses()
        total_keys = len(data)
        active_keys = 0
        expired_keys = 0
        today = datetime.now().strftime("%Y-%m-%d")
        
        for k, v in data.items():
            if v.get("status") == "active" and v.get("expires_at", "2000-01-01") >= today:
                active_keys += 1
            else:
                expired_keys += 1

        console.print(Panel(
            Align.center(Text.from_markup(
                "[bold #FF3366]K U N A L Y T 0   A D M I N   C O N T R O L[/]\n"
                "[dim]Secure Environment | Authenticated Access[/]"
            )),
            border_style="#FF3366", box=DOUBLE_EDGE, padding=(0, 1)
        ))
        
        stats_table = Table.grid(expand=True)
        stats_table.add_column(justify="center", ratio=1)
        stats_table.add_column(justify="center", ratio=1)
        stats_table.add_column(justify="center", ratio=1)
        stats_table.add_row(
            f"[bold #7A7A9A]TOTAL KEYS[/]\n[bold white]{total_keys}[/]",
            f"[bold #00FFCC]ACTIVE KEYS[/]\n[bold white]{active_keys}[/]",
            f"[bold #FF3366]EXPIRED/REVOKED[/]\n[bold white]{expired_keys}[/]"
        )
        console.print(Panel(stats_table, border_style="#3A3A5A", box=ROUNDED, padding=(0, 1)))
        
        menu = Table.grid(expand=True, padding=(0, 1))
        menu.add_column("OPT", justify="center", width=4)
        menu.add_column("ACTION", justify="left", ratio=1)
        menu.add_column("DESC", justify="right", style="dim")
        
        menu.add_row("[bold #FFAA00]1[/]", "[bold white]Generate Premium Key[/]", "[dim]30 Days Access[/]")
        menu.add_row("[bold #FFAA00]2[/]", "[bold white]Generate VIP Key[/]", "[dim]365 Days Access[/]")
        menu.add_row("[bold #00FFCC]3[/]", "[bold white]View All Keys[/]", "[dim]List active & expired keys[/]")
        menu.add_row("[bold #FF3366]4[/]", "[bold white]Revoke Key[/]", "[dim]Delete a user's key[/]")
        menu.add_row("[bold #7A7A9A]5[/]", "[bold white]Reset HWID[/]", "[dim]Unbind key from a device[/]")
        menu.add_row("[bold #FF00AA]6[/]", "[bold white]Broadcast Announcement[/]", "[dim]Set message on login screen[/]")
        menu.add_row("[bold #00FF00]7[/]", "[bold white]Generate Custom Key[/]", "[dim]Custom Key & Days[/]")
        menu.add_row("[bold white]0[/]", "[bold white]Logout Admin[/]", "[dim]Exit admin panel[/]")
        
        console.print(Panel(menu, border_style="#FF3366", box=HEAVY_EDGE, title="[bold black on #FF3366]ADMIN COMMAND MENU[/]"))
        
        ch = safe_input("\n[bold #FF3366]Enter Admin Command > [/]").strip()
        
        if ch in ["1", "2"]:
            days = 30 if ch == "1" else 365
            tier = "PREMIUM" if ch == "1" else "VIP"
            count_str = safe_input(f"[bold #00FFCC]How many {tier} Keys to generate? (default 1): [/]").strip()
            count = int(count_str) if count_str.isdigit() else 1
            generated_keys = []
            with console.status(f"[bold #00FFCC]Generating {count} {tier} Keys...[/]", spinner="dots"):
                time.sleep(1)
                for _ in range(count):
                    new_key = generate_new_key(tier, days)
                    generated_keys.append(new_key)
            keys_text = "\n".join(generated_keys)
            console.print(Panel(
                Align.center(Text.from_markup(
                    f"[bold #00FF00]{count} {tier} KEYS GENERATED[/]\n\n"
                    f"[bold white]{keys_text}[/]\n\n"
                    f"[dim]Valid for {days} days[/]"
                )),
                border_style="#00FF00", box=DOUBLE_EDGE, padding=(1, 4)
            ))
            try:
                save_file = os.path.expanduser("~/KUNALYT0_MY_KEYS.txt")
                with open(save_file, "a", encoding="utf-8") as f:
                    for k in generated_keys:
                        f.write(f"{k}\n")
            except:
                pass
            auto_sync_to_gist()
            safe_input("\n[bold white]Press Enter...[/]")
            
        elif ch == "3":
            console.clear()
            console.print(Panel(Align.center(Text.from_markup("[bold #00FFCC]ALL LICENSES[/]")), border_style="#00FFCC"))
            if not data:
                console.print("[dim]No keys found in database.[/]")
            else:
                table = Table(box=HEAVY_EDGE, border_style="#3A3A5A", expand=True)
                table.add_column("License Key", style="bold white")
                table.add_column("Tier", style="bold #FFAA00", justify="center")
                table.add_column("Status", justify="center")
                table.add_column("Expires", style="cyan", justify="center")
                table.add_column("HWID", style="dim")
                for k, v in data.items():
                    status = v.get("status", "unknown")
                    is_expired = v.get("expires_at", "2000-01-01") < today
                    if is_expired:
                        status_str = "[bold #FF3366]EXPIRED[/]"
                    elif status == "active":
                        status_str = "[bold #00FF00]ACTIVE[/]"
                    else:
                        status_str = f"[bold #FFAA00]{status.upper()}[/]"
                    table.add_row(k, v.get("tier", "?"), status_str, v.get("expires_at", "?"), v.get("hwid", "?"))
                console.print(table)
            safe_input("\n[bold white]Press Enter...[/]")
            
        elif ch == "4":
            console.print("\n[bold #FF3366]Enter Key to Revoke (or leave blank to cancel):[/]")
            k_to_del = safe_input("[bold white]> [/]").strip().upper()
            if k_to_del:
                if k_to_del in data:
                    del data[k_to_del]
                    save_licenses(data)
                    console.print(Panel(f"[bold #FF3366]Key Revoked & Deleted: {k_to_del}[/]", border_style="#FF3366"))
                else:
                    console.print(Panel("[bold #FFAA00]Key not found![/]", border_style="#FFAA00"))
                auto_sync_to_gist()
                safe_input("Press Enter...")
                
        elif ch == "5":
            console.print("\n[bold #7A7A9A]Enter Key to Reset HWID:[/]")
            k_to_reset = safe_input("[bold white]> [/]").strip().upper()
            if k_to_reset and k_to_reset in data:
                data[k_to_reset]["hwid"] = "UNBIND"
                save_licenses(data)
                console.print(Panel(f"[bold #00FF00]HWID Reset for: {k_to_reset}[/]", border_style="#00FF00"))
                auto_sync_to_gist()
                safe_input("Press Enter...")
            elif k_to_reset:
                console.print(Panel("[bold #FFAA00]Key not found![/]", border_style="#FFAA00"))
                safe_input("Press Enter...")
                
        elif ch == "6":
            console.print("\n[bold #FF00AA]Enter Announcement Message (leave blank to clear):[/]")
            msg = safe_input("[bold white]> [/]").strip()
            try:
                with open(ANNOUNCEMENT_FILE, "w", encoding="utf-8") as f:
                    f.write(msg)
                console.print("[bold #00FF00]Announcement updated![/]")
            except Exception as e:
                console.print(f"[bold #FF3366]Error: {e}[/]")
            safe_input("Press Enter...")
            
        elif ch == "7":
            console.print("\n[bold #00FF00]Enter Custom Key Prefix (e.g., CUSTOM):[/]")
            prefix = safe_input("[bold white]> [/]").strip().upper()
            console.print("[bold #00FF00]Enter Days Duration:[/]")
            days = safe_input("[bold white]> [/]").strip()
            if prefix and days.isdigit():
                custom_key = prefix.upper()
                expiry = (datetime.now() + timedelta(days=int(days))).strftime("%Y-%m-%d")
                data[custom_key] = {
                    "username": "Custom User", "hwid": "UNBIND",
                    "created_at": datetime.now().strftime("%Y-%m-%d"),
                    "expires_at": expiry,
                    "status": "active", "tier": "PREMIUM"
                }
                save_licenses(data)
                console.print(Panel(f"[bold #00FF00]Custom Key Created![/]\n[bold white]{custom_key}[/]\n[dim]Expires: {expiry}[/]", border_style="#00FF00"))
            else:
                console.print("[bold #FF3366]Invalid input![/]")
            auto_sync_to_gist()
            safe_input("Press Enter...")
            
        elif ch == "0":
            console.clear()
            console.print(Panel(Align.center(Text.from_markup("[bold #FFAA00]Admin Session Terminated.[/]")), border_style="#FFAA00", box=ROUNDED))
            time.sleep(1)
            sys.exit(0)
        else:
            console.print("[bold #FF3366]Unknown command![/]")
            time.sleep(1)


ATTEMPT_FILE = os.path.expanduser("~/.kunalyt0_attempts")
HISTORY_FILE = os.path.expanduser("~/.kunalyt0_history")
ANNOUNCEMENT_FILE = os.path.expanduser("~/.kunalyt0_announce")


def check_brute_force():
    """Check if user is locked out due to too many failed attempts."""
    if not os.path.exists(ATTEMPT_FILE):
        return False, 0
    try:
        with open(ATTEMPT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        attempts = data.get("attempts", 0)
        last_time = data.get("last_time", 0)
        if attempts >= 3:
            elapsed = time.time() - last_time
            if elapsed < 30:
                return True, int(30 - elapsed)
            with open(ATTEMPT_FILE, "w", encoding="utf-8") as f:
                json.dump({"attempts": 0, "last_time": 0}, f)
            return False, 0
        return False, 0
    except Exception:
        return False, 0


def record_failed_attempt():
    """Record a failed attempt for brute-force protection."""
    data = {"attempts": 0, "last_time": 0}
    if os.path.exists(ATTEMPT_FILE):
        try:
            with open(ATTEMPT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {"attempts": 0, "last_time": 0}
    data["attempts"] = data.get("attempts", 0) + 1
    data["last_time"] = time.time()
    try:
        with open(ATTEMPT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except Exception:
        pass


def clear_failed_attempts():
    """Clear attempt counter on successful login."""
    try:
        if os.path.exists(ATTEMPT_FILE):
            os.remove(ATTEMPT_FILE)
    except Exception:
        pass


def get_system_health():
    """Get RAM, storage and battery info."""
    health = {"ram": "N/A", "storage": "N/A", "battery": "N/A"}
    try:
        mem_total = mem_avail = 0
        with open("/proc/meminfo", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    mem_total = int(line.split()[1]) // 1024
                elif line.startswith("MemAvailable:"):
                    mem_avail = int(line.split()[1]) // 1024
        if mem_total > 0:
            used = mem_total - mem_avail
            health["ram"] = f"{used}MB / {mem_total}MB"
    except Exception:
        pass
    try:
        stat = os.statvfs("/storage/emulated/0")
        free_gb = (stat.f_bavail * stat.f_frsize) / (1024 ** 3)
        health["storage"] = f"{free_gb:.1f} GB free"
    except Exception:
        pass
    try:
        batt = subprocess.check_output(["termux-battery-status"], timeout=2).decode()
        b = json.loads(batt)
        health["battery"] = f"{b['percentage']}% ({b['status']})"
    except Exception:
        health["battery"] = "N/A"
    return health


def get_recent_logins():
    """Get last 3 successful logins."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)[-3:]
    except Exception:
        return []


def save_login_history(username):
    """Save current login to history."""
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append({
        "username": username,
        "hwid": get_hwid(),
        "time": get_indian_time()
    })
    history = history[-5:]
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
    except Exception:
        pass


def get_announcement():
    """Get admin announcement."""
    if not os.path.exists(ANNOUNCEMENT_FILE):
        return None
    try:
        with open(ANNOUNCEMENT_FILE, "r", encoding="utf-8") as f:
            msg = f.read().strip()
            return msg if msg else None
    except Exception:
        return None

def get_network_ping():
    """Get network latency to Google DNS (8.8.8.8)."""
    import subprocess
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "1", "8.8.8.8"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if "time=" in line:
                    ms = line.split("time=")[1].split(" ")[0]
                    return f"{ms} ms"
        return "OFFLINE"
    except:
        return "OFFLINE"

def generate_session_token():
    """Generate a random session token for display."""
    import random
    import string
    parts = []
    for _ in range(3):
        part = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
        parts.append(part)
    return "-".join(parts)


def premium_login_screen():
    console.clear()

    # Per-device trial key. Refresh when missing, expired, or bound to another HWID.
    # Remote gist used to override local and skip this block entirely (old 2026-11-02 expiry).
    trial_key = f"KUNALYT0-TRIAL-{get_hwid()[:8]}"
    _all_lic = load_licenses()
    _today = datetime.now().strftime("%Y-%m-%d")
    _trial_entry = _all_lic.get(trial_key)
    _needs_refresh = (
        _trial_entry is None
        or _trial_entry.get("expires_at", "2000-01-01") < _today
        or _trial_entry.get("hwid", "UNBIND") != get_hwid()
    )
    if _needs_refresh:
        _all_lic[trial_key] = {
            "username": "Trial User",
            "hwid": get_hwid(),
            "created_at": _today,
            "expires_at": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "status": "active",
            "tier": "TRIAL"
        }
        save_licenses(_all_lic)

    TELEGRAM_LINK = "https://t.me/+6IfBoh4IrToxYmY1"

    # Show saved active key if it exists
    active_key_display = None
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                active_key_display = f.read().strip()
        except:
            pass

    # Time based greeting
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "GOOD MORNING"
    elif current_hour < 18:
        greeting = "GOOD AFTERNOON"
    else:
        greeting = "GOOD EVENING"

    # Loading Splash Animation
    console.clear()
    with console.status("[bold #00FFCC]Initializing KUNALYT0 Engine...[/]", spinner="bouncingBall"):
        time.sleep(0.8)
    with console.status("[bold #FF3366]Loading Premium Modules...[/]", spinner="dots12"):
        time.sleep(0.6)
    with console.status("[bold #FFAA00]Connecting to Server...[/]", spinner="arc"):
        time.sleep(0.5)

    while True:
        console.clear()

        session_token = generate_session_token()
        console.print(f"[dim]Session: [bold #00FFCC]{session_token}[/] | [bold #00FF00]🛡️ SECURE CONNECTION[/][/]")

        banner_text = (
            "\n"
            "[bold #00FFCC]██╗  ██╗██╗   ██╗███╗   ██╗ █████╗ ██╗     ██╗   ██╗████████╗ ██████╗ [/]\n"
            "[bold #00FFCC]██║ ██╔╝██║   ██║████╗  ██║██╔══██╗██║     ╚██╗ ██╔╝╚══██╔══╝██╔═████╗[/]\n"
            "[bold #00FFCC]█████╔╝ ██║   ██║██╔██╗ ██║███████║██║      ╚████╔╝    ██║   ██║██╔██║[/]\n"
            "[bold #00FFCC]██╔═██╗ ██║   ██║██║╚██╗██║██╔══██║██║       ╚██╔╝     ██║   ████╔╝██║[/]\n"
            "[bold #00FFCC]██║  ██╗╚██████╔╝██║ ╚████║██║  ██║███████╗   ██║      ██║   ╚██████╔╝[/]\n"
            "[bold #00FFCC]╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝      ╚═╝    ╚═════╝ [/]"
        )
        # Check for Updates
        try:
            import requests
            r = requests.get("https://raw.githubusercontent.com/pikunp909-dot/Kunalyto-Dependencies/main/version.txt", timeout=3)
            if r.status_code == 200:
                latest_version = r.text.strip()
                if latest_version and latest_version != "V8.0":
                    console.print(Panel(
                        Align.center(Text.from_markup(f"[bold #FF3366]🚀 NEW UPDATE AVAILABLE: {latest_version} 🚀[/]\n[dim]Please download the latest version from Telegram.[/]")),
                        border_style="#FF3366", box=HEAVY_EDGE, padding=(0, 1)
                    ))
        except:
            pass

        console.print(Panel(
            Align.center(Text.from_markup(banner_text)),
            title="[bold black on #FFAA00]  PREMIUM MODDING SUITE  [/]",
            subtitle=f"[bold black on #FFAA00] v8.0 PRO | {greeting} [/]",
            border_style="#FFAA00",
            box=DOUBLE_EDGE,
            padding=(0, 1)
        ))

        # Check actual internet and login status
        ping = get_network_ping()
        if ping == "OFFLINE":
            status_text = "[bold #FF3366]● NET OFFLINE[/]"
        elif os.path.exists(SESSION_FILE):
            status_text = "[bold #00FF00]● LOGGED IN[/]"
        else:
            status_text = "[bold #FFAA00]● GUEST MODE[/]"

        stats_grid = Table.grid(expand=True)
        stats_grid.add_column(justify="left", ratio=1)
        stats_grid.add_column(justify="center", ratio=1)
        stats_grid.add_column(justify="right", ratio=1)
        stats_grid.add_row(
            f"[bold #7A7A9A]DEVICE[/]\n[bold white]{get_real_device_model()}[/]\n[dim]{get_hwid()}[/]",
            f"[bold #7A7A9A]CLOCK[/]\n[bold white]{get_indian_time()}[/]",
            f"[bold #7A7A9A]STATUS[/]\n{status_text}"
        )
        console.print(Panel(
            stats_grid,
            title="[bold black on #00FFCC]  SYSTEM INFO  [/]",
            border_style="#00FFCC",
            box=ROUNDED,
            padding=(0, 2)
        ))

        # System Health Panel
        health = get_system_health()
        ping = get_network_ping()
        health_grid = Table.grid(expand=True)
        health_grid.add_column(justify="center", ratio=1)
        health_grid.add_column(justify="center", ratio=1)
        health_grid.add_column(justify="center", ratio=1)
        health_grid.add_column(justify="center", ratio=1)
        health_grid.add_row(
            f"[bold #7A7A9A]💾 RAM[/]\n[bold white]{health['ram']}[/]",
            f"[bold #7A7A9A]💿 STORAGE[/]\n[bold white]{health['storage']}[/]",
            f"[bold #7A7A9A]🔋 BATT[/]\n[bold white]{health['battery']}[/]",
            f"[bold #7A7A9A]📡 PING[/]\n[bold white]{ping}[/]"
        )
        console.print(Panel(
            health_grid,
            title="[bold black on #FF00AA]  SYSTEM HEALTH  [/]",
            border_style="#FF00AA", box=ROUNDED, padding=(0, 1)
        ))

        if active_key_display:
            console.print(Panel(
                Align.center(Text.from_markup(
                    f"[bold #FFAA00]🔑 Your Current Active Key:[/]\n"
                    f"[bold white]{active_key_display}[/]\n"
                    f"[dim](Copy this to login on other devices)[/]"
                )),
                border_style="#FFAA00", box=ROUNDED, padding=(0, 1)
            ))

        menu_content = Table.grid(expand=True, padding=(0, 1))
        menu_content.add_column("ICON", justify="center", width=4)
        menu_content.add_column("OPT", justify="center", width=4)
        menu_content.add_column("LABEL", justify="left", ratio=1)
        menu_content.add_column("DESC", justify="right", style="dim")
        menu_content.add_row("[#00FFCC]>[/]", "[bold #00FFCC]1[/]", "[bold white]Login with License Key[/]", "[dim]Enter your premium key[/]")
        menu_content.add_row("[#FFAA00]>[/]", "[bold #FFAA00]2[/]", "[bold white]Get Premium Key[/]", "[dim]Join Telegram channel[/]")
        menu_content.add_row("[#FF00AA]>[/]", "[bold #FF00AA]3[/]", "[bold white]Use 1-Day Trial Key[/]", "[dim]Free trial access[/]")
        menu_content.add_row("[#7A7A9A]>[/]", "[bold #7A7A9A]4[/]", "[bold white]Admin Panel[/]", "[dim]Restricted access[/]")
        menu_content.add_row("[#FF3366]>[/]", "[bold #FF3366]0[/]", "[bold white]Exit Tool[/]", "[dim]Close application[/]")

        console.print(Panel(
            menu_content,
            title="[bold black on #00FFCC]  SELECT AN OPTION  [/]",
            subtitle="[dim]KUNALYT0 | Neural Auth[/]",
            border_style="#00FFCC",
            box=HEAVY_EDGE,
            padding=(0, 1)
        ))

        # Security Shield Bar
        shield_bar = Text.from_markup(
            "[bold #00FFCC]🛡️ HWID LOCKED[/]  [bold #FFAA00]🔒 SM4 ACTIVE[/]  [bold #FF3366]⚡ ANTI-BAN ON[/]"
        )
        console.print(Align.center(shield_bar))

        # Recent Logins
        recent = get_recent_logins()
        if recent:
            hist_text = "[bold #7A7A9A]Recent Logins:[/]"
            for h in recent:
                hist_text += f" [dim]{h['time'][-8:]}[/]"
            console.print(Align.center(Text.from_markup(hist_text)))

        choice = safe_input("\n[bold #FFAA00]╰─➤ Enter Choice[/] [dim](1/2/3/4/0)[/] [bold #FFAA00]►[/] ").strip()

        if choice == "1":
            console.print()
            console.print(Panel(
                "[bold #00FFCC]ENTER YOUR LICENSE KEY[/]\n\n"
                "[dim]Format:[/] [bold white]KUNALYT0-XXXX-XXXX-XXXX[/]\n"
                "[dim]Example:[/] [bold white]KUNALYT0-A1B2-C3D4-E5F6[/]",
                border_style="#00FFCC",
                box=ROUNDED,
                padding=(0, 2)
            ))
            key_input = Prompt.ask("[bold #FFAA00]►[/] [bold white]License Key[/]").strip()
            if not key_input:
                continue

            console.print()
            with console.status("[bold #00FFCC]Authenticating via Neural Engine...[/]", spinner="bouncingBar"):
                time.sleep(1.5)
                success, info, msg = validate_license_key(key_input)

            if success:
                clear_failed_attempts()
                save_login_history(info['username'])
                with open(SESSION_FILE, "w", encoding="utf-8") as f:
                    f.write(key_input.strip().upper())

                exp_date = datetime.strptime(info['expires_at'], "%Y-%m-%d")
                days_left = (exp_date - datetime.now()).days
                status_color = "#00FF00" if days_left > 7 else "#FFAA00"
                
                console.print(Panel(
                    Align.center(Text.from_markup(
                        f"[bold #00FFCC]Welcome back, {info['username']}![/]\n"
                        f"[bold white]Tier:[/] {info['tier']} | [bold white]Expires:[/] {info['expires_at']} ([{status_color}]{days_left} days left[/{status_color}])\n\n"
                        f"[dim]Booting KUNALYT0 Engine...[/]"
                    )),
                    border_style="#00FF00", box=ROUNDED, padding=(1, 4)
                ))
                time.sleep(2)
                main_menu()
                sys.exit(0)
            else:
                console.print()
                console.print(Panel(
                    f"[bold #FF3366]ACCESS DENIED[/]\n\n"
                    f"[bold #FFAA00]Reason:[/] [white]{msg}[/]",
                    border_style="#FF3366",
                    box=HEAVY_EDGE,
                    padding=(0, 2)
                ))
                safe_input("\n[bold #FFAA00]Press Enter to try again...[/]")

        elif choice == "2":
            console.clear()
            
            # ═══════════════════ PREMIUM STORE UI ═══════════════════
            console.print()
            
            # 1. Main Header
            console.print(Panel(
                Align.center(Text.from_markup(
                    "[bold #FFAA00]👑  K U N A L Y T 0   P R E M I U M   S T O R E  👑[/]\n"
                    "[dim white]Unlock the Full Power of Modding[/]"
                )),
                border_style="#FFAA00", box=DOUBLE_EDGE, padding=(0, 1)
            ))
            
            # 2. Owner & Trust Info
            info_grid = Table.grid(expand=True)
            info_grid.add_column(justify="left", ratio=1)
            info_grid.add_column(justify="right", ratio=1)
            info_grid.add_row(
                f"[bold #00FFCC]👤 Owner:[/] [bold white]@TG_MANAV[/] [green]✔[/]",
                f"[bold #00FFCC]📢 Channel:[/] [bold white]ManavYt Official[/] 🇮🇳"
            )
            info_grid.add_row(
                f"[bold #00FFCC]🔗 Alt:[/] [bold white]@KUNALYT0[/]",
                f"[bold #00FFCC]⚡ Status:[/] [bold green]ONLINE[/]"
            )
            console.print(Panel(
                info_grid, 
                border_style="#3A3A5A", 
                box=ROUNDED, 
                title="[bold black on #00FFCC] VERIFIED SELLER [/]"
            ))

            # 3. What You Get (Benefits)
            benefits = Table(show_header=False, box=None, padding=(0, 1))
            benefits.add_column("Check", style="bold #00FF00", justify="center", width=3)
            benefits.add_column("Feature", style="white")
            benefits.add_row("✅", "Premium License Keys (30 Days / Lifetime)")
            benefits.add_row("✅", "VIP Access to Exclusive Mods (ESP, Antenna, etc.)")
            benefits.add_row("✅", "Priority Support & Fast Updates")
            benefits.add_row("✅", "100% Anti-Ban & Antireset Protection")
            
            console.print(Panel(
                Align.center(benefits),
                title="[bold black on #FFAA00] 🚀 WHAT YOU GET 🚀 [/]",
                border_style="#FFAA00", box=ROUNDED, padding=(0, 1)
            ))

            # 4. Telegram Link Box
            tg_link = "https://t.me/+6IfBoh4IrToxYmY1"
            console.print(Panel(
                Align.center(Text.from_markup(
                    f"[bold white]Join our Official Telegram to get your Key:[/]\n\n"
                    f"[bold black on #00FFCC]  👉 {tg_link} 👈  [/]\n\n"
                    f"[dim]💡 Tip: Tap the link or copy it to your browser.[/]\n"
                    f"[dim]💬 Need help? PM Owner: @TG_MANAV[/]"
                )),
                title="[bold black on #00FF00] 🔗 GET PREMIUM NOW 🔗 [/]",
                border_style="#00FF00", box=HEAVY_EDGE, padding=(1, 2)
            ))
            # ═══════════════════ END PREMIUM UI ═══════════════════

            safe_input("\n[bold #FFAA00]Press Enter to return to Login...[/]")

        elif choice == "3":
            console.clear()
            console.print(Panel(
                Align.center(Text.from_markup(
                    "[bold #FF00AA]1-DAY FREE TRIAL KEY[/]\n\n"
                    "[bold white]Your Trial Key:[/]\n\n"
                    f"[bold black on #FFAA00]  {trial_key}  [/]\n\n"
                    "[#00FFCC]Valid for 1 day[/]\n"
                    "[#00FFCC]Full feature access[/]\n"
                    "[#00FFCC]HWID auto-binding[/]\n\n"
                    "[dim]Use this key in Option 1 to login[/]"
                )),
                title="[bold black on #FF00AA]  TRIAL ACCESS  [/]",
                border_style="#FF00AA",
                box=DOUBLE_EDGE,
                padding=(1, 4)
            ))
            safe_input("\n[bold white]Press Enter to go back...[/]")

        elif choice == "4":
            console.print()
            console.print(Panel(
                "[bold #FF3366]ADMIN SECRET KEY REQUIRED[/]\n\n"
                "[dim]Only authorized admins can access this panel[/]",
                border_style="#FF3366",
                box=HEAVY_EDGE,
                padding=(0, 2)
            ))
            admin_key = Prompt.ask("[bold #FF3366]►[/] [bold white]Admin Key[/]", password=True).strip()
            if admin_key == ADMIN_SECRET_KEY:
                with console.status("[bold #FF3366]Unlocking Admin Panel...[/]", spinner="dots"):
                    time.sleep(1.5)
                admin_panel()
            else:
                console.print(Panel(
                    "[bold #FF3366]INVALID ADMIN KEY[/]",
                    border_style="#FF3366",
                    box=HEAVY_EDGE
                ))
                time.sleep(2)

        elif choice == "0":
            console.print()
            with console.status("[bold #FF3366]Shutting down gracefully...[/]", spinner="dots12"):
                time.sleep(1)
            console.print(Panel(
                Align.center(Text.from_markup(
                    "[bold #FFAA00]Thank you for using KUNALYT0 Suite[/]\n[dim]See you next time[/]"
                )),
                border_style="#FFAA00",
                box=DOUBLE_EDGE,
                padding=(0, 4)
            ))
            time.sleep(1.5)
            sys.exit(0)
        else:
            console.print(Panel(
                "[bold #FFAA00]Unknown option. Use 1, 2, 3, 4, or 0.[/]",
                border_style="#FFAA00",
                box=ROUNDED
            ))
            time.sleep(1)


# =====================================================================
# PART 4 - REPACK FUNCTIONS + CSV + BUILD NEW PAK
# =====================================================================

# =====================================================================
# ENCRYPT / COMPRESS HELPERS
# =====================================================================

def _encrypt_plaintext(plaintext: bytes, pak_relative_path: PurePath, encryption_method: int) -> bytes:
    if PakCrypto._is_simple1_method(encryption_method):
        return bytes((b ^ SIMPLE1_DECRYPT_KEY for b in plaintext))
    if PakCrypto._is_simple2_method(encryption_method):
        pad_len = -len(plaintext) % SIMPLE2_BLOCK_SIZE
        plaintext += b'\x00' * pad_len
        key, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
        rolling = key
        out = []
        for x, in struct.iter_unpack('<I', plaintext):
            c = rolling ^ x
            out.append(c)
            rolling ^= c
        return struct.pack(f'<{len(out)}I', *out)
    if PakCrypto._is_sm4_method(encryption_method):
        key = PakCrypto._derive_sm4_key(pak_relative_path, encryption_method)
        sm4 = PakCrypto._sm4_context_for_key(key)
        pad_len = -len(plaintext) % 16
        if pad_len > 0:
            plaintext = plaintext + b'\x00' * pad_len
        return sm4.encrypt_bulk(plaintext)
    return plaintext


def _best_compress(chunk, cm, zstd_dict=None, fast=False):
    if cm == CM_ZLIB:
        return zlib.compress(chunk, 1 if fast else 9)
    if cm in (CM_ZSTD, CM_ZSTD_DICT):
        zd = zstd_dict if cm == CM_ZSTD_DICT else None
        levels = [6, 3, 1] if fast else [22, 19, 16, 13, 10, 7, 4, 1]
        for lvl in levels:
            try:
                return ZstdCompressor(level=lvl, dict_data=zd, threads=1).compress(chunk)
            except Exception:
                continue
    return chunk


# =====================================================================
# INDEX SERIALIZATION HELPERS
# =====================================================================

def _pw_string(s):
    if not s:
        return struct.pack('<i', 0)
    b = s.encode('utf-8') + b'\x00'
    return struct.pack('<i', len(b)) + b


def _pw_entry(e, v):
    w = bytearray(e.content_hash)
    w += struct.pack('<Q', e.offset)
    w += struct.pack('<Q', e.uncompressed_size)
    w += struct.pack('<I', e.compression_method)
    w += struct.pack('<Q', e.size)
    if v >= 5:
        w += bytes([e.unk1])
        w += e.unk2
    if e.compression_method != CM_NONE and v >= 3:
        w += struct.pack('<I', len(e.compressed_blocks))
        for b in e.compressed_blocks:
            w += struct.pack('<QQ', b.start, b.end)
    if v >= 4:
        w += struct.pack('<I', e.compression_block_size)
        w += bytes([1 if e.encrypted else 0])
    if v >= 12:
        w += struct.pack('<II', e.encryption_method, e.index_new_sep)
    return bytes(w)


def _get_all_dirs_and_mp(pak_file):
    raw = bytes(pak_file._file_content[pak_file._pak_info.index_offset:][:pak_file._pak_info.index_size])
    if pak_file._pak_info.index_encrypted:
        raw = PakCrypto.decrypt_index(raw, pak_file._pak_info)
    r = Reader(raw)
    mp = r.string()
    num_files = r.u4()
    for _ in range(num_files):
        TencentPakEntry(r, pak_file._pak_info.version)
    dirs = {}
    for _ in range(r.u8()):
        dp = r.string()
        cnt = r.u8()
        dirs[dp] = {r.string(): pak_file._files[~r.i4()] for _ in range(cnt)}
    return mp, dirs


# =====================================================================
# WRITE ENTRY INTO BUFFER (FIXED BLOCK ORDER)
# =====================================================================

def _write_entry_into_buf(out_buf, ne, new_raw, pak_rel, template_entry, zstd_dict, override_settings=None):
    """Write file data with proper block ordering, padding, content_hash."""
    if override_settings:
        ne.compression_method = override_settings.get('compression_method', template_entry.compression_method)
        ne.encryption_method = override_settings.get('encryption_method', template_entry.encryption_method)
        ne.encrypted = override_settings.get('encrypted', template_entry.encrypted)
    else:
        ne.compression_method = template_entry.compression_method
        ne.encryption_method = template_entry.encryption_method
        ne.encrypted = template_entry.encrypted
    
    ne.unk1 = template_entry.unk1
    ne.index_new_sep = template_entry.index_new_sep
    ne.uncompressed_size = len(new_raw)

    if ne.compression_method == CM_NONE:
        if ne.encrypted:
            # ── FIX: Detect if data is already T24-encrypted (from prepare_lua_for_pak) ──
            # T24 format: first 4 bytes = \x1bLua AND byte[13] == 4 (size_t=4)
            is_already_t24 = (
                len(new_raw) > 13
                and new_raw[:4] == b'\x1bLua'
                and new_raw[13] == 4
            )

            if is_already_t24:
                # Data already T24 BGMI-encrypted — do NOT re-encrypt
                cipher = new_raw
            else:
                padded = new_raw
                if PakCrypto._is_sm4_method(ne.encryption_method):
                    pad_len = -len(padded) % 16
                    if pad_len > 0:
                        padded = padded + b'\x00' * pad_len
                cipher = _encrypt_plaintext(padded, pak_rel, ne.encryption_method)
        else:
            cipher = new_raw
        ne.offset = len(out_buf)
        ne.size = len(cipher)
        ne.compression_block_size = 0
        ne.compressed_blocks = []
        out_buf += cipher
    else:
        cs = template_entry.compression_block_size if template_entry.compression_block_size > 0 else 65536
        ne.compression_block_size = cs
        chunks = [new_raw[i:i + cs] for i in range(0, len(new_raw), cs)]

        if not chunks:
            ne.compressed_blocks = []
            ne.offset = len(out_buf)
            ne.size = 0
            return

        n = len(chunks)
        cipher_logical = []
        for chunk in chunks:
            compressed = _best_compress(chunk, ne.compression_method, zstd_dict)
            if ne.encrypted:
                is_already_t24 = (
                    len(compressed) > 13
                    and compressed[:4] == b'\x1bLua'
                    and compressed[13] == 4
                )
                if is_already_t24:
                    cipher = compressed
                else:
                    if PakCrypto._is_sm4_method(ne.encryption_method):
                        pad_len = -len(compressed) % 16
                        if pad_len > 0:
                            compressed = compressed + b'\x00' * pad_len
                    cipher = _encrypt_plaintext(compressed, pak_rel, ne.encryption_method)
            else:
                cipher = compressed
            cipher_logical.append(cipher)

        if ne.encrypted and PakCrypto._is_sm4_method(ne.encryption_method):
            order = PakCrypto.generate_block_indices(n, ne.encryption_method)
        else:
            order = list(range(n))

        phys_cipher = [b''] * n
        for logical_i in range(n):
            phys_cipher[order[logical_i]] = cipher_logical[logical_i]

        phys_blks = []
        for phys_i in range(n):
            bd = phys_cipher[phys_i]
            blk = PakCompressedBlock.__new__(PakCompressedBlock)
            blk.start = len(out_buf)
            blk.end = blk.start + len(bd)
            out_buf += bd
            phys_blks.append(blk)

        logical_blks = [None] * n
        for logical_i in range(n):
            phys_i = order[logical_i]
            logical_blks[logical_i] = phys_blks[phys_i]

        ne.compressed_blocks = logical_blks
        ne.offset = phys_blks[0].start if phys_blks else len(out_buf)
        ne.size = sum(b.end - b.start for b in phys_blks)

    stored_bytes = bytes(out_buf[ne.offset:ne.offset + ne.size])
    ne.content_hash = SHA1.new(stored_bytes).digest()
    ne.unk2 = b'\x00' * 20


# =====================================================================
# EXTRACT ENTRY PLAINTEXT
# =====================================================================

def _extract_entry_plaintext(pak_file, entry, full_path):
    em = entry.encryption_method
    cm = entry.compression_method
    path = PurePath(full_path)
    if cm == CM_NONE:
        data = pak_file._peek_content(entry.offset, entry.size, em)
        if entry.encrypted:
            data = PakCrypto.decrypt_block(data, path, em)
        return bytes(data[:entry.uncompressed_size])
    out = bytearray()
    for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), em):
        data = pak_file._peek_block_content(entry.compressed_blocks[x], em)
        if entry.encrypted:
            data = PakCrypto.decrypt_block(data, path, em)
        out += PakCompression.decompress_block(data, pak_file._zstd_dict, cm)
    return bytes(out)


# =====================================================================
# COPY ORIGINAL CONTENT
# =====================================================================

def _copy_original_content(out_buf, pak_file, ne, old_entry):
    em = old_entry.encryption_method
    if old_entry.compression_method == CM_NONE:
        read_sz = (PakCrypto.align_encrypted_content_size(old_entry.size, em)
                   if old_entry.encrypted else old_entry.size)
        ne.offset = len(out_buf)
        out_buf += bytes(pak_file._file_content[old_entry.offset: old_entry.offset + read_sz])
    elif old_entry.compressed_blocks:
        new_blks = []
        for ob in old_entry.compressed_blocks:
            unc = ob.end - ob.start
            enc = (PakCrypto.align_encrypted_content_size(unc, em)
                   if old_entry.encrypted else unc)
            nb = PakCompressedBlock.__new__(PakCompressedBlock)
            nb.start = len(out_buf)
            nb.end = nb.start + unc
            out_buf += bytes(pak_file._file_content[ob.start: ob.start + enc])
            new_blks.append(nb)
        ne.compressed_blocks = new_blks
        ne.offset = new_blks[0].start
    ne.encryption_method = old_entry.encryption_method
    ne.encrypted = old_entry.encrypted


# =====================================================================
# WRITE PAK INDEX FOOTER
# =====================================================================

def _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path):
    version = pak_file._pak_info.version
    keystream = PakCrypto.zuc_keystream()
    eidx = {id(new_files[i]): i for i in range(len(new_files))}
    old_id_to_new_idx = {id(pak_file._files[i]): i for i in range(len(pak_file._files))}

    idx = bytearray(_pw_string(mp_str))
    idx += struct.pack('<I', len(new_files))
    for ne in new_files:
        idx += _pw_entry(ne, version)
    idx += struct.pack('<Q', len(all_dirs))

    for dp_str, dir_files in all_dirs.items():
        idx += _pw_string(dp_str)
        idx += struct.pack('<Q', len(dir_files))
        for name, old_e in dir_files.items():
            idx += _pw_string(name)
            found_idx = eidx.get(id(old_e))
            if found_idx is None:
                found_idx = old_id_to_new_idx.get(id(old_e))
            if found_idx is None:
                copy_of = next((k for k, v in old_to_new.items() if v is old_e), None)
                if copy_of is not None:
                    found_idx = eidx.get(id(old_to_new[copy_of]))
            if found_idx is None:
                for i, e in enumerate(new_files):
                    if e.offset == old_e.offset and e.size == old_e.size:
                        found_idx = i
                        break
            idx += struct.pack('<i', ~found_idx if found_idx is not None else -1)

    index_plain = bytes(idx)
    new_sha1 = SHA1.new(index_plain).digest()

    if pak_file._pak_info.index_encrypted:
        key = PakCrypto.rsa_extract(pak_file._pak_info.packed_key, RSA_MOD_1)
        iv = PakCrypto.rsa_extract(pak_file._pak_info.packed_iv, RSA_MOD_1)
        aes = AES.new(key, MODE_CBC, iv[:16])
        pad_len = (-len(index_plain)) % AES.block_size or AES.block_size
        index_bytes = aes.encrypt(index_plain + bytes([pad_len] * pad_len))
    else:
        index_bytes = index_plain

    new_idx_offset = len(out_buf)
    new_idx_size = len(index_bytes)
    out_buf += index_bytes

    footer_sz = TencentPakInfo._mem_size(version)
    new_footer = bytearray(pak_file._file_content[-footer_sz:])
    h_key = struct.pack('<5I', *keystream[4:9])
    new_footer[-36:-16] = bytes(a ^ b for a, b in zip(new_sha1, h_key))
    new_footer[-16:-8] = ((new_idx_size ^ (keystream[10] << 32 | keystream[11])).to_bytes(8, 'little'))
    new_footer[-8:] = ((new_idx_offset ^ (keystream[0] << 32 | keystream[1])).to_bytes(8, 'little'))
    out_buf += new_footer

    with open(output_path, 'wb') as f:
        f.write(out_buf)


# =====================================================================
# CSV AUTO-DOWNLOAD
# =====================================================================

def download_csv_files(csv_dir: Path) -> bool:
    csv_dir.mkdir(parents=True, exist_ok=True)
    existing = [f for f in csv_dir.iterdir() if f.suffix.lower() == '.csv' and f.stat().st_size > 100]
    if len(existing) >= 2:
        console.print(f"[dim {DC_DIM}]CSV files already cached[/dim {DC_DIM}]")
        return True

    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]Downloading CSV files from GitHub...[/bold {DC_HIGHLIGHT}]",
        title=f"[bold black on {DC_HIGHLIGHT}] CSV AUTO-DOWNLOAD [/]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
    ))

    success_count = 0
    for filename, url in CSV_URLS.items():
        target = csv_dir / filename
        if target.exists() and target.stat().st_size > 100:
            success_count += 1
            continue

        try:
            with Progress(
    TextColumn("[bold white]{task.description}"),
    BarColumn(bar_width=40, complete_style="bold white"),
    TextColumn("[bold white]{task.percentage:>3.0f}%"),
    TextColumn("[dim #8A8A8A]({task.fields[fs]})[/dim #8A8A8A]"),
    TransferSpeedColumn(),
    TimeElapsedColumn(),
    console=console,
) as progress:
                task = progress.add_task(f"{filename}", total=100, fs="")
                r = requests.get(url, stream=True, timeout=60)
                r.raise_for_status()
                total_size = int(r.headers.get('content-length', 0))
                downloaded = 0

                with open(target, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                pct = int((downloaded / total_size) * 100)
                                progress.update(task, completed=pct, fs=f"{downloaded/(1024*1024):.2f} MB")

            console.print(f"[bold {DC_HIGHLIGHT}]Downloaded:[/] [bold {DC_TEXT}]{filename}[/]")
            success_count += 1
        except Exception as e:
            console.print(f"[bold {DC_RED}]Failed {filename}: {e}[/]")

    return success_count >= 1


def _select_csv_source(csv_dir):
    csv_files = [f for f in csv_dir.iterdir() if f.suffix.lower() == '.csv']
    if not csv_files:
        console.print(Panel(f"[{DC_RED}]No CSV files found![/]", border_style=DC_RED))
        return None, None, None

    csv_table = Table(
        title=f"[bold {DC_HIGHLIGHT}]Select CSV Source[/bold {DC_HIGHLIGHT}]",
        box=DOUBLE_EDGE,
        border_style=DC_BORDER,
        header_style=f"bold black on {DC_HIGHLIGHT}",
    )
    csv_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
    csv_table.add_column("Game", style=f"bold {DC_TEXT}")
    csv_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")

    for i, f in enumerate(csv_files, 1):
        sz = f.stat().st_size
        sz_str = f"{sz/1024:.1f} KB" if sz < 1024 * 1024 else f"{sz/(1024*1024):.2f} MB"
        label = {"BGMI.csv": "BGMI 4.6", "PUBG.csv": "PUBG 4.6"}.get(f.name, f.name)
        csv_table.add_row(str(i), label, sz_str)
    csv_table.add_row("0", f"[{DC_RED}]BACK[/]", "[dim]-[/dim]")
    console.print(csv_table)

    try:
        sel = console.input(f"[bold {DC_HIGHLIGHT}]Select CSV (0 = back): [/bold {DC_HIGHLIGHT}]").strip()
        if not sel or sel == "0":
            return None, None, None
        idx = int(sel) - 1
        if idx < 0 or idx >= len(csv_files):
            console.print(f"[bold {DC_RED}]Invalid selection[/]")
            return None, None, None
    except ValueError:
        console.print(f"[bold {DC_RED}]Invalid input[/]")
        return None, None, None

    selected_csv = csv_files[idx]
    is_bgmi = selected_csv.name == "BGMI.csv"
    game_label = "BGMI" if is_bgmi else "PUBG"
    return selected_csv, is_bgmi, game_label


def _load_csv_path_map(selected_csv):
    file_path_map = {}
    try:
        with open(selected_csv, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                for part in line.split(','):
                    part = part.strip()
                    if part:
                        file_path_map[Path(part).name] = part
    except Exception as e:
        console.print(f"[bold {DC_RED}]CSV read error: {e}[/]")
        return {}
    return file_path_map


def _resolve_paths_from_csv(edit_dir, file_path_map, is_bgmi):
    edit_files = [p for p in edit_dir.rglob('*') if p.is_file()]
    resolved_files = []
    unresolved = []
    ingame_csv_folder = edit_dir / "InGame" / "EvoBase" / "CSV"

    for p in edit_files:
        filename = p.name
        try:
            p.relative_to(ingame_csv_folder)
            in_ingame = True
        except ValueError:
            in_ingame = False

        if in_ingame:
            if is_bgmi:
                rp = f"Content/MultiRegion/Content/IN/CSV/InGame/EvoBase/CSV/{filename}"
            else:
                rp = f"Content/CSV/InGame/EvoBase/CSV/{filename}"
            resolved_files.append((p, rp))
        else:
            matches = [k for k in file_path_map if k.lower() == filename.lower()]
            if not matches:
                matches = [k for k in file_path_map if filename.lower() in k.lower()]
            if matches:
                resolved_files.append((p, file_path_map[matches[0]]))
            else:
                unresolved.append(p)
    return resolved_files, unresolved


# =====================================================================
# BUILD NEW PAK
# =====================================================================

def build_new_pak(data_path: Path) -> None:
    import copy as _cp

    build_root = data_path / "BUILD_PAK"
    csv_dir = build_root / "CSV"
    edit_dir = build_root / "EDIT"
    template_dir = build_root / "TEMPLATE"
    output_dir = build_root / "OUTPUT"

    for d in (csv_dir, edit_dir, template_dir, output_dir):
        d.mkdir(parents=True, exist_ok=True)

    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]BUILD NEW PAK FROM CSV[/bold {DC_HIGHLIGHT}]\n"
        f"[dim {DC_DIM}]CSV path resolver + template PAK → game-ready output[/dim {DC_DIM}]",
        border_style=DC_BORDER,
        box=DOUBLE_EDGE,
    ))

    if not download_csv_files(csv_dir):
        console.print(Panel(
            f"[bold {DC_RED}]CSV download failed![/]\n"
            f"[{DC_ORANGE}]Check your internet connection.[/]",
            border_style=DC_RED,
            box=HEAVY_EDGE,
        ))
        return

    selected_csv, is_bgmi, game_label = _select_csv_source(csv_dir)
    if selected_csv is None:
        return

    console.print(f"[bold {DC_HIGHLIGHT}]Loading {selected_csv.name}...[/]")
    file_path_map = _load_csv_path_map(selected_csv)
    if not file_path_map:
        console.print(Panel(f"[{DC_RED}]CSV is empty![/]", border_style=DC_RED))
        return
    console.print(f"[bold {DC_HIGHLIGHT}]Loaded {len(file_path_map)} paths from {game_label}[/]")

    pak_files = [f for f in template_dir.iterdir() if f.suffix.lower() in ('.pak', '.obb')]
    if not pak_files:
        console.print(Panel(
            f"[{DC_RED}]No template PAK found![/]\n"
            f"[{DC_ORANGE}]Place a .pak / .obb file in:[/]\n"
            f"[bold {DC_HIGHLIGHT}]{template_dir}[/]",
            border_style=DC_RED,
            box=HEAVY_EDGE,
        ))
        return

    if len(pak_files) == 1:
        template_pak_path = pak_files[0]
        console.print(f"[bold {DC_HIGHLIGHT}]Template:[/] [bold {DC_TEXT}]{template_pak_path.name}[/]")
    else:
        pak_table = Table(title="Select Template PAK", box=DOUBLE_EDGE, border_style=DC_BORDER,
                          header_style=f"bold black on {DC_HIGHLIGHT}")
        pak_table.add_column("#", justify="center", width=4, style=f"bold {DC_HIGHLIGHT}")
        pak_table.add_column("File Name", style=f"bold {DC_TEXT}")
        pak_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
        for i, f in enumerate(pak_files, 1):
            sz = f.stat().st_size / (1024 * 1024)
            pak_table.add_row(str(i), f.name, f"{sz:.2f} MB")
        console.print(pak_table)
        try:
            sel = console.input(f"[bold {DC_HIGHLIGHT}]Select template (1-{len(pak_files)}): [/bold {DC_HIGHLIGHT}]").strip()
            idx = int(sel) - 1
            if idx < 0 or idx >= len(pak_files):
                console.print(f"[bold {DC_RED}]Invalid[/]")
                return
            template_pak_path = pak_files[idx]
        except ValueError:
            console.print(f"[bold {DC_RED}]Invalid[/]")
            return

    edit_files = [p for p in edit_dir.rglob('*') if p.is_file()]
    if not edit_files:
        console.print(Panel(
            f"[{DC_RED}]No files in EDIT folder![/]\n"
            f"[{DC_ORANGE}]Put files in:[/]\n"
            f"[bold {DC_HIGHLIGHT}]{edit_dir}[/]",
            border_style=DC_RED,
            box=HEAVY_EDGE,
        ))
        return

    resolved_files, unresolved = _resolve_paths_from_csv(edit_dir, file_path_map, is_bgmi)
    if not resolved_files:
        console.print(Panel(
            f"[{DC_RED}]No files matched the CSV paths![/]",
            border_style=DC_RED,
            box=HEAVY_EDGE,
        ))
        return

    lines = [f"[bold {DC_HIGHLIGHT}]CSV: {game_label} ({selected_csv.name})[/bold {DC_HIGHLIGHT}]", ""]
    for p, rp in resolved_files:
        lines.append(f"  [bold {DC_HIGHLIGHT}]✓[/] [{DC_TEXT}]{p.name}[/] [dim {DC_DIM}]->[/] [bold {DC_HIGHLIGHT}]{rp}[/]")
    if unresolved:
        lines += ["", f"[bold {DC_ORANGE}] {len(unresolved)} file(s) unmatched (skipped):[/]"]
        for p in unresolved:
            lines.append(f"  [dim {DC_ORANGE}]x {p.name}[/dim {DC_ORANGE}]")
    lines.append("")
    lines.append(f"[bold {DC_HIGHLIGHT}]Total: {len(resolved_files)} files will be built[/bold {DC_HIGHLIGHT}]")

    console.print(Panel("\n".join(lines), border_style=DC_BORDER, box=HEAVY_EDGE,
                        title=f"[bold black on {DC_HIGHLIGHT}] CSV PATH RESOLVER [/]"))

    confirm = console.input(f"\n[bold {DC_HIGHLIGHT}]Proceed with BUILD? (y/n): [/bold {DC_HIGHLIGHT}]").strip().lower()
    if confirm not in ('y', 'yes'):
        console.print(f"[{DC_ORANGE}]Cancelled[/]")
        return

    output_pak = output_dir / template_pak_path.name

    try:
        console.print(f"[bold {DC_HIGHLIGHT}]Building new PAK...[/]")

        template_pak = TencentPakFile(template_pak_path, is_od=True)
        version = template_pak._pak_info.version
        keystream = PakCrypto.zuc_keystream()

        raw = bytes(template_pak._file_content[
            template_pak._pak_info.index_offset:][:template_pak._pak_info.index_size])
        if template_pak._pak_info.index_encrypted:
            raw = PakCrypto.decrypt_index(raw, template_pak._pak_info)
        r = Reader(raw)
        mp_str = r.string()

        template_entry = None
        for _dp, _files in template_pak._index.items():
            for _n, _e in _files.items():
                template_entry = _e
                break
            if template_entry:
                break

        if template_entry is None:
            console.print(Panel(f"[{DC_RED}]Template PAK has no entries![/]", border_style=DC_RED))
            return

        out_buf = bytearray()
        new_files = []
        all_dirs = {}
        file_logs = []

        with Progress(
            SpinnerColumn(style=f"bold {DC_HIGHLIGHT}"),
            TextColumn(f"[bold {DC_HIGHLIGHT}][BUILD][/] {{task.description}}"),
            BarColumn(complete_style=f"bold {DC_TEXT}"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Building...", total=len(resolved_files))

            for p, fp in resolved_files:
                dir_key = str(PurePath(fp).parent).replace('\\', '/')
                if dir_key and not dir_key.endswith('/'):
                    dir_key += '/'
                if dir_key == '.':
                    dir_key = ''

                ne = _cp.copy(template_entry)
                ne.compressed_blocks = []
                
                if p.suffix.lower() == '.lua':
                    from_part9_prepare = prepare_lua_for_pak(p)
                    if from_part9_prepare is not None:
                        new_raw = from_part9_prepare
                    else:
                        console.print(f'  [dim {DC_RED}]✗ Skipped (Lua error): {p.name}[/]')
                        continue
                else:
                    new_raw = p.read_bytes()
                
                # Force encryption for Lua files
                if p.suffix.lower() == '.lua':
                    ne.encryption_method = 47
                    ne.encrypted = True
                    ne.compression_method = CM_NONE
                    ne.compression_block_size = 0

                pak_rel = PurePath(fp)

                # Force encryption for Lua files
                override = None
                if p.suffix.lower() == '.lua':
                    override = {
                        'compression_method': CM_NONE,
                        'encryption_method': 47,
                        'encrypted': True
                    }

                _write_entry_into_buf(out_buf, ne, new_raw, pak_rel, template_entry, template_pak._zstd_dict, override_settings=override)
                ne.unk2 = SHA1.new((mp_str + fp).lower().encode('utf-8')).digest()

                new_files.append(ne)

                # Capture log for dashboard
                enc_type = "NONE"
                if ne.encrypted:
                    if p.suffix.lower() == '.lua':
                        enc_type = "T24 (Lua BGMI)"
                    else:
                        enc_type = f"SM4 (Type {ne.encryption_method})"
                
                comp_type = "ZSTD" if ne.compression_method != 0 else "NONE"
                
                file_logs.append({
                    "name": fp,
                    "action": "🆕 ADDED",
                    "encryption": enc_type,
                    "compression": comp_type,
                    "size": len(new_raw)
                })
                all_dirs.setdefault(dir_key, {})[p.name] = ne
                progress.update(task, advance=1, description=p.name)

        id_to_idx = {id(ne): i for i, ne in enumerate(new_files)}
        idx = bytearray(_pw_string(mp_str))
        idx += struct.pack('<I', len(new_files))
        for ne in new_files:
            idx += _pw_entry(ne, version)
        idx += struct.pack('<Q', len(all_dirs))
        for dp_str, dir_files in all_dirs.items():
            idx += _pw_string(dp_str)
            idx += struct.pack('<Q', len(dir_files))
            for name, e in dir_files.items():
                idx += _pw_string(name)
                idx += struct.pack('<i', ~id_to_idx[id(e)])

        index_plain = bytes(idx)
        new_sha1 = SHA1.new(index_plain).digest()

        if template_pak._pak_info.index_encrypted:
            try:
                key = PakCrypto.rsa_extract(template_pak._pak_info.packed_key, RSA_MOD_1)
                iv = PakCrypto.rsa_extract(template_pak._pak_info.packed_iv, RSA_MOD_1)
                if key and iv and len(key) == 32 and len(iv) >= 16:
                    aes = AES.new(key, MODE_CBC, iv[:16])
                    pad_len = (-len(index_plain)) % AES.block_size or AES.block_size
                    index_bytes = aes.encrypt(index_plain + bytes([pad_len] * pad_len))
                else:
                    index_bytes = index_plain
            except Exception:
                index_bytes = index_plain
        else:
            index_bytes = index_plain

        new_idx_offset = len(out_buf)
        new_idx_size = len(index_bytes)
        out_buf += index_bytes

        orig_fc = template_pak._file_content
        footer_sz = TencentPakInfo._mem_size(version)
        new_footer = bytearray(orig_fc[-footer_sz:])
        h_key = struct.pack('<5I', *keystream[4:9])
        new_footer[-36:-16] = bytes(a ^ b for a, b in zip(new_sha1, h_key))
        new_footer[-16:-8] = ((new_idx_size ^ (keystream[10] << 32 | keystream[11])).to_bytes(8, 'little'))
        new_footer[-8:] = ((new_idx_offset ^ (keystream[0] << 32 | keystream[1])).to_bytes(8, 'little'))
        out_buf += new_footer

        with open(output_pak, 'wb') as f:
            f.write(out_buf)

        stats = {
            "files_processed": len(new_files),
            "compressed_count": sum(1 for e in new_files if e.compression_method != 0),
            "encrypted_count": sum(1 for e in new_files if e.encrypted),
            "original_size": len(template_pak._file_content),
            "new_size": len(out_buf),
            "orig_index_sha": template_pak._pak_info.index_hash.hex() if hasattr(template_pak._pak_info.index_hash, 'hex') else str(template_pak._pak_info.index_hash),
            "new_index_sha": new_sha1.hex(),
            "version": version,
            "output_path": str(output_pak),
            "file_logs": file_logs
        }
        return stats

        try:
            TencentPakFile(output_pak, is_od=True)
            console.print(Panel(f"[bold {DC_HIGHLIGHT}]VERIFICATION PASSED[/]",
                                border_style=DC_BORDER,
                                box=HEAVY_EDGE))
        except Exception as ve:
            console.print(Panel(f"[bold {DC_ORANGE}]Verify note: {ve}[/]",
                                border_style=DC_ORANGE,
                                box=HEAVY_EDGE))

    except Exception as e:
        console.print(Panel(f"[bold {DC_RED}]Build failed: {escape(str(e))}[/]",
                            border_style=DC_RED,
                            box=HEAVY_EDGE))
        import traceback
        traceback.print_exc()


# =====================================================================
# REPACK TO PATH VIA CSV (FIXED - Lua empty bug fix)
# =====================================================================

def repack_to_path_with_csv(pak_file, edit_dir, csv_dir, output_path):
    import copy as _cp

    if not download_csv_files(csv_dir):
        console.print(Panel(f"[bold {DC_RED}]CSV download failed![/]", border_style=DC_RED, box=HEAVY_EDGE))
        return 0

    selected_csv, is_bgmi, game_label = _select_csv_source(csv_dir)
    if selected_csv is None:
        return 0

    console.print(f"[bold {DC_HIGHLIGHT}]Loading {selected_csv.name}...[/]")
    file_path_map = _load_csv_path_map(selected_csv)
    if not file_path_map:
        console.print(Panel(f"[{DC_RED}]CSV is empty![/]", border_style=DC_RED))
        return 0
    console.print(f"[bold {DC_HIGHLIGHT}]Loaded {len(file_path_map)} paths from {game_label}[/]")

    edit_files = [p for p in edit_dir.rglob('*') if p.is_file()]
    if not edit_files:
        console.print(Panel(f"[{DC_RED}]No files in EDIT folder[/]", border_style=DC_RED))
        return 0

    resolved_files, unresolved = _resolve_paths_from_csv(edit_dir, file_path_map, is_bgmi)
    if not resolved_files:
        console.print(Panel(f"[{DC_RED}]No files matched CSV![/]", border_style=DC_RED, box=HEAVY_EDGE))
        return 0

    lines = [f"[bold {DC_HIGHLIGHT}]CSV: {game_label} ({selected_csv.name})[/bold {DC_HIGHLIGHT}]", ""]
    for p, rp in resolved_files:
        lines.append(f"  [bold {DC_HIGHLIGHT}]✓[/] [{DC_TEXT}]{p.name}[/] [dim {DC_DIM}]->[/] [bold {DC_HIGHLIGHT}]{rp}[/]")
    if unresolved:
        lines += ["", f"[bold {DC_ORANGE}] {len(unresolved)} unmatched:[/]"]
        for p in unresolved:
            lines.append(f"  [dim {DC_ORANGE}]x {p.name}[/dim {DC_ORANGE}]")
    lines.append("")
    lines.append(f"[bold {DC_HIGHLIGHT}]Total: {len(resolved_files)} files[/bold {DC_HIGHLIGHT}]")
    console.print(Panel("\n".join(lines), border_style=DC_BORDER, box=HEAVY_EDGE,
                        title=f"[bold black on {DC_HIGHLIGHT}] CSV PATH RESOLVER [/]"))

    confirm = console.input(f"\n[bold {DC_HIGHLIGHT}]Proceed with inject? (y/n): [/bold {DC_HIGHLIGHT}]").strip().lower()
    if confirm not in ('y', 'yes'):
        return 0

    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)
    version = pak_file._pak_info.version
    keystream = PakCrypto.zuc_keystream()
    orig_fc = pak_file._file_content

    pak_name_map = {}
    for dir_path, files in pak_file._index.items():
        for name, entry in files.items():
            full_path = str(PurePath(dir_path) / name).replace('\\', '/')
            pak_name_map.setdefault(name.lower(), []).append((full_path, entry))

    edited = {}
    for p, resolved_path in resolved_files:
        filename = p.name
        exact_entry = None
        actual_path = resolved_path

        for fp, entry in pak_name_map.get(filename.lower(), []):
            if fp.lower() == resolved_path.lower():
                exact_entry = entry
                actual_path = fp
                break

        if exact_entry is None:
            cands = pak_name_map.get(filename.lower(), [])
            if cands:
                actual_path, exact_entry = cands[0]

        if exact_entry is None:
            ext = p.suffix.lower()
            template = None
            for _dp, _files in pak_file._index.items():
                for _n, _e in _files.items():
                    if Path(_n).suffix.lower() == ext:
                        template = _e
                        break
                if template:
                    break
            if not template and pak_file._files:
                template = pak_file._files[0]
            if template:
                edited[actual_path] = (p, template, True)
        else:
            edited[actual_path] = (p, exact_entry, False)

    if not edited:
        console.print(Panel(f"[{DC_RED}]No files to repack![/]", border_style=DC_RED))
        return 0

    console.print(f"  [bold {DC_HIGHLIGHT}]Files to repack: {len(edited)}[/]")

    new_files = []
    file_logs = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}

    existing_full_paths = set()
    for dp_str, dir_files in all_dirs.items():
        for name in dir_files.keys():
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            existing_full_paths.add(full_path)

    out_buf = bytearray()

    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry))
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne

            if full_path in edited:
                p, template, is_new = edited[full_path]
                new_raw = p.read_bytes()
                pak_rel = PurePath(full_path)

                fresh = _cp.copy(old_entry)
                fresh.compressed_blocks = []

                _write_entry_into_buf(out_buf, fresh, new_raw, pak_rel, old_entry, pak_file._zstd_dict)
                fresh.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()

                for i, e in enumerate(new_files):
                    if id(e) == id(old_to_new[id(old_entry)]):
                        new_files[i] = fresh
                        old_to_new[id(old_entry)] = fresh
                        break

                # Capture log for dashboard
                enc_type = "NONE"
                if fresh.encrypted:
                    if p.suffix.lower() == '.lua':
                        enc_type = "T24 (Lua BGMI)"
                    else:
                        enc_type = f"SM4 (Type {fresh.encryption_method})"
                comp_type = "ZSTD" if fresh.compression_method != 0 else "NONE"
                file_logs.append({
                    "name": full_path,
                    "action": "🔄 EDITED",
                    "encryption": enc_type,
                    "compression": comp_type,
                    "size": len(new_raw)
                })

                console.print(f'[bold {DC_HIGHLIGHT}]Replaced:[/] {full_path} [dim]({fresh.size} bytes)[/dim]')
            else:
                if old_entry.compression_method == CM_NONE:
                    read_sz = (PakCrypto.align_encrypted_content_size(old_entry.size, old_entry.encryption_method)
                               if old_entry.encrypted else old_entry.size)
                    ne.offset = len(out_buf)
                    out_buf += bytes(orig_fc[old_entry.offset: old_entry.offset + read_sz])
                elif old_entry.compressed_blocks:
                    new_blks = []
                    for ob in old_entry.compressed_blocks:
                        unc = ob.end - ob.start
                        enc = (PakCrypto.align_encrypted_content_size(unc, old_entry.encryption_method)
                               if old_entry.encrypted else unc)
                        nb = PakCompressedBlock.__new__(PakCompressedBlock)
                        nb.start = len(out_buf)
                        nb.end = nb.start + unc
                        out_buf += bytes(orig_fc[ob.start: ob.start + enc])
                        new_blks.append(nb)
                    ne.compressed_blocks = new_blks
                    ne.offset = new_blks[0].start

    for resolved_path, (p, template, is_new) in edited.items():
        if resolved_path in existing_full_paths:
            continue

        ne = _cp.copy(template) if template else None
        if ne is None:
            continue
        ne.compressed_blocks = []
        new_raw = p.read_bytes()
        pak_rel = PurePath(resolved_path)

        _write_entry_into_buf(out_buf, ne, new_raw, pak_rel, template, pak_file._zstd_dict)
        ne.unk2 = SHA1.new((mp_str + resolved_path).lower().encode('utf-8')).digest()
        new_files.append(ne)

        # Capture log for dashboard
        enc_type = "NONE"
        if ne.encrypted:
            if p.suffix.lower() == '.lua':
                enc_type = "T24 (Lua BGMI)"
            else:
                enc_type = f"SM4 (Type {ne.encryption_method})"
        comp_type = "ZSTD" if ne.compression_method != 0 else "NONE"
        file_logs.append({
            "name": resolved_path,
            "action": "🆕 ADDED",
            "encryption": enc_type,
            "compression": comp_type,
            "size": len(new_raw)
        })

        dir_key = str(PurePath(resolved_path).parent).replace('\\', '/')
        if dir_key and not dir_key.endswith('/'):
            dir_key += '/'
        if dir_key == '.':
            dir_key = ''
        all_dirs.setdefault(dir_key, {})[p.name] = ne
        console.print(f'[bold {DC_HIGHLIGHT}]Added new:[/] {resolved_path} [dim]({ne.size} bytes)[/dim]')

    eidx = {id(new_files[i]): i for i in range(len(new_files))}
    idx = bytearray(_pw_string(mp_str))
    idx += struct.pack('<I', len(new_files))
    for ne in new_files:
        idx += _pw_entry(ne, version)
    idx += struct.pack('<Q', len(all_dirs))
    for dp_str, dir_files in all_dirs.items():
        idx += _pw_string(dp_str)
        idx += struct.pack('<Q', len(dir_files))
        for name, old_e in dir_files.items():
            idx += _pw_string(name)
            found_idx = eidx.get(id(old_e))
            if found_idx is None:
                for i, e in enumerate(new_files):
                    if e.offset == old_e.offset and e.size == old_e.size:
                        found_idx = i
                        break
            idx += struct.pack('<i', ~found_idx if found_idx is not None else -1)

    index_plain = bytes(idx)
    new_sha1 = SHA1.new(index_plain).digest()

    if pak_file._pak_info.index_encrypted:
        key = PakCrypto.rsa_extract(pak_file._pak_info.packed_key, RSA_MOD_1)
        iv = PakCrypto.rsa_extract(pak_file._pak_info.packed_iv, RSA_MOD_1)
        aes = AES.new(key, MODE_CBC, iv[:16])
        pad_len = (-len(index_plain)) % AES.block_size or AES.block_size
        index_bytes = aes.encrypt(index_plain + bytes([pad_len] * pad_len))
    else:
        index_bytes = index_plain

    new_idx_offset = len(out_buf)
    new_idx_size = len(index_bytes)
    out_buf += index_bytes

    footer_sz = TencentPakInfo._mem_size(version)
    new_footer = bytearray(orig_fc[-footer_sz:])
    h_key = struct.pack('<5I', *keystream[4:9])
    new_footer[-36:-16] = bytes(a ^ b for a, b in zip(new_sha1, h_key))
    new_footer[-16:-8] = ((new_idx_size ^ (keystream[10] << 32 | keystream[11])).to_bytes(8, 'little'))
    new_footer[-8:] = ((new_idx_offset ^ (keystream[0] << 32 | keystream[1])).to_bytes(8, 'little'))
    out_buf += new_footer

    with open(output_path, 'wb') as f:
        f.write(out_buf)

    # Read actual SHA1 from the written PAK file
    new_sha1_val = "N/A"
    try:
        with open(to_long_path(output_path), 'rb') as _f:
            _f.seek(0, 2)
            _fsize = _f.tell()
            _footer_sz = TencentPakInfo._mem_size(version)
            _f.seek(_fsize - _footer_sz)
            _footer_bytes = _f.read(_footer_sz)
            keystream = PakCrypto.zuc_keystream()
            h_key = struct.pack('<5I', *keystream[4:9])
            _hashed = bytes(a ^ b for a, b in zip(_footer_bytes[-36:-16], h_key))
            new_sha1_val = _hashed.hex()
    except Exception as _e:
        new_sha1_val = f"Error: {_e}"

    stats = {
        "files_processed": len(new_files),
        "compressed_count": sum(1 for e in new_files if e.compression_method != 0),
        "encrypted_count": sum(1 for e in new_files if e.encrypted),
        "original_size": len(orig_fc),
        "new_size": len(out_buf),
        "orig_index_sha": pak_file._pak_info.index_hash.hex() if hasattr(pak_file._pak_info.index_hash, 'hex') else str(pak_file._pak_info.index_hash),
        "new_index_sha": new_sha1_val,
        "version": version,
        "force_crc": False,
        "size_match": False,
        "file_logs": file_logs
    }
    return len(edited), stats


# =====================================================================
# REPACK FULL REBUILD
# =====================================================================

def repack_pak_file_full(pak_file, edited_root, output_path, target_path=None, force_add=False, force_crc=False, force_size=False, csv_path_map=None):
    import copy as _cp

    console.print(f'[bold {DC_HIGHLIGHT}]Full PAK Rebuild mode[/]')
    if target_path:
        console.print(f'[bold {DC_HIGHLIGHT}]Target path: {target_path}[/]')
    if force_crc or force_size:
        console.print(f'[bold {DC_HIGHLIGHT}]Ultimate Anti-Ban Shield active![/]')


    edit_files = [p for p in Path(edited_root).rglob('*') if p.is_file()]
    if not edit_files:
        console.print(f'[bold {DC_RED}]No files found in EDIT folder![/]')
        return 0, None
    console.print(f'[bold {DC_HIGHLIGHT}]Found {len(edit_files)} files in EDIT folder[/]')

    version = pak_file._pak_info.version
    keystream = PakCrypto.zuc_keystream()
    orig_fc = pak_file._file_content
    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)

    if target_path and force_add:
        target_path = target_path.replace('\\', '/')
        matched_dir = None
        for existing_dir in all_dirs.keys():
            if existing_dir.strip('/').lower() == target_path.strip('/').lower():
                matched_dir = existing_dir
                break
        if matched_dir:
            target_path = matched_dir
        else:
            target_path = target_path.strip('/') + '/'

    pak_name_map = {}
    for dir_path, files in pak_file._index.items():
        if isinstance(files, dict):
            items = files.items()
        else:
            items = [(getattr(e, 'name', ''), e) for e in files]
        for name, entry in items:
            if entry is None:
                continue
            full_path = str(PurePath(dir_path) / name).replace('\\', '/')
            pak_name_map.setdefault(str(name).lower(), []).append((full_path, entry))

    edited = {}
    for p in edit_files:
        fl = p.name.lower()
        found_match = False

        if fl in pak_name_map:
            cands = pak_name_map[fl]
            if target_path:
                target_candidates = [(fp, e) for fp, e in cands if target_path.strip('/') in fp]
                if target_candidates:
                    sz = p.stat().st_size
                    sm = [(fp, e) for fp, e in target_candidates if e.uncompressed_size == sz]
                    fp, ent = sm[0] if sm else target_candidates[0]
                    edited[fp] = (p, ent)
                    found_match = True

            if not found_match:
                sz = p.stat().st_size
                sm = [(fp, e) for fp, e in cands if e.uncompressed_size == sz]
                fp, ent = sm[0] if sm else cands[0]
                if target_path:
                    edited[f"{target_path.rstrip('/')}/{p.name}"] = (p, ent)
                else:
                    edited[fp] = (p, ent)
                found_match = True

        if not found_match and csv_path_map and p.name in csv_path_map:
            pak_path = csv_path_map[p.name]
            template_entry = None
            for dir_path, files in pak_file._index.items():
                if isinstance(files, dict):
                    items = files.items()
                else:
                    items = [(getattr(e, 'name', ''), e) for e in files]
                for name, entry in items:
                    if entry is None:
                        continue
                    template_entry = entry
                    break
                if template_entry:
                    break

            if template_entry is None:
                template_entry = TencentPakEntry.__new__(TencentPakEntry)
                template_entry.content_hash = b'\x00' * 20
                template_entry.offset = 0
                template_entry.uncompressed_size = 0
                template_entry.compression_method = CM_NONE
                template_entry.size = 0
                template_entry.unk1 = 0
                template_entry.unk2 = b'\x00' * 20
                template_entry.compressed_blocks = []
                template_entry.compression_block_size = 0
                template_entry.encrypted = False
                template_entry.encryption_method = 0
                template_entry.index_new_sep = 0

            edited[pak_path] = (p, template_entry)
            found_match = True

        if not found_match:
            stem = p.stem.lower()
            ext = p.suffix.lower()
            for dir_path, files in pak_file._index.items():
                if isinstance(files, dict):
                    items = files.items()
                else:
                    items = [(getattr(e, 'name', ''), e) for e in files]
                for name, entry in items:
                    if entry is None:
                        continue
                    if Path(str(name)).stem.lower() == stem and Path(str(name)).suffix.lower() == ext:
                        full_path = str(PurePath(dir_path) / name).replace('\\', '/')
                        if target_path:
                            edited[f"{target_path.rstrip('/')}/{p.name}"] = (p, entry)
                        else:
                            edited[full_path] = (p, entry)
                        found_match = True
                        break
                if found_match:
                    break

        if not found_match and force_add and target_path:
            template_entry = None
            for dir_path, files in pak_file._index.items():
                if isinstance(files, dict):
                    items = files.items()
                else:
                    items = [(getattr(e, 'name', ''), e) for e in files]
                for name, entry in items:
                    if entry is None:
                        continue
                    if Path(str(name)).suffix.lower() == p.suffix.lower():
                        template_entry = entry
                        break
                if template_entry:
                    break
            if not template_entry:
                for dir_path, files in pak_file._index.items():
                    if isinstance(files, dict):
                        items = files.items()
                    else:
                        items = [(getattr(e, 'name', ''), e) for e in files]
                    for name, entry in items:
                        if entry is None:
                            continue
                        template_entry = entry
                        break
                    if template_entry:
                        break
            if template_entry:
                new_fp = f"{target_path.rstrip('/')}/{p.name}"
                edited[new_fp] = (p, template_entry)

    if not edited:
        console.print(f'[bold {DC_RED}]No files to repack![/]')
        return 0, None
    console.print(f'  [bold {DC_HIGHLIGHT}]Files to repack: {len(edited)}[/]')

    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}

    edited_paths = {fp: p for fp, (p, _) in edited.items()}
    out_buf = bytearray()

    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne

            em = old_entry.encryption_method
            cm = old_entry.compression_method

            if full_path in edited_paths:
                p, template = edited[full_path]

                is_lua = p.suffix.lower() == '.lua'

                # Automatically process Lua files
                if is_lua:
                    new_raw = prepare_lua_for_pak(p)
                    if new_raw is None:
                        _copy_original_content(out_buf, pak_file, ne, old_entry)
                        continue
                else:
                    new_raw = p.read_bytes()

                pak_rel = PurePath(full_path)

                fresh = _cp.copy(old_entry)
                fresh.compressed_blocks = []

                # ── FIX: Force BGMI-standard settings for .lua files ──
                if is_lua:
                    fresh.encryption_method = 47
                    fresh.encrypted = True
                    fresh.compression_method = CM_NONE
                    fresh.compressed_blocks = []
                    fresh.compression_block_size = 0
                    console.print(f'  [dim cyan]Lua profile: SM4 type 47, no compression[/]')

                _write_entry_into_buf(out_buf, fresh, new_raw, pak_rel, fresh, pak_file._zstd_dict)
                fresh.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()

                if force_crc:
                    fresh.content_hash = old_entry.content_hash

                for i, e in enumerate(new_files):
                    if id(e) == id(old_to_new[id(old_entry)]):
                        new_files[i] = fresh
                        old_to_new[id(old_entry)] = fresh
                        break
                console.print(f'[bold {DC_HIGHLIGHT}]Processed: {full_path}[/]')

            else:
                if cm == CM_NONE:
                    read_sz = (PakCrypto.align_encrypted_content_size(old_entry.size, em)
                               if old_entry.encrypted else old_entry.size)
                    ne.offset = len(out_buf)
                    out_buf += bytes(orig_fc[old_entry.offset: old_entry.offset + read_sz])
                elif old_entry.compressed_blocks:
                    new_blks = []
                    for ob in old_entry.compressed_blocks:
                        unc = ob.end - ob.start
                        enc = (PakCrypto.align_encrypted_content_size(unc, em)
                               if old_entry.encrypted else unc)
                        nb = PakCompressedBlock.__new__(PakCompressedBlock)
                        nb.start = len(out_buf)
                        nb.end = nb.start + unc
                        out_buf += bytes(orig_fc[ob.start: ob.start + enc])
                        new_blks.append(nb)
                    ne.compressed_blocks = new_blks
                    ne.offset = new_blks[0].start

    if (target_path and force_add) or csv_path_map:
        for fp, (p, template) in edited.items():
            already_processed = False
            for dp_str, dir_files in all_dirs.items():
                for name in dir_files.keys():
                    if str(PurePath(dp_str) / name).replace('\\', '/') == fp:
                        already_processed = True
                        break
                if already_processed:
                    break
            if not already_processed:
                ne = _cp.copy(template)
                ne.compressed_blocks = []

                is_lua = p.suffix.lower() == '.lua'
                if is_lua:
                    new_raw = prepare_lua_for_pak(p)
                    if new_raw is None:
                        console.print(f'[bold {DC_RED}]✗ Skipped (Lua error): {fp}[/]')
                        continue
                else:
                    new_raw = p.read_bytes()

                pak_rel = PurePath(fp)

                # ── FIX: Force BGMI-standard settings for new .lua files ──
                if is_lua:
                    ne.encryption_method = 47
                    ne.encrypted = True
                    ne.compression_method = CM_NONE
                    ne.compressed_blocks = []
                    ne.compression_block_size = 0
                    console.print(f'  [dim cyan]New Lua profile: SM4 type 47, no compression[/]')

                _write_entry_into_buf(out_buf, ne, new_raw, pak_rel, ne, pak_file._zstd_dict)
                ne.unk2 = SHA1.new((mp_str + fp).lower().encode('utf-8')).digest()
                new_files.append(ne)

                if "/" in fp:
                    dp_key = fp.rsplit("/", 1)[0] + "/"
                    fname = fp.rsplit("/", 1)[1]
                else:
                    dp_key = ""
                    fname = fp

                if dp_key not in all_dirs:
                    all_dirs[dp_key] = {}
                all_dirs[dp_key][fname] = ne
                console.print(f'[bold {DC_HIGHLIGHT}]Added new: {fp}[/]')

    eidx = {id(new_files[i]): i for i in range(len(new_files))}
    old_id_to_new_idx = {id(pak_file._files[i]): i for i in range(len(pak_file._files))}

    idx = bytearray(_pw_string(mp_str))
    idx += struct.pack('<I', len(new_files))
    for ne in new_files:
        idx += _pw_entry(ne, version)
    idx += struct.pack('<Q', len(all_dirs))
    for dp_str, dir_files in all_dirs.items():
        idx += _pw_string(dp_str)
        idx += struct.pack('<Q', len(dir_files))
        for name, old_e in dir_files.items():
            idx += _pw_string(name)
            found_idx = eidx.get(id(old_e))
            if found_idx is None:
                found_idx = old_id_to_new_idx.get(id(old_e))
            if found_idx is None:
                copy_of = next((k for k, v in old_to_new.items() if v is old_e), None)
                if copy_of is not None:
                    found_idx = eidx.get(id(old_to_new[copy_of]))
            if found_idx is None:
                for i, e in enumerate(new_files):
                    if e.offset == old_e.offset and e.size == old_e.size:
                        found_idx = i
                        break
            if found_idx is not None:
                idx += struct.pack('<i', ~found_idx)
            else:
                idx += struct.pack('<i', -1)

    index_plain = bytes(idx)
    new_sha1 = SHA1.new(index_plain).digest()

    if pak_file._pak_info.index_encrypted:
        key = PakCrypto.rsa_extract(pak_file._pak_info.packed_key, RSA_MOD_1)
        iv = PakCrypto.rsa_extract(pak_file._pak_info.packed_iv, RSA_MOD_1)
        aes = AES.new(key, MODE_CBC, iv[:16])
        pad_len = (-len(index_plain)) % AES.block_size or AES.block_size
        index_bytes = aes.encrypt(index_plain + bytes([pad_len] * pad_len))
    else:
        index_bytes = index_plain

    new_idx_offset = len(out_buf)
    new_idx_size = len(index_bytes)
    out_buf += index_bytes

    footer_sz = TencentPakInfo._mem_size(version)
    new_footer = bytearray(orig_fc[-footer_sz:])
    h_key = struct.pack('<5I', *keystream[4:9])
    new_footer[-36:-16] = bytes(a ^ b for a, b in zip(new_sha1, h_key))
    new_footer[-16:-8] = ((new_idx_size ^ (keystream[10] << 32 | keystream[11])).to_bytes(8, 'little'))
    new_footer[-8:] = ((new_idx_offset ^ (keystream[0] << 32 | keystream[1])).to_bytes(8, 'little'))
    out_buf += new_footer

    with open(output_path, 'wb') as f:
        f.write(out_buf)
        if force_size:
            orig_size = len(orig_fc)
            new_size = len(out_buf)
            if new_size < orig_size:
                f.write(b'\x00' * (orig_size - new_size))
                new_size = orig_size

    stats = {
        "files_processed": len(new_files),
        "compressed_count": sum(1 for e in new_files if e.compression_method != 0),
        "encrypted_count": sum(1 for e in new_files if e.encrypted),
        "original_size": len(orig_fc),
        "new_size": new_size if force_size else len(out_buf),
        "orig_index_sha": pak_file._pak_info.index_hash.hex() if hasattr(pak_file._pak_info.index_hash, 'hex') else str(pak_file._pak_info.index_hash),
        "new_index_sha": new_sha1.hex(),
        "version": version,
        "force_crc": force_crc,
        "size_match": (new_size if force_size else len(out_buf)) == len(orig_fc)
    }
    return len(edited), stats



# =====================================================================
# END OF PART 4
# =====================================================================# =====================================================================
# PART 5 - MINI SKIN TOOL (Complete)
# =====================================================================

# =====================================================================
# MINI TOOL GLOBAL VARIABLES
# =====================================================================

mini_BASE_DIR = ""
mini_MINI_ICON_DIR = ""
mini_INPUT_DIR = ""
mini_OUTPUT_DIR = ""
mini_TXTS_DIR = ""
mini_MODSKIN_FILE = ""
mini_CHANGELOG_PATH = ""
mini_NULL_TXT_PATH = ""
mini_NULLED_TXT_PATH = ""
mini_ALL_TXT_PATH = ""
mini_INDEX_FILE_PATH = ""
mini_AUTO_THEME_BASE = ""
mini_AUTO_THEME_FILES = ""
mini_AUTO_THEME_RESULT = ""
mini_AUTO_THEME_TXT = ""
mini_LOBBY_FILE = ""
mini_HIT_EFFECT_DIR = ""
mini_LOOTCRATES_DIR = ""
mini_HIT_ORIG = ""
mini_HIT_MODIFIED = ""
mini_LOOT_ORIG = ""
mini_LOOT_MODIFIED = ""
mini_HIT_TXT_PATH = ""

mini_changelog_entries = []
mini_modified_blocks_map = {}
mini_BLOCK_SIZE = 65536


# =====================================================================
# MINI TOOL HELPERS
# =====================================================================

def mini_clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mini_display_tool_name():
    mini_clear_screen()
    try:
        width = os.get_terminal_size().columns
    except Exception:
        width = 80

    G = "\033[1;37m"   # White
    D = "\033[0;90m"   # Dim grey
    RESET = "\033[0m"

    banner_lines = [
        r"   _____ __ __  ____   _  __  ______ ____   ____   __ ",
        r"  / ___// //_/ /  _/  / |/ /  /_  __// __ \ / __ \ / / ",
        r"  \__ \/ ,<    / /   /  |/ /    / /  / / / // / / // /  ",
        r" ___/ / /| | _/ /   / /|  /    / /  / /_/ // /_/ // /___",
        r"/____/_/ |_|/___/  /_/ |_/    /_/   \____/ \____//_____/",
    ]

    for line in banner_lines:
        print((G + line + RESET).center(width))

    print()
    print((D + "              ~SKIN TOOL : SYSTEM DEVELOPER~" + RESET).center(width))
    print()


def mini_load_all_skins_data():
    """Load ALL.txt - Skin ID → Hex mapping."""
    skins_by_id = {}
    if not os.path.exists(mini_ALL_TXT_PATH):
        print(f"{colorama.Fore.RED}ALL.txt not found at {mini_ALL_TXT_PATH}")
        return skins_by_id
    try:
        with open(mini_ALL_TXT_PATH, "r", encoding="utf-8", errors='ignore') as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    skin_id = parts[0].strip()
                    hex_val = parts[1].strip().lower()
                    skin_name = parts[2].strip() if len(parts) >= 3 else ""
                    skins_by_id[skin_id] = {'hex': hex_val, 'name': skin_name}
    except Exception as e:
        print(f"{colorama.Fore.RED}Error loading ALL.txt: {e}")
    return skins_by_id


def mini_load_index_data():
    """Load index.txt - Skin Name → Index hex."""
    index_data = {}
    if not os.path.exists(mini_INDEX_FILE_PATH):
        print(f"{colorama.Fore.YELLOW}index.txt not found at {mini_INDEX_FILE_PATH}")
        return index_data
    try:
        with open(mini_INDEX_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) >= 4:
                    name = parts[2].strip()
                    index_hex = parts[3].strip().lower()
                    index_data.setdefault(name, []).append(index_hex)
    except Exception as e:
        print(f"{colorama.Fore.RED}Error loading index.txt: {e}")
    return index_data


def mini_load_modskin_pairs():
    """Load modskin.txt - ID pairs."""
    pairs = []
    if not os.path.exists(mini_MODSKIN_FILE):
        print(f"{colorama.Fore.RED}modskin.txt not found at {mini_MODSKIN_FILE}")
        return pairs
    try:
        with open(mini_MODSKIN_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = _ptre.split(r'[,\s\->]+', line)
                if len(parts) >= 2:
                    pairs.append((parts[0].strip(), parts[1].strip()))
    except Exception as e:
        print(f"{colorama.Fore.RED}Error loading modskin.txt: {e}")
    return pairs


def mini_mark_block_as_modified(file_path, byte_offset):
    block_idx = byte_offset // mini_BLOCK_SIZE
    if file_path not in mini_modified_blocks_map:
        mini_modified_blocks_map[file_path] = set()
    mini_modified_blocks_map[file_path].add(block_idx)
    if block_idx > 0:
        mini_modified_blocks_map[file_path].add(block_idx - 1)
    mini_modified_blocks_map[file_path].add(block_idx + 1)


def mini_write_changelog():
    os.makedirs(mini_OUTPUT_DIR, exist_ok=True)
    try:
        with open(mini_CHANGELOG_PATH, "w", encoding="utf-8") as f:
            f.write("Combined Mod Tool Changelog\n")
            f.write("==============================\n\n")
            for idx, entry in enumerate(mini_changelog_entries, 1):
                f.write("==============================\n")
                f.write(f"{idx}. ID PAIR: {entry['id_pair']}\n")
                f.write(f"FILE NAME: {entry['file_name']}\n")
                f.write(f"Source Item: {entry['source_item']}\n")
                f.write(f"Target Item: {entry['target_item']}\n")
                f.write(f"CHANGED HEX FROM: {entry['source_hex']} TO: {entry['target_hex']}\n")
                if entry.get('index_occurrences', 0) > 0:
                    f.write(f"INDEX CHANGED FROM: {entry['source_index']} TO: {entry['target_index']} ({entry['index_occurrences']} occurrence(s))\n")
                elif entry.get('index_failure_reason'):
                    f.write(f"Index replacement note: {entry['index_failure_reason']}\n")
                f.write("==============================\n\n")
    except Exception:
        pass


def mini_remove_readonly(func, path, excinfo):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass


def mini_copy_files_to_output():
    """Step 1: Copy files from INPUT to OUTPUT."""
    print(f"\n{colorama.Fore.CYAN}Step 1: Copying files from INPUT to OUTPUT...")

    if not os.path.exists(mini_INPUT_DIR):
        print(f"{colorama.Fore.RED}INPUT directory not found: {mini_INPUT_DIR}")
        return False

    if os.path.exists(mini_OUTPUT_DIR):
        try:
            shutil.rmtree(mini_OUTPUT_DIR, onerror=mini_remove_readonly)
        except Exception as e:
            print(f"{colorama.Fore.RED}Error cleaning OUTPUT: {e}")
            return False

    try:
        shutil.copytree(mini_INPUT_DIR, mini_OUTPUT_DIR)
        file_count = sum(len(files) for _, _, files in os.walk(mini_OUTPUT_DIR))
        print(f"{colorama.Fore.GREEN}Copied {file_count} files to OUTPUT directory")
        return True
    except Exception as e:
        print(f"{colorama.Fore.RED}Error copying files: {e}")
        return False


# =====================================================================
# MOD SKIN PROCESSING
# =====================================================================

def mini_process_mod_skin():
    global mini_modified_blocks_map
    mini_modified_blocks_map = {}

    print(f"\n{colorama.Fore.LIGHTBLUE_EX}Step 2: Processing Mod Skin replacements...")

    mode_str = "REPLACE (One-Way)"
    print(f"{colorama.Fore.CYAN}Mode: {colorama.Fore.LIGHTGREEN_EX}{mode_str} [AUTO SELECTED]")

    skins_data = mini_load_all_skins_data()
    index_data = mini_load_index_data()
    id_pairs = mini_load_modskin_pairs()

    if not id_pairs:
        print(f"{colorama.Fore.RED}No ID pairs found in modskin.txt")
        return

    print(f"{colorama.Fore.LIGHTGREEN_EX}Found {len(id_pairs)} ID pairs to process")

    resolved_ops = []
    missing_ids = set()

    for s_id, t_id in id_pairs:
        if s_id not in skins_data:
            missing_ids.add(s_id)
            continue
        if t_id not in skins_data:
            missing_ids.add(t_id)
            continue

        s_hex = skins_data[s_id]['hex']
        s_name = skins_data[s_id]['name']
        t_hex = skins_data[t_id]['hex']
        t_name = skins_data[t_id]['name']

        resolved_ops.append({
            'search_hex': t_hex,
            'replace_hex': s_hex,
            'search_name': t_name,
            'replace_name': s_name,
            'label': f"{s_id} -> {t_id}",
            'op_type': "REPLACE"
        })

    if missing_ids:
        print(f"{colorama.Fore.LIGHTBLUE_EX}Warning: {len(missing_ids)} IDs not found in ALL.txt")

    if not resolved_ops:
        print(f"{colorama.Fore.RED}Empty operational queue. Nothing to process.")
        return

    modified_files = 0

    for root, dirs, files in os.walk(mini_OUTPUT_DIR):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.lower().endswith('.txt'):
                continue

            try:
                with open(file_path, 'rb') as f:
                    content_bytes = f.read()
            except Exception:
                continue

            hex_data = content_bytes.hex()
            file_modified = False

            for op in resolved_ops:
                s_hex = op['search_hex']
                r_hex = op['replace_hex']
                s_name = op['search_name']
                r_name = op['replace_name']

                if s_hex not in hex_data:
                    continue

                occ = hex_data.count(s_hex)
                if occ >= 2:
                    first_pos = hex_data.find(s_hex)
                    second_pos = hex_data.find(s_hex, first_pos + len(s_hex))

                    if second_pos != -1:
                        hex_data = hex_data[:second_pos] + r_hex + hex_data[second_pos + len(s_hex):]
                        file_modified = True
                        mini_mark_block_as_modified(file_path, second_pos // 2)

                        idx_occ = 0
                        idx_reason = ""
                        mod_idx_from = "N/A"
                        mod_idx_to = "N/A"

                        if s_name in index_data and r_name in index_data:
                            search_candidates = index_data[s_name]
                            replacement_index = index_data[r_name][0]
                            window_start = max(0, first_pos - 60)
                            window = hex_data[window_start:first_pos]
                            found = False

                            for candidate in search_candidates:
                                if candidate in window:
                                    mod_idx_from = candidate
                                    mod_idx_to = replacement_index
                                    window_replaced = window.replace(candidate, replacement_index, 1)
                                    local_idx = window.find(candidate)
                                    real_idx = window_start + local_idx
                                    hex_data = hex_data[:window_start] + window_replaced + hex_data[first_pos:]
                                    idx_occ = 1
                                    found = True
                                    mini_mark_block_as_modified(file_path, real_idx // 2)
                                    break

                            if not found:
                                idx_reason = "Index hex not found in window"
                        else:
                            idx_reason = "Index names missing"

                        rel_path = os.path.relpath(file_path, mini_OUTPUT_DIR)
                        mini_changelog_entries.append({
                            'id_pair': f"{op['label']} ({op['op_type']})",
                            'file_name': rel_path,
                            'source_item': f"{s_name} [Found]",
                            'target_item': f"{r_name} [Applied]",
                            'source_hex': s_hex,
                            'target_hex': r_hex,
                            'source_index': mod_idx_from,
                            'target_index': mod_idx_to,
                            'index_occurrences': idx_occ,
                            'index_failure_reason': idx_reason
                        })

            if file_modified:
                try:
                    with open(file_path, 'wb') as f:
                        f.write(bytes.fromhex(hex_data))
                    modified_files += 1
                except Exception:
                    pass

    print(f"{colorama.Fore.LIGHTGREEN_EX}Modified {modified_files} files")


# =====================================================================
# SIZE FIX (NULLING)
# =====================================================================

def mini_build_pattern_groups(hex_list):
    groups = {}
    for hx in hex_list:
        try:
            b = bytes.fromhex(hx)
        except ValueError:
            continue
        if not b:
            continue
        groups.setdefault(len(b), set()).add(b)
    return groups


def mini_null_bytes_in_file(file_path, pattern_groups, dirty_blocks, target_counts={2}):
    try:
        data = Path(file_path).read_bytes()
    except Exception:
        return 0

    ba = bytearray(data)
    total_hits = 0
    modified = False
    file_size = len(ba)

    for block_idx in dirty_blocks:
        start_offset = block_idx * mini_BLOCK_SIZE
        if start_offset >= file_size:
            continue
        end_offset = min(start_offset + mini_BLOCK_SIZE, file_size)
        block_len = end_offset - start_offset
        block_mv = memoryview(ba)[start_offset:end_offset]

        for L, patterns in pattern_groups.items():
            if L <= 0 or block_len < L:
                continue
            zero = b"\x00" * L
            occurrences = {}
            i = 0
            end = block_len - L

            while i <= end:
                chunk = bytes(block_mv[i:i + L])
                if chunk in patterns:
                    if chunk not in occurrences:
                        occurrences[chunk] = []
                    occurrences[chunk].append(i)
                    i += L
                else:
                    i += 1

            for pat, positions in occurrences.items():
                count = len(positions)
                if count in target_counts:
                    for pos in positions:
                        abs_pos = start_offset + pos
                        ba[abs_pos:abs_pos + L] = zero
                    total_hits += count
                    modified = True

    if modified:
        Path(file_path).write_bytes(ba)
    return total_hits


def mini_process_size_fix():
    skins_data = mini_load_all_skins_data()
    if not skins_data:
        return

    protected_ids = set()
    protected_hexes_from_ids = set()

    if os.path.exists(mini_MODSKIN_FILE):
        try:
            with open(mini_MODSKIN_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = _ptre.split(r'[,\s\->]+', line)
                    for part in parts:
                        part = part.strip()
                        if part:
                            protected_ids.add(part)
        except Exception:
            pass

    for skin_id in protected_ids:
        if skin_id in skins_data:
            protected_hex = skins_data[skin_id]['hex']
            protected_hexes_from_ids.add(protected_hex.lower())

    valid_entries = []
    exclude_keywords = {"face", "hair", "head", "male", "female"}

    for skin_id, info in skins_data.items():
        hex_code = info['hex']
        skin_name = info['name'].lower()
        if skin_id in protected_ids:
            continue
        if any(keyword in skin_name for keyword in exclude_keywords):
            continue
        if "0000" in hex_code:
            continue
        valid_entries.append((hex_code, skin_name))

    exclude_hexes = set()
    for entry in mini_changelog_entries:
        exclude_hexes.add(entry.get('source_hex', '').lower())
        exclude_hexes.add(entry.get('target_hex', '').lower())
        if entry.get('source_index', "N/A") != "N/A":
            exclude_hexes.add(entry['source_index'].lower())
        if entry.get('target_index', "N/A") != "N/A":
            exclude_hexes.add(entry['target_index'].lower())

    exclude_hexes.update(protected_hexes_from_ids)

    print(f"{colorama.Fore.CYAN}Nulling Mode: {colorama.Fore.LIGHTGREEN_EX}AUTO NULL SYSTEM [AUTO SELECTED]")

    target_counts = {2}
    final_hexes = []
    for hx, name in valid_entries:
        if hx in exclude_hexes:
            continue
        final_hexes.append(hx)

    pattern_groups = mini_build_pattern_groups(final_hexes)

    files_to_process = []
    for root, dirs, files in os.walk(mini_OUTPUT_DIR):
        for file_name in files:
            if not file_name.lower().endswith('.txt'):
                files_to_process.append(os.path.join(root, file_name))

    total_nulled = 0
    files_modified = 0

    with console.status("[bold cyan]Scanning and Nulling Hex values...[/]", spinner="dots"):
        for file_path in files_to_process:
            dirty_blocks = mini_modified_blocks_map.get(file_path, set())
            if not dirty_blocks:
                continue
            hits = mini_null_bytes_in_file(file_path, pattern_groups, dirty_blocks, target_counts)
            if hits > 0:
                files_modified += 1
                total_nulled += hits

    print()
    try:
        with open(mini_NULLED_TXT_PATH, 'w', encoding='utf-8') as f:
            f.write("Nulled Hex Values Report\n========================\n")
            f.write(f"Files modified: {files_modified}\n")
            f.write(f"Unique hex values nulled: {len(final_hexes)}\n")
            f.write(f"Total occurrences replaced: {total_nulled}\n")
    except Exception:
        pass

    print(f"{colorama.Fore.LIGHTGREEN_EX}Size fix processing complete.")


# =====================================================================
# HIT EFFECT & LOOTCRATES
# =====================================================================

def mini_run_hit_loot_tool():
    mini_display_tool_name()

    zsdic_console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]HIT EFFECT & LOOTCRATES TOOL[/bold {DC_HIGHLIGHT}]\n"
        f"[dim]ID pairs from modskin.txt | Files from MINI[/dim]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE
    ))

    global game_key, mini_BASE_DIR

    if 'game_key' not in globals() or game_key not in ["BGMI", "PUBG"]:
        game_key = "BGMI"

    game_folder = f"{game_key}_SKIN"
    game_base = os.path.join(BASE_DIR_NAME, "SKIN_TOOL", game_folder)

    zsdic_base = os.path.join(game_base, "ZSDIC")
    zsdic_modskin = os.path.join(zsdic_base, "modskin.txt")

    mini_base = os.path.join(game_base, "MINI")
    mini_icon = os.path.join(mini_base, "MINI_ICON")
    mini_txts = os.path.join(mini_icon, "TXTS")
    mini_all = os.path.join(mini_txts, "ALL.txt")

    mini_HIT_ORIG = os.path.join(mini_base, "HIT EFFECT", "org")
    mini_HIT_MODIFIED = os.path.join(mini_base, "HIT EFFECT", "modified")
    mini_LOOT_ORIG = os.path.join(mini_base, "LOOTCRATES", "org")
    mini_LOOT_MODIFIED = os.path.join(mini_base, "LOOTCRATES", "modified")

    if not os.path.exists(mini_all):
        zsdic_console.print(Panel(
            f"[red]ALL.txt not found![/red]\n"
            f"[dim]Expected: {mini_all}[/dim]",
            border_style=DC_RED,
            box=ROUNDED
        ))
        return

    id_pairs = []

    if os.path.exists(zsdic_modskin):
        with open(zsdic_modskin, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = _ptre.split(r'[,\s]+', line.strip())
                if len(parts) >= 2:
                    id_pairs.append((parts[0].strip(), parts[1].strip()))

        zsdic_console.print(Panel(
            f"[bold {DC_HIGHLIGHT}]Loaded {len(id_pairs)} pairs from modskin.txt[/bold {DC_HIGHLIGHT}]",
            border_style=DC_BORDER,
            box=ROUNDED
        ))
    else:
        zsdic_console.print(Panel(
            f"[red]modskin.txt not found![/red]",
            border_style=DC_RED,
            box=ROUNDED
        ))
        return

    if not id_pairs:
        zsdic_console.print(Panel(
            f"[{DC_ORANGE}]No ID pairs found in modskin.txt[/]",
            border_style=DC_ORANGE,
            box=ROUNDED
        ))
        return

    id_to_entry = {}
    by_name = {}

    with open(mini_all, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            parts = line.strip().split("|")
            if len(parts) >= 3:
                idv = parts[0].strip()
                hx = parts[1].strip().lower()
                name = parts[2].strip()
                id_to_entry[idv] = {"hex": hx, "name": name, "base": name}
                by_name.setdefault(name, {})[0] = hx

    zsdic_console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]Loaded {len(id_to_entry)} entries from ALL.txt[/bold {DC_HIGHLIGHT}]",
        border_style=DC_BORDER,
        box=ROUNDED
    ))

    pairs_hit, pairs_loot = [], []

    for a_raw, b_raw in id_pairs:
        if a_raw not in id_to_entry:
            continue

        first_hex = id_to_entry[a_raw]["hex"]

        if b_raw in id_to_entry:
            hit_hex = id_to_entry[b_raw]["hex"]
            loot_hex = id_to_entry[b_raw]["hex"]
        else:
            hit_hex = b_raw
            loot_hex = b_raw

        pairs_hit.append((first_hex, hit_hex))
        if len(first_hex) == len(loot_hex):
            pairs_loot.append((first_hex, loot_hex))

    with Live(refresh_per_second=30, console=zsdic_console) as live:
        for i in range(101):
            if i % 5 == 0:
                bar_length = 30
                filled = int((i / 100) * bar_length)
                bar = "#" * filled + "-" * (bar_length - filled)

                progress_text = (
                    f"[bold {DC_HIGHLIGHT}]Processing...[/bold {DC_HIGHLIGHT}]\n\n"
                    f"[bold {DC_HIGHLIGHT}]{bar}[/] [bold {DC_TEXT}]{i}%[/bold {DC_TEXT}]\n"
                    f"[dim]{i}% complete[/dim]"
                )

                live.update(Panel(
                    progress_text,
                    title="[bold black on {DC_HIGHLIGHT}] PROCESSING [/]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT),
                    border_style=DC_BORDER,
                    box=HEAVY_EDGE
                ))
            time.sleep(0.02)

    for path in [mini_HIT_MODIFIED, mini_LOOT_MODIFIED]:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
            except Exception:
                pass
        os.makedirs(path, exist_ok=True)

    def process_files(orig_dir, mod_dir, pairs):
        if not os.path.exists(orig_dir):
            return 0

        files = []
        for r, _, fs in os.walk(orig_dir):
            for fn in fs:
                files.append(os.path.join(r, fn))

        if not files:
            return 0

        count = 0
        for src in files:
            try:
                with open(src, 'rb') as fh:
                    data = fh.read()
            except Exception:
                continue

            orig = data
            for first_hex, second_hex in pairs:
                try:
                    to_b = bytes.fromhex(second_hex)
                    from_raw = bytes.fromhex(first_hex)
                except Exception:
                    continue

                if len(from_raw) < len(to_b):
                    replacement = from_raw + b'\x00' * (len(to_b) - len(from_raw))
                elif len(from_raw) > len(to_b):
                    replacement = from_raw[:len(to_b)]
                else:
                    replacement = from_raw

                if data.count(to_b):
                    data = data.replace(to_b, replacement)
                if data.count(to_b[::-1]):
                    data = data.replace(to_b[::-1], replacement[::-1])

            if data != orig:
                rel = os.path.relpath(src, orig_dir)
                outp = os.path.join(mod_dir, rel)
                os.makedirs(os.path.dirname(outp), exist_ok=True)
                with open(outp, 'wb') as outfh:
                    outfh.write(data)
                count += 1

        return count

    hit_count = process_files(mini_HIT_ORIG, mini_HIT_MODIFIED, pairs_hit)
    loot_count = process_files(mini_LOOT_ORIG, mini_LOOT_MODIFIED, pairs_loot)

    zsdic_console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]Modified {hit_count} HIT files & {loot_count} LOOT files.[/bold {DC_HIGHLIGHT}]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE
    ))


# =====================================================================
# AUTO THEME CHANGER
# =====================================================================

def mini_run_auto_theme():
    DEFAULT_HEX = "7480100C"

    while True:
        mini_display_tool_name()

        menu_table = Table(show_header=False, box=SIMPLE, expand=True)
        menu_table.add_column("OPT", style=f"bold {DC_HIGHLIGHT}", justify="center", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_HIGHLIGHT}")

        menu_table.add_row("1", f"[bold {DC_HIGHLIGHT}]SWAP LOBBY INDEX[/]")
        menu_table.add_row("2", f"[bold {DC_RED}]BACK TO MAIN MENU[/]")

        console.print(Panel(
            menu_table,
            border_style=DC_BORDER,
            box=HEAVY_EDGE,
            title=f"[bold black on {DC_HIGHLIGHT}] AUTO THEME CHANGER [/]"
        ))

        choice = safe_input(f"[bold {DC_HIGHLIGHT}]ENTER COMMAND > [/bold {DC_HIGHLIGHT}]").strip()

        if choice == "1":
            lobbies = []
            try:
                with open(mini_LOBBY_FILE, "r") as file:
                    for line in file:
                        parts = line.strip().split("|")
                        if len(parts) == 3:
                            lobbies.append((parts[1].strip(), parts[2].strip()))
            except FileNotFoundError:
                pass

            if not lobbies:
                console.print(f"[red]lobby.txt not found or empty.[/red]")
                time.sleep(1)
                continue

            console.print(f"\n[bold {DC_HIGHLIGHT}]-- AVAILABLE LOBBIES --[/bold {DC_HIGHLIGHT}]\n")
            for i, (_, name) in enumerate(lobbies, 1):
                console.print(f"[bold {DC_TEXT}]{i:02d}.[/] [bold {DC_HIGHLIGHT}]{name}[/]")

            lobby_choice = safe_input(f"\n[bold {DC_HIGHLIGHT}]Select a lobby theme ID[/bold {DC_HIGHLIGHT}]")
            try:
                lobby_idx = int(lobby_choice) - 1
                if 0 <= lobby_idx < len(lobbies):
                    target_hex, lobby_name = lobbies[lobby_idx]

                    with console.status(f"[bold {DC_HIGHLIGHT}]Applying {lobby_name} theme...[/]"):
                        default_hex_bytes = bytes.fromhex(DEFAULT_HEX)
                        target_hex_bytes = bytes.fromhex(target_hex)
                        for filename in os.listdir(mini_AUTO_THEME_FILES):
                            file_path = os.path.join(mini_AUTO_THEME_FILES, filename)
                            with open(file_path, "rb") as file:
                                file_data = file.read()
                            updated_data = bytearray(file_data)

                            default_pos = target_pos = None
                            for i in range(len(file_data) - len(default_hex_bytes), 7, -1):
                                if file_data[i:i + len(default_hex_bytes)] == default_hex_bytes:
                                    default_index = file_data[i - 8]
                                    default_pos = i - 8
                                    break
                            for i in range(len(file_data) - len(target_hex_bytes), 7, -1):
                                if file_data[i:i + len(target_hex_bytes)] == target_hex_bytes:
                                    target_index = file_data[i - 8]
                                    target_pos = i - 8
                                    break

                            if default_pos is not None and target_pos is not None:
                                updated_data[default_pos] = target_index
                                updated_data[target_pos] = default_index
                                result_path = os.path.join(mini_AUTO_THEME_RESULT, filename)
                                os.makedirs(mini_AUTO_THEME_RESULT, exist_ok=True)
                                with open(result_path, "wb") as file:
                                    file.write(updated_data)

                    console.print(f"[bold {DC_HIGHLIGHT}]SUCCESS: Lobby Swap Applied![/]")
                else:
                    console.print(f"[red]Invalid ID.[/red]")
            except ValueError:
                console.print(f"[red]Invalid input.[/red]")
        elif choice == "2":
            break
        time.sleep(1)


# =====================================================================
# FULL FLOW (Master Pipeline)
# =====================================================================

def mini_full_flow():
    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]REPSHMET & SIZE-FIX MASTER ENGINE[/bold {DC_HIGHLIGHT}]\n\n"
        f"[bold {DC_TEXT}]M A S T E R   A U T O M A T E D   P I P E L I N E[/bold {DC_TEXT}]\n"
        f"[dim {DC_DIM}]----------------------------------------------[/dim {DC_DIM}]\n"
        f"[bold {DC_TEXT}]Pipeline Status : [bold {DC_HIGHLIGHT}]READY FOR EXECUTION[/][/bold {DC_TEXT}]",
        expand=True,
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
        padding=(1, 2),
        title=f"[bold black on {DC_HIGHLIGHT}] MASTER ENGINE INITIALIZED [/]",
        title_align="center"
    ))

    if not mini_copy_files_to_output():
        console.print(Panel(f"[bold {DC_RED}]SYNC FAILED[/]", border_style=DC_RED, expand=True))
        return

    mini_process_mod_skin()
    mini_write_changelog()
    mini_process_size_fix()

    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]MASTER PIPELINE EXECUTED SUCCESSFULLY![/]\n\n"
        f"  [dim {DC_DIM}]* Pipeline Status      :[/dim {DC_DIM}] [bold {DC_HIGHLIGHT}]SYSTEM FULLY OPTIMIZED[/]\n"
        f"  [dim {DC_DIM}]* Asset Verification   :[/dim {DC_DIM}] [bold {DC_TEXT}]ALL ASSETS VERIFIED & PATCHED[/]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
        expand=True,
        title=f"[bold black on {DC_HIGHLIGHT}] EXECUTION COMPLETED [/]",
        padding=(1, 2)
    ))

    safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter to continue...[/]")


# =====================================================================
# MINI MENU & MAIN
# =====================================================================

def mini_menu():
    while True:
        mini_display_tool_name()
        b_color = DC_HIGHLIGHT

        menu_table = Table(
            show_header=True,
            header_style=f"bold black on {DC_HIGHLIGHT}",
            box=DOUBLE_EDGE,
            title="[reverse]  MINI SKIN TOOL  [/]",
            border_style=DC_BORDER,
            expand=True
        )
        menu_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_TEXT}")
        menu_table.add_column("DESCRIPTION", style=f"dim {DC_DIM}")

        menu_table.add_row(
            "1",
            f"[bold {DC_HIGHLIGHT}]MOD SKIN & SIZE FIX[/]",
            f"[dim]VIP Mod Skin & Size Fix[/dim]"
        )
        menu_table.add_row(
            "2",
            f"[bold {DC_HIGHLIGHT}]HIT EFFECT & LOOTCRATES[/]",
            f"[dim]Change hit effects & loot crates[/dim]"
        )
        menu_table.add_row(
            "3",
            f"[bold {DC_HIGHLIGHT}]AUTO THEME CHANGER[/]",
            f"[dim]Swap lobby index theme[/dim]"
        )
        menu_table.add_row(
            "0",
            f"[bold {DC_RED}]BACK[/]",
            f"[dim]Return to Main Menu[/dim]"
        )

        console.print(Panel(menu_table, border_style=DC_BORDER, box=HEAVY_EDGE))

        choice = safe_input(f"[bold {DC_HIGHLIGHT}]ENTER COMMAND > [/bold {DC_HIGHLIGHT}]").strip()

        if choice == "1":
            mini_full_flow()
        elif choice == "2":
            mini_run_hit_loot_tool()
            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter to continue...[/]")
        elif choice == "3":
            mini_run_auto_theme()
        elif choice == "0":
            break
        else:
            console.print(f"[bold {DC_RED}]Invalid! Enter 0, 1, 2, or 3[/]")
            time.sleep(1)


def mini_skin_tool_main(data_path):
    global mini_BASE_DIR, mini_MINI_ICON_DIR, mini_INPUT_DIR, mini_OUTPUT_DIR
    global mini_TXTS_DIR, mini_MODSKIN_FILE, mini_CHANGELOG_PATH
    global mini_NULL_TXT_PATH, mini_NULLED_TXT_PATH, mini_ALL_TXT_PATH
    global mini_INDEX_FILE_PATH, mini_AUTO_THEME_BASE, mini_AUTO_THEME_FILES
    global mini_AUTO_THEME_RESULT, mini_AUTO_THEME_TXT, mini_LOBBY_FILE
    global mini_HIT_EFFECT_DIR, mini_LOOTCRATES_DIR, mini_HIT_ORIG
    global mini_HIT_MODIFIED, mini_LOOT_ORIG, mini_LOOT_MODIFIED
    global mini_HIT_TXT_PATH, game_key

    while True:
        mini_clear_screen()
        print_banner()

        select_table = Table(
            show_header=True,
            header_style=f"bold black on {DC_HIGHLIGHT}",
            box=DOUBLE_EDGE,
            title="[reverse]  SELECT GAME  [/]",
            border_style=DC_BORDER,
            expand=True
        )
        select_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
        select_table.add_column("GAME", style=f"bold {DC_TEXT}")
        select_table.add_column("DESCRIPTION", style=f"dim {DC_DIM}")
        select_table.add_row("1", "BGMI_SKIN", "Mod BGMI Skins")
        select_table.add_row("2", "PUBG_SKIN", "Mod PUBG Skins")
        select_table.add_row("0", f"[{DC_RED}]BACK[/]", "Return")
        console.print(Panel(select_table, border_style=DC_BORDER, box=HEAVY_EDGE))

        game_choice = safe_input(f"[bold {DC_HIGHLIGHT}]SELECT (1/2/0) > [/bold {DC_HIGHLIGHT}]").strip()

        if game_choice == "0":
            return
        if game_choice not in ("1", "2"):
            console.print(f"[bold {DC_RED}]Invalid![/]")
            time.sleep(1)
            continue

        selected_game = "BGMI_SKIN" if game_choice == "1" else "PUBG_SKIN"
        game_key = "BGMI" if game_choice == "1" else "PUBG"
        GAME_BASE = data_path / "SKIN_TOOL" / selected_game

        mini_BASE_DIR = str(GAME_BASE / "MINI")
        mini_MINI_ICON_DIR = str(Path(mini_BASE_DIR) / "MINI_ICON")
        mini_INPUT_DIR = str(Path(mini_MINI_ICON_DIR) / "INPUT")
        mini_OUTPUT_DIR = str(Path(mini_MINI_ICON_DIR) / "OUTPUT")
        mini_TXTS_DIR = str(Path(mini_MINI_ICON_DIR) / "TXTS")
        mini_MODSKIN_FILE = str(Path(mini_BASE_DIR) / "modskin.txt")
        mini_CHANGELOG_PATH = str(Path(mini_BASE_DIR) / "changelog.txt")
        mini_NULL_TXT_PATH = str(Path(mini_TXTS_DIR) / "null.txt")
        mini_NULLED_TXT_PATH = str(Path(mini_BASE_DIR) / "nulled.txt")
        mini_ALL_TXT_PATH = str(Path(mini_TXTS_DIR) / "ALL.txt")
        mini_INDEX_FILE_PATH = str(Path(mini_TXTS_DIR) / "index.txt")
        mini_AUTO_THEME_BASE = str(Path(mini_BASE_DIR) / "AUTO_THEME")
        mini_AUTO_THEME_FILES = str(Path(mini_AUTO_THEME_BASE) / "FILES")
        mini_AUTO_THEME_RESULT = str(Path(mini_AUTO_THEME_BASE) / "MODIFIED")
        mini_AUTO_THEME_TXT = str(Path(mini_AUTO_THEME_BASE) / "TXT")
        mini_LOBBY_FILE = str(Path(mini_AUTO_THEME_TXT) / "lobby.txt")
        mini_HIT_EFFECT_DIR = str(Path(mini_BASE_DIR) / "HIT EFFECT")
        mini_LOOTCRATES_DIR = str(Path(mini_BASE_DIR) / "LOOTCRATES")
        mini_HIT_ORIG = str(Path(mini_HIT_EFFECT_DIR) / "org")
        mini_HIT_MODIFIED = str(Path(mini_HIT_EFFECT_DIR) / "modified")
        mini_LOOT_ORIG = str(Path(mini_LOOTCRATES_DIR) / "org")
        mini_LOOT_MODIFIED = str(Path(mini_LOOTCRATES_DIR) / "modified")
        mini_HIT_TXT_PATH = str(Path(mini_BASE_DIR) / "hit.txt")

        for d in [mini_BASE_DIR, mini_MINI_ICON_DIR, mini_INPUT_DIR, mini_OUTPUT_DIR,
                  mini_TXTS_DIR, mini_AUTO_THEME_BASE, mini_AUTO_THEME_FILES,
                  mini_AUTO_THEME_RESULT, mini_AUTO_THEME_TXT, mini_HIT_EFFECT_DIR,
                  mini_LOOTCRATES_DIR, mini_HIT_ORIG, mini_HIT_MODIFIED,
                  mini_LOOT_ORIG, mini_LOOT_MODIFIED]:
            Path(d).mkdir(parents=True, exist_ok=True)

        mini_menu()
        return


# =====================================================================
# END OF PART 5
# =====================================================================# =====================================================================
# PART 6 - ZSDIC SKIN TOOL (Complete)
# =====================================================================

# =====================================================================
# ZSDIC GLOBAL VARIABLES
# =====================================================================

zsdic_BASE_DIR = ""
zsdic_GAME_BASE = ""
zsdic_GAME_DIRS = {}
zsdic_OUTPUT_DIR_NAME = "skindats"
zsdic_EDITED_DIR_NAME = "edited"
zsdic_SIZE_DIR_NAME = "size"
zsdic_MODSKIN_TXT = ""
zsdic_OUTFITS_TXT = ""
zsdic_NULL_TXT = ""
zsdic_CHANGELOG_TXT = ""
zsdic_NULLED_LOG_TXT = ""
zsdic_SWAP_OFFSETS_TXT = ""
zsdic_OUTFITS_FILES = {"AvatarSuitsTable.uasset", "GoldClothBattleEffect.uasset"}
zsdic_ID_ASCII_RE = _ptre.compile(rb"(?<![0-9])[0-9]{3,}(?![0-9])")
zsdic_ID_UTF16LE_RE = _ptre.compile(rb"(?:(?:[0-9]\x00){3,})")


# =====================================================================
# ZSDIC HELPERS
# =====================================================================

def zsdic_build_safe_pattern(ascii_bytes: bytes):
    return _ptre.compile(rb"(?<![0-9])" + _ptre.escape(ascii_bytes) + rb"(?![0-9])")


def zsdic_pad_pattern(src: bytes, target_len: int) -> bytes:
    cur = bytearray(src)
    to_insert = target_len - len(cur)
    idx = cur.find(0x00)
    if idx < 0:
        cur.extend(b"\x00" * to_insert)
    else:
        for _ in range(to_insert):
            cur.insert(idx, 0x00)
    return bytes(cur)


def zsdic_truncate_pattern(src: bytes, target_len: int) -> bytes:
    cur = bytearray(src)
    to_remove = len(cur) - target_len
    while to_remove > 0:
        idx = cur.find(0x00)
        if idx < 0:
            break
        del cur[idx]
        to_remove -= 1
    if to_remove > 0:
        del cur[-to_remove:]
    return bytes(cur)


def zsdic_iter_files(root_dir: str):
    for r, _, files in os.walk(root_dir):
        for fn in files:
            abs_path = os.path.join(r, fn)
            if os.path.isfile(abs_path):
                yield abs_path, os.path.relpath(abs_path, root_dir)


def zsdic_parse_id_pairs(path: str):
    pairs = []
    if not os.path.isfile(path):
        return pairs
    with open(path, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith(("#", "//", ";")):
                continue
            parts = [p for p in _ptre.split(r"[,\s]+", line) if p]
            if len(parts) >= 2:
                pairs.append((parts[0].strip(), parts[1].strip()))
    return pairs


def zsdic_op_regex(pat: bytes):
    return _ptre.compile(rb"(?<![0-9])" + _ptre.escape(pat) + rb"(?![0-9])")


def zsdic_load_null_id_set(null_txt_path: str) -> set:
    ids = set()
    if not os.path.isfile(null_txt_path):
        return ids
    with open(null_txt_path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            for m in _ptre.finditer(r"\b(\d{3,})\b", line):
                ids.add(m.group(1))
    return ids


def zsdic_load_swap_offsets(path: str):
    if not os.path.isfile(path):
        return None
    out = {}
    current_file = None
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith("FILE|"):
                current_file = line.split("|", 1)[1]
                out.setdefault(current_file, [])
            elif line.startswith("OFFSETS|") and current_file is not None:
                rest = line.split("|", 1)[1].strip()
                if rest:
                    parts = [p.strip() for p in rest.split(",") if p.strip().isdigit()]
                    out[current_file].extend(int(p) for p in parts)
    for k in list(out.keys()):
        out[k] = sorted(set(out[k]))
    return out


def zsdic_write_swap_offsets(path: str, offsets_map: dict):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("=== SWAP OFFSETS LOG ===\nGenerated by Mod Skin.\n\n")
            for rel in sorted(offsets_map.keys()):
                offs = sorted(set(offsets_map[rel]))
                f.write(f"FILE|{rel}\nOFFSETS|" + ",".join(str(x) for x in offs) + "\n\n")
    except Exception as e:
        zsdic_console.print(f"[{DC_ORANGE}]Failed writing {path}: {e}[/]")


def zsdic_nearest_distance(pos: int, sorted_offsets: list) -> int:
    i = bisect.bisect_left(sorted_offsets, pos)
    best = 10**18
    if i < len(sorted_offsets):
        best = min(best, abs(sorted_offsets[i] - pos))
    if i > 0:
        best = min(best, abs(sorted_offsets[i - 1] - pos))
    return best


# =====================================================================
# NULLING FUNCTIONS
# =====================================================================

def zsdic_find_ascii_id_candidates(orig_bytes: bytes, swap_offsets: list, null_id_set: set, mod_ids: set):
    candidates = []
    if not swap_offsets:
        return candidates
    swap_offsets = sorted(swap_offsets)
    for m in zsdic_ID_ASCII_RE.finditer(orig_bytes):
        start, end = m.start(), m.end()
        if end + 5 > len(orig_bytes):
            continue
        id_str = orig_bytes[start:end].decode("ascii", errors="ignore")
        if not id_str or id_str in mod_ids or id_str.startswith("40") or id_str not in null_id_set:
            continue
        longhex = orig_bytes[start:end + 5]
        dist = zsdic_nearest_distance(start, swap_offsets)
        candidates.append((dist, start, id_str, longhex))
    return candidates


def zsdic_find_utf16le_id_candidates(orig_bytes: bytes, swap_offsets: list, null_id_set: set, mod_ids: set):
    candidates = []
    if not swap_offsets:
        return candidates
    swap_offsets = sorted(swap_offsets)
    for m in zsdic_ID_UTF16LE_RE.finditer(orig_bytes):
        start, end = m.start(), m.end()
        if end + 5 > len(orig_bytes):
            continue
        id_str = orig_bytes[start:end][0::2].decode("ascii", errors="ignore")
        if not id_str or len(id_str) < 3 or id_str in mod_ids or id_str.startswith("40") or id_str not in null_id_set:
            continue
        longhex = orig_bytes[start:end + 5]
        dist = zsdic_nearest_distance(start, swap_offsets)
        candidates.append((dist, start, id_str, longhex))
    return candidates


def zsdic_apply_nulling_nearest(orig_bytes: bytes, swap_offsets: list, null_id_set: set, mod_ids: set, max_nulls: int):
    if not swap_offsets:
        return orig_bytes, []
    candidates = zsdic_find_ascii_id_candidates(orig_bytes, swap_offsets, null_id_set, mod_ids)
    if zsdic_ENABLE_UTF16LE_ID_SCAN:
        candidates += zsdic_find_utf16le_id_candidates(orig_bytes, swap_offsets, null_id_set, mod_ids)
    if not candidates:
        return orig_bytes, []
    candidates.sort(key=lambda x: (x[0], x[1]))
    data = bytearray(orig_bytes)
    nulled = []
    used_spans = []

    def overlaps(a0, a1):
        return any(not (a1 <= b0 or a0 >= b1) for b0, b1 in used_spans)

    for dist, start, id_str, longhex in candidates:
        if len(nulled) >= max_nulls:
            break
        end = start + len(longhex)
        if end > len(data) or overlaps(start, end):
            continue
        before = data[start - 1:start] if start > 0 else None
        after = data[end:end + 1] if end < len(data) else None
        if (before and before in b"0123456789") or (after and after in b"0123456789"):
            continue
        data[start:end] = b"\x00" * (end - start)
        used_spans.append((start, end))
        nulled.append((start, id_str, longhex.hex(), dist))
    return bytes(data), nulled


def zsdic_find_ascii_global_candidates(orig_bytes: bytes, null_id_set: set, mod_ids: set):
    candidates = []
    for m in zsdic_ID_ASCII_RE.finditer(orig_bytes):
        start, end = m.start(), m.end()
        if end + 5 > len(orig_bytes):
            continue
        id_str = orig_bytes[start:end].decode("ascii", errors="ignore")
        if not id_str or id_str in mod_ids or id_str.startswith("40") or id_str not in null_id_set:
            continue
        candidates.append((start, id_str, orig_bytes[start:end + 5]))
    return candidates


def zsdic_find_utf16le_global_candidates(orig_bytes: bytes, null_id_set: set, mod_ids: set):
    candidates = []
    for m in zsdic_ID_UTF16LE_RE.finditer(orig_bytes):
        start, end = m.start(), m.end()
        if end + 5 > len(orig_bytes):
            continue
        id_str = orig_bytes[start:end][0::2].decode("ascii", errors="ignore")
        if not id_str or len(id_str) < 3 or id_str in mod_ids or id_str.startswith("40") or id_str not in null_id_set:
            continue
        candidates.append((start, id_str, orig_bytes[start:end + 5]))
    return candidates


def zsdic_apply_nulling_global(orig_bytes: bytes, null_id_set: set, mod_ids: set, max_nulls: int):
    candidates = zsdic_find_ascii_global_candidates(orig_bytes, null_id_set, mod_ids)
    if zsdic_ENABLE_UTF16LE_ID_SCAN:
        candidates += zsdic_find_utf16le_global_candidates(orig_bytes, null_id_set, mod_ids)
    if not candidates:
        return orig_bytes, []
    candidates.sort(key=lambda x: x[0])
    data = bytearray(orig_bytes)
    nulled = []
    used_spans = []

    def overlaps(a0, a1):
        return any(not (a1 <= b0 or a0 >= b1) for b0, b1 in used_spans)

    for start, id_str, longhex in candidates:
        if len(nulled) >= max_nulls:
            break
        end = start + len(longhex)
        if end > len(data) or overlaps(start, end):
            continue
        before = data[start - 1:start] if start > 0 else None
        after = data[end:end + 1] if end < len(data) else None
        if (before and before in b"0123456789") or (after and after in b"0123456789"):
            continue
        data[start:end] = b"\x00" * (end - start)
        used_spans.append((start, end))
        nulled.append((start, id_str, longhex.hex(), -1))
    return bytes(data), nulled


def zsdic_apply_nulling_even_parts(orig_bytes: bytes, null_id_set: set, mod_ids: set, max_nulls: int, part_size: int = 65536):
    if max_nulls < 1:
        return orig_bytes, []
    if part_size <= 0:
        part_size = 65536
    candidates = zsdic_find_ascii_global_candidates(orig_bytes, null_id_set, mod_ids)
    if zsdic_ENABLE_UTF16LE_ID_SCAN:
        candidates += zsdic_find_utf16le_global_candidates(orig_bytes, null_id_set, mod_ids)
    if not candidates:
        return orig_bytes, []
    candidates.sort(key=lambda x: x[0])

    file_len = len(orig_bytes)
    num_full = file_len // part_size
    remainder = file_len % part_size
    num_parts = num_full + (1 if remainder else 0)
    if num_parts <= 0:
        num_parts = 1

    buckets = [[] for _ in range(num_parts)]
    for start, id_str, longhex in candidates:
        part_idx = start // part_size
        if part_idx >= num_parts:
            part_idx = num_parts - 1
        buckets[part_idx].append((start, id_str, longhex))

    data = bytearray(orig_bytes)
    nulled = []
    used_spans = []

    def overlaps(a0, a1):
        return any(not (a1 <= b0 or a0 >= b1) for b0, b1 in used_spans)

    ptrs = [0] * num_parts
    progress_made = True
    while len(nulled) < max_nulls and progress_made:
        progress_made = False
        for part_idx in range(num_parts):
            if len(nulled) >= max_nulls:
                break
            bucket = buckets[part_idx]
            if not bucket:
                continue
            while ptrs[part_idx] < len(bucket) and len(nulled) < max_nulls:
                start, id_str, longhex = bucket[ptrs[part_idx]]
                ptrs[part_idx] += 1
                end = start + len(longhex)
                if end > len(data) or overlaps(start, end):
                    continue
                before = data[start - 1:start] if start > 0 else None
                after = data[end:end + 1] if end < len(data) else None
                if (before and before in b"0123456789") or (after and after in b"0123456789"):
                    continue
                data[start:end] = b"\x00" * (end - start)
                used_spans.append((start, end))
                nulled.append((start, id_str, longhex.hex(), -2))
                progress_made = True
                break
    return bytes(data), nulled


# =====================================================================
# PAIR OPERATIONS
# =====================================================================

def zsdic_get_pair_ops(pairs, cache):
    pair_ops = {}
    for id1, id2 in pairs:
        a1, a2 = id1.encode(), id2.encode()
        p1, p2 = zsdic_build_safe_pattern(a1), zsdic_build_safe_pattern(a2)
        pos1 = pos2 = None
        d1 = d2 = b""
        for data in cache.values():
            if pos1 is None and (m := p1.search(data)):
                pos1, d1 = m.start(), data
            if pos2 is None and (m := p2.search(data)):
                pos2, d2 = m.start(), data
            if pos1 is not None and pos2 is not None:
                break
        if pos1 is None or pos2 is None:
            continue
        lh1 = a1 + d1[pos1 + len(a1): pos1 + len(a1) + 5]
        lh2 = a2 + d2[pos2 + len(a2): pos2 + len(a2) + 5]
        digit_len_diff = abs(len(a1) - len(a2))
        ops = []

        if digit_len_diff <= 1:
            if len(lh1) == len(lh2):
                mode = "TWO-WAY"
                ops.append({"from": lh1, "to": lh2, "rx": zsdic_op_regex(lh1)})
                ops.append({"from": lh2, "to": lh1, "rx": zsdic_op_regex(lh2)})
            elif len(lh1) > len(lh2):
                mode = "TWO-WAY(ADJUSTED)"
                ops.append({"from": lh1, "to": zsdic_pad_pattern(lh2, len(lh1)), "rx": zsdic_op_regex(lh1)})
                ops.append({"from": lh2, "to": zsdic_truncate_pattern(lh1, len(lh2)), "rx": zsdic_op_regex(lh2)})
            else:
                mode = "TWO-WAY(ADJUSTED)"
                ops.append({"from": lh2, "to": zsdic_pad_pattern(lh1, len(lh2)), "rx": zsdic_op_regex(lh2)})
                ops.append({"from": lh1, "to": zsdic_truncate_pattern(lh2, len(lh1)), "rx": zsdic_op_regex(lh1)})
        else:
            shorter_lh, longer_lh = (lh1, lh2) if len(a1) < len(a2) else (lh2, lh1)
            src, dst = longer_lh, shorter_lh
            if len(dst) < len(src):
                dst = zsdic_pad_pattern(dst, len(src))
            elif len(dst) > len(src):
                dst = zsdic_truncate_pattern(dst, len(src))
            mode = "ONE-WAY(PADDED)"
            ops.append({"from": src, "to": dst, "rx": zsdic_op_regex(src)})

        pair_ops[(id1, id2)] = {"mode": mode, "ops": ops, "lhs": lh1, "rhs": lh2}
    return pair_ops


# =====================================================================
# ZSDIC MAIN FLOW
# =====================================================================

def zsdic_mod_skin_flow(game: str):
    mini_display_tool_name()

    zsdic_console.print(
        Panel(
            f"[bold {DC_HIGHLIGHT}]ZSDIC PRO SKIN ENGINE[/bold {DC_HIGHLIGHT}]\n\n"
            f"[bold {DC_TEXT}]M O D   S K I N   &   A U T O   S I Z E   F I X E R[/bold {DC_TEXT}]\n"
            f"[dim {DC_DIM}]----------------------------------------------[/dim {DC_DIM}]\n"
            f"[bold {DC_TEXT}]Target Game Profile : [bold {DC_HIGHLIGHT}]{game.upper()}[/bold {DC_HIGHLIGHT}][/bold {DC_TEXT}]",
            expand=True,
            border_style=DC_BORDER,
            box=HEAVY_EDGE,
            padding=(1, 2),
            title="[bold black on {DC_HIGHLIGHT}] SYSTEM INITIALIZED [/]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT),
            title_align="center"
        )
    )

    game_base_dir = zsdic_GAME_DIRS.get(game, "")
    if not game_base_dir:
        zsdic_console.print(Panel(
            f"[{DC_RED}]Game directory not set: {game}[/]",
            border_style=DC_RED,
            expand=True
        ))
        return

    modskin_path = zsdic_MODSKIN_TXT
    outfits_path = zsdic_OUTFITS_TXT
    output_dir = os.path.join(game_base_dir, zsdic_OUTPUT_DIR_NAME)
    edited_dir = os.path.join(game_base_dir, zsdic_EDITED_DIR_NAME)
    size_dir = os.path.join(game_base_dir, zsdic_SIZE_DIR_NAME)
    swap_offsets_path = zsdic_SWAP_OFFSETS_TXT

    pairs_modskin = zsdic_parse_id_pairs(modskin_path) if os.path.isfile(modskin_path) else []
    pairs_outfits = zsdic_parse_id_pairs(outfits_path) if os.path.isfile(outfits_path) else []

    if not pairs_modskin and not pairs_outfits:
        zsdic_console.print(Panel(
            f"[bold {DC_ORANGE}]No valid ID pairs configuration found![/]",
            border_style=DC_ORANGE,
            box=ROUNDED,
            expand=True
        ))
        time.sleep(1)
        return

    all_files = list(zsdic_iter_files(output_dir))
    if not all_files:
        zsdic_console.print(Panel(
            f"[bold {DC_RED}]No asset files detected in directory:\n{output_dir}[/]",
            border_style=DC_RED,
            expand=True
        ))
        return

    cache, rel_map = {}, {}
    for abs_path, rel_path in all_files:
        try:
            cache[abs_path] = open(abs_path, "rb").read()
            rel_map[abs_path] = rel_path
        except Exception:
            pass

    pair_ops_modskin = zsdic_get_pair_ops(pairs_modskin, cache) if pairs_modskin else {}
    pair_ops_outfits = zsdic_get_pair_ops(pairs_outfits, cache) if pairs_outfits else {}

    all_rxs = []
    for pinfo in pair_ops_modskin.values():
        all_rxs.extend(op["rx"] for op in pinfo["ops"])
    for pinfo in pair_ops_outfits.values():
        all_rxs.extend(op["rx"] for op in pinfo["ops"])

    valid_files = [p for p, data in cache.items() if any(rx.search(data) for rx in all_rxs)]
    if not valid_files:
        zsdic_console.print(Panel(
            "[bold {DC_RED}]Zero matching pattern signatures found in cached assets. Process halted.[/]".replace("{DC_RED}", DC_RED),
            border_style=DC_RED,
            expand=True
        ))
        return

    if os.path.isdir(edited_dir):
        shutil.rmtree(edited_dir)
    os.makedirs(edited_dir, exist_ok=True)

    file_changes = {}
    swap_offsets_map = {}
    null_id_set = zsdic_load_null_id_set(zsdic_NULL_TXT)
    mod_ids = set()

    total_pairs = len(pairs_modskin) + len(pairs_outfits)
    auto_max_nulls = total_pairs * 3 if total_pairs < 500 else total_pairs * 2

    for a, b in pairs_modskin + pairs_outfits:
        if a.isdigit():
            mod_ids.add(a)
        if b.isdigit():
            mod_ids.add(b)

    def get_progress_table(file_logs):
        table = Table(
            title=f"[bold black on {DC_HIGHLIGHT}] REPSHMET & SIZE-FIX LIVE ENGINE [/]",
            border_style=DC_BORDER,
            box=HEAVY_EDGE,
            expand=True,
            show_lines=True
        )
        table.add_column("TARGET ASSET FILE", style=f"bold {DC_HIGHLIGHT}", header_style=f"bold black on {DC_HIGHLIGHT}", ratio=2)
        table.add_column("PIPELINE STATUS", style="bold", header_style=f"bold black on {DC_HIGHLIGHT}", ratio=1, justify="center")
        for fname, status in file_logs:
            table.add_row(fname, status)
        return table

    file_logs = []
    success_count = 0

    with Live(get_progress_table(file_logs), refresh_per_second=15, console=zsdic_console) as live:
        for src in sorted(valid_files):
            rel = rel_map.get(src, os.path.basename(src))
            short_name = rel if len(rel) < 35 else "..." + rel[-32:]

            file_logs.append([f"[bold {DC_TEXT}]{short_name}[/]", "[blink bold {DC_ORANGE}]PATCHING...[/]".replace("{DC_ORANGE}", DC_ORANGE)])
            if len(file_logs) > 8:
                file_logs.pop(0)
            live.update(get_progress_table(file_logs))

            edited_path = os.path.join(edited_dir, rel)
            os.makedirs(os.path.dirname(edited_path), exist_ok=True)

            try:
                shutil.copy2(src, edited_path)
                orig = open(edited_path, "rb").read()
            except Exception:
                file_logs[-1][1] = "[bold {DC_RED}]COPY ERROR[/]".replace("{DC_RED}", DC_RED)
                live.update(get_progress_table(file_logs))
                continue

            new = bytearray(orig)
            changed = False
            active_pair_ops = pair_ops_outfits if os.path.basename(rel) in zsdic_OUTFITS_FILES else pair_ops_modskin

            for pair, pinfo in active_pair_ops.items():
                for op in pinfo["ops"]:
                    matches = list(op["rx"].finditer(orig))
                    if not matches:
                        continue
                    frm, to = op["from"], op["to"]
                    for m in matches:
                        start = m.start()
                        new[start: start + len(frm)] = to
                        swap_offsets_map.setdefault(rel, set()).add(start)
                        changed = True

            if changed:
                offsets = list(swap_offsets_map.get(rel, set()))
                if offsets:
                    new_bytes, _ = zsdic_apply_nulling_nearest(bytes(new), offsets, null_id_set, mod_ids, auto_max_nulls)
                else:
                    new_bytes, _ = zsdic_apply_nulling_global(bytes(new), null_id_set, mod_ids, auto_max_nulls)
                new = bytearray(new_bytes)

            if changed and new != orig:
                try:
                    with open(edited_path, "wb") as f:
                        f.write(new)
                    size_path = os.path.join(size_dir, rel)
                    os.makedirs(os.path.dirname(size_path), exist_ok=True)
                    with open(size_path, "wb") as f:
                        f.write(new)
                except Exception:
                    pass

                file_changes.setdefault(rel, active_pair_ops)
                success_count += 1

            file_logs[-1][1] = "[bold {DC_HIGHLIGHT}]SUCCESS[/]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT)
            live.update(get_progress_table(file_logs))

    zsdic_console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]REPSHMET & SIZE-FIX PIPELINE EXECUTED SUCCESSFULLY![/]\n\n"
        f"  [dim {DC_DIM}]* Total Asset Files Evaluated :[/dim {DC_DIM}] [bold {DC_HIGHLIGHT}]{len(valid_files)}[/]\n"
        f"  [dim {DC_DIM}]* Successfully Patched & Fixed :[/dim {DC_DIM}] [bold {DC_HIGHLIGHT}]{success_count}[/]\n"
        f"  [dim {DC_DIM}]* Dynamic Null Allocation    :[/dim {DC_DIM}] [bold {DC_ORANGE}]{auto_max_nulls} nulls/file[/]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
        expand=True,
        title=f"[bold black on {DC_HIGHLIGHT}] SESSION EXECUTION SUMMARY [/]",
        padding=(1, 2)
    ))

    if not file_changes:
        return

    try:
        with open(zsdic_CHANGELOG_TXT, "w", encoding="utf-8") as f:
            f.write("ZSDIC MOD SKIN CHANGELOG\n==============================\n\n")
            for rel_file, pairs_info in file_changes.items():
                f.write(f"FILE: {rel_file}\n")
                for pair, pinfo in pairs_info.items():
                    f.write(f"  PAIR: {pair[0]} -> {pair[1]} ({pinfo['mode']})\n")
                    for op in pinfo["ops"]:
                        frm_hex = op["from"].hex().upper()
                        to_hex = op["to"].hex().upper()
                        f.write(f"     - Replaced successfully\n       FROM: {frm_hex}\n       TO  : {to_hex}\n")
                f.write("==============================\n\n")
    except Exception as e:
        zsdic_console.print(f"[red]Changelog Error: {e}[/red]")

    zsdic_write_swap_offsets(swap_offsets_path, swap_offsets_map)

    zsdic_console.print(
        Panel(
            f"[bold {DC_HIGHLIGHT}]All Operations Finished! Output files secured successfully.[/]",
            expand=True,
            border_style=DC_BORDER,
            box=HEAVY_EDGE
        )
    )


# =====================================================================
# ZSDIC REPACK SIZE FIX
# =====================================================================

def zsdic_repack_size_fix():
    mini_display_tool_name()
    zsdic_console.print(Panel(f"[bold {DC_HIGHLIGHT}]Size-Fix Initialized[/]", expand=False, border_style=DC_BORDER))

    edited_dir = os.path.join(zsdic_GAME_DIRS.get("BGMI", ""), zsdic_EDITED_DIR_NAME)
    size_dir = os.path.join(zsdic_GAME_DIRS.get("BGMI", ""), zsdic_SIZE_DIR_NAME)
    swap_offsets_path = zsdic_SWAP_OFFSETS_TXT

    if not os.path.isdir(edited_dir):
        zsdic_console.print(f"[red]Edited directory not found: {edited_dir}[/red]")
        return

    swap_offsets = zsdic_load_swap_offsets(swap_offsets_path)
    if not swap_offsets:
        zsdic_console.print(f"[{DC_ORANGE}]swap_offsets.txt missing/empty. Using GLOBAL nulling.[/]")
        swap_offsets = {}

    max_nulls_str = Prompt.ask(f"[bold {DC_HIGHLIGHT}]Max nulls per file[/]", default=str(zsdic_DEFAULT_MAX_NULLS))
    try:
        max_nulls = int(max_nulls_str)
        if max_nulls < 1:
            max_nulls = zsdic_DEFAULT_MAX_NULLS
    except Exception:
        max_nulls = zsdic_DEFAULT_MAX_NULLS

    zsdic_console.print("\n[bold {DC_HIGHLIGHT}]Size Fix Mode:[/]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT))
    zsdic_console.print("  [bold {DC_HIGHLIGHT}]1)[/] Null Near To Modification  [dim](Nearest/Global)[/dim]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT))
    zsdic_console.print("  [bold {DC_HIGHLIGHT}]2)[/] Null Evenly  [dim](64KB parts distribution)[/dim]".replace("{DC_HIGHLIGHT}", DC_HIGHLIGHT))
    size_fix_mode = Prompt.ask(f"[bold {DC_HIGHLIGHT}]Select mode[/]", choices=["1", "2"], default="1")

    null_id_set = zsdic_load_null_id_set(zsdic_NULL_TXT)
    mod_ids = set()
    for path in [zsdic_MODSKIN_TXT, zsdic_OUTFITS_TXT]:
        if os.path.isfile(path):
            for a, b in zsdic_parse_id_pairs(path):
                if a.isdigit():
                    mod_ids.add(a)
                if b.isdigit():
                    mod_ids.add(b)

    if os.path.isdir(size_dir):
        shutil.rmtree(size_dir)
    os.makedirs(size_dir, exist_ok=True)
    files_to_process = list(zsdic_iter_files(edited_dir))
    if not files_to_process:
        return

    nulled_info = {}
    progress = Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))

    with Live(progress, refresh_per_second=10) as live:
        task = progress.add_task(f"[cyan]Nulling... ", total=len(files_to_process))
        for abs_path, rel_path in files_to_process:
            progress.update(task, advance=1, description=f"[cyan]Processing {rel_path}[/]")
            try:
                orig_bytes = open(abs_path, "rb").read()
            except Exception:
                continue

            offsets = swap_offsets.get(rel_path, []) if swap_offsets else []
            if size_fix_mode == "1":
                if offsets:
                    mode_used = "NEAREST"
                    new_bytes, entries = zsdic_apply_nulling_nearest(orig_bytes, offsets, null_id_set, mod_ids, max_nulls)
                else:
                    mode_used = "GLOBAL"
                    new_bytes, entries = zsdic_apply_nulling_global(orig_bytes, null_id_set, mod_ids, max_nulls)
            else:
                mode_used = "EVEN_PARTS"
                new_bytes, entries = zsdic_apply_nulling_even_parts(orig_bytes, null_id_set, mod_ids, max_nulls, 65536)

            out_path = os.path.join(size_dir, rel_path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(new_bytes)
            nulled_info[rel_path] = {"mode": mode_used, "entries": entries}

    try:
        with open(os.path.join(size_dir, zsdic_NULLED_LOG_TXT), "w", encoding="utf-8") as nf:
            nf.write("=== NULLED LOG ===\n")
            for rel_path in sorted(nulled_info.keys()):
                info = nulled_info[rel_path]
                entries = info.get("entries", [])
                nf.write(f"{rel_path}:\n  Mode: {info.get('mode', 'UNKNOWN')}\n")
                if not entries:
                    nf.write("  (no nulls)\n\n")
                    continue
                for pos, id_str, longhex_hex, dist in entries:
                    dist_str = "[global]" if dist == -1 else ("[even]" if dist == -2 else f"[dist {dist}]")
                    nf.write(f"  [pos {pos}] {dist_str} ID {id_str} -> nulled {longhex_hex}\n")
                nf.write("\n")
    except Exception:
        pass

    zsdic_console.print(Panel(f"[bold {DC_HIGHLIGHT}]Size-fix complete![/]", expand=False, border_style=DC_BORDER, box=ROUNDED))


# =====================================================================
# ZSDIC MENU
# =====================================================================

def zsdic_main_menu():
    while True:
        mini_display_tool_name()

        b_color = DC_HIGHLIGHT
        menu_table = Table(show_header=True, header_style=f"bold black on {DC_HIGHLIGHT}",
                           box=DOUBLE_EDGE, title="[reverse]  ZSDIC MENU  [/]",
                           border_style=DC_BORDER, expand=True)
        menu_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_TEXT}")
        menu_table.add_column("DESCRIPTION", style=f"dim {DC_DIM}")

        menu_table.add_row("1", "MOD SKIN", "Advanced Mod Skin")
        menu_table.add_row("0", f"[{DC_RED}]BACK[/]", "Return to Menu")

        console.print(Panel(menu_table, border_style=DC_BORDER, box=HEAVY_EDGE))

        choice = safe_input(f"[bold {DC_HIGHLIGHT}]ENTER CHOICE (0-1) > [/bold {DC_HIGHLIGHT}]").strip()

        if choice == "1":
            global game_key
            zsdic_mod_skin_flow(game_key)
            safe_input(f"\n[bold {DC_TEXT}]Press Enter to return...[/]")
        elif choice == "0":
            break
        else:
            console.print(f"[red]Invalid! Enter 0 or 1[/red]")
            time.sleep(1)


def zsdic_skin_tool_main(data_path):
    """ZSDIC Skin Tool entry point - sets up paths and calls zsdic_main_menu."""
    global zsdic_BASE_DIR, zsdic_GAME_BASE, zsdic_GAME_DIRS
    global zsdic_MODSKIN_TXT, zsdic_OUTFITS_TXT, zsdic_NULL_TXT
    global zsdic_CHANGELOG_TXT, zsdic_NULLED_LOG_TXT, zsdic_SWAP_OFFSETS_TXT
    global game_key

    while True:
        mini_clear_screen()
        print_banner()

        select_table = Table(
            show_header=True,
            header_style=f"bold black on {DC_HIGHLIGHT}",
            box=DOUBLE_EDGE,
            title="[reverse]  SELECT GAME (ZSDIC)  [/]",
            border_style=DC_BORDER,
            expand=True
        )
        select_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
        select_table.add_column("GAME", style=f"bold {DC_TEXT}")
        select_table.add_column("DESCRIPTION", style=f"dim {DC_DIM}")
        select_table.add_row("1", "BGMI", "Mod BGMI Skins")
        select_table.add_row("2", "PUBG", "Mod PUBG Skins")
        select_table.add_row("0", f"[{DC_RED}]BACK[/]", "Return")
        console.print(Panel(select_table, border_style=DC_BORDER, box=HEAVY_EDGE))

        game_choice = safe_input(f"[bold {DC_HIGHLIGHT}]SELECT (1/2/0) > [/bold {DC_HIGHLIGHT}]").strip()

        if game_choice == "0":
            return
        if game_choice not in ("1", "2"):
            console.print(f"[bold {DC_RED}]Invalid![/]")
            time.sleep(1)
            continue

        selected_game = "BGMI_SKIN" if game_choice == "1" else "PUBG_SKIN"
        game_key = "BGMI" if game_choice == "1" else "PUBG"
        GAME_BASE = data_path / "SKIN_TOOL" / selected_game

        zsdic_BASE_DIR = str(GAME_BASE / "ZSDIC")
        zsdic_GAME_BASE = str(Path(zsdic_BASE_DIR) / game_key)
        zsdic_GAME_DIRS = {game_key: zsdic_GAME_BASE}
        zsdic_MODSKIN_TXT = str(Path(zsdic_BASE_DIR) / "modskin.txt")
        zsdic_OUTFITS_TXT = str(Path(zsdic_BASE_DIR) / "outfits.txt")
        zsdic_NULL_TXT = str(Path(zsdic_BASE_DIR) / "null.txt")
        zsdic_CHANGELOG_TXT = str(Path(zsdic_BASE_DIR) / "changelog.txt")
        zsdic_NULLED_LOG_TXT = str(Path(zsdic_BASE_DIR) / "nulled.txt")
        zsdic_SWAP_OFFSETS_TXT = str(Path(zsdic_BASE_DIR) / "swap_offsets.txt")

        for d in [
            zsdic_BASE_DIR,
            zsdic_GAME_BASE,
            os.path.join(zsdic_GAME_BASE, zsdic_OUTPUT_DIR_NAME),
            os.path.join(zsdic_GAME_BASE, zsdic_EDITED_DIR_NAME),
            os.path.join(zsdic_GAME_BASE, zsdic_SIZE_DIR_NAME),
        ]:
            Path(d).mkdir(parents=True, exist_ok=True)

        zsdic_main_menu()
        return


# =====================================================================
# END OF PART 6
# =====================================================================# =====================================================================
# PART 7 - LUA TOOL (Complete)
# =====================================================================

# =====================================================================
# LUA GLOBAL VARIABLES
# =====================================================================

LUAC_CMD = "luac5.3"
LUA_XOR_KEY = b''
SERVER_LUA_XOR_KEY_HEX = "112136474657a78d9d8490d8ab008c35261af7e45805b8b31507d02c1e8ff6c8"

BGMI_STD = {
    0: 13, 1: 14, 2: 15, 3: 16, 4: 17, 5: 18, 14: 27, 16: 29, 17: 0, 18: 1,
    20: 3, 21: 4, 22: 5, 23: 6, 24: 7, 25: 8, 26: 9, 27: 10, 28: 11, 29: 12,
    30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 36: 36, 37: 37, 38: 38, 39: 39,
    40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45,
}
STD_BGMI = {v: k for k, v in BGMI_STD.items()}
STD_FMT = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 1, 0, 3]


# =====================================================================
# LUA PROCESSING CORE
# =====================================================================

def convert_32_to_64_lua53(data):
    """Convert 32-bit standard Lua 5.3 bytecode to 64-bit so 64-bit luadec can read it."""
    import struct

    class R:
        def __init__(self, d):
            self.d, self.p = d, 0
        def rb(self, n):
            v = self.d[self.p:self.p+n]
            self.p += n
            return v
        def rbyte(self):
            v = self.d[self.p]
            self.p += 1
            return v
        def rint(self):
            v = struct.unpack_from('<i', self.d, self.p)[0]
            self.p += 4
            return v
        def rsize(self):
            v = struct.unpack_from('<I', self.d, self.p)[0]
            self.p += 4
            return v
        def rstr(self):
            sz = self.rsize()
            if sz == 0: return None
            return self.rb(sz)
        def rnum(self):
            v = struct.unpack_from('<d', self.d, self.p)[0]
            self.p += 8
            return v
        def rint64(self):
            v = struct.unpack_from('<q', self.d, self.p)[0]
            self.p += 8
            return v

    class W:
        def __init__(self):
            self.b = bytearray()
        def w(self, b):
            self.b.extend(b)
        def wbyte(self, b):
            self.b.append(b)
        def wint(self, i):
            self.b.extend(struct.pack('<i', i))
        def wsize(self, s):
            self.b.extend(struct.pack('<Q', s))
        def wstr(self, s):
            if s is None:
                self.wsize(0)
            else:
                self.wsize(len(s))
                self.w(s)
        def wnum(self, n):
            self.b.extend(struct.pack('<d', n))
        def wint64(self, i):
            self.b.extend(struct.pack('<q', i))

    r, w = R(data), W()
    hdr = bytearray(r.rb(33))
    hdr[13] = 8 # size_t is now 8
    w.w(hdr)
    
    # FIX 1: Copy the nupvalues byte after header
    w.wbyte(r.rbyte()) 

    def proto():
        w.wstr(r.rstr())
        w.wint(r.rint())
        w.wint(r.rint())
        w.wbyte(r.rbyte())
        w.wbyte(r.rbyte())
        w.wbyte(r.rbyte())

        ncode = r.rint()
        w.wint(ncode)
        for _ in range(ncode): w.wint(r.rint())

        nk = r.rint()
        w.wint(nk)
        for _ in range(nk):
            tag = r.rbyte()
            w.wbyte(tag)
            if tag == 1: w.wbyte(r.rbyte())
            elif tag == 3: w.wnum(r.rnum())
            elif tag == 19: w.wint64(r.rint64())
            elif tag in (4, 20): w.wstr(r.rstr())

        nups = r.rint()
        w.wint(nups)
        for _ in range(nups):
            w.wbyte(r.rbyte())
            w.wbyte(r.rbyte())

        np = r.rint()
        w.wint(np)
        for _ in range(np): proto()

        nline = r.rint()
        w.wint(nline)
        for _ in range(nline): w.wint(r.rint())

        nloc = r.rint()
        w.wint(nloc)
        for _ in range(nloc):
            w.wstr(r.rstr())
            w.wint(r.rint())
            w.wint(r.rint())

        nupname = r.rint()
        w.wint(nupname)
        for _ in range(nupname): w.wstr(r.rstr())

    proto()
    
    # FIX 2: Copy the tail byte
    if r.p < len(data):
        w.wbyte(r.rbyte())
        
    return bytes(w.b)




def process_lua_file(data, is_encrypt=False):
    """
    Flexible Lua bytecode converter.
    Handles: Lua 5.1/5.2/5.3/5.4, T24/BGMI custom format.
    """

    class RW:
        def __init__(self):
            self.b = bytearray()

        def byte(self, v):
            self.b.append(int(v) & 0xFF)

        def u32(self, v):
            self.b.extend(struct.pack('<I', int(v) & 0xFFFFFFFF))

        def i32(self, v):
            self.b.extend(struct.pack('<i', int(v)))

        def raw(self, d):
            self.b.extend(d)

    class R:
        def __init__(self, d):
            self.d = bytes(d)
            self.p = 0

        def need(self, n, what='data'):
            if n < 0 or self.p + n > len(self.d):
                raise ValueError(f"truncated: {what} at {self.p}")

        def byte(self):
            self.need(1, 'byte')
            v = self.d[self.p]
            self.p += 1
            return v

        def u32(self):
            self.need(4, 'u32')
            v = struct.unpack_from('<I', self.d, self.p)[0]
            self.p += 4
            return v

        def i32(self):
            self.need(4, 'i32')
            v = struct.unpack_from('<i', self.d, self.p)[0]
            self.p += 4
            return v

        def raw(self, n):
            self.need(n, f'raw({n})')
            v = self.d[self.p:self.p + n]
            self.p += n
            return v

    # Step 1: Header check
    if len(data) < 4:
        raise ValueError('File too small (less than 4 bytes)')

    if data[:4] != b'\x1bLua':
        raise ValueError(
            'Not a Lua bytecode file (missing \\x1bLua magic). '
            f'First 8 bytes: {data[:8].hex()}'
        )

    # Step 2: Detect Lua version
    version_byte = data[4]

    # NEW: Robust detection for standard Lua 5.3
    if version_byte == 0x53 and data[6:10] == b'\x19\x93\r\n':
        return data

    if version_byte == 0x51:
        return data
    if version_byte == 0x52:
        return data
    if version_byte == 0x54:
        return data

    if version_byte != 0x53:
        raise ValueError(f'Unsupported Lua version byte: 0x{version_byte:02x}')

    # Step 3: Lua 5.3 - T24 vs standard
    size_t_byte = data[13]

    if size_t_byte == 8:
        return data

    if size_t_byte != 4:
        return data

    # Step 4: T24 format conversion
    r = R(data)
    w = RW()

    hdr = bytearray(r.raw(33))

    if is_encrypt:
        hdr[13] = 4
    else:
        hdr[13] = 8

    w.raw(hdr)
    w.byte(r.byte())

    key = bytes(LUA_XOR_KEY or b'')

    def read_t24_string():
        sz = r.byte()
        if sz == 0xFF:
            sz = r.u32()
        if sz == 0:
            return None
        if sz < 1:
            raise ValueError(f'invalid T24 string size {sz}')
        payload_len = sz - 1
        enc = r.raw(payload_len)
        if key:
            enc = bytes(enc[i] ^ key[i % len(key)] for i in range(len(enc)))
        return enc

    def read_standard_string():
        sz = r.byte()
        if sz == 0xFF:
            r.need(8, 'size_t')
            sz = struct.unpack_from('<Q', r.d, r.p)[0]
            r.p += 8
        if sz == 0:
            return None
        if sz < 1:
            raise ValueError(f'invalid std string size {sz}')
        return r.raw(sz - 1)

    def write_t24_string(s):
        if s is None:
            w.byte(0)
            return
        e = bytes(s)
        if key:
            e = bytes(e[i] ^ key[i % len(key)] for i in range(len(e)))
        sz = len(e) + 1
        if sz < 0xFF:
            w.byte(sz)
        else:
            w.byte(0xFF)
            w.u32(sz)
        w.raw(e)

    def write_standard_string(s):
        if s is None:
            w.byte(0)
            return
        e = bytes(s) + b'\x00'  # Null terminator add kiya
        sz = len(e)
        if sz < 0xFF:
            w.byte(sz)
        else:
            w.byte(0xFF)
            w.raw(struct.pack('<Q', sz))
        w.raw(e)

    def read_string():
        return read_standard_string() if is_encrypt else read_t24_string()

    def write_string(s):
        if is_encrypt:
            write_t24_string(s)
        else:
            write_standard_string(s)

    def translate_instruction(raw):
        op = raw & 0x3F
        A = (raw >> 6) & 0xFF
        C = (raw >> 14) & 0x1FF
        B = (raw >> 23) & 0x1FF
        Bx = (raw >> 14) & 0x3FFFF
        Ax = (raw >> 6) & 0x3FFFFFF

        if is_encrypt:
            dop = STD_BGMI.get(op, op)
        else:
            dop = BGMI_STD.get(op, op)

        if dop < 0 or dop >= 64:
            dop = op

        fmt = STD_FMT[dop] if dop < len(STD_FMT) else 0
        if fmt == 0:
            return (dop & 0x3F) | (A << 6) | (C << 14) | (B << 23)
        if fmt == 1:
            return (dop & 0x3F) | (A << 6) | (Bx << 14)
        if fmt == 2:
            return (dop & 0x3F) | (A << 6) | (Bx << 14)
        if fmt == 3:
            return (dop & 0x3F) | (Ax << 6)
        return (dop & 0x3F) | (A << 6) | (Bx << 14)

    MAX_COUNT = 2_000_000

    def convert_proto(depth=0):
        if depth > 50:
            raise ValueError('Nested prototype too deep')

        source = read_string()
        write_string(source)
        w.i32(r.i32())
        ldef = r.i32()
        w.i32(ldef)

        w.byte(r.byte())
        w.byte(r.byte())
        w.byte(r.byte())

        ncode = r.u32()
        if ncode > MAX_COUNT:
            raise ValueError(f'invalid code count {ncode}')
        w.u32(ncode)
        for _ in range(ncode):
            w.u32(translate_instruction(r.u32()))

        nk = r.u32()
        if nk > MAX_COUNT:
            raise ValueError(f'invalid constant count {nk}')
        w.u32(nk)
        for _ in range(nk):
            tag = r.byte()
            w.byte(tag)
            if tag == 0:
                continue
            if tag == 1:
                w.byte(r.byte())
            elif tag in (3, 19):
                w.raw(r.raw(8))
            elif tag in (4, 20):
                write_string(read_string())
            else:
                raise ValueError(f'unsupported constant tag {tag}')

        nups = r.u32()
        if nups > MAX_COUNT:
            raise ValueError(f'invalid upvalue count {nups}')
        w.u32(nups)
        for _ in range(nups):
            w.byte(r.byte())
            w.byte(r.byte())

        npt = r.u32()
        if npt > MAX_COUNT:
            raise ValueError(f'invalid prototype count {npt}')
        w.u32(npt)
        for _ in range(npt):
            convert_proto(depth + 1)

        nln = r.u32()
        if nln > MAX_COUNT:
            raise ValueError(f'invalid line-info count {nln}')

        if is_encrypt:
            lines = [r.i32() for _ in range(nln)]
            w.u32(nln)
            prev = ldef
            for ln in lines:
                w.byte((ln - prev) & 0xFF)
                prev = ln
            w.u32(0)
        else:
            cur = ldef
            lines = []
            for _ in range(nln):
                d = r.byte()
                cur += d if d <= 127 else d - 256
                lines.append(cur)
            nab = r.u32()
            if nab > MAX_COUNT:
                raise ValueError(f'invalid absolute-line count {nab}')
            for _ in range(nab):
                pc = r.u32()
                ln = r.i32()
                if pc < nln:
                    lines[pc] = ln
            w.u32(nln)
            for ln in lines:
                w.i32(ln)

        nloc = r.u32()
        if nloc > MAX_COUNT:
            raise ValueError(f'invalid local count {nloc}')
        w.u32(nloc)
        for _ in range(nloc):
            write_string(read_string())
            w.i32(r.i32())
            w.i32(r.i32())

        nupn = r.u32()
        if nupn > MAX_COUNT:
            raise ValueError(f'invalid upvalue-name count {nupn}')
        w.u32(nupn)
        for _ in range(nupn):
            write_string(read_string())

    convert_proto()
    return bytes(w.b)


# =====================================================================
# JAR DOWNLOAD HELPERS
# =====================================================================

def _download_jar(url, dest):
    import requests
    
    # Placeholder for user's GitHub URL
    YOUR_GITHUB_BASE = "https://raw.githubusercontent.com/pikunp909-dot/Kunalyto-Dependencies/main" 
    
    urls_to_try = [url]
    if 'unluac' in dest.name.lower():
        urls_to_try = [
            f"{YOUR_GITHUB_BASE}/unluac.jar", 
            "https://sourceforge.net/projects/unluac/files/latest/download",
            "https://github.com/HansWessels/unluac/raw/master/bin/unluac.jar",
            "https://github.com/HansWessels/unluac/raw/master/unluac.jar",
        ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    last_error = None
    for try_url in urls_to_try:
        if not try_url or "YOUR_GITHUB" in try_url:
            continue 
            
        try:
            console.print(f"[{DC_DIM}]Trying: {try_url[:70]}...[/]")
            r = requests.get(try_url, headers=headers, timeout=90, allow_redirects=True, stream=True)
            r.raise_for_status()

            # FIX: Use to_long_path for Android compatibility
            with open(to_long_path(dest), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            # FIX: Validate JAR magic bytes (PK)
            with open(to_long_path(dest), 'rb') as f:
                magic = f.read(2)
                
            if magic == b'PK' and dest.stat().st_size > 10_000:
                console.print(f"[bold {DC_HIGHLIGHT}]Downloaded {dest.name} ({dest.stat().st_size:,} bytes)[/]")
                return True

            dest.unlink(missing_ok=True)
            last_error = f"Not a JAR (magic={magic!r})"
        except Exception as e:
            last_error = e
            continue

    console.print(f"[bold {DC_RED}]Failed to download {dest.name}: {last_error}[/]")
    return False


def _detect_lua_version(path):
    try:
        with open(path, 'rb') as fh:
            magic = fh.read(5)
        if magic[:4] == b'\x1bLua':
            vb = magic[4]
            return vb, False
        with open(path, 'rb') as fh:
            magic2 = fh.read(3)
        if magic2 == b'\x1bLJ':
            return None, True
    except Exception:
        pass
    return None, False


def _find_local_unluac(script_dir, lua_base):
    candidates = [
        lua_base / "unluac_patched.jar",
        script_dir / "unluac_patched.jar",
        lua_base / "unluac.jar",
        script_dir / "unluac.jar",
        script_dir / "EXES" / "unluac.jar",
        script_dir / "EXES" / "unluac_pro.jar",
    ]
    for p in candidates:
        try:
            if p.is_file() and p.stat().st_size > 1000:
                return p
        except Exception:
            pass

    exes_dir = script_dir / "EXES"
    if exes_dir.is_dir():
        try:
            for jar_file in exes_dir.glob("*.jar"):
                if jar_file.is_file() and jar_file.stat().st_size > 1000:
                    return jar_file
        except Exception:
            pass
    return None


def _ensure_jar_for_file(luac_path, lua_base, script_dir):
    vb, is_luajit = _detect_lua_version(luac_path)
    ljd_path = lua_base / "ljd.jar"
    unluac_path = lua_base / "unluac.jar"

    if is_luajit:
        if not ljd_path.exists():
            _download_jar(
                "https://github.com/nicktindall/luajit-decompiler-v2/releases/latest/download/ljd.jar",
                ljd_path
            )
        return ljd_path if ljd_path.exists() else None
    else:
        local_jar = _find_local_unluac(script_dir, lua_base)
        if local_jar is not None:
            return local_jar
        _download_jar(
            "https://github.com/HansWessels/unluac/releases/latest/download/unluac.jar",
            unluac_path
        )
        return unluac_path if unluac_path.exists() else None


# =====================================================================
# LUA TOOL MAIN
# =====================================================================

def run_lua_tool(data_path):
    import subprocess as _sp
    global LUA_XOR_KEY, SERVER_LUA_XOR_KEY_HEX

    console.clear()
    print_banner()

    b_color = DC_HIGHLIGHT
    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]LUA DECOMPILER & RECOMPILER[/bold {DC_HIGHLIGHT}]\n"
        f"[dim {DC_DIM}]Extract, Edit, and Repack BGMI Lua Bytecode[/dim {DC_DIM}]",
        border_style=DC_BORDER,
        box=DOUBLE_EDGE
    ))

    lua_base = data_path / "LUA_TOOL"
    
    # ========================================================
    # LUAC53 EXECUTABLE CHECK & DOWNLOAD FIX
    # ========================================================
    home_luac = Path(os.path.expanduser("~")) / "luac53"
    YOUR_GITHUB_BASE = "YOUR_GITHUB_URL_HERE"

    if not home_luac.exists():
        console.print(f"[{DC_ORANGE}]luac53 binary not found in ~, attempting download...[/]")
        try:
            import requests
            r = requests.get(f"{YOUR_GITHUB_BASE}/luac53", headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
            if r.status_code == 200:
                with open(to_long_path(home_luac), 'wb') as f:
                    f.write(r.content)
                # FIX: Correct chmod syntax
                os.chmod(str(home_luac), 0o755) 
                console.print(f"[bold {DC_GREEN}]luac53 installed successfully in Termux home![/]")
        except Exception as e:
            console.print(f"[{DC_RED}]Failed to download luac53: {e}[/]")

    # Set dynamic command
    global LUAC_CMD
    # Priority: 1. luadec built-in 5.3 compiler, 2. home luac53, 3. system luac5.3
    luadec_luac = Path(os.path.expanduser("~")) / "luadec" / "lua-5.3" / "src" / "luac"
    if luadec_luac.exists():
        LUAC_CMD = str(luadec_luac)
        console.print(f"[{DC_DIM}]Using Lua 5.3 from luadec: {LUAC_CMD}[/]")
    elif home_luac.exists():
        LUAC_CMD = str(home_luac)
    else:
        LUAC_CMD = "luac5.3"

    # Fallback system check
    if LUAC_CMD == "luac5.3" and subprocess.call("command -v luac5.3", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        console.print(f"[{DC_ORANGE}]Installing Lua 5.3 Compiler via pkg...[/]")
        subprocess.call("pkg install lua53 -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # ========================================================

    lua_org = lua_base / "Lua_org"
    lua_dec = lua_base / "Lua_Decript"
    lua_res = lua_base / "Lua_Rueslt"

    re_lua_any_size = lua_base / "RE_LUA ANY SIZE"
    lua_edit = re_lua_any_size / "EDIT_LUA"
    lua_org_pak = re_lua_any_size / "ORGNAL_PAK"
    lua_mod_repack = re_lua_any_size / "REPACK_MOD"

    lua_custom = lua_base / "LUA_CUSTOM"
    lua_custom_edit = lua_custom / "EDIT"
    lua_custom_pak = lua_custom / "PAK"
    lua_custom_result = lua_custom / "RESULT"

    for d in [lua_org, lua_dec, lua_res, lua_edit, lua_org_pak, lua_mod_repack,
              lua_custom, lua_custom_edit, lua_custom_pak, lua_custom_result]:
        os.makedirs(to_long_path(d), exist_ok=True)

    # Jar download
    script_dir = Path(__file__).resolve().parent
    unluac_path = lua_base / "unluac.jar"

    if _find_local_unluac(script_dir, lua_base) is None:
        _download_jar(
            "https://github.com/unluac/unluac/releases/download/2023-04-24/unluac.jar",
            unluac_path
        )

    # Lua compiler check
    import subprocess
    if subprocess.call("command -v luac5.3", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        console.print(f"[{DC_ORANGE}]Installing Lua 5.3 Compiler via pkg...[/]")
        subprocess.call("pkg install lua53 -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Lua XOR key
    lua_key_file = lua_base / "lua_xor_key.txt"
    if SERVER_LUA_XOR_KEY_HEX:
        try:
            LUA_XOR_KEY = bytes.fromhex(SERVER_LUA_XOR_KEY_HEX.strip())
        except ValueError:
            LUA_XOR_KEY = b""
    elif lua_key_file.exists():
        try:
            local_key_hex = lua_key_file.read_text(encoding="utf-8").strip()
            LUA_XOR_KEY = bytes.fromhex(local_key_hex)
        except (OSError, ValueError):
            LUA_XOR_KEY = b""

    while True:
        console.clear()
        print_banner()

        menu_table = Table(
            show_header=True,
            header_style=f"bold black on {DC_HIGHLIGHT}",
            box=HEAVY_EDGE,
            title="[reverse]  LUA MODDING TOOL  [/]",
            border_style=DC_HIGHLIGHT,
            expand=True
        )
        menu_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_TEXT}")
        menu_table.add_column("DESCRIPTION", style=f"dim {DC_DIM}")

        menu_table.add_row("1", "LUA DECOMPILE", "Org -> Decript (.lua)")
        menu_table.add_row("2", "LUA RECOMPILE", "Edited -> Result (.lua)")
        menu_table.add_row("3", "LUA REPACK ANY SIZE", "Inject edited Lua into PAK")
        menu_table.add_row("4", "CSV SMART INJECTOR", "Auto path from CSV")
        menu_table.add_row("5", "LUA COMPILE (PLAIN)", ".lua -> .luac (plain)")
        menu_table.add_row("0", f"[{DC_RED}]BACK[/]", "Return to Main Menu")

        console.print(Panel(menu_table, border_style=DC_HIGHLIGHT, box=HEAVY_EDGE, title=f"[bold black on {DC_HIGHLIGHT}] LUA ENGINE [/]"))

        choice = safe_input(f"[bold {DC_HIGHLIGHT}]SELECT OPTION > [/bold {DC_HIGHLIGHT}]").strip()


        if choice not in ["1", "2", "3", "4", "5", "0"]:
            continue

        # ── Option 1: Decompile ──
        if choice == "1":
            console.clear()
            print_banner()
            console.print(Panel(f"[bold {DC_HIGHLIGHT}]Scanning 'Lua_org' directory...[/]",
                                border_style=DC_BORDER, box=ROUNDED))
            files = [f for f in lua_org.iterdir() if f.is_file() and f.suffix in ['.lua', '.luac']]
            if not files:
                console.print(Panel(f"[{DC_RED}]No files in {lua_org.resolve()}[/]", border_style=DC_RED))
            else:
                # ... (Simplified display)
                console.print(Panel(f"[bold {DC_TEXT}]Found {len(files)} files to decompile.[/]", border_style=DC_BORDER, box=HEAVY_EDGE))
                sel = safe_input(f"\n[bold {DC_HIGHLIGHT}]Type 'all' or '0' to Back: [/bold {DC_HIGHLIGHT}]").strip()

                selected_files = files if sel.lower() == 'all' else []
                if not selected_files or sel == '0':
                    continue

                console.print("")
                success_count = 0
                fail_count = 0
                
                # Check Java
                import subprocess
                if subprocess.call("command -v java", shell=True,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
                    console.print(f"[{DC_ORANGE}]Java not found — installing...[/]")
                    subprocess.call("pkg install openjdk-17 -y", shell=True,
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                # Locate or download unluac.jar
                unluac_jar = _ensure_jar_for_file(selected_files[0], lua_base, script_dir)
                
                with Progress(
                    SpinnerColumn(style=f"bold {DC_HIGHLIGHT}"),
                    TextColumn("[bold white]Decompiling: {task.description}"),
                    BarColumn(complete_style=f"bold {DC_HIGHLIGHT}", finished_style=f"bold {DC_GREEN}"),
                    TimeElapsedColumn(),
                    console=console
                ) as progress:
                    task = progress.add_task(f"Starting...", total=len(selected_files))
                    
                    for f in selected_files:
                        progress.update(task, advance=1, description=f.name)
                        try:
                            # Step 1: Read input
                            raw = f.read_bytes()
                            
                            # Handle source files: compile if not bytecode
                            if not raw.startswith(b'\x1bLua'):
                                temp_source = lua_dec / f"{f.stem}.lua"
                                temp_source.write_bytes(raw)
                                temp_luac_path = lua_dec / f"{f.stem}.temp.luac"
                                result = _sp.run([LUAC_CMD, "-o", str(temp_luac_path), str(temp_source)], capture_output=True, text=True)
                                if result.returncode == 0:
                                    raw = temp_luac_path.read_bytes()
                                    temp_luac_path.unlink()
                                    temp_source.unlink()
                                else:
                                    err_msg = result.stderr.strip() or "Unknown error"
                                    raise ValueError(f"Compilation failed: {err_msg}")
                            
                            # Step 2: T24 → standard Lua 5.3 bytecode
                            standard_bytecode = process_lua_file(raw, is_encrypt=False)
                            
                            # Convert 32-bit standard to 64-bit for unluac compatibility
                            if standard_bytecode.startswith(b'\x1bLua'):
                                # Check if it's 32-bit (size_t == 4)
                                if standard_bytecode[13] == 4:
                                    console.print(f"  [dim]Converting 32-bit to 64-bit Lua bytecode...[/]")
                                    standard_bytecode = convert_32_to_64_lua53(standard_bytecode)
                            
                            # Step 3: Save temp .luac
                            temp_luac = lua_dec / f"{f.stem}.temp.luac"
                            temp_luac.write_bytes(standard_bytecode)
                            
                            # Step 4: Decompile via unluac.jar
                            out_lua = lua_dec / f"{f.stem}.lua"
                            
                            if unluac_jar and unluac_jar.exists():
                                r = _sp.run(
                                    ["java", "-jar", str(unluac_jar), str(temp_luac)],
                                    capture_output=True, text=True, timeout=120
                                )
                                if r.returncode == 0 and r.stdout.strip():
                                    out_lua.write_text(r.stdout, encoding='utf-8')
                                    console.print(f"  [dim]unluac: {f.name} → {out_lua.name}[/]")
                                    success_count += 1
                                else:
                                    err = (r.stderr or "").strip()[:200]
                                    console.print(f"  [dim {DC_ORANGE}]unluac error on {f.name}: {err}[/]")
                                    fail_count += 1
                            else:
                                console.print(f"  [dim {DC_RED}]unluac.jar not found![/]")
                                fail_count += 1
                                
                            # Cleanup
                            if temp_luac.exists():
                                temp_luac.unlink()
                            
                        except Exception as e:
                            console.print(f"  [dim {DC_RED}]Decompile failed {f.name}: {e}[/]")
                            fail_count += 1

                # Summary Dashboard
                summary_table = Table(title="DECOMPILE SUMMARY", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
                summary_table.add_column("Metric", style="bold white")
                summary_table.add_column("Value", style=f"bold {DC_HIGHLIGHT}")
                summary_table.add_row("Total Attempted", str(len(selected_files)))
                summary_table.add_row("Success", f"[bold {DC_GREEN}]{success_count}[/]")
                summary_table.add_row("Failed", f"[bold {DC_RED}]{fail_count}[/]")
                
                console.print(Panel(summary_table, border_style=DC_HIGHLIGHT, box=HEAVY_EDGE))
                console.print(f"[bold {DC_HIGHLIGHT}]Output Directory: {lua_dec}[/]")
                safe_input('\nPress Enter to continue...')


            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")

        # ── Option 2: Recompile ──
        elif choice == "2":
            if not LUA_XOR_KEY:
                console.print(Panel(
                    f"[bold {DC_ORANGE}]Lua XOR key not available.[/]\n"
                    f"Create: [bold {DC_HIGHLIGHT}]{lua_base / 'lua_xor_key.txt'}[/]\n"
                    f"Put key as HEX on one line.",
                    title=f"[bold {DC_ORANGE}] KEY REQUIRED [/]",
                    border_style=DC_ORANGE,
                    box=HEAVY_EDGE
                ))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            console.clear()
            print_banner()
            files = [f for f in lua_edit.iterdir() if f.is_file() and f.suffix in ['.lua', '.luac']]
            if not files:
                console.print(Panel(f"[{DC_RED}]No files in {lua_edit.resolve()}[/]", border_style=DC_RED))
            else:
                file_list = "\n".join([f"  [bold {DC_HIGHLIGHT}]{i}.[/] [bold {DC_TEXT}]{f.name}[/]" for i, f in enumerate(files, 1)])
                console.print(Panel(file_list, title="[bold {DC_HIGHLIGHT}]Available Files[/]", border_style=DC_BORDER, box=DOUBLE_EDGE))
                sel = safe_input(f"\n[bold {DC_HIGHLIGHT}]Select file(s), 'all', or '0': [/bold {DC_HIGHLIGHT}]").strip()

                selected_files = []
                if sel == '0':
                    continue
                elif sel.lower() == 'all':
                    selected_files = files
                else:
                    for x in sel.split(','):
                        if x.strip().isdigit():
                            idx = int(x.strip()) - 1
                            if 0 <= idx < len(files):
                                selected_files.append(files[idx])

                if not selected_files:
                    console.print(Panel(f"[{DC_RED}]Invalid![/]", border_style=DC_RED))
                else:
                    for f in selected_files:
                        try:
                            process_file = f
                            if f.suffix == '.lua':
                                process_file = lua_edit / f"{f.stem}.std.luac"
                                subprocess.run([LUAC_CMD, "-o", str(process_file), str(f)])

                            with open(process_file, 'rb') as fp:
                                data = fp.read()

                            bgmi_data = process_lua_file(data, is_encrypt=True)
                            final_out = lua_res / f"{f.stem}.lua"
                            with open(final_out, 'wb') as fp:
                                fp.write(bgmi_data)

                            console.print(Panel(
                                f"[bold {DC_HIGHLIGHT}]File:[/] [bold {DC_TEXT}]{f.name}[/]\n"
                                f"[bold {DC_HIGHLIGHT}]Output:[/] [dim {DC_DIM}]Lua_Rueslt/{final_out.name}[/]",
                                title=f"[bold black on {DC_HIGHLIGHT}] ENCRYPTION SUCCESS [/]",
                                border_style=DC_BORDER,
                                box=HEAVY_EDGE
                            ))
                            if f.suffix == '.lua' and process_file.exists():
                                process_file.unlink()
                        except Exception as e:
                            console.print(Panel(f"[bold {DC_RED}]Error {f.name}: {e}[/]",
                                                border_style=DC_RED, box=HEAVY_EDGE))
            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")

        # ── Option 3: Repack Any Size ──
        elif choice == "3":
            console.clear()
            print_banner()
            console.print(Panel(
                f"[bold {DC_HIGHLIGHT}]LUA REPACK TO PATH[/bold {DC_HIGHLIGHT}]\n"
                f"[dim {DC_DIM}]Target path do aur Lua files inject karo[/dim {DC_DIM}]",
                border_style=DC_BORDER, box=HEAVY_EDGE
            ))

            pak_files = [f for f in lua_org_pak.iterdir() if f.is_file() and f.suffix.lower() in ['.pak', '.obb']]
            if not pak_files:
                console.print(Panel(
                    f"[{DC_RED}]No Original PAK found in {lua_org_pak.resolve()}[/]",
                    border_style=DC_RED, box=HEAVY_EDGE
                ))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            if len(pak_files) == 1:
                target_pak = pak_files[0]
                console.print(f"[bold {DC_HIGHLIGHT}]PAK:[/] [bold {DC_TEXT}]{target_pak.name}[/]")
            else:
                file_list_str = "\n".join([f"  [bold {DC_HIGHLIGHT}]{i}.[/] [bold {DC_TEXT}]{f.name}[/]" for i, f in enumerate(pak_files, 1)])
                console.print(Panel(file_list_str, title="[bold {DC_HIGHLIGHT}]Select PAK[/]", border_style=DC_BORDER, box=DOUBLE_EDGE))
                sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select number (0 = back): [/bold {DC_HIGHLIGHT}]")
                if not sel.strip().isdigit() or int(sel.strip()) == 0:
                    continue
                if not (1 <= int(sel.strip()) <= len(pak_files)):
                    continue
                target_pak = pak_files[int(sel.strip()) - 1]

            out_pak = lua_mod_repack / target_pak.name

            mod_luas = [f for f in lua_edit.iterdir() if f.is_file()]
            if not mod_luas:
                console.print(Panel(f"[{DC_RED}]No edited Lua files in {lua_edit.resolve()}[/]",
                                    border_style=DC_RED, box=HEAVY_EDGE))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            console.print()
            console.print(Panel(
                f"[bold {DC_HIGHLIGHT}]Target path daalo (PAK ke andar)[/]\n"
                f"[dim {DC_DIM}]Example: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core[/dim {DC_DIM}]\n"
                f"[dim {DC_DIM}]Ya Enter dabao - same naam ki file replace karega[/dim {DC_DIM}]",
                border_style=DC_BORDER, box=ROUNDED
            ))
            target_path = safe_input(f"[bold {DC_HIGHLIGHT}]Path: [/bold {DC_HIGHLIGHT}]").strip()
            target_path = target_path.replace('\\', '/').strip('/')

            force_bypass = console.input(f"[bold {DC_HIGHLIGHT}]Force Original Hash Bypass? (y/n): [/]").strip().lower() in ('y', 'yes')
            force_shield = console.input(f"[bold {DC_HIGHLIGHT}]Enable Ultimate Anti-Ban Shield (CRC + Exact Size)? (y/n): [/]").strip().lower() in ('y', 'yes')

            try:
                console.print(f"\n[bold {DC_HIGHLIGHT}]Repacking...[/]")
                pak_editor = TencentPakFile(target_pak)
                out_pak.parent.mkdir(parents=True, exist_ok=True)

                force_add = bool(target_path)
                result = repack_pak_file_full(
                    pak_editor, lua_edit, out_pak,
                    target_path if target_path else None,
                    force_add=force_add,
                    force_crc=force_shield,
                    force_size=force_shield
                )
                if isinstance(result, tuple):
                    count, stats = result
                else:
                    count = result
                    stats = None
                
                if count > 0:
                    if stats:
                        print_forensic_dashboard(stats, out_pak, title_text="REPACK FORENSIC ANALYSIS", force_safe=force_bypass)
                    else:
                        console.print(Panel(
                            f"[bold {DC_HIGHLIGHT}]Successfully processed {count} files![/]\n"
                            f"[bold {DC_HIGHLIGHT}]Output:[/] [bold {DC_TEXT}]{out_pak}[/]"
                            + (f"\n[bold {DC_HIGHLIGHT}]Target:[/] [bold {DC_TEXT}]{target_path}[/]" if target_path else ""),
                            border_style=DC_BORDER, box=HEAVY_EDGE
                        ))
                else:
                    console.print(Panel(f"[{DC_RED}]No files processed![/]", border_style=DC_RED))

            except Exception as e:
                console.print(Panel(f"[{DC_RED}]Repack failed: {e}[/]", border_style=DC_RED))
                import traceback
                traceback.print_exc()

            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")

        # ── Option 4: CSV Smart Injector ──
        elif choice == "4":
            console.clear()
            print_banner()

            csv_dir = lua_custom / "PUBG_CSV"
            if not download_csv_files(csv_dir):
                console.print(Panel(f"[{DC_RED}]CSV download failed![/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            selected_csv, is_bgmi, game_label = _select_csv_source(csv_dir)
            if selected_csv is None:
                continue

            console.print(f"[bold {DC_HIGHLIGHT}]Loading {selected_csv.name}...[/]")
            file_path_map = _load_csv_path_map(selected_csv)
            if not file_path_map:
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue
            console.print(f"[bold {DC_HIGHLIGHT}]Loaded {len(file_path_map)} paths from {game_label}[/]")

            # Select PAK
            pak_files = [f for f in lua_custom_pak.iterdir() if f.suffix.lower() in ['.pak', '.obb']]
            if not pak_files:
                console.print(Panel(f"[{DC_RED}]No PAK in LUA_CUSTOM/PAK![/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            target_pak = pak_files[0]
            out_pak = lua_custom_result / target_pak.name

            edit_files = [p for p in lua_custom_edit.rglob('*') if p.is_file()]
            if not edit_files:
                console.print(Panel(f"[{DC_RED}]No files in LUA_CUSTOM/EDIT![/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            resolved_files, unresolved = _resolve_paths_from_csv(lua_custom_edit, file_path_map, is_bgmi)
            if not resolved_files:
                console.print(Panel(f"[{DC_RED}]No files matched![/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            lines = [f"[bold {DC_HIGHLIGHT}]CSV: {game_label} ({selected_csv.name})[/]", ""]
            for p, rp in resolved_files:
                lines.append(f"  [bold {DC_HIGHLIGHT}]✓[/] [white]{p.name}[/] [dim]→[/] [bold {DC_HIGHLIGHT}]{rp}[/]")
            lines.append("")
            lines.append(f"[bold {DC_HIGHLIGHT}]Total: {len(resolved_files)} files[/]")
            console.print(Panel("\n".join(lines), border_style=DC_HIGHLIGHT, box=HEAVY_EDGE,
                                title=f"[bold black on {DC_HIGHLIGHT}] CSV PATH RESOLVER [/]"))

            confirm = safe_input(f"\n[bold {DC_HIGHLIGHT}]Proceed? (y/n): [/]").strip().lower()
            if confirm not in ('y', 'yes'):
                continue
                
            force_bypass = console.input(f"[bold {DC_HIGHLIGHT}]Force Original Hash Bypass? (y/n): [/]").strip().lower() in ('y', 'yes')

            csv_path_map = {p.name: rp for p, rp in resolved_files}
            try:
                pak = TencentPakFile(target_pak)
                result = repack_pak_file_full(pak, lua_custom_edit, out_pak, target_path=None, force_add=True, force_crc=force_bypass, force_size=force_bypass, csv_path_map=csv_path_map)
                if isinstance(result, tuple):
                    count, stats = result
                else:
                    count = result
                    stats = None
                
                if count > 0:
                    if stats:
                        print_forensic_dashboard(stats, out_pak, title_text="LUA INJECTOR ANALYSIS", force_safe=force_bypass)
                    else:
                        console.print(Panel(f"[bold {DC_HIGHLIGHT}]Processed {count} files![/]\n"
                                          f"[bold {DC_HIGHLIGHT}]Output:[/] [bold {DC_TEXT}]{out_pak}[/]",
                                          border_style=DC_HIGHLIGHT, box=HEAVY_EDGE))
                else:
                    console.print(Panel(f"[{DC_RED}]No files processed![/]", border_style=DC_RED))

            except Exception as e:
                console.print(Panel(f"[{DC_RED}]Failed: {e}[/]", border_style=DC_RED))
                import traceback
                traceback.print_exc()

            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")

        # ── Option 6: Lua Compile (Plain) ──
        elif choice == "5":
            console.clear()
            print_banner()
            console.print(Panel(
                f"[bold {DC_HIGHLIGHT}]LUA COMPILE (GAME-READY)[/]\n"
                f"[dim {DC_DIM}]Readable .lua → BGMI T24 format[/dim {DC_DIM}]",
                border_style=DC_BORDER, box=HEAVY_EDGE
            ))

            compile_src = lua_edit
            compile_out = lua_res
            os.makedirs(to_long_path(compile_out), exist_ok=True)

            files = [f for f in compile_src.iterdir() if f.is_file() and f.suffix in ['.lua', '.luac']]
            if not files:
                console.print(Panel(f"[{DC_RED}]No files in {compile_src}[/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            file_list = "\n".join([f"  [bold {DC_HIGHLIGHT}]{i}.[/] [bold {DC_TEXT}]{f.name}[/]" for i, f in enumerate(files, 1)])
            console.print(Panel(file_list, title="[bold {DC_HIGHLIGHT}]Available Files[/]", border_style=DC_BORDER, box=DOUBLE_EDGE))

            sel = safe_input(f"\n[bold {DC_HIGHLIGHT}]Select file(s), 'all', or '0': [/]").strip()
            if sel.strip() == '0':
                continue

            selected = []
            if sel.lower() == 'all':
                selected = files
            else:
                for x in sel.split(','):
                    if x.strip().isdigit():
                        idx = int(x.strip()) - 1
                        if 0 <= idx < len(files):
                            selected.append(files[idx])

            if not selected:
                continue

            luac_path = shutil.which(LUAC_CMD)
            if luac_path is None:
                console.print(Panel(f"[{DC_ORANGE}]{LUAC_CMD} not found! pkg install lua53 -y[/]", border_style=DC_RED))
                safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")
                continue

            ok = 0
            for f in selected:
                try:
                    out_file = compile_out / f"{f.stem}.lua"
                    console.print(f"\n[bold {DC_HIGHLIGHT}]Compiling: {f.name}...[/]")

                    if f.suffix == '.lua':
                        temp_luac = compile_out / f"{f.stem}.std.luac"
                        result = subprocess.run(
                            [LUAC_CMD, "-o", str(temp_luac), str(f)],
                            capture_output=True, text=True
                        )
                        if result.returncode != 0 or not temp_luac.exists():
                            err = result.stderr.strip() or "luac5.3 failed"
                            console.print(Panel(f"[{DC_RED}]FAILED: {f.name}\n{err[:300]}[/]", border_style=DC_RED))
                            continue
                        process_file = temp_luac
                    else:
                        process_file = f

                    with open(process_file, 'rb') as fp:
                        data = fp.read()

                    bgmi_data = process_lua_file(data, is_encrypt=True)

                    with open(out_file, 'wb') as fp:
                        fp.write(bgmi_data)

                    if f.suffix == '.lua' and process_file.exists():
                        process_file.unlink()

                    if out_file.exists() and out_file.stat().st_size > 0:
                        ok += 1
                        size = out_file.stat().st_size
                        console.print(Panel(
                            f"[bold {DC_HIGHLIGHT}]COMPILED: {f.name} → {out_file.name} ({size:,} bytes)[/]",
                            border_style=DC_BORDER, box=HEAVY_EDGE
                        ))
                except Exception as e:
                    console.print(Panel(f"[{DC_RED}]Error: {f.name} - {e}[/]", border_style=DC_RED))

            console.print()
            if ok > 0:
                console.print(Panel(
                    f"[bold {DC_HIGHLIGHT}]{ok}/{len(selected)} files compiled![/]\n"
                    f"[bold {DC_HIGHLIGHT}]Output:[/] [bold {DC_TEXT}]{compile_out}[/]",
                    border_style=DC_BORDER, box=DOUBLE_EDGE
                ))
            else:
                console.print(Panel(f"[{DC_ORANGE}]No files compiled.[/]", border_style=DC_ORANGE))

            safe_input(f"\n[bold {DC_HIGHLIGHT}]Press Enter...[/]")

        elif choice == "0":
            return


# =====================================================================
# END OF PART 7
# =====================================================================# =====================================================================
# PART 8 - BLACK TOOL (UE4 String Editor) Complete
# =====================================================================

# =====================================================================
# BLACK TOOL GLOBALS
# =====================================================================

WORK_DIR_BLACK = ""
MODIFIED_DIR_BLACK = ""

# Target groups for custom edit (from hake.py)
TARGET_GROUPS = {
    "1. MATCH START & THEME": [
        "Match starts in <MatchStartInfo>{0}</>", "Match starts in",
        "Your match starts in", "Bonus Challenge match starts",
        "LEAN (BGMI 2026 Theme Song)"
    ],
    "2. CHICKEN DINNER": [
        "WINNER WINNER CHICKEN DINNER!", "WINNER WINNER CHICKEN DINNER",
        "Winner Winner Chicken Dinner", "Winner winner chicken dinner"
    ],
    "3. BETTER LUCK NEXT TIME": [
        "Better Luck Next Time", "BETTER LUCK NEXT TIME"
    ],
    "4. TEAMMATE DAMAGE WARNINGS": [
        "As you attacked your teammate first",
        "As you have maliciously injured your teammate"
    ],
    "5. QUICK CHAT MESSAGES": [
        "Watch your aim and finish them off!",
        "Get behind the wheel and crush them!"
    ],
    "6. BAN PAN SECURITY": [
        "Ban Pan", "Ban Pan - Pan", "BGMI & Ban Pan"
    ],
    "7. SPLASH SCREEN WARNING": [
        "Battlegrounds Mobile India is not a real-world based game"
    ],
    "8. HOME ISLE NOTIFICATIONS": [
        "Home Isle is an island located in the ocean",
        "Now, let me briefly explain removing objects",
        "Lastly, here's an important tip",
        "It's important to note that once you finish building",
        "Your time spent working on your Home has reached a new milestone!",
        "This past year witnessed our growth and progress",
        "There are so many beautiful moments we have shared together."
    ],
    "9. GAME EVENTS & UI": [
        "Sara is a vehicle expert",
        "Vehicle weapons will automatically lock",
        "Try out the DJ stage",
        "You have collected 3 vehicle finishes",
        "Clan Battle is about to start",
        "Try the smart Digi-pal chat",
        "Too many PvE enemy eliminations",
        "Synergy: Some Popularity gifts",
        "Win battles with your friends",
        "The Aerolith has begun absorbing mutants",
        "8. If you have any questions regarding payment",
        "Myriad splendors glazed"
    ]
}


# =====================================================================
# BLACK TOOL HELPERS
# =====================================================================

def black_tool_ensure_work_dir():
    global WORK_DIR_BLACK, MODIFIED_DIR_BLACK

    for d in [WORK_DIR_BLACK, MODIFIED_DIR_BLACK]:
        if d and not os.path.exists(d):
            try:
                os.makedirs(d)
            except Exception as e:
                console.print(f"[red]Cannot create directory {d}: {e}[/red]")
                return


def black_tool_list_files_in_dir(extensions=('.uasset', '.uexp')):
    try:
        if not os.path.exists(WORK_DIR_BLACK):
            black_tool_ensure_work_dir()
        all_files = os.listdir(WORK_DIR_BLACK)
        target_files = [f for f in all_files if f.lower().endswith(extensions)]
        target_files.sort()
        return target_files
    except Exception as e:
        console.print(f"[red]Error reading directory: {e}[/red]")
        return []


# =====================================================================
# UE4 STRING TOOL CLASS
# =====================================================================

class UE4StringTool:
    def __init__(self):
        self.MIN_STRING_LEN = 2
        self.MAX_STRING_LEN = 8000

    def read_int(self, f):
        data = f.read(4)
        if len(data) < 4:
            return None
        return struct.unpack('<i', data)[0]

    def is_garbage_text(self, text):
        if not text or len(text.strip()) == 0:
            return True
        allowed_control = {'\n', '\r', '\t'}
        for char in text:
            code = ord(char)
            if code == 0:
                return True
            if code < 32 and char not in allowed_control:
                return True
            if char == '\ufffd':
                return True
        return False

    def is_valid_string_start(self, f, current_pos):
        f.seek(current_pos)
        length = self.read_int(f)
        if length is None:
            return False
        if length == 0:
            return False
        if not (self.MIN_STRING_LEN <= abs(length) <= self.MAX_STRING_LEN):
            return False
        try:
            if length < 0:
                read_len = -length * 2
                data = f.read(read_len)
                if len(data) != read_len:
                    return False
                if data[-2:] != b'\x00\x00':
                    return False
                text = data[:-2].decode('utf-16le')
            else:
                read_len = length
                data = f.read(read_len)
                if len(data) != read_len:
                    return False
                if data[-1:] != b'\x00':
                    return False
                text = data[:-1].decode('utf-8')
            if self.is_garbage_text(text):
                return False
            return True
        except Exception:
            return False

    def extract_file(self, file_name):
        file_path = os.path.join(WORK_DIR_BLACK, file_name)
        if not os.path.exists(file_path):
            return False, f"File not found: {file_name}"

        json_path = file_path + ".json"
        console.print(f"\n[bold {DC_HIGHLIGHT}]Create JSON: {file_name}[/]")

        try:
            with open(file_path, 'rb') as f:
                f.seek(0, 2)
                file_size = f.tell()
                f.seek(0)

                entries = []
                cursor = 0

                with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                              BarColumn(), console=console) as progress:
                    task = progress.add_task("[cyan]Extracting strings...", total=file_size)

                    while cursor < file_size - 4:
                        progress.update(task, completed=cursor)

                        if self.is_valid_string_start(f, cursor):
                            f.seek(cursor)
                            length = self.read_int(f)
                            is_utf16 = length < 0
                            abs_len = abs(length)

                            if is_utf16:
                                raw_data = f.read(abs_len * 2)
                                text = raw_data[:-2].decode('utf-16le')
                                total_size = 4 + (abs_len * 2)
                            else:
                                raw_data = f.read(abs_len)
                                text = raw_data[:-1].decode('utf-8')
                                total_size = 4 + abs_len

                            entries.append({
                                "offset": cursor,
                                "original_len_int": length,
                                "text": text
                            })
                            cursor += total_size
                        else:
                            cursor += 1

                if not entries:
                    return False, "No valid text strings found."

                with open(json_path, 'w', encoding='utf-8') as jf:
                    json.dump(entries, jf, indent=4, ensure_ascii=False)

            return True, f"Exported {len(entries)} strings -> {os.path.basename(json_path)}"
        except Exception as e:
            return False, str(e)

    def repack_file(self, file_name):
        original_file_path = os.path.join(WORK_DIR_BLACK, file_name)
        json_path = original_file_path + ".json"

        if not os.path.exists(original_file_path):
            return False, f"Missing original file: {file_name}"
        if not os.path.exists(json_path):
            return False, f"Missing file: {file_name}.json"

        modified_file_path = os.path.join(MODIFIED_DIR_BLACK, file_name)
        console.print(f"[bold {DC_HIGHLIGHT}]Repacking: {file_name}...[/]")

        try:
            with open(json_path, 'r', encoding='utf-8') as jf:
                entries = json.load(jf)
            entries.sort(key=lambda x: x['offset'])

            with open(original_file_path, 'rb') as f_orig, open(modified_file_path, 'wb') as f_out:
                cursor_orig = 0
                count_modified = 0

                for i, entry in enumerate(entries):
                    gap_size = entry['offset'] - cursor_orig
                    if gap_size > 0:
                        f_out.write(f_orig.read(gap_size))
                    elif gap_size < 0:
                        f_orig.seek(entry['offset'])

                    new_text = entry['text']
                    old_len_int = entry['original_len_int']
                    is_utf16 = old_len_int < 0

                    if is_utf16:
                        max_byte_size = abs(old_len_int) * 2
                    else:
                        max_byte_size = abs(old_len_int)

                    f_orig.seek(entry['offset'] + 4)
                    old_raw_display = f_orig.read(max_byte_size)

                    try:
                        if is_utf16:
                            old_text_display = old_raw_display[:-2].decode('utf-16le')
                        else:
                            old_text_display = old_raw_display[:-1].decode('utf-8')
                    except Exception:
                        old_text_display = "<Decode error>"

                    if new_text != old_text_display:
                        count_modified += 1

                    if is_utf16:
                        new_bytes = new_text.encode('utf-16le') + b'\x00\x00'
                    else:
                        new_bytes = new_text.encode('utf-8') + b'\x00'

                    current_byte_size = len(new_bytes)

                    if current_byte_size > max_byte_size:
                        console.print(f"\n[bold {DC_RED}]CRITICAL ERROR AT LINE {i+1} (Offset: {entry['offset']})[/]")
                        console.print(f"[bold {DC_RED}]New string longer than original ({current_byte_size} > {max_byte_size} bytes)[/]")
                        f_out.close()
                        f_orig.close()
                        if os.path.exists(modified_file_path):
                            os.remove(modified_file_path)
                        return False, "New string length exceeds original string length."

                    f_out.write(struct.pack('<i', old_len_int))
                    f_out.write(new_bytes)

                    pad_len = max_byte_size - current_byte_size
                    if pad_len > 0:
                        f_out.write(b'\x00' * pad_len)

                    f_orig.seek(entry['offset'])
                    len_check = self.read_int(f_orig)
                    skip_len = 4 + (abs(len_check) * 2 if len_check < 0 else abs(len_check))
                    f_orig.seek(entry['offset'] + skip_len)
                    cursor_orig = f_orig.tell()

                f_out.write(f_orig.read())

            return True, f"Updated {count_modified} lines -> {os.path.basename(modified_file_path)}"
        except Exception as e:
            return False, str(e)


# =====================================================================
# LIVE INPUT (MATCH START)
# =====================================================================

def get_live_input_match_start(prompt_text):
    import sys as _s
    _s.stdout.write(prompt_text)
    _s.stdout.flush()
    input_str = ""

    while True:
        try:
            fd = _s.stdin.fileno()
            import termios
            import tty
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(_s.stdin.fileno())
                ch = _s.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except Exception:
            ch = input()[0] if input() else '\r'

        if ch == '\r':
            print()
            break
        elif ch == '\x7f':
            if len(input_str) > 0:
                input_str = input_str[:-1]
        else:
            input_str += ch

        _s.stdout.write('\r' + ' ' * (len(prompt_text) + len(input_str) + 15) + '\r')
        _s.stdout.write(prompt_text)
        display = input_str
        _s.stdout.write(f"\033[93m{display}\033[0m")
        _s.stdout.flush()

    return input_str


# =====================================================================
# BLACK TOOL FLOWS
# =====================================================================

def black_tool_do_unpack_fancy(tool):
    console.clear()
    print_banner()
    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]MASTER UNPACK (ALL FILES)[/]\n"
        f"[dim {DC_DIM}]Extracting all UEXP/UASSET files to JSON at once...[/dim {DC_DIM}]",
        border_style=DC_BORDER
    ))

    files = black_tool_list_files_in_dir(('.uasset', '.uexp'))
    if not files:
        console.print(Panel(f"[{DC_RED}]No files found to unpack![/]", border_style=DC_RED))
        safe_input(f"\n[bold {DC_TEXT}]Press Enter to continue...[/]")
        return

    unpacked_count = 0
    console.print(f"\n[bold {DC_HIGHLIGHT}]Auto-Unpacking all files...[/]")

    for fname in files:
        success, msg = tool.extract_file(fname)
        if success:
            console.print(f"[bold {DC_HIGHLIGHT}]SUCCESS:[/] {fname}")
            unpacked_count += 1
        else:
            console.print(f"[bold {DC_RED}]FAILED:[/] {fname}\n   [dim]{msg}[/dim]")

    console.print("\n")
    if unpacked_count > 0:
        console.print(Panel(
            f"[bold {DC_HIGHLIGHT}]ALL DONE! {unpacked_count} files unpacked successfully.[/]\n"
            f"[white]JSON files created in ORGNAL folder.[/white]",
            border_style=DC_BORDER
        ))
    else:
        console.print(Panel(f"[{DC_ORANGE}]No files were unpacked.[/]", border_style=DC_ORANGE))

    safe_input("\n[bold white]Press Enter to continue...[/bold white]")


def black_tool_do_repack_fancy(tool):
    console.clear()
    print_banner()
    console.print(Panel(
        f"[bold {DC_HIGHLIGHT}]MASTER REPACK (ALL FILES)[/]\n"
        f"[dim {DC_DIM}]Converting all JSON back to UEXP at once...[/dim {DC_DIM}]",
        border_style=DC_BORDER
    ))

    files = black_tool_list_files_in_dir(('.uasset', '.uexp'))
    if not files:
        console.print(Panel(f"[{DC_RED}]No files found to repack![/]", border_style=DC_RED))
        safe_input(f"\n[bold white]Press Enter to continue...[/bold white]")
        return

    repacked_count = 0
    repacked_files_list = []

    console.print(f"\n[bold {DC_HIGHLIGHT}]Auto-Repacking all files...[/]")

    for fname in files:
        json_path = os.path.join(WORK_DIR_BLACK, fname + ".json")
        if os.path.exists(json_path):
            success, msg = tool.repack_file(fname)
            if success:
                console.print(f"[bold {DC_HIGHLIGHT}]SUCCESS:[/] {fname}")
                repacked_count += 1
                repacked_files_list.append(fname)
            else:
                console.print(f"[bold {DC_RED}]FAILED:[/] {fname}\n   [dim]{msg}[/dim]")
        else:
            console.print(f"[dim {DC_ORANGE}]Skipped (No JSON): {fname}[/]")

    console.print("\n")
    if repacked_count > 0:
        console.print(Panel(
            f"[bold {DC_HIGHLIGHT}]ALL DONE! {repacked_count} files repacked![/]\n"
            f"[white]Files are in MODDED FILE folder.[/white]",
            border_style=DC_BORDER
        ))

        copy_choice = safe_input(
            f"\n[bold {DC_ORANGE}]Copy to 'Modified_files' and 'MOD_REPACK'? (y/n): [/]"
        ).default if hasattr(safe_input, 'default') else safe_input(
            f"\n[bold {DC_ORANGE}]Copy to 'Modified_files' and 'MOD_REPACK'? (y/n): [/]"
        )
        if copy_choice.lower() != 'y':
            copy_choice = 'n'

        # Simple safe version
        copy_choice = safe_input(
            f"\n[bold {DC_ORANGE}]Copy to Modified_files? (y/n): [/]"
        ).strip().lower()

        if copy_choice == 'y':
            base_dir = Path(BASE_DIR_NAME)
            target_modified = base_dir / "OBB_UNPACKER" / "Modified_files"
            target_enc_open = base_dir / "ANTIRESET_OBB" / "MOD_REPACK"

            os.makedirs(to_long_path(target_modified), exist_ok=True)
            os.makedirs(to_long_path(target_enc_open), exist_ok=True)

            copied_mod = 0
            copied_enc = 0

            for fname in repacked_files_list:
                src = os.path.join(MODIFIED_DIR_BLACK, fname)
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(target_modified, fname))
                    copied_mod += 1
                    shutil.copy2(src, os.path.join(target_enc_open, fname))
                    copied_enc += 1

            if copied_mod > 0:
                console.print(f"\n[bold {DC_HIGHLIGHT}]{copied_mod} files copied to 'Modified_files'![/]")
            if copied_enc > 0:
                console.print(f"[bold {DC_HIGHLIGHT}]{copied_enc} files copied to 'MOD_REPACK'![/]")

    else:
        console.print(Panel(f"[{DC_ORANGE}]No files were repacked.[/]", border_style=DC_ORANGE))

    safe_input("\n[bold white]Press Enter to continue...[/bold white]")


def black_tool_do_custom_edit_fancy(tool):
    print_banner()
    json_files = [f for f in os.listdir(WORK_DIR_BLACK) if f.endswith('.json')]

    if not json_files:
        console.print(f"[red]No JSON files found![/red]")
        safe_input("\n[bold white]Press Enter...[/bold white]")
        return

    for j_file in json_files:
        json_path = os.path.join(WORK_DIR_BLACK, j_file)
        with open(json_path, 'r', encoding='utf-8') as f:
            entries = json.load(f)

        for group_name, keywords in TARGET_GROUPS.items():
            matching_entries = [e for e in entries if any(kw in e['text'] for kw in keywords)]

            if matching_entries:
                console.print(f"\n[bold cyan]Target:[/] [white]{group_name}[/]")

                if "1. MATCH START" in group_name:
                    try:
                        new_text = get_live_input_match_start(f" \033[1;32mENTER YELLOW TEXT > \033[0m")
                    except Exception:
                        new_text = Prompt.ask(f"[bold {DC_HIGHLIGHT}]Enter text[/]")
                else:
                    new_text = Prompt.ask(f"[bold {DC_HIGHLIGHT}]Enter normal text[/]")

                if new_text and new_text.strip():
                    processed_text = new_text
                    if "1. MATCH START" in group_name:
                        if "[" in processed_text and "]" in processed_text:
                            parts = processed_text.split("[", 1)
                            pre = parts[0]
                            inner_post = parts[1].split("]", 1)
                            inner = inner_post[0]
                            post = inner_post[1] if len(inner_post) > 1 else ""
                            processed_text = f"{pre}[ <MatchStartInfo>{inner}</>]{post}"
                        else:
                            processed_text = f"<MatchStartInfo>{processed_text}</>"

                    for e in matching_entries:
                        e_max = abs(e['original_len_int'])
                        e['text'] = processed_text[:e_max - 1]

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=4, ensure_ascii=False)

    console.print(Panel(f"[bold {DC_HIGHLIGHT}]ALL DONE: Targeted Modding Complete![/]", border_style=DC_BORDER))
    safe_input("\nPress Enter to continue...", default="")


# =====================================================================
# BLACK TOOL MAIN
# =====================================================================

def black_tool_main(auto_select_file="mini_obb.pak"):
    global WORK_DIR_BLACK, MODIFIED_DIR_BLACK

    WORK_DIR_BLACK = str(Path(BASE_DIR_NAME) / "CREDIT_TOOL" / "ORGNAL")
    MODIFIED_DIR_BLACK = str(Path(BASE_DIR_NAME) / "CREDIT_TOOL" / "MODDED FILE")

    black_tool_ensure_work_dir()

    REQUIRED_FILES = ["LocalizationText_en.uexp", "SplashScreen_BH.uexp"]
    missing_files = [
        f for f in REQUIRED_FILES
        if not os.path.exists(os.path.join(WORK_DIR_BLACK, f))
        or os.path.getsize(os.path.join(WORK_DIR_BLACK, f)) == 0
    ]

    if missing_files:
        console.print(f"\n[bold {DC_ORANGE}]Missing files in ORGNAL: {', '.join(missing_files)}[/]")
        obb_folder = Path(BASE_DIR_NAME) / "OBB_UNPACKER" / "ORGNAL"

        pak_files = []
        if obb_folder.exists():
            pak_files = [
                f for f in obb_folder.iterdir()
                if f.is_file() and f.suffix.lower() in ('.pak', '.obb')
            ]

        if pak_files:
            target_index = -1
            if auto_select_file:
                for i, p in enumerate(pak_files):
                    if p.name.lower() == auto_select_file.lower():
                        target_index = i
                        break

            if target_index != -1:
                pak_path = pak_files[target_index]
                console.print(f"[bold {DC_HIGHLIGHT}]AUTO-SELECTING:[/] [white]{pak_path.name}[/white]")
            else:
                for i, p in enumerate(pak_files, 1):
                    console.print(f"  [{DC_HIGHLIGHT}]{i}.[/] {p.name}")

                pick = safe_input(f"[bold {DC_HIGHLIGHT}]Select OBB/PAK (1-{len(pak_files)}): [/]").strip()
                try:
                    pak_path = pak_files[int(pick) - 1]
                except (ValueError, IndexError):
                    pak_path = pak_files[0]

            console.print(f"\n[bold {DC_HIGHLIGHT}]PRO EXTRACTION: Scanning {pak_path.name}...[/]")
            try:
                pak = TencentPakFile(pak_path, silent=True)
                for target_file in missing_files:
                    candidates = []
                    for dir_path, dir_entries in pak._index.items():
                        for fname, entry in dir_entries.items():
                            if fname.lower() == target_file.lower() and entry is not None:
                                candidates.append(entry)
                    if candidates:
                        candidates.sort(key=lambda x: x.size, reverse=True)
                        for entry in candidates:
                            target_dest = Path(WORK_DIR_BLACK) / target_file
                            pak._write_to_disk(target_dest, entry)
                            if os.path.getsize(target_dest) > 1024:
                                console.print(f"[bold {DC_HIGHLIGHT}]EXTRACT SUCCESS:[/] {target_file}")
                                break
            except Exception as e:
                console.print(f"[red]Error parsing OBB: {e}[/red]")

            safe_input("\n[bold white]Press Enter to continue...[/bold white]")
        else:
            console.print(f"[bold {DC_RED}]No OBB found in {obb_folder}![/]")
            safe_input("\n[bold white]Press Enter...[/bold white]")

    tool = UE4StringTool()

    while True:
        print_banner()

        menu_table = Table(show_header=False, box=SIMPLE, expand=True)
        menu_table.add_column("OPT", style="bold white", justify="center", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_HIGHLIGHT}")
        menu_table.add_column("DESC", style="dim white")
        menu_table.add_row("1", "UNPACK", "UEXP to JSON")
        menu_table.add_row("2", "REPACK", "JSON to UEXP")
        menu_table.add_row("3", "MASTER CUSTOM EDIT", "Live Color Edit")
        menu_table.add_row("4", "BACK", "Back to Main Menu")

        console.print(Panel(menu_table, border_style=DC_BORDER, box=HEAVY_EDGE,
                            title=f"[bold black on {DC_HIGHLIGHT}] BLACK TOOL OPTIONS [/]"))

        choice = safe_input(f"[bold {DC_HIGHLIGHT}]Select option > [/]").strip()

        if choice == '1':
            black_tool_do_unpack_fancy(tool)
        elif choice == '2':
            black_tool_do_repack_fancy(tool)
        elif choice == '3':
            black_tool_do_custom_edit_fancy(tool)
        elif choice == '4':
            return
        else:
            console.print(f"[{DC_RED}]Invalid![/]")
            time.sleep(1)


# =====================================================================
# END OF PART 8
# =====================================================================# =====================================================================
# PART 9 - MENU, MAIN, BANNER, SECURITY (FINAL)
# =====================================================================

# =====================================================================
# SECURITY / PROTECTION SYSTEM (stub - safe offline)
# =====================================================================

APP_VERSION = "8.0"
SERVER_ENGINE_TOKEN = "0" * 64
ENGINE_LOCKED = False
SYSTEM_ACCESS_TOKEN = "0" * 64
DEBUG_BYPASS = False

# License database
VALID_LICENSE_KEYS = [
    "KAZUKI-PREMIUM-2025-AAAAA",
    "KAZUKI-ULTRA-2025-BBBBB",
    "KAZUKI-VIP-LIFETIME-0001",
    "KAZUKI-PRO-MASTER-2025",
    "GODXKAZUKII-PREMIUM-2026",
]

LICENSE_DATABASE = {}
TRIAL_DATABASE = {}


def trigger_hard_crash():
    return False


def background_shield_monitor():
    pass


def kill_hacker():
    return False


def security_guard(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def show_premium_unpack_dashboard(pak_name, unpack_root, ext_counts, enc_methods, comp_methods, version, total_uncompressed, time_taken, enc_breakdown=None):
    # 1. File Types Table
    table_types = Table(title="Asset Distribution", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
    table_types.add_column("Type", style="bold white")
    table_types.add_column("Count", style=f"bold {DC_HIGHLIGHT}", justify="right")

    total = 0
    for ext, count in sorted(ext_counts.items(), key=lambda x: x[1], reverse=True):
        table_types.add_row(ext, str(count))
        total += count

    # 2. Metadata Table
    table_meta = Table(title="PAK Metadata", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
    table_meta.add_column("Property", style="bold white")
    table_meta.add_column("Value", style=f"bold {DC_HIGHLIGHT}")
    table_meta.add_row("Encryption", ", ".join(enc_methods) or "NONE")
    table_meta.add_row("Compression", ", ".join(comp_methods) or "NONE")
    table_meta.add_row("Version", str(version))

    # 3. Stats Table
    table_stats = Table(title="Operation Stats", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
    table_stats.add_column("Metric", style="bold white")
    table_stats.add_column("Value", style=f"bold {DC_GREEN}")
    table_stats.add_row("Uncompressed", human_size(total_uncompressed))
    table_stats.add_row("Time Taken", f"{time_taken:.2f}s")
    table_stats.add_row("Total Files", str(total))

    # Encryption Breakdown Table
    table_enc = Table(title="Encryption Breakdown", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
    table_enc.add_column("Method", style="bold white")
    table_enc.add_column("Count", style=f"bold {DC_ORANGE}", justify="right")
    
    if enc_breakdown:
        for method, count in sorted(enc_breakdown.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                color = DC_GREEN if method == "NONE" else DC_ORANGE
                table_enc.add_row(f"[{color}]{method}[/{color}]", str(count))
    else:
        table_enc.add_row("N/A", "0")

    # Dashboard using grid
    grid = Table.grid(expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_row(table_types, table_meta)
    grid.add_row(table_stats, table_enc)
    grid.add_row(Align.center(Text("\n► OPERATION COMPLETE ◄", style=f"bold {DC_GREEN}"), vertical="middle"))

    dashboard = Group(
        grid,
        Text(""),
        Align.center(Text(f"► TARGET PATH: {unpack_root} ◄", style=f"bold {DC_HIGHLIGHT}"))
    )

    console.print(Panel(
        dashboard,
        title=f"[bold black on {DC_HIGHLIGHT}] KUNALYT0 DASHBOARD [/]",
        border_style=DC_HIGHLIGHT,
        box=HEAVY_EDGE,
        padding=(1, 1),
    ))


def check_password_login():
    """Auto-bypass - no key system."""
    global SERVER_ENGINE_TOKEN, SYSTEM_ACCESS_TOKEN, ENGINE_LOCKED
    global SESSION_USER, SESSION_KEY, SESSION_EXPIRY

    SERVER_ENGINE_TOKEN = "0" * 64
    SYSTEM_ACCESS_TOKEN = "0" * 64
    ENGINE_LOCKED = False
    SESSION_USER = "VIP USER"
    SESSION_KEY = "LOCAL-BYPASS"
    SESSION_EXPIRY = "LIFETIME"
    return "KAZUKI_KEYED"


def run_security_check():
    return True


# =====================================================================
# BANNER
# =====================================================================

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = r"""
    ██╗  ██╗██╗   ██╗███╗   ██╗ █████╗ ██╗     ██╗   ██╗████████╗ ██████╗
    ██║ ██╔╝██║   ██║████╗  ██║██╔══██╗██║     ╚██╗ ██╔╝╚══██╔══╝██╔═████╗
    █████╔╝ ██║   ██║██╔██╗ ██║███████║██║      ╚████╔╝    ██║   ██║██╔██║
    ██╔═██╗ ██║   ██║██║╚██╗██║██╔══██║██║       ╚██╔╝     ██║   ██║╚═╝██║
    ██║  ██╗╚██████╔╝██║ ╚████║██║  ██║███████╗   ██║      ██║   ╚██████╔╝
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝      ╚═╝    ╚═════╝
    """

    banner_panel = Panel(
        Align.center(Text.from_markup(f"[bold {DC_HIGHLIGHT}]{banner}[/]")),
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
        title=f"[bold black on {DC_HIGHLIGHT}] ULTIMATE MODDING SUITE [/]",
        subtitle=f"[bold {DC_TEXT}]V8.0 PRO | {get_indian_time()}[/]"
    )
    console.print(banner_panel)
    console.print()


def print_forensic_dashboard(stats, output_path, title_text="FORENSIC ANALYSIS DASHBOARD", force_safe=False):
    # Size logic
    orig_size = stats['original_size']
    new_size = stats['new_size']
    diff = new_size - orig_size
    diff_str = human_size(abs(diff))
    diff_color = DC_RED if diff > 0 else DC_HIGHLIGHT
    diff_sign = "+" if diff > 0 else "-"

    # Hash logic
    orig_sha = stats['orig_index_sha']
    new_sha = stats['new_index_sha']
    match = (str(orig_sha).lower() == str(new_sha).lower()) or force_safe
    
    # 1. Core Metrics
    table_core = Table.grid(expand=True)
    table_core.add_column(ratio=1)
    table_core.add_column(ratio=1)
    
    # Left: Core sizes
    left_metrics = Table(box=SIMPLE, border_style=DC_BORDER)
    left_metrics.add_column("Core Metric", style="bold white")
    left_metrics.add_column("Value", style=f"bold {DC_HIGHLIGHT}")
    left_metrics.add_row("Total Files", str(stats['files_processed']))
    left_metrics.add_row("Original Size", human_size(orig_size))
    left_metrics.add_row("New Size", human_size(new_size))
    left_metrics.add_row("Size Delta", f"[{diff_color}]{diff_sign}{diff_str}[/]")
    left_metrics.add_row("CRC Match", "[green]✔ ORIGINAL[/]" if stats.get('force_crc') else "[dim]N/A[/]")

    left_metrics.add_row("Size Match", "[green]✔ EXACT[/]" if int(stats['original_size']) == int(stats['new_size']) else f"[red]! MISMATCH[/]")


    
    # Right: Structural
    right_metrics = Table(box=SIMPLE, border_style=DC_BORDER)
    right_metrics.add_column("Structure", style="bold white")
    right_metrics.add_column("Value", style=f"bold {DC_HIGHLIGHT}")
    right_metrics.add_row("Compressed", str(stats['compressed_count']))
    right_metrics.add_row("Encrypted", str(stats['encrypted_count']))
    right_metrics.add_row("PAK Version", str(stats['version']))
    right_metrics.add_row("Status", "[bold green]STABLE[/]")
    
    table_core.add_row(left_metrics, right_metrics)

    # 2. Deep Hash Security
    hash_table = Table(box=ROUNDED, border_style=DC_BORDER, expand=True, title="[bold white]Deep Hash Security[/]")
    hash_table.add_column("Index Component", style="dim white", width=20)
    hash_table.add_column("SHA1 Fingerprint", style=f"bold {DC_HIGHLIGHT}")
    hash_table.add_row("Original SHA1", str(orig_sha))
    hash_table.add_row("Generated SHA1", str(new_sha))
    
    if match:
        match_status = f"[bold {DC_GREEN}][✔] PERFECT MATCH (100% Safe)[/]"
        meter = f"[bold {DC_GREEN}][■■■■■■■■■■] 100% SAFE[/]"
    else:
        match_status = f"[bold {DC_RED}][!] HASH MISMATCH (Modified)[/]"
        meter = f"[bold {DC_RED}][■■■■□□□□□□] 40% RISK[/]"
    
    warning_text = Text("\nWARNING: Modified PAKs are detectable in online matches. Use only for offline or private servers.", 
                        style="italic dim white", justify="center")

    dashboard = Group(
        table_core,
        hash_table,
        Align.center(Text.from_markup(match_status)),
        Text(""),
        Align.center(Text.from_markup(meter)),
        warning_text,
        Text(""),
        Align.center(Text(f"OUTPUT: {output_path}", style=f"bold {DC_HIGHLIGHT}"))
    )

    console.print(Panel(
        dashboard,
        title=f"[bold black on #FF3366] {title_text} [/]",
        border_style="#FF3366",
        box=HEAVY_EDGE,
    ))


def print_user_profile():
    import os
    from datetime import datetime
    
    key_str = "GUEST MODE"
    expiry_str = "N/A"
    valid_str = "N/A"
    tier_str = "N/A"
    
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                saved_key = f.read().strip()
            
            data = load_licenses()
            info = data.get(saved_key)
            
            if info:
                key_str = saved_key[:15] + "..." if len(saved_key) > 15 else saved_key
                expiry_str = info.get('expires_at', 'Unknown')
                tier_str = info.get('tier', 'Unknown')
                
                try:
                    exp_date = datetime.strptime(expiry_str, "%Y-%m-%d")
                    days_left = (exp_date - datetime.now()).days
                    valid_str = f"{days_left} Days" if days_left >= 0 else "EXPIRED"
                except:
                    valid_str = "Unknown"
        except:
            pass
            
    grid = Table.grid(expand=True)
    grid.add_column(justify="left")
    grid.add_column(justify="right")
    grid.add_row(
        f"[bold {DC_HIGHLIGHT}]Key:[/] [bold {DC_TEXT}]{key_str}[/]",
        f"[bold {DC_HIGHLIGHT}]Tier:[/] [bold {DC_TEXT}]{tier_str}[/]"
    )
    grid.add_row(
        f"[bold {DC_HIGHLIGHT}]Expiry:[/] [bold {DC_TEXT}]{expiry_str}[/]",
        f"[bold {DC_HIGHLIGHT}]Valid:[/] [bold {DC_TEXT}]{valid_str}[/]"
    )
    console.print(Panel(
        grid,
        title=f"[bold black on {DC_HIGHLIGHT}] VIP ACCOUNT INFO [/]",
        border_style=DC_BORDER,
        box=HEAVY_EDGE,
        padding=(0, 1)
    ))


# =====================================================================
# AUTO MAKING MODS
# =====================================================================

# Exact file requirements for each mod
MOD_FILE_REQUIREMENTS = {
    "1": {"name": "AimBot",       "files": ["bp_shootweaponbase.uexp"]},
    "2": {"name": "Small Cross",  "files": ["bp_shootweaponbase.uexp"]},
    "3": {"name": "Less Recoil",  "files": ["bp_playerpawn.uexp", "bp_playerpawn.uasset", "c_recoil_"]},
    "4": {"name": "Fast Switch",  "files": ["bp_shootweaponbase.uexp"]},
    "5": {"name": "Magic Bullet", "files": ["ch_base_sk_physicsasset.uexp", "ch_base_sk_physicsasset.uasset"]},
    "6": {"name": "Headshot",     "files": ["bp_playerpawn.uasset", "bp_playerpawn.uexp"]},
    "7": {"name": "iPad Scope",   "files": ["bp_playerpawn.uexp", "bp_shootweapondata.uexp"]},
    "8": {"name": "Big Character","files": ["bp_playerpawn.uasset", "bp_playerpawn.uexp"]},
    "9": {"name": "Walk Speed",   "files": ["bp_playerpawn.uexp"]},
    "10": {"name": "Antenna",     "files": ["bp_playerpawn.uasset", "bp_playerpawn.uexp"]},
}

def auto_patch_float_by_context(file_path, target_string, offset_from_string, new_value, float_size=4):
    """
    Finds a string (e.g., b'RangeRate') in the file, then applies an offset to find the float value, and replaces it.
    """
    import struct
    try:
        data = bytearray(open(file_path, "rb").read())
        target_bytes = target_string.encode('utf-8')
        
        # Find all occurrences of the string
        indices = []
        start = 0
        while True:
            idx = data.find(target_bytes, start)
            if idx == -1: break
            indices.append(idx)
            start = idx + 1
            
        if not indices:
            console.print(f"[red]❌ Context String '{target_string}' not found in file![/]")
            return False
            
        console.print(f"[cyan]🔍 Found '{target_string}' at {len(indices)} location(s)[/]")
        
        patched_count = 0
        for idx in indices:
            # Calculate float position based on offset
            float_pos = idx + offset_from_string
            if 0 <= float_pos <= len(data) - float_size:
                # Read the original float
                old_bytes = data[float_pos:float_pos+float_size]
                old_val = struct.unpack("<f", old_bytes)[0]
                
                # Replace with new float
                new_bytes = struct.pack("<f", new_value)
                data[float_pos:float_pos+float_size] = new_bytes
                console.print(f"  [dim]Replaced float at 0x{float_pos:X}: {old_val:.3f} -> {new_value:.3f}[/]")
                patched_count += 1
                
        if patched_count > 0:
            open(file_path, "wb").write(data)
            console.print(f"[bold green]✅ Contextual patch applied ({patched_count} changes)![/]")
            return True
        else:
            console.print("[yellow]⚠ String found but no valid offset for float![/]")
            return False
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")
        return False

def auto_aim_menu(file_path, preset=None):
    import struct
    try:
        if preset:
            speed = preset.get("speed", 2.5)
            r_range = preset.get("range", 100.0)
            r_speed = preset.get("speed_rate", 60.0)
        else:
            speed = float(safe_input("Speed value (e.g., 0.5): "))
            r_range = float(safe_input("RangeRate (e.g., 100.0): "))
            r_speed = float(safe_input("SpeedRate (e.g., 50.0): "))

        success = False
        aim_contexts = [
            ("RangeRate", 8, r_range), ("SpeedRate", 8, r_speed),
            ("RangeRateSight", 8, r_range), ("SpeedRateSight", 8, r_speed),
            ("CrouchRate", 8, 0.5), ("ProneRate", 8, 0.1)
        ]
        
        for s_name, offset, val in aim_contexts:
            if auto_patch_float_by_context(file_path, s_name, offset, val):
                success = True
                
        if not success:
            console.print("[yellow]⚠ Strings not found. Trying blind search...[/]")
            content = open(file_path, "rb").read()
            changes = 0
            for val in [3.5, 2.5, 3.6, 2.6]:
                anchor = struct.pack("<f", val)
                if anchor in content:
                    content = content.replace(anchor, struct.pack("<f", speed))
                    changes += 1
            if changes > 0:
                open(file_path, "wb").write(content)
                console.print(f"[bold green]✅ AimBot: {changes} value(s) replaced[/]")
                success = True
            else:
                console.print("[bold red]❌ No changes made! Wrong file type?[/]")
                console.print("[dim]💡 AimBot needs BP_ShootWeaponBase.uexp, not .uasset files[/]")
                return
        
        if success:
            console.print("[bold green]✅ AimBot Modification Done![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_small_cross(file_path, preset=None):
    import struct
    try:
        if preset:
            new_val = preset.get("cross", 0.5)
        else:
            new_val = float(safe_input("Crosshair Value (under 1.0): "))
            
        success = False
        # Contextual try
        for string_name, offset in [("Crosshair", 8), ("CrosshairSize", 8), ("WeaponCrosshair", 12)]:
            if auto_patch_float_by_context(file_path, string_name, offset, new_val):
                success = True
                break
        
        if not success:
            console.print("[yellow]⚠ Falling back to blind search...[/]")
            content = open(file_path, "rb").read()
            for val in [3.36, 1.09375, 3.37, 1.10, 3.35, 1.09]:
                b = struct.pack("<f", val)
                content = content.replace(b, struct.pack("<f", new_val))
            open(file_path, "wb").write(content)
            console.print("[bold green]✅ Crosshair Patch Done (Fallback)![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_less_recoil(file_path, preset=None):
    import struct
    try:
        if preset:
            new_val = preset.get("recoil", 0.4)
        else:
            new_val = float(safe_input("Recoil Value (under 1.0): "))
            
        console.print(f"[cyan]🔄 Attempting Contextual Search for Recoil...[/]")
        
        # Try Contextual Search (String ke paas wali float)
        contexts = [
            ("WeaponRecoil", 8), ("Recoil", 8), ("Recoil", 12), 
            ("BodyDuability", 20), ("WeaponRecoil", 16)
        ]
        
        success = False
        for string_name, offset in contexts:
            if auto_patch_float_by_context(file_path, string_name, offset, new_val):
                success = True
                break
                
        if not success:
            # FALLBACK: Old blind search if strings are stripped
            console.print("[yellow]⚠ Contextual search failed. Trying Fallback blind search...[/]")
            content = open(file_path, "rb").read()
            matches = 0
            # 3.0 aur 0.5 ke beech ki common values jo update mein change hoti hain
            for val in [0.52, 0.65, 0.9, 0.53, 0.66, 0.91, 0.51, 0.64, 0.89]:
                b = struct.pack("<f", val)
                if b in content:
                    content = content.replace(b, struct.pack("<f", new_val))
                    matches += 1
            if matches > 0:
                open(file_path, "wb").write(content)
                console.print("[bold green]✅ Fallback Recoil Patch Done![/]")
            else:
                console.print("[red]❌ Target values not found! File version might be different.[/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_fast_switch(file_path, preset=None):
    import struct
    try:
        if preset:
            new_val = preset.get("switch", 0.5)
        else:
            new_val = float(safe_input("Switch Value (under 1.0): "))
            
        success = False
        for string_name, offset in [("SwitchSpeed", 8), ("WeaponSwitch", 8)]:
            if auto_patch_float_by_context(file_path, string_name, offset, new_val):
                success = True
                break
                
        if not success:
            console.print("[yellow]⚠ Contextual failed. Blind search...[/]")
            content = open(file_path, "rb").read()
            for val in [0.65, 0.7, 0.66, 0.71, 0.64, 0.69]:
                b = struct.pack("<f", val)
                content = content.replace(b, struct.pack("<f", new_val))
            open(file_path, "wb").write(content)
            console.print("[bold green]✅ Fast Switch Done (Fallback)![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_magic_bullet(file_path):
    import struct
    try:
        new_x = float(safe_input("X Value: "))
        new_yz = float(safe_input("Y/Z Value: "))
        target_vals = [(35.0, 33.0, 69.5), (23.0, 25.0, 30.5), (15.0, 30.0, 30.0), (15.0, 30.0, 30.0), (40.0, 33.0, 69.5)]
        
        data = bytearray(open(file_path, "rb").read())
        offset = 0
        for x, y, z in target_vals:
            pos = data.find(struct.pack("<f", x), offset)
            if pos != -1:
                data[pos:pos+4] = struct.pack("<f", new_x)
                offset = pos + 4
                y_pos = data.find(struct.pack("<f", y), offset)
                if y_pos != -1: data[y_pos:y_pos+4] = struct.pack("<f", new_yz)
                z_pos = data.find(struct.pack("<f", z), y_pos + 4)
                if z_pos != -1: data[z_pos:z_pos+4] = struct.pack("<f", new_yz)
        open(file_path, "wb").write(data)
        console.print("[bold green]✅ Magic Bullet Done![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_headshot_uexp(file_path):
    try:
        data = bytearray(open(file_path, "rb").read())
        repl = {
            b"EAvatarDamagePosition::BigBody": b"EAvatarDamagePosition::BigHead",
            b"EAvatarDamagePosition::BigFoot": b"EAvatarDamagePosition::BigHead",
            b"EAvatarDamagePosition::BigHand": b"EAvatarDamagePosition::BigHead",
            b"EAvatarDamagePosition::BigLimbs": b"EAvatarDamagePosition::BigHead",
            b"spine_01": b"spine_03",
            b"spine_02": b"spine_03"
        }
        for t, r in repl.items():
            idx = 0
            while True:
                pos = data.find(t, idx)
                if pos == -1: break
                padded = r + b'\x00' * (len(t) - len(r))
                data[pos:pos+len(t)] = padded
                idx = pos + len(t)
        open(file_path, "wb").write(data)
        console.print("[bold green]✅ Headshot Patch Done![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_ipad_scope(file_path, preset=None):
    import struct
    try:
        if preset:
            new_val = preset.get("scope", 8.0)
        else:
            new_val = float(safe_input("Scope Value (under 20.0): "))
            
        success = False
        for string_name, offset in [("ScopeFOV", 8), ("ADS_FOV", 8), ("ScopeView", 12)]:
            if auto_patch_float_by_context(file_path, string_name, offset, new_val):
                success = True
                break
                
        if not success:
            console.print("[yellow]⚠ Contextual failed. Blind search...[/]")
            data = bytearray(open(file_path, "rb").read())
            target = struct.pack("<f", 5.0)
            indices = []
            start = 0
            while True:
                idx = data.find(target, start)
                if idx == -1: break
                indices.append(idx)
                start = idx + 4
            if len(indices) >= 22:
                pos = indices[21]
                data[pos:pos+4] = struct.pack("<f", new_val)
                open(file_path, "wb").write(data)
                console.print("[bold green]✅ iPad Scope Modified (Fallback)![/]")
            else:
                console.print("[red]❌ Target values not found![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_big_character(file_path, preset=None):
    import struct
    try:
        console.print("[cyan]🔄 Attempting Big Character Modification...[/]")
        data = bytearray(open(file_path, "rb").read())
        
        search_string = b"BodyDuability"
        idx = data.find(search_string)
        if idx == -1:
            console.print("[red]❌ 'BodyDuability' string not found in file![/]")
            return
            
        hex_to_find = b"\xcd\xcc"
        indices = []
        start = 0
        while True:
            pos = data.find(hex_to_find, start)
            if pos == -1: break
            indices.append(pos)
            start = pos + 1
            
        if len(indices) >= 17:
            target_idx = indices[16]
            extract_pos = target_idx - 49
            extracted_bytes = data[extract_pos:extract_pos+2] if extract_pos >= 0 else b'\x00\x00'
        else:
            extracted_bytes = b'\x00\x00'

        float_target = struct.pack('<f', -88.0)
        float_indices = []
        start = 0
        while True:
            pos = data.find(float_target, start)
            if pos == -1: break
            float_indices.append(pos)
            start = pos + 1

        if not float_indices:
            console.print("[red]❌ Target value (-88.0) not found![/]")
            return

        for pos in float_indices:
            data[pos - 8:pos - 6] = extracted_bytes
            data[pos - 4:pos - 2] = extracted_bytes

        if preset:
            user_val = preset.get("big_char", 2.0)
        else:
            user_val = float(safe_input("Character Size Value (0.0 to 3.0, e.g., 2.5): "))

        user_bytes = struct.pack('<f', user_val)

        for pos in float_indices:
            data[pos:pos+4] = user_bytes
            data[pos-4:pos] = user_bytes
            data[pos-8:pos-4] = user_bytes

        open(file_path, "wb").write(data)
        console.print("[bold green]✅ Big Character Patch Done![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_walk_speed(file_path, preset=None):
    import struct
    try:
        if preset:
            new_val = preset.get("walk_speed", 600.0)
        else:
            new_val = float(safe_input("Walk Speed (default 600.0): "))
            
        success = False
        if auto_patch_float_by_context(file_path, "MaxWalkSpeed", 12, new_val):
            success = True
            
        if not success:
            console.print("[yellow]⚠ Context failed. Trying blind search...[/]")
            content = open(file_path, "rb").read()
            for val in [600.0, 400.0, 300.0]:
                b = struct.pack("<f", val)
                if b in content:
                    content = content.replace(b, struct.pack("<f", new_val))
                    success = True
            if success:
                open(file_path, "wb").write(content)
        
        if success:
            console.print(f"[bold green]✅ Walk Speed set to {new_val}![/]")
        else:
            console.print("[red]❌ Target not found![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_antenna(file_path, preset=None):
    import struct
    try:
        console.print("[cyan]🔄 Applying Antenna Patch...[/]")
        data = bytearray(open(file_path, "rb").read())
        
        pattern = b"\x00\x00\x80\x3f" # 1.0 float
        repl = b"\x00\x00\x00\x40" # 2.0 float
        
        data = data.replace(pattern, repl)
        
        open(file_path, "wb").write(data)
        console.print("[bold green]✅ Antenna Patch Done![/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def auto_extract_mod_files(data_path):
    from rich.panel import Panel
    from rich.table import Table
    from rich import box as _box
    import zipfile
    import tempfile
    import shutil

    console.clear()
    print_banner()
    console.print(Panel(
        "[bold #00FFCC]📦 AUTO-EXTRACT MOD FILES[/]\n"
        "[dim]Select a PAK/OBB file. OBB files are auto-unzipped.[/]",
        border_style="#00FFCC", box=DOUBLE_EDGE
    ))

    # 1. Required files
    required_files = set()
    for req in MOD_FILE_REQUIREMENTS.values():
        for f in req["files"]:
            if "*" not in f:
                required_files.add(f.lower())

    # 2. Search ALL possible source folders (with deduplication)
    source_dirs = [
        data_path / "PAK",
        data_path / "OBB_UNPACKER" / "ORGNAL",
        data_path / "OBB_UNPACKER" / "PAKS",
        data_path / "PAK TOOL" / "PAK",
    ]

    pak_files = []
    seen_paths = set()
    for sd in source_dirs:
        if sd.exists():
            for f in list(sd.glob("*.pak")) + list(sd.glob("*.obb")):
                real_path = f.resolve()
                if real_path not in seen_paths:
                    seen_paths.add(real_path)
                    pak_files.append(f)

    if not pak_files:
        console.print(f"[bold #FF3366]❌ No .pak or .obb found in any source folder![/]")
        safe_input("\nPress Enter...")
        return

    # Show PAK files
    sel_table = Table(box=ROUNDED, border_style="cyan")
    sel_table.add_column("#", justify="center", style="bold #00FFCC", width=4)
    sel_table.add_column("PAK / OBB File", style="bold white")
    sel_table.add_column("TYPE", justify="center", style="bold #FFAA00", width=6)
    sel_table.add_column("SOURCE FOLDER", style="#7A7A9A", justify="right")
    for i, f in enumerate(pak_files, 1):
        ftype = "OBB" if f.suffix.lower() == ".obb" else "PAK"
        sel_table.add_row(str(i), f.name, ftype, f.parent.name)
    console.print(sel_table)

    choice = safe_input("\n[bold #FFAA00]► Select File to Extract (0=Back): [/]").strip()
    if choice == "0" or not choice.isdigit(): return

    try:
        target_file = pak_files[int(choice) - 1]
    except:
        return

    input_dir = data_path / "AUTO_MODS" / "INPUT"
    input_dir.mkdir(parents=True, exist_ok=True)
    
    extracted_count = 0
    found_files = []
    extracted_set = set()

    def _extract_from_pak(pak_path):
        """Extract required files from a single PAK"""
        nonlocal extracted_count
        try:
            pak = TencentPakFile(pak_path)
            for dir_path, files in pak._index.items():
                for fname, entry in files.items():
                    if fname.lower() in required_files:
                        dest = input_dir / fname
                        try:
                            pak._write_to_disk(dest, entry)
                            extracted_count += 1
                            found_files.append(fname)
                            extracted_set.add(fname.lower())
                        except Exception:
                            pass
            return True
        except Exception as e:
            console.print(f"[yellow]⚠ Could not open {pak_path.name}: {e}[/]")
            return False

    # 3. Handle OBB vs PAK
    if target_file.suffix.lower() == ".obb":
        console.print(f"\n[bold #00FFCC]📦 OBB detected. Unzipping {target_file.name}...[/]")
        temp_dir = tempfile.mkdtemp(prefix="obb_extract_")
        try:
            with zipfile.ZipFile(target_file, 'r') as zf:
                pak_entries = [n for n in zf.namelist() if n.lower().endswith('.pak')]
                if not pak_entries:
                    console.print("[bold #FF3366]❌ No .pak files found inside OBB![/]")
                    return
                
                console.print(f"[cyan]Found {len(pak_entries)} PAK(s) inside OBB[/]")
                
                with console.status("[bold #00FFCC]Extracting PAKs from OBB...[/]", spinner="dots"):
                    zf.extractall(temp_dir)
                
                # Now scan each PAK inside
                console.print(f"\n[bold #00FFCC]🔍 Scanning {len(pak_entries)} PAK(s) for mod files...[/]")
                with console.status("[bold #00FFCC]Searching required files...[/]", spinner="dots"):
                    for pak_entry in pak_entries:
                        pak_path = Path(temp_dir) / pak_entry
                        if pak_path.exists():
                            _extract_from_pak(pak_path)
        except zipfile.BadZipFile:
            console.print(f"[bold #FF3366]❌ Invalid OBB file (not a valid ZIP)![/]")
            safe_input("\nPress Enter...")
            return
        except Exception as e:
            console.print(f"[bold #FF3366]❌ OBB error: {e}[/]")
            safe_input("\nPress Enter...")
            return
        finally:
            # Cleanup temp
            try:
                shutil.rmtree(temp_dir)
            except:
                pass
    else:
        # Direct PAK
        console.print(f"\n[bold #00FFCC]🔍 Scanning {target_file.name} for mod files...[/]")
        with console.status("[bold #00FFCC]Extracting...[/]", spinner="dots"):
            _extract_from_pak(target_file)

    # 4. Show results
    if extracted_count > 0:
        files_str = "\n".join([f"  [dim]✓ {f}[/]" for f in found_files[:10]])
        if len(found_files) > 10:
            files_str += "\n  [dim]...and " + str(len(found_files) - 10) + " more[/]"
        
        console.print(Panel(
            f"[bold #00FF00]✅ EXTRACTED {extracted_count} FILES![/]\n\n"
            f"{files_str}\n\n"
            f"[bold #00FFCC]📂 Location:[/] {input_dir}",
            border_style="#00FF00", box=DOUBLE_EDGE, padding=(1, 2)
        ))
        
        missing = required_files - extracted_set
        if missing:
            missing_str = "\n".join([f"  [bold #FFAA00]•[/] {m}" for m in sorted(missing)[:15]])
            console.print(Panel(
                f"[bold #FFAA00]⚠️ STILL MISSING {len(missing)} FILES:[/]\n\n"
                f"{missing_str}\n\n"
                f"[dim]💡 Try extracting from a different PAK/OBB.[/]",
                border_style="#FFAA00", box=ROUNDED, padding=(1, 2)
            ))
        else:
            console.print(Panel(
                "[bold #00FF00]🎉 ALL REQUIRED FILES EXTRACTED![/]\n"
                "[dim]Ready to apply any mod.[/]",
                border_style="#00FF00", box=ROUNDED
            ))
    else:
        console.print(Panel(
            "[bold #FF3366]❌ Required files not found![/]\n"
            "[dim]Try a different PAK/OBB file.[/]",
            border_style="#FF3366", box=ROUNDED
        ))

    safe_input("\n[bold #FFAA00]Press Enter to continue...[/]")


def handle_auto_making_mods(data_path):
    from rich.align import Align
    from rich.text import Text
    from rich.panel import Panel
    from rich.table import Table
    from rich import box as _box
    import os
    
    input_dir = data_path / "AUTO_MODS" / "INPUT"
    output_dir = data_path / "AUTO_MODS" / "OUTPUT"
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    while True:
        console.clear()
        print_banner()
        
        # ═══════════════════ PREMIUM HEADER ═══════════════════
        console.print(Panel(
            Align.center(Text.from_markup(
                f"[bold #00FFCC]╔══════════════════════════════════════════════════════════════╗\n"
                f"║      ⚙️   A U T O   M A K I N G   M O D S   ⚙️      ║\n"
                f"╚══════════════════════════════════════════════════════════════╝[/]\n"
                f"[dim #FFAA00]Direct UEXP/UASSET Binary Patcher | Update-Proof Edition[/]"
            )),
            border_style="#FFAA00", box=DOUBLE_EDGE, padding=(0, 1)
        ))

        # Action Menu
        # Check how many files are ready
        ready_files_count = len([f for f in input_dir.iterdir() if f.is_file()])

        # Premium Header
        console.print(Panel(
            Align.center(Text.from_markup(
                f"[bold #00FFCC]⚡  A U T O   M O D   E N G I N E  ⚡[/]\n"
                f"[dim #FFAA00]Select your operation below[/]"
            )),
            border_style="#00FFCC", box=DOUBLE_EDGE, padding=(0, 1)
        ))

        # Status Bar
        console.print(Panel(
            f"[bold #FFAA00]📂 Files in INPUT:[/] [bold white]{ready_files_count}[/]    "
            f"[bold #FFAA00]📁 Output:[/] [dim]{output_dir.name}[/]",
            border_style="#3A3A5A", box=ROUNDED, padding=(0, 1)
        ))

        action_table = Table(show_header=True, box=HEAVY_EDGE, border_style="#00FFCC", expand=True, header_style="bold black on #00FFCC")
        action_table.add_column("OPT", justify="center", style="bold #FFAA00", width=4)
        action_table.add_column("ICON", justify="center", width=4)
        action_table.add_column("ACTION", style="bold white", ratio=1)
        action_table.add_column("DESCRIPTION", style="#7A7A9A", ratio=2)

        action_table.add_row("1", "📦", "Auto-Extract Required Files", "Extract mod files from OBB/PAK")
        action_table.add_row("2", "🛠", "Patch Extracted Files", "Apply mods to files in INPUT folder")
        action_table.add_row("0", "❌", "Back", "Return to Main Menu")
        
        console.print(action_table)
        
        main_choice = safe_input("\n[bold #FFAA00]► Select Action: [/]").strip()
        if main_choice == "0": return
        if main_choice == "1":
            auto_extract_mod_files(data_path)
            continue
        if main_choice != "2": continue

        # ═══════════════════ FILE LIST ═══════════════════
        files = [f for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() in ['.uexp', '.uasset']]
        
        if not files:
            console.print(Panel(
                f"[bold #FF3366]❌ No UEXP/UASSET files found in INPUT folder![/]\n"
                f"[dim]Please place your target file in:[/]\n"
                f"[bold #00FFCC]{input_dir}[/]",
                border_style="#FF3366", box=ROUNDED
            ))
            safe_input("\n[bold white]Press Enter to return...[/]")
            return

        file_table = Table(box=HEAVY_EDGE, border_style="#3A3A5A", expand=True, title="[bold black on #00FFCC] 📂 SELECT TARGET FILE [/]")
        file_table.add_column("#", justify="center", style="bold #00FFCC", width=4)
        file_table.add_column("FILE NAME", style="bold white", ratio=1)
        file_table.add_column("SIZE", justify="right", style="#7A7A9A")
        
        for i, f in enumerate(files, 1):
            size_kb = f.stat().st_size / 1024
            file_table.add_row(str(i), f.name, f"{size_kb:.1f} KB")
        
        file_table.add_row("0", "[#FF3366]Back[/]", "-")
        console.print(file_table)

        file_choice = safe_input("\n[bold #FFAA00]► Select File (0=Back): [/]").strip()
        if file_choice == "0" or not file_choice.isdigit(): 
            return
        
        try:
            target_file = files[int(file_choice) - 1]
        except:
            continue

        # Copy to output before modifying
        out_file = output_dir / target_file.name
        shutil.copy2(target_file, out_file)

        # ═══════════════════ MOD SELECTION MENU ═══════════════════
        while True:
            console.clear()
            print_banner()
            
            # Header showing selected file
            console.print(Panel(
                f"[bold #00FFCC]Selected File:[/] [white]{target_file.name}[/]\n"
                f"[dim]Output will be saved to: {output_dir}[/]",
                border_style="#3A3A5A", box=ROUNDED
            ))

            # --- SMART MOD FILTERING ---
            fname_lower = target_file.name.lower()
            compatible_mods = []
            
            # Check which mods are compatible with this file
            for opt, req in MOD_FILE_REQUIREMENTS.items():
                if any(kw in fname_lower for kw in req["files"]):
                    compatible_mods.append(opt)
            
            if not compatible_mods:
                console.print(Panel(
                    f"[bold #FF3366]❌ No mods are compatible with {target_file.name}![/]\n"
                    f"[dim]Try selecting a different file (like BP_PlayerPawn.uexp or BP_ShootWeaponBase.uexp)[/]",
                    border_style="#FF3366", box=ROUNDED
                ))
                safe_input("\n[bold #FFAA00]Press Enter to go back...[/]")
                break
            # ---------------------------

            menu = Table(show_header=True, box=HEAVY_EDGE, border_style="#00FFCC", expand=True, header_style="bold black on #00FFCC")
            menu.add_column("OPT", justify="center", style="bold #FFAA00", width=4)
            menu.add_column("ICON", justify="center", width=4)
            menu.add_column("MOD NAME", style="bold white", ratio=1)
            menu.add_column("DESCRIPTION", style="dim #7A7A9A", ratio=2)
            
            # Sirf compatible mods add karo
            if "1" in compatible_mods: menu.add_row("1", "🎯", "AimBot", "Adjust Range, Speed & Crouch rates")
            if "2" in compatible_mods: menu.add_row("2", "➕", "Small Crosshair", "Reduce crosshair size to 0.5")
            if "3" in compatible_mods: menu.add_row("3", "🔫", "Less Recoil", "Drastically reduce weapon recoil")
            if "4" in compatible_mods: menu.add_row("4", "⚡", "Fast Switch", "Faster weapon switching speed")
            if "5" in compatible_mods: menu.add_row("5", "🔮", "Magic Bullet", "Bullets hit through obstacles")
            if "6" in compatible_mods: menu.add_row("6", "💀", "Headshot (Uexp)", "Force all damage to BigHead")
            if "7" in compatible_mods: menu.add_row("7", "🔭", "iPad Scope View", "Wider Field of View when scoping")
            if "8" in compatible_mods: menu.add_row("8", "🧍", "Big Character", "Increase character body size")
            if "9" in compatible_mods: menu.add_row("9", "🏃", "Walk Speed", "Adjust player walk speed")
            if "10" in compatible_mods: menu.add_row("10", "📡", "Antenna", "Add antenna to player model")
            
            menu.add_row("0", "❌", "Back to File Select", "")
            console.print(menu)

            mod_choice = safe_input("\n[bold #FFAA00]► Select Mod (0=Back): [/]").strip()
            
            if mod_choice == "0":
                break # Go back to file selection
            
            # ═══════════════════ EXECUTION ═══════════════════
            if mod_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                console.print()
                
                # --- SMART FILE VALIDATOR ---
                req = MOD_FILE_REQUIREMENTS.get(mod_choice)
                if req:
                    fname_lower = target_file.name.lower()
                    is_valid = any(kw in fname_lower for kw in req["files"])
                    
                    if not is_valid:
                        console.print(Panel(
                            f"[bold #FFAA00]⚠️ WRONG FILE SELECTED![/]\n\n"
                            f"[white]Mod [bold]{req['name']}[/] requires one of these files:[/]\n"
                            f"[bold #00FFCC]{', '.join(req['files'])}[/]\n\n"
                            f"[white]But you selected:[/] [bold #FF3366]{target_file.name}[/]\n\n"
                            f"[dim]💡 Tip: Place the correct .uexp file in AUTO_MODS/INPUT/[/]",
                            border_style="#FFAA00", box=ROUNDED
                        ))
                        if safe_input("\n[bold #FFAA00]Force apply anyway? (y/n): [/]").strip().lower() != "y":
                            continue # Wapas mod menu pe bhej do
                # -----------------------------

                preset = None  # Default None
                
                if mod_choice == "1": auto_aim_menu(out_file, preset)
                elif mod_choice == "2": auto_small_cross(out_file, preset)
                elif mod_choice == "3": auto_less_recoil(out_file, preset)
                elif mod_choice == "4": auto_fast_switch(out_file, preset)
                elif mod_choice == "5": auto_magic_bullet(out_file)
                elif mod_choice == "6": auto_headshot_uexp(out_file)
                elif mod_choice == "7": auto_ipad_scope(out_file, preset)
                elif mod_choice == "8": auto_big_character(out_file, preset)
                elif mod_choice == "9": auto_walk_speed(out_file, preset)
                elif mod_choice == "10": auto_antenna(out_file, preset)
                
                # ═══════════════════ SUCCESS BADGE ═══════════════════
                console.print(Panel(
                    Align.center(Text.from_markup(
                        f"[bold #00FF00]✨ MOD APPLIED SUCCESSFULLY ✨[/]\n\n"
                        f"[bold white]Target:[/] {out_file.name}\n"
                        f"[bold white]Output:[/] [dim]{output_dir}[/]"
                    )),
                    border_style="#00FF00", box=DOUBLE_EDGE, padding=(1, 4)
                ))
                safe_input("\n[bold #FFAA00]Press Enter to continue...[/]")
            else:
                console.print("[bold #FF3366]Invalid option![/]")
                time.sleep(1)

# =====================================================================
# MAIN MENU
# =====================================================================

def print_main_menu():
    # Header Title
    menu_title = Text()
    menu_title.append("═" * 15, style=f"dim {DC_BORDER}")
    menu_title.append("  K U N A L Y T 0   E N G I N E  ", style=f"bold {DC_HIGHLIGHT}")
    menu_title.append("═" * 15, style=f"dim {DC_BORDER}")

    # Options List
    options = [
        ("1",  "UNPACK PAK",           "Extract all files (S=pause, B=stop)"),
        ("2",  "INJECT / EDIT FILES",  "Multi-file inject with paths"),
        ("3",  "REPACK FULL REBUILD",  "Rebuild with any size files"),
        ("4",  "REPACK TO PATH",       "Add new files to specific path"),
        ("5",  "PROTECT PAK (SM4)",    "Re-encrypt all files with SM4"),
        ("6",  "BUILD NEW PAK (CSV)",  "Build game-ready PAK from CSV paths"),
        ("7",  "DELETE FOLDER",        "Remove extracted folders"),
        ("8",  "MINI SKIN TOOL",       "VIP Mod Skin & Size Fix"),
        ("9",  "ZSDIC SKIN TOOL",      "Advanced Repacking"),
        ("10", "LUA TOOL",             "Lua Decompile / Recompile"),
        ("11", "BLACK TOOL (UE4)",     "UE4 String Editor"),
        ("12", "ANALYZE PAK",        "Deep scan without extraction"),
        ("13", "AUTO-EXTRACT KEYS",  "Scan .so for SM4 keys"),
        ("14", "OBB ALL-IN-ONE",       "Extract -> Unpack -> Repack -> Antireset"),
        ("15", "AUTO MAKING MODS",     "UEXP/UASSET Auto Patcher"),
        ("0",  "EXIT",                 "Close the tool"),
    ]

    menu_content = [Align.center(menu_title), Text("")]

    # Format Options
    for num, label, desc in options:
        row = Text()
        row.append("  ╭─[", style=f"dim {DC_BORDER}")
        row.append(f"{num:>2}", style=f"bold {DC_HIGHLIGHT}")
        row.append("] ", style=f"dim {DC_BORDER}")
        row.append(f"{label:<20}", style=f"bold {DC_TEXT}")
        row.append(" » ", style=f"bold {DC_HIGHLIGHT}")
        row.append(f"{desc}", style=f"dim {DC_DIM}")
        menu_content.append(Align.left(row))

    menu_content.append(Text(""))
    menu_content.append(Align.center(Text("═" * 58, style=f"dim {DC_BORDER}")))

    # Footer Tips
    tip1 = Text()
    tip1.append("  ⚡ Tip: ", style=f"bold {DC_ORANGE}")
    tip1.append("During UNPACK press ", style=f"{DC_DIM}")
    tip1.append("S", style=f"bold {DC_HIGHLIGHT}")
    tip1.append(" to pause, ", style=f"{DC_DIM}")
    tip1.append("B", style=f"bold {DC_RED}")
    tip1.append(" to stop", style=f"{DC_DIM}")
    menu_content.append(Align.left(tip1))

    tip2 = Text()
    tip2.append("  📂 Dir: ", style=f"bold {DC_ORANGE}")
    tip2.append("SKIN_TOOL/ | LUA_TOOL/ | CREDIT_TOOL/ | BUILD_PAK/", style=f"{DC_DIM}")
    menu_content.append(Align.left(tip2))

    menu_content.append(Text(""))
    menu_content.append(Align.center(Text("H A P P Y   M O D D I N G !", style=f"bold {DC_HIGHLIGHT}")))

    # Final Box
    menu_panel = Panel(
        Group(*menu_content),
        title=f"[bold black on {DC_HIGHLIGHT}] KUNALYT0 SYSTEM [/]",
        border_style=DC_HIGHLIGHT,
        box=ROUNDED,
        padding=(1, 3),
        subtitle=f"[bold black on {DC_HIGHLIGHT}] {get_indian_time()} [/]",
    )
    console.print(menu_panel)
    console.print()


# =====================================================================
# DELETE FOLDER
# =====================================================================

def delete_folder(data_path):
    import subprocess
    try:
        folders = []
        for item in data_path.iterdir():
            if item.is_dir() and item.name not in [
                'PAK', 'UNPACK', 'REPACK', 'RESULT', 'PAK TOOL',
                'BUILD_PAK', 'SKIN_TOOL', 'LUA_TOOL', 'CREDIT_TOOL', 'EXES', 'OBB_UNPACKER', 'ANTIRESET_OBB'
            ]:
                folders.append(item)

        if not folders:
            console.print(f'[bold {DC_HIGHLIGHT}]No folders found to delete![/]')
            safe_input('\nPress Enter to continue...')
            return

        folder_table = Table(
            title=f"[bold {DC_HIGHLIGHT}]AVAILABLE FOLDERS[/]",
            border_style=DC_BORDER,
            box=DOUBLE_EDGE,
            header_style=f"bold black on {DC_HIGHLIGHT}",
        )
        folder_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=6)
        folder_table.add_column("Folder Name", justify="left", style=f"bold {DC_TEXT}")
        folder_table.add_column("Status", justify="right", style=f"dim {DC_DIM}")

        # Fast scan - don't calculate size for every folder (too slow)
        for i, folder in enumerate(folders, 1):
            folder_table.add_row(str(i), folder.name, "Ready")

        console.print(folder_table)

        choice_str = safe_input(f"\n[bold {DC_HIGHLIGHT}]Select folder number (1-{len(folders)}) or 0 to cancel: [/]")
        if not choice_str.isdigit():
            return
        choice = int(choice_str)

        if 0 < choice <= len(folders):
            sel = folders[choice - 1]
            confirm = safe_input(f"[bold {DC_RED}]Delete '{sel.name}'? (yes/no): [/]").strip().lower()
            if confirm in ('y', 'yes'):
                console.print(f"[bold {DC_ORANGE}]Deleting {sel.name}... Please wait.[/]")
                
                # Use native rm -rf command for fast deletion on Termux/Android
                result = subprocess.run(["rm", "-rf", str(sel)], capture_output=True, text=True)
                
                if result.returncode == 0:
                    console.print(f'[bold {DC_GREEN}]✅ Deleted: {sel.name}[/]')
                else:
                    console.print(f'[bold {DC_RED}]Failed to delete: {result.stderr}[/]')
            else:
                console.print(f'[{DC_ORANGE}]Cancelled[/]')
        elif choice != 0:
            console.print(f'[{DC_RED}]Invalid selection[/]')
            
    except Exception as e:
        console.print(f"[bold {DC_RED}]Error in delete_folder: {e}[/]")

    safe_input('\nPress Enter to continue...')


# =====================================================================
# FILE SELECTOR
# =====================================================================

def display_file_selector(title, folder_path, file_pattern="*.pak"):
    files = list(folder_path.glob(file_pattern))
    if not files:
        console.print(f"[bold {DC_RED}]ERROR: No {file_pattern} files in {folder_path}[/]")
        return None, None

    selection_table = Table(
        title=f"[bold {DC_HIGHLIGHT}]{title}[/]",
        expand=True,
        box=DOUBLE_EDGE,
        border_style=DC_BORDER,
        header_style=f"bold black on {DC_HIGHLIGHT}",
    )
    selection_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=6)
    selection_table.add_column("File Name", justify="left", style=f"bold {DC_TEXT}")
    selection_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
    selection_table.add_column("Modified", justify="right", style=f"dim {DC_DIM}")

    for i, f in enumerate(files, 1):
        size_mb = f.stat().st_size / (1024 * 1024)
        mod_time = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        selection_table.add_row(
            str(i),
            f.name,
            f"{size_mb:.2f} MB",
            f"[dim {DC_DIM}]{mod_time}[/dim {DC_DIM}]",
        )

    console.print(selection_table)
    try:
        idx = int(console.input(
            f"\n[bold {DC_HIGHLIGHT}]Select file number (1-{len(files)}): [/]"
        )) - 1
        if idx < 0 or idx >= len(files):
            console.print(f"[bold {DC_RED}]Invalid selection[/]")
            return None, None
        return files[idx], files
    except ValueError:
        console.print(f"[bold {DC_RED}]Please enter a valid number[/]")
        return None, None


# =====================================================================
# INJECT EDIT FILES (Option 2)
# =====================================================================

def prepare_lua_for_pak(file_path):
    """Checks syntax (if plain text), compiles, and encrypts a Lua file for BGMI."""
    raw_data = file_path.read_bytes()
    
    if raw_data.startswith(b'\x1bLua'):
        # If it's already T24 (32-bit size_t), return as is (already encrypted)
        if len(raw_data) > 13 and raw_data[13] == 4:
            console.print(f"  [dim]Lua already T24 encrypted: {file_path.name}[/]")
            return raw_data
            
        # If it's standard Lua 5.3 (64-bit), encrypt it to T24
        try:
            encrypted_data = process_lua_file(raw_data, is_encrypt=True)
            return encrypted_data
        except Exception as e:
            console.print(f"[bold {DC_RED}]✗ Lua encryption failed for {file_path.name}: {e}[/]")
            return None
            
    # Plain text .lua handling
    luac_path = shutil.which(LUAC_CMD)
    if not luac_path:
        console.print(f"[{DC_ORANGE}]⚠ {LUAC_CMD} not found. Cannot compile {file_path.name}. Injecting as raw text.[/]")
        return raw_data
        
    # Syntax Check
    res = subprocess.run([luac_path, "-p", str(file_path)], capture_output=True, text=True)
    if res.returncode != 0:
        console.print(f"[bold {DC_RED}]✗ LUA SYNTAX ERROR in {file_path.name}:[/]")
        console.print(f"[bold {DC_ORANGE}]Raw stderr:[/]")
        console.print(f"[dim]{res.stderr.strip()}[/]")
        console.print(f"[bold {DC_ORANGE}]Raw stdout:[/]")
        console.print(f"[dim]{res.stdout.strip()}[/]")
        return None
        
    # Compile & Encrypt
    temp_out = file_path.parent / f"{file_path.stem}_temp.luac"
    try:
        subprocess.run([luac_path, "-o", str(temp_out), str(file_path)], check=True, capture_output=True)
        std_data = temp_out.read_bytes()
        encrypted_data = process_lua_file(std_data, is_encrypt=True)
        return encrypted_data
    except Exception as e:
        console.print(f"[bold {DC_RED}]✗ Compilation/Encryption failed for {file_path.name}: {e}[/]")
        return None
    finally:
        if temp_out.exists():
            temp_out.unlink()


def inject_edit_files(pak_file, edit_root, output_path, protect_new=False, sm4_type=47):
    import copy as _cp
    version = pak_file._pak_info.version
    file_logs = []

    edit_files = [p for p in Path(edit_root).rglob('*') if p.is_file()]
    if not edit_files:
        raise ValueError(f'No files found in EDIT folder: {edit_root}')

    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)

    injections = {}
    for p in edit_files:
        rel = p.relative_to(edit_root)
        parts = rel.parts
        file_name = parts[-1]
        rel_dir = '/'.join(parts[:-1]).replace('\\', '/')

        target_dir = _find_existing_dir(all_dirs, rel_dir) if rel_dir.strip('/') else ''
        if target_dir is None:
            target_dir = _normalize_dir_key(rel_dir)

        existing = None
        if target_dir in all_dirs:
            for name, e in list(all_dirs[target_dir].items()):
                if name.lower() == file_name.lower():
                    existing = (name, e)
                    break

        if existing:
            full_path = target_dir + existing[0]
            injections[full_path] = (p, existing[1], False)
        else:
            full_path = target_dir + file_name
            template = _pick_template(pak_file, all_dirs, target_dir, file_name)
            injections[full_path] = (p, template, True)

        console.print(f'  [bold {DC_HIGHLIGHT}]>>[/] [white]{full_path}[/white]')

    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}

    out_buf = bytearray()
    edited_count = 0
    new_count = 0

    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne

            if full_path in injections:
                p, template, is_new = injections[full_path]
                
                # Automatically process Lua files
                if p.suffix.lower() == '.lua':
                    new_raw = prepare_lua_for_pak(p)
                    if new_raw is None: continue # Skip if syntax error
                else:
                    new_raw = p.read_bytes()
                
                pak_rel = PurePath(full_path)

                fresh = _cp.copy(old_entry) if not is_new else (_cp.copy(template) if template else None)

                if fresh is None:
                    fresh = TencentPakEntry.__new__(TencentPakEntry)
                    fresh.content_hash = b'\x00' * 20
                    fresh.offset = 0
                    fresh.uncompressed_size = 0
                    fresh.compression_method = CM_NONE
                    fresh.size = 0
                    fresh.unk1 = 0
                    fresh.unk2 = b'\x00' * 20
                    fresh.compressed_blocks = []
                    fresh.compression_block_size = 0
                    fresh.encrypted = False
                    fresh.encryption_method = 0
                    fresh.index_new_sep = 0

                fresh.compressed_blocks = []
                if protect_new and is_new:
                    fresh.encryption_method = sm4_type
                    fresh.encrypted = True

                _write_entry_into_buf(out_buf, fresh, new_raw, pak_rel, fresh, pak_file._zstd_dict)
                fresh.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()

                if is_new:
                    new_files.append(fresh)
                    dp_key = full_path.rsplit('/', 1)[0] + '/' if '/' in full_path else ''
                    all_dirs.setdefault(dp_key, {})[full_path.rsplit('/', 1)[-1]] = fresh
                    new_count += 1
                else:
                    for i, e in enumerate(new_files):
                        if id(e) == id(old_to_new[id(old_entry)]):
                            new_files[i] = fresh
                            old_to_new[id(old_entry)] = fresh
                            break
                    edited_count += 1

                # Determine encryption and compression type
                enc_type = "NONE"
                if fresh.encrypted:
                    if p.suffix.lower() == '.lua':
                        enc_type = "T24 (Lua BGMI)"
                    else:
                        enc_type = f"SM4 (Type {fresh.encryption_method})"
                
                comp_type = "ZSTD" if fresh.compression_method != 0 else "NONE"

                file_logs.append({
                    "name": full_path,
                    "action": "🔄 EDITED" if not is_new else "🆕 ADDED",
                    "encryption": enc_type,
                    "compression": comp_type,
                    "size": len(new_raw)
                })

                console.print(f'  [bold {DC_HIGHLIGHT}]OK:[/] {full_path}')
            else:
                _copy_original_content(out_buf, pak_file, ne, old_entry)

    # ============ PROCESS NEW FILES (not in original PAK) ============
    for full_path, (p, template, is_new) in injections.items():
        already_processed = False
        for dp_str, dir_files in all_dirs.items():
            for name in dir_files.keys():
                if str(PurePath(dp_str) / name).replace('\\', '/') == full_path:
                    already_processed = True
                    break
            if already_processed:
                break
                
        if not already_processed:
            # Prepare the file content
            if p.suffix.lower() == '.lua':
                new_raw = prepare_lua_for_pak(p)
                if new_raw is None:
                    console.print(f'  [bold {DC_RED}]✗ Skipped (Lua error): {full_path}[/]')
                    continue
            else:
                new_raw = p.read_bytes()

            pak_rel = PurePath(full_path)
            
            # Create a fresh entry
            fresh = _cp.copy(template) if template else None
            if fresh is None:
                fresh = TencentPakEntry.__new__(TencentPakEntry)
                fresh.content_hash = b'\x00' * 20
                fresh.offset = 0
                fresh.uncompressed_size = 0
                fresh.compression_method = CM_NONE
                fresh.size = 0
                fresh.unk1 = 0
                fresh.unk2 = b'\x00' * 20
                fresh.compressed_blocks = []
                fresh.compression_block_size = 0
                fresh.encrypted = False
                fresh.encryption_method = 0
                fresh.index_new_sep = 0

            fresh.compressed_blocks = []
            if protect_new and is_new:
                fresh.encryption_method = sm4_type
                fresh.encrypted = True

            _write_entry_into_buf(out_buf, fresh, new_raw, pak_rel, fresh, pak_file._zstd_dict)
            fresh.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()

            new_files.append(fresh)
            
            # Add to all_dirs so it appears in the index
            if '/' in full_path:
                dp_key = full_path.rsplit('/', 1)[0] + '/'
                fname = full_path.rsplit('/', 1)[1]
            else:
                dp_key = ''
                fname = full_path
            all_dirs.setdefault(dp_key, {})[fname] = fresh
            
            
            # Determine encryption and compression type
            enc_type = "NONE"
            if fresh.encrypted:
                if p.suffix.lower() == '.lua':
                    enc_type = "T24 (Lua BGMI)"
                else:
                    enc_type = f"SM4 (Type {fresh.encryption_method})"
            
            comp_type = "ZSTD" if fresh.compression_method != 0 else "NONE"

            file_logs.append({
                "name": full_path,
                "action": "🔄 EDITED" if not is_new else "🆕 ADDED",
                "encryption": enc_type,
                "compression": comp_type,
                "size": len(new_raw)
            })

            new_count += 1
            console.print(f'  [bold {DC_HIGHLIGHT}]✅ Added NEW:[/] {full_path}')
    # ============ END NEW FILES LOGIC ============

    _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path)

    # Read actual SHA1 from the written PAK file
    new_sha1_val = "N/A"
    try:
        with open(to_long_path(output_path), 'rb') as _f:
            _f.seek(0, 2)
            _fsize = _f.tell()
            _footer_sz = TencentPakInfo._mem_size(version)
            _f.seek(_fsize - _footer_sz)
            _footer_bytes = _f.read(_footer_sz)
            # index_hash is at offset -36 to -16 (encrypted with keystream)
            keystream = PakCrypto.zuc_keystream()
            h_key = struct.pack('<5I', *keystream[4:9])
            _hashed = bytes(a ^ b for a, b in zip(_footer_bytes[-36:-16], h_key))
            new_sha1_val = _hashed.hex()
    except Exception as _e:
        new_sha1_val = f"Error: {_e}"

    # Generate stats for forensic dashboard
    stats = {
        "files_processed": len(new_files),
        "compressed_count": sum(1 for e in new_files if e.compression_method != 0),
        "encrypted_count": sum(1 for e in new_files if e.encrypted),
        "original_size": len(pak_file._file_content),
        "new_size": len(out_buf),
        "orig_index_sha": pak_file._pak_info.index_hash.hex() if hasattr(pak_file._pak_info.index_hash, 'hex') else str(pak_file._pak_info.index_hash),
        "new_index_sha": new_sha1_val,
        "version": version,
        "force_crc": False,
        "size_match": False,
        "edited": edited_count,
        "added": new_count,
        "file_logs": file_logs
    }
    return edited_count, new_count, stats


# =====================================================================
# PROTECT PAK FILE (Option 5)
# =====================================================================

def protect_pak_file(pak_file, output_path, sm4_type=47):
    import copy as _cp
    version = pak_file._pak_info.version
    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)

    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}

    out_buf = bytearray()
    protected = 0
    skipped = 0

    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne

            is_marker = (old_entry.compression_method == CM_NONE and old_entry.size == 0)
            is_zdict = (pak_file._zstd_dict_entry is not None and old_entry is pak_file._zstd_dict_entry)

            if is_marker or is_zdict:
                _copy_original_content(out_buf, pak_file, ne, old_entry)
                skipped += 1
                continue

            try:
                plaintext = _extract_entry_plaintext(pak_file, old_entry, full_path)
            except Exception:
                _copy_original_content(out_buf, pak_file, ne, old_entry)
                skipped += 1
                console.print(f"  [bold {DC_RED}]![/] Skipped: {full_path}")
                continue

            fresh = _cp.copy(old_entry)
            fresh.compressed_blocks = []
            fresh.encryption_method = sm4_type
            fresh.encrypted = True
            if fresh.compression_method == CM_NONE:
                fresh.compression_method = CM_ZLIB

            _write_entry_into_buf(out_buf, fresh, plaintext, PurePath(full_path), fresh, pak_file._zstd_dict)

            for i, e in enumerate(new_files):
                if id(e) == id(old_to_new[id(old_entry)]):
                    new_files[i] = fresh
                    old_to_new[id(old_entry)] = fresh
                    break

            protected += 1
            if protected <= 12 or protected % 250 == 0:
                console.print(f'  [bold {DC_HIGHLIGHT}]LOCKED:[/] {full_path}')

    _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path)

    # Read actual SHA1 from the written PAK file
    new_sha1_val = "N/A"
    try:
        with open(to_long_path(output_path), 'rb') as _f:
            _f.seek(0, 2)
            _fsize = _f.tell()
            _footer_sz = TencentPakInfo._mem_size(version)
            _f.seek(_fsize - _footer_sz)
            _footer_bytes = _f.read(_footer_sz)
            keystream = PakCrypto.zuc_keystream()
            h_key = struct.pack('<5I', *keystream[4:9])
            _hashed = bytes(a ^ b for a, b in zip(_footer_bytes[-36:-16], h_key))
            new_sha1_val = _hashed.hex()
    except Exception as _e:
        new_sha1_val = f"Error: {_e}"

    stats = {
        "files_processed": len(new_files),
        "compressed_count": sum(1 for e in new_files if e.compression_method != 0),
        "encrypted_count": sum(1 for e in new_files if e.encrypted),
        "original_size": len(pak_file._file_content),
        "new_size": len(out_buf),
        "orig_index_sha": pak_file._pak_info.index_hash.hex() if hasattr(pak_file._pak_info.index_hash, 'hex') else str(pak_file._pak_info.index_hash),
        "new_index_sha": new_sha1_val,
        "version": version,
        "force_crc": False,
        "size_match": False,
        "protected": protected,
        "skipped": skipped
    }
    return protected, skipped, stats


# =====================================================================
# HELPER DIRS
# =====================================================================

def _normalize_dir_key(path_str):
    s = str(path_str).replace('\\', '/').strip('/')
    return (s + '/') if s else ''


def _find_existing_dir(all_dirs, want_dir):
    want = _normalize_dir_key(want_dir).strip('/').lower()
    if not want:
        return ''
    for k in all_dirs:
        if k.strip('/').lower() == want:
            return k
    best = None
    for k in all_dirs:
        key = k.strip('/').lower()
        if key and want.endswith('/' + key):
            if best is None or len(key) > len(best):
                best = k
    return best


def _pick_template(pak_file, all_dirs, target_dir, file_name):
    ext = Path(file_name).suffix.lower()
    if target_dir in all_dirs:
        for name, e in all_dirs[target_dir].items():
            if Path(name).suffix.lower() == ext:
                return e
    for dp, files in all_dirs.items():
        for name, e in files.items():
            if Path(name).suffix.lower() == ext:
                return e
    for dp, files in all_dirs.items():
        for name, e in files.items():
            return e
    return pak_file._files[0] if pak_file._files else None


# =====================================================================
# UNPACK LOG
# =====================================================================

def dump_unpacking_log(pak_file, output_log_path):
    try:
        with open(output_log_path, 'w', encoding='utf-8') as log_file:
            log_file.write('=' * 80 + '\nPAK UNPACKING DEBUG LOG\n' + '=' * 80 + '\n\n')
            log_file.write(f'PAK File: {pak_file._file_path}\n')
            log_file.write(f'PAK Info Version: {pak_file._pak_info.version}\n')
            log_file.write(f'Mount Point: {pak_file._mount_point}\n')
            log_file.write('-' * 80 + '\n\n')
            file_count = 0
            for dir_path, files in pak_file._index.items():
                for file_name, entry in files.items():
                    file_count += 1
                    full_path = str(PurePath(dir_path) / file_name).replace('\\', '/')
                    log_file.write(f'\n[{file_count}] {full_path}\n')
                    log_file.write(f'  Uncompressed Size: {entry.uncompressed_size:,} bytes\n')
                    log_file.write(f'  Compressed Size: {entry.size:,} bytes\n')
                    log_file.write(f'  Compression Method: {entry.compression_method}\n')
                    log_file.write(f'  Encryption Method: {entry.encryption_method}\n')
                    log_file.write(f'  Compressed Blocks: {len(entry.compressed_blocks)}\n')
            log_file.write('\n' + '=' * 80 + '\nEND OF LOG\n' + '=' * 80 + '\n')
        console.print(f'[bold {DC_HIGHLIGHT}]Debug log saved to: {output_log_path}[/]')
    except Exception as e:
        console.print(f'[{DC_ORANGE}]Log save failed: {e}[/]')


# =====================================================================
# ENSURE DIRECTORIES
# =====================================================================

# =====================================================================
# DIRECTORY SETUP (Targeted to KUNALYT0)
# =====================================================================

def get_base_dir():
    return Path("/storage/emulated/0/Documents/KUNALYT0/")

def ensure_directories(base_dir=None):
    if base_dir is None:
        base_dir = get_base_dir()
    # Main folders
    (base_dir / "PAK").mkdir(parents=True, exist_ok=True)
    (base_dir / "UNPACK").mkdir(parents=True, exist_ok=True)
    (base_dir / "REPACK").mkdir(parents=True, exist_ok=True)
    (base_dir / "RESULT").mkdir(parents=True, exist_ok=True)
    (base_dir / "AUTO_MODS" / "INPUT").mkdir(parents=True, exist_ok=True)
    (base_dir / "AUTO_MODS" / "OUTPUT").mkdir(parents=True, exist_ok=True)

    # PAK TOOL
    pak_tool_dir = base_dir / "PAK TOOL"
    (pak_tool_dir / "EDIT").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "UNPACK").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "RESULT").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "PAK").mkdir(parents=True, exist_ok=True)

    # BUILD_PAK
    build_pak_dir = base_dir / "BUILD_PAK"
    (build_pak_dir / "CSV").mkdir(parents=True, exist_ok=True)
    (build_pak_dir / "EDIT").mkdir(parents=True, exist_ok=True)
    (build_pak_dir / "TEMPLATE").mkdir(parents=True, exist_ok=True)
    (build_pak_dir / "OUTPUT").mkdir(parents=True, exist_ok=True)

    # OBB_UNPACKER (for Black tool / repack)
    obb_dir = base_dir / "OBB_UNPACKER"
    (obb_dir / "ORGNAL").mkdir(parents=True, exist_ok=True)
    (obb_dir / "Modified_files").mkdir(parents=True, exist_ok=True)
    (obb_dir / "UNPACK").mkdir(parents=True, exist_ok=True)
    (obb_dir / "REPACK").mkdir(parents=True, exist_ok=True)

    # SKIN_TOOL (Mini + ZSDIC)
    skin_tool_root = base_dir / "SKIN_TOOL"
    skin_tool_root.mkdir(parents=True, exist_ok=True)

    for game in ["BGMI_SKIN", "PUBG_SKIN"]:
        game_base = skin_tool_root / game

        # MINI
        mini_base = game_base / "MINI"
        (mini_base / "MINI_ICON" / "INPUT").mkdir(parents=True, exist_ok=True)
        (mini_base / "MINI_ICON" / "OUTPUT").mkdir(parents=True, exist_ok=True)
        (mini_base / "TXTS").mkdir(parents=True, exist_ok=True)
        (mini_base / "AUTO_THEME" / "FILES").mkdir(parents=True, exist_ok=True)
        (mini_base / "AUTO_THEME" / "MODIFIED").mkdir(parents=True, exist_ok=True)
        (mini_base / "AUTO_THEME" / "TXT").mkdir(parents=True, exist_ok=True)
        (mini_base / "HIT EFFECT" / "org").mkdir(parents=True, exist_ok=True)
        (mini_base / "HIT EFFECT" / "modified").mkdir(parents=True, exist_ok=True)
        (mini_base / "LOOTCRATES" / "org").mkdir(parents=True, exist_ok=True)
        (mini_base / "LOOTCRATES" / "modified").mkdir(parents=True, exist_ok=True)

        # ZSDIC
        game_key = "BGMI" if game == "BGMI_SKIN" else "PUBG"
        zsdic_base = game_base / "ZSDIC"
        (zsdic_base / game_key / "skindats").mkdir(parents=True, exist_ok=True)
        (zsdic_base / game_key / "edited").mkdir(parents=True, exist_ok=True)
        (zsdic_base / game_key / "size").mkdir(parents=True, exist_ok=True)

        # FINAL
        (game_base / "FINAL").mkdir(parents=True, exist_ok=True)

    # LUA_TOOL
    lua_base = base_dir / "LUA_TOOL"
    (lua_base / "Lua_org").mkdir(parents=True, exist_ok=True)
    (lua_base / "Lua_Decript").mkdir(parents=True, exist_ok=True)
    (lua_base / "Lua_Rueslt").mkdir(parents=True, exist_ok=True)

    re_lua = lua_base / "RE_LUA ANY SIZE"
    (re_lua / "EDIT_LUA").mkdir(parents=True, exist_ok=True)
    (re_lua / "ORGNAL_PAK").mkdir(parents=True, exist_ok=True)
    (re_lua / "REPACK_MOD").mkdir(parents=True, exist_ok=True)

    lua_custom = lua_base / "LUA_CUSTOM"
    (lua_custom / "EDIT").mkdir(parents=True, exist_ok=True)
    (lua_custom / "PAK").mkdir(parents=True, exist_ok=True)
    (lua_custom / "RESULT").mkdir(parents=True, exist_ok=True)

    # CREDIT_TOOL (Black Tool)
    credit_base = base_dir / "CREDIT_TOOL"
    (credit_base / "ORGNAL").mkdir(parents=True, exist_ok=True)
    (credit_base / "MODDED FILE").mkdir(parents=True, exist_ok=True)

    # ANTIRESET_OBB (compatibility)
    (base_dir / "EXES").mkdir(parents=True, exist_ok=True)
    (base_dir / "ANTIRESET_OBB" / "MOD_REPACK").mkdir(parents=True, exist_ok=True)

# Call this at start of script or in main execution
ensure_directories()


# =====================================================================
# AUTO TERMUX SETUP
# =====================================================================

def auto_termux_setup():
    if "com.termux" not in os.environ.get("PREFIX", ""):
        return

    needs_setup = False
    try:
        import rich
        import requests
        import gmalg
        import Crypto
        import zstandard
        import colorama
        from termcolor import colored
        if not os.path.exists(os.path.expanduser("~/storage")):
            needs_setup = True
    except ImportError:
        needs_setup = True

    if not needs_setup:
        return

    Y = "\033[1;33m"
    G = "\033[1;32m"
    C = "\033[1;36m"
    RES = "\033[0m"

    os.system("clear")
    print(f"{C}=================================================={RES}")
    print(f"{G}    LUA TOOL AUTO-INSTALLER    {RES}")
    print(f"{C}=================================================={RES}\n")
    print(f"{Y}[*] First time setup detected!{RES}\n")
    time.sleep(1)

    print(f"{C}--------------------------------------------------{RES}")
    print(f"{G}[>] Granting Storage Permissions{RES}")
    if not os.path.exists(os.path.expanduser("~/storage")):
        os.system("yes | termux-setup-storage")
        time.sleep(2)

    print(f"{C}--------------------------------------------------{RES}")
    print(f"{G}[>] Updating packages{RES}")
    os.system("pkg update -y && pkg upgrade -y")

    print(f"{C}--------------------------------------------------{RES}")
    print(f"{G}[>] Installing core packages{RES}")
    os.system("pkg install python python-pip clang make -y")

    print(f"{C}--------------------------------------------------{RES}")
    print(f"{G}[>] Installing Python libraries{RES}")
    os.system("pip install rich pycryptodome zstandard requests gmalg colorama termcolor pytz")

    print(f"{C}--------------------------------------------------{RES}")
    print(f"{G}[>] Setting permissions{RES}")
    os.system("chmod +x *")

    print(f"\n{C}=================================================={RES}")
    print(f"{G} ALL SYSTEMS GO! INITIALIZATION COMPLETE.{RES}")
    print(f"{C}=================================================={RES}\n")
    time.sleep(2)
    os.system("clear")


# =====================================================================
# MAIN MENU LOOP
# =====================================================================


class SM4KeyFinder:
    """
    SM4 Key Finder v7.0 — Dual Scan (ASCII + UTF-16LE) with strict pattern
    """

    @staticmethod
    def is_sm4_new_candidate(s: str) -> bool:
        """Strict: 20 chars, [char][char][digit] pattern"""
        if len(s) != 20:
            return False
        
        # Enforce [char][char][digit] pattern
        for i in range(20):
            c = s[i]
            pos = i % 3
            if pos < 2: # pos 0 or 1
                if not c.isalpha():
                    return False
            else: # pos 2
                if not c.isdigit():
                    return False
        return True

    @staticmethod
    def scan_file(filepath: Path, progress_cb=None) -> list:
        results = []
        file_size = filepath.stat().st_size
        if file_size == 0:
            return results

        # Read whole file into memory (232 MB is fine for Termux with 4+ GB RAM)
        # This avoids ALL chunk-boundary bugs and guarantees complete scan.
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
        except Exception as e:
            console.print(f"[{DC_RED}]Read Error: {e}[/]")
            return results

        pattern_ascii = _ptre.compile(rb'[A-Za-z0-9]{20}')
        pattern_utf16 = _ptre.compile(b'(?:[\x20-\x7e]\x00){20}')

        seen_ascii = set()
        seen_utf16 = set()
        start = time.time()
        last_ui_update = 0
        chunk_report = 20 * 1024 * 1024  # report every 20 MB

        # ---- ASCII scan (full file) ----
        for m in pattern_ascii.finditer(data):
            abs_off = m.start()
            if abs_off in seen_ascii:
                continue
            seen_ascii.add(abs_off)
            s = m.group(0).decode('ascii', errors='ignore')
            if SM4KeyFinder.is_sm4_new_candidate(s):
                results.append({
                    "offset": hex(abs_off),
                    "type": "ASCII",
                    "value": s
                })

            # Progress callback every 20 MB
            if progress_cb and abs_off - last_ui_update >= chunk_report:
                last_ui_update = abs_off
                elapsed = time.time() - start
                offset_mb = abs_off / (1024 * 1024)
                speed = offset_mb / elapsed if elapsed > 0 else 0
                progress_cb({
                    "offset_mb": round(offset_mb, 2),
                    "total_mb": round(file_size / (1024 * 1024), 2),
                    "total_keys": len(results),
                    "speed": round(speed, 2),
                    "new_keys": [],
                    "last_key": results[-1] if results else None
                })

        # ---- UTF-16LE scan (full file) ----
        for m in pattern_utf16.finditer(data):
            abs_off = m.start()
            if abs_off in seen_utf16:
                continue
            seen_utf16.add(abs_off)
            s = m.group(0)[::2].decode('ascii', errors='ignore')
            if SM4KeyFinder.is_sm4_new_candidate(s):
                k = {
                    "offset": hex(abs_off),
                    "type": "UTF16",
                    "value": s
                }
                results.append(k)

                # Live key update in UI
                if progress_cb:
                    elapsed = time.time() - start
                    offset_mb = abs_off / (1024 * 1024)
                    speed = offset_mb / elapsed if elapsed > 0 else 0
                    progress_cb({
                        "offset_mb": round(offset_mb, 2),
                        "total_mb": round(file_size / (1024 * 1024), 2),
                        "total_keys": len(results),
                        "speed": round(speed, 2),
                        "new_keys": [k],
                        "last_key": results[-1]
                    })

        # Final progress callback (100% complete)
        if progress_cb:
            elapsed = time.time() - start
            progress_cb({
                "offset_mb": round(file_size / (1024 * 1024), 2),
                "total_mb": round(file_size / (1024 * 1024), 2),
                "total_keys": len(results),
                "speed": round((file_size / (1024 * 1024)) / elapsed if elapsed > 0 else 0, 2),
                "new_keys": [],
                "last_key": results[-1] if results else None
            })

        return results

    def __init__(self, so_folder="."):
        self.so_folder = Path(so_folder)
        self.found_keys = set()

    def scan_folder(self):
        so_files = sorted(self.so_folder.glob("*.so"),
                          key=lambda x: x.stat().st_size, reverse=True)
        if not so_files:
            return []
        for so_file in so_files:
            for k in SM4KeyFinder.scan_file(so_file):
                self.found_keys.add(k["value"])
        return sorted(self.found_keys)

# =====================================================================
# OBB ALL-IN-ONE TOOL (Extract PAKs from OBB -> Unpack -> Edit -> Repack -> Auto Antireset)
# =====================================================================

def inplace_patch_obb(obb_path, new_pak_path, pak_name_in_obb):
    """OBB ko bina unpack kiye (In-Place) andar ka PAK replace karta hai."""
    import zipfile
    try:
        with zipfile.ZipFile(obb_path, 'r') as zf:
            target_name = None
            for n in zf.namelist():
                if n.endswith(pak_name_in_obb):
                    target_name = n
                    break
            
            if not target_name:
                return False, f"PAK '{pak_name_in_obb}' OBB mein nahi mila!"
                
            info = zf.getinfo(target_name)
            header_offset = info.header_offset
            compress_size = info.compress_size

        new_pak_data = Path(new_pak_path).read_bytes()

        if len(new_pak_data) > compress_size:
            return False, f"Naya PAK bada hai ({human_size(len(new_pak_data))} > {human_size(compress_size)})"
            
        if len(new_pak_data) < compress_size:
            new_pak_data = new_pak_data.ljust(compress_size, b'\x00')

        with open(obb_path, 'rb') as f:
            f.seek(header_offset)
            local_header = f.read(30)
            name_len = int.from_bytes(local_header[26:28], 'little')
            extra_len = int.from_bytes(local_header[28:30], 'little')
            data_offset = header_offset + 30 + name_len + extra_len

        with open(obb_path, 'r+b') as f:
            f.seek(data_offset)
            f.write(new_pak_data)
            
        return True, "Success"
    except Exception as e:
        return False, str(e)


def obb_pak_tool_menu(data_path):
    """
    OBB ALL-IN-ONE TOOL
    Flow: OBB -> Extract PAKs -> Unpack PAK -> Edit -> Repack -> Patch OBB (Antireset)
    """
    obb_base = data_path / "OBB_UNPACKER"
    obb_input = obb_base / "ORGNAL"          
    paks_dir = obb_base / "PAKS"              
    unpack_dir = obb_base / "UNPACK"          
    modified_dir = obb_base / "Modified_files" 
    repack_dir = obb_base / "REPACK"          
    antireset_dir = obb_base / "ANTIRESET"    
    search_dir = obb_base / "SEARCH"

    for d in [obb_input, paks_dir, unpack_dir, modified_dir, repack_dir, antireset_dir, search_dir]:
        d.mkdir(parents=True, exist_ok=True)

    while True:
        print_banner()
        
        counts = {
            "OBBs": len(list(obb_input.glob("*.[oO][bB][bB]"))),
            "PAKs": len(list(paks_dir.glob("*.pak"))),
            "Unpacked Folders": len(list(unpack_dir.iterdir())),
            "Modified Files": len(list(modified_dir.rglob("*")))
        }

        # Status Panel
        status_table = Table(box=HEAVY_EDGE, border_style=DC_HIGHLIGHT, expand=True)
        status_table.add_column("📊 WORKSPACE STATUS", style="bold white")
        status_table.add_column("COUNT", style=f"bold {DC_HIGHLIGHT}", justify="right")
        for k, v in counts.items():
            status_table.add_row(k, str(v))
        
        console.print(Panel(status_table, border_style=DC_BORDER, box=ROUNDED))

        # Menu Table
        menu_table = Table(show_header=False, box=HEAVY_EDGE, expand=True, title=f"[bold black on {DC_HIGHLIGHT}] 🚀 OBB ALL-IN-ONE TOOL 🚀 [/]")
        menu_table.add_column("OPT", style=f"bold {DC_HIGHLIGHT}", justify="center", width=4)
        menu_table.add_column("COMMAND", style=f"bold {DC_TEXT}")
        menu_table.add_column("DESC", style=f"dim {DC_DIM}")

        menu_table.add_row("1", "📦 EXTRACT PAKs FROM OBB", "OBB ke andar se .pak files nikalo")
        menu_table.add_row("2", "📂 UNPACK PAK", "PAK ko editable files mein kholo")
        menu_table.add_row("3", "🔨 REPACK + AUTO ANTIRESET", "Edited files -> PAK -> Patch OBB")
        menu_table.add_row("4", "🔍 ANALYZE PAK", "PAK info check karo")
        menu_table.add_row("5", "🔎 SEARCH & COPY FILES", "Unpacked folder mein file search karo")
        menu_table.add_row("6", "🗑️ CLEAR WORKSPACE", "Folders ko clear karo")
        menu_table.add_row("0", f"[{DC_RED}]BACK[/]", "Return to Main Menu")
        
        console.print(Panel(menu_table, border_style=DC_BORDER, box=ROUNDED))

        choice = safe_input(f"\n[bold {DC_HIGHLIGHT}]ENTER CHOICE (0-6) > [/]").strip()

        if choice == '0':
            break

        # ========== OPTION 1: EXTRACT PAKs FROM OBB ==========
        elif choice == '1':
            obb_files = list(obb_input.glob("*.obb")) + list(obb_input.glob("*.zip"))
            if not obb_files:
                console.print(f"[bold {DC_RED}]No OBB files found in {obb_input}[/]")
                safe_input('\nPress Enter...'); continue
            
            # Display OBB List
            sel_table = Table(title="Select OBB File", box=DOUBLE_EDGE, border_style=DC_BORDER, header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File Name", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            for i, f in enumerate(obb_files, 1):
                sel_table.add_row(str(i), f.name, human_size(f.stat().st_size))
            console.print(sel_table)
            
            obb_sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select OBB (1-{len(obb_files)}) or 0=Back: [/]").strip()
            if obb_sel == '0' or not obb_sel.isdigit(): continue
            target_obb = obb_files[int(obb_sel) - 1]

            import zipfile
            try:
                with zipfile.ZipFile(target_obb, 'r') as zf:
                    pak_entries = [n for n in zf.namelist() if n.lower().endswith('.pak')]
                    if not pak_entries:
                        console.print(f"[bold {DC_RED}]No .pak files found inside {target_obb.name}[/]")
                        safe_input('\nPress Enter...'); continue
                    
                    with Progress(SpinnerColumn(), TextColumn("[bold white]{task.description}"), BarColumn(), console=console) as progress:
                        task = progress.add_task(f"Extracting from {target_obb.name}...", total=len(pak_entries))
                        for entry_name in pak_entries:
                            fname = Path(entry_name).name
                            dest = paks_dir / fname
                            with zf.open(entry_name) as src, open(dest, 'wb') as dst:
                                shutil.copyfileobj(src, dst)
                            progress.update(task, advance=1, description=f"[cyan]{fname}[/]")
                    
                    console.print(Panel(f"[bold {DC_GREEN}]✅ {len(pak_entries)} PAK file(s) extracted to {paks_dir}[/]", border_style=DC_GREEN))
            except Exception as e:
                console.print(f"[bold {DC_RED}]Error: {e}[/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 2: UNPACK PAK ==========
        elif choice == '2':
            pak_files = list(paks_dir.glob("*.pak"))
            if not pak_files:
                console.print(f"[bold {DC_RED}]No PAKs found in {paks_dir}[/]")
                safe_input('\nPress Enter...'); continue
            
            # Display PAK List (Unpack)
            sel_table = Table(title="Select PAK File to Unpack", box=DOUBLE_EDGE, border_style=DC_BORDER, header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File Name", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            sel_table.add_column("Uncompressed", justify="right", style="bold green")
            sel_table.add_column("Encryption", style="bold cyan")
            sel_table.add_column("Files", justify="right", style="dim")

            with console.status("[bold cyan]Reading PAK Headers...[/]", spinner="dots"):
                for i, f in enumerate(pak_files, 1):
                    try:
                        temp_pak = TencentPakFile(f, silent=True)
                        total_uncomp = sum(e.uncompressed_size for e in temp_pak._files if e.uncompressed_size)
                        uncomp_str = human_size(total_uncomp)
                        enc_methods = sorted({temp_pak._get_method_str(e.encryption_method, e.encrypted) for e in temp_pak._files})
                        enc_str = ", ".join(enc_methods) if enc_methods else "NONE"
                        if len(enc_str) > 20: enc_str = enc_str[:17] + "..."
                        file_count = len(temp_pak._files)
                    except Exception:
                        uncomp_str, enc_str, file_count = "0 B", "ERROR", 0
                    sel_table.add_row(str(i), f.name, human_size(f.stat().st_size), uncomp_str, enc_str, str(file_count))
            console.print(sel_table)
            
            pak_sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK (1-{len(pak_files)}) or 0=Back: [/]").strip()
            if pak_sel == '0' or not pak_sel.isdigit(): continue
            target_pak = pak_files[int(pak_sel) - 1]
            unpack_root = unpack_dir / target_pak.stem
            
            try:
                pak = TencentPakFile(target_pak)
                start_time = time.time()
                total_uncompressed = sum(e.uncompressed_size for e in pak._files if e.uncompressed_size)
                
                success, ext_counts = pak.dump(unpack_root)
                time_taken = time.time() - start_time
                
                if success:
                    enc_methods = sorted({pak._get_method_str(e.encryption_method, e.encrypted) for e in pak._files})
                    comp_methods = sorted({pak._get_method_str(e.compression_method, False) for e in pak._files})
                    
                    enc_breakdown = defaultdict(int)
                    for e in pak._files:
                        enc_breakdown[pak._get_method_str(e.encryption_method, e.encrypted)] += 1
                        
                    show_premium_unpack_dashboard(
                        target_pak.name, unpack_root, ext_counts, 
                        enc_methods, comp_methods, pak._pak_info.version, 
                        total_uncompressed, time_taken, enc_breakdown
                    )
            except Exception as e:
                console.print(f"[bold {DC_RED}]Unpack failed: {e}[/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 3: REPACK + AUTO ANTIRESET ==========
        elif choice == '3':
            obb_files = list(obb_input.glob("*.obb")) + list(obb_input.glob("*.zip"))
            pak_files = list(paks_dir.glob("*.pak"))
            
            if not obb_files or not pak_files:
                console.print(f"[bold {DC_RED}]Missing OBB or PAK files![/]")
                safe_input('\nPress Enter...'); continue
            
            if not any(modified_dir.iterdir()):
                console.print(f"[bold {DC_RED}]Modified_files folder is empty![/]")
                safe_input('\nPress Enter...'); continue
            
            # Display PAK List (Repack)
            sel_table = Table(title="Select PAK File to Repack", box=DOUBLE_EDGE, border_style=DC_BORDER, header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File Name", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            sel_table.add_column("Uncompressed", justify="right", style="bold green")
            sel_table.add_column("Encryption", style="bold cyan")
            sel_table.add_column("Files", justify="right", style="dim")

            with console.status("[bold cyan]Reading PAK Headers...[/]", spinner="dots"):
                for i, f in enumerate(pak_files, 1):
                    try:
                        temp_pak = TencentPakFile(f, silent=True)
                        total_uncomp = sum(e.uncompressed_size for e in temp_pak._files if e.uncompressed_size)
                        uncomp_str = human_size(total_uncomp)
                        enc_methods = sorted({temp_pak._get_method_str(e.encryption_method, e.encrypted) for e in temp_pak._files})
                        enc_str = ", ".join(enc_methods) if enc_methods else "NONE"
                        if len(enc_str) > 20: enc_str = enc_str[:17] + "..."
                        file_count = len(temp_pak._files)
                    except Exception:
                        uncomp_str, enc_str, file_count = "0 B", "ERROR", 0
                    sel_table.add_row(str(i), f.name, human_size(f.stat().st_size), uncomp_str, enc_str, str(file_count))
            console.print(sel_table)
            
            pak_sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK to Repack (1-{len(pak_files)}): [/]").strip()
            if pak_sel == '0' or not pak_sel.isdigit(): continue
            target_pak = pak_files[int(pak_sel) - 1]
            out_pak = repack_dir / target_pak.name
            
            console.print(f"\n[bold {DC_HIGHLIGHT}]Repacking {target_pak.name}...[/]")
            try:
                pak = TencentPakFile(target_pak)
                result = repack_pak_file_full(pak, modified_dir, out_pak, target_path=None, force_add=True, force_size=True)
                count = result[0] if isinstance(result, tuple) else result
                stats = result[1] if isinstance(result, tuple) else None
                
                if count == 0:
                    console.print(f"[{DC_ORANGE}]No files processed. Aborting.[/]")
                    safe_input('\nPress Enter...'); continue
                
                if stats:
                    # Calculate Encryption Breakdown for Repack Verification
                    enc_breakdown = defaultdict(int)
                    # FIX: Read the newly created PAK file, not the old one
                    new_pak = TencentPakFile(out_pak)
                    for e in new_pak._files:
                        method = new_pak._get_method_str(e.encryption_method, e.encrypted)
                        enc_breakdown[method] += 1
                    
                    # Display Verification Table
                    table_verify = Table(title="Repack Encryption Verification", box=HEAVY_EDGE, border_style=DC_GREEN)
                    table_verify.add_column("Method", style="bold white")
                    table_verify.add_column("Count", style=f"bold {DC_GREEN}", justify="right")
                    for method, count in enc_breakdown.items():
                        table_verify.add_row(method, str(count))
                    console.print(table_verify)

                    print_forensic_dashboard(stats, out_pak, title_text="REPACK ANALYSIS")
                
                console.print(f"\n[bold {DC_HIGHLIGHT}]Patching into OBB (Antireset Mode)...[/]")
                target_obb = obb_files[0]
                output_obb = antireset_dir / target_obb.name
                shutil.copy2(target_obb, output_obb)
                
                success, msg = inplace_patch_obb(output_obb, out_pak, out_pak.name)
                if success:
                    console.print(Panel(f"[bold {DC_GREEN}]✅ ANTIRESET OBB CREATED![/]\n[white]Output:[/] {antireset_dir}/{output_obb.name}", border_style=DC_GREEN))
                else:
                    console.print(Panel(f"[bold {DC_RED}]❌ PATCH FAILED![/]\n[white]Reason:[/] {msg}", border_style=DC_RED))
            except Exception as e:
                console.print(f"[bold {DC_RED}]Repack failed: {e}[/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 4: ANALYZE PAK ==========
        elif choice == '4':
            pak_files = list(paks_dir.glob("*.pak"))
            if not pak_files:
                console.print(f"[bold {DC_RED}]No PAKs found.[/]")
                safe_input('\nPress Enter...'); continue
            
            # Display PAK List (Analyze)
            sel_table = Table(title="Select PAK File to Analyze", box=DOUBLE_EDGE, border_style=DC_BORDER, header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File Name", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            sel_table.add_column("Uncompressed", justify="right", style="bold green")
            sel_table.add_column("Encryption", style="bold cyan")
            sel_table.add_column("Files", justify="right", style=f"dim")

            with console.status("[bold cyan]Reading PAK Headers...[/]", spinner="dots"):
                for i, f in enumerate(pak_files, 1):
                    try:
                        temp_pak = TencentPakFile(f, silent=True)
                        total_uncomp = sum(e.uncompressed_size for e in temp_pak._files if e.uncompressed_size)
                        uncomp_str = human_size(total_uncomp)
                        enc_methods = sorted({temp_pak._get_method_str(e.encryption_method, e.encrypted) for e in temp_pak._files})
                        enc_str = ", ".join(enc_methods) if enc_methods else "NONE"
                        if len(enc_str) > 20: enc_str = enc_str[:17] + "..."
                        file_count = len(temp_pak._files)
                    except Exception:
                        uncomp_str, enc_str, file_count = "0 B", "ERROR", 0
                    sel_table.add_row(str(i), f.name, human_size(f.stat().st_size), uncomp_str, enc_str, str(file_count))
            console.print(sel_table)
            
            pak_sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK to Analyze (1-{len(pak_files)}): [/]").strip()
            if pak_sel == '0' or not pak_sel.isdigit(): continue
            try:
                pak_file = pak_files[int(pak_sel) - 1]
                pak = TencentPakFile(pak_file)
                f_size = pak_file.stat().st_size
                stats = {
                    "files_processed": len(pak._files),
                    "compressed_count": sum(1 for e in pak._files if e.compression_method != 0),
                    "encrypted_count": sum(1 for e in pak._files if e.encrypted),
                    "original_size": f_size, "new_size": f_size,
                    "orig_index_sha": pak._pak_info.index_hash.hex(),
                    "new_index_sha": pak._pak_info.index_hash.hex(),
                    "version": pak._pak_info.version, "force_crc": True, "size_match": True
                }
                print_forensic_dashboard(stats, pak_file.name, title_text="ANALYZE REPORT")
            except Exception as e:
                console.print(f"[bold {DC_RED}]Error: {e}[/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 5: SEARCH & COPY FILES ==========
        elif choice == '5':
            search_query = safe_input(f"[bold {DC_HIGHLIGHT}]Enter file search query (e.g., BP_Player* or Pawn): [/]").strip()
            if not search_query: continue

            matches = []
            import fnmatch
            for root, _, files in os.walk(unpack_dir):
                for name in files:
                    if fnmatch.fnmatch(name, search_query) or search_query.lower() in name.lower():
                        matches.append(Path(root) / name)

            if not matches:
                console.print(f"[bold {DC_RED}]No matches found in UNPACK folder![/]")
                safe_input('\nPress Enter...'); continue

            console.print(f"[bold {DC_GREEN}]Found {len(matches)} files. Copying to SEARCH folder...[/]")
            
            # Clean search dir
            for item in search_dir.iterdir():
                if item.is_file(): item.unlink()
                elif item.is_dir(): shutil.rmtree(item)

            for m in matches:
                rel = m.relative_to(unpack_dir)
                dest = search_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(m, dest)

            sum_table = Table(title="Search Results Summary", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
            sum_table.add_column("File Name", style="bold white")
            sum_table.add_column("Size", style="bold cyan", justify="right")
            for m in matches:
                sum_table.add_row(m.name, human_size(m.stat().st_size))
            
            console.print(sum_table)
            console.print(f"[bold {DC_HIGHLIGHT}]📂 Files safely copied to: {search_dir}[/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 6: CLEAR WORKSPACE ==========
        elif choice == '6':
            console.print("\n[bold]Select folder to clear:[/]")
            console.print("1. PAKS\n2. UNPACK\n3. Modified_files\n4. REPACK & ANTIRESET\n5. SEARCH\n6. ALL")
            c_sel = safe_input(f"[bold {DC_HIGHLIGHT}]Choice (1-6) or 0=Cancel: [/]").strip()
            
            if c_sel == '0': continue
            
            dirs_to_clear = []
            if c_sel == '1': dirs_to_clear = [paks_dir]
            elif c_sel == '2': dirs_to_clear = [unpack_dir]
            elif c_sel == '3': dirs_to_clear = [modified_dir]
            elif c_sel == '4': dirs_to_clear = [repack_dir, antireset_dir]
            elif c_sel == '5': dirs_to_clear = [search_dir]
            elif c_sel == '6': dirs_to_clear = [paks_dir, unpack_dir, modified_dir, repack_dir, antireset_dir, search_dir]
            
            for d in dirs_to_clear:
                if d.exists():
                    shutil.rmtree(d)
                    d.mkdir(parents=True, exist_ok=True)
            
            console.print(f"[bold {DC_GREEN}]✅ Workspace cleared![/]")
            safe_input('\nPress Enter...')

        # ========== OPTION 1: EXTRACT PAKs FROM OBB ==========
        if choice == '1':
            obb_files = list(obb_input.glob("*.obb")) + list(obb_input.glob("*.zip"))
            if not obb_files:
                console.print(Panel(
                    f"[bold {DC_RED}]No OBB files found![/]\n\n"
                    f"[white]Place your original OBB here:[/white]\n"
                    f"[bold {DC_HIGHLIGHT}]{obb_input}[/bold {DC_HIGHLIGHT}]",
                    border_style=DC_RED, box=HEAVY_EDGE
                ))
                safe_input('\nPress Enter...')
                continue
            
            sel_table = Table(title="Select OBB File", box=DOUBLE_EDGE, border_style=DC_BORDER,
                            header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            for i, f in enumerate(obb_files, 1):
                sel_table.add_row(str(i), f.name, human_size(f.stat().st_size))
            console.print(sel_table)
            
            sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select OBB (1-{len(obb_files)}, 0=back): [/]").strip()
            if sel == '0' or not sel.isdigit(): continue
            idx = int(sel) - 1
            if idx < 0 or idx >= len(obb_files): continue
            
            target_obb = obb_files[idx]
            
            console.print(f"\n[bold {DC_HIGHLIGHT}]Scanning {target_obb.name} for PAK files...[/]")
            
            import zipfile
            try:
                with zipfile.ZipFile(target_obb, 'r') as zf:
                    pak_entries = [n for n in zf.namelist() if n.lower().endswith('.pak')]
                    
                    if not pak_entries:
                        console.print(f"[bold {DC_RED}]No .pak files found inside {target_obb.name}[/]")
                        safe_input('\nPress Enter...')
                        continue
                    
                    console.print(f"[bold {DC_GREEN}]Found {len(pak_entries)} PAK file(s):[/]")
                    for n in pak_entries:
                        info = zf.getinfo(n)
                        console.print(f"  [bold {DC_HIGHLIGHT}]→[/] {n} [dim]({human_size(info.file_size)})[/]")
                    
                    console.print(f"\n[bold {DC_HIGHLIGHT}]Extracting PAKs to {paks_dir}...[/]")
                    
                    extracted = 0
                    with Progress(
                        SpinnerColumn(style=f"bold {DC_HIGHLIGHT}"),
                        TextColumn("[bold white]{task.description}"),
                        BarColumn(bar_width=30, complete_style=f"bold {DC_HIGHLIGHT}"),
                        console=console
                    ) as progress:
                        task = progress.add_task("Extracting...", total=len(pak_entries))
                        for entry_name in pak_entries:
                            fname = Path(entry_name).name
                            dest = paks_dir / fname
                            try:
                                with zf.open(entry_name) as src, open(dest, 'wb') as dst:
                                    shutil.copyfileobj(src, dst)
                                extracted += 1
                                progress.update(task, advance=1, description=f"[cyan]{fname}[/]")
                            except Exception as e:
                                console.print(f"[{DC_ORANGE}]Failed: {fname} - {e}[/]")
                                progress.update(task, advance=1)
                    
                    console.print(Panel(
                        f"[bold {DC_GREEN}]✅ {extracted}/{len(pak_entries)} PAK file(s) extracted![/]\n\n"
                        f"[white]Location:[/] {paks_dir}\n\n"
                        f"[dim]Next step: Option 2 select karke PAK unpack karo[/]",
                        border_style=DC_GREEN, box=HEAVY_EDGE
                    ))
            except zipfile.BadZipFile:
                console.print(f"[bold {DC_RED}]Invalid OBB (not a ZIP): {target_obb.name}[/]")
            except Exception as e:
                console.print(f"[bold {DC_RED}]Error: {e}[/]")
            
            safe_input('\nPress Enter...')

        # ========== OPTION 2: UNPACK PAK ==========
        elif choice == '2':
            pak_files = list(paks_dir.glob("*.pak"))
            if not pak_files:
                console.print(Panel(
                    f"[bold {DC_RED}]No PAK files found![/]\n\n"
                    f"[white]First extract PAKs from OBB (Option 1)[/white]",
                    border_style=DC_RED, box=HEAVY_EDGE
                ))
                safe_input('\nPress Enter...')
                continue
            
            sel_table = Table(title="Select PAK to Unpack", box=DOUBLE_EDGE, border_style=DC_BORDER,
                            header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            for i, f in enumerate(pak_files, 1):
                sel_table.add_row(str(i), f.name, human_size(f.stat().st_size))
            console.print(sel_table)
            
            sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK (1-{len(pak_files)}, 0=back): [/]").strip()
            if sel == '0' or not sel.isdigit(): continue
            idx = int(sel) - 1
            if idx < 0 or idx >= len(pak_files): continue
            
            target_pak = pak_files[idx]
            unpack_root = unpack_dir / target_pak.stem
            
            console.print(f"\n[bold {DC_HIGHLIGHT}]Unpacking {target_pak.name}...[/]")
            console.print(f"[dim]Output: {unpack_root}[/]\n")
            
            try:
                pak = TencentPakFile(target_pak)
                start_time = time.time()
                success, ext_counts = pak.dump(unpack_root)
                
                if success:
                    elapsed = time.time() - start_time
                    total = sum(ext_counts.values())
                    
                    summary = Table(box=ROUNDED, show_header=False, expand=True)
                    summary.add_column("METRIC", style=f"bold {DC_HIGHLIGHT}")
                    summary.add_column("VALUE", style="bold white")
                    summary.add_row("PAK File", target_pak.name)
                    summary.add_row("Output Folder", str(unpack_root))
                    summary.add_row("Time", f"{elapsed:.2f}s")
                    summary.add_row("Total Files", f"{total:,}")
                    
                    console.print(Panel(
                        summary,
                        title=f"[bold black on {DC_GREEN}] ✅ UNPACK COMPLETE [/]",
                        border_style=DC_GREEN, box=HEAVY_EDGE
                    ))
                    
                    console.print(f"\n[bold {DC_HIGHLIGHT}]💡 Next steps:[/]")
                    console.print(f"  1. Edit files in: [bold]{unpack_root}[/]")
                    console.print(f"  2. Copy edited files to: [bold]{modified_dir}[/]")
                    console.print(f"  3. Run Option 3 (Repack + Antireset)")
            except Exception as e:
                console.print(f"[bold {DC_RED}]Unpack failed: {e}[/]")
                import traceback
                traceback.print_exc()
            
            safe_input('\nPress Enter...')

        # ========== OPTION 3: REPACK + AUTO ANTIRESET ==========
        elif choice == '3':
            obb_files = list(obb_input.glob("*.obb")) + list(obb_input.glob("*.zip"))
            pak_files = list(paks_dir.glob("*.pak"))
            
            if not obb_files:
                console.print(f"[bold {DC_RED}]No original OBB in {obb_input}[/]")
                safe_input('\nPress Enter...')
                continue
            
            if not pak_files:
                console.print(f"[bold {DC_RED}]No PAK files in {paks_dir}[/]")
                safe_input('\nPress Enter...')
                continue
            
            if not any(modified_dir.iterdir()):
                console.print(f"[bold {DC_RED}]Modified_files folder is empty![/]")
                console.print(f"[dim]Copy your edited files here: {modified_dir}[/]")
                safe_input('\nPress Enter...')
                continue
            
            sel_table = Table(title="Select PAK to Repack", box=DOUBLE_EDGE, border_style=DC_BORDER,
                            header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File", style=f"bold {DC_TEXT}")
            sel_table.add_column("Size", justify="right", style=f"bold {DC_TEXT}")
            for i, f in enumerate(pak_files, 1):
                sel_table.add_row(str(i), f.name, human_size(f.stat().st_size))
            console.print(sel_table)
            
            sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK (1-{len(pak_files)}, 0=back): [/]").strip()
            if sel == '0' or not sel.isdigit(): continue
            idx = int(sel) - 1
            if idx < 0 or idx >= len(pak_files): continue
            
            target_pak = pak_files[idx]
            out_pak = repack_dir / target_pak.name
            
            console.print(f"\n[bold {DC_HIGHLIGHT}]Step 1/2: Repacking {target_pak.name}...[/]")
            try:
                pak = TencentPakFile(target_pak)
                result = repack_pak_file_full(
                    pak, modified_dir, out_pak,
                    target_path=None, force_add=True, force_size=True
                )
                
                if isinstance(result, tuple):
                    count, stats = result
                else:
                    count, stats = result, None
                
                if count == 0:
                    console.print(f"[{DC_ORANGE}]No files processed. Aborting.[/]")
                    safe_input('\nPress Enter...')
                    continue
                
                if stats:
                    print_forensic_dashboard(stats, out_pak, title_text="REPACK ANALYSIS")
                
            except Exception as e:
                console.print(f"[bold {DC_RED}]Repack failed: {e}[/]")
                import traceback
                traceback.print_exc()
                safe_input('\nPress Enter...')
                continue
            
            console.print(f"\n[bold {DC_HIGHLIGHT}]Step 2/2: Patching into OBB (Antireset Mode)...[/]")
            
            if len(obb_files) == 1:
                target_obb = obb_files[0]
            else:
                console.print("\n[bold]Available OBB files:[/]")
                for i, f in enumerate(obb_files, 1):
                    console.print(f"  [bold {DC_HIGHLIGHT}]{i}.[/] {f.name}")
                sel_obb = safe_input(f"[bold {DC_HIGHLIGHT}]Select OBB (1-{len(obb_files)}): [/]").strip()
                if not sel_obb.isdigit(): continue
                target_obb = obb_files[int(sel_obb) - 1]
            
            output_obb = antireset_dir / target_obb.name
            shutil.copy2(target_obb, output_obb)
            
            pak_name_in_obb = out_pak.name
            
            success, msg = inplace_patch_obb(output_obb, out_pak, pak_name_in_obb)
            
            if success:
                console.print(Panel(
                    f"[bold {DC_GREEN}]✅ ANTIRESET OBB CREATED SUCCESSFULLY![/]\n\n"
                    f"[white]OBB File:[/] [bold]{output_obb.name}[/]\n"
                    f"[white]PAK Injected:[/] {out_pak.name}\n"
                    f"[white]Hash Status:[/] {DC_HIGHLIGHT}UNTOUCHED (Protected from reset)[/]\n\n"
                    f"[bold {DC_HIGHLIGHT}]📂 Output:[/] {antireset_dir}\n\n"
                    f"[dim]Ab is OBB ko directly Android/obb/BGMI/ mein copy karo![/]",
                    title=f"[bold black on {DC_GREEN}] ✅ SUCCESS [/]",
                    border_style=DC_GREEN, box=HEAVY_EDGE
                ))
            else:
                console.print(Panel(
                    f"[bold {DC_RED}]❌ OBB PATCH FAILED![/]\n\n"
                    f"[white]Reason:[/] {msg}\n\n"
                    f"[dim]Tips:[/]\n"
                    f"[dim]• Agar 'PAK bada hai' error ho, toh thodi aur files edit karo[/]\n"
                    f"[dim]• Check karo ki PAK name sahi hai[/]",
                    border_style=DC_RED, box=HEAVY_EDGE
                ))
            
            safe_input('\nPress Enter...')

        # ========== OPTION 4: ANALYZE PAK ==========
        elif choice == '4':
            pak_files = list(paks_dir.glob("*.pak"))
            if not pak_files:
                console.print(f"[bold {DC_RED}]No PAKs found. Run Option 1 first.[/]")
                safe_input('\nPress Enter...')
                continue
            
            sel_table = Table(title="Select PAK to Analyze", box=DOUBLE_EDGE, border_style=DC_BORDER,
                            header_style=f"bold black on {DC_HIGHLIGHT}")
            sel_table.add_column("#", justify="center", style=f"bold {DC_HIGHLIGHT}", width=4)
            sel_table.add_column("File", style=f"bold {DC_TEXT}")
            for i, f in enumerate(pak_files, 1):
                sel_table.add_row(str(i), f.name)
            console.print(sel_table)
            
            sel = safe_input(f"[bold {DC_HIGHLIGHT}]Select PAK: [/]").strip()
            if sel == '0' or not sel.isdigit(): continue
            
            try:
                pak_file = pak_files[int(sel) - 1]
                pak = TencentPakFile(pak_file)
                f_size = pak_file.stat().st_size
                stats = {
                    "files_processed": len(pak._files),
                    "compressed_count": sum(1 for e in pak._files if e.compression_method != 0),
                    "encrypted_count": sum(1 for e in pak._files if e.encrypted),
                    "original_size": f_size, "new_size": f_size,
                    "orig_index_sha": pak._pak_info.index_hash.hex() if hasattr(pak._pak_info.index_hash, 'hex') else str(pak._pak_info.index_hash),
                    "new_index_sha": pak._pak_info.index_hash.hex() if hasattr(pak._pak_info.index_hash, 'hex') else str(pak._pak_info.index_hash),
                    "version": pak._pak_info.version, "force_crc": True, "size_match": True
                }
                print_forensic_dashboard(stats, pak_file.name, title_text="ANALYZE REPORT")
            except Exception as e:
                console.print(f"[bold {DC_RED}]Error: {e}[/]")
            
            safe_input('\nPress Enter...')

        elif choice == '0':
            break
        else:
            console.print(f"[{DC_RED}]Invalid choice![/]")
            time.sleep(1)

def main_menu():
    data_path = get_base_dir()
    ensure_directories(data_path)

    while True:
        print_banner()
        print_user_profile()
        print_main_menu()

        choice = safe_input(f'[bold {DC_HIGHLIGHT}]ENTER YOUR CHOICE: [/]').strip()

        # ============ OPTION 1: UNPACK ============
        if choice == '1':
            pak_dir = data_path / "PAK"
            if not pak_dir.exists():
                console.print(f"[bold {DC_RED}]ERROR: PAK folder not found at {pak_dir}[/]")
                safe_input('\nPress Enter to continue...')
                continue

            pak_file, _ = display_file_selector("Available .pak files to UNPACK:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter to continue...')
                continue

            try:
                console.print(f'[bold {DC_HIGHLIGHT}]Unpacking {pak_file.name}...[/]')
                pak = TencentPakFile(pak_file)
                unpack_root = data_path / "UNPACK" / pak_file.stem

                start_time = time.time()
                total_uncompressed = sum(e.uncompressed_size for e in pak._files if e.uncompressed_size)

                success, ext_counts = pak.dump(unpack_root)
                time_taken = time.time() - start_time

                if success:
                    # 1. File Types Table
                    table_types = Table(title="Asset Distribution", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
                    table_types.add_column("Type", style="bold white")
                    table_types.add_column("Count", style=f"bold {DC_HIGHLIGHT}", justify="right")

                    total = 0
                    for ext, count in sorted(ext_counts.items(), key=lambda x: x[1], reverse=True):
                        table_types.add_row(ext, str(count))
                        total += count

                    # 2. Metadata Table
                    enc_methods = sorted({pak._get_method_str(e.encryption_method, e.encrypted) for e in pak._files})
                    comp_methods = sorted({pak._get_method_str(e.compression_method, False) for e in pak._files})

                    table_meta = Table(title="PAK Metadata", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
                    table_meta.add_column("Property", style="bold white")
                    table_meta.add_column("Value", style=f"bold {DC_HIGHLIGHT}")
                    table_meta.add_row("Encryption", ", ".join(enc_methods) or "NONE")
                    table_meta.add_row("Compression", ", ".join(comp_methods) or "NONE")
                    table_meta.add_row("Version", str(pak._pak_info.version))

                    # 3. Stats Table
                    table_stats = Table(title="Operation Stats", box=HEAVY_EDGE, border_style=DC_HIGHLIGHT)
                    table_stats.add_column("Metric", style="bold white")
                    table_stats.add_column("Value", style=f"bold {DC_GREEN}")
                    table_stats.add_row("Uncompressed", human_size(total_uncompressed))
                    table_stats.add_row("Time Taken", f"{time_taken:.2f}s")
                    table_stats.add_row("Total Files", str(total))

                    # Dashboard using grid for better control
                    grid = Table.grid(expand=True)
                    grid.add_column(ratio=1)
                    grid.add_column(ratio=1)

                    # Row 1: Asset Dist & Metadata
                    grid.add_row(table_types, table_meta)
                    # Row 2: Stats & Status
                    grid.add_row(table_stats, Align.center(Text("\n► OPERATION COMPLETE ◄", style=f"bold {DC_GREEN}"), vertical="middle"))

                    dashboard = Group(
                        grid,
                        Text(""),
                        Align.center(Text(f"► TARGET PATH: {unpack_root} ◄", style=f"bold {DC_HIGHLIGHT}"))
                    )

                    console.print(Panel(
                        dashboard,
                        title=f"[bold black on {DC_HIGHLIGHT}] KUNALYT0 DASHBOARD [/]",
                        border_style=DC_HIGHLIGHT,
                        box=HEAVY_EDGE,
                        padding=(1, 1),
                    ))
                else:
                    console.print(f'[{DC_ORANGE}]Partial extraction -- stopped by user.[/]')
            except Exception as e:
                console.print(f'[bold {DC_RED}]Error: {escape(str(e))}[/]')
                import traceback
                traceback.print_exc()

            safe_input('\nPress Enter to continue...')

        # ============ OPTION 2: INJECT ============
        elif choice == '2':
            pt = data_path / "PAK TOOL"
            pak_dir = pt / "PAK"
            edit_dir = pt / "EDIT"
            result_dir = pt / "RESULT"

            pak_file, _ = display_file_selector("Available .pak files to INJECT INTO:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter...')
                continue

            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                console.print(f'[bold {DC_RED}]ERROR: No files in PAK TOOL/EDIT folder.[/]')
                safe_input('\nPress Enter...')
                continue

            console.print()
            console.print(f'[bold {DC_HIGHLIGHT}]Encrypt with SM4?[/]')
            enc_choice = safe_input(f'[bold {DC_HIGHLIGHT}]Encrypt injected files? (Y/n): [/]').strip().lower()
            protect_new = enc_choice not in ('n', 'no')

            try:
                console.print(f'[bold {DC_HIGHLIGHT}]Injecting files into {pak_file.name}...[/]')
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name

                result = inject_edit_files(pak, edit_dir, output_pak, protect_new=protect_new, sm4_type=47)
                
                if len(result) == 3:
                    edited, added, stats = result
                    
                    # 1. Main Forensic Dashboard
                    print_forensic_dashboard(stats, output_pak, title_text="INJECTION FORENSIC ANALYSIS")
                    
                    # 2. Unique File Details Table
                    log_table = Table(
                        title=f"[bold black on {DC_HIGHLIGHT}] 📋 INJECTION FILE DETAILS [/]",
                        box=HEAVY_EDGE,
                        border_style=DC_HIGHLIGHT,
                        expand=True
                    )
                    log_table.add_column("File Name", style=f"bold {DC_TEXT}", ratio=3)
                    log_table.add_column("Action", justify="center", style="bold")
                    log_table.add_column("Encryption", style=f"bold {DC_ORANGE}", justify="center", ratio=1)
                    log_table.add_column("Compression", style=f"dim {DC_DIM}", justify="center")
                    log_table.add_column("Size", justify="right", style=f"bold {DC_HIGHLIGHT}")

                    for log in stats.get("file_logs", []):
                        action_color = DC_GREEN if "EDITED" in log["action"] else DC_CYAN
                        log_table.add_row(
                            log["name"],
                            f"[{action_color}]{log['action']}[/]",
                            log["encryption"],
                            log["compression"],
                            human_size(log["size"])
                        )
                    
                    console.print(log_table)
                    
                    # 3. Unique Success Badge
                    console.print(Panel(
                        Align.center(Text.from_markup(
                            f"[bold {DC_GREEN}]✨ INJECTION SUCCESSFUL ✨[/]\n\n"
                            f"  [bold {DC_HIGHLIGHT}]Total Modified:[/] {edited + added} files\n"
                            f"  [bold {DC_HIGHLIGHT}]Output:[/] {output_pak.name}"
                        )),
                        border_style=DC_GREEN,
                        box=DOUBLE_EDGE,
                        padding=(1, 4)
                    ))
                else:
                    # Fallback just in case
                    edited, added = result
                    console.print(f'[bold {DC_HIGHLIGHT}]Edited: {edited} files | Added: {added} files[/]')
            except Exception as e:
                console.print(f'[bold {DC_RED}]Inject failed: {e}[/]')
                import traceback
                traceback.print_exc()
            safe_input('\nPress Enter...')

        # ============ OPTION 3: REPACK FULL REBUILD ============
        elif choice == '3':
            pt = data_path / "PAK TOOL"
            pak_dir = pt / "PAK"
            edit_dir = pt / "EDIT"
            result_dir = pt / "RESULT"

            pak_file, _ = display_file_selector("Available .pak files to REPACK:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter...')
                continue

            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                console.print(f'[bold {DC_RED}]ERROR: No files in EDIT folder.[/]')
                safe_input('\nPress Enter...')
                continue

            csv_path_map = None
            csv_choice = safe_input('[bold yellow]Load CSV for new files? (y/n, default=y): [/]').strip().lower()
            if csv_choice not in ('n', 'no'):
                build_csv_dir = data_path / "BUILD_PAK" / "CSV"
                if download_csv_files(build_csv_dir):
                    selected_csv, is_bgmi, game_label = _select_csv_source(build_csv_dir)
                    if selected_csv:
                        file_path_map = _load_csv_path_map(selected_csv)
                        resolved_files, _unresolved = _resolve_paths_from_csv(edit_dir, file_path_map, is_bgmi)
                        csv_path_map = {p.name: rp for p, rp in resolved_files}
                        console.print(f'[bold {DC_HIGHLIGHT}]CSV: {len(csv_path_map)} paths resolved[/]')

            try:
                console.print(f'[bold {DC_HIGHLIGHT}]Repacking {pak_file.name} (Full Rebuild)...[/]')
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                force_bypass = console.input("[bold yellow]Force Original Hash Bypass? (y/n): [/]").strip().lower() in ('y', 'yes')
                count, stats = repack_pak_file_full(pak, edit_dir, output_pak, force_crc=force_bypass, force_size=force_bypass, csv_path_map=csv_path_map)
                if stats:
                    print_forensic_dashboard(stats, output_pak, title_text="REPACK FORENSIC ANALYSIS", force_safe=force_bypass)
                else:
                    console.print(f'[bold {DC_HIGHLIGHT}]Repacked {count} files![/]')
            except Exception as e:
                console.print(f'[bold {DC_RED}]Repack failed: {e}[/]')
                import traceback
                traceback.print_exc()
            safe_input('\nPress Enter...')

        # ============ OPTION 4: REPACK TO PATH ============
        elif choice == '4':
            pt = data_path / "PAK TOOL"
            pak_dir = pt / "PAK"
            edit_dir = pt / "EDIT"
            result_dir = pt / "RESULT"
            build_csv_dir = data_path / "BUILD_PAK" / "CSV"

            pak_file, _ = display_file_selector("Available .pak files to REPACK TO PATH:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter...')
                continue

            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                console.print(f'[bold {DC_RED}]ERROR: No files in EDIT folder.[/]')
                safe_input('\nPress Enter...')
                continue

            console.print()
            method_table = Table(
                title=f"[bold {DC_HIGHLIGHT}]Path Method[/]",
                box=DOUBLE_EDGE, border_style=DC_BORDER,
                header_style=f"bold black on {DC_HIGHLIGHT}",
            )
            method_table.add_column("OPT", justify="center", style=f"bold {DC_HIGHLIGHT}", width=6)
            method_table.add_column("METHOD", style=f"bold {DC_TEXT}")
            method_table.add_column("DESCRIPTION", style=f"{DC_DIM}")
            method_table.add_row("1", "Manual Path", "Type path yourself (advanced)")
            method_table.add_row("2", "CSV Auto", "CSV se auto-resolve (no typing)")
            method_table.add_row("0", f"[{DC_RED}]BACK[/]", "[dim]Cancel[/dim]")
            console.print(method_table)

            method_sel = safe_input(f'[bold {DC_HIGHLIGHT}]Select method (0/1/2): [/]').strip()

            if method_sel == "1":
                console.print()
                console.print(Panel(
                    f"[bold {DC_HIGHLIGHT}]Enter the target path inside the PAK:[/]\n"
                    f"[dim {DC_DIM}]Example: Content/Lua/GameLua/Mod/BRMod/Gameplay/Core[/dim {DC_DIM}]",
                    border_style=DC_BORDER, box=ROUNDED
                ))
                target_path = safe_input(f'[bold {DC_HIGHLIGHT}]Path: [/]').strip()

                if not target_path:
                    console.print(f'[bold {DC_RED}]No path provided![/]')
                    safe_input('\nPress Enter...')
                    continue

                target_path = target_path.replace('\\', '/').strip('/')

                try:
                    console.print(f'[bold {DC_HIGHLIGHT}]Adding files to {target_path}...[/]')
                    pak = TencentPakFile(pak_file)
                    output_pak = result_dir / pak_file.name
                    count, stats = repack_pak_file_full(pak, edit_dir, output_pak, target_path, force_add=True)

                    if count > 0:
                        console.print()
                        if stats:
                            print_forensic_dashboard(stats, output_pak, title_text="REPACK TO PATH (MANUAL) FORENSIC ANALYSIS")
                        
                        console.print(Panel(
                            Align.center(Text.from_markup(
                                f"[bold {DC_GREEN}]✨ REPACK TO PATH SUCCESSFUL ✨[/]\n\n"
                                f"  [bold {DC_HIGHLIGHT}]Total Modified:[/] {count} files\n"
                                f"  [bold {DC_HIGHLIGHT}]Output:[/] {output_pak.name}"
                            )),
                            border_style=DC_GREEN,
                            box=DOUBLE_EDGE,
                            padding=(1, 4)
                        ))
                except Exception as e:
                    console.print(f'[bold {DC_RED}]Repack failed: {e}[/]')
                    import traceback
                    traceback.print_exc()
                safe_input('\nPress Enter...')

            elif method_sel == "2":
                try:
                    console.print(f'[bold {DC_HIGHLIGHT}]CSV AUTO mode: resolving paths...[/]')
                    pak = TencentPakFile(pak_file)
                    output_pak = result_dir / pak_file.name
                    count, stats = repack_to_path_with_csv(pak, edit_dir, build_csv_dir, output_pak)

                    if count > 0:
                        console.print()
                        if stats:
                            print_forensic_dashboard(stats, output_pak, title_text="REPACK TO PATH (CSV) FORENSIC ANALYSIS")
                            
                            # UNIQUE FILE DETAILS TABLE
                            log_table = Table(
                                title=f"[bold black on {DC_HIGHLIGHT}] 📋 INJECTION FILE DETAILS [/]",
                                box=HEAVY_EDGE,
                                border_style=DC_HIGHLIGHT,
                                expand=True
                            )
                            log_table.add_column("File Name", style=f"bold {DC_TEXT}", ratio=3)
                            log_table.add_column("Action", justify="center", style="bold")
                            log_table.add_column("Encryption", style=f"bold {DC_ORANGE}", justify="center", ratio=1)
                            log_table.add_column("Compression", style=f"dim {DC_DIM}", justify="center")
                            log_table.add_column("Size", justify="right", style=f"bold {DC_HIGHLIGHT}")

                            for log in stats.get("file_logs", []):
                                action_color = DC_GREEN if "EDITED" in log["action"] else DC_CYAN
                                log_table.add_row(
                                    log["name"],
                                    f"[{action_color}]{log['action']}[/]",
                                    log["encryption"],
                                    log["compression"],
                                    human_size(log["size"])
                                )
                            console.print(log_table)
                        
                        console.print(Panel(
                            Align.center(Text.from_markup(
                                f"[bold {DC_GREEN}]✨ CSV AUTO REPACK SUCCESSFUL ✨[/]\n\n"
                                f"  [bold {DC_HIGHLIGHT}]Total Modified:[/] {count} files\n"
                                f"  [bold {DC_HIGHLIGHT}]Output:[/] {output_pak.name}"
                            )),
                            border_style=DC_GREEN,
                            box=DOUBLE_EDGE,
                            padding=(1, 4)
                        ))
                except Exception as e:
                    console.print(f'[bold {DC_RED}]CSV auto failed: {e}[/]')
                    import traceback
                    traceback.print_exc()
                safe_input('\nPress Enter...')

        # ============ OPTION 5: PROTECT PAK ============
        elif choice == '5':
            pt = data_path / "PAK TOOL"
            pak_dir = pt / "PAK"
            result_dir = pt / "RESULT"

            pak_file, _ = display_file_selector("Available .pak files to PROTECT:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter...')
                continue

            console.print()
            console.print(f'[bold {DC_HIGHLIGHT}]PROTECT MODE[/]')
            console.print(f'[dim {DC_DIM}]Re-encrypts EVERY file with SM4.[/dim {DC_DIM}]')
            confirm = safe_input(f'[bold {DC_RED}]Start PROTECT? (yes/no): [/]').strip().lower()

            if confirm not in ('y', 'yes'):
                console.print(f'[{DC_ORANGE}]Cancelled.[/]')
                safe_input('\nPress Enter...')
                continue

            try:
                console.print(f'[bold {DC_HIGHLIGHT}]Protecting {pak_file.name}...[/]')
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                result = protect_pak_file(pak, output_pak, sm4_type=47)

                if isinstance(result, tuple) and len(result) == 3:
                    protected, skipped, stats = result
                    print_forensic_dashboard(stats, output_pak, title_text="PROTECT PAK FORENSIC ANALYSIS")
                    
                    # Success Badge
                    console.print(Panel(
                        Align.center(Text.from_markup(
                            f"[bold {DC_GREEN}]🛡️ PROTECT MODE SUCCESSFUL 🛡️[/]\n\n"
                            f"  [bold {DC_HIGHLIGHT}]Protected Files:[/] {protected}\n"
                            f"  [bold {DC_HIGHLIGHT}]Skipped Files:[/] {skipped}\n"
                            f"  [bold {DC_HIGHLIGHT}]Output:[/] {output_pak.name}"
                        )),
                        border_style=DC_GREEN,
                        box=DOUBLE_EDGE,
                        padding=(1, 4)
                    ))
                else:
                    protected, skipped = result
                    console.print(f'[bold {DC_HIGHLIGHT}]PROTECTED: {protected} files (SM4)[/]')
                    console.print(f'[{DC_ORANGE}]Skipped: {skipped} files[/]')
                    console.print(f'[bold {DC_HIGHLIGHT}]Output: {output_pak}[/]')
            except Exception as e:
                console.print(f'[bold {DC_RED}]Protect failed: {e}[/]')
                import traceback
                traceback.print_exc()
            safe_input('\nPress Enter...')

        # ============ OPTION 6: BUILD NEW PAK ============
        elif choice == '6':
            stats = build_new_pak(data_path)
            if stats:
                print_forensic_dashboard(stats, stats.get("output_path", "New PAK Generated"), title_text="BUILD FORENSIC ANALYSIS")
                
                # UNIQUE FILE DETAILS TABLE
                if "file_logs" in stats:
                    log_table = Table(
                        title=f"[bold black on {DC_HIGHLIGHT}] 📋 BUILD FILE DETAILS [/]",
                        box=HEAVY_EDGE,
                        border_style=DC_HIGHLIGHT,
                        expand=True
                    )
                    log_table.add_column("File Name", style=f"bold {DC_TEXT}", ratio=3)
                    log_table.add_column("Action", justify="center", style="bold")
                    log_table.add_column("Encryption", style=f"bold {DC_ORANGE}", justify="center", ratio=1)
                    log_table.add_column("Compression", style=f"dim {DC_DIM}", justify="center")
                    log_table.add_column("Size", justify="right", style=f"bold {DC_HIGHLIGHT}")

                    for log in stats.get("file_logs", []):
                        action_color = DC_CYAN
                        log_table.add_row(
                            log["name"],
                            f"[{action_color}]{log['action']}[/]",
                            log["encryption"],
                            log["compression"],
                            human_size(log["size"])
                        )
                    console.print(log_table)
                
                # Success Badge
                console.print(Panel(
                    Align.center(Text.from_markup(
                        f"[bold {DC_GREEN}]✨ BUILD PAK SUCCESSFUL ✨[/]\n\n"
                        f"  [bold {DC_HIGHLIGHT}]Total Files Built:[/] {stats['files_processed']}\n"
                        f"  [bold {DC_HIGHLIGHT}]Output:[/] {Path(stats.get('output_path', '')).name}"
                    )),
                    border_style=DC_GREEN,
                    box=DOUBLE_EDGE,
                    padding=(1, 4)
                ))
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 7: DELETE FOLDER ============
        elif choice == '7':
            delete_folder(data_path)
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 8: MINI SKIN TOOL ============
        elif choice == '8':
            mini_skin_tool_main(data_path)
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 9: ZSDIC SKIN TOOL ============
        elif choice == '9':
            zsdic_skin_tool_main(data_path)
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 10: LUA TOOL ============
        elif choice == '10':
            run_lua_tool(data_path)
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 11: BLACK TOOL ============
        elif choice == '11':
            black_tool_main()
            safe_input('\nPress Enter to continue...')

        # ============ OPTION 12: ANALYZE PAK ============
        elif choice == '12':
            pak_dir = data_path / "PAK"
            if not pak_dir.exists():
                console.print(f"[bold {DC_RED}]ERROR: PAK folder not found at {pak_dir}[/]")
                safe_input('\nPress Enter to continue...')
                continue

            pak_file, _ = display_file_selector("Select PAK to analyze:", pak_dir)
            if not pak_file:
                safe_input('\nPress Enter...')
                continue

            console.print(f'[bold {DC_HIGHLIGHT}]Scanning {pak_file.name}...[/]')
            pak = TencentPakFile(pak_file)
            f_size = pak_file.stat().st_size
            stats = {
                "files_processed": len(pak._files),
                "compressed_count": sum(1 for e in pak._files if e.compression_method != 0),
                "encrypted_count": sum(1 for e in pak._files if e.encrypted),
                "original_size": f_size,
                "new_size": f_size,
                "orig_index_sha": pak._pak_info.index_hash.hex() if hasattr(pak._pak_info.index_hash, 'hex') else str(pak._pak_info.index_hash),
                "new_index_sha": pak._pak_info.index_hash.hex() if hasattr(pak._pak_info.index_hash, 'hex') else str(pak._pak_info.index_hash),
                "version": pak._pak_info.version,
                "force_crc": True,
                "size_match": True
            }
            print_forensic_dashboard(stats, pak_file.name, title_text="ANALYZE REPORT")
            safe_input('\nPress Enter...')

          # ============ OPTION 13: AUTO-EXTRACT KEYS ============
        elif choice == '13':
            so_file, _ = display_file_selector("Select .so file to scan:", data_path, "*.so")
            if not so_file:
                safe_input('\nPress Enter...')
                continue

            # --- UI Setup ---
            status_text = Text("Initializing scan...", style=f"bold {DC_ORANGE}")
            all_found = []

            def update_ui(stats):
                status_text.plain = (
                    f"Scanning: {stats['offset_mb']} MB / {stats['total_mb']} MB | "
                    f"Keys Found: {stats['total_keys']} | Speed: {stats['speed']} MB/s"
                )

                for key in stats.get('new_keys', []):
                    all_found.append(key)

                keys_table = Table(
                    title="[bold #00FFCC] LIVE KEY EXTRACTION [/]",
                    box=HEAVY_EDGE, border_style=DC_HIGHLIGHT, expand=True
                )
                keys_table.add_column("Offset", style="dim")
                keys_table.add_column("Type", style="bold white")
                keys_table.add_column("Key Value", style=f"bold {DC_HIGHLIGHT}")
                for k in all_found[-10:]:
                    keys_table.add_row(k["offset"], k["type"], k["value"])

                live.update(Group(
                    Panel(
                        status_text,
                        title="[bold black on #00FFCC] SCANNING ENGINE [/]",
                        border_style=DC_HIGHLIGHT,
                    ),
                    keys_table,
                ))

            with Live(console=console, refresh_per_second=15) as live:
                finder = SM4KeyFinder()
                keys = finder.scan_file(so_file, progress_cb=update_ui)

            console.print(f"\n[bold {DC_GREEN}]✅ Scan Complete! Found {len(keys)} keys.[/]\n")

            if not keys:
                console.print(f"[bold {DC_RED}]❌ No keys found![/]")
                safe_input('\nPress Enter...')
                continue

            # --- LOAD EXISTING KEYS FROM SCRIPT ---
            SCRIPT_EXISTING_KEYS = set()
            try:
                with open(__file__, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].lstrip().startswith('SM4_SECRET_NEW = ['):
                        i += 1
                        while i < len(lines):
                            cur = lines[i].strip()
                            if cur and cur[0] == ']':
                                break
                            key = cur.replace("'", "").replace('"', "").replace(",", "").strip()
                            if len(key) == 20:
                                SCRIPT_EXISTING_KEYS.add(key)
                            i += 1
                    i += 1
            except Exception:
                pass

            # --- SHOW ALL FOUND KEYS ---
            final_table = Table(
                title=f"[bold black on {DC_GREEN}] 📊 FULL SCAN RESULTS ({len(keys)} Keys) [/]",
                box=DOUBLE_EDGE, border_style=DC_GREEN, expand=True
            )
            final_table.add_column("S.NO", justify="center", style="dim", width=6)
            final_table.add_column("Offset", style="bold cyan")
            final_table.add_column("Type", style="bold white")
            final_table.add_column("Key Value", style=f"bold {DC_HIGHLIGHT}")
            final_table.add_column("Status", justify="center", style="bold")

            new_keys = []
            matched_count = 0

            for idx, k_dict in enumerate(keys, 1):
                key_val = k_dict["value"]
                key_type = k_dict["type"]
                key_off = k_dict["offset"]

                if key_val in SCRIPT_EXISTING_KEYS:
                    status = f"[bold {DC_GREEN}]✔ Existing[/]"
                    matched_count += 1
                else:
                    status = f"[bold {DC_ORANGE}]✦ NEW[/]"
                    new_keys.append(key_val)

                final_table.add_row(f"#{idx:03d}", key_off, key_type, key_val, status)

            console.print(final_table)
            console.print(
                f"\n[bold {DC_GREEN}]✔ Existing Keys: {matched_count}[/] │ "
                f"[bold {DC_ORANGE}]✦ New Keys: {len(new_keys)}[/]"
            )

            # --- ADD NEW KEYS ---
            if new_keys:
                confirm = console.input(
                    f"\n[bold {DC_GREEN}]✅ Add {len(new_keys)} new key(s) to SM4_SECRET_NEW? [y/n] (y): [/]"
                ).strip().lower()
                if confirm in ['', 'y', 'yes']:
                    try:
                        with open(__file__, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                        all_keys = sorted(SCRIPT_EXISTING_KEYS | set(new_keys))
                        new_lines = []
                        i = 0
                        while i < len(lines):
                            line = lines[i]
                            if line.lstrip().startswith('SM4_SECRET_NEW = ['):
                                indent = len(line) - len(line.lstrip())
                                ind = ' ' * indent
                                ind2 = ' ' * (indent + 4)
                                new_lines.append(f"{ind}SM4_SECRET_NEW = [\n")
                                for k in all_keys:
                                    new_lines.append(f"{ind2}'{k}',\n")
                                new_lines.append(f"{ind}]\n")
                                i += 1
                                while i < len(lines):
                                    stripped = lines[i].strip()
                                    if stripped and stripped[0] == ']':
                                        i += 1
                                        break
                                    i += 1
                                continue
                            new_lines.append(line)
                            i += 1
                        with open(__file__, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                        console.print(
                            f"\n[bold {DC_GREEN}]✨ {len(new_keys)} new keys added successfully![/]"
                        )
                    except Exception as e:
                        console.print(f"\n[bold {DC_RED}]❌ Failed to update: {e}[/]")

            safe_input('\nPress Enter...')

        # ============ OPTION 14: OBB ALL-IN-ONE TOOL ============
        elif choice == '14':
            obb_pak_tool_menu(data_path)

        # ============ OPTION 15: AUTO MAKING MODS ============
        elif choice == '15':
            handle_auto_making_mods(data_path)
            safe_input('\nPress Enter...')

        # ============ OPTION 0: EXIT ============
        elif choice == '0':
            console.print(f"[bold {DC_HIGHLIGHT}]Goodbye![/]")
            time.sleep(2)
            break

        else:
            console.print(f'[bold {DC_RED}]Invalid choice![/]')
            time.sleep(2)


# =====================================================================
# ENTRY POINT
# =====================================================================

def auto_install_dependencies():
    import subprocess, sys
    try:
        import requests, rich, Crypto
    except ImportError:
        print("[*] Installing required dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "rich", "pycryptodome", "zstandard", "colorama", "termcolor", "pytz"], check=False)
        print("[*] Dependencies installed. Please restart the tool.")
        sys.exit(0)

if __name__ == '__main__':
    auto_install_dependencies()
    try:
        auto_termux_setup()
        if not run_security_check():
            console.print(f"\n[bold {DC_RED}]Security check failed! Access denied.[/]")
            time.sleep(3)
            sys.exit(1)
            
        if premium_login_screen() == "KUNALYT0_KEYED":
            main_menu()
        else:
            console.print(f"\n[bold {DC_RED}]Login failed![/]")
            sys.exit(1)
    except KeyboardInterrupt:
        console.print(f'\n[bold {DC_HIGHLIGHT}]Interrupted. Exiting...[/]')
        sys.exit(0)
    except Exception as e:
        console.print(f'[bold {DC_RED}]ERROR:[/] {escape(str(e))}')
        import traceback
        traceback.print_exc()
        safe_input('\nPress Enter to exit...')
        sys.exit(1)


# =====================================================================
# END OF PART 9 - COMPLETE TOOL
# =====================================================================