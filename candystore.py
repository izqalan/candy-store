

print "please enter your shipping details"

name = raw_input("Name\n")
address = raw_input("Address\n")
cell = raw_input('Phone Number\n')

while 1:                                #use 1 for endless loop
    yn = raw_input("Are you sure the information are correct? (Y/N)\n")
    if yn ==  "N" or yn == "n":
        name =raw_input("Name\n")
        address = raw_input("Address\n")
        cell = raw_input('phone number\n')
        
    elif yn == "Y" or yn == "y":
        break

#----------------------choosing candy---------------------------------

    
print "Choose 1 flavour ONLY\n"
print "APPLE\t KIWI\t CHERRY COLA\t PASSION FRUIT\t WILDBERRY\n"
flav = raw_input('which flavour do you like? [NO CAPS]\n')
while flav != 'apple' or flav != 'kiwi' or flav != 'cherry cola' or flav != 'passion fruit' or flav != 'wildberry':
    print 'INVALID | check your keyword!!!'
    flav = raw_input('which flavour do you like? [NO CAPS]\n')
    
    if flav == 'apple' or flav == 'kiwi' or flav == 'cherry cola' or flav == 'passion fruit' or flav == 'wildberry':
        break



#----------------------How much---------------------------------------

    
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

#--------------------packaging----------------------------------------

pack = raw_input('jar or bag [NO CAPS]')
if pack == 'jar':
    packprice = 1.5  #100 grams per jar
elif pack == 'bag':
    packprice == 0.6  #50 grams per bag


    



