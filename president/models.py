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

seats = {
    ("PRESIDENT", "President"),
    ("SCHOOL_REP", "SchoolRep"),
    ("WOMENS_REP","WomenRep"),
    ("MEN_REP","MenRep"),
    
}

def upload_location(instance, filename):
    file_path = 'images/{account_id}/{party}-{filename}'.format(
        account_id=str(instance.account.id),
        party=str(instance.party),
        filename=filename

    )
    return file_path
    
class Candidate(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ballotName = models.CharField(max_length=50)
    party =models.CharField(max_length= 100,choices=parties, default="Independent")
    seat = models.CharField(max_length=200, choices=seats)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    school =models.CharField(max_length=200,choices=schools, null=True,blank=True)
    description = models.TextField()
    votes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.ballotName) + ' ' + str(self.seat)
    
    


