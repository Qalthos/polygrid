# This file is part of CIVX.
#
# CIVX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CIVX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CIVX.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2009-2010, CIVX, Inc.
"""
The CIVX Grid Widget
====================
"""

from uuid import uuid4
from inspect import isclass
from tg import config
from tw2.core import Widget, JSLink, CSSLink, js_callback
from tw2.jquery import jquery_js, jQuery
from tw2.jqplugins.jqgrid.base import jqgrid_locale, jqgrid_js, jqgrid_css


blueprint_sprites_css = CSSLink(
    modname='blueprint',
    filename='static/plugins/sprites/sprite.css',
    media='screen')
blueprint_screen_css = CSSLink(
    modname='blueprint',
    filename='static/screen.css',
    media='screen, projection')
blueprint_print_css = CSSLink(
    modname='blueprint',
    filename='static/print.css',
    media='print')

civx_js = JSLink(link='static/js/civx.js', javascript=[jquery_js])
civx_css = CSSLink(link='static/css/civx.css')
#from civx.widgets.civx_menu import CIVXMenu
#from civx.controllers.topN import graphs

jquery_ui_all_js = JSLink(filename='static/js/jquery-ui-1.8.2.custom.min.js',
                          modname=__name__)
jquery_layout_js = JSLink(filename='static/js/jquery.layout.js',
                          modname=__name__)
jquery_tablednd_js = JSLink(filename='static/js/jquery.tablednd.js',
                            modname=__name__)
jquery_modal_js = JSLink(filename='static/js/jqModal.js',
                         modname=__name__)
jquery_dnr_js = JSLink(filename='static/js/jqDnR.js',
                       modname=__name__)
jqgrid_contextmenu_js = JSLink(filename='static/js/jquery.contextmenu.js',
                               modname=__name__)
jqgrid_multiselect_js = JSLink(filename='static/js/ui.multiselect.js',
                               modname=__name__)

lightness_ui_css = CSSLink(filename='static/themes/start/jquery-ui.custom.css',
                           modname=__name__, media='screen')

ui_multiselect_css = CSSLink(filename='static/themes/ui.multiselect.css',
                        modname=__name__, media='screen')
jqgrid_fluid_js = JSLink(filename='static/js/jquery.jqGrid.fluid.js', modname=__name__)

gitweb_url = config.get('civx.gitweb.url',
                        'http://civx-git1.csh.rit.edu/repoweb')

class JQueryGrid(Widget):
    template = 'mako:polygrid.templates.jqgrid'
    resources = [jquery_js, jquery_ui_all_js, jquery_layout_js,
                  jqgrid_multiselect_js,
                  jqgrid_locale, jqgrid_js, jqgrid_css,
                  #jquery_tablednd_js,#jqgrid_contextmenu_js,
                  civx_js, lightness_ui_css,
           blueprint_screen_css, blueprint_print_css, blueprint_sprites_css,
           civx_css, ui_multiselect_css]

    civx_menu = False # Whether or not to display the menu
    #menu = CIVXMenu('civx_menu')

    def prepare(self):
        """ Assign a unique ID to this widget when it is rendered """
        super(JQueryGrid, self).prepare()
        if not self.id:
            self.id = str(uuid4())
        self.gridname = self.__class__.__name__
        self.graphs = graphs
        if self.model:
            if isinstance(self.model, basestring):
                civx_model = civx.utils.get_model(self.model)
                if civx_model:
                    self.model = civx_model
            if isclass(self.model):
                self.git_repo = civx.utils.get_git_repo_from_model(self.model)
                self.gitweb = gitweb_url
                self.model_module = self.model.__module__ + '.' + self.model.__name__
                scraper = civx.utils.get_scraper_from_model(self.model)
                if scraper:
                    self.scraper_module = scraper.__module__ + '.' + scraper.__name__

# vim: expandtab sw=4 ts=4 ai
