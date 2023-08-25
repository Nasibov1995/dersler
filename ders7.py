# "r" texti oxummaq
# "a" textin uzerine yeni element elave etmek
# "w" movcud textin icindeki elementleri silir yeni element elave edir


# a = open('test.txt','a')

# a.write(' ' +'Aslan')


# a = open('test.txt','w')

# a.write(' ' +'Fuad')


# a = open('test.txt').read()


# print(a)




# a = open('test.txt').read()

# if len(a) == 0:
#     a = open('test.txt','a')
#     a.write('Fuad')
# else:
#     a = open('test.txt','a')
#     a.write(' '+'Aslan')
    
# a = open('test.txt','r').read()

# print(a)

# a = open('test.txt')

# print(a.readlines())


# ad = input('Secim edin : (1) Bazaya yeni ad elave edin : (2) Butun melumatlari sil ve teze melumat yaz: (3) Melumat : ')


# a = open('test.txt').read()


# if ad == '1':
    
#     txt = input('Bazaya yeni ad elave edin : ')
    
#     if len(a) == 0:
        
#         a = open('test.txt','a')
#         a.write(txt)
#     else:
#         txt = input('Bazaya yeni ad elave edin : ')
#         a = open('test.txt','a')
#         a.write(' '+txt)
        
# elif ad == '2':
#     txt = input('Butun melumatlari sil ve teze melumat yaz:  ')
#     a = open('test.txt','w')
#     a.write(txt)
    
# elif ad == '3':
#     a = open('test.txt','r').read()
    
#     c = a.split()
    
#     if len(c) == 0:
#         print('Bazada hec bir melumat yoxdur ')
        
#     else:
#         print('Bazada '+str(len(c))+' element var ')

# else:
#     print('Duzgun daxil etmediniz ')
    
# import os

# secim = input('Secim edin : (1) Spesifik elementi qaytar : (2) Bazani sil ')
    
    
# if secim == '1':
#     ad = int(input('Secin : '))
#     a = open('test.txt').readlines()
#     print(a[ad])
# elif secim == '2':
#     os.remove('test.txt')
    
class Insan():
    
    def __init__(self,il,reng,motor):
        self.il = il
        self.reng = reng
        self.motor = motor
    def cagir(self):
        print(
            
            """
            Il: {}
            Reng: {}
            Motor: {}
            
            """.format(self.il,self.reng,self.motor)
        )
        
    def elave_et(self):
        self.reng.append('qirmizi')
        
ad = Insan(1999,['ag','qara','mavi'],1.4)

ad.elave_et()
        
ad.cagir()


  
    
