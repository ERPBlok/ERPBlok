# This file is a part of the AnyBlok project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import anyblok
from anyblok.blok import BlokManager
from anyblok.registry import RegistryManager
from anyblok.config import Configuration, get_url
from logging import getLogger
from sqlalchemy_utils.functions import database_exists, create_database

logger = getLogger(__name__)

Configuration.add_application_properties(
    'update-project', ['logging', 'create_db'],
    prog='AnyBlok update project, version')


def update_project():
    anyblok.load_init_function_from_entry_points()
    Configuration.load('update-project')
    anyblok.configuration_post_load()
    BlokManager.load()
    db_name = Configuration.get('db_name')
    logger.info("update project: db_name=%r", db_name)

    to_install = []
    to_update = []
    to_uninstall = []

    url = get_url()
    options = {}
    if not database_exists(url):
        db_template_name = Configuration.get('db_template_name', None)
        create_database(url, template=db_template_name)
        to_install.append('erpblok')
        version = None
        registry = RegistryManager.get(db_name, **options)
        with_demo = Configuration.get('with_demo', False)
        registry.System.Parameter.set("with-demo", with_demo)
        if with_demo:
            to_install.append('erpblok-blok-manager')

    else:
        options.update(dict(loadwithoutmigration=True))
        registry = RegistryManager.get(db_name, **options)

    registry.update_blok_list()  # case, new blok added
    version = registry.System.Blok.query().filter_by(
        name='erpblok').one().installed_version

    if version is None:
        pass
    else:
        to_update.append('erpblok')

    registry.upgrade(install=to_install, update=to_update,
                     uninstall=to_uninstall)

    if version is None:
        admin = registry.Pyramid.User.insert(login='admin')
        registry.Pyramid.CredentialStore.insert(
            login='admin', password='admin')
        admin.roles.append(registry.Pyramid.Role.query().get('admin'))

    registry.commit()
    registry.close()
    logger.info("Project updated: db_name=%r", db_name)


if __name__ == '__main__':
    update_project()
