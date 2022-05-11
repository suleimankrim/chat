from django.db import models
from client.models import User
import random

# Create your models here.
class CodeModel(models.Model):
    number = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        number_list=[x for x in range(10)]
        code_item=[]
        for i in range(5):
            num = random.choice(number_list)
            code_item.append(num)
            self.number=''.join(str(x) for x in code_item)
        super().save(*args, **kwargs)
