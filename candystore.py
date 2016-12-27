sos = "1 : Billing Info \n2 : candy Flavor \n3 : Amount & Packaging \n0 : for summary"
print sos

#-----FORCE--------


name =raw_input("\nName\n")
address = raw_input("Address\n")
cell = raw_input('phone number\n')




while 1:
    func = raw_input("choose function")
    
    if func == '0':
        break

    elif func == 'help':
        print sos
        
    elif func == '1':
        name =raw_input("Name\n")
        address = raw_input("Address\n")
        cell = raw_input('phone number\n')
        
    elif func == '2':
        print "Choose 1 flavour ONLY\n"
        print "APPLE\t KIWI\t CHERRY COLA\t PASSION FRUIT\t WILDBERRY\n"

        flav = {
            "apple",
            "kiwi",
            "cherry cola",
            "passion fruit",
            "wildberry",
            }
        while 1:
            flav = raw_input("Which one do you like [NO CAPS]\n")
            if flav == 'apple' or flav == 'kiwi' or flav == 'cherry cola' or flav == 'passion fruit' or flav == 'wildberry' :
                break
            else:
                print 'invalid'
    
    elif func == '3':               #pricepack
        weight = 0.0
        weight = input('Amount (kg)')
        while weight < 5:
            weight = input('In must be 5kg or more\n ')
        while 1:                            #use 1 for endless loop
            yn = raw_input("Are you sure this is the right amount? (Y/N)\n")
            if yn ==  "N" or yn == "n":
                weight = input('Amount (kg)')
                while weight < 5:
                    weight = input('In must be 5kg or more\n ')
            elif yn == "Y" or yn == "y":
                break
#-----------PACKAGING------------------PACKAGING-------------------PACKAGING--        

        print "Jar(100g) or Bag(50g)"
        while 1:
            pack = raw_input("what type of packaging do you prefer")
            if pack == "jar" or pack == "Jar":
                pricepack = (weight/0.1) * 1.5
                break
            elif pack == "Bag" or pack == "bag":
                pricepack = (weight/0.05) * 0.6
                break
            else:
                print 'invalid'
            
        while 1:
            yn = raw_input('do ye want custom made label ?')
            if yn == 'y' or yn == 'Y':
                nlabel = input('how many ?')
                label = raw_input("what is it ?")
                pricepack = pricepack + (0.2 * nlabel)
                break
            elif yn == 'n' or yn == 'N':
                break
            else:
                print 'invalid'
                   
#----------------------------------CALCULATION----------------------------  
print 'calculation'

if weight <= 5:
    price = (weight * 35.0) + pricepack
elif weight > 5 and weight <= 7:
    price = (weight - 5)*33.5 + (5*35.0) + pricepack
elif weight => 8 and weight =< 9:
    price = (weight-7)*31.5 + (5*35.0) + (2*33.5)
elif

