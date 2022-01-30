# -*- coding: utf-8 -*-
ogrenciler = ["kubra", "seyda","emre","sedef","huseyin"]

filetoAppend = open("ogrenciler","a")

for ogrenci in ogrenciler:
    filetoAppend.write(ogrenci)
    filetoAppend.write("\n")

filetoAppend.close()

