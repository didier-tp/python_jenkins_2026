from flask import Flask, request
from mensualite import mensualite

app = Flask(__name__)

# http://127.0.0.1:5000/hello 
@app.route("/hello")
def hello_world():
    return "<p>Hello, Bonjour</p>"
    
# http://127.0.0.1:5000/mensualite?montant=10000&duree=60&taux=2
# retournant {"mensualite":175.27760053243998,"montant":10000.0,"duree":60.0,"taux":2.0} (à peu près)   
@app.route("/mensualite")
def get_mensualite():
    montant = float(request.args.get('montant'))
    nb_mois = float(request.args.get('duree'))
    taux= float(request.args.get('taux'))
    res_mensualite=mensualite(montant,nb_mois,taux)
    print("mensualite=",res_mensualite)
    return "{"+f'"mensualite":{res_mensualite},"montant":{montant},"duree":{nb_mois},"taux":{taux}'+"}"
    
    
#installation possible de flask sur debian:
#sudo apt install python3-flask 
#
#lancement du serveur avec flask:
#flask --app emprunt_api run 
#
#URL de test: http://127.0.0.1:5000/hello
#             http://127.0.0.1:5000/mensualite?montant=10000&duree=60&taux=2
#avec navigateur ou bien 
#curl http://127.0.0.1:5000/hello 
#curl 'http://127.0.0.1:5000/mensualite?montant=10000&duree=60&taux=2'