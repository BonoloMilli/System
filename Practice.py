class Clients(object):
    def __init__(self, studentNum):
        self.studentNum = studentNum

    def compare(self):
        students = ["214", "265", "256", "245", "888", "254"]
        if self.studentNum not in students:
            print("You are not in the system")

# Example usage
client = Clients("123")
client.compare()  # Output: You are not in the system

client = Clients("214")
client.compare()  # No output, since 214 is in the list
