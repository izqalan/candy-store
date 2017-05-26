import sys, time

print "welcome to our program"

def sos():
    print "1 : Billing Info \n2 : candy Flavor \n3 : Amount & Packaging \n0 : for summary"
    
def terminate():
    print "system will termminate in 3s"
    time.sleep(3)
    sys.exit(0)


def summary():
    print '____________________________________________________________________________'
    print
    print """
            _____.___.                     .__  __                  
            \__  |   | ____  __ _________  |__|/  |_  ____   _____  
             /   |   |/  _ \|  |  \_  __ \ |  \   __\/ __ \ /     \ 
             \____   (  <_> )  |  /|  | \/ |  ||  | \  ___/|  Y Y  |
             / ______|\____/|____/ |__|    |__||__|  \___  >__|_|  /
             .


            """
   
          

    print "\t\t\t\t Menu"
    print "\t\t\t\t Name: ",name #name
    print "\t\t\t\t CELL-NUMBER :", cell #cell
    print "\t\t\t\t ADDRESS :", address #address
    print "\t\t\t\t CANDY FLAVOR :", flav #flav
    print "\t\t\t\t WEIGHT :" ,weight ,'Kg' #weight
    print "\t\t\t\t TYPE OF PACK :", pack#pack
    print "\t\t\t\t LABEL MESSAGE :", label #label
    print "\t\t\t\t NUMBER OF LABEL :", nlabel #nlabel
    print "\t\t\t\t GST :", gst #gst
    print "\t\t\t\t PRICE PACK :", pricepack
    print "\t\t\t\t[TOTAL PRICE] :", "RM",price #price
    print "\n____________________________________________________________________________"
    print """
                                              ^====^
                 Thank you                \  {0 ~~ 0)  /
                                           \  |----|  /
         ^====^                             \|  ==  |/
     \  {0 ~~ 0)  /     for choosing us
      \  |----|  /
       \|  ==  |/            ^====^
                         \  {0 ~~ 0)  /
                          \  |----|  /
                           \|  ==  |/   As your best candy stoooore!
    """


#-----MANDATORY--------
time.sleep(1)
name =raw_input("\nName\n")
address = raw_input("Address\n")
cell = raw_input('phone number [Numeric Only]\n')

#+++++++++++FLAV.MANDATORY+++++++++++
time.sleep(0.5)
print "Choose 1 flavour ONLY\n"
time.sleep(0.5)
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

#+++++++++++++++AMOUNT.MANDATORY+++++++++++++
    
time.sleep(1)
weight = 0.0
weight = input('Amount (kg)\n')
while weight < 5:
    weight = input('In must be 5kg or more\n ')
while 1:                            #use 1 for endless loop
    yn = raw_input("Are you sure this is the right amount? (Y/N)\n")
    if yn ==  "N" or yn == "n":
        weight = input('Amount (kg)\n')
        while weight < 5:
            weight = input('In must be 5kg or more\n ')
    elif yn == "Y" or yn == "y":
        break
    
#+++++++++++++PACK.MANDATORY+++++++++++++
time.sleep(0.5)
print "Jar(100g) or Bag(50g)\n"
while 1:
    pack = raw_input("which type of packaging do you prefer [NO CAPS]\n")
    if pack == "jar" or pack == "Jar":
        pricepack = (weight/0.1) * 1.5
        break
    elif pack == "Bag" or pack == "bag":
        pricepack = (weight/0.05) * 0.6
        break
    else:
        print 'invalid'
time.sleep(0.5)      
while 1:
    yn = raw_input('do you want custom made label ? y/n [NO CAPS] ')
    if yn == 'y' or yn == 'Y':
        nlabel = input('how many ?')
        label = raw_input("what is it ? ")
        pricepack = pricepack + (0.2 * nlabel)
        break
    elif yn == 'n' or yn == 'N':
        label = "N/A"
        nlabel = "N/A"
        break
    else:
        print 'invalid'

#-----MANDATORY-END------------------------------------------------------
#--------------Customer.Information.loop--------------------------------
while 1:
    print "type help for help"
    func = raw_input("choose function ")
    
    if func == '0':
        if name == '' or address == '' or cell == '':
            print "please Insert your shipping info"
            continue
        else:
            break

    elif func == 'help':
        sos()
        
    elif func == '1':
        time.sleep(1)
        name =raw_input("Name\n")
        address = raw_input("Address\n")
        cell = raw_input('phone number [Numeric Only]\n')
        
    elif func == '2':
        time.sleep(0.5)
        print "Choose 1 flavour ONLY\n"
        time.sleep(0.5)
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
        time.sleep(1)
        weight = 0.0
        weight = input('Amount (kg)\n')
        while weight < 5:
            weight = input('In must be 5kg or more\n ')
        while 1:                            #use 1 for endless loop
            yn = raw_input("Are you sure this is the right amount? (Y/N)\n")
            if yn ==  "N" or yn == "n":
                weight = input('Amount (kg)\n')
                while weight < 5:
                    weight = input('In must be 5kg or more\n ')
            elif yn == "Y" or yn == "y":
                break
            
#-----------PACKAGING------------------PACKAGING-------------------PACKAGING--        

        print "Jar(100g) or Bag(50g)"
        while 1:
            pack = raw_input("which type of packaging do you prefer [NO CAPS]\n")
            if pack == "jar" or pack == "Jar":
                pricepack = (weight/0.1) * 1.5
                break
            elif pack == "Bag" or pack == "bag":
                pricepack = (weight/0.05) * 0.6
                break
            else:
                print 'invalid'
            
        while 1:
            yn = raw_input('do you want custom made label ? y/n [NO CAPS] ')
            if yn == 'y' or yn == 'Y':
                nlabel = input('how many ?\n')
                label = raw_input("what is it ?\n")
                pricepack = pricepack + (0.2 * nlabel)
                break
            elif yn == 'n' or yn == 'N':
                label = "N/A"
                nlabel = "N/A"
                
                break
            else:
                print 'invalid'
           

                   
#----------------------------------CALCULATION----------------------------
time.sleep(0.5)
print "processing"
time.sleep(1)

if weight == 5:
    price = (weight * 35.0) + pricepack
elif weight > 5 and weight <= 7:
    price = (weight - 5)*33.5 + (5*35.0) + pricepack
elif weight >= 8 and weight <= 9:
    price = (weight-7)*31.5 + (5*35.0) + (7*33.5) + pricepack
elif weight >= 10 and weight <= 11:
    price = (weight - 9)*30.0 + (5*35.0) + (7*33.5) + (9*31.5) + pricepack
elif weight >= 12 and weight <= 14:
    price =(weight - 11)*27.0 + (5*35.0) + (7*33.5) + (9*31.5) + (11*30.0) + pricepack
else:
    price = (weight - 14)*25.0 + (5*35.0) + (7*33.5) + (9*31.5) + (11*30.0) + (14*27.0) + pricepack


gst = price * 0.06

price = price + gst


#----------------------SUMMARY-----------------------------

summary()

#-----------------------TERMINATE-----------------


while 1:
    out=raw_input('press 0 to exit the program ')
    if out == '0':
        terminate()
    else:
        print ''













