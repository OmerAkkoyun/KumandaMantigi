import random
import time

class Kumanda():#Kumanda adýnda Klasýmýzý oluþturduk.Aþaðýda Ýçindekileri Giricez...
    def __init__(self,tv_durumu="kapalý",tv_ses=10,tv_kanal_listesi=["atv"],kanal=["atv"]):
        self.tv_durumu=tv_durumu
        self.tv_ses= tv_ses
        self.tv_kanal_listesi=tv_kanal_listesi
        self.kanal=kanal
#Buraya kadar içinde olacak özellikleri girdik...

    def tv_ac(self):#Tv açma özelliðini ekliyoruz
        if self.tv_durumu =="kapalý":
            print("TV Açýldý..")
            self.tv_durumu="açýk"
        else:
            print("TV Zaten Açýk..")


    def tv_kapat(self):#Tv Kapatma özelliðini ekliyoruz.
        if self.tv_durumu=="açýk" :
            print("TV Kapatýldý..")
            self.tv_durumu="kapalý"
        else:
            print("Tv Zaten Kapalý..")

    def ses_ayari(self):#Tv SES ayarý özellikleri burada verilecek.
        while True:#Döngü içinde olmasý daha saðlýklý
            cevap=input("Sesi kýsmak için '<' iþareti\nSesi artýrmak için'>' iþareti yazýn.\nÇýkýþ için 'çýkýþ yazýn\n ='")
            if cevap=="<":
                if self.tv_ses!=0:
                    self.tv_ses-=1
                    print("Þimdiki Ses Düzeyi =",self.tv_ses)
            elif cevap==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                    print("Þimdiki Ses Düzeyi =", self.tv_ses)
            elif cevap=="çýkýþ":
                print("çýkýþ yapýldý")
                break
            else:print("Geçersiz Ýþlem girdiniz!")

    def kanal_ekle(self):#Burada append iþlemi ile kanal listesine yeni kanal aklenebilecek.
          while True:
            ekleyin=input("Eklenecek kanalý yazýn(çýkýþ için 'çýkýþ yazýn'):")
            if ekleyin!="çýkýþ":
                print("Kanal ekleniyor")
                time.sleep(1)
                self.tv_kanal_listesi.append(ekleyin)
                print("kanal baþarýyla eklendi")
                print("Güncel Kanal Listeniz =",self.tv_kanal_listesi)
            else:
                break





    def kanaldegis(self,):
        while True:
            print("Güncel Kanal Listesi:",self.tv_kanal_listesi,"bunlardýr.\n")
            kanalsec=input("lütfen kanal listesinden bir kanal yazýn  = ")
            if kanalsec in self.tv_kanal_listesi:
                print("Kanal Deðiþtirildi")
                self.kanal = kanalsec
                break
            else:

                print("HATA! Lütfen Sadece Kanal listesinde var olan kanallarý yazýn..")







    def __str__(self):
        return"Tv Durumu = {}\nSes Düzeyi= {}\nKanal = {}\nTv Kanal Listesi = {}\n".format(self.tv_durumu,self.tv_ses,self.kanal,self.tv_kanal_listesi)

kumanda=Kumanda()
print("""
Kumanda Uygulamasý

1.Tv Aç
2.Tv Kapat
3.Tv Ses Ayarlarý
4.Tv Kanal Ekleme
5.Tv Kanal Deðiþtir
6.Genel Özellikler

Lütfen Aþaðýya Yapmak istediðiniz Ýþlem Numarasýný Giriniz...
""")
while True:
    islem=(input("Ýþlem Numarasýný Girin ="))
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
    elif islem=="çýkýþ":
        print("Çýkýþ yapýlýyor..")
        time.sleep(1)
        break

    else:
        print("Geçerli iþlem numarasý girin")

