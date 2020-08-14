from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=11, blank=True)
    points = models.IntegerField(default=0)

    #포인트를 올리는 함수.
    def get_points(self, points):
        self.points += points
        self.save()