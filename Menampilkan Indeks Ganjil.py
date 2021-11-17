# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:16:09 2021

@author: User
"""
print("====== PROGRAM MEMUNCULKAN KARAKTER INDEKS GANJIL ======")

kata = input("Masukan Sebuah Kata : ")

def ganjil(teks):
    panjang = (teks[i] for i in range(len(teks)) if i%2==1)
    print("Karakter Indeks Ganjil : ","".join(panjang))
    
    return(panjang) 
   
ganjil(kata)