#!/usr/bin/python3
"""
Fabric script that creates and distributes
an archive to web servers
"""

from fabric.api import env, put, run
from datetime import datetime
from os.path import exists
from fabric.api import local

env.hosts = ["54.90.51.191", "52.3.251.97"] 


def do_pack():
    """Creates a compressed archive of the web_static folder"""
    local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(archive_path))
    if exists(archive_path):
        return archive_path
    return None


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

        # Create a new symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
