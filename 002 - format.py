#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#       ceksoft.wordpress.com       #
#                                   #
#                                   #
#                                   #
#####################################

# format() metodunun kullanımı ve url yazdırma
"""
print("-"*30)
url = input("Url adresini giriniz : ")
print("Ben '{}' adresini bulamadım :(".format(url))
"""
# Dilekçe örneği
print("-"*30)
dilekce = """

											Tarih: {}


T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına

Fakültenizin {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim yılı {}. yarıyılında
öğrenime ara izni (kayıt dondurma) istiyorum.

	Bilgilerinizi ve gereğini arz ederim.


	İmza
Ad            : {}
Soyad         : {}
T.C Kimlik No : {}
Adres         : {}
Telefon       : {}
Ekler         : {}
"""
tarih = input("Tarih: ")
universite = input("Üniversite Adı: ")
fakulte = input("Fakülte Adı: ")
bolum = input("Bölüm Adı: ")
ogrenci_no = input("Öğrenci Numarası: ")
ogretim_yılı = input("Öğretim Yılı: ")
yarı_yıl = input("Yarı yıl: ")
ad = input("Öğrencinin Adı: ")
soyad = input("Öğrencinin Soyadı: ")
tc_kimlik_no = input("TC Kimlik Numarası: ")
adres = input("Adres: ")
telefon = input("Telefon: ")
ekler = input("Ekler: ")

print(dilekce.format(tarih,universite,fakulte,bolum,ogrenci_no,
					 ogretim_yılı,yarı_yıl,ad,soyad,tc_kimlik_no,adres,
					 telefon,ekler))
