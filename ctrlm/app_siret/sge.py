# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 01:51:12 2020

@author: C21373
"""
from webcontroller.ie import IExplore
import models
import sys

URL_SGE_ROOT = "https://sge.enedis.fr"
URL_PDL = "/sgePortail/appmanager/portail/bureau?_nfpb=true&_windowLabel=portlet_gestion_pdl_2&portlet_gestion_pdl_2_actionOverride=%2Fportlets%2FgestionPdl%2FconsulterPdm&portlet_gestion_pdl_2idPdm=[PDL]&_pageLabel=sge_page_accueil"


def readPdl(rae):
    ie= IExplore("Système de Gestion des Echanges")
    if ie == None:
        print(" Echèc  control internet explorer")
    ie.load(URL_SGE_ROOT + URL_PDL.replace('[PDL]',"{:>014}".format(rae)))

    try:
        tpl_rae = ((ie.getdocument().all("prmId").value), 
                    (ie.getdocument().all("voie").value),
                    (ie.getdocument().all("codePostal").value),
                    (ie.getdocument().all("commune").value),
                    (ie.getdocument().all("codeINSEE").value)
                )                   
    except:
        if (ie.getwebbrowser().locationUrl == URL_SGE_ROOT + URL_PDL.replace('[PDL]',rae)):
            tpl_rae =(rae, "pdl inexistant", "", "", "", )
        else:
            tpl_rae = ()
            print("erreur sur le pdl: " , rae )
    
    return tpl_rae

todolist = models.readMinus("liste", "pdl", 'rae,siren')
print(len(todolist))


for tpl_row in todolist:
    tpl_rae = readPdl(tpl_row[0])
    tpl_raesiren = tpl_rae + (tpl_row[1],)
    
    header = ("rae","voie","code_postal","commune","code_insee","siren" )
    if len(tpl_raesiren)  == len(header):
       try:
           models.write("pdl", header, tpl_raesiren)
       except:
           print("Unexpected error:", sys.exc_info())        
               
    
    print(tpl_raesiren)
