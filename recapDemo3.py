#asal sayı uygulama

sayi=int(input("bir sayi giriniz="))
asalMi="evet"

for x in range(2,sayi):
    if sayi % x == 0:
        asalMi="hayır"
        break

if asalMi == "evet":
    print("asal")
else:
    print("asal degil")        

