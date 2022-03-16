from csv import reader
from main import app
from __init__ import db
from model import Voitures



with app.app_context():
    with open('test.csv', 'r', encoding='UTF-8', errors='ignore') as file:
        csv_reader = reader(file)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                # print(row[3])
                v = Voitures(url = row[0], title = row[1],version = row[2], prix = row[3], annee = row[4], kilometrage = row[7], energie = row[9], emissions = row[10], transmission = row[11],portes=row[12],puissance=row[13],places=row[14])
                db.session.add(v)
    db.session.commit()
