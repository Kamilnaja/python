def e(d):
  return ''.join(list(map(lambda x: (f"{ord(x)-96:02d}"), d)))

print(e("helloworld"))
print(e("helloworld") == '08051212152315181204')
# 71
# print("helloworld"=lambda x:x)
mess = "helloworld"
# print(lambda x: x+=(f"{ord(x)-96:02d}"), mess)
# lambda x:"".join()
f = lambda x:"".join("%02i"%(ord(j)-96)for j in x)
print(f("hello"))
# g = lambda x: "".join(f"{ord(x)-96:02d}")for j in x)
# g = lambda x: "".join("{ord(x)-96:02d}" for j in x)
# print(g("hello"))