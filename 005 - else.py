#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#                                   #
#                                   #
#                                   #
#####################################

# Basit else örneği
print("*"*30)
meyve = input("Bir meyve giriniz: ")

if meyve == "elma":
	print("evet, elma bir meyvedir")
elif meyve == "muz":
	print("evet, muz sarı bir meyvedir")
elif meyve == "armut":
	print("hmm, doğru armut da bir meyvedir.")
else:
	print("Yazdığın şey bir meyve midir?")
print("*"*30)
# Basit if-else örneği
print("*"*30)
soru = input("Programdan çıkmak istiyormusunuz?\
(Çıkmak için 'e' giriniz): ")
if soru == "e":
    print("Haydi güle güle..")
elif soru == "b":
    print("Kararsız mısın?")
else:
    print("Hadi devam edelim sohbete")
