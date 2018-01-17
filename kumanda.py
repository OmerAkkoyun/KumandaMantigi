import random
import time

class Kumanda():#Kumanda ad�nda Klas�m�z� olu�turduk.A�a��da ��indekileri Giricez...
    def __init__(self,tv_durumu="kapal�",tv_ses=10,tv_kanal_listesi=["atv"],kanal=["atv"]):
        self.tv_durumu=tv_durumu
        self.tv_ses= tv_ses
        self.tv_kanal_listesi=tv_kanal_listesi
        self.kanal=kanal
#Buraya kadar i�inde olacak �zellikleri girdik...

    def tv_ac(self):#Tv a�ma �zelli�ini ekliyoruz
        if self.tv_durumu =="kapal�":
            print("TV A��ld�..")
            self.tv_durumu="a��k"
        else:
            print("TV Zaten A��k..")


    def tv_kapat(self):#Tv Kapatma �zelli�ini ekliyoruz.
        if self.tv_durumu=="a��k" :
            print("TV Kapat�ld�..")
            self.tv_durumu="kapal�"
        else:
            print("Tv Zaten Kapal�..")

    def ses_ayari(self):#Tv SES ayar� �zellikleri burada verilecek.
        while True:#D�ng� i�inde olmas� daha sa�l�kl�
            cevap=input("Sesi k�smak i�in '<' i�areti\nSesi art�rmak i�in'>' i�areti yaz�n.\n��k�� i�in '��k�� yaz�n\n ='")
            if cevap=="<":
                if self.tv_ses!=0:
                    self.tv_ses-=1
                    print("�imdiki Ses D�zeyi =",self.tv_ses)
            elif cevap==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                    print("�imdiki Ses D�zeyi =", self.tv_ses)
            elif cevap=="��k��":
                print("��k�� yap�ld�")
                break
            else:print("Ge�ersiz ��lem girdiniz!")

    def kanal_ekle(self):#Burada append i�lemi ile kanal listesine yeni kanal aklenebilecek.
          while True:
            ekleyin=input("Eklenecek kanal� yaz�n(��k�� i�in '��k�� yaz�n'):")
            if ekleyin!="��k��":
                print("Kanal ekleniyor")
                time.sleep(1)
                self.tv_kanal_listesi.append(ekleyin)
                print("kanal ba�ar�yla eklendi")
                print("G�ncel Kanal Listeniz =",self.tv_kanal_listesi)
            else:
                break





    def kanaldegis(self,):
        while True:
            print("G�ncel Kanal Listesi:",self.tv_kanal_listesi,"bunlard�r.\n")
            kanalsec=input("l�tfen kanal listesinden bir kanal yaz�n  = ")
            if kanalsec in self.tv_kanal_listesi:
                print("Kanal De�i�tirildi")
                self.kanal = kanalsec
                break
            else:

                print("HATA! L�tfen Sadece Kanal listesinde var olan kanallar� yaz�n..")







    def __str__(self):
        return"Tv Durumu = {}\nSes D�zeyi= {}\nKanal = {}\nTv Kanal Listesi = {}\n".format(self.tv_durumu,self.tv_ses,self.kanal,self.tv_kanal_listesi)

kumanda=Kumanda()
print("""
Kumanda Uygulamas�

1.Tv A�
2.Tv Kapat
3.Tv Ses Ayarlar�
4.Tv Kanal Ekleme
5.Tv Kanal De�i�tir
6.Genel �zellikler

L�tfen A�a��ya Yapmak istedi�iniz ��lem Numaras�n� Giriniz...
""")
while True:
    islem=(input("��lem Numaras�n� Girin ="))
    if islem =="1":
        kumanda.tv_ac()
    elif islem=="2":
        kumanda.tv_kapat()
    elif islem=="3":
        kumanda.ses_ayari()
    elif islem=="4":
        kumanda.kanal_ekle()
    elif islem=="5":
        kumanda.kanaldegis()
    elif islem=="6":
        print(kumanda)
    elif islem=="��k��":
        print("��k�� yap�l�yor..")
        time.sleep(1)
        break

    else:
        print("Ge�erli i�lem numaras� girin")

