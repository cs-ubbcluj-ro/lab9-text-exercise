class Entity:
    def __init__(self, entity_id):
        self.__entity_id = entity_id

    @property
    def entity_id(self):
        return self.__entity_id

class Student(Entity):
    def __init__(self, entity_id, name):
        super().__init__(entity_id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def     student_to_line(student):
        return f"{student.entity_id}, {student.name}"

    @staticmethod
    def line_to_student(line):
        words = line.split(',')
        return Student(int(words[0]), words[1])
