# create random string with given length
import random;

searchedString = 'One touch of nature makes the whole world kin';
searchedString2 = 'abcdef'
searchedArr = list(searchedString2)
randomStr = '';
i = 0;

# def checkEqual(generated, searchArr):
#     print('generated ', generated, ' searchedArr :', searchArr)
#     if (generated == searchArr):
#         print('search done in: ', i, 'found : ' , searchArr)
#         return True;
#     return False;

# def removeCorrect(generated):
#     #  if there is one or more letters on good position, reduce string 
#     for j in range(0, len(generated) - 1):
#         # print('searched : ', searchedArr)
#         if generated[j] == searchedArr[j]:
#             del searchedArr[j];
#     return checkEqual(generated, searchedArr)

# while (removeCorrect(randomStr) == False):
#     i = i + 1;
#     temp = [];
#     for x in range(0, len(searchedArr)):
#         # takes number from range ` to z in ascii Dec
#         asciDec = random.randint(96, 111);
#         asciDec = chr(asciDec);         
#         # convert ` to space`
#         temp.append(asciDec.replace('`', ' '));
#     randomStr = temp;

generated = '';
searched = 'lorem';
isEqual = False;
while (isEqual == False):
    searchedSub = [];
    for x in range(0, len(searched)):
        asciDec = random.randint(96, 111);
        searchedSub.append(chr(asciDec))
        # check if the same 
    print(searchedSub)
    for i in range(0, len(searched) - 1):
        print(searchedSub[i])
        if searched[i] == searchedSub[i]:
            print(searched[i], 'is the same')