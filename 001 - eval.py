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

# Basit hesapmakinesi eval() fonksiyonunun çalışması
print("-"*30)
print("""
Hesap Makinesi Uygulaması

	* Çarpma  işlemi
	/ Bölme   işlemi
	+ Toplama işlemi
	- Çıkarma işlemi

Yapmak istediğiniz işlemi yazıp enter tuşuna basınız.
Örnek işlem => 23 + 32 yazdıktan sonra ENTER'a basınız.
""")
veri = input("İşleminiz: ")
hesaplama_sonucu = eval(veri)
print(hesaplama_sonucu)
print("-"*30)
