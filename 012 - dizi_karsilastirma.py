#####################################
#                                   #
#                                   #
#                                   #
#      Eyüp Can KILINÇDEMİR         #
#    eyupcankilincdemir@gmail.com   #
#    	ceksoft.wordpress.com       #
#     	  Dizi Karşılaştırma        #
#                                   #
#                                   #
#####################################

print("*"*30)

birinci_metin = "qwertryruııxoopıouıyutryterwqrewtreytryuıtrewrqwreytruyıoıwrrrer"
ikinci_metin = "qwerwtreyujhgdfsdarytuyıuoıoşkljhewtrytuyıuoılrewasdyuıı"

fark = ""

for karakter in birinci_metin:
	if not karakter in ikinci_metin:
		if not karakter in fark:  
			fark += karakter		
print(fark)
fark = "" 
print("*"*30)

for karakter in ikinci_metin:
	if not karakter in birinci_metin:
		if not karakter in fark:  
			fark += karakter			
print(fark)
print("*"*30)
