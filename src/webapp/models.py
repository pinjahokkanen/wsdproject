from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Setting the name and description of the game. All the names are unique, and primary key (game id, referenced pk) is created automatically by django.
# States - don't know what this does? Was in the project plan.
# Added a developer field - foreign key reference to one User (will need to create the user model) that also needs to be a developer. When the user (developer) is deleted, this field is set to NULL (instead of deleting the game). Can also be an admin/platform owner this point, and game would be free?
# Highcores defined as a ManyToMany - relationship (a game has several highscores from different players (always player's highest score)). No need for a seperate model, since highscores referenced with players_highscores from the User model.
class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    states = models.IntegerField() #WHAT IS THIS?!?!?!?!
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2) #Changed the float to decimal due to rounding issues
    developer = models.ForeignKey('Profile', related_name='developed_games', null=True, on_delete=models.SET_NULL)
    highscores = models.ManyToManyField('Profile', related_name='highscores', related_query_name='scores')
