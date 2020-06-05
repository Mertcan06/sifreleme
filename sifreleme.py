import argparse
#********************sezar*****************
tralfabe = "abcçdefgğhıijklmnoöprsştuüvyz" 
def sezar(metin, key):
    new_chr = ""
    for x in metin:  
        if x in tralfabe:
            alfabe = abs((tralfabe.index(x)) + key)
            if alfabe > (tralfabe.index('z')):
                alfabe -= 28
            sifrelimesaj = tralfabe[alfabe]
        else:
            sifrelimesaj = x
        new_chr += sifrelimesaj
    return new_chr
def sezar_cozum(metin,key):
    new_chr = ""
    for x in metin:  
        if x in tralfabe:
            alfabe = abs((tralfabe.index(x)) - key)
            if alfabe > (tralfabe.index('z')):
                alfabe -= 28
            mesaj = tralfabe[alfabe]
        else:
            mesaj = x
        new_chr += mesaj
    return new_chr
#********************doğrusal********************
def dogrusal(metin,a,b):#y = xa+b mod n
    cipher_text = ""
    for m in metin:
        if not m in tralfabe:
            cipher_text = cipher_text + m
            continue
        new_chr = abs((tralfabe.index(m)+1)*a+b)
        new_chr = new_chr%29
        new_chr = tralfabe[new_chr]
        cipher_text = cipher_text + new_chr
    return cipher_text
def find_z(a):
    for i in range(0,30):
        result = (a*i)%29
        if result == 1:
            return i
def dogrusal_cozum(metin,a,b):#z(y-b) mod n (doğrusalın çözümü)
    cipher_text = ""
    for m in metin:
        if not m in    tralfabe:
            cipher_text = cipher_text + m
            continue
        z = find_z(a)
        print(z)
        new_chr = abs(z*((tralfabe.index(m)+1) - b))
        new_chr = new_chr%29
        new_chr = tralfabe[new_chr]
        cipher_text = cipher_text + new_chr
    return cipher_text

#*********************************** 
def main(args):
    if args.sifreleme == "sezar":
        if args.islem == "sifrele":
            print(sezar(args.metin, int(args.key)))
        elif args.islem == "coz":
            print(sezar_cozum(args.metin, int(args.key)))
    if args.sifreleme == "dogrusal":
        if args.islem == "sifrele":
            print(dogrusal(args.metin, int(args.key), int(args.key2)))
        elif args.islem == "coz":
            print(dogrusal_cozum(args.metin, int(args.key), int(args.key2)))
    else:
        print("yanlış işlem...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='program acıklaması')
    parser.add_argument('-sifreleme', type=str, help='algoritma isimleri yazılacak')
    parser.add_argument('-metin',type=str,help='sifrelenecek metin yazılacak')
    parser.add_argument('-islem',type=str,default="sifrele", help='yapılacak islemi yaz(sifrele,çoz')
    parser.add_argument('-key', type=str, help='algoritma anahtarı yazılacak')
    parser.add_argument('-key2', default="", type=str, help='algoritma anahtarı yazılacak')
    
    args = parser.parse_args()
    main(args)