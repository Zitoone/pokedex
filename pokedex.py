import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

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
root.config(background="#E0B0FF")
root.iconbitmap("pikachu.ico")

title = tk.Label(root, text="♀ LES MEILLEURES FEMELLES ♀", padx=20, pady=50, font=("Helvetica bold", 20), bg="#E0B0FF", fg="purple")
title.pack()

frame1 = tk.Frame(root, bg="#E0B0FF", highlightbackground="purple", highlightthickness=3,height="300", width=100, bd=5, relief="raised")
frame1.pack(side="left", padx=20, pady=20, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame1, height=5, justify="center", bg="pink", font="Helvetica", fg="purple")
listbox.pack(side=tk.TOP, padx=10)

label_image = tk.Label(frame1, bg="#E0B0FF")
label_image.pack(padx=20, pady=20)

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

for nom in dictionnaire:
    listbox.insert(tk.END, nom)

frame2 = tk.Frame(root, bg="pink", highlightbackground="purple", highlightthickness=3,height="300", width=100, bd=5, relief="raised")
frame2.pack(side="top", fill=tk.NONE, expand=False)


label_info = tk.Label(frame2, bg="pink", text="Sélectionne une pokémone pour voir les détails.", font=("Helvetica", 14), fg="purple", bd=1)
label_info.pack(pady=10)

new_pok=tk.Entry(frame2, fg="purple")
user=tk.Label(frame2, text="Nom de ta pokemone", bg="pink")
user.pack()
new_pok.pack(pady=10)

listbox.bind("<<ListboxSelect>>", afficher_details)

def bouton_clique():
    messagebox.showinfo("Boite de dialogue", "A bientôt!!")
   
bouton=tk.Button(root, text="QUITTER", bg="#E0B0FF", command=bouton_clique)
bouton.place(x=800, y=550)


root.mainloop()
