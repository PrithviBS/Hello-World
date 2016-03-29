##convert given decimal number to Roman number (Number Range: 1 to 100) using Recursion
import sys, os
sRomanValglobal=""
##This method appends the new Roman characters  
##to the existing string
def postAppend(c=None, n=0, sRomanVal=None):
    sRomanVal=sRomanVal+c*n
    #print sRomanVal
    return sRomanVal
    #for j in range(1,n):
        #sRomanVal[index++]=c

##This method used to appned 2 roman numbers for a string
##which is genrally used for 4, 9, 40, 90(XC).
def preAppend(cRoman=None, cRoman1=None, sRomanVal=None):
    #sRomanVal[index++] = cRoman
    #sRomanVal[index++] = cRoman1
    sRomanVal=sRomanVal+cRoman+cRoman1
    return sRomanVal


##This method converts Decimal number to Roman number
def convertToRoman(number=None, sRomanVal=None):
    if number<=0:
        return None
    if number == 100:
        sRomanVal=sRomanVal+'C'
        return sRomanVal
    elif number>=50:
        if number<90:
            sRomanVal=postAppend('L', number / 50, sRomanVal)
            number=number%50
        else:
            sRomanVal=preAppend('X','C', sRomanVal)
            number = number-90
    elif number>=10:
        if number<40:
            sRomanVal=postAppend('X', number / 10, sRomanVal)
            number = number % 10
        else:
            sRomanVal=preAppend('X','L', sRomanVal)
            number = number - 40
    elif number>=5:
        if number<9:
            sRomanVal=postAppend('V', number / 5, sRomanVal)
            number = number % 5
        else:
            sRomanVal=preAppend('I', 'X', sRomanVal)
            number = number - 9
    elif number>=1:
        if number<4:
            sRomanVal=postAppend('I', number / 1, sRomanVal)
            number = number % 1
        else:
            sRomanVal=preAppend('I', 'V', sRomanVal)
            number = number - 4
    print sRomanVal
    sRomanVal=convertToRoman(number, sRomanVal)
    return sRomanVal
##    print("Roman number Output: {0}".format(sRomanVal))
##    sys.exit()

try:
    number=int(raw_input('"Enter the decimal number to convert Roman:'))
except ValueError:
    print "Not a number"
if (number <=0)|(number > 100):
    print("Invalid decimal number")
    sys.exit() 
sRomanVal=""
sRomanVal=convertToRoman(number,sRomanVal)
print("Roman number Output: {0}".format(sRomanVal))
sys.exit()

    
