#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#   Girilen karakterin metindeki    #
#              sayısı               #
#                                   #
#####################################

metin = """Savaşların tümünde savaşarak zapt etmek en üstün başarı değildir. Üstün başarı 
düşmanın direncini savaşmadan kırmaktır. (III. Bölüm 2. madde)
Sonuçta, düşmanı ve kendinizi iyi biliyorsanız, yüzlerce savaşa
girseniz bile sonuçtan emin olabilirsiniz. Kendinizi bilip, 
düşmanı bilmiyorsanız, kazanacağınız her zafere karşın yenilgiyle de 
tanışabilirsiniz. Ne kendinizi ne de düşmanı bilmiyorsanız sizin için gireceğiniz her 
savaşta yenilgi kaçınılmazdır. (III. Bölüm 19. Madde)
İnsanlar bir kez birleştiler mi, cesurlar tek başlarına ilerleyemez, 
korkaklar ise tek başlarına geri çekilemezler. (VII. Bölüm 14.Madde)
Savaşta usta asker sinirlenmeyen askerdir. Zaferde usta asker 
korkusuz askerdir. Bu nedenle akıllı olan savaşı önceden kazanır, 
oysa cahil olan kazanmak için savaşmak zorundadır."""

aranan_harf = input("Sayılacak harfi giriniz: ")

sonuc = 0

for harf in metin:
	if aranan_harf == harf:
		sonuc += 1

print(aranan_harf + " harfinden metinde "  + str(sonuc) + " tane vardır")