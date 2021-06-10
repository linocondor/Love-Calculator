
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.lower()
name2 = name2.lower()
name3 = name1 + name2

T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")

true_sum = T + R + U + E 

L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")

love_sum = L + O + V + E

join = int(str(true_sum)+ str(love_sum))

if join < 10 or join > 90:
    
    print(f"Your score is {join}, you go together like coke and mentos")

elif join >= 40 and  join <=50:

    print(f"Your score is {join}, you are alright together.")
else:
    print(f"Your score is {join}.")



