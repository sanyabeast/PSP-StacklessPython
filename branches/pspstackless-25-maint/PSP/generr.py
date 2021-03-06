#!/usr/bin/env python
#-*- coding: ISO-8859-1 -*-

#****h* /generr.py
#  NAME
#    generr -- Scan pspkerror.h for error names
#  COPYRIGHT
#
#  Copyright (C) 2005 J�r�me Laheurte <fraca7@free.fr>
#
# This library  is free software; you can  redistribute it and/or
# modify  it under  the terms  of the  GNU Lesser  General Public
# License as  published by  the Free Software  Foundation; either
# version  2.1 of  the License,  or  (at your  option) any  later
# version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY;  without even the implied warranty of
# MERCHANTABILITY or  FITNESS FOR A PARTICULAR  PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You  should have  received a  copy  of the  GNU Lesser  General
# Public License  along with this  library; if not, write  to the
# Free  Software Foundation,  Inc., 59  Temple Place,  Suite 330,
# Boston, MA 02111-1307 USA
#
#  CREATION DATE
#    29 Oct 2005
#***

"""

Scan pspkerror.h for error names

"""

__rcsid__ = '$Id$'

import os, re

def main():
    path = 'pspkerror.h'
    s = 0
    fp = file(path, 'r')
    rx = re.compile('SCE_KERNEL_ERROR_([A-Z0-9_]+)\s*=\s*0x([0-9a-fA-F]+)')
    ls = []

    for line in fp:
        mt = rx.search(line)
        if mt:
            ls.append((mt.group(1), int(mt.group(2), 16)))

    fp = file('psperror.c', 'w')
    fp.write('// Generated by generr.py. Do not edit.\n')
    fp.write('''

char* formatPSPError(int code)
{
    switch (code)
    {
''')
    for name, code in ls:
        fp.write('        case %dU:\n' % code)
        fp.write('            return "%s";\n' % name)
        fp.write('\n')

    fp.write('        default:\n')
    fp.write('            return "UNKNOWN_ERROR";\n')

    fp.write('    }\n}\n')

if __name__ == '__main__':
    main()
