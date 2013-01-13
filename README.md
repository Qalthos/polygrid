polygrid
========

To test, follow these simple steps:
* git clone && setup.py develop (preferably in a virtualenv)
* make a new TG2 quickstart
* edit the root controller; add GridController as grid from polygrid.controllers, and make or edit an entry to have a PolyGrid from polygrid.widgets
* either have a knowledge db locally, or edit the polygrid to give it the location of one
* paster serve development.ini
