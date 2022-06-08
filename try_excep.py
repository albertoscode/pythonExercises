#In this example the firstName has not been defined 
# therefore the code raises an exception and prints the message: There is an exception!

"""try:
  print(firstName)
except:
  print("There is an exception!")"""
  
  
#Example using the NameError exception type

"""try:
  print(firstName)
except NameError:
  print("firstName variable has not been defined")
except: 
    print("There is another problem, please check and try again")"""


#Examples with else

"""try:
  print("Alberto")
except NameError:
  print("variable has not been definied")
else: 
    print("System is OK")"""
    
#if the code raises an exception, then the "ELSE" statement is not executed
    
"""try:
  print(firstName)
except NameError:
  print("variable has not been definied")
else: 
    print("System is OK")"""

#Examples with finally statement
#the "FINALLY" statement will always be executed

"""try:
  print("Alberto")
except NameError:
  print("firstName variable has not been defined")
finally:
    print("The try and except were executed and the finally statement too")"""


#Even if the code does or does not raise an exception, the "FINALLY" statement will be executed too

"""try:
  print(firstName)
except NameError:
  print("firstName variable has not been defined")
finally:
    print("The try and except were executed and the finally statement too")"""
    
    
  
