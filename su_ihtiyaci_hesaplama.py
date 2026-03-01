
def su_hesapla(kilo):
    erkek = kilo * 0.04
    kadin = kilo * 0.03

    cinsiyet = input("Lütfen Cinsiyetinizi Belirtiniz: ").lower()

    if cinsiyet == "erkek":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print("Kilonuz: ",kilo)
        print(erkek,"Litre Su İçmelisiniz.")
        print("-"*30)
    elif not cinsiyet:
        print("Lütfen Önce Cinsiyetinizi Belirtin!")
    elif cinsiyet == "kadın":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print("Kilonuz: ",kilo)
        print(kadin,"Litre Su İçmelisiniz.")
        print("-"*30)

kilo_al = int(input("Lütfen Kilonuzu Girin: "))

su_hesapla(kilo_al)