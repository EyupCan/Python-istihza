#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#      join, count, index, rindex   #
#             find, rfind           #
#                                   #
#####################################

print("""join metodu: karakter dizilerinin parçalı 
hallerini birleştirmeye yarar.""")
karakter_dizisi = "Luffy Zoro Usopp Sanji Nami Chopper Robin Franky Brook"
print("Orjinal karakter dizisi: " + karakter_dizisi)
karakter_dizisi = karakter_dizisi.split()
print("split metodu sonrası karakter dizisi: " + str(karakter_dizisi))
karakter_dizisi = "-".join(karakter_dizisi) 
print("join metodundan sonra karakter dizisi: " + karakter_dizisi)
print(30*"#")

print("""count metodu: karakter dizilerinde bir karakterin
kaç kez geçtiğini sorgulamaya yarar.""")
karakter_dizisi2 = "Göktürk"
print("Karakter dizimizin değeri: " + karakter_dizisi2)
print("İçinde ki k harf sayısı " + str(karakter_dizisi2.count("k")))
print(30*"#")


parola = input("Yeni parolanızı giriniz: ")
kontrol = True

for karakter in parola:
	if parola.count(karakter) > 1:
		kontrol = False
if kontrol:
	print("Parola başarılı bir şekilde değiştirildi")
else:
	print("Parolanızın içerisinde aynı karakterden sadece 1 tane olabilir!")
print(30*"#")

kelime = input("Bir kelime giriniz: ")
farkli_karakter = ""
for karakter in kelime:
	if karakter not in farkli_karakter:
		farkli_karakter += karakter 
for karakter in farkli_karakter:		
	print("{} karakteri {} kelimesinde {} kere geçmektedir.".format(karakter, kelime, kelime.count(karakter)))
print(30*"#")

print("""index metodu: karakter dizilerinde bir karakterin 
kaçıncı sırada olduğunu öğrenmeye yarar. Karakter yoksa
bir hata mesajı döner.""")
karakter_dizisi3 = input("Bir metin giriniz: ")
aranacak_karakter = input("Konumunu aradığınız karakteri girin: ")
for konum in range(len(karakter_dizisi3)):
	if konum == karakter_dizisi3.index(aranacak_karakter, konum):
		print("%s. sırada 1 adet %s harfi bulunuyor" %(konum, aranacak_karakter))
print(30*"#")

print("""rindex metodu: index metoduyla aynı işlemi yapar
	farklı olarak sağdan sola tarama yapar.""")
degisken = "alabasta"
print("Degiskenimizin degeri: " + degisken)
print("index metodu ile a karakterinin konumu " + str(degisken.index("a")))
print("rindex metodu ile a karakterinin konumu " + str(degisken.rindex("a")))
print(30*"#")

print("""find ve rfind metodu: index metodu ve rindex metodları
	ile aynı görevi görürler aralarındaki fark hata mesajı yerine
	-1 döndürmeleridir.""")
degisken2 = "papatya"
print("Degiskenimizin degeri: " + degisken2)
print("find metodu ile olmayan e harf sonucu: " + str(degisken2.find("e")))
print("rfind metodu ile a karakterinin konumu: " + str(degisken2.rfind("a")))