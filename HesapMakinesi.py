#!/usr/bin/env python
# coding: utf-8

# In[19]:


def toplama(a,b):
    sonuc=a+b
    return sonuc

def cikarma(a,b):
    sonuc=a-b
    return sonuc
def carpma(a,b):
    sonuc=a*b
    return sonuc
def bolme(a,b):
    sonuc=a/b
    return sonuc

a1=int(input("ilk sayıyı girin"))
b1=int(input("ikinci sayıyı girin"))
c1=int(input("İşlemi seçin"))

if c1 == 0:
    print(toplama(a1,b1))
elif c1==1:
    print(cikarma(a1,b1))
elif c1==2:
    print(carpma(a1,b1))
elif c1==3:
    print(bolme(a1,b1))


# In[ ]:





# In[ ]:




