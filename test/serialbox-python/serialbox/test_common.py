#!/usr/bin/python3
# -*- coding: utf-8 -*-
##===-----------------------------------------------------------------------------*- Python -*-===##
##
##                                   S E R I A L B O X
##
## This file is distributed under terms of BSD license. 
## See LICENSE.txt for more information.
##
##===------------------------------------------------------------------------------------------===##
##
## Unittest of the common utility functions.
##
##===------------------------------------------------------------------------------------------===##

from serialbox import get_library, register_library
import unittest

class TestCommon(unittest.TestCase):
    def test_get_library(self):
        lib = get_library()
        register_library(lib)

if __name__ == "__main__":
    unittest.main()
