import hashlib

dosya='.\md5random.py'

with open(dosya,"rb") as file:
    x=hashlib.md5(file.read()).hexdigest()

basamak=int(input("kac basamakli sayi uretilsin? :"))

a=""

for i in range(basamak):
    a=a+((str(x))[7])
    x=hashlib.md5((str(x)).encode("utf-8")).hexdigest()

print(basamak,"basamakli random hexadecimal sayi=",a)
print("Hexadecimal sayinin decimal karsiligi=",int(a,16))
    
    
