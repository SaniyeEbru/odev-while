satismiktari=500
birimsatisfiyati=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=ciro+(satismiktari*birimsatisfiyati)
    satismiktari=satismiktari+200
    birimsatisfiyati=birimsatisfiyati+10
    i=i+1
print('500.000 den fazla kar',i,'.ayda tamamlanmıştır')




stokmiktari=10000
i=0
alinanürün=100
satilanürün=500
fark=alinanürün-satilanürün
while(stokmiktari>0):
    stokmiktari=stokmiktari+fark
    i=i+1
print(i,"ay sonra stoklar sıfırlanır.")




toplam=0
while True:
    print("Bir sayı giriniz,çıkış için 0(sıfır).")
    girilen=int(input("Sayı: "))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print("Toplam=",toplam)
    else:
        print("Çıkış yapıldı.")
        break


calisan=50
yevmiye=90
aylikmesai=0
haftalikmaas=630
aylikmaas=0
while aylikmesai<=22:
    haftalikmesai=int(input("haftalık mesai:"))
    aylikmesai=haftalikmesai*4
    haftalikmaas=haftalikmaas+(haftalikmesai*yevmiye*0.10)
    aylikmaas=aylikmaas+haftalikmaas*4
    print("Aylık maaş:",aylikmaas)
else:
    print("Aylık mesai 22 saatten fazla olamaz.")
    




gunlukuretilen=200
gunlukdefoluurun=0
toplamdefurun=0
i=0
while(gunlukdefoluurun<=gunlukuretilen*0.20):
    gunlukdefoluurun=int(input("Günlük defolu ürün miktarı:"))
    toplamdefurun=toplamdefurun+gunlukdefoluurun
    i=i+1
    if(gunlukdefoluurun>=gunlukuretilen*0.20):
        print("Defolu ürün sayısı limiti aştı")
        break
    
    print(i,"Günlük", "Defolu ürün sayısı",toplamdefurun)




