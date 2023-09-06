#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime
import os


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
