# Author : Ali Snedden
# Date   : 11/15/24
#
# Copyright (C) 2024 Ali Snedden
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#
#
#
import os
import sys
import math
import random
import argparse
import datetime
import numpy as np
import pandas as pd
from collections import OrderedDict


class Measurable :
    """Class that maps to a single Slurm job"""

    def __init__(self, start : int = None, end : str = None, measurable : str = None):

        """Initialize Job Class

        Args :

        Returns :

        Raises :

        """
        # https://stackoverflow.com/a/5166588/4021436
        self.node = node
        self.gpu  = gpu
        self.user = user
        self.reqtres = reqtres
        # Set these PRIOR to parsing reqtres in case no GPUs were present
        self.ngpu       = 0
        self.gputimeraw = 0
        self.stepL = []
        self.externL = []
        self.batchL = []


class Gpu :
    """Class that maps to a single Slurm job"""

    def __init__(self, jobid : int = None, jobname : str = None, user : str = None,
                 reqtres : str = None):

        """Initialize Job Class

        Args :

        Returns :

        Raises :

        """


class Node :
    """Class that maps to a single Slurm job"""

    def __init__(self, jobid : int = None, jobname : str = None, user : str = None,
                 reqtres : str = None):

        """Initialize Job Class

        Args :

        Returns :

        Raises :

        """


