import os
print('Bubble search ')

registered = {
    'google': 'Google\nhttps://www.google.com\n\nBing\nhttps://www.bing.com',
    'chatgpt': 'ChatGPT\nhttps://www.chatgpt.com\n\nGemini\nhttps://gemini.google.com\n\nCopilot\nhttps://www.microsoftcopilot.com',
    'wikipedia': 'Wikipedia : l\'encyclopédie libre\nhttps://fr.wikipedia.org\n\n\tEnvie de changement ?\n\nFandom\nhttps://www.fandom.com',
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
    'facebook': 'Facebook\nhttps://www.facebook.,com',
    'trad':'Google Traduction\nhttps://translate.google.fr\n\nDeepL\nhttps://www.deepl.com',
    'trinket':'Trinket\n(strongly recommended)\nhttps://www.trinket.io',
    'moteur de recherche':'Google (https://www.google.com)et Bing (https://www.bing.com)sont les plus connus.\n Voici quelques alternatives :\n\nDuckDuckGo\nhttps://www.duckduckgo.com\n\nEcosia\nhttps://www.ecosia.org\nBubble Search reste le plus sur car il n\'interagit pas avec le web.',
    'apprendre à coder':'Je te conseille Codegym, il te permet d\'apprendre quasiment tous les langages en t\'amusant. \nhttps://www.codegym.cc'
}
def dictSearch(entree) :
  for key in registered :
    if key.startswith(entree) :
      print(registered[key])
  
espaces=' '*20

while True:
    try:
        search = input('🔎')
        os.system('clear')
        print(espaces+'🔎'+search)
        dictSearch(search)
    except KeyError:
        if not search.islower():
            print('Veuillez écrire en minuscules uniquement. Nous ne supportons pas les majuscules.')
        else:
            print('Rien ne correspond à votre recherche... Évitez les espaces inutiles.')
        
        if 'goo' in search.lower():
          print('Essayez google')
        if 'je' in search.lower():
          print('Essayez jeux ')
        if 'cha'in search.lower():
          print('Essayez chatgpt')
        if 'w' in search.lower() :
          print('Essayez wikipedia')
        if 'ca' in search.lower():
          print('Essayez canva')
        if 'y' in search.lower() :
          print('Essayez youtube')
        if 'gi' in search.lower() or 'gui' in search.lower() :
          print('Essayez github')
        if 's' in search.lower() :
          print('Essayez stackoverflow')
         
          
        
    finally :
        print('C\'est tout pour l\'instant !')
