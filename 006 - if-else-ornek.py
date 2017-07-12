#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#                                   #
#                                   #
#                                   #
#####################################

print("*"*30)
kullanici_adi = input("Kullanıcı adını giriniz: ")
parola = input("Parola giriniz: ")

toplam_uzunluk = len(kullanici_adi) + len(parola)

mesaj = "Girdiğiniz kullanıcı adı ve parola uzunluğunun toplamı {} karakterdir."

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk > 40:
    print("Parola ve kullanıcı adınızın toplam uzunluğu \
40 karakterden fazla olmamalıdır.")
else:
    print("Sisteme Hoş Geldiniz")
print("*"*30)
