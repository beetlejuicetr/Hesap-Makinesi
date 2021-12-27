print("""

    -------------------------------
    |Hesap Makinesine Hoşgeldin!  |
    |                             |
    |Sürüm   : v1.2               |
    |Yapımcı : Beetlejuicetr (MID)|
    |Dil     : Python             |
    -------------------------------

    """)

print("""
    *Nasıl Kullanılır?:
    ---------------------------------
    Hesap makinesini kullanmak
    oldukça basitdir.
    Örnegin bir kaç sayıyı toplama
    ihtiyacı duyuyorsun veya
    daha karmaşık işlemler yapmak
    istiyorsun. Bunun için
    sadece işlemi yazman yeterli. :)

    Çıkmak için ' cıkıs ' yazman gerekiyor.
    ---------------------------------
    """)

while True:
    islem = input("İşlem: ")
    if islem == "cıkıs":
        print("Çıkış Yapılıyor...")
        break
    try:
        print(eval(islem))
    except :
        print("Sadece sayı girmelisin!")

