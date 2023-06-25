class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_l(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += grade
            else:
                lector.grades[course] = grade
        else:
            return 'Ошибка'


    def _grade(self):
        grades_list = []
        for i in self.grades:
            grades_list += some_student.grades[i]
        grades_list = round(sum(grades_list) / len(grades_list), 1)
        return grades_list


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._grade()}\nКурсы в процессе завершения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res


    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self._grade() > other._grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def _grade(self):
        grades_list = []
        for i in self.grades:
            grades_list += some_lector.grades[i]
        grades_list = round(sum(grades_list) / len(grades_list), 1)
        return grades_list


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._grade()}'
        return res


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self._grade() > other._grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student = Student('Harry', 'Potter')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']


some_student1 = Student('Ron', 'Weesly')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Введение в программирование']


some_lector = Lecturer('Oleg', 'Buligin')
some_lector.courses_attached = some_student.courses_in_progress
some_student.rate_l(some_lector, 'Python', [10, 10, 10])
some_student.rate_l(some_lector, 'Git', [10, 9, 9])

some_lector1 = Lecturer('Timur', 'Timurov')
some_lector1.courses_attached = some_student.courses_in_progress
some_student.rate_l(some_lector1, 'Python', [9, 9, 9])
some_student.rate_l(some_lector1, 'Git', [10, 10, 10])


some_reviwer = Reviewer('Some', 'Buddy')
some_reviwer.courses_attached = some_student.courses_in_progress
some_reviwer.rate_hw(some_student, 'Python', [10, 10, 10])
some_reviwer.rate_hw(some_student, 'Git', [10, 10, 10])


some_reviwer.courses_attached = some_student1.courses_in_progress
some_reviwer.rate_hw(some_student1, 'Python', [10, 10, 9])
some_reviwer.rate_hw(some_student1, 'Git', [9, 8, 9])


#print(some_reviwer)
#print(some_lector)
#print(some_student)


def average_hw_grade(students, course):
    grades_list = []
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            grades_list += student.grades[course]
    if len(grades_list) == 0:
        return 0
    else:
        return print(f'На курсе {course} средняя оценка у студентов: {round(sum(grades_list) / len(grades_list), 2)}')


def avg_lecture_grade(lecturers, course):
    grades_list = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            grades_list += lecturer.grades[course]
    if len(grades_list) == 0:
        return 0
    else:
        return print(f'На курсе {course} средняя оценка у лекторов: {round(sum(grades_list) / len(grades_list), 2)}')


average_hw_grade([some_student, some_student1], 'Python')
average_hw_grade([some_student, some_student1], 'Git')
avg_lecture_grade([some_lector, some_lector1], 'Python')
avg_lecture_grade([some_lector, some_lector1], 'Git')