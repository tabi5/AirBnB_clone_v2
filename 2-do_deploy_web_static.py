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
#   - False: If the file doesn"t exist at archive_path or
# an error occurs during the deployment.
#   - True: If the deployment is successful.


from datetime import datetime
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["54.90.51.191", "52.3.251.97"]


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        archive_filename = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/" + archive_filename[:-4]
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, folder_name))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True
    except:
        return False
