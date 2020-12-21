#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# le "re"=expression régulière
import os, json, re 
os.system("clear")

from flask import Flask
app = Flask(__name__)
app._static_folder = os.path.abspath("./")
   
# route qui renvoie la page HTML   
@app.route('/client')  
def recherche_1():
   print('/client')
   if os.path.isfile("client.html") :
       return app.send_static_file("client.html")
   return "client.html non accessible"

# route qui renvoie le CSS
@app.route('/css')
def css():
   print('/css')
   if os.path.isfile("client.css") :
       return app.send_static_file("client.css")
   return "client.css non accessible"

# route qui renvoie le fond
@app.route('/image')
def image():
   print('/image')
   if os.path.isfile("fond1.jpg") :
       return app.send_static_file("fond1.jpg")
   return "fond non accessible"

# route qui renvoie le favicon
@app.route('/favicon')
def favicon():
   print('/favicon')
   if os.path.isfile("favicon.ico") :
       return app.send_static_file("favicon.ico")
   return "favicon non accessible"


# route qui renvoie le critère
@app.route('/client/<critere>')
def recherche_critere(critere):
   print("/client/"+critere)
   lignes = []
   liste = os.listdir("PAGES")
   for fichier in liste :
      fd = open("PAGES/"+fichier)
      print (fichier)
      for ligne in fd.readlines() :
         # L'expression régulière (re) permet de récupérer ce dont on a besoin (, +, /,., etc.)
         res1 = re.search("\[\[.+\]\]", ligne) 
         # IGNORECASE permet de ne pas pendre en compte les majuscules 
         res2 = re.search(critere, ligne, re.IGNORECASE)        
         if res1 and res2 :
            # Le nom de la page est envoyée avant la ligne dans une sous-liste
            lignes.append([fichier,ligne])
            '''lignes.append(ligne)'''
    
    #Structure et transmet des données sur des sites web 
    #(Ex : envoie des données serveur --> client pour les afficher sur une page web, ou vice versa)
   return json.dumps(lignes) 


app.run(host='127.0.0.1', port=5000,debug=True)
