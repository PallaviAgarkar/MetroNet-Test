import json
import re

regex = '^(\w|\.|\_|\-|\[0-9])+[@](\w|\_|\-|\.)+[.]\w{2,3}$'  ##format for email
regex1 = '^[0-9|\-]*$'                                        ##format for valid phone number containg only digits and dashes

## Function to verify valid phone number
def checkValidPhNo(phNo):
    phNo = ''.join(phNo.split(' '))             ## remove space from phNo
    if (re.fullmatch(regex1, phNo)):
        return True
    else:
        return False
   
## Function to verify valid Email address
def checkValidEmail(email):
    if (re.search(regex, email)):
        return True
    else:
        return False

## Function to print list on sepatate lines
def printOrder(conList):
    for i in range(0, len(conList)):
        print(conList[i])


## Read the contacts file
with open('contacts.json', 'r') as file:
    reader = json.load(file)
    contacts = list(reader)
    #print(contacts)

## create list to show validation record for contacts
contactList = []

for contact in contacts:
    personList = []
    for key, value in contact.items():
        if key == "fullName":
            personList.append(value)

        elif key == "cityName":
            personList.append(value)

        elif key == "phoneNumber":
            personList.append(value)
            phNumber = checkValidPhNo(value)
            personList.append(phNumber)

        elif key == "emailAddress":
            personList.append(value)
            email = checkValidEmail(value)
            personList.append(email)

    contactList.append(personList)
#contactList = sorted(contactList)       

"""
## print contact details in terminal
print("\n Contact list from file: \n", contactList)

## save contact details in validationResults.txt file
file = open("validationResults.txt", "wt") 
file.write("Contact List: \n \n")
file.write(str(contactList))
"""

## Step1: list all contact records with status of validation
pEValid = []            ## list containg Full name, city and validation record
conValidRecord = []     ## Step1 result :list containg Full name and validation record

for contact in contactList:
    phoneEmailValid = []                ## individual list containg Full name of contact, city and validation record
    phoneEmailValid.append(contact[1])
    phoneEmailValid.append(contact[0])

    conRecord = []                      ## individual list containg Full name of contact and validation record
    conRecord.append(contact[0])

    if contact[3]== True and contact[5] == True:
        phoneEmailValid.append('Valid')
        conRecord.append('Valid')
    elif contact[3]== True and contact[5] == False:
        phoneEmailValid.append('Email is invalid')
        conRecord.append('Email is invalid')
    elif contact[3]== False and contact[5] == True:
        phoneEmailValid.append('Phone is invalid')
        conRecord.append('Phone is invalid')
    elif contact[3]== False and contact[5] == False:
        phoneEmailValid.append('Email and Phone are invalid')
        conRecord.append('Email and Phone are invalid')
    
    pEValid.append(phoneEmailValid)

    conValidRecord.append(conRecord)
"""
pEValid = sorted(pEValid)
print("\n Contact list and city with validation error report: \n", pEValid)
"""
conValidRecord = sorted(conValidRecord)
print("\n Contact list with validation error report: \n")
printOrder(conValidRecord)

## Store the results in validationResults.txt file
file = open("validationResults.txt", "wt") 
file.write("\nStep1 Output: \nContact List with validation error report:\n")
file.write(str(conValidRecord))


"""
file = open("validationResults.txt", "a") 
file.write("\n \n Contact List with validation error report:\n")
file.write(str(pEValid))
"""

cityValidation ={}  ## dictionary to store validation errors for cities
for contact in pEValid:
    
    if contact[0] not in cityValidation:
        cityValidation[contact[0]] =0
    if contact[2] != 'Valid': 
        cityValidation[contact[0]] += 1

## sort the cityValidation record by number of validation errors in descending order
sort_cityValidation = sorted(cityValidation.items(), key=lambda x: x[1], reverse= True)
print("\n City Validation errors: \n", sort_cityValidation)

file = open("validationResults.txt", "a") 
file.write("\n \nStep2 Output: \nCity validation error report:\n")
file.write(str(sort_cityValidation))
file.close()

"""
##Output:
Contact list with validation error report:

['Abigail Rodriguez', 'Valid']
['Amelia Davis', 'Valid']
['Benjamin Hermandez', 'Valid']
['Charlotte Miller', 'Valid']
['Elijah Martin', 'Email is invalid']
['Emma Smith', 'Phone is invalid']
['Evelyn Garcia', 'Valid']
['Isabella Williams', 'Valid']
['Jacob Thompson', 'Valid']
['James Taylor', 'Email is invalid']
['James White', 'Valid']
['Liam Martinez', 'Email is invalid']
['Logan Thomas', 'Email and Phone are invalid']
['Mary Wilson', 'Email and Phone are invalid']
['Mason Moore', 'Valid']
['Oliver Jackson', 'Valid']
['Olivia Johnson', 'Valid']
['Sophia Brown', 'Valid']
['Taylor Jones', 'Valid']
['William Anderson', 'Valid']

 
 City Validation errors:
 [('Evansville', 2), ('Chicago', 2), ('Kansas City', 2), ('Seattle', 0), ('New York', 0), ('San Franscico', 0)]
"""