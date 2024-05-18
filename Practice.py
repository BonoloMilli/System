money = 1600
def food(amount):
   expense = amount - 300
   return expense
def invest(amount):
    increase = amount + 150
    return increase

print("Hello your initial balance is :R",money," After buying food you will be left with ",food(money))
print("After you invest your money your total will be :R",invest(food(money)))


if(invest(food(money)) == 1650):
    print("you managed invest and gain a little money even though it is not equal to the initial amout")
elif(invest(food(money)) < 1650):
    print("You wasted money bruh")


list = [10,5,5]
print(len(list))

list[1] = 10
print(list)

list.append(25)
print(list)

del(list[0])
print(list)


dict = {"Tlotliso": 2000,"Phantsha": 2020}

print(dict["Phantsha"])
print(dict.keys())
print(dict.values())

print("Tlotliso" in dict)


lists = [10,20,30]
i = 0
for list in lists:
    print(list)
    i = i+1
    print(i)

class mpeoa(object):

   def display(name):
     alert = print("Hello im working")
     return alert
Tlotliso = "Tlotliso"
show = mpeoa("Tlotliso")
