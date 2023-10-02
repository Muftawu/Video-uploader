from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"{self.name}-{self.file}"