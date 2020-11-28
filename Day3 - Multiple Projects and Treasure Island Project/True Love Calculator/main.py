
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Below is the method using for loops 

"""
name1_lower = name1.lower()
name2_lower = name2.lower()

True_Count = 0
Love_Count = 0

for n in name1_lower:
  if n == 't':
    True_Count +=1
  if n =='r':
    True_Count +=1
  if n =='u':
    True_Count +=1
  if n =='e':
    True_Count +=1

for m in name2_lower:
  if m == 't':
    True_Count +=1
  if m =='r':
    True_Count +=1
  if m =='u':
    True_Count +=1
  if m =='e':
    True_Count +=1

for n in name1_lower:
  if n == 'l':
    Love_Count +=1
  if n =='o':
    Love_Count +=1
  if n =='v':
    Love_Count +=1
  if n =='e':
    Love_Count +=1

for m in name2_lower:
  if m == 'l':
    Love_Count +=1
  if m =='o':
    Love_Count +=1
  if m =='v':
    Love_Count +=1
  if m =='e':
    Love_Count +=1

#print(True_Count)
#print(Love_Count)
Love_Score = str(True_Count)+ str(Love_Count)
print(f"Your love score is {Love_Score}")

"""

"""Below is more effective and the alternate method using count function"""

combined_name = name1 + name2
combined_name_lower = combined_name.lower()

t = combined_name_lower.count("t")
r = combined_name_lower.count("r")
u = combined_name_lower.count("u")
e = combined_name_lower.count("e")

true = t + r + u + e

l = combined_name_lower.count("l")
o = combined_name_lower.count("o")
v = combined_name_lower.count("v")
e = combined_name_lower.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score >90):
  print(f"Your love score is {love_score},you go together like coke and mentos")

elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your love score is {love_score}")
