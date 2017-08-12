#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#   lower, upper, islower, isupper  #
#        endswith, startswith       #
#                                   #
#####################################

print("lower metodu")
kisi = input("Aradığınız kişinin adını ve soyadını aralarında boşluk olacak şekilde giriniz: ")
kisi = kisi.replace("I","ı").replace("İ","i").lower()

if kisi == "kisi k":
	print("e-mail: example@gmail.com")
	print("telefon: 05554443322")
	print("şehir: Tr")
elif kisi == "kisi b":
	print("e-mail: example1@gmail.com")
	print("telefon: 06665554433")
	print("şehir: Tr")
elif kisi == "kisi g":
	print("e-mail: example2@gmail.com")
	print("telefon: 07776665544")
	print("şehir: Tr")
else:
	print("Aradığınız kişi kayıtlı degil!!")
print(30*"#")

print("upper metodu")
sehir = input("Hava durumu için şehir giriniz: ")
sehir = sehir.replace("i","İ").upper()

if sehir == "TRABZON":
	print("Her zaman ki gibi yağmurlu")
elif sehir == "MANİSA":
	print("Havada tek bir bulut bile yok")
elif sehir == "İSTANBUL":
	print("Tabiki pis bir sis bulutu var")
else:
	print("Aradığınız şehir kayıtlı değil!!")
print(30*"#")

print("islower metodu")
kisi = input("İsminizi giriniz: ")
if not kisi.islower():
	print("Lütfen isminizi küçük harfle giriniz!!")
print(30*"#")

print("isupper metodu")
metin = input("Mesajınızı giriniz: ")
metin = metin.split()

for kelime in metin:
	if kelime.isupper():
		print("Lütfen tamamı büyük harflerden oluşan kelime yazmayınız!!")
print(30*"#")


print("endswith metodu")
dosya_listesi = "abc.c def.py asd.mp4 asd.mp3 erl.sh op.lf"
dosya_listesi = dosya_listesi.split(" ")

for dosya in dosya_listesi:
	if dosya.endswith(".py"):
		print("Python dosyası adı: " + dosya)
print(30*"#")


print("startswith metodu")
dosya_listesi = "abc.c def.py asd.mp4 asd.mp3 erl.sh op.lf"
dosya_listesi = dosya_listesi.split(" ")

for dosya in dosya_listesi:
	if dosya.startswith("a"):
		print("a ile baslayan dosya adı: " + dosya)
