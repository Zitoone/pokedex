import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

bg="#E0B0FF"

def afficher_details(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        nom = listbox.get(index)
        details = dictionnaire[nom]

        label_info.config(text=f"Nom : {nom}\nType : {details['Type']}\nTalent : {details['Talent']}\nTaux de capture : {details['Taux de capture']}")
        
        if 'image' in details:
            image = details['image']
            image_resized = image.resize((250, 250))
            image_resized = ImageTk.PhotoImage(image_resized)
            label_image.config(image=image_resized)
            label_image.image = image_resized 
        else:
            label_image.config(image='')

root = tk.Tk()
root.title("POKEDEX Olivia")
root.geometry("980x620")
root.config(bg=bg)
root.iconbitmap("pikachu.ico")

title = tk.Label(root, text="♀ LES MEILLEURES FEMELLES ♀", padx=20, pady=50, font=("Helvetica bold", 20), bg=bg, fg="purple")
title.pack()

frame1=tk.Frame(root, bg=bg, height=300, width=100)
frame1.place(x=50, y=150)

listbox = tk.Listbox(frame1, height=7, justify="center", bg="pink", font="Helvetica", fg="purple")
listbox.pack(side=tk.TOP, padx=10)

label_image = tk.Label(frame1, bg=bg)
label_image.pack(padx=20, pady=20)

class Pokemons:
    def __init__(self, nom, type, talent, taux_de_capture, image):
        self.pokemons={}
        self.nom= nom
        self.type=type
        self.talent= talent
        self.taux_de_capture= taux_de_capture
        self.image= image

dictionnaire = {
    "Flabébé": {
        "Type": "Fée",
        "Talent": "Flora voile / Symbiose",
        "Taux de capture": "225",
        "image": Image.open("flabébé.png"),
    },
    "Floette": {
        "Type": "Fée",
        "Talent": "Joli sourire / Garde magic",
        "Taux de capture": "120",
        "image": Image.open("Floette.png")
    },
    "Forgella": {
        "Type": "Fée / Acier",
        "Talent": "Brise Moule / Tempo Perso / Pickpocket",
        "Taux de capture": "90",
        "image": Image.open("Forgella.png")
    },
    "Lumivole": {
        "Type": "Insecte",
        "Talent": "Benêt / Lentiteintée / Farceur",
        "Taux de capture": "150",
        "image": Image.open("Lumivole.png")
    },
    "Sucreine": {
        "Type": "Plante",
        "Talent": "Feuille Garde / Prestance Royale",
        "Taux de capture": "45",
        "image": Image.open("Sucreine.png")
    },
}
for Nom in dictionnaire:
    listbox.insert(tk.END, Nom)

frame2 = tk.Frame(root, bg=bg, highlightbackground="purple", highlightthickness=3,height="300", width=100, bd=5, relief="raised")
frame2.place(x=400, y=150)

label_info = tk.Label(frame2, bg=bg, text="Tu peux sélectionner une pokémone pour voir ses détails\nou saisir une nouvelle ci-dessus", font=("Helvetica", 12), fg="purple", bd=1)
label_info.pack(pady=10)

frame3= tk.Frame(root, bg=bg)
frame3.place(x=440, y=300)

def ajouter_pokemon():
    nom=champ_nom.get()
    type=champ_type.get()
    talent=champ_talent.get()
    taux_de_capture=champ_taux.get()
    label_info.config(text=f"nom: {nom}\nType {type}\nTalent : {talent}\nTaux de capture : {taux_de_capture}")

def add_to_listbox():
    new_name = champ_nom.get()
    if new_name:
        listbox.insert(tk.END, new_name)

def download_image():
    file_path=filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        image=Image.open(file_path)
        image_resized = image.resize((250, 250))
        image_resized = ImageTk.PhotoImage(image_resized)
        dictionnaire[file_path]=image_resized

champ_nom=tk.Entry(frame3, fg="purple", width=30, font="Arial", justify="center")
add_name=tk.Label(frame3, text="Nom de ta pokemone", bg=bg)
add_name.pack()
champ_nom.pack(pady=2)
champ_type=tk.Entry(frame3, fg="purple",width=30, font="Arial", justify="center")
add_type=tk.Label(frame3, text="Type", bg=bg)
add_type.pack()
champ_type.pack(pady=2)
champ_talent=tk.Entry(frame3, fg="purple", width=30, font="Arial", justify="center")
add_talent=tk.Label(frame3, text="Talent", bg=bg)
add_talent.pack()
champ_talent.pack(pady=2)
champ_taux=tk.Entry(frame3, fg="purple",width=30, font="Arial", justify="center")
add_taux=tk.Label(frame3, text="Taux de capture", bg=bg)
add_taux.pack()
champ_taux.pack(pady=2)
champ_image=tk.Entry(frame3, fg="purple")
add_image=tk.Label(frame3, text="Télécharge sa photo", bg=bg)
add_image.pack()
champ_image.pack(pady=2)

enter=tk.Button(frame3, text="Ajouter", bg=bg, fg="purple", command=lambda:[ajouter_pokemon(),add_to_listbox(),download_image()])
enter.pack(pady=20)

listbox.bind("<<ListboxSelect>>", afficher_details)

bouton=tk.Button(root, text="QUITTER", bg=bg, fg="purple", command=root.destroy)
bouton.place(x=900, y=580)

root.mainloop()