from random import randint as g


# a =  []
# k = int(input("k= "))
# for i in range(k):
#     a.append(input(f"{i+1}-sonni kiriting: "))
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# kerak_mahsulotlar = []
# yoq_mahsulotlar = []
# bor_mahsulotlar = []
# for i in range(5):
#     kerak_mahsulotlar.append(input(f"{i+1}-mahsulot nomini kiriting: "))
# for d in mahsulotlar:
#     if kerak_mahsulotlar in d:
#         bor_mahsulotlar.append(kerak_mahsulotlar)
#         print(f"bizning do'konda {bor_mahsulotlar} bor")
#     else:
#         yoq_mahsulotlar.append(kerak_mahsulotlar)
#         print(f"bizning do'konda {yoq_mahsulotlar} yoq")


class Mashinalar:
    def __init__(self,nomi,modeli,rangi,raqami,yili):
        self.nomi=nomi
        self.modeli=modeli
        self.rangi=rangi
        self.raqami=raqami
        self.yili=yili
    b = int(input("nechta mashinani ko'zdan kechirmoqchisiz: "))
    for i in range(b):
        a = input("Tanlagan mashinagiz nomini kiriting: ")
        if a.lower() == 'matiz':
            def matiz(self):
                return f" Modeli: {self.modeli}, Rangi: {self.rangi}, Raqami: {self.raqami}, Yili: {self.yili}  "
        else:
            def none(self):
                return f"siz tanlagan mashina do'konimizda yo'q"

a =  input('tanlagan mashina nomini qaytadan kiriting: ')
t = Mashinalar("matiz","daewo",'qora',145,2000)
if a == 'matiz':
    print(t.matiz())
else:
    print(t.none())
