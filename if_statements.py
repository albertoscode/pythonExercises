
#produt_cost = 1200
#money_available = 430

#if produt_cost > money_available:
#    print("you don't have enough money to buy this product") 



#produt_cost = 1
#money_available = 2500

#if produt_cost > money_available:
#    print("you don't have enough money to buy this product")

#else:
#    print("Please contact customer service")



#produt_cost = 2600
#money_available = 2600

#if produt_cost > money_available:
#    print("you don't have enough money to buy this product")

#elif produt_cost < money_available:
#    print("you can buy this product")
 
#else:
#    print("Please contact customer service")   
  
  
    
#produt_cost = 2500
#money_available = 2500

#if produt_cost > money_available:
#    print("you don't have enough money to buy this product")

#elif produt_cost < money_available:
#    print("Great! you can buy this product")

#elif produt_cost == money_available:
#    print("you can buy this product")   
 
#else:
#    print("Please contact customer service")
    


#produt_cost = 0
#money_available = 3500

#if produt_cost > money_available:
#    print("you don't have enough money to buy this product")
    
#elif produt_cost <= money_available and produt_cost == 0:
#    print("this product is for FREE!")
    
#elif produt_cost <= money_available:
#    print("Good news! you can buy this product") 

#else:
#    print("Please contact customer service")
    


"""
The following is an example of short hand for one line if staments
"""

#produt_cost = 3600
#money_available = 3500

#print("you cannot buy this") if produt_cost > money_available else print("please wait")



#produt_cost = 0
#money_available = 3500

#print("Buy it") if produt_cost <= money_available else print("cannot buy it")



"""
The following is an example of ternary operators or conditional expressions
"""



#produt_cost = 0
#money_available = 3500

#print("Product is for free") if produt_cost <= money_available and produt_cost == 0 else print("Buy it") if produt_cost <= money_available else print ("Cannot buy it")


"""
The following is an example of nested if staments
"""

temperature = 71

if temperature >= 65 and temperature <= 75:
    print("temperature is normal")
    if temperature >= 70 and temperature <= 75:
        print("but it's getting warm")
else:
    print("temperature warning!")
        

        