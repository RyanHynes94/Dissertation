from django.db import models

# Create your models here.

class Dataset(models.Model):
    
    Season = models.DateField(("Season"), max_length=255)
    Player = models.CharField(("Player"), max_length=255)
    Liga_Goals = models.IntegerField(("Liga_Goals"))
    Liga_Asts = models.IntegerField(("Liga_Asts"))
    Liga_Aps = models.IntegerField(("Liga_Aps"))
    Liga_Mins = models.IntegerField(("Liga_Mins"))
    Cl_Goals = models.IntegerField(("CL_Goals"))
    Cl_Asts = models.IntegerField(("CL_Asts"))
    Cl_Aps = models.IntegerField(("CL_Aps"))
    Cl_Mins = models.IntegerField(("CL_Mins"))






