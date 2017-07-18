# -*- coding: utf-8
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

import sys

_2x_metni = """
Python'ın 2.x sürümlerinde program çalışmamaktadır.
Lütfen 3.x sürümlerinden birini kullanın."""

_3x_metni = "Hesap Makinesine Hoş Geldiniz."

try:
	if sys.version_info.major < 3:
		print(_2x_metni)
	else:
		print(_3x_metni)

except AttributeError:
	print(_2x_metni)



giris = """
(1) Toplama İşlemi
(2) Çıkarma İşlemi
(3) Çarpma İşlemi
(4) Bölme İşlemi
(5) Kare Hesaplama
(6) Karekök Hesaplama İşlemi
"""

while True:
	
	print(giris)	

	islem = input("Yapmak istediğiniz işlemin numarasını giriniz(çıkmak için q giriniz): ")
	
	try:
		if islem == "q":
			print("Programdan çıkılıyor..")
			break
		elif islem == "1":
			sayi1 = int(input("Toplama işlemi için birinci sayıyı giriniz: "))
			sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
			print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
		elif islem == "2":
			sayi1 = int(input("Çıkarma işlemi için birinci sayıyı giriniz: "))
			sayi2 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
			print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
		elif islem == "3":
			sayi1 = int(input("Çarpma işlemi için birinci sayıyı giriniz: "))
			sayi2 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
			print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
		elif islem == "4":
			sayi1 = int(input("Bölme işlemi için birinci sayıyı giriniz: "))
			sayi2 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
			print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
		elif islem == "5":
			sayi1 = int(input("Kare hesaplama işlemi için sayıyı giriniz: "))
			print(sayi1, "sayısının karesi", "=", sayi1 ** 2)
		elif islem == "6":
			sayi1 = int(input("Karekök hesaplama işlemi için  sayıyı giriniz: "))
			print(sayi1, "sayısının karekökü", "=", sayi1 ** 0.5)
		else:
			print("""
Yanlış işlem numarası girdiniz!!
Aşağıdaki seçeneklerden birini giriniz!!
""")
	except ValueError:
			print(17*"!!")
			print("!!Yanlış türde değişken girdiniz!!")
			print(17*"!!")
	except ZeroDivisionError:
			print(17*"!!")
			print("!!Sıfıra bölme hatası!!")
			print(17*"!!")