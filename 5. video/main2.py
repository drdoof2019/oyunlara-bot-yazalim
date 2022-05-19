import pyautogui
import time
import os
import random
import math

def giris_yap():
    os.popen('start firefox')
    time.sleep(1)
    pyautogui.write('https://www.tribalwars.net/en-dk/')
    pyautogui.press('enter')
    time.sleep(3)
    coord = pyautogui.locateCenterOnScreen(r'.\assets\world.png',confidence=0.85)
    pyautogui.moveTo(coord,duration=1)
    time.sleep(1)
    pyautogui.leftClick(coord)
    time.sleep(3)
    coord = pyautogui.locateCenterOnScreen(r'.\assets\ic_mey.png',confidence=0.85)
    if coord != None:
        pyautogui.moveTo(coord,duration=1)
        time.sleep(1)
        pyautogui.leftClick(coord)
        time.sleep(2)
        coord = pyautogui.locateCenterOnScreen(r'.\assets\temizlik.png',confidence=0.85)
        pyautogui.moveTo(coord,duration=1)
        time.sleep(1)
        pyautogui.leftClick(coord)
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(1)
    else:
        coord = pyautogui.locateCenterOnScreen(r'.\assets\ic_mey_gece.png',confidence=0.85)
        pyautogui.moveTo(coord,duration=1)
        time.sleep(1)
        pyautogui.leftClick(coord)
        time.sleep(2)
        coord = pyautogui.locateCenterOnScreen(r'.\assets\temizlik.png',confidence=0.85)
        pyautogui.moveTo(coord,duration=1)
        time.sleep(1)
        pyautogui.leftClick(coord)
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(1)



def kilic_mizrak_degeri_gir(mizrak_sayi,kilic_sayi):
    mizrak_coord = pyautogui.locateCenterOnScreen(r'.\assets\mizrak.png',confidence=0.85)
    kilic_coord = pyautogui.locateCenterOnScreen(r'.\assets\kilic.png',confidence=0.85)
    if mizrak_sayi != 0:
        pyautogui.moveTo((mizrak_coord.x,mizrak_coord.y+30))
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.write(mizrak_sayi)
    if kilic_sayi != 0:
        pyautogui.moveTo((kilic_coord.x,kilic_coord.y+30))
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.write(kilic_sayi)


def basla_butonuna_bas():
    basla_butonlari = pyautogui.locateAllOnScreen(r'.\assets\basla.png',confidence=0.85)
    #print(list(basla_butonlari))
    basla_butonlari = list(list(basla_butonlari))
    if len(basla_butonlari) != 0:
        #print(pyautogui.center(basla_butonlari[0]))
        pyautogui.moveTo(pyautogui.center(basla_butonlari[-1]))
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(100,100)
        time.sleep(1)
    else:
        print("Tespit edilemedi")

def sure_hesapla(mizrak_sayi,kilic_sayi,seviye):
    ham_miktari = int(mizrak_sayi) * 25 + int(kilic_sayi) * 15
    if seviye == 2:
        seviye_2_icin_formul = (((0.25 * ham_miktari) ** 2 * 100) ** 0.45 + 1800) * 0.7722074897
        return math.ceil(seviye_2_icin_formul)
    if seviye == 1:
        seviye_1_icin_formul = (((0.1 * ham_miktari ) ** 2 * 100)** 0.45 + 1800) * 0.7722074897
        return math.ceil(seviye_1_icin_formul)

def firefox_kapat():
    coord = (1890,20)
    time.sleep(1)
    pyautogui.moveTo(coord)
    time.sleep(1)
    pyautogui.leftClick()

if __name__ == "__main__":

    while True:
        giris_yap()
        time.sleep(1)
        # Humble Haulers
        kilic_mizrak_degeri_gir("5","5")
        basla_butonuna_bas()
        sure1 = sure_hesapla("5","5",2)
        # Lackadaisical Looters
        kilic_mizrak_degeri_gir("10","5")
        basla_butonuna_bas()
        time.sleep(1)
        sure2 = sure_hesapla("10","5",1)
        time.sleep(2)
        firefox_kapat()
        print("sure1:",sure1)
        print("sure2:",sure2)
        if sure1>sure2:
            print("sure1 kadar bekliyoruz")
            time.sleep(sure1)
        else:
            print("sure2 kadar bekliyoruz")
            time.sleep(sure2)
