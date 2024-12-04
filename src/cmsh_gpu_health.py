# Author : Ali Snedden
# Date   : 11/15/24
# Goals (ranked by priority) :
#
# Refs :
#   a)
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
import os
import sys
import random
import argparse
import datetime
import operator
import numpy as np
import pandas as pd
import matplotlib
#matplotlib.use('tkagg')        # Linux
matplotlib.use('qtagg')        # Linux
from classes import User
import matplotlib.pyplot as plt
from plot_funcs import make_pie
from plot_funcs import plot_time_series
from functions import make_autopct
from functions import parse_sacct_file
from functions import is_job_in_time_range


# Expects data like : sacct --allusers -P -S 2024-08-01 --format="jobid,jobname,user,nodelist,elapsedraw,alloccpus,cputimeraw,maxrss,state,start,end,reqtres" > sacct_2024-08-01.txt

# Run via
#    python -m pdb src/bcm_accounting_plots.py --path data/sacct_2024-05-01_to_2024-10-31.txt --start 2024-05-01T00:00:00 --end 2024-11-01T00:00:00 --plottyp time-series --users all
def main():
    """Loads the sacct .

    Args

        N/A

    Returns

    Raises

    """

    parser = argparse.ArgumentParser(
                    description="This generates plots from output of `sacct`")
    parser.add_argument('--path', metavar='path/to/data/dir', type=str,
                        help='Path to parsable sacct file')
    #parser.add_argument('--start', metavar='starttime', type=str,
    #                    help='Time in YYYY-MM-DDTHH:MM:SS format')
    #parser.add_argument('--end', metavar='endtime', type=str,
    #                    help='Time in YYYY-MM-DDTHH:MM:SS format')
    #parser.add_argument('--plottype', metavar='plottype', type=str,
    #                    help='Options : "histogram", "pie" or "time-series"')
    #parser.add_argument('--users', metavar='users', type=str,
    #                    help='Options : "all", "total" or "someuser"')
    #parser.add_argument('--plottype', metavar='plottype', type=str,
    #                    help='Options : "histogram", "pie" or "time-series"')
    args = parser.parse_args()
    path = args.path
    sys.exit(0)


if __name__ == "__main__":

    main()


