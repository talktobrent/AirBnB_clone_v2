#!/usr/bin/python3
""" fabric script """

from fabric.api import local
from time import strftime


def do_pack():
    """ fabric script generates generates .tgz archive
    from the the web_static folder of your AirBnB Clone repo"""

    if local('mkdir -p versions').return_code is 0:
        archive = "versions/web_static_{}.tgz".format(strftime("%Y%m%d%H%M%S"))
        if local('tar -czvf {} web_static'.format(archive)).return_code is 0:
            return archive
    return None
