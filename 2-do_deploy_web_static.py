#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy."""
from fabric.api import *
import os

env.hosts = ["34.227.89.39", "35.174.184.2"]


def do_deploy(archive_path):
    """Function to distribute an archive to web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        file_names = archive_path.split("/")
        file_name = file_names[-1].split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))
        run("rm -rf /tmp/{}.tgz".format(file_name))
        run(("mv /data/web_static/releases/{}/web_static/* " +
            "/data/web_static/releases/{}/").format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run(("ln -s /data/web_static/releases/{}/" +
            " /data/web_static/current").format(file_name))
        return True
    except Exception:
        return False
