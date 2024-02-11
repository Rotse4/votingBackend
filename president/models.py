from django.conf import settings
from django.db import models


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

def upload_location(instance, filename):
    file_path = 'images/{name_id}/{party}-{filename}'.format(
        name_id=str(instance.name.id),
        party=str(instance.party),
        filename=filename

    )
    return file_path
    
class Candidate(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    party =models.CharField(max_length= 100,choices=parties, default="Independent")
    seat = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    school =models.CharField(max_length=200, null=True,blank=True)
    description = models.TextField()
    votes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + ' ' + str(self.seat)
    
    


