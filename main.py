# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenth_of_name=len(names)
choice=random.randint(0,lenth_of_name-1)

print(f"{names[choice]} is going to buy the meal today! \nHave a fun with friends")
