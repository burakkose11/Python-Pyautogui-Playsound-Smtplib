import sys
import pyautogui
from playsound import playsound
import smtplib

while 1:
    gonderen_kullanici = "mailadresiniz@outlook.com"
    gonderen_sifre = 'sifreniz'
    alici_mail = 'alicimail@gmail.com'
    alici_konu = 'Oyun Uyarisi'
    alici_mesaj = 'Aman Tanrim Oyun Durdu !!! '
    email_text = """
    From: {}
    To: {}
    Subject: {}
    {}
    """ .format(gonderen_kullanici, alici_mail, alici_konu, alici_mesaj)
    try:
        server = smtplib.SMTP('smtp.office365.com:587')
        server.starttls()
        server.login(gonderen_kullanici, gonderen_sifre)
    except:
        print("birsey oldu!")

    if pyautogui.locateOnScreen('oyunBitti.png', confidence=0.8) != None:
        server.sendmail(gonderen_kullanici, alici_mail, email_text)
        print('mail uctu haberin olsun')
        server.close()
        print("görüyorum")
        playsound("hucummarsi.mp3")
    else:
        print("göremiyorum")