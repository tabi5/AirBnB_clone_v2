#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
#
# Functions:
#   do_clean(number=0): Delete out-of-date archives.
#
# Args:
#   number (int): The number of archives to keep.
#                  Default is 0.
#
# Notes:
#   If number is 0 or 1, keeps only the most recent archive.
#   If number is 2, keeps the most and second-most recent archives, etc.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

     Args:
        number (int): The number of archives to keep.
                      Default is 0.

     Notes:
        If number is 0 or 1, keeps only the most recent archive.
        If number is 2, keeps the most and second-most recent archives, etc.
    """
    # variable to store the number of archives to keep
    num_archives = 1 if int(number) == 0 else int(number)

    # variable to store the local directory path
    local_dir_path = "versions"

    # variable to store the remote directory path
    remote_dir_path = "/data/web_static/releases"

    # Get the list of archives in the local directory
    local_archives = sorted(os.listdir(local_dir_path))

    # Remove the most recent archives from the list
    [local_archives.pop() for _ in range(num_archives)]

    # Delete the out-of-date archives in the local directory
    with lcd(local_dir_path):
        [local("rm ./{}".format(a)) for a in local_archives]

    # Get the list of archives in the remote directory
    remote_archives = run("ls -tr").split()

    # Filter the list to include only the archives
    remote_archives = [a for a in remote_archives if "web_static_" in a]

    # Remove the most recent archives from the list
    [remote_archives.pop() for _ in range(num_archives)]

    # Delete the out-of-date archives in the remote directory
    with cd(remote_dir_path):
        [run("rm -rf ./{}".format(a)) for a in remote_archives]

    return True
