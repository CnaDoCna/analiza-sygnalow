import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag ##wymagany we wspólnym katalogu

dane = pd.read_csv(r"sub-02_trial-04.csv", delimiter=',', engine='python')

t = np.linspace (0, 35, 200*35)
sygnal=dane['kol1'][0:7000]
num=dane['num'][0:7000]
filtr1=ag.pasmowozaporowy(sygnal, 200, 49, 51)
filtr2=ag.pasmowoprzepustowy(filtr1, 200, 1, 50)

plt.subplot(3, 1, 1)
plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.title("Ryc. 1.1. Sygnał")

plt.subplot(3, 1, 2)
plt.plot(t, filtr2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.title("Ryc. 1.2. Sygnał po filtracji")

plt.subplot(3, 1, 3)
plt.plot(t, num)
plt.xlabel("Czas [s]")
plt.ylabel("Cyfra [-]")
plt.title("Ryc. 1.3. Podświetlane kolejno cyfry")
plt.tight_layout()

plt.figtext(0.45, 0.01,'Ryc. 1.', ha='center', fontsize=12)
plt.show()


kod=[]
probka_p=0
probka_k=probka_p+1400

for j in range(0, 5):
    szczyt=filtr2[0]

    for i in range(probka_p, probka_k):
        if filtr2[i]>szczyt:
            szczyt=filtr2[i]
            print(szczyt)
            ktora=i

    probka_p+=1400
    probka_k+=1400
    if j==5:
        probka_k==probka_p
    kod.append(num[ktora])
print("Kod:", kod)
