#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     							    #
#                                   #
#                                   #
#####################################

# Mod öperatörü
print("~"*30)
bolunen = int(input("Bölünecek sayıyı giriniz: "))
bolen = int(input("Bölen sayıyı giriniz: "))

metin = "{} sayısı {} sayısına tam".format(bolunen,bolen)

if bolunen % bolen == 0:
	print(metin,"bölünür!")
else:
	print(metin,"bölünmez!")
print("~"*30)
# Parola kontrolü
print("~"*30)
parola = "1234qwer"
soru = input("Parolanızı giriniz: ")
if soru == parola:
	print("Doğru parola girdiniz :)")
else:
	print("Yanlış parola girdiniz!")
print("~"*30)
# Kullanıcı adi ve parola sorgusu
print("~"*30)
username = input("Kullanıcı adı giriniz: ")
password = input("Parola giriniz: ")

if username == "Eyüp Can" and password == "1234qwer":
	print("Sisteme Hoşgeldiniz")
else:
	print("Yanlış parola veya kullanıcı adı girdiniz!! ")
print("~"*30)
