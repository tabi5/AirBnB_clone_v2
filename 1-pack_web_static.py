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

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # generate the file name in the format web_static_<year><month><day><hour><minute><second>.tgz
    file_name = "versions/web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    # use the tar command to create a .tgz archive of the web_static directory
    result = local("tar -cvzf {} web_static".format(file_name))

    # return the archive path if the archive was correctly generated, otherwise return None
    if result.failed:
        return None
    else:
        return file_name
