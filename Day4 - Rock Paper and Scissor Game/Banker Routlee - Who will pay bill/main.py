import random

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(",")

"""Method 1"""

#num_items = len(names)
#rand_choice = random.randint(0 , num_items-1)
#person_who_pay = names[rand_choice]

"""Method 2"""
person_who_pay = random.choice(names)

print(f"{person_who_pay} is going to pay the bill today !")




