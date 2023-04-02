class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        avg_grade = sum(all_grades) / len(all_grades)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n' + \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' + \
            f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        all_grades_1 = [grade for course_grades in self.grades.values() for grade in course_grades]
        avg_grade_1 = sum(all_grades_1) / len(all_grades_1)
        all_grades_2 = [grade for course_grades in other.grades.values() for grade in course_grades]
        avg_grade_2 = sum(all_grades_2) / len(all_grades_2)
        return all_grades_1 < all_grades_2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:' \
               f' {sum(all_grades) / len(all_grades):.1f}'

    def __lt__(self, other):
        all_grades_1 = [grade for course_grades in self.grades.values() for grade in course_grades]
        avg_grades_1 = sum(all_grades_1) / len(all_grades_1)
        all_grades_2 = [grade for course_grades in other.grades.values() for grade in course_grades]
        avg_grades_2 = sum(all_grades_2) / len(all_grades_2)
        return avg_grades_1 < avg_grades_2

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Students:
best_student = Student('Ruoy', 'Eman', 'M')
bad_student = Student('leo', 'Watson', 'M')

#Reviewers:
cool_reviewer = Reviewer('Some', 'Buddy')

#Lecturers:
cool_lecturer = Lecturer('David', 'Brown')
bad_lecturer = Lecturer('Really', 'Bad')


#adds courses to students:
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C++']
bad_student.courses_in_progress += ['Java']

#adds courses to reviewers:
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

#adds courses to lecturers:
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']
bad_lecturer.courses_attached += ['Java']

#Reviewres marks:
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(bad_student, 'Java', 5)

#Lecturers marks of students:
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Java', 5)
best_student.rate_lecture(bad_lecturer, 'Java', 2)
bad_student.rate_lecture(bad_lecturer, 'Java', 4)

# print(cool_lecturer.grades)
# print(best_student.grades)
# print(bad_student.grades)
#
# print(f'{cool_reviewer}\n')
# print(f'{cool_lecturer}\n')
# print(f'{best_student}\n')
# print(f'{bad_student}\n')
# print(f'{bad_lecturer}\n')

print(best_student < bad_student)
print(bad_lecturer < cool_lecturer)
