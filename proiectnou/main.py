from domain.entity import Student
from persistency import file_repository
from persistency.file_repository import FileRepository


repo = FileRepository('student',Student.line_to_student,Student.student_to_line)

repo.add(Student(1,'da'))
repo.add(Student(2,'da'))
repo.add(Student(3,'da'))