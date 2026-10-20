# # i = 0
# # while i<10:
# #     print(i)
# #     i=i+1
#
# # while True:
# #     print("Hello World")
#
# """
# break
# """
# while True:
#     ism = input("Ism kiriting: (boshqa kiritmasangiz 'stop' deb yozing!)")
#     if ism == "stop":
#         break
#     else:
#         print(ism)

print("1 - Buyurtma ro'yxati")
print("2 - Mahsulot va narxlar")
tanlov = input("Tanlang: ")

if tanlov == "1":
    buyurtma = []

    while True:
        mahsulot = input("Mahsulot kiriting (tugatish uchun stop): ")
        if mahsulot == "stop":
            break
        else:
            buyurtma = buyurtma + [mahsulot]

    print("Buyurtma:")
    for mahsulot in buyurtma:
        print(mahsulot)
else:
    mahsulotlar = {}

    while True:
        mahsulot = input("Mahsulot kiriting (tugatish uchun stop): ")
        if mahsulot == "stop":
            break
        else:
            narx = input("Narxini kiriting: ")
            mahsulotlar[mahsulot] = narx

    print("Mahsulotlar:")
    for mahsulot in mahsulotlar:
        print(mahsulot, "-", mahsulotlar[mahsulot])
