tralfabe = "ertyuıopğüasdfghjklşizcvbnmöç"
def sezar(girdi, key): 
    new_chr = ""
    for x in girdi:
        if x in tralfabe:
            alfabe = ord(x) + key 
            if alfabe > ord('z'):
                alfabe -= 26
            sifrelimesaj = chr(alfabe)
        new_chr += sifrelimesaj
    return new_chr
#***********************************
cikis = ""
while cikis != "exit":
    a = True
    islem = input("işlem gir(metin,exit):")
    if islem == "metin":
        girdi = input("metin gir:")
        key = int(input("anahtar gir:"))
        if girdi == "1234567890":
            a = False
        elif a:
            print(sezar(girdi, key))
    elif islem == "exit":
        print("çıkılıyor...")
        cikis = "exit"
    else:
        print("yanlış işlem...")