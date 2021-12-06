# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:39:29 2021

@judul : Praktikum ke-12 latihan ke-1
@NIM : 065002100002
@author: Nabilah Putri


"""

class mahasiswa:


    def _init_(self,nama,nim,tahun):
        self.nama=nama
        self.nim=nim
        self.tahun=tahun
    def printMaha(self):
        print("Nama :"+self.nama)
        print("Nim :"+str(self.nim))
        print("Tahun angkatan :"+str(self.tahun))

nama=input("silahkan masukan namamu :")
nim=str(input("silahkan masukan nim kamu : "))
tahun=str(input("silahkan masukan tahun angkatanmu :"))

maha1=mahasiswa(nama,nim,tahun)
maha1.printMaha()