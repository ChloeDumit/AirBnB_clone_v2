#!/usr/bin/python3
""" create a .tgz file"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """ create a .tgz file"""
    today = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions/")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(today))
        return "versions/web_static/{}".format(today)
    except Exception:
        return None
