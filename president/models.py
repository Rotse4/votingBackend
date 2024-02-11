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

# class President(models.Model):
#     name = models.CharField(max_length=200)
#     party =models.CharField(max_length= 100,choices=parties, default="Independent")
#     # school=models.CharField(choice=parties)
#     # profile_pic =models.ImageField(upload_to=upload_location, null=False, blank=False)
#     votes = models.IntegerField(default=0)
#     # description=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name[0:50]
# class Voter(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     # vote=models.ForeignKey(Candidate, on_delete=models.DO_NOTHING)
#     voted= models.BooleanField(default=False)
#     regNo= models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
class Candidate(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    party =models.CharField(max_length= 100,choices=parties, default="Independent")
    seat = models.CharField(max_length=200)
    school =models.CharField(max_length=200, null=True,blank=True)
    description = models.TextField()
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.name + self.seat
    
    


