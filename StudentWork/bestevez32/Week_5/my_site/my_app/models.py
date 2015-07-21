from django.db import models


# Create your models here.


class Character(models.Model):
    character_name=models.CharField(max_length=50, default="Enter next name here")
    agility_score=models.IntegerField()
    smarts_score=models.IntegerField()
    strength_score=models.IntegerField()
    spirit_score=models.IntegerField()
    vigor_score=models.IntegerField()

    def __str__(self):
        return str(self.character_name) + " \nAgility:"+ str(self.agility_score) + " Smarts:" + str(self.smarts_score) + " Strength:" + str(self.strength_score) + \
               " Spirit:" + str(self.spirit_score) + " Vigor:" + str(self.vigor_score)


    def __unicode__(self):
        return str(self.character_name) + " \nAgility:"+ str(self.agility_score) + " Smarts:" + str(self.smarts_score) + " Strength:" + str(self.strength_score) + \
               " Spirit:" + str(self.spirit_score) + " Vigor:" + str(self.vigor_score)









