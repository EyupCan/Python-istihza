#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     Hesap Makinesi Versiyon 2     #
#                                   #
#                                   #
#####################################

giris = """
(1) Toplama İşlemi
(2) Çıkarma İşlemi
(3) Çarpma İşlemi
(4) Bölme İşlemi
(5) Kare Hesaplama
(6) Karekök Hesaplama İşlemi
"""
print(giris)

cikis_islemi = 1

while cikis_islemi == 1:

	islem = input("Yapmak istediğiniz işlemin numarasını giriniz(çıkmak için q giriniz): ")
	
	if islem == "q":
		print("Programdan çıkılıyor..")
		cikis_islemi = 0
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
		print("Yanlış işlem numarası girdiniz!!")

