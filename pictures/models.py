from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey('pin')
    category = models.ForeignKey('section')
    mboto = models.ImageField(upload_to='upload_storage/', blank=True)

    def __str__(self):
        return self.title

    def save_upload(self):
        self.save()

class pin (models.Model):
    pin_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.pin_name

    def save_pin(self):
        self.save()

class Section(models.Model):
    section_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.section_name

    def save_section(self):
        self.save()
