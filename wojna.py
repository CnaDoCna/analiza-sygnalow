import random
import time
import os
class graWojna:
    talia=[ "Dwojka Trefl", "Trojka Trefl", "Czworka Trefl", "Piatka Trefl", "Szostka Trefl", "Siodemka Trefl", "Osemka Trefl", "Dziewiatka Trefl", "Dziesiatka Trefl", "Walet Trefl", "Dama Trefl", "Krol Trefl", "As Trefl",
    "Dwojka Karo", "Trojka Karo", "Czworka Karo", "Piatka Karo", "Szostka Karo", "Siodemka Karo", "Osemka Karo", "Dziewiatka Karo", "Dziesiatka Karo", "Walet Karo", "Dama Karo", "Krol Karo", "As Karo",
    "Dwojka Kier", "Trojka Kier", "Czworka Kier", "Piatka Kier", "Szostka Kier", "Siodemka Kier", "Osemka Kier", "Dziewiatka Kier", "Dziesiatka Kier", "Walet Kier", "Dama Kier", "Krol Kier", "As Kier",
    "Dwojka Pik", "Trojka Pik", "Czworka Pik", "Piatka Pik", "Szostka Pik", "Siodemka Pik", "Osemka Pik", "Dziewiatka Pik", "Dziesiatka Pik", "Walet Pik", "Dama Pik", "Krol Pik", "As Pik"]
    wartosci={"Dwojka Trefl":0, "Dwojka Karo":0,"Dwojka Kier":0,"Dwojka Pik":0,"Trojka Trefl":1,"Trojka Karo":1,"Trojka Kier":1,"Trojka Pik":1,"Czworka Trefl":2,"Czworka Karo":2,"Czworka Kier":2,"Czworka Pik":2,
    "Piatka Trefl":3,"Piatka Karo":3,"Piatka Kier":3,"Piatka Pik":3,"Szostka Trefl":4,"Szostka Karo":4,"Szostka Kier":4,"Szostka Pik":4,"Siodemka Trefl":5,"Siodemka Karo":5,"Siodemka Kier":5,"Siodemka Pik":5,
    "Osemka Trefl":6,"Osemka Karo":6,"Osemka Kier":6,"Osemka Pik":6,"Dziewiatka Trefl":7,"Dziewiatka Karo":7,"Dziewiatka Kier":7,"Dziewiatka Pik":7,"Dziesiatka Trefl":8,"Dziesiatka Karo":8,"Dziesiatka Kier":8,"Dziesiatka Pik":8,"Walet Trefl":9,"Walet Karo":9,"Walet Kier":9,"Walet Pik":9,
    "Dama Trefl":10,"Dama Karo":10,"Dama Kier":10, "Dama Pik":10, "Krol Trefl":11,"Krol Karo":11,"Krol Kier":11,"Krol Pik":11,"As Trefl":12,"As Karo":12,"As Kier":12,"As Pik":12}
    karty1=[]
    karty2=[]
    wojennySchowek=[]


    def __init__(self):
        os.system('cls')

    def losowanieKarty1(self):
        while len(self.karty1)<26:

            if len(self.talia)==0:
                self.losowanieKarty1()
            else:
                losKarta=random.randint(0,len(self.talia)-1)
                self.karty1.append(self.talia[losKarta])
                self.talia.remove(self.talia[losKarta])

        time.sleep(1)
        print("Gracz pierwszy dostal 26 kart:")
        print(self.karty1)

    def losowanieKarty2(self):
        while len(self.talia)!=0:

            if len(self.talia)==0:
                self.losowanieKarty1()
            else:
                losKarta=random.randint(0,len(self.talia)-1)
                self.karty2.append(self.talia[losKarta])
                self.talia.remove(self.talia[losKarta])
        time.sleep(1)
        print("\nGracz drugi dostal 26 kart:")
        print(self.karty2)


    def rozgrywka(self):
        while len(self.karty1)!=0 or len(self.karty2)!=0:
            time.sleep(2)
            print("\nGracz pierwszy: ", self.karty1[0],"\nLiczba kart: ",len(self.karty1))
            print("\nGracz drugi: ", self.karty2[0],"\nLiczba kart: ",len(self.karty2),"\n")


            time.sleep(2)
            if self.wartosci[self.karty1[0]]>self.wartosci[self.karty2[0]]:
                print("BITWE WYGRYWA GRACZ PIERWSZY\n")
                self.wojennySchowek.append(self.karty1[0])
                self.wojennySchowek.append(self.karty2[0])
                self.karty1.remove(self.karty1[0])
                self.karty2.remove(self.karty2[0])
                self.karty1.extend(self.wojennySchowek)
                self.wojennySchowek.clear()
            elif self.wartosci[self.karty1[0]]<self.wartosci[self.karty2[0]]:
                print("BITWE WYGRYWA GRACZ DRUGI\n")
                self.wojennySchowek.append(self.karty1[0])
                self.wojennySchowek.append(self.karty2[0])
                self.karty1.remove(self.karty1[0])
                self.karty2.remove(self.karty2[0])
                self.karty2.extend(self.wojennySchowek)
                self.wojennySchowek.clear()
            else:
                self.wojna()



    def wojna(self):
        time.sleep(2)
        print("\nWOJNAAA!\n")
        time.sleep(2)

        for i in range(0,3):
            self.wojennySchowek.append(self.karty1[i])
            self.wojennySchowek.append(self.karty2[i])
            # print(self.wojennySchowek)
            temp1=self.karty1[i]
            temp2=self.karty2[i]
            self.karty1.remove(self.karty1[i])
            self.karty2.remove(self.karty2[i])
        print("Gracz pierwszy walczy: ",self.karty1[0], "-zakryta karta-", temp1)
        print("Gracz drugi walczy: ", self.karty2[0], "-zakryta karta-", temp2)
        time.sleep(4)

        if self.wartosci[temp1]>self.wartosci[temp2]:
            print("\n\nWOJNE WYGRYWA GRACZ PIERWSZY. Dostaje karty:")
            for i in self.wojennySchowek:
                print(i)
            self.karty1.extend(self.wojennySchowek)
            self.wojennySchowek.clear()
        elif self.wartosci[temp1]<self.wartosci[temp2]:
            print("\n\nWOJNE WYGRYWA GRACZ DRUGI. Dostaje karty:")
            for i in self.wojennySchowek:
                print(i)
            self.karty2.extend(self.wojennySchowek)
            self.wojennySchowek.clear()
        else:
            self.wojna()

osoba1=graWojna()
osoba2=graWojna()
osoba1.losowanieKarty1()
osoba2.losowanieKarty2()
osoba1.rozgrywka()
osoba2.rozgrywka()
