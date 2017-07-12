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

# Basit while örnekleri
print("#"*30)
a = 1
while a < 11:
	print(a)
	a += 1
print("#"*30)
# Parola sorgusu uzunluğun küçük büyük sınırına uyması

while True:
	parola = input("Yeni Parola giriniz: ")
	
	if not parola:
		print("Parola kısmı boş bırakılamaz!!")
	elif len(parola) > 10 or len(parola) < 3:
		print("Parola 10 karakterden büyük 3 karakterden küçük olamaz!")
	else:
		print("Yeni parolanız", parola)
