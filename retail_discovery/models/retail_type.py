from django.db import models

from retail_discovery.models.base import BaseModel


class RetailType(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "RetailType"
        ordering = ['-created_at']
