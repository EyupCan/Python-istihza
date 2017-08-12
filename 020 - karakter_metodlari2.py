#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#   replace, split, splitlines      #
#                                   #
#                                   #
#####################################

import sys

print("replace metodu")

kardes = "luffy"
print("replace metodu öncesi değişken değeri: " + kardes)
print("replace metodu sonrası değişken değeri: " + kardes.replace("f","F"))
value = "türkiye"
print("replace metodu öncesi değişken değeri: " + value)
print("replace metodu sonrası değişken değeri: " + value.replace("tür","TÜR"))
print(30*"#")


print("split metodu")


value_2 = input("Kısaltma yapılacak ifadeyi giriniz: ")
for kelime in value_2.split():
	print(kelime[0],end=".")
print()
print(30*"#")

value_3 = "Büyük Hun, Avrupa Hun, Göktürk, Hazar, Uygur"
for kelime in value_3.split(", "):
	print(kelime)
print(30*"#")

version = sys.version
print(version.split()[0])
print(30*"#")

print("split metodu ile çıktı: " + str(value_3.split(",", 2)))
print("rsplit metodu ile çıktı: " + str(value_3.rsplit(",", 2)))
print(30*"#")

metin = """The Sopranos is an American crime drama television series 
created by David Chase. The story revolves around the fictional 
character, New Jersey-based Italian American mobster Tony Soprano 
(James Gandolfini). The series portrays the difficulties he faces 
as he tries to balance the conflicting requirements of his home 
life and his criminal organization. These are often highlighted 
during his therapy sessions with psychiatrist Jennifer Melfi 
(Lorraine Bracco). The series features Tony's family members, 
mafia colleagues and rivals, in prominent roles and story arcs, 
most notably his wife Carmela (Edie Falco) and protégé Christopher 
Moltisanti (Michael Imperioli)."""
print(metin.splitlines())
print(30*"#")
