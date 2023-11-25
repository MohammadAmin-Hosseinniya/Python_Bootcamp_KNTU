name = input('Name : ')
gender = input('Whats your gender? ("m" for man and "w" for woman) : ')
age = int(input('How old are you?'))

def greeting(name , gender , age) :
    if gender == 'm':
        payam = """Hi, Mr. {} Welcome to our python bootcamp.
You are {} years old now and We hope you'll be a great Python programmer by the time you're {}""".format(name, age, age+2)
        print(payam)
    elif gender == 'w':
        payam = """Hi, Miss. {} Welcome to our python bootcamp.
You are {} years old now and We hope you'll be a great Python programmer by the time you're {}""".format(name, age, age+2)
        print(payam)
    else :
        print('we dont have your gender yet!')


greeting(name , gender , age)