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
The CIVX Poly Grid
==================
"""

import logging

from tw2.core import js_callback
from tw2.jquery import jQuery

from knowledge.model import Entity

from utils import get_colmodel_from_entity, get_colnames_from_entity
from widget import JQueryGrid

log = logging.getLogger(__name__)

class PolyGrid(JQueryGrid):
    params = ['entity']

    template = """
<div>
  <div class="gridfooter" align="right">
    ## TODO:
    ## - render custom links from facts about the entity

    <ul>
        % if entity:
            <h1>${entity.title}</h1>
            <h2>Facts</h2>
            % for fact in entity.facts:
                % if entity[fact].startswith('http'):
                    <li><b>${fact}:</b> <a href="${entity[fact]}">${entity[fact]}</a></li>
                % else:
                    <li><b>${fact}:</b> ${entity[fact]}</li>
                % endif
            % endfor
         % endif
    </ul>

    ##% if model:
    ##    % if model.__name__ in graphs:
    ##      <a href="#" onclick="civx_new_tab_iframe('#${model.__name__}_metrics', '${model.__name__} Metrics', '/topN/${model.__name__}'); return false;"><span class="ss_sprite ss_chart_bar">Metrics</span></a>
    ##      <a href="/feeds/${model.__name__}"><span class="ss_sprite ss_feed">Feed</span></a>
    ##      <a href="/documentation/models/${model.__name__}"><span class="ss_sprite ss_report">Docs</span></a>
    ##    % endif
    ##    % if git_repo:
    ##      <a href="#" onclick="civx_new_tab_iframe('#${model.__name__}_raw', '${model.__name__} Raw Data', '${gitweb}/?p=civx-csv&a=tree&f=${git_repo}'); return false;"><span class="ss_sprite ss_page_white_text">Raw</span></a>
    ##    % endif
    ##    <a href="#" onclick="moksha.view_module_source('${model_module}'); return false;"><span class="ss_sprite ss_database_gear">Model Source</span></a>
    ##    <a href="#" onclick="moksha.view_module_source('${scraper_module}'); return false;"><span class="ss_sprite ss_script_gear">Scraper Source</span></a>
    ##    <a href="#" onclick="moksha.view_module_source('${gridname}'); return false;"><span class="ss_sprite ss_brick">Widget Source</span></a>
    ##    <a href="#" onclick="civx_new_tab('#Attribution', 'Attribution', '/widgets/entourage'); return false;"><span class="ss_sprite ss_information">Attribution</span></a>
    ##    <a href="#" onclick="civx_embed_widget_dialog('${gridname}'); return false;"><span class="ss_sprite ss_html_add">Embed</span></a>
    ##% endif
  </div>
  <br/>
  <table id="${id}" class="scroll" cellpadding="0" cellspacing="0"></table>
  <div id="${id}_pager" class="scroll" style="text-align:center;"></div>
</div>
    """
    engine_name = 'mako'

    def update_params(self, d):
        super(PolyGrid, self).update_params(d)

        Knowledge = get_knowledge_session()
        try:
            entity = Knowledge.query(Entity).filter_by(name=d.model).one()
        except Exception, e:
            log.warning(e)
            entity = Knowledge.query(Entity).filter_by(name=d.model).first()

        colNames = get_colnames_from_entity(entity)
        colModel = get_colmodel_from_entity(entity)

        params = {
            'url': '/grids/query?widget=' + entity.name,
            'datatype': 'json',
            'colNames': colNames,
            'colModel': colModel,
            'height': 550,
            'rowNum': 25,
            #'rowList': [10,20,30],
            'pager': '#%s_pager' % d.id,
            'sortname': 'id',
            'viewrecords': True,
            'sortorder': "desc",
            'caption': entity.name,
            'autowidth': True,
            'loadui': 'block',
            #'shrinkToFit': True,
            'forcefit': True,
            }

        self.add_call(jQuery('#' + d.id)
                        .jqGrid(params)
                        .navGrid('#%s_pager' % d.id, {
                            'add': False,
                            'del': False,
                            'edit': False,
                            'search': False,
                            }, {}, {}, {}, {'multipleSearch': True}))

        self.add_call(jQuery('#' + d.id)
                        .jqGrid('filterToolbar',{
                            'stringResult': True,
                            'searchOnEnter': False
                            }));

        self.add_call(jQuery('#' + d.id)
                        .jqGrid('navButtonAdd', '#%s_pager' % d.id, {
                            'caption': 'Columns',
                            'title': 'Reorder Columns',
                            'onClickButton': js_callback("""
                                function() {
                                    jQuery('#%s').jqGrid('columnChooser');
                                }
                            """ %  d.id),
                            }))
