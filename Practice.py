
class Clients(object):
   
   
    def __init__(self, studentNum,mark1,mark2):
        self.studentNum = studentNum
        self.mark1 = mark1
        self.mark2 = mark2
    def compare(self):
        students = [("214"), ("265"), ("256"), ("245"), ("888"), ("254")]
        stuMarks = []
        if self.studentNum not in students:
            print("You are not in the system")
        else:
              print("WELCOME BACK")
              
        for i,student in enumerate(students):
         if  student == self.studentNum:
             stuMarks[i] = self.mark1
             stuMarks[i] = self.mark2
             print(f"{self.studentNum} {self.mark1} {self.mark2}") 
         else:
                ("Invalid marks/s")
                                

stud = int(input("Enter Student Number:"))
test1 = int(input("Test 1:"))
test2 = int(input("Test 2:"))
obj = Clients(stud,test1,test2)
obj.compare()