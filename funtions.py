#this is a simple example of a function in Python

"""def cities():
    print("New York", "San Francisco", "Boston")
    
cities()"""


#the following is an example of a function with one parameter(variable), therefore, 
#this function can only accept one argument(value)

"""def location(city):
    print(city, "is in the US")
    print("")

location("Boston")
location("Los Ángeles")"""


#the following is an example of a function with two parameters(variables), therefore, 
#this function can only accept two argument(value)

"""def info(capital, state):
    print(capital, "is the capital of", state)
    print("\n")

info("Boston", "Massachusetts")
info("Sacramento", "California")"""


#the following is an example of a function with Arbitrary Arguments


"""def travel(*city):
    print("We have been to", city[1] )
    print("\n")

travel("Los Ángeles","New York")

travel("Boston","New York", "San Francisco")"""


#the following is an example of a function with positional Arguments


"""def info(city, state):
    print(city,"is the capital of", state)
    print("\n")
    
info("Tallahassee", "Florida")"""


#the following is an example of a function with key Arguments

"""def info(city, state):
    print(city,"is the capital of", state)
    print("\n")
    

info(city="Sacramento",state="California")

info(city="Tallahassee",state="Florida")"""

#the following is an example of a function using default values

"""def info(city, state= "Florida"):
    print(city,"is located in", state)
    print("\n")
    

info("Tallahassee")

info("Sacramento", "California")"""

#the following is an example of a function using None to make an argument optional

"""def info(city, state=None):
    print("I have been to " + city + "\n")
    
    if state:
        print(city+" is the capital of " + state + "\n")
        print("****************END********************\n")
    else:
        print("************IMPORTANT****************")
        print("***SYSTEM DID NOT GET ANY STATE***")
        print("***THE SYSTEM IS SHUTTING DOWN***")
        print("***SYSTEM IS OFF***")
        print("************************************\n")
   
info("Tallahassee")

info("Tallahassee", "Florida")

info("Sacramento", "California")"""


#the following is an example of a function using return statement

def aircraft(type, location):
    aircraft_info= "The aircraft type is "+ type + " and it is located in " + location
    return aircraft_info

aircraft_details=aircraft("TURBOPROP", "CALIFORNIA")
print(aircraft_details)

