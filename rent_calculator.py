# Rent Calculator Project

print("========== RENT CALCULATOR ==========\n")

total_rent = int(input("Enter total rent of the room/house: "))
food_bill = int(input("Enter total food bill: "))
electricity_units = int(input("Enter electricity units used: "))
price_per_unit = int(input("Enter price per unit: "))
other_expense = int(input("Enter any other expense (0 if none): "))
persons = int(input("Enter number of persons living: "))

electricity_bill = electricity_units * price_per_unit

total_amount = total_rent + food_bill + electricity_bill + other_expense

per_person = total_amount / persons

print("\n----------- BILL DETAILS -----------")
print("House Rent       :", total_rent)
print("Food Bill        :", food_bill)
print("Electricity Bill :", electricity_bill)
print("Other Expense    :", other_expense)
print("------------------------------------")
print("Total Amount     :", total_amount)
print("Each Person Pays :", round(per_person, 2))
print("------------------------------------")