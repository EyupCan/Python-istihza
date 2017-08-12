#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     capitalize, title, swapcase   #
#         strip, rstrip, lstrip     #
#                                   #
#####################################

print("""capitalize metodu: karakter dizilerindeki
ilk kelimenin baş harfini büyütür.""")


karakter_dizisi = "eyüp can"
print("capitalize metodundan önce değişken değeri: " + karakter_dizisi)

if karakter_dizisi.startswith("i"): #Türkçe karakter sorunu i harfi büyütülürken I olur bu sorunu aşmak için.
	karakter_dizisi = "İ" + karakter_dizisi[1:]


karakter_dizisi = karakter_dizisi.capitalize()
print("capitalize metodundan sonra değişken değeri: " + karakter_dizisi)
print(30*"#")


print("""title metodu: karakter dizilerindeki tüm
kelimelerin ilk harfini büyütür.""")

karakter_dizisi = "eyüp can ikişer ikişer saydı"
print("title metodundan önce değişken değeri: " + karakter_dizisi)
karakter_dizisi2 = ""
for kelime in karakter_dizisi.split(" "):
	if kelime.startswith("i"):
		karakter_dizisi2 = karakter_dizisi2 + "İ" + kelime[1:] + " "
	else:
		karakter_dizisi2 = karakter_dizisi2 + kelime + " " 
	karakter_dizisi2 = karakter_dizisi2.title()
print("title metodundan sonra değişken değeri: " + karakter_dizisi2)
print(30*"#")

print("""swapcase metodu: karakterlerin küçük harfleri büyük harfe
büyük harfleri küçük harfe çevirir.""")

karakter_dizisi3 = "aAaAAaa aAAAAa AAaaa"
print("swapcase metodundan önce değişken değeri: " + karakter_dizisi3)
print("swapcase metodundan sonra değişken değeri: " + karakter_dizisi3.swapcase()) #Türkçe karakter sorunu var	
print(30*"#")

print("""strip metodu: karakter dizisinin sağındaki ve 
solundaki karakterleri siler""")
karakter_dizisi4 = """<Sana ufak bir kıvılcım delilik verilmiş. Onu da kaybetmemelisin. 
<İnsanlar sana ne söylerse söylesin, dünyayı kelimeler ve fikirler değiştirebilir. 
<Eskiden dünyadaki en kötü şeyin yalnız başına ölmek olduğunu düşünürdüm. Değilmiş. 
<Dünyadaki en kötü şey sana yalnız olduğun hissetiren kişilerin yanında ölmek. 
<Lütfen bu kadar endişelenmeyin. Çünkü sonunda hiçbirimiz bu gezegende uzun süre kalmayacağız. 
<Yaşam çok hızlı ilerliyor. Zaman en iyi öğretmendir ama tüm öğrencilerini öldüren bir öğretmen.
"""

print("strip metodu öncesi metin: " + karakter_dizisi4)
print("strip metodu sonrası metin: ", end = "")
for kelime in karakter_dizisi4.split():
	print(kelime.strip("<"), end = " ")
print()
print(30*"#")
print("rstrip ve lstrip metodları kelimenin sağınkadi ve solundaki karakterleri silerler.")
kelime = "!!OnePiece!!"
print("orjinal kelime: " + kelime)
print("rstrip sonrası değişken değeri: " + kelime.rstrip("!"))
print("lstrip sonrası değişken değeri: " + kelime.lstrip("!"))