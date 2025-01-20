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


class Temp :
    """Class that maps entry in a node*_gputemp_gpu*.txt"""

    def __init__(self, line : str = None):

        """Initialize Temp Class

        Args :
            line = line with date and temp in node*_gputemp_gpu*.txt files

        Returns :
            Temp class

        Raises :
            ValueError when unexpected line format is encountered

        """
        strL = line.split()
        datestr = " ".join(strL[0:2])
        datestr = datestr.split('.')[0]
        try :
            self.date = datetime.datetime.strptime(datestr, "%Y/%m/%d %H:%M:%S")
            self.temp = float(strL[2])
        except ValueError :
            ## If no data, set to invalid value
            if 'no data' in line.lower():
                self.temp = -1
            else :
                raise ValueError("ERROR!!! Parsing line = {}".format(line))


class Gpu :
    """Class that maps to a single Slurm job"""

    def __init__(self, gpupath : str = None):

        """Initialize Gpu Class

        Args :

        Returns :

        Raises :

        """
        fin = open(gpupath, 'r')
        gidx = gpupath.split("/")[-1]
        gidx = gidx.split(".")[0]
        gidx = int(gidx.split("gpu")[-1])
        self.gidx = gidx
        self.tempL = []
        self.healthy = True
        for line in fin:
            if line[0] == '#':
                strL = line.split()
                datestr = " ".join(strL[4:8])
                datestr = datestr.split('.')[0]

                # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
                if 'Start' in line :
                    self.start = datetime.datetime.strptime(datestr, "%b %d %H:%M:%S %Y")
                if 'End' in line :
                    self.end= datetime.datetime.strptime(datestr, "%b %d %H:%M:%S %Y")
            else :
                temp = Temp(line)
                if temp.temp > 80 :
                    self.healthy = False
                self.tempL.append(temp)
        fin.close()


class Node :
    """Take list of gputemp files, read in and allocate gpus"""

    def __init__(self, gpupathL : str = None):

        """Initialize Node Class,

        Args :
            gpuL = list of node*_gputemp_*.txt files, used to allocate Gpu class and
                   read the data

        Returns :

        Raises :

        """
        self.gpuL = []
        name = gpupathL[0].split("/")[-1]
        name = name.split("_")[0]
        self.name = name
        for gpupath in gpupathL:
            gpu = Gpu(gpupath)
            if gpu.healthy is False :
                print("{} : gpu{}".format(self.name, gpu.gidx))
            self.gpuL.append(gpu)


