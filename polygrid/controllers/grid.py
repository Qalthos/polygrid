from tg import expose

from knowledge.model import Entity

from polygrid.utils import get_knowledge_session, get_colmodel_and_colnames_from_entity

__all__ = ['GridController']

class GridController(object):
    @expose('json')
    def query(self, like, sidx, rows=25, sord='desc', page=1, _search=False, **kw):
        Knowledge = get_knowledge_session("sqlite:///knowledge.db")
        query = Knowledge.query(Entity).filter(Entity.name.like(like))
        count = query.count()
        page = int(page)
        rows = int(rows)
        total_pages = count / rows
        if page > total_pages:
            page = total_pages

        model, columns = get_colmodel_and_colnames_from_entity(Knowledge, like)
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
                cell.append(row[col])
            # Note: this requires each model to have an 'id' column...
            entries.append({'id': row.id, 'cell': cell})

        return dict(page=page, total=total_pages, records=count, rows=entries)
