#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.

    Returns:
        str: The path of the created archive file.
        If an error occurs, returns None.
    """
    # New variable to store the current date and time
    dt = datetime.utcnow()

    # New variable to store the file name
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                     dt.month,
                                                     dt.day,
                                                     dt.hour,
                                                     dt.minute,
                                                     dt.second)
    dir_path = "versions"
    file_path = "{}/{}".format(dir_path, file_name)

    # Check if the directory exists
    if not os.path.isdir(dir_path):
        # If not, create the directory
        if local("mkdir -p {}".format(dir_path)).failed:
            return None

    # Create the tar gzipped archive
    if local("tar -cvzf {} web_static".format(file_path)).failed:
        return None

    # Return the path of the created archive file
    return file_path


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if the distribution is successful, False otherwise.
    """
    # New variable to store the file name
    file_name = archive_path.split("/")[-1]

    # New variable to store the name without extension
    name = file_name.split(".")[0]

    # New variable to store the temporary file path
    tmp_file_path = "/tmp/{}".format(file_name)

    # New variable to store the release directory path
    release_dir_path = "/data/web_static/releases/{}/".format(name)

    # New variable to store the current directory path
    current_dir_path = "/data/web_static/current"

    # Check if the archive file exists
    if not os.path.isfile(archive_path):
        return False

    # Distribute the archive to the web server
    if put(archive_path, tmp_file_path).failed:
        return False
    if run("rm -rf {}".format(release_dir_path)).failed:
        return False
    if run("mkdir -p {}".format(release_dir_path)).failed:
        return False
    if run("tar -xzf {} -C {}".format(tmp_file_path, release_dir_path)).failed:
        return False
    if run("rm {}".format(tmp_file_path)).failed:
        return False
    if run("mv {}web_static/* {}"
            .format(release_dir_path, release_dir_path)).failed:
        return False
    if run("rm -rf {}web_static".format(release_dir_path)).failed:
        return False
    if run("rm -rf {}".format(current_dir_path)).failed:
        return False
    if run("ln -s {} {}".format(release_dir_path, current_dir_path)).failed:
        return False

    return True


def deploy():
    """
    Create and distribute an archive to a web server.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """

    archive_file_path = do_pack()

    # Check if the archive file is created successfully
    if archive_file_path is None:
        return False

    # Distribute the archive to the web server
    return do_deploy(archive_file_path)
