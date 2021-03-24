=======
erpblok
=======

A short description of the Anyblok based project


* Free software: Mozilla Public License Version 2.0
* Documentation: https://erpblok.readthedocs.io.

Setup
-----

* Clone the repository

* Installer le projet et le blok de compta::

     python3 -m venv venv
     source venv/bin/activate
     make setup-dev
     anyblok_updatedb -c app.dev.cfg --install-bloks erpblok-compta

* Lancer le server python en auto reload::
   
     source venv/bin/activate
     make run-dev

* Lancer le client FuretUI (Le serveur doit être lancer)::
   
     source venv/bin/activate
     make run-dev-npm

# Lancer les tests U::

     source venv/bin/activate
     make setup-tests
     make test

# Lanver un interpreter python::

     source venv/bin/activate
     anyblok_interpreter -c app.dev.cfg


`doc AnyBlok <https://doc.anyblok.org/en/latest/MEMENTO.html>`_
`doc SQLAlchemy <https://docs.sqlalchemy.org/en/14/orm/query.html?highlight=query#sqlalchemy.orm.Query>`_




Features
--------

* TODO

Author
------

Your name 
Your address email (eq. you@example.com)
https://github.com/Your github username

Credits
-------

.. _`Anyblok`: https://github.com/AnyBlok/AnyBlok

This `Anyblok`_ package was created with `audreyr/cookiecutter`_ and the `AnyBlok/cookiecutter-anyblok-project`_ project template.

.. _`AnyBlok/cookiecutter-anyblok-project`: https://github.com/Anyblok/cookiecutter-anyblok-project
.. _`audreyr/cookiecutter`: https://github.com/audreyr/cookiecutter

