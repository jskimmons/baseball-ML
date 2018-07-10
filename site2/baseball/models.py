from django.db import models

# Create your models here.

class Game(models.Model):

    date = models.CharField(max_length = 200)

    t1_name = models.CharField(max_length = 10)
    t2_name = models.CharField(max_length = 10)

    t1_batAvg = models.FloatField()
    t2_batAvg = models.FloatField()

    t1_OBP = models.FloatField()
    t2_OBP = models.FloatField()

    t1_OPS = models.FloatField()
    t2_OPS = models.FloatField()

    t1_slug = models.FloatField()
    t2_slug = models.FloatField()

    t1_ERA = models.FloatField()
    t2_ERA = models.FloatField()

    t1_winner = models.IntegerField()


    def __str__(self):

        return "{} vs {} on {}".format(self.t1_name, self.t2_name, self.date)

#    class Meta:
#        
#        ordering = ['date']
#
#    class Admin:
#        
#        pass
