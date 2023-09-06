#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""

from fabric.api import run, put, env
from os import path

env.hosts = ['34.227.89.39', '35.174.184.2']


def do_deploy(archive_path):
    """Function to distribute an archive to web servers."""
    if not path.exists(archive_path):
        return False
    try:
        arch_name = path.basename(archive_path)
        arch_no_ext = path.splitext(arch_name)[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(arch_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(arch_name, arch_no_ext))
        run("rm -rf /tmp/{}".format(arch_name))
        run(("mv /data/web_static/releases/{}/web_static/* " +
            "/data/web_static/releases/{}/").format(arch_no_ext, arch_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static/"
            .format(arch_no_ext))
        run("rm -rf /data/web_static/current")
        run(("ln -s /data/web_static/releases/{}/ " +
            "/data/web_static/current").format(arch_no_ext))
        return True
    except Exception:
        return False
