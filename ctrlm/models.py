import sqlite3

from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Etab(models.Model):
    siret = models.CharField(primary_key=True, max_length=25)
    nom_commercial = models.CharField(max_length=32, null=True)
    voie = models.CharField(max_length=100, null=True)
    code_postal = models.CharField(max_length=5, null=True)
    commune = models.CharField(max_length=30, null=True)
    code_insee = models.CharField(max_length=5, null=True)
    siren = models.CharField(max_length=9)


    def __str__(self):
        return "siret: {}, siren: {}, code postal: {}".format(self.siret, self.siren, self.code_postal)


class Liste(models.Model):
    rae = models.CharField(primary_key=True, max_length=14)
    siren = models.CharField(max_length=9)
    statut_traitement = models.CharField(max_length=25, null=True)

    def __str__(self):
        return "rae: {}, siren: {}, statut: {}".format(self.rae, self.siren, self.statut_traitement)


class Pdl(models.Model):
    rae = models.CharField(primary_key=True, max_length=14)
    voie = models.CharField(max_length=100, null=True)
    code_postal = models.CharField(max_length=5, null=True)
    commune = models.CharField(max_length=30, null=True)
    code_insee = models.CharField(max_length=5, null=True)
    siren = models.CharField(max_length=5)

    def __str__(self):
        return "rae: {}, siren: {}, code postal: {}".format(self.rae, self.siren, self.code_postal)


# class RelationRaeSiret(models.Model):
#     id = models.AutoField(primary_key=True)
#     rae = models.CharField(primary_key=True, max_length=14)
#     siret = models.CharField(primary_key=True, max_length=25)
#     precision = models.IntegerField()

def setup_data():
    with sqlite3.connect("ctrlm.db") as conn:
        table_names = ('Pdl', 'Etab', 'Liste',)
        header_names = (
            ('rae', 'voie', 'code_postal', 'commune', 'code_insee', 'siren'),
            ('siret', 'nom_commercial', 'voie', 'code_postal', 'commune', 'code_insee', 'siren'),
            ('rae', 'siren', 'statut_traitement'),
        )

        for table_name, headers in zip(table_names, header_names):

            query = "SELECT {} FROM {}".format(','.join(headers), table_name)
            print('query:  ', query)
            result = conn.cursor().execute(query).fetchall()

            rec = eval('{}()'.format(table_name))
            for values in result:
                for field, value in zip(headers, values):
                    setattr(rec, field, value)
                rec.save()
