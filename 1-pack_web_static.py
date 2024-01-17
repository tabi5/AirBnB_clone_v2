#!/usr/bin/python3
# Description: Fabfile to generate a .
# tgz archive from the contents of web_static.
#
# This script creates a compressed .
# tgz archive file from the contents of the web_static directory.
# The archive is saved in the "versions" directory with a timestamped filename.
#
# Function:
#   - do_pack: Creates a tar gzipped archive of the web_static directory.
#
# Parameters:
#   None
#
# Returns:
#   - file: The path to the generated archive file,
# or None if the operation fails.

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    try:
        dt = datetime.utcnow()
        dir_name = "versions"
        file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             dt.hour,
                                                             dt.minute,
                                                             dt.second)
        if os.path.isdir(dir_name) is False:
            if local("mkdir -p versions").failed is True:
                return None
        if local("tar -cvzf {} web_static".format(file)).failed is True:
            return None
        return file
    except Exception as e:
        print(f"An error occurred: {e}")
