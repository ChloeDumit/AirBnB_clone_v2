#!/usr/bin/python3
""" Program that compress a dir with tar before sending """
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['35.231.99.203', '104.196.174.128']


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo """
    today = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions/")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(today))
        return "versions/web_static_{}.tgz".format(today)
    except Exception:
        return None


def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False
    
    file_path = archive_path.split("/")[1]
    serv_folder = "/data/web_static/releases/" + file_path
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p" + serv_folder)
        run("sudo tar -xzf /tmp/" + file_path + " -C " + serv_folder + "/")
        run("sudo rm /tmp/" + file_path)
        run("sudo mv " + serv_folder + "/web_static/* " + serv_folder)
        run("sudo rm -rf " + serv_folder + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + serv_folder + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
