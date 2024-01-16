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
    # New variables
    dir_name = "versions"
    static_dir = "web_static"

    dt = datetime.utcnow()
    file_name = "{}_{}{}{}{}{}{}.tgz".format(static_dir,
                                             dt.year,
                                             dt.month,
                                             dt.day,
                                             dt.hour,
                                             dt.minute,
                                             dt.second)
    file_path = os.path.join(dir_name, file_name)

    if not os.path.exists(dir_name):
        mkdir_command = "mkdir -p {}".format(dir_name)
        result = local(mkdir_command)
        if result.failed:
            return None

    tar_command = "tar -cvzf {} {}".format(file_path, static_dir)
    result = local(tar_command)
    if result.failed:
        return None

    return file_path
