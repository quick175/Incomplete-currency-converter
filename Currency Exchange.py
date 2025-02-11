#errors here and there.don't use this garbage
#currency values done-ETB,SAR,IDR,PHP,usd,gbp
#varblud if b2s var sigma if s2b
print("Hello and welcome to the Currency Exchange program!")
print("List of all available exchange rate \nGBP,USD,SAR,ETB,IDR,PHP")
print("Values from 8/2/25")
dummylist = "GBP,USD,SAR,ETB,IDR,PHP"
choice1 = str(input("Choose a currency to start with  ==> ").upper())
choice2 = str(input("Choose another currency ==> ").upper())
if choice1 == choice2:
	print("you trolling \nyou dont deserve to be here...........")
	exit()
if choice1 in dummylist and choice2 in dummylist:
	pass
else:
	print("go away")
	print("if you would like to use the program then plz input only the available currencies")
	exit()
ETB_PHP = 0.460308
PHP_ETB = 2.17246
IDR_USD = 0.0000612407
USD_IDR = 16329
GBP_IDR = 20259.2
IDR_GBP = 0.0000493603
IDR_PHP = 0.0036
PHP_IDR = 281.04
USD_ETB = 126.248
ETB_USD = 0.00792093
ETB_GBP = 0.00638507
GBP_ETB = 156.615
IDR_ETB = 0.00773158
ETB_IDR = 129.34
SAR_ETB = 34.14
ETB_SAR = 0.029
sar_usd = 3.75
USD_SAR = 0.27
GBP_SAR = 4.67
SAR_GBP = 0.22
IDR_SAR = 0.000230328
SAR_IDR = 4341.63
PHP_SAR = 0.064
SAR_PHP = 15.51
GBP_USD = 1.24
USD_GBP = 0.81
PHP_GBP = 0.014
GBP_PHP = 71.99
PHP_USD = 0.017
USD_PHP = 58.14

"""blud = 0.000
examp = float('nan')
exchange_b2s= blud * examp
sigma_s2b = blud /examp"""

if choice1 and choice2 == str:
	print("Welcome!")

else:
	print("you do not deserve to be here")
	exit()


if choice1 == "SAR" and choice2 == "USD":
	amount=input("How many riyals would you like to spend ==> ")
	final= float(amount) * sar_usd
	print(final)


if choice1 == "USD" and choice2 == "SAR":
	amount=input("How many dollars would you like to spend ==> ")
	final = float(amount) /USD_SAR
	print(final)

if choice1 == "GBP" and choice2 == "SAR":
	amount=input("How many pounds would you like to spend m8 ==> ")
	final = float(amount) / GBP_SAR
	print(final)

if choice1 == "SAR" and choice2 == "GBP":
	amount=input("How many riyals would you like to spend ==> ")
	final = float(amount) * SAR_GBP
	print(final)

if choice1 == "SAR" and choice2 == "PHP":
	amount = input("How many riyals would you like to spend ==> ")
	final = float(amount) / SAR_PHP
	print(final)

if choice1 == "PHP" and choice2 == "SAR":
	amount = input("How many pesos would you like to spend ==> ")
	final = float(amount) * PHP_SAR
	print(final)

