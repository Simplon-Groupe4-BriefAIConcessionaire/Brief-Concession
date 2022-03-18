from flask import Blueprint, render_template, request, redirect, url_for, session, json
from .model import Voitures
from app import db
import pandas as pd
from .arbre import arbre

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template("accueil.html")

@views.route('/liste_voitures', methods=['GET', 'POST'])
def ListeVoitures():
    voiture_dataframe = requete_database_voiture()
    return render_template('liste_voitures.html', liste_voitures=voiture_dataframe)

def requete_database_voiture():
    voiture_dataframe = pd.read_sql_table('voiture', db.engine)
    return voiture_dataframe.head(10)

@views.route('/ajout_voiture', methods=['GET', 'POST'])
def AjoutVoiture():

    if request.method == "POST":
        voiture_url = request.form['url']
        voiture_title = request.form['title']
        voiture_version = request.form['version']
        voiture_prix = request.form['prix']
        voiture_annee = request.form['annee']
        voiture_kilometrage = request.form['kilometrage']
        voiture_energie= request.form['energie']
        voiture_emissions = request.form['emissions']
        voiture_transmission = request.form['transmission']
        voiture_portes = request.form['portes']
        voiture_puissance = request.form['puissance']
        voiture_places = request.form['places']
        
        nv_voiture = Voitures(url =voiture_url, 
        title = voiture_title,
        version = voiture_version,
        prix = voiture_prix,
        annee = voiture_annee,
        kilometrage = voiture_kilometrage,
        energie = voiture_energie,
        emissions = voiture_emissions,
        transmission = voiture_transmission,
        portes=voiture_portes,
        puissance=voiture_puissance,
        places=voiture_places
        )

    db.session.add(nv_voiture)
    db.session.commit()
    
    
    
@views.route('/prediction', methods=['GET', 'POST'])
def prediction_nouvelle_voiture():
    if request.method == "POST":
        voiture_annee = request.form['Date']
        voiture_kilometrage = request.form['Km']
        voiture_puissance = request.form['Puissance']
    result = arbre.my_model_execution()
    return prediction_nouvelle_voiture(result)
    # result = result
    # return render_template("prediction.html", result = result)
    # return "<p>"+str(voiture_prix)+"</p>"
