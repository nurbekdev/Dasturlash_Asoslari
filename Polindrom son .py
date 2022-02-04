"""
Created on Tue Apr 13 22:07:55 2021

Mahmudov Abdurahim

http:\\telegram.me\developing_programmer

"""

son=int(input('Son kiriting\n>>>'))
sonlar = []
a = len(str(son))
raqamlar = []
for _ in range(a):
    b=son%10
    son//=10
    raqamlar.append(b)
s = ''.join(str(raqam) for raqam in raqamlar)
raqamlar.reverse()
d = ''.join(str(raqam) for raqam in raqamlar)
if int(s)-int(d)==0:
    print('Bu sonlar polindrom ')
else:
    print('Bu sonlar polidrom emas')
print(s ,end=' ')
print(d)