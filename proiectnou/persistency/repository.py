class RepositoryException(Exception):
    pass

class Repository:
    def __init__(self):
        self._entities = dict()

    def __len__(self):
        return len(self._entities)

    def add(self, entity):
        if entity.entity_id in self._entities:
            raise RepositoryException("element existent")
        self._entities[entity.entity_id] = entity

    def search_by_id(self, entity_id):
        if entity_id not in self._entities:
            raise RepositoryException('element inexistent')
        return self._entities[entity_id]

    def delete_by_id(self, entity_id):
        if entity_id not in self._entities:
            raise RepositoryException('element inexistent')
        del self._entities[entity_id]

    def update(self, new_entity):
        if new_entity.entity_id not in self._entities:
            raise RepositoryException('element inexistent')
        self._entities[new_entity.entity_id] = new_entity

    def get_all(self):
        return list(self._entities.values())

