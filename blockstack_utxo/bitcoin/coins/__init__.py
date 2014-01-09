# -*- coding: utf-8 -*-
"""
    Coins
    ~~~~~

    :copyright: (c) 2013 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.2.2'

from .entropy import random_secret_exponent
from .passphrase import random_256bit_passphrase, random_160bit_passphrase
from .b58check import b58check_encode, b58check_decode, b58check_unpack, \
	b58check_version_byte, is_b58check
from .utils import is_hex, is_secret_exponent, is_256bit_hex_string, \
    is_wif_pk, is_b58check_address, extract_pk_as_int

from .keypair import *