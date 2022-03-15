exchange = 3.28
months = 12
salary = int(input("Please input potential salary  "))
monthly = salary / months
print(monthly)
print(exchange * monthly)
print("This is your monthly in dollars and in shekels.")
maxrent = int(input("What is your maxium expected local rent?"))
minrent = int(input("What is your lowest expected local rent?"))
if maxrent > monthly:
    print("You don't have enough for your max rent")
else:
    print("You have enough for your max rent")
if minrent > monthly:
    print("You are way too poor for this shit")
else:
    print("you can afford your minimum rent")
