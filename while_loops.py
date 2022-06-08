
#temperature = 74

#while temperature < 77:
#    print(temperature)
#    temperature +=1
    


"""
the following example include "break" 
"""    



#temperature = 50

#while temperature <= 77:
#    print(temperature)
#    if temperature >= 76:
#        break
#    temperature +=1
    
    
    
"""
Another example with break
"""    

#temperature = 78

#while temperature <= 80:
#    print(temperature,"Degrees, temperature is normal" )
#    temperature +=1
#    if temperature > 80:
#        print("")
#        print(temperature, "Dregrees")
#        print("")
#        print("WARNING temperature is above 80", "Dregrees")
#        print("System is turning off...")
#        print("System is OFF")
#        break
#    print("System is OK")
#
#print("System is out of service")
  
   
   
   
"""
This an example with continue
"""  



temperature = 75

while temperature <= 83:
    print(temperature,"Degrees, temperature is normal" )
    temperature +=1
    if temperature >=80 and temperature <=82:
        print("")
        print("System checking...")
        print(temperature,"Degrees, temperature is going up" )
        print("System OK...")
        print("")
        continue
        
    if temperature >= 82:
        print(temperature,"Degrees, temperature is higt" )
        print("System checking...")
        print("System failure")
        print("")
        print("System is turning off...")
        print("System is OFF")
        print("")
        break
    
    print("System is OK")
    
print("System is out of service now")




"""
This an example with else
"""  



#temperature = 75

#while temperature <= 80:
#    print(temperature)
#    temperature +=1
#else:
#    print(temperature)
#    print("temperature is above 80")