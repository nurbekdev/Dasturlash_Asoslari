"""
Theme : Sonlarni soz bilan yozib beruvchi dastur

Mahmudov Abdurahim

http:\telegram.me\developing_programmer

"""

a=int(input('Son kiriting\n>>>'))
b=len(str(a))
raqamlar=[]
sonlar=[]
for _ in range(b):
    s=a%10
    a//=10
    raqamlar.append(s)
for i in range(b):
    if raqamlar[i]==0:
        son=''
    elif raqamlar[i]==1:
        son='bir'
    elif raqamlar[i]==2:
        son='ikki'
    elif raqamlar[i]==3:
        son='uch'
    elif raqamlar[i]==4:
        son='tort'
    elif raqamlar[i]==5:
        son='besh'
    elif raqamlar[i]==6:
        son='olti'
    elif raqamlar[i]==7:
        son='yetti'
    elif raqamlar[i]==8:
        son='sakkiz'
    elif raqamlar[i]==9:
        son='toqqiz'
    if i in [1, 4, 7, 10, 134125]:
        if raqamlar[i]==0:
            son=''
        elif raqamlar[i]==1:
            son='o`n'
        elif raqamlar[i]==2:
            son='yigirma'
        elif raqamlar[i]==3:
            son='ottiz'
        elif raqamlar[i]==4:
            son='qirq'
        elif raqamlar[i]==5:
            son='ellik'
        elif raqamlar[i]==6:
            son='oltmish'
        elif raqamlar[i]==7:
            son='yetmish'
        elif raqamlar[i]==8:
            son='sakson'
        elif raqamlar[i]==9:
            son='toqson'
    elif i in [2, 5, 8, 11, 14]:
        if son!='':
            son = f'{son} yuz'
    elif i==3:
        if raqamlar[3]!=0 or raqamlar[4]!=0 or raqamlar[5]!=0:
            son = f'{son} ming'
    elif i==6:
        if raqamlar[6]!=0 or raqamlar[7]!=0 or raqamlar[8]!=0:
            son = f'{son} million'
    elif i==9:
        if raqamlar[9]!=0 or raqamlar[10]!=0 or raqamlar[11]!=0:
            son = f'{son} milliard'
    elif i==12:
        son = f'{son} trillion'
    sonlar.append(son)
sonlar.reverse()
for son in sonlar:
    if son !='':
        print(son.strip(),end=" ")
