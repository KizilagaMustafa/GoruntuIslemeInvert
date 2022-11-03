import numpy as np
import cv2 as cv

# Görsel Renklerinin Ters Çevirildiği Bölüm

def Gorsel_Cevirme(Gorsel):
    yukseklik = Gorsel.shape[0]
    genislik = Gorsel.shape[1]
    katmanlar = Gorsel.shape[2]

    Boyut = (yukseklik, genislik, katmanlar)
    Yeni_Gorsel = np.zeros(Boyut, np.uint8)

    for x in range(0, yukseklik):
        for y in range(0, genislik):
            for z in range(0, katmanlar):
                Yeni_Gorsel[x, y, z] = 255 - Gorsel[x,y,z]
    return Yeni_Gorsel


# Görselin Alınıp Okunduğu ve Tersinin Kayıt Edildiği Bölüm
# Okunma Yapılması İçin Görsel MUTLAKA proje dizininde olmalı!!!!!

def main():
    Alinan_Gorsel = cv.imread("k.jpg")

    Cevrilmis_Gorsel = Gorsel_Cevirme(Alinan_Gorsel)

    cv.imwrite("k_ters.jpg", Cevrilmis_Gorsel)

    input("Lütfen Devam Etmek İçin Enter'a Basın...")


if __name__ == '__main__':
    main()