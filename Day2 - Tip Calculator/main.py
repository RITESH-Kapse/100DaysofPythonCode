print("Welcome to the tip calculator")

total_bill = input("How much was the total bill ?")

tip_precentage = input("What percentage of tip did you give ? 10  12 or 15 ?")

total_people = input("How many people are splitting the bill ?")

total_tip = int(tip_precentage)*int(total_bill)/100

new_bill = int(total_bill)+  total_tip

final_calculation = round(new_bill/int(total_people),2)

print(f"Each person should pay: ${final_calculation}")


