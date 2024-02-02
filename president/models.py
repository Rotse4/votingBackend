from django.db import models
from django.contrib.auth.models import User

# Create your models here.

parties = {
    ("Orange", "Orange"),
    ("Banana", "Banana"),
    ("Independent","Independent")
}

schools = {
    ("SCI", "SCI"),
    ("SBE", "SBE"),
    ("SED","SED"),
    ("SPAS","SPAS"),
    ("SON", "SON"),
    ("SEA","SEA"),
    ("SAFS","SAFS"),

}

class President(models.Model):
    name = models.CharField(max_length=200)
    party =models.CharField(max_length= 100,choices=parties, default="Independent")
    # school=models.CharField(choice=parties)
    # profile_pic =models.ImageField(upload_to=upload_location, null=False, blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name[0:50]
    

