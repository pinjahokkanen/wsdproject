from django.test import TestCase
from django.db import models
from .models import Profile, Game
import sys
# Create your tests here.

class M2MThroughTest(TestCase):
    def setUp(self):
        self.k1 = Profile.objects.create('k1', 'k1@k.com','kayttajansalasana1')
        self.k2 = Profile.objects.create('k2', 'k2@k.com','kayttajansalasana2')
        self.k3 = Profile.objects.create('k3', 'k3@k.com','kayttajansalasana3')

        self.peli1 = Game.objects.create(name='p1')
        self.peli2 = Game.objects.create(name='p2')
        self.peli3 = Game.objects.create(name='p3')

    def gamesAreAdded(self):
        k1.games.add(peli1)
        k1.games.add(peli3)
        k2.games.add(peli2)

#        self.assertEqual(k1.games.all(), 'There should be the games peli1 & peli3')
#        self.assertEqual(k2.games.all(), 'There should be the game peli2')
#        self.assertEqual(k3.games.all(), 'There should be no games')
