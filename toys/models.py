from django.db import models

class Toy(models.Model):
    toy_name = models.CharField('Toy Name', primary_key=True, max_length=200, null=False)
    toy_model = models.CharField('Toy Model', max_length=10, null=False)
    toy_price = models.CharField('Toy Price', max_length=10, null=False)
    toy_description = models.CharField('Toy Description', max_length=2000)
    
    def __str__(self):
        return self.toy_name
