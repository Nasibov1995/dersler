# r - yalniz oxumaq
# w - movcud melumat silinir yeni melumat yazilir
# a - Movcud melumatin uzerine yeni melumat gelir



# ad = input('Secim edin : (1) Bazaya yeni ad elave edin : (2) Butun melumatlari sil ve teze melumat yaz: (3) Melumat')


# if ad == '1':
#     c = input('Bazaya ad daxil edin : ')
#     a = open('test.txt', 'r').read()

#     if len(a) == 0:
#         a = open('test.txt', 'a')
#         a.write(c)
        
#     else:
#         a = open('test.txt', 'a')
#         a.write(' '+c)

#     a = open('test.txt','r')
     
#     print(a.read())

# elif ad == '2':
#     c = input('adi secin : ')
#     a = open('test.txt', 'w')
#     a.write(c)
#     a = open('test.txt','r')
     
#     print(a.read())
    
# elif ad =='3':
#     a = open('test.txt', 'r').read()
#     a = a.split()

#     if len(a) == 0:
#         print('Bazada hec bir melumat yoxdur')
#     else:
#         print('Bazada ' +str(len(a))+' ad var ')
        
#     a = open('test.txt','r')
     
#     print(a.read())


# from datetime import datetime


# a = input('Dogum gununuzu daxil edin : ')

# now = datetime.now()

# dogum_gunu = datetime.strptime(a, '%Y-%m-%d')

# netice = now - dogum_gunu

# netice = netice.total_seconds()


# san = netice
# deq = int(san / 60)
# saat =int(deq / 60)
# gun = int(saat / 24)
# ay = int(gun / 30)
# yash = int(ay / 12)

# print('Siz heyatda '+str(san)+ ' saniye '+str(yash)+' yash')


# a = open('test.txt','r').read()

# if len(a) == 0:
#     a = open('test.txt','a')
#     a.write('\ntest')
# else:
#     a = open('test.txt','a')
#     a.write('\ntest')





