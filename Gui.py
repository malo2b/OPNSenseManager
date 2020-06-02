from tkinter import *
from tkinter import ttk
from systemeLogs import *
from traitementFichierIni import ecrireConfigIni
import json
from Base import *
from apiFunc import *

# BG color #353542
# Sucess color #32b643
# Error color #e44414
# Button color #5757da
# font color #e6eced


def recupereDonneesFormConfig(ip,apiKey,apiSecret,window):
    datas = {
        "ip" : ip,
        "apiKey" : apiKey,
        "apiSecret" : apiSecret
    }
    datas_dump=json.dumps(datas)
    datas_json=json.loads(datas_dump)


    choisirPage(window,"accueil")
    ecrireConfigIni(datas_json["ip"], datas_json["apiKey"], datas_json["apiSecret"])

    if lireIni():
        choisirPage(window,"accueil")
    else:
        choisirPage(window,"config")



def afficherPageConfig(window):
    logger.warning('Affichage page config')
    # frame Titre
    frame_title=Frame(window,bg='#353542')
    title=Label(frame_title,text="Configuation", font=("Courrier",20), bg='#353542', fg='#e6eced')
    title.pack()
    frame_title.pack()

    # frame Formulaire
    frame_form=Frame(window,bg='#353542')

    ipText = Label(text = "IP",width = "20")
    apiKeyText = Label(text = "api key",width = "20")
    apiSecretText = Label(text = "api secret",width = "20")
    ipText.place(x = 15, y = 70)
    apiKeyText.place(x = 15, y = 140)
    apiSecretText.place(x = 15, y = 210)

    ip = StringVar()
    apiKey = StringVar()
    apiSecret = StringVar()

    ip_entry = Entry(textvariable = ip, width = "20")
    apiKey_entry = Entry(textvariable = apiKey, width = "20")
    apiSecret_entry = Entry(textvariable = apiSecret, width = "20")

    ip_entry.place(x = 220, y = 70)
    apiKey_entry.place(x = 220, y = 140)
    apiSecret_entry.place(x = 220, y = 210)

    register = Button(window,text = "Valider", width = "20", height = "1", command = lambda: recupereDonneesFormConfig(ip.get(),apiKey.get(),apiSecret.get(), window), bg = "#32b643")
    register.place(x = 15, y = 260)


def afficherPageAccueil(window):
    logger.info('Affichage page accueil')
    # Frame title
    frame_title=Frame(window,bg='#353542')
    title=Label(frame_title,text="OPNSense Manager", font=("Courrier",20), bg='#353542', fg='#e6eced')
    title.pack()
    frame_title.pack()

    etatInternet=True

    # Button
    if etatInternet==False:
        bouton_internet=Button(window,text="Activer Internet",font=("courrier",20),bg="#32b643",fg="#e6eced") 
        bouton_internet.place(x=75,y=220)

    elif etatInternet==True:
        bouton_internet=Button(window,text="Désactiver Internet",font=("courrier",20),bg="#e44414",fg="#e6eced")
        bouton_internet.place(x=75,y=220)
        

    bouton_avance=Button(window,text="Paramètres avancés", font=("courrier",10), bg="#5757da", fg="#e6eced", command=lambda:choisirPage(window,"avance"))
    bouton_avance.place(x=200,y=450)

def afficherPageAvancee(window):
    logger.info("Affichage page avancee")

    # frame Titre
    frame_title=Frame(window,bg='#353542')
    title=Label(frame_title,text="Avancé", font=("Courrier",20), bg='#353542', fg='#e6eced')
    title.pack()
    frame_title.pack()

    # Check box

    checkBox1 = Checkbutton(window, text="Choix 1", bg='#353542', fg='#e6eced', font=("courrier",13))
    checkBox2 = Checkbutton(window, text="Choix 2", bg='#353542', fg='#e6eced', font=("courrier",13))
    checkBox3 = Checkbutton(window, text="Choix 3", bg='#353542', fg='#e6eced', font=("courrier",13))
    checkBox1.place(x=280,y=70)
    checkBox2.place(x=280,y=110)
    checkBox3.place(x=280,y=150)

    # Radio Bouton

    rb=IntVar()

    def choixRadioBouton():
        print(rb.get())

    objectJsonSourceInternet = json.loads(listeSourceInternet())
    listeSource=[]
    listeRadioBouton=[]

    y=70
    i=0

    for source in objectJsonSourceInternet:
        
        listeSource.append(objectJsonSourceInternet[source])
        listeRadioBouton.append(Radiobutton(text = listeSource[i] , variable=rb, value=i, command=choixRadioBouton, bg='#353542', fg='#e6eced', font=("courrier",13)))

        listeRadioBouton[i].place(x=15,y=y)
        y=y+30
        i+=1


    # radioButton1 = Radiobutton(text = "Choix 1", variable=rb, value=1, command=choixRadioBouton, bg='#353542', fg='#e6eced', font=("courrier",13))
    # radioButton2 = Radiobutton(text = "Choix 2", variable=rb, value=2, command=choixRadioBouton, bg='#353542', fg='#e6eced', font=("courrier",13))
    # radioButton3 = Radiobutton(text = "Choix 3", variable=rb, value=3, command=choixRadioBouton, bg='#353542', fg='#e6eced', font=("courrier",13))
    # radioButton1.place(x = 15, y = 70)
    # radioButton2.place(x = 15, y = 110)
    # radioButton3.place(x = 15, y = 150)

  
    # Liste Déroulante

    objectJsonIP = json.loads(listePostes())
    listeNom = []

    for poste in objectJsonIP:
        listeNom.append(objectJsonIP[poste]["utilisateur"])
        
    listeDéroulante= ttk.Combobox(window,values=listeNom)
    listeDéroulante.place(x=15,y=y+30, height=30, width=200)

    # retour

    bouton_retour=Button(window,text="Retour", font=("courrier",10), bg="#5757da", fg="#e6eced", command=lambda:choisirPage(window,"accueil"))
    bouton_retour.place(x=200,y=450)

def closeWindow(window):
    window.destroy()

def choisirPage(window,cible):
    for c in window.winfo_children():
        c.destroy()
    if cible == "config":
        afficherPageConfig(window)
    elif cible == "avance":
        afficherPageAvancee(window)
    else:
        afficherPageAccueil(window)
    

def afficherGui(choix):
    # Creation fenetre
    window=Tk()
    window.resizable(width=False, height=False)

    # Parametres
    window.title("OPNSense-Manager")
    window.geometry("400x500")
    window.config(background='#353542')

    choisirPage(window,choix)

    # afficher
    window.mainloop()

afficherGui("avance")