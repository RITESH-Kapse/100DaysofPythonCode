year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0 :
    if year % 400 == 0:
      print("Year is Leap Year")
    else:
      print("Not a Leap year !")
  else:
     print(" Year is Leap Year")
else:
  print("Not a Leap year !")

