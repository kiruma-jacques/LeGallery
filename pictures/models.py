from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.CharField()
    description = models.TextField()
    location = models.ForeignKey(Pin)
    category = models.ForeignKey(Section)
    mboto = models.ImageField(upload_to='photo_storage/', blank=True)

    def __str__(self):
        return self.title

    def save_upload(self):
        self.save()

class Pin(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    def save_pin(self):
        self.save()

class Section(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    def save_section(self):
        self.save()
