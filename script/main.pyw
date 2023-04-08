from tkinter import *

from phonenumbers import geocoder, parse, carrier
 
root = Tk()
root.geometry("400x175")
root.title('Phone Tracker')

def afficher_pressed():
    
    
    numero = my_entry.get()
    root.geometry("400x275")
    
    content_txt3 = "Numero de téléphone : "+ str(numero)
    txt3.set(content_txt3)
    
    content_txt4 = "Location : "+ geocoder.description_for_number(parse(numero, "CH"), "fr")
    txt4.set(content_txt4)
    
    content_txt5 = "Service : "+ carrier.name_for_number(parse(numero, "RO"),"fr")
    txt5.set(content_txt5)

txt1=StringVar()
txt1.set("INSCRIVEZ LE NUMERO DE TELEPHONE DONT VOUS")
texteLabel = Label(root, textvariable = txt1)
texteLabel.pack(side=TOP, padx=50, pady=10)

txt2=StringVar()
txt2.set("VOULEZ DES INFORMATIONS    (ex : +33606060606 )")
texteLabel = Label(root, textvariable = txt2)
texteLabel.pack(side=TOP, padx=50, pady=0)

my_entry = Entry(root, width=200)
my_entry.pack(side=TOP, padx=50, pady=10)

bouton=Button(root, text="Afficher les informations", padx=50, pady=10, command=afficher_pressed, width=200)
bouton.pack(side=TOP, padx=50, pady=10)

txt3=StringVar()
content_txt3 = "Numero de téléphone :       "
txt3.set(content_txt3)
texteLabel = Label(root, textvariable = txt3)
texteLabel.pack(padx=50, pady=5)

txt4=StringVar()
content_txt4 = "Location :       "
txt4.set(content_txt4)
texteLabel = Label(root, textvariable = txt4)
texteLabel.pack(padx=50, pady=5)

txt5=StringVar()
content_txt5 = "Service :       "
txt5.set(content_txt5)
texteLabel = Label(root, textvariable = txt5)
texteLabel.pack(padx=50, pady=5)
 
root.mainloop()
