# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 01:51:12 2020
@author: C21373
"""
from webcontroller.ie import IExplore
import models
import sys, time, re
from bs4 import BeautifulSoup
params_search ={
    "__checkbox_recherche.excludeClosed":"true",
    "recherche.adresse": "",
    "recherche.captcha": "",
    "recherche.commune": "",
    "recherche.excludeClosed": "true",
    "recherche.raisonSociale":"",
    "recherche.sirenSiret":""
}
___URL_SIRENE_ROOT___ = "https://sirene.fr/sirene/public/recherche"
___ERROR_ETAB_NOT_FOUND___ = 'Aucun établissement pour le siren avec ce code postal'
class sirene(object,):

    def __init__(self, urlroot):
        self.__urlroot__ = urlroot
        self.__ie__ =  IExplore(self.__urlroot__)


    def find(self,list_criterias):
        params_search.update(list_criterias)    
        url = self.__urlroot__ + "?" + self.createHttpRequestParam(params_search)
        self.__ie__.load(url)
        self.read()

    def createHttpRequestParam(self, list_params):
        return ( "&".join([("{}={}".format(key, list_params[key])) for key in list_params]))
    

    def readitems(self, s, name):
        label = s.find_all("label", text = re.compile(name))[0]
        value = label.find_parent().get_text("", strip = False).replace("\n", " ").replace("\t", " ")
        value = re.sub(r"( ){2,}", " ", value)
        values = re.match( r"(.*)[:](.*)",  value).groups()
        # if (len(values) > 1 ):
        #     lists[values[0].strip()] = ":".join(values[1:] ).strip()
        return values 


    def read(self):
        doc = self.__ie__.getdocument()            
       
        soup = BeautifulSoup(doc.body.innerHTML)
        form = soup.select('#rechercheEntreprise')
        if not (form):
            print("form: " , form)
            return 0        

        etab_groups = soup.select(".accordion-group")

        if not len(etab_groups):
            raise Exception(___ERROR_ETAB_NOT_FOUND___)

        for group in etab_groups:

            siret = re.sub(r"[^0-9]", "", group.select("span.echo-siret")[0].get_text(strip = True))

            infos_etab = dict({'siret': siret})       
            infos_etab['siren'] =  infos_etab['siret'][0:9]       
            infos_etab["nom_commercial"] = self.readitems(group, "Enseigne")[1]
            
            adresse = self.readitems(group, "Adresse")[1]
            address = re.match( r"(.*)([0-9]{5}) ([a-zA-Z].*)", adresse).groups()
            if (len(address) > 2):
                infos_etab.update(dict({"voie": address[0], "code_postal": address[-2], "commune": address[-1]}))

            models.write2('etab', infos_etab)


def HttpRequestParam(paramsNew):
    PARAMS = {"__checkbox_recherche.excludeClosed":"true",
            "recherche.adresse": "",
            "recherche.captcha": "",
            "recherche.commune": "",
            "recherche.excludeClosed": "true",
            "recherche.raisonSociale":"",
            "recherche.sirenSiret":"" }
    PARAMS.update(paramsNew)
    return ( "&".join([("{}={}".format(key, PARAMS[key])) for key in PARAMS]))


def readetablissement(doc):
    
    # arg = "div.accordion-group"
    html = doc.body.innerHTML
    soup = BeautifulSoup(html)
    form = soup.select('#rechercheEntreprise')
    if not (form):
        print("form: " , form)
        return 0

    etab_groups = soup.select(".accordion-group")
    print("len: " ,  len(etab_groups))

    if not len(etab_groups):
        raise Exception(___ERROR_ETAB_NOT_FOUND___)

    for group in etab_groups:

        siret = re.sub(r"[^0-9]", "", group.select("span.echo-siret")[0].get_text(strip = True))

        lists = dict({'siret': siret})

        for label in group.find_all("label"):

            if not re.match("(Adresse|Enseigne)",label.get_text()):
                continue

            text = label.find_parent().get_text("", strip = False).replace("\n", " ").replace("\t", " ")
            while(True):
                text = text.replace("  ", " ")
                if (text == text.replace("  ", " ")):
                    break

            values = re.match( r"(.*)[:](.*)",  text).groups()

            if (len(values) > 1 ):
                lists[values[0].strip()] = ":".join(values[1:] ).strip()

        infos_etab = {"nom_commercial" : lists['Enseigne'] , "siret" : lists['siret'], "code_insee":"" , "siren":lists['siret'][:9] }

        address = re.match( r"(.*)([0-9]{5}) ([a-zA-Z].*)",  lists["Adresse"]).groups()
        if (len(address) > 2):
            infos_etab.update(dict({"voie": address[0], "code_postal": address[-2], "commune": address[-1]}))

        models.write2('etab', infos_etab)
       
# ie= IExplore(___URL_SIRENE_ROOT___)

todolist = models.readMinusDistinct("pdl", "etab", 'code_postal,siren')
print("il reste {} à traiter".format(len(todolist)))

for code_postal, siren  in todolist:
    ie= sirene(___URL_SIRENE_ROOT___)
    if (code_postal =="" or siren ==""):
        continue

    # print(code_postal, siren)
    # exit()
    sirenUrl = siren[0:3] + "+" + siren[3:6] + "+" + siren[6:9]
    liste = {"recherche.sirenSiret": sirenUrl, "recherche.commune": code_postal }
    ie.find(liste)


# try:
#     readetablissement(ie.getdocument())
# except:
#     infos_etab =dict({'code_postal': todolist[0][0], 'siren': todolist[0][1]})
#     print("Unexpected error:", sys.exc_info())
# exit()

# for code_postal, siren  in todolist:
#     if (code_postal =="" or siren ==""):
#         continue

#     # print(code_postal, siren)
#     # exit()
#     sirenUrl = siren[0:3] + "+" + siren[3:6] + "+" + siren[6:9]

#     url = ___URL_SIRENE_ROOT___ + "?" +  HttpRequestParam({"recherche.sirenSiret": sirenUrl, "recherche.commune": code_postal })
#     ie.load(url)
#     print("url: ", url)
#     try:
#         readetablissement(ie.getdocument())
#     except:
#         error_msg =  sys.exc_info()[1]
#         print("Unexpected error:", error_msg)
#         models.write2('etab', dict({'siret': 'ERROR_{}/{}'.format(code_postal, siren) , 'voie' : ___ERROR_ETAB_NOT_FOUND___ ,'code_postal': code_postal, 'siren': siren}))

# ***