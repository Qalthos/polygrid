import json
import math

from sqlalchemy import and_, or_, func
from tg import expose

from knowledge.model import Entity

from polygrid.utils import get_knowledge_session, get_colmodel_and_colnames_from_entity

__all__ = ['GridController']

class GridController(object):
    @expose('json')
    def query(self, like, sidx, rows=25, sord='desc', page=1, _search=False, **kw):
        Knowledge = get_knowledge_session("sqlite:///knowledge.db")
        query = Knowledge.query(Entity).filter(Entity.name.like(like))

        model, columns = get_colmodel_and_colnames_from_entity(Knowledge, like)

        if _search and _search.lower() == 'true':

            if 'filters' in kw:
                filters = json.loads(kw['filters'])
                if filters['groupOp'] == 'AND':
                    group_func = and_
                elif filters['groupOp'] == 'OR':
                    group_func = or_

                multi_query = []
                for rule in filters['rules']:
                    col = getattr(Entity, rule['field'])
                    multi_query.append(self.query_filter(rule['op'],
                                                         col,
                                                         rule['data']))
                query = query.filter(group_func(*multi_query))


        count = query.count()
        page = int(page)
        rows = int(rows)
        total_pages = math.ceil(float(count) / rows)
        if page > total_pages:
            page = total_pages

        # This goes before offset, if it gets fixed
        #~ .order_by(getattr(getattr(model, sidx), sord)()) \
        query = query \
                  .offset(max(page*rows - rows, 0)) \
                  .limit(rows) \
                  .all()

        entries = []
        for row in query:
            cell = []
            for col in columns:
                if col == 'id':
                    continue
                try:
                    cell.append(row[col])
                except KeyError:
                    cell.append(None)
            # Note: this requires each model to have an 'id' column...
            entries.append({'id': row.id, 'cell': cell})

        return dict(page=page, total=total_pages, records=count, rows=entries)

    def query_filter(self, oper, col, string):
        if oper == 'eq':
            return col == string
        elif oper == 'ne':
            return col != string
        elif  oper == 'lt':
            return col < string
        elif oper == 'le':
            return col <= string
        elif oper == 'gt':
            return col > string
        elif oper == 'ge':
            return col >= string
        elif oper == 'bw':
            return func.lower(col).like(string.lower() + '%')
        elif oper == 'ew':
            return func.lower(col).like('%' + string.lower())
        elif oper == 'cn':
            return func.lower(col).like('%' + string.lower() + '%')
