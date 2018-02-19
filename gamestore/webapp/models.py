from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    developer = models.BooleanField(default=False) #false = player, True=developer
    games = models.ManyToManyField('Game', related_name='+')

    def __unicode__(self):
        return str(self.user.username) #How viewed in django admin, same as __str__ in python2
    def __str__(self):
        return self.user.username #These still needed, don't know why

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# Setting the name and description of the game. All the names are unique, and primary key (game id, referenced pk) is created automatically by django.
# States - don't know what this does? Was in the project plan.
# Added a developer field - foreign key reference to one User (will need to create the user model) that also needs to be a developer. When the user (developer) is deleted, this field is set to NULL (instead of deleting the game). Can also be an admin/platform owner this point, and game would be free?
# Highcores defined as a ManyToMany - relationship (a game has several highscores from different players (always player's highest score)). No need for a seperate model, since highscores referenced with players_highscores from the User model.
class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=250)
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2) #Changed the float to decimal due to rounding issues
    developer = models.ForeignKey('Profile', related_name='developed_games', default='request.user', null=True, on_delete=models.SET_NULL)
#    highscores = models.ManyToManyField('Profile', related_name='highscores', related_query_name='scores')

    pubDate = models.DateTimeField(auto_now_add=True)
    CATEGORY_CHOICES = (
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('PUZZLE', 'Puzzle'),
        ('SPORTS', 'Sports'),
        ('EDUCATIONAL', 'Educational'),
        ('UNDEFINED', 'Undefined')
    )
    category = models.CharField(max_length=12,choices=CATEGORY_CHOICES, default='UNDEFINED')
#   img = models.URLField(default="http://www.google.com") ##Game logo to be displayed
    #category = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse("developer:developedgame", kwargs={'pk': self.pk})

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return self.name
    def to_json_dict(self, user=None):
        result = {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'url': self.url,
            'price': self.price,
            # 'developer': self.developer.user.username,
            #'category': self.category.name,
            #'category_id': self.category.id,
        }

        # Check user ownership of game
        if user is not None and isinstance(user, User) and user.is_authenticated():
            owned = False
            o = user.profile.games.filter(id=self.id)
            if o.count() > 0:
                result['owned'] = True
            else:
                result['owned'] = False

        return result


# class Category(models.Model):
#     name = models.CharField(max_length=30, unique= True)
#     id = models.AutoField(primary_key=True)

#     def to_json_dict(self):
#         result = {
#             'name': self.name,
#             'id': self.id
#         }
#         return result
#     def __str__(self):
#         return str(self.name)

class Order(models.Model):
    # Order Id
    id = models.AutoField(primary_key=True)
    # Buyer
    player = models.ForeignKey('Profile', null=False, on_delete=models.DO_NOTHING,)
    # Order content
    games = models.ManyToManyField('Game', default=None, blank=True)
    # Total sum of the order
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Order date and time
    orderDate = models.DateTimeField(default=timezone.now, null=False)
    # Payment reference
    paymentReference = models.IntegerField(null=True, default=0)
    # Payment date and time
    paymentDate = models.DateTimeField(default=None, null=True)
    # Order status
    status = models.CharField(max_length=10, null=False, default="pending")

    def __str__(self):
        return str(self.id)

class GameState(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True, default=0) #needs to be changed to highscore, since gamestate also saves score
    state = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.game)
