#!/usr/bin/python3
""" fabric script """

from fabric.api import run, put, env
import os


env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.hosts = ["35.237.72.232", "34.73.16.66"]


def do_deploy(archive_path):
    """ distributes an archive to your web servers """

    if not os.path.exists(archive_path) or os.path.isdir(archive_path):
        return False

    no_path = archive_path.split('/')[-1]
    no_ext = no_path.rsplit('.', 1)[0]

    try:
        put(local_path=archive_path, remote_path="/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
             no_path, no_ext))
        run("rm /tmp/{}".format(no_path))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext))
    except BaseException:
        return False
    return True
