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
from fabric.api import *
import os.path

env.hosts = ["54.90.51.191", "52.3.251.97"]  # Replace with your web server IPs

def do_deploy(archive_path):
    """Deploys the specified archive to web servers."""

    if not os.path.exists(archive_path):
        return False

    with settings(warn_only=True):
        result = put(archive_path, "/tmp/")
        if result.failed:
            return False

    with cd("/data/web_static/releases"):
        archive_filename = os.path.basename(archive_path)
        release_dirname = archive_filename.replace(".tgz", "")
        run("mkdir -p " + release_dirname)
        run("tar -xzf /tmp/" + archive_filename + " -C " + release_dirname)
        run("rm /tmp/" + archive_filename)

        # Additional commands specific to your archive structure
        run("mv " + release_dirname + "/web_static/* " + release_dirname)
        run("rm -rf " + release_dirname + "/web_static")

    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/" + release_dirname + " /data/web_static/current")
    print("New version deployed!")
    return True
