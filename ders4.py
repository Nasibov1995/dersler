# x = ['Fuad','Tural','Samir']
# x = [1,2,3,4,5]
# print(x[0])
# x.pop()
# print(x)
# x.remove('Samir')
# print(x)
# print(x.remove('Fuad'))

# x.append('Hesen')
# print(x)

# x.insert(2,'Hesen')
# print(x)

# print(len(x))

# print(sum(x))

# x.reverse()

# print(x)

# x = [ [1,2,3] , [4,5,6] , [7,8,9] ]

# print(x[1][1])

# a = [1,'Fuad',True,2.5]

# print(a[1])

# x = list(('Fuad','Aslan'))

# print(x)

# x = []


# x = ['Fuad','Tural','Samir']

# a = x

# print(a)

# x = ['Fuad','Tural','Samir','Mehemmed']

# for i in x:
#     if 'a' in i:
#         print(i)
       
    
# meyveler = ["alma", "banan", "gilas", "kivi", "manqo"]

# print(type(meyveler))

# newlist = []

# for x in meyveler:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# x = ['Fuad','Tural','Samir']

# x[1] = 'Hesen'

# print(x)
# 

# a = { 'Baki': {'Unvan':'Baki'},'ad':[['Hesen', 'Fuad']]}
# for i in a.items():
#     print(i)

# a = {'child1':'Emil','yash':15}
# b = {'child2':'Ayxan','yash':10}

# c = {'member1':a,'member2':b}

# print(c['member1'])

# a = {5,6,7,8,9}

# a.pop()
# print(a)

# a = [1,2,3,4]

# print(a[0])
# print('')
# print(a[-1])

# test_list = [5, 6, [], 3, [], [], 9]

# for i in test_list:
#     if i != []:
#         print(i)
    
# l = ['Fuad', 'Ayxan']
# secim = int(input(' Secim edin :\n (1) Adi daxil edin \n (2) Adi silin '))


# if secim == 1:
#     ad = input('Adi secin : ')
#     if len(ad) < 15:
#         l.append(ad)
#         print(l)
#         for i in l:
#             print(i)
#     else:
#         print('Maksimum 15 characters')
        
    
# if secim == 2:
#     ad = input('Adi secin : ')
#     l.remove(ad)
#     print(l)
#     for i in l:
#         print(i)
    
# x = int(input('Eded daxil edin : '))

# if x < 0:
#     print('Bu eded menfidir')
# else:
#     print('Bu eded musbetdir')

# a =(1,2,3,4)

# print(a.index(3))


# a = {'Sheher' :'Baki','Unvan' :'Serifzade'}

# ad = input('daxil edin (1) Key - (2)Values: ')


# if ad == '':
#     print('hecne Daxil etmediniz')
# if ad == '1':
#     print(a.keys())
# if ad == '2':
#     print(a.values())


# a = ['Fuad','Aslan','Afaq']
    
# ad = int(input('Ad daxil edin (1) Adi silin (2) : '))

# if ad == 1:
#     s = input('Ad daxil edin : ')
#     a.append(s)
#     print(a)
#     for i in a:
#         print(i)
# if ad == 2:
#     s = input('Adi silin : ')
#     a.remove(s)
#     print(a)
#     for i in a:
#         print(i)

# a = [1,2,3,4,5]

# print(a[0])
# print()
# print(a[-1])


# test_list = [5, 6, [], 3, [], [], 9]


# for x in test_list:
#     if x != []:
#         print(x)

# a = int(input('Eded daxil edin : '))

# if a < 0 :
#     print('Bu eded menfidir ')
# else:
#     print('Bu eded musbetdir ')
    

# a = {'Sheher':'Baki','Unvan':[['Serifzade','Abbasov']]}


# print(a.get('Unvan'))


# a.pop('Unvan')
# print(a)

# a.popitem()

# print(a)

# a.update({'Sheher':'Sumqayit'})

# print(a)

# a.clear()

# print(a)


# a = {'ad' : ' Emil'}

# b = {'ad' : 'Aslan'}

# c = {
    
#     'child1' : a,
#     'child2' : b
     
#      }

# print(c['child2']['ad'])



# a = {1,2,3,4,5}

# a.add(6)

# print(a)


# set1 = {"a", "b" , "c"}

# set2 = {1, 2, 3}

# set1.update(set2)

# print(set1)

# immutable

# a = ( 1, 2, 3 )


# print(type(a))

# print(a.index(1))


# tuple1 = (1,2,3,4,5)

# tuple2 = (5,6,7,8,9)

# tuple3 = tuple1 + tuple2

# print(tuple3)

# a = [1,2,3,4,5,6,7,8,9,10,11,12]


# for i in a:
#     if i % 3 == 0:
#         print(i)

# a = 'Python'

# if a.startswith('f'):
#     print(a)

# a = {1:"Python",2:"CSharp",3:"PHP"}

# a.pop(1)
# print(a)

# def python(*x,z=5):
#     c = x  * z
#     print(c)
    
    
# python(2,4)


# def my_function(**kids):
#   print(kids)

# my_function(a = 'Emil')


# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))


# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')


# def a(x):
#     return x + 5

# print(a(10))






# a.popitem()

# print(a)


# def call():
    
#     a = {'ad':'Fuad'}
#     ad = int(input('Secim edin (1) Keys ,  (2) Values '))

#     if ad == 1:
#         print(a.keys())
#     elif ad == 2:
#         print(a.values())
#     else:
#         print('Xahis edirik  1 ve ya 2 duymesini basin ')
        
# call()


# a = {'ad' : ' Emil'}

# b = {'ad' : 'Aslan'}

# c = {
    
#     'child1' : a,
#     'child2' : b
     
#      }

# print(c['child2']['ad'])


# a = 'Pythonn'

# print(a.count('n'))


# a = (1,2,3,4,5)

# a = list(a)

# a.append(6)

# a = tuple(a)

# print(a)


# person = {
    
#     'shexsi_melumatlar':{'ad' : 'Fuad' , 'Soyad' : 'Eliyev' , 'ata _adi' : 'Firuz' },
    
#     'Unvan' : ['Baki,Nax kuc. men 56'] ,
    
#     'Is_yeri' : ['Reabilitasiya_merkezi'] 
    
#         }



# person['Is_yeri'].remove('Reabilitasiya_merkezi')

# print(person)

# def a(x,y):
#     pass
    
    
    
    
# print(a(2,5))
    
# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def adder(*num):
#     sum = 0
    
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)

# def my_function(*kid):
#   print("His last name is " + kid[0])

# my_function("Fuad")



# i = 0
# while i < 10:
#     i+=1
    
#     if i == 4:
#         raise TypeError('gicsen')
#     print(i)




# def a(x):
#     return x
   
# print(a(4))


# def call(a):
#     pass
    

# def my_function(country = "Norway"):
#     print("I am from " + country)



# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def a (x,y):
#     c = x +y
    
# a()



# def a(*args):
#   print("His last name is " + str(args))
    
# a( 'John','Fuad')

# c = lambda x,y: x ** y

# print(c(2,4))

# try:
#     a = 5
#     c = a / 0
#     print(c)
# except ZeroDivisionError:
#     print('0-a bolmek olmaz ')





    
    







# a = 5

# try:
#     c = 5 / 5
#     print(c)
# except ZeroDivisionError :
#     print('0 -a bolmek olmaz')
        


# def a(x):
#     print(x)



# try:
#     a(1,2)
# except  TypeError :
#     print('a sadece 1 argument qebul ede biler ')





# def task():
#     a = ['Fuad','Aslan','Afaq']  
#     ad = int(input('Ad daxil edin (1) Adi silin (2) : '))

#     if ad == 1:
#         s = input('Ad daxil edin : ')
#         a.append(s)
#         print(a)
#         for i in a:
#             print(i)
#     if ad == 2:
#         s = input('Adi silin : ')
#         a.remove(s)
#         print(a)
#         for i in a:
#             print(i)
            
# task()



# a = [1,2,3,4,5]


# try:
#     print(a[0])
# except  IndexError :
#     print('bu index listde yoxdur')