#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#         karakter metodları        #
#                                   #
#                                   #
#####################################

isim = input("İsminizi giriniz: ") 


print("İsmin harflerini sırasıyla ekrana basma")
for sira in range(len(isim)):
	print("İsminizin {}. harfi: {}".format(sira+1,isim[sira]))
print(30*"#")

print("İsmin belirli bir bölümünü ekrana basma")
print(isim[0:4])
print(isim[4:7])
print(30*"#")

print("Baştan ve sonran string ayırma")
site1 = "www.istihza.com"
site2 = "www.siberbulten.com"
site3 = "www.mertsarica.com"
for site in site1,site2,site3:
	print("Site: ",site[4:-4])
print(30*"#")

print("Stringi ters çevirme")
metin = "Bir kedi gördüm sanki"
print("Orjinal Metin: " + metin)
print("Tersine çevrilmiş hali :" + metin[::-1])
print(metin[7:3:-1])
print(30*"#")

print("Karakter dizisinin harflerinin sıralanması")
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
siralanan_metin = "maviçiçek"
print(sorted(siralanan_metin,key=çevrim.get))
print(30*"#")

print("Karakter dizisini sesli sessiz harf ayrılması")
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler  = ""
sessizler = ""

metin2 = "koccamanbirkedigördümsanki"
for harf in metin2:
	if harf in sesli_harfler:
		sesliler += harf
	else:
		sessizler += harf

print("Karakter dizisindeki sesli harfler: " + sesliler)
print("Karakter dizisindeki sessiz harfler: " + sessizler)
print(30*"#")
