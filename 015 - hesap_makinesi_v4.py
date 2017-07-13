#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     Hesap Makinesi Versiyon 4     #
#                                   #
#                                   #
#####################################

izinli_karakterler = "0123456789+-*/ "

giris = """
***Merhabalar Hesap Makinesi Uygulamamıza Hoş Geldiniz***

Operatörler

		'+' Toplama İşlemi
		'-' Çıkarma İşlemi
		'*' Çarpma İşlemi
		'/' Bölme işlemi

Yapmak istediğiniz işlemi yazıp ENTER'a basınız.
(Örneğin 11 ve 13 sayılarını toplamak için 11 + 13
yazdıktan sonra	 ENTER'a basın)
"""

print(giris)

while True:

	veri = input("İşleminiz: ")

	if veri == "q":
		print("Programdan çıkılıyor..")
		break

	for karakter in veri:
		if karakter not in izinli_karakterler:
			print("!!Hey dostum amacın nedir!!")
			quit()
	hesaplama_sonucu = eval(veri)
	
	print(hesaplama_sonucu)
