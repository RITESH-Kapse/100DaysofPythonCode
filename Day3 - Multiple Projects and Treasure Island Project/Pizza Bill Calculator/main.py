
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total = 0

if size == 'S':
  total += 15
  if add_pepperoni == 'Y':
    total +=3
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total
  else :
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total

elif size == 'M':
  total += 20
  if add_pepperoni == 'Y':
    total +=3
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total
  else :
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total


elif size == 'L':
  total += 25
  if add_pepperoni == 'Y':
    total +=3
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total
  else :
    if extra_cheese == 'Y':
      total +=1
    else:
      total = total




print(f"Your total bill is {total}")


