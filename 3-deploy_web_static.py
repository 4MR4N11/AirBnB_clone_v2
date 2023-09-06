#!/usr/bin/python3
"""Fabric script that automatically archive and deploys archives to your web
servers, using the function deploy."""
from fabric.api import *
from datetime import datetime
import os

env.hosts = [
    '34.227.89.39',
    '35.174.184.2'
]


@runs_once
def do_pack():
    """Function to generate a .tgz archive from web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(file))
    try:
        local("tar -cvzf {} web_static".format(file))
        print("web_static packed: {} -> {}Bytes".format(file,
                                                        os.path.getsize(file)))
        return file
    except Exception:
        return None


def do_deploy(archive_path):
    """Function to distribute an archive to web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        arch_name = os.path.basename(archive_path)
        arch_no_ext = os.path.splitext(arch_name)[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(arch_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(arch_name, arch_no_ext))
        run("rm -rf /tmp/{}".format(arch_name))
        run(("mv /data/web_static/releases/{}/web_static/* " +
            "/data/web_static/releases/{}/").format(arch_no_ext, arch_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(arch_no_ext))
        run("rm -rf /data/web_static/current")
        run(("ln -s /data/web_static/releases/{}/ " +
            "/data/web_static/current").format(arch_no_ext))
        return True
    except Exception:
        return False


def deploy():
    """Function to archive and deploy web_static."""
    filename = do_pack()
    if filename:
        return do_deploy(filename)
    else:
        return False
