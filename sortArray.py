if (2 > 5):
    print("false")
else:
    print("true")

print("jestem januszem " + "i o tym wiem " + str(1))
x = str("Lorem mopsium dolor sit amet")
y = int(10)
print(x)
print(y)
print(x[len(x) - 1 ])
print(x[2:10])
print(x[:10])
print(x[10:])
toStrip = ' lorem , Mosium, satan satan';
print(len(toStrip))
print(len(toStrip.strip()))
print(toStrip.swapcase())
print(toStrip.lower().replace('o', '666'))
print(toStrip.split(','))

if 'LoReM' in toStrip.split(','):
    print("yes yes yes")

fruits = 'banana, juice, cherry'

if 'banana' in fruits.split(','):
    print('banana')

if 'lorem' in toStrip.split(','):
    print('yes')

for x in fruits:
    print(x);