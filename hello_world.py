#print("Hello Python world!")
#message = "Hello Python world!"
#print(message)
#message = "Hello Python Crash Course world!"
#print(message)
#message = 'I told my friend,"Python is my favorite language!"'
#print(message)
#message = "The language 'Python' is named after Monty Python,not the snake"
#print(message)
#message = "One of Python's strengths is its diverse and supportive communtity."
#print(message)
#name = "ada lovelacce  "
#print(name.title())
#print(name.lower())
#print(name.upper())
#print(name.rstrip())
#print(name)
#print(3*0.1)
#print(16/2)
#print((1+3)*2)
#print(2*2+2*2)
#print(4*4/2)
#bicycles=['trek','cannondale',"rediline","specialized"]
#print(bicycles)
#print(bicycles[0].title())
#print(bicycles[-1].title())
#if(bicycles[-1].title() == bicycles[0].title()):
#	print("same")
#else:
#	print("different")
	
#squares = []
#for value in range(1,11):
#	square= value**3
#	squares.append(square)
	
#print(squares)

#squares1 = [value **2 for value in range(1,11)]
#print(squares1)

#for value in range(1,21):
#	print(value)

#for value in list(range(1,101)):
#	print(value)

#listNum=range(1,21)
#print(min(listNum))
#print(max(listNum))
#print(sum(listNum))

#listNum2 = list(range(1,21,3))
#Sprint(listNum2)

#listNum3 = list(range(3,31,3))
#for value in listNum3:
#	print(value)
	
#cars = ['audi','bmw','subaru','toyota']
#for car in cars:
#	if(car=='bmw'):
#		print(car.upper())
#	else:
#		print(car.title())
		
#user_0 = {
#	'username' : 'efermi',
#	'first' : 'enrico',
#	'last' : 'fermi',
#	}
#for key,value in user_0.items():
#	print("\nKey: "+key)
#	print("Value: "+value)
#for key in user_0.values():
#	print(key)	

#pizza = {
#	'crust':'thick',
#	'toppings':['mushrooms','extra cheese'],
#	}
#print("you ordered a " + pizza['crust'] + "-crust pizza " + 
#	"with the following toppings")
#for topping in pizza['toppings']:
#	print("\t" + topping)
	
#print(len(pizza))

#age = input("how old are you ?")
#print(age)
##	print("Welcome to Bar !")
#else:
#	print("Sorry, You cannot come in !")

def get_formatted_name(first_name,last_name):
	full_name = first_name + "" + last_name
	return full_name
	
while True:
	print("Please tell me your name:")
	print("(enter 'q' at any time to quite)")
	f_name = input("First name:")
	if(f_name == 'q'):
		break
	l_name = input("Last name:")
	if(l_name == 'q'):
		break
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")














