#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of svmodule. See the root README for further
# informations.
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
# Copyright (C) 2013-2019 Christophe Clienti

from svmodule.printers.instance import Instance
from svmodule.printers.logic import Logic
from .printerbase import PrinterBase
from .align import vertical_align_string

class Testbench(PrinterBase):
    """Returns simple testbench with no initial block
    """

    def get_logic(self):
        return Logic(self.pmod, self.isize, **self.properties).getstr()
    
    def get_instance(self):
        return Instance(self.pmod, self.isize, **self.properties).getstr()

    def getstr(self):
        idt = ' '*self.isize
        modname = self.pmod['name']
        strval = 'module tb_' + modname + ';\n'

        # Insert logic
        strval += '\n' + self.get_logic()

        # Insert module instance
        strval += '\n' + self.get_instance()
        strval += '\n' + 'endmodule'
        return strval