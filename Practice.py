class TakeDetails:
    def __init__(self, name, surname, idNum):
        self.name = name
        self.surname = surname
        self.idNum = idNum

    def register(self):
        clientName = self.name
        clientSurname = self.surname
        return clientName, clientSurname

    def idConfirm(self):
        if self.idNum.isdigit() and len(self.idNum) == 13:
            print("ID number is valid.")
        else:
            print("Your ID number is invalid.")


class addToClient:
    def __init__(self, name, surname, idNum):
        self.name = name
        self.surname = surname
        self.idNum = idNum

    def add(self):
        clients = []
        clients.append(self.name)
        clients.append(self.surname)
        clients.append(self.idNum)
        client_tuple = (clients[0], clients[1], clients[2])
        return client_tuple
    idNum = int
    check = int

    while check != 0:


        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        idnum = input("Enter your ID number: ")
        check = input("Enter your Lucky")


name = str
surname = str
idnum = int

reg = TakeDetails(name, surname, idnum)
reg.register()
reg.idConfirm()

dic = addToClient(name, surname, idnum)
client_tuple = dic.add()
ClientDic = {"Client": client_tuple}

print("Here are your clients:", ClientDic["Client"])

