# -*- coding: utf-8 -*-
import sqlite3,sys

___DB_CTRLM_PATH___ = "../data/ctrlm.db"
def read(table_name, field = '*' , where = ""):
    with sqlite3.connect (___DB_CTRLM_PATH___) as conn:
        cur = conn.cursor()
        req = "SELECT {} FROM {} ".format(field, table_name)
        if(where != ""):
            req += "WHERE {}".format(where)
            print(req)
            
        result = cur.execute(req)
        return result.fetchall()

def readMinus(table_name1, table_name2, field = '*'):
    with sqlite3.connect (___DB_CTRLM_PATH___) as conn:
        cur = conn.cursor()
        req = "SELECT {} FROM {}".format(field, table_name1)
        req += " EXCEPT SELECT {} FROM {}".format(field, table_name2)
        result = cur.execute(req)
        return result.fetchall()


def readMinusDistinct(table_name1, table_name2, field = '*'):
    with sqlite3.connect (___DB_CTRLM_PATH___) as conn:
        cur = conn.cursor()
        req = "SELECT DISTINCT {} FROM {}".format(field, table_name1)
        req += " EXCEPT SELECT DISTINCT {} FROM {}".format(field, table_name2)
        print("req : " + req)

        result = cur.execute(req)
        return result.fetchall()


def dict_totuples(dic):
    db_headers = ()
    db_values = ()
    for key, value in dic.items():
        db_headers  = db_headers + (key,)
        db_values = db_values + (value,)

    return db_headers, db_values


def write(table_name, tpl_entetes, tpl_values):
    with sqlite3.connect (___DB_CTRLM_PATH___) as conn:
        cur = conn.cursor()
        req = """
                INSERT INTO {}
                {}
                VALUES{}
              """.format(table_name,  tpl_entetes, tpl_values) 
        cur.execute(req)
        conn.commit()

def write2(table_name, dic_record):
    db_headers,  db_values = dict_totuples(dic_record)
    try:
        write(table_name, db_headers, db_values)
    except:
        print("Unexpected error:", sys.exc_info())


def update(table_name,  valuesdict, where):
    with sqlite3.connect (___DB_CTRLM_PATH___) as conn:
        cur = conn.cursor()
        req = "UPDATE {} SET {} WHERE {}".format(table_name,  valuesdict, where) 
        # print(req)
        cur.execute(req)
        conn.commit()
        
def copieCsvpdl(filename):           
    header = ("rae","voie","code_postal","commune","code_insee","siren" )
    with open(filename) as file:
        row_infos = file.readline().strip()
        
        while(len(row_infos)>0):
            try:
                listInfos = row_infos.split(";")
                tpl_infos =(listInfos[1],listInfos[2],listInfos[3],listInfos[4],listInfos[6],listInfos[0])
                write("pdl", header , tpl_infos)
                row_infos = file.readline().strip()
            except:
                pass
        print("terminé")
        
    
def copieCsvSiret():           
    header = ("siret","voie","code_postal","commune","code_insee","siren" )
    with open("C:\\Users\\c21373\\Documents\\___Projets\\Ctrlm@\\ctrlm@siren\\model\\data\\T_1") as file:
        row_infos = file.readline().strip()
        
        while(len(row_infos)>0):
            try:
                listInfos = row_infos.split(";")
                tpl_infos =(listInfos[1],listInfos[2],listInfos[3],listInfos[4],listInfos[6],listInfos[0])
                write("pdl", header , tpl_infos)
                row_infos = file.readline().strip()
            except:
                pass
        print("terminé")
        
       
        
def copieListe():
    header = ("siren","rae", "statut_traitement" )
    with open('//atlas.edf.fr/in/dc-75sms/C21373/CTRL@M/ctrlm@siret/data/Saur_Siren_mino.csv') as file:
        row_infos = file.readline().strip()
        while(True):
            row_infos = file.readline().strip()     
            # print(row_infos)
            if (len(row_infos) == 0):
                break
            try:
                # print(row_infos)
                listInfos = row_infos.split(";")
                tpl_infos =(listInfos[0],listInfos[1],"non")
                write("liste", header , tpl_infos)
            except:
                # print("pass")
                pass           
        
        print("terminé")  