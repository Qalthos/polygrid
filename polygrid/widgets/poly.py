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

from tw2.jquery import jQuery, jquery_js
from tw2.jqplugins.jqgrid.base import jqgrid_js, jqgrid_css

from knowledge.model import Entity

from polygrid.utils import get_knowledge_session, get_colmodel_from_entity, get_colnames_from_entity
from polygrid.widgets import JQueryGrid

log = logging.getLogger(__name__)

class PolyGrid(JQueryGrid):
    resources = [
        jquery_js,
        jqgrid_js, jqgrid_css,
    ]
    template = "mako:polygrid.templates.polygrid"

    def prepare(self):
        super(PolyGrid, self).prepare()

        Knowledge = get_knowledge_session()
        try:
            self.entity = Knowledge.query(Entity).filter_by(name=self.model).one()
        except Exception, e:
            log.warning(e)
            self.entity = Knowledge.query(Entity).filter_by(name=self.model).first()

        colNames = get_colnames_from_entity(self.entity)
        colModel = get_colmodel_from_entity(self.entity)

        params = {
            'url': '/grids/query?widget=knowledge' + self.entity.name,
            'datatype': 'json',
            'colNames': colNames,
            'colModel': colModel,
            'height': 550,
            'rowNum': 25,
            #'rowList': [10,20,30],
            'pager': '#%s_pager' % self.id,
            'sortname': 'id',
            'viewrecords': True,
            'sortorder': "desc",
            'caption': self.entity.name,
            'autowidth': True,
            'loadui': 'block',
            #'shrinkToFit': True,
            'forcefit': True,
            }

        self.add_call(jQuery('#' + self.id)
                        .jqGrid(params)
                        .navGrid('#%s_pager' % self.id, {
                            'add': False,
                            'del': False,
                            'edit': False,
                            'search': False,
                            }, {}, {}, {}, {'multipleSearch': True}))

        self.add_call(jQuery('#' + self.id)
                        .jqGrid('filterToolbar',{
                            'stringResult': True,
                            'searchOnEnter': False
                            }));

        self.add_call(jQuery('#' + self.id)
                        .jqGrid('navButtonAdd', '#%s_pager' % self.id, {
                            'caption': 'Columns',
                            'title': 'Reorder Columns',
                            'onClickButton': js_callback("""
                                function() {
                                    jQuery('#%s').jqGrid('columnChooser');
                                }
                            """ %  self.id),
                            }))
