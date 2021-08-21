import string
import time
import allPasswordLengths as crack


# ADD DICTIONARY SELECTION 

generator = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def passwordCrack():
    passwordsLength = int(input("password length: "))
    print("\n")
    passwordToCrack = input("Search password combination: ")
    time_start = time.perf_counter()
    passwords = compare(passwordsLength)
    z = 0
    u = len(passwords)
    print("SCRIPT ONLINE\nBrute force attack has started.\nPlease wait..")
    while z <= u:
        for password in passwords:
            if password == passwordToCrack:
                print("PASSWORD FOUND --> "+password)
                z = u+1
            elif z == u:
                print("Password not found")
                break
        z += 1
    time_end = time.perf_counter()
    difference = time_end - time_start
    print(difference)
    print('TOTAL TIME: '+str(difference)+" seconds")



def compare(i):
    a = 0
    for number in generator:
        if i == number:
            print(f"Generating all possible combinations for passwords of {i} CHARACTERS from provided dictionary..\nThis could take a while.")
            
    characters = string.printable
    
    if i == 1:
        return crack.oneCharacter(characters)
    elif i == 2:
        return crack.twoCharacters(characters)
    elif i == 3:
        return crack.threeCharacters(characters)
    elif i == 4:
        return crack.fourCharactersSOLO(characters)
    elif i == 5:
        return crack.fiveCharacters(characters)
    elif i == 6:
        return crack.sixCharacters(characters)
    elif i == 7:
        return crack.sevenCharacters(characters)
    elif i == 8:
        return crack.eightCharacters(characters)
    elif i == 9:
        return crack.nineCharacters(characters)
    elif i == 10:
        return crack.tenCharacters(characters)
        

def startProgramMessage():
    print("/----------------------------------------------------------\\")
    print("|              BIG BOGUS PASSWORD CRACKER                  |")
    print("\----------------------------------------------------------/")
    print("|              2021 LINUXBOYS - lukkelele                  |")
    print("/----------------------------------------------------------\\")
    
def endProgramMessage():
    print("/----------------------------------------------------------\\")
    print("|            COPYRIGHTED - by megachinCHAD bogus           |")
    print("\----------------------------------------------------------/")
    print("|                                                          |")
    print("/----------------------------------------------------------\\")
    