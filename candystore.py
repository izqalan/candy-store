import sys, time
sos = "1 : Billing Info \n2 : candy Flavor \n3 : Amount & Packaging \n0 : for summary \ntype sos for help"
print "welcome to our program"

#-----MANDATORY--------

time.sleep(1)
name =raw_input("\nName\n")
address = raw_input("Address\n")
cell = raw_input('phone number\n')

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
    
#+++++++++++++PACK.MANDATORY+++++++++++++
time.sleep(0.5)
print "Jar(100g) or Bag(50g)"
while 1:
    pack = raw_input("which type of packaging do you prefer [NO CAPS]")
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
    yn = raw_input('do you want custom made label ? y/n [NO CAPS]')
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
while 1:
    func = raw_input("choose function")
    
    if func == '0':
        if name == '' and address == '' and cell == '':
            print "pls"
            continue
        else:
            break

    elif func == 'help':
        print sos
        
    elif func == '1':
        time.sleep(1)
        name =raw_input("Name\n")
        address = raw_input("Address\n")
        cell = raw_input('phone number\n')
        
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
            pack = raw_input("which type of packaging do you prefer [NO CAPS]")
            if pack == "jar" or pack == "Jar":
                pricepack = (weight/0.1) * 1.5
                break
            elif pack == "Bag" or pack == "bag":
                pricepack = (weight/0.05) * 0.6
                break
            else:
                print 'invalid'
            
        while 1:
            yn = raw_input('do you want custom made label ? y/n [NO CAPS]')
            if yn == 'y' or yn == 'Y':
                nlabel = input('how many ?')
                label = raw_input("what is it ? ")
                pricepack = pricepack + (0.2 * nlabel)
                print "type sos for help"
                break
            elif yn == 'n' or yn == 'N':
                label = "N/A"
                nlabel = "N/A"
                print "type sos for help"
                break
            else:
                print 'invalid'

                   
#----------------------------------CALCULATION----------------------------
time.sleep(0.5)
print "processing"
time.sleep(1)

if weight == 5:
    price = 35.0 + pricepack
elif weight > 5 and weight <= 7:
    price = (weight - 5)*33.5 + 35.0 + pricepack
elif weight >= 8 and weight <= 9:
    price = (weight-7)*31.5 + 35.0 + (2*33.5) + pricepack
elif weight >= 10 and weight <= 11:
    price = (weight - 9)*30.0 + 35.0 + (2*33.5) + (2*31.5) + pricepack
elif weight >= 12 and weight <= 14:
    price =(weight - 11)*27.0 + 35.0 + (2*33.5) + (2*31.5) + (2*30.0) + pricepack
else:
    price = (weight - 14)*25.0 + 35.0 + (2*33.5) + (2*31.5) + (2*30.0) + (3*27.0) + pricepack


gst = price * 0.06

price = price + gst


#----------------------SUMMARY-----------------------------

print name#name
print cell#cell
print address#address
print flav#flav
print weight#weight
print pack#pack
print label#label
print nlabel#nlabel
print gst#gst
print pricepack
print "RM", price#price


#-----------------------TERMINATE-----------------
def main(out):
    print "system will termminate in 3s"
    time.sleep(3)
    sys.exit("Thank you, for using our program.")




