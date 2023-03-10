from django.db import models

class BaseModel(models.Model):
    
    created_on= models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True
    )

    class Meta:
        abstract = True