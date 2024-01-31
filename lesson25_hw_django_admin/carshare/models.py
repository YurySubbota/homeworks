from django.db import models


# Create your models here.

class Auto(models.Model):
    CHOICES = (
        ('FR', 'FREE'),
        ('US', 'INUSE'),
        ('SE', 'SERVICE')
    )
    vin_code = models.CharField(max_length=255)
    status = models.CharField(choices=CHOICES, max_length=255)
    auto_model = models.ForeignKey('AutoModel', max_length=255, on_delete=models.CASCADE)
    user = models.ForeignKey('AutoUser', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.vin_code[:3:]}***'

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'


class AutoUser(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.phone}'


class AutoBrand(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    brand = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.brand}'


class AutoModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
