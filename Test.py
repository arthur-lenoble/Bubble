import tkinter as tk
from tkinter import messagebox

# Dictionnaire des sites enregistrés
registered = {
    'google': 'Google\nhttps://www.google.com',
    'chatgpt': 'ChatGPT\nhttps://www.chatgpt.com',
    'wikipedia': 'Wikipedia : l\'encyclopédie libre\nhttps://fr.wikipedia.org',
    'jeux': 'Crazy Games\nhttps://www.crazygames.com',
    'canva': 'Canva\nhttps://www.canva.com',
    'youtube': 'YouTube\nhttps://www.youtube.com',
    'github': 'GitHub\nhttps://www.github.com',
    'stackoverflow': 'Stack Overflow\nhttps://www.stackoverflow.com',
    'reddit': 'Reddit\nhttps://www.reddit.com',
    'linkedin': 'LinkedIn\nhttps://www.linkedin.com',
    'amazon': 'Amazon\nhttps://www.amazon.com',
    'twitter': 'Twitter\nhttps://www.twitter.com',
    'instagram': 'Instagram\nhttps://www.instagram.com',
    'facebook': 'Facebook\nhttps://www.facebook.com',  # Correction du lien
    'trad': 'Google Traduction\nhttps://translate.google.fr\n\nDeepL\nhttps://www.deepl.com',
    'trinket': 'Trinket\n(strongly recommended)\nhttps://www.trinket.io'
}

# Fonction de recherche
def dictSearch():
    search_term = search_entry.get().strip().lower()  # Récupérer l'entrée utilisateur
    result_text.delete(1.0, tk.END)  # Effacer les anciens résultats
    found = False
    
    # Recherche des correspondances
    for key, value in registered.items():
        if key.startswith(search_term):
            result_text.insert(tk.END, f"{value}\n\n")
            found = True
    
    if not found:
        result_text.insert(tk.END, "Rien ne correspond à votre recherche...\n")
        suggest(search_term)

# Suggestions basées sur l'entrée utilisateur
def suggest(search_term):
    suggestions = {
        'goo': 'Essayez Google',
        'je': 'Essayez Jeux',
        'cha': 'Essayez ChatGPT',
        'w': 'Essayez Wikipedia',
        'ca': 'Essayez Canva',
        'y': 'Essayez YouTube',
        'gi': 'Essayez GitHub',
        's': 'Essayez Stack Overflow'
    }
    for key, suggestion in suggestions.items():
        if key in search_term:
            result_text.insert(tk.END, f"{suggestion}\n")

# Création de l'interface graphique
root = tk.Tk()
root.title("Bubble Search")
root.geometry("500x400")

# Champ de recherche
search_label = tk.Label(root, text="Entrez votre recherche :", font=("Arial", 12))
search_label.pack(pady=10)

search_entry = tk.Entry(root, font=("Arial", 14), width=30)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Rechercher", command=dictSearch, font=("Arial", 12), bg="lightblue")
search_button.pack(pady=10)

# Zone d'affichage des résultats
result_text = tk.Text(root, height=15, font=("Arial", 12), wrap=tk.WORD)
result_text.pack(pady=10, padx=10)

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quitter", command=root.destroy, font=("Arial", 12), bg="lightcoral")
quit_button.pack(pady=5)

# Lancement de la boucle principale
root.mainloop()
