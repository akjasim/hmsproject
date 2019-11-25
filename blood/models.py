from django.db import models

# Create your models here.


class Blood(models.Model):
    group = models.CharField(max_length=10)
    availability = models.IntegerField(help_text="Specify in bottles.")

    def __str__(self):
        return self.group
