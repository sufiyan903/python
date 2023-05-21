food_rating = int(input("Food Rating (1-5): "))
service_rating = int(input("Service Rating (1-5): "))
ambience_rating = int(input("Ambience Rating (1-5): "))
bill_amount = float(input("Bill Amount: "))

if food_rating >= 4 and service_rating >= 4 and ambience_rating >= 4:
    tip = 0.1 * bill_amount  # 10% tip for good or excellent food with good or excellent service and ambience
elif food_rating >= 4 or service_rating >= 4 or ambience_rating >= 4:
    tip = 0.05 * bill_amount  # 5% tip for good or excellent food with average/okay/bad service or ambience
else:
    tip = 0.01 * bill_amount  # 1% tip for average/okay/bad food with average/okay/bad service and ambience

print("Tip Amount: ", tip)
