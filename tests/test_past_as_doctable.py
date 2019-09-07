# -*- coding: utf-8 -*-
#
# This file is part of svmodule. See the root README.md for further
# information.
#
# svmodule is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# svmodule is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with svmodule.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2019 Christophe Clienti

"""Test Printer classes."""

import unittest

from svmodule.moddict import ModDict
from svmodule.printer import Printer

from . import test_printers_inputs as inputs


class TestPastAsDocTable(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_doctable_0(self):
        """Test past as doctable with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        doctable = printer['DocTable']

        self.assertEqual(doctable, TEST_MODULE_0_REF)

    def test_past_as_doctable_1(self):
        """Test past as doctable with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        doctable = printer['DocTable']

        self.assertEqual(doctable, TEST_MODULE_1_REF)

    def test_past_as_doctable_2(self):
        """Test past as doctable with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        doctable = printer['DocTable']

        self.assertEqual(doctable, TEST_MODULE_2_REF)

    def test_past_as_doctable_3(self):
        """Test past as doctable with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=2)
        doctable = printer['DocTable']

        self.assertEqual(doctable, TEST_MODULE_3_REF)


TEST_MODULE_0_REF = (
    '=================  =======  ==============  ========================================\n'
    'Name               Type     Default value   Description\n'
    '=================  =======  ==============  ========================================\n'
    'add_extra_instr             1               \n'
    '-----------------  -------  --------------  ----------------------------------------\n'
    'add_select_instr            1               \n'
    '-----------------  -------  --------------  ----------------------------------------\n'
    'add_select_instr   string   "M144k,auto"    \n'
    '-----------------  -------  --------------  ----------------------------------------\n'
    'shorten_pipeline            0               \n'
    '=================  =======  ==============  ========================================\n'
    '\n'
    '==========  =========  =======  ========================================\n'
    'Name        I/O type   Range    Description\n'
    '==========  =========  =======  ========================================\n'
    'clk         input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'enable      input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'is_signed   input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'enacc       input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'sub_nadd    input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'selacc      input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'resetrs0    input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'rs0         input      [31:0]   \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'rs1         input      [31:0]   \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'imm         input      [31:0]   \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'mulmux      input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'selop0      input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'selop1      input      1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'selshift    input      [1:0]    \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'cmode       input      [1:0]    \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'opcode1     input      [2:0]    \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'opcode2     input      [2:0]    \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'out_en      output     1        \n'
    '----------  ---------  -------  ----------------------------------------\n'
    'out         output     [31:0]   \n'
    '==========  =========  =======  ========================================\n')


TEST_MODULE_1_REF = (
    '==============  =====  ==============  ========================================\n'
    'Name            Type   Default value   Description\n'
    '==============  =====  ==============  ========================================\n'
    'GEN1                   48              \n'
    '--------------  -----  --------------  ----------------------------------------\n'
    'GEN2                   45              \n'
    '--------------  -----  --------------  ----------------------------------------\n'
    'GEN3_WIDTH             $clog2(VALUE)   \n'
    '--------------  -----  --------------  ----------------------------------------\n'
    'DEFAULT_VAL_A          32\'b0           \n'
    '--------------  -----  --------------  ----------------------------------------\n'
    'DEFAULT_VAL_B   int    32\'b0           \n'
    '--------------  -----  --------------  ----------------------------------------\n'
    'DEFAULT_VAL_C                          \n'
    '==============  =====  ==============  ========================================\n'
    '\n'
    '================  ===================  ===========================  ========================================\n'
    'Name              I/O type             Range                        Description\n'
    '================  ===================  ===========================  ========================================\n'
    'reset_n           input logic          1                            \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'clock             input logic          1                            \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'test              input logic          [$clog2(GEN3_WIDTH+1)-1:0]   \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'clock2            input pkg::typedef   1                            \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'm_master          myinterface.master   1                            \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    's_slave           myinterface.slave    1                            \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'm_big_array       output logic         [1:0][2:0]                   \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'm_simple_array    output logic         [28:0][$clog2(GEN1):0]       \n'
    '----------------  -------------------  ---------------------------  ----------------------------------------\n'
    'm_simple_array3   output logic         [15:0]                       \n'
    '================  ===================  ===========================  ========================================\n')


TEST_MODULE_2_REF = (
    '==============  =====================  =======  ========================================\n'
    'Name            I/O type               Range    Description\n'
    '==============  =====================  =======  ========================================\n'
    'srst            input logic            1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'clk             input logic            1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'itf1            myinterface.slave      1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'itf2            myinterface.master     1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'insig1          input logic            1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'insig2          input logic            [31:0]   \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'insig3          input logic            [10:0]   \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'insig4          input logic            [7:0]    \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'outsig1         output logic           [47:0]   \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'outsig2         output logic           [15:0]   \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'another_srst    input logic            1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'another_clock   input logic            1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'oitf            otherinterface.slave   1        \n'
    '--------------  ---------------------  -------  ----------------------------------------\n'
    'outsig3         output logic           1        \n'
    '==============  =====================  =======  ========================================\n')


TEST_MODULE_3_REF = (
    '==============  =====================  ======  ========================================\n'
    'Name            I/O type               Range   Description\n'
    '==============  =====================  ======  ========================================\n'
    'srst            input logic            1       \n'
    '--------------  ---------------------  ------  ----------------------------------------\n'
    'clk             input logic            1       \n'
    '--------------  ---------------------  ------  ----------------------------------------\n'
    'another_srst    input logic            1       \n'
    '--------------  ---------------------  ------  ----------------------------------------\n'
    'another_clock   input logic            1       \n'
    '--------------  ---------------------  ------  ----------------------------------------\n'
    'oitf            otherinterface.slave   [2:0]   \n'
    '--------------  ---------------------  ------  ----------------------------------------\n'
    'outsig3         output logic           [1:0]   \n'
    '==============  =====================  ======  ========================================\n')


if __name__ == '__main__':
    unittest.main()
