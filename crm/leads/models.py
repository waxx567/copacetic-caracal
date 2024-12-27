from django.db import models

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('Phone', 'Phone'),
        ('Website', 'Website'),
        ('Google', 'Google'),
        ('Facebook', 'Facebook'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True) # blank=True means that the field is not required
    special_files = models.FileField(blank=True, null=True) # null=True means that the field can be empty