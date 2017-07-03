"""""""""""""""""""""""""""
date = "23.06.2016"
day = "perşembe"
time = "oglen"
print(date,day,time,"bulusalim")
print("Merhaba güzel insanlar")
day = 33
donus = 1.6
gidis = 1.4
masraf = day * (donus + gidis)
# "-"*30 ifadesi güzel bir görüntü oluşturuyor sevdim
print("-"*30)
print("Çalışılan gün sayısı\t:",day)
print("Gidiş ücreti\t\t:",gidis)
print("Dönüş ücreti\t\t:",donus)
print("-"*30)
print("Toplam yol masrafı\t:",masraf)

isim = "C"
soyisim = "Kılınçdemir"
is_sis = "Ubuntu"
sehir = "Trabzon"
# bu tarz bir yazım daha okunaklı yapıyor
print("-"*30)
print("İsim            : ",isim,"\n",
	  "Soyisim         : ",soyisim,"\n",
	  "İşletim sistemi : ",is_sis,"\n",
	  "Şehir           : ",sehir, sep="")	
print("-"*30)
# input fonksiyonu kullanarak isim alma
print("-"*30)
isim = input("Adını gir bro : ")
print("Merhaba",isim, end="\n")
print("-"*30)
# input fonksiyonuyla bir örnek daha yaptım yaşını sordum
print("-"*30)
yas = input("Yaşını gir bro : ")
print("Demek",yas,"yaşındasın bro")
print("Genç misin yaşlımısın bilemedim ama brosun o kesin")
print("-"*30)
# dairenin alanını ve cevresini hesaplayan bir örnek
print("-"*30)
cap = input("Dairenin çapını giriniz : ");
yari_cap = int(cap) / 2
pi_sayisi = 3.1415926535897932
alan = pi_sayisi * (pow(yari_cap,2))
cevre = 2 * pi_sayisi * yari_cap 
print("Dairenin alanı   : ",alan,"\n"
	  "Dairenin çevresi : ",cevre, sep="")
print("-"*30)
#alınan verinin tipini öğrenme
print("-"*30)
veri = input("Hergangi bir veri giriniz : ")
tip = type(veri)
print("Girilen veri", tip,"tipindedir.")
# Tip dönüşümü örnekleri 
print("-"*30)
data = input("Lütfen bir sayi giriniz : ")
print("Girdiğiniz sayinin karesi :",int(data) ** 2)
print("-"*30)
# Tip dönüşümü ile toplama işlemi
print("-"*30)
number_1 = input("Birinci sayiyi giriniz: ")
number_2 = input("İkinci sayiyi giriniz : ")
print(number_1, "+", number_2, "=", int(number_1) + int(number_2))
print("-"*30)
# Girilen sayının kaç haneli olduğunu bulma ve bir sayiyi karakter dizisine cevirme
print("-"*30)
number_1 = 2124563456245323
print("Kayıtlı number_1 sayısı: ", number_1,"\n",
	  "Hane sayisi            : ", len(str(number_1)),sep="")
number_2 = input("Bir sayı giriniz : ")
print("Girdiğiniz sayı",len(number_2), "hanelidir")
print("-"*30)
"""""""""""""""""""""""""""
# Doğalgaz faturalandırma
print("-"*30)
ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = eylul = haziran = kasim = 30
subat = 28
birim_fiyat = 0.81
aylik_kullanim = input("Aylık kullanım miktarınızı metreküp cinsinden giriniz : ")
donem = input("""Hangi aya ait faturayı hesaplamak istersiniz? 
Ay ismini küçük harf ve ingilizce karakterler ile giriniz): """)
ay = eval(donem)
gunluk_kullanim = int(aylik_kullanim) / ay
fatura = gunluk_kullanim * birim_fiyat * ay
print("-"*30)
print("Günlük kullanım miktarınız : ", gunluk_kullanim, " metreküp \n",
	  "tahmini fatura tutarınız   : ", fatura, "TL", sep="" )
print("-"*30)
