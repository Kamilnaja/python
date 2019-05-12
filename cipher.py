e = lambda x: "".join(f"{ord(j)-96:02}" for j in x)
print(e("helloworld"))
f = lambda x: "".join("%02i" % (ord(j) - 96) for j in x)
print(e("helloworld") == "08051212152315181204")
# 71
# print("helloworld"=lambda x:x)
mess = "helloworld"
# print(lambda x: x+=(f"{ord(x)-96:02d}"), mess)
# lambda x:"".join()
print(f("hello"))
# g = lambda x: "".join(f"{ord(x)-96:02d}")for j in x)
# g = lambda x: "".join("{ord(x)-96:02d}" for j in x)
# print(g("hello"))

