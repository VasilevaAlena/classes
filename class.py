lecturers_list = []   
students_list = [] 

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def av_rating(self):
        rating = []
        for v in self.grades.values():
            rating += v
            average_rating = sum(rating)/len(rating)
        return average_rating         
           
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'  
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.av_rating()} \n' \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, student):
        return (self.av_rating() == student.av_rating())
    
    def __gt__(self, student):
        return (self.av_rating() > student.av_rating())
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        lecturers_list.append(self)

    def av_rating(self):
        rating = []
        for v in self.grades.values():
            rating += v
            average_rating = sum(rating)/len(rating)
        return average_rating

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_rating()}'
    
    def __eq__(self, lecturer):
        return (self.av_rating() == lecturer.av_rating())
    
    def __gt__(self, lecturer):
        return (self.av_rating() > lecturer.av_rating())
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
        self.courses_attached = []

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

def av_grade_students(students_list, course):
    students_av_grade = []
    for student in students_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for courses, grade in student.grades.items():
                if course in courses:
                    students_av_grade += grade
    return round(sum(students_av_grade) / len(students_av_grade), 2)

def av_grade_lecturers(lecturers_list, course):
    lecturers_av_grade = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for courses, grade in lecturer.grades.items():
                if course in courses:
                    lecturers_av_grade += grade
    return round(sum(lecturers_av_grade) / len(lecturers_av_grade), 2)

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student_2 = Student('Petr', 'Petrov', 'your_gender')
some_student_2.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Git']
 
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer_2 = Lecturer('Yana', 'Kruglova')
some_lecturer_2.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Git']

some_reviewer = Reviewer('Ivan', 'Pupkin')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer_2 = Reviewer('Irina', 'Shilova')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Git']
 
some_reviewer.rate_hw(some_student_2, 'Git', 5)
some_reviewer.rate_hw(some_student_2, 'Git', 7)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer_2.rate_hw(some_student, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Python', 6)

some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 7)
some_student.rate_lecturer(some_lecturer_2, 'Git', 10)
some_student_2.rate_lecturer(some_lecturer_2, 'Git', 9)

comparison_student_eq = some_student.__eq__(some_student_2)
comparison_student_gt = some_student.__gt__(some_student_2)
comparison_lecturer_eq = some_lecturer.__eq__(some_lecturer_2)
comparison_lecturer_gt = some_lecturer.__gt__(some_lecturer_2)


if comparison_student_eq:
    print(f'{some_student.name} and {some_student_2.name} learn the same way')
else:
    if comparison_student_gt:
        print(f'{some_student.name} studies better than {some_student_2.name}')
    else:
        print(f'{some_student_2.name} studies better than {some_student.name}')

if comparison_lecturer_eq:
    print(f'{some_lecturer.name} and {some_lecturer_2.name} teach the same')
else:
    if comparison_lecturer_gt:
        print(f'{some_lecturer.name} teaches better than {some_lecturer_2.name}')
    else:
        print(f'{some_lecturer_2.name} teaches better than {some_lecturer.name}')

print(some_reviewer)
print(some_lecturer)
print(some_student)
print(av_grade_students(students_list, 'Python')) 
print(av_grade_students(students_list, 'Git')) 
print(av_grade_lecturers(lecturers_list, 'Python'))   
print(av_grade_lecturers(lecturers_list, 'Git'))      
