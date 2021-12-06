import pickle

from persistency.repository import Repository

class FileRepository(Repository):
    def __init__(self, file_path, entity_from_line, entity_to_line):
        super().__init__()
        self.__file_path = file_path
        self.__entity_from_line = entity_from_line
        self.__entity_to_line = entity_to_line

    def __len__(self):
        self.__read_from_file()
        return super().__len__()

    def __append_to_file(self, entity):
        # with open(self.__file_path, 'a') as f:
        #     f.write(self.__entity_to_line(entity) + '\n')
        with open(self.__file_path, 'wb') as f:
            pickle.dump(self._entities, f)

    def __read_from_file(self):
        # with open(self.__file_path, 'r') as f:
        #     lines = f.readlines()
        #     self._entities.clear()
        #     for line in lines:
        #         line = line.strip()
        #         if len(line) > 0:
        #             entity = self.__entity_from_line(line)
        #             self._entities[entity.entity_id] = entity
        with  open(self.__file_path, 'rb') as f:
            try:
                self._entities = pickle.load(f)
            except EOFError:
                pass

    def __write_to_file(self):
        # with open(self.__file_path, 'w') as f:
        #     for entity_id in self._entities:
        #         f.write(self.__entity_to_line(self._entities[entity_id]) + '\n')
        with open(self.__file_path, 'wb') as f:
            pickle.dump(self._entities, f)

    def add(self, entity):
        self.__read_from_file()
        super().add(entity)
        self.__append_to_file(entity)

    def search_by_id(self, entity_id):
        self.__read_from_file()
        return super().search_by_id(entity_id)

    def delete_by_id(self, entity_id):
        self.__read_from_file()
        super().delete_by_id(entity_id)
        self.__write_to_file()

    def update(self, entity):
        self.__read_from_file()
        super().update(entity)
        self.__write_to_file()

    def get_all(self):
        self.__read_from_file()
        return super().get_all()
