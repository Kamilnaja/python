# create random string with given length
import random;

searchedString = 'One touch of nature makes the whole world kin';
searchedString2 = ['a', 'l', 'l', 'g', 'h'];
randomStr = '';
i = 0;

def checkEqual(generated, searched):
    if (generated == searched):
        print('search done in: ', i, ' res : ', generated, 'found : ' , searched)
        return True;
    return False;

def removeCorrect(generated, searched):
    #  if there is one or more letters on good position, reduce string 
    for j in range(0, len(generated)):
        if generated[j] == searched[j]:
            print('one on good position')
            # del searched[j]
    return checkEqual(generated, searched)

while (removeCorrect(randomStr, searchedString2) == False):
    i = i + 1;
    temp = [];
    for x in range(0, len(searchedString2)):
        # takes number from range ` to z in ascii Dec
        asciDec = random.randint(96, 111);
        asciDec = chr(asciDec);         
        # convert ` to space`
        temp.append(asciDec.replace('`', ' '));
    randomStr = temp;