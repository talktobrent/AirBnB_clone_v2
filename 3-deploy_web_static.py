#!/usr/bin/python3
""" deploy module """

from fabric.api import env
pack = __import__("1-pack_web_static", fromlist=['do_pack'])
deploy = __import__("2-do_deploy_web_static", fromlist=['do_deploy',
                    'env.user', 'env.key_filename', 'env.hosts'])


packer = pack.do_pack
sender = deploy.do_deploy
env.user = deploy.env.user
env.key_filename = deploy.env.key_filename
env.hosts = deploy.env.hosts

archive = packer()


def deploy():
    """ deploy """
    if not archive:
        return False
    return sender(archive)
