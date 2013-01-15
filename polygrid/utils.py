from knowledge.model import Entity

def get_knowledge_session(db_uri):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import scoped_session, sessionmaker, mapper
    from knowledge.model import metadata
    engine = create_engine(db_uri)
    metadata.bind = engine
    return scoped_session(sessionmaker(bind=engine))

def get_colmodel_and_colnames_from_entity(knowledge, like):
    entities = knowledge.query(Entity).filter(Entity.name.like(like))
    colModel = [{
        'name': 'id',
        'index': 'id',
        'hidden': True,
        'width': 1,
        'key': True,
        'search': False
    }, {'name':'name', 'index':'name'}]
    columns = ['id', 'name']
    for entity in entities:
        for fact in entity.facts:
            if fact not in columns:
                columns.append(fact)
                colModel.append({'name': fact, 'index': fact})

    return (colModel, columns)
