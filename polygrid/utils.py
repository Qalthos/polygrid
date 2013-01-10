def get_colmodel_from_entity(entity, show=10):
    """ Build the dynamic jqGrid colModel from an Entity """
    colModel = [{
        'name': 'id',
        'index': 'id',
        'hidden': True,
        'width': 1,
        'key': True,
        'search': False
    }]
    for i, col in enumerate(entity[u'columns']):
        if i >= show:
            colModel.append({'name': col, 'index': col, 'hidden': True})
        else:
            colModel.append({'name': col, 'index': col})
    return colModel

def get_colnames_from_entity(entity):
    return ['id'] + entity[u'column_names']
