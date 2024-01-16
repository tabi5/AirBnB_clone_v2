#!/usr/bin/python3
# Description: Fabfile to distribute an archive to a web server.
#
# This script is used to distribute an archive file to a web server.
# It assumes that the web server
# has been configured with the necessary directory structure for deployment.
# The archive file is
# transferred to the server, extracted, and the appropriate symlinks
# are created to make it the
# current active version.
#
# Function:
#   - do_deploy: Distributes an archive to a web server.
#
# Parameters:
#   - archive_path (str): The path of the archive to distribute.
#
# Returns:
#   - False: If the file doesn't exist at archive_path or
# an error occurs during the deployment.
#   - True: If the deployment is successful.

import os
from fabric.api import env, put, run

# Hosts
env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        - False: If the file doesn't exist at archive_path or
          an error occurs during the deployment.
        - True: If the deployment is successful.
    """
    # New variables
    tmp_dir = "/tmp"
    release_dir = "/data/web_static/releases"
    current_dir = "/data/web_static/current"

    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name, ext = os.path.splitext(file)

    if put(archive_path, os.path.join(tmp_dir, file)).failed:
        return False
    if run(f"rm -rf {os.path.join(release_dir, name)}").failed:
        return False
    if run(f"mkdir -p {os.path.join(release_dir, name)}").failed:
        return False
    command = f"tar -xzf {os.path.join(tmp_dir, file)} -C " \
              f"{os.path.join(release_dir, name)}"
    if run(command).failed:
        return False
    # Handle the case when the command fails
    # Add your code here
    """if run(f"tar -xzf {os.path.join(tmp_dir, file)} -C
           {os.path.join(release_dir, name)}").failed:
    """
    if run(f"rm {os.path.join(tmp_dir, file)}").failed:
        return False
    if run(f"mv {os.path.join(release_dir, name, 'web_static', '*')}
           {os.path.join(release_dir, name)}").failed:
        return False
    if run(f"rm -rf {os.path.join(release_dir, name, 'web_static')}").failed:
        return False
    if run(f"rm -rf {current_dir}").failed:
        return False
    if run(f"ln -s {os.path.join(release_dir, name)} {current_dir}").failed:
        return False

    return True
