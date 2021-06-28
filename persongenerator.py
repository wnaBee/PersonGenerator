import card_num_gen
import random
import datetime
import nameenum

def birthdate():
	months = ["january", "february", "march", "april", "may", "june", "july",\
		  "august", "september", "october", "november", "december"]
	age = random.randint(14, 80)
	year = datetime.datetime.now().year - age
	month = random.randint(1,12)

	if month == 2:
		day = random.randint(1, 28)
	elif (month == 4 | month == 6 | month == 9 | month == 11):
		day = random.randint(1, 30)
	else:
		day = random.randint(1, 31)

	return months[month - 1], day, month, year, age

Fname, sex = nameenum.firstname()
Ename = nameenum.lastname()
Birthmonthname, birthday, birthmonth, birthyear, age = birthdate()

print("Sex:", sex)
print("Name:", Fname, Ename)
print("Initials:",Fname[0] + "." + Ename[0] + ".\n")

print("Age:", age)
print("Birth month:", Birthmonthname)
print("Birthdate: " + str(birthday) + "/" + str(birthmonth) + "/" + str(birthyear) + "\n")
6
creditnum, cardtype = card_num_gen.generate_card()
print("credit card:", cardtype)
print("card number:", creditnum)
print("CVV:", random.randint(100,999))
print("Expiry date: " + str(random.randint(1,12)) + "/" + str(datetime.datetime.now().year + random.randint(0, 5))[2:])

