#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#           	                    #
#                                   #
#                                   #
#####################################

# Basit for örneği
print("*"*30)
sayılar = "123456789"

for sayı in sayılar:
	print(int(sayı)*2)
print("*"*30)
# Karakter sorgulama
tr_karakterler = "ığüÜĞşŞİöÖçÇ"
parola = input("Parolanızı giriniz: ")

for karakter in parola:
	if karakter in tr_karakterler:
		print("Parola türkçe karakter içeremez!!")
print("*"*30)

