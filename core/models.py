from django.db import models

# Create your models here.
class Students(models.Model):
    sid = models.CharField(max_length =100, unique = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    department = models.CharField(max_length = 100)
    batch = models.CharField(max_length = 100)
    image = models.ImageField(
        upload_to = 'student/images',
        blank = True,
        null = True
    )

    def __str__(self):
        return f"{self.sid} - {self.name}"