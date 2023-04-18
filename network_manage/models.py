from django.db import models


class PC(models.Model):
    name = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)
    is_on = models.BooleanField(default=False)

    def __str__(self):
        return self.name


