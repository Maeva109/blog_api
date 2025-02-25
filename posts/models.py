from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre