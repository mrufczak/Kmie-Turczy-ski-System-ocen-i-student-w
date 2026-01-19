class User:
    def __init__(self, login, password, first_name, last_name, role):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return f"User: {self.login} ({self.role})"
    
class Grade:
    def __init__(self, value, category="default"):
        self.value = float(value)
        self.category = category

    def __repr__(self):
        return f"{self.value}"

class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, value, category="default"):
        self.grades.append(Grade(value, category))

    def calculate_avg(self):

        if not self.grades:
            return 0.0
    
        total = sum(g.value for g in self.grades)
        return round(total / len(self.grades), 2)

class Student(User):
    def __init__(self, login, password, first_name, last_name, index_number):
        super().__init__(login, password, first_name, last_name, role = "student")

        self.index_number = index_number
        self.subjects = {}

    def get_subject(self, subject_name):
        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject(subject_name)
            #tutaj nie wiem czy powinnismy tworzyc nowy, trzeba spytac co ma sie stac, jak student nie ma tego przedmiotu
        return self.subjects[subject_name]
    
    def add_grade(self, subject_name, grade_value, category = "deafault"):
        self.get_subject(subject_name).add_grade(grade_value, category)

    def calculate_sem_avg(self):
        if not self.subjects:
            return 0.0
        sub_avgs = []

        for subject in self.subjects.values():
            avg = subject.calculate_avg()
            if avg > 0:
                sub_avgs.append(avg)
        
        total = sum(sub_avgs)

        count = len([s for s in self.subjects.values() if s.calculate_avg() > 0])

        return round(total/count, 2) if count > 0 else 0.0
    
    def to_dict(self):
        subjetcts_data = {}


        for name, subject in self.subjects.items():

            clean_grades = []
            
            for g in subject.grades:
                only_val = g.value
                clean_grades.append(only_val)

            subjetcts_data[name] = clean_grades

        return {
            "login": self.login,
            "password": self.password,
            "role": "student",
            "first_name": self.first_name,
            "last_name": self.last_name,
            "index_number": self.index_number,
            "subjects": subjetcts_data
        }
    
class Employee(User):
    def __init__(self, login, password, first_name, last_name):
        super().__init__(login, password, first_name, last_name, role = "employee")
        self.teaching_subjects = []

    def add_subject(self, subject_name):
        if subject_name not in self.teaching_subjects:
            self.teaching_subjects.append(subject_name)
    
    def remove_subject(self, subject_name):
        if subject_name in self.teaching_subjects:
            self.teaching_subjects.remove(subject_name)

    def can_teach(self, subject_name):
        return subject_name in self.teaching_subjects
    
    def to_dict(self):

        return {
            "login": self.login,
            "password": self.password,
            "role": "employee",
            "first_name": self.first_name,
            "last_name": self.last_name,
            "teaching_subjects": self.teaching_subjects
        }

    def __repr__(self):
        return f"Nauczyciel: {self.last_name} (Przedmioty: {', '.join(self.teaching_subjects)})"