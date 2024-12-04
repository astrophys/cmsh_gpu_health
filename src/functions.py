import os
import glob
from classes import Node


def read_data_dir(path : str = None):
    """Read directory with ALL node*_gputemp_gpu*.txt files

    Args :
        path = path to directory with node*_gputemp_gpu*.txt file

    Returns

    Raises

    """
    fileL = os.listdir(path)
    # Gather list of nodes
    nodenameL = []
    for fin in fileL:
        if 'collect_data.sh' in fin:
            continue
        nodename = fin.split('_')[0]
        if nodename not in nodenameL:
            nodenameL.append(nodename)
    # Only do temperature
    for nodename in nodenameL:
        gpupathL = glob.glob("{}/{}_gputemp_*".format(path,nodename))
        node = Node(gpupathL=gpupathL)

    print('done')

