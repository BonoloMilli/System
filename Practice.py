
class Clients(object):
   
   
    def __init__(self, studentNum,mark1,mark2):
        self.studentNum = studentNum
        self.mark1 = mark1
        self.mark2 = mark2
        self.students = [{'studNo':214, 'mak1': None, 'mak2':None}, 
                         {'studNo':233, 'mak1': None, 'mak2':None},
                         {'studNo':776, 'mak1': None, 'mak2':None},
                         {'studNo':543, 'mak1': None, 'mak2':None},
                         {'studNo':278, 'mak1': None, 'mak2':None}]
        
    def compare(self):
        if not any(student['studNo'] == self.studentNum for student in self.students):
            print("You are not in the system")    
        else:
              print("WELCOME BACK")
    def inputsMarks(self):
        for student in self.students:
         if self.studentNum == student['studNo']:
               student['mak1'] = self.mark1
               student['mak2'] = self.mark2
               print(f"{self.studentNum} {student['mak1']} {student['mak2']}") 
         else:
                print("Invalid marks/s")
                                

stud = int(input("Enter Student Number:"))
test1 = int(input("Test 1:"))
test2 = int(input("Test 2:"))
obj = Clients(stud,test1,test2)
obj.compare()
obj.inputsMarks()