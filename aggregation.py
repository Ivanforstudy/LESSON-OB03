class Teacher():
    def Teach(self):
        print("Преподаватель учит")
class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    def start_lesson(self):
        self.teacher.Teach()

my_teacher = Teacher()
my_school = School(my_teacher)