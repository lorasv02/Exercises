
kg_or_lbs = input ("kg or lbs")

if "kg" in kg_or_lbs:
    kg_weigth = input ("What is your weigth?")
    weigth_in_lbs = float(kg_weigth) * 2.205
    print (f"Your weigth is {weigth_in_lbs} lbs")

elif "lbs" in kg_or_lbs:
    lbs_weigth = input ("What is your weigth?")
    weigth_in_kg = float(lbs_weigth) / 2.205
    print (f"Your weigth is {weigth_in_kg} kg")

