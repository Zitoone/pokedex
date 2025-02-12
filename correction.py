# correction JL

"""
Un Pokédex simple qui permet :
- D'afficher les informations sur un pokemon
- D'ajouter un pokemoent
- De changer de pokemon pour voir ses infos
"""
import tkinter as tk
from tkinter import messagebox

class Pokemon:
   def __init__(self, name, type, capacities):
      self.name = name
      self.type = type
      self.capacities = capacities

# Peupler des pokémons par défaut
pokedex = [
   Pokemon("Bulbizarre", "Grass", ["Grass, Poison"]),
   Pokemon("Charmander", "Fire", ["Fire, Tail hit"]),
   Pokemon("Squirtle", "Water", ["Water, other"]),
   Pokemon("Pikachu", "Electric", ["Electric, Quick Attack"]),
]

# C'est une fonction et non une méthode de Pokemon
def add_pokemon():
   name = entry_name.get()
   type = entry_type.get()
   capacities = entry_capacities.get().split(", ")
   # Ajouter le nouveau pokémon dans la liste
   pokedex.append(Pokemon(name, type, capacities))
   list_pokemons.insert(tk.END, name)
   messagebox.showinfo("Ajout du pokémon", f"Le pokémon {name} a été ajouté avec succès")

# Afficher le pokémon dans une messagebox
def show_pokemon():
   index = list_pokemons.curselection()
   if index:
      pokemon = pokedex[index[0]]
      messagebox.showinfo("Détails du pokémon", f"Nom : {pokemon.name}\nType : {pokemon.type}\nCapacités : {pokemon.capacities}")
   else:
      messagebox.showerror("Erreur", "Vous devez sélectionner un pokémon")

root = tk.Tk()
root.title("Pokédex")

# Liste des pokemons
list_pokemons = tk.Listbox(root)
# Parcourir la liste des pokemons (pour afficher les infos)
for pokemon in pokedex:
   list_pokemons.insert(tk.END, pokemon.name)
list_pokemons.pack()
button_details = tk.Button(root, text="Afficher les infos", command=show_pokemon)
button_details.pack()

# Formulaire d'ajout de pokemon
label_name = tk.Label(root, text="Nom du Pokémon :")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_type = tk.Label(root, text="Type du Pokémon :")
label_type.pack()
entry_type = tk.Entry(root)
entry_type.pack()

label_capacities = tk.Label(root, text="Capacités du Pokémon (séparé par une virgule) :")
label_capacities.pack()
entry_capacities = tk.Entry(root)
entry_capacities.pack()

button_add = tk.Button(root, text="Ajouter le pokémon", command=add_pokemon)
button_add.pack()

root.mainloop()
