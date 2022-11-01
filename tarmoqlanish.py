# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i.lower()=='gm':
#         print(cars[3].upper())
#     else:
#         print(i.title())

# a = input("login ismingizni kiriting: ")
# if a.lower()=='admin':
#     print("Hush kelibsiz",a.title(), "foydalanuvchilar ro'yhatini ko'rasizmi")
# else:
#     print(f"Hush kelibsiz {a.title()}")

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))

# if a==b:
#     print("Sonlar teng ")
# else:
#     print("Sonlar teng emas ekan")

# a = int(input("1-sonni kiriting: "))

# if a>0:
#     print("Musbat son ")
# else:
#     print("Manfiy son ")

# a = float(input("a="))
# if a>0:
#     print(a**(1/2))
# else:
#     print("musbat son kiriting: ")


# a = int(input("juft son kiriting: "))
# if a%2==0:
#     print("a juft son")
# else:
#     print("a toq son")

# a = int(input("yoshingizni kiriting: "))

# if 4>a or a>60:
#     print("Sizga kirish bepul")
# elif a>18:
#     print("sizga kirish 20 ming")
# else:
#     print("sizga kirish 10 ming")

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a==b:
#     print("Bu ikki son teng:")
# elif a>b:
#     print("1-son katta")
# else:
#     print("2-son katta")

# mahsulot = ['anor','olma','tuxum','kartoshka','sabzi','bumaga','tuz','gugurt']
# savat = []

# for i in range(5):
#     savat.append(input(f"{i+1} mahsulot nomini kiriting: "))

# for d in savat:
#     if d in mahsulot:
#         print(f"{d} bizning do'konda bor: ")
#     else:
#         print(f"{d} bizning do'konda yo'q")

# mahsulot = ['anor','olma','tuxum','kartoshka','sabzi','bumaga','tuz','gugurt']
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# savat = []
# for i in range(5):
#     a = input("mahsulot nomini kiriting: ")
#     if a in mahsulot:
#         bor_mahsulotlar.append(a)
#     else:
#         yoq_mahsulotlar.append(a)
# if yoq_mahsulotlar == []:
#     msg = "Hammasi bor"
#             #print("Siz so'raganlar bor")
# else:
#     msg = yoq_mahsulotlar
# print(msg)

mahsulot = ['un',"yog'","kartoshka",'kolbasa','qatiq','olma',"olxo'ri"]
bor_mahsulotlar = []
yoq_mahsulotlar = []
biz_tanlagan_mahsulotlar = []

for i in range(5):
    biz_tanlagan_mahsulotlar.append(input(f"{i+1}-mahsulot nomini kiriting: "))
for z in biz_tanlagan_mahsulotlar:

    if z in mahsulot:
        bor_mahsulotlar.append(z)
        
    else:
        yoq_mahsulotlar.append(z)
    
for d in bor_mahsulotlar:
    if d in mahsulot:
        print(d)
    else:
        for s in yoq_mahsulotlar:
            print(s)
    

