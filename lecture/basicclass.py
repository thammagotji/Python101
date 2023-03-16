class school:
    # attribute
    school_name = 'anuban mheenoi'

    # constructor: work simultaneously when define instance
    def __init__(self, subject='Python programming'):
        print('instance constructed') 
        self.subject = subject

    # method
    def hello(self):
        print('ohayo dozo minasang')
    
    def teach(self):
        print(f'this school teaches {self.subject}')

class student(school):
    def __init__(self, fullname, level, score, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.level = level
        self.score = score

    def check_grade(self):
        if self.score >= 80:
            print(f'subject {self.subject} got A')
        elif self.score >= 70:
            print(f'subject {self.subject} got B')
        elif self.score >= 60:
            print(f'subject {self.subject} got C')
        elif self.score >= 50:
            print(f'subject {self.subject} got D')
        else:
            print(f'subject {self.subject} got F')

# instance: define name from object
#school1 = school('maths')
#print(f'school name: {school1.school_name}')
#school1.hello()
#school1.teach()
print('--------------------')
student01 = student('somsak makmhokmoon', 5, 75, 'maths')
student01.hello()
print(f'school name: {student01.school_name}')
print(f'student name: {student01.fullname}')
print(f'student level: {student01.level}')
student01.check_grade()
print('--------------------')
student02 = student('somgeat beadbor', 4, 46, 'english')
print(f'school name: {student02.school_name}')
print(f'student name: {student02.fullname}')
print(f'student level: {student02.level}')
student02.check_grade()
print('--------------------')
student03 = student('somying yingjonghong', 4, 91, 'physics')
print(f'school name: {student03.school_name}')
print(f'student name: {student03.fullname}')
print(f'student level: {student03.level}')
student03.check_grade()
