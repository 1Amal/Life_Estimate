# Created by Amal Kariyawasam from Melbourne, Australia on 30/04/2022 :-)
# I love coding and doing this to learn and improve my coding skills !
# Description of program: Life estimate using Python based on concept "Your life in weeks https://waitbutwhy.com/2014/05/life-weeks.html ""

print("This is a fun little Python program to estimate how much time left in your life based on your current age !")
print("Assumption is that you will live till age 90 ! Also assumed that 365 Days in a year, 30 Days in a month, 7 Days to a week :-)")
age = input("What is your current age?")
name=input("What is your name? ")

yearsLeft=90-int(age) # Code to calculate years left
monthsLeft=int(yearsLeft*12) # Code to calculate months left based on 12 months per year
weeksLeft=int(monthsLeft*4) # Code to calculate weeks left based on 4 weeks a month 
daysLeft=int(weeksLeft*7) # Code to calculate days left based on 7 days per week
print(f"'{name}', based on your current age of {age} You have {yearsLeft} years, {monthsLeft} Months, {weeksLeft} Weeks, {daysLeft} Days left till you reach age 90, life is too short mate, better enjoy it :-) ")

#End of code
