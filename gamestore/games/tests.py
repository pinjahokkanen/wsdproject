from django.test import TestCase
from webapp.models import Profile, Game, Order
from django.contrib.auth.models import User

class ModelsTest(TestCase):

    def testStore(self):
        testUser = User.objects.create(username="testperson", password="qwerty", email="test@try.com")
        testperson = Profile.objects.create(user=testUser)

        testGame = Game.objects.create(name="Awesome Game", description="None", url="http://www.gameon.com", price=5, img="http://www.yourimage.com", category="action", developer=testperson)

        testperson.games.add(testGame)

        self.assertEqual(testperson.get(pk=testGame.pk), testGame)
        self.assertEqual(testGame.name, "Awesome Game")
        self.assertEqual(testGame.description, "None")
        self.assertEqual(testGame.url, "http://www.gameon.com")
        self.assertEqual(testGame.price, 5)
        self.assertEqual(testGame.logo, "http://www.yourimage.com")
        self.assertEqual(testGame.category, "action")
        self.assertEqual(testGame.developer, testperson)

    def testOrder(self):

        testUser = User.objects.create(username="testperson", password="qwerty", email="test@try.com")
        testperson = Profile.objects.create(user=testUser)

        testGame  = Game.objects.create(name="Awesome Game", description="None", url="http://www.gameon.com", price=5, img="http://www.yourimage.com", category="action", developer=testperson)
        testGame2 = Game.objects.create(name="Awesome Game 2", description="None", url="http://www.gameon.com", price=5, img="http://www.yourimage.com", category="action", developer=testperson)


        testOrder = Order.objects.create(player=testperson, status="success", paymentRef=1337)
        testOrder.games.add(testGame)
        testOrder.games.add(testGame2)

        for game in testOrder.games.all():
            testOrder.total += game.price

        self.assertEqual(testOrder.games.get(pk=testGame.pk), testGame)
        self.assertEqual(testOrder.player, testperson)
        self.assertEqual(testOrder.paymentRef, 1337)
        self.assertEqual(testOrder.status, "success")

        testOrder.games.remove(testGame)
        ordergames = testOrder.all()
        self.assertEqual(ordergames.count(), 1)

