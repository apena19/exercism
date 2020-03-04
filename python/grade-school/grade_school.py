class School:
    def __init__(self):
        self.student_dictionary = {}

    grade_list = []

    def add_student(self, name, grade):
        if grade in self.student_dictionary:
            self.student_dictionary[grade] = sorted(
                    self.student_dictionary[grade] + [name]
                    )
        else:
            self.student_dictionary[grade] = [name]
        self.grade_list = sorted(list(set(self.grade_list+[grade])))

    def roster(self):
        arr = []
        for grade in self.grade_list:
            arr += self.student_dictionary[grade]
        return arr

    def grade(self, grade_number):
        if grade_number in self.student_dictionary:
            return self.student_dictionary[grade_number]
        else:
            return []
