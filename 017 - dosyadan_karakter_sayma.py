#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#   Girilen karakterin dosyadaki    #
#              sayısı               #
#                                   #
#####################################

okunan_metin = open("karakter_oku.txt",encoding = "utf-8")

aranan_harf = input("Sayısının tespit edileceği harfi giriniz: ")

sonuc = 0

for satir in okunan_metin:
	for harf in satir:
		if aranan_harf == harf:
			sonuc += 1

print("Sorguladığınız " + aranan_harf + " harfi dosyada " + str(sonuc) + " kez kullanılmıştır.")

okunan_metin.close()