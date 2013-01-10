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
jqgrid_locale_en = JSLink(filename='static/js/i18n/grid.locale-en.js',
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
jquery_jqgrid_js = JSLink(filename='static/js/jquery.jqGrid.js',
              javascript=[jqgrid_multiselect_js],
                          modname=__name__)

lightness_ui_css = CSSLink(filename='static/themes/start/jquery-ui.custom.css',
                           modname=__name__, media='screen')
ui_jqgrid_css = CSSLink(filename='static/themes/ui.jqgrid.css',
                        modname=__name__, media='screen')

ui_multiselect_css = CSSLink(filename='static/themes/ui.multiselect.css',
                        modname=__name__, media='screen')
jqgrid_fluid_js = JSLink(filename='static/js/jquery.jqGrid.fluid.js', modname=__name__)

gitweb_url = config.get('civx.gitweb.url',
                        'http://civx-git1.csh.rit.edu/repoweb')

class JQueryGrid(Widget):
    params = ['id', 'model', 'gridname', 'graphs', 'git_repo', 'gitweb',
              'model_module', 'scraper_module', 'civx_menu', 'menu']
    template = 'mako:polygrid.templates.jqgrid'
    javascript = [jquery_js, jquery_ui_all_js, jquery_layout_js,
                  jqgrid_multiselect_js,
                  jqgrid_locale_en, jquery_jqgrid_js,
                  #jquery_tablednd_js,#jqgrid_contextmenu_js,
                  civx_js]
    css = [lightness_ui_css, ui_jqgrid_css,
           blueprint_screen_css, blueprint_print_css, blueprint_sprites_css,
           civx_css, ui_multiselect_css]

    civx_menu = False # Whether or not to display the menu
    #menu = CIVXMenu('civx_menu')

    def update_params(self, d):
        """ Assign a unique ID to this widget when it is rendered """
        super(JQueryGrid, self).update_params(d)
        if not d.id:
            d.id = str(uuid4())
        d.gridname = self.__class__.__name__
        d.graphs = graphs
        if d.model:
            if isinstance(d.model, basestring):
                civx_model = civx.utils.get_model(d.model)
                if civx_model:
                    d.model = civx_model
            if isclass(d.model):
                d.git_repo = civx.utils.get_git_repo_from_model(d.model)
                d.gitweb = gitweb_url
                d.model_module = d.model.__module__ + '.' + d.model.__name__
                scraper = civx.utils.get_scraper_from_model(d.model)
                if scraper:
                    d.scraper_module = scraper.__module__ + '.' + scraper.__name__

# vim: expandtab sw=4 ts=4 ai
