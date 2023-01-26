#Week 02 Prove: Calling Functions
#By Raymund Antrone 01/11/23
# import math in order to access math.pi
import math
from datetime import date
current_date = date.today()
print()
print("File name: tire_volume")
print("This program computes and outputs the volume of a tire")
print("based on  its width, aspect ratio, and the diameter")
print("of the wheel it is  meant to fit.")
print()
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
top_formula = math.pi * (w**2) * a *(w * a +2540 *d)
v = round(top_formula/10000000000,2)
print()
print(f"""You entered a tire with the following dimensions:
Width: {w}
Aspect Ratio: {a}
Diameter {d}
A tire of that size will have an approximate volume of {v:.2f} liters""")
tire_price = None
if w == 265 and a == 40 and d == 21:
    tire_price = 247.64
elif  w == 265 and a == 70 and d == 16:
    tire_price = 159
elif  w == 245 and a == 50 and d == 20:
    tire_price = 152
elif  w == 215 and a == 55 and d == 17:
    tire_price = 78.93
elif  w == 215 and a == 45 and d == 17:
    tire_price = 73.63
elif  w == 235 and a == 50 and d == 18:
    tire_price = 95.67
elif  w == 225 and a == 65 and d == 17:
    tire_price = 112
if tire_price == None:
    with open ("volumes.txt", "at") as v_record:
        print (f"{current_date}, {w}, {a}, {d}, {v}", file=v_record)
else:
    print(f"We have a tire that will fit your car on sale for ${tire_price:.2f}.")
    user_choice = input("Would you be interested in purchasing a set? ")
    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        phone_number = input("Please enter your phone number: ")
        
        customer_name = input("And who should we ask for when we call? ")
        print("Wonderful! We'll be in touch soon to arrange for delivery and installation.")
        with open ("volumes.txt", "at") as v_record:
            print (f"{current_date}, {w}, {a}, {d}, {v}, {phone_number}, {customer_name}", file=v_record)
    else:
        with open ("volumes.txt", "at") as v_record:
            print (f"{current_date}, {w}, {a}, {d}, {v}", file=v_record)
            
print("That's the over all Sum of the tire statement")