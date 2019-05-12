# create random string with given length
import random;

searchedString = 'One touch of nature makes the whole world kin';
searchedString2 = 'all ';
randomStr = '';
i = 0;

def compareWithPatch(val1, val2):
    print('Comparing' + val1, val2)

def compare(val1, val2):
    print('Comparing: ' + val1.lower() , val2.lower(), i)
    if (val1 in val2):
        print(val1, ' contains ' , val2)
        findIndex = val2.find(val1);
        print('reduced ', val2.split(findIndex, 1))
        return True;

    if (val1.lower() == val2.lower()):
        print('search done in: ', i)
        return True;
    return False;

while (compare(randomStr, searchedString2) == False):
    i = i + 1;
    temp = "";
    for x in range(0, len(searchedString2)):
        # takes number from range ` to z in ascii Dec
        asciDec = random.randint(96, 111);
        asciDec = chr(asciDec);         
        # convert ` to space`
        temp = asciDec.replace('`', ' ')

    randomStr = temp;