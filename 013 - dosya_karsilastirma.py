#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     	  Dosya Karşılaştırma       #
#                                   #
#                                   #
#####################################

print("*"*30)
dosya1 = open("isimler1.txt")
dosya1_satırlar = dosya1.readlines()

dosya2 = open("isimler2.txt")
dosya2_satırlar = dosya2.readlines()

for satır in dosya2_satırlar:
	if not satır in dosya1_satırlar:
		print(satır)
print("*"*30)
dosya1.close()
dosya2.close()
