from django.test import TestCase
import _sqlite3

# Create your tests here.
from ctrlm.models import Pdl, Liste, Etab


class TestPdl(TestCase):

    def setUp(self):
        # a = Pdl()
        # for(attr in head ):
        #
        # print('a:    ', a)
        #

        pass

    def test_pdl_count(self):
        count = Pdl.objects.count()
        print("count of PDL: ", count)
        self.assertGreater(count, 1, "au moins un object  dans  la  base")

    def test_etab_count(self):
        count = Etab.objects.count()
        print("count of Etab: ", count)
        self.assertGreater(count, 1, "au moins un object  dans  la  base")

    def test_liste_count(self):
        count = Liste.objects.count()
        print("count of Liste: ", count)
        self.assertGreater(count, 1, "au moins un object  dans  la  base")