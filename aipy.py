#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Scripts for AI.
""" 

import sys

from aparser import ProgramArguments
import agents
    
def main(progargs):
    """Main function.
    
    Args:
        progargs: Program arguments already processed.

    """    
    
    agents.launch()

        
    print "Program finished."
    
    return 0

# Where all begins ...
if __name__ == "__main__":
    
    # Object to process the program arguments.
    progargs = ProgramArguments()
    
    sys.exit(main(progargs))      