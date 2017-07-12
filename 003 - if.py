#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     			            #
#                                   #
#                                   #
#####################################

# Basit Sayı Kontrolü
sayi = int(input("Bir sayi giriniz: "))
print("-"*30)
if(sayi > 24):
	print("Girdiğiniz sayi 24 ten büyüktür")
if(sayi == 24):
	print("Girdiğiniz sayi 24 e eşittir.")
if(sayi < 24):
	print("Girdiğiniz sayi 24 ten küçüktür")
print("-"*30)
# Basit String Kontrolü
print("-"*30)
print("""
     Wuhuuu Eyüp Can Parola Kontrol Mekanizmasına
                    HOŞGELDİNİZ
""")
print("-"*30)
parola = input("Parola Giriniz: ")
if(parola == "fibonacci"):
	print("Böyle parolamı konur arkadaş!!")
if(parola != "fibonacci"):
	print("Yanlış parola")
print("-"*30)
