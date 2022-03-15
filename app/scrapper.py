import requests, re, time
from bs4 import BeautifulSoup


def get_links():

    with open("app/links.txt", 'w') as f:

        for i in range(1, 21):
            urlrecherche = "https://www.paruvendu.fr/auto-moto/listefo/default/default?auto-typeRech=&reaf=1&r2=&px1=&md=&codeINSEE=&lo=&pa=&ray=15&r=VVO00000&r1=&trub=&nrj=&km1=&co2=&a0=&a1=&npo=0&tr=&pf0=&pf1=&fulltext=&codPro=&p=" + str(i)
            response = requests.get(urlrecherche)
            soup = BeautifulSoup(response.text, 'html.parser')
            div = soup.findAll("div", {"class": "lazyload_bloc ergov3-annonce ergov3-annonceauto"})

            for l in div:
                a = l.find('a')
                link = a['href']
                f.write(link  + '\n')

get_links()


def get_infos():

    file1 = open('app\links.txt', 'r')

    links = file1.readlines()

    infos = []

    i = 0

    for link in links :

        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')


        try:
            version = soup.find("li", {"class": "vers"})
            version = version.find("span").get_text().strip()
        except:
            version = "null"


        try:
            prix = soup.find("li", {"class": "px"})
            prix = prix.find("span").get_text().strip()
            prix = prix.replace("€", "")
            prix = prix.replace(" ", "")
        except:
            prix = "null"


        try:
            annee = soup.find("li", {"class": "ann"})
            annee = annee.find("span").get_text()
            annee = annee.split('Le Comparateur')[0]
            annee = annee.strip()
        except:
            annee = "null"


        try:
            km = soup.find("li", {"class": "kil"})
            km = km.find("span").get_text()
            km = km.replace("km", "")
            km = km.replace(" ", "")
            km = km.strip()
        except:
            km = "null"


        try:
            energie = soup.find("li", {"class": "en"})
            energie = energie.find("span").get_text()
            energie = energie.strip()
        except:
            energie = "null"


        try:
            emission = soup.find("li", {"class": "emiss"})
            emission = emission.find("span").get_text()
            emission = emission.replace ("g/km", "")
            emission = emission.strip()
        except:
            emission = "null"


        try:
            conso = soup.find("li", {"class": "cons"})
            conso = conso.find("span").get_text()
            conso = conso.replace("litres / 100 km", "")
            conso = conso.strip()
        except:
            conso = "null"


        try:
            boitier = soup.find("li", {"class": "vit"})
            boitier = boitier.find("span").get_text()
            boitier = boitier.strip()
        except:
            boitier = "null"


        try:
            portes = soup.find("li", {"class": "carro"})
            portes = portes.find("span").get_text()
            portes = portes.strip()
        except:
            portes = "null"


        try:
            puissance = soup.find("li", {"class": "puiss"})
            puissance = puissance.find("span").get_text()
            puissance = puissance.replace("CV", "")
            puissance = puissance.strip()
        except:
            puissance = "null"


        try:
            places = soup.find("li", {"class": "por"})
            places = places.find("span").get_text()
            places = (re.findall('\d+', places )[0])
        except:
            places = "null"

        infos.append([version, prix, annee, km, energie, emission, conso, boitier, portes, puissance, places])

        
        i = i+1
        time.sleep(5)
        return infos

get_infos()