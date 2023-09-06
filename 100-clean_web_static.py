#!/usr/bin/python3
"""Fabric script that clean archives."""
from fabric.api import *
from datetime import datetime
import os

env.hosts = [
    '34.227.89.39',
    '35.174.184.2'
]


def do_clean(number=0):
    """Function to clean archives."""
    number = int(number)
    if number < 2:
        number = 2
    else:
        number += 1
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf --".format(number))
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf --".format(number))
