import uuid

from django.db import models


def upload_certificate(instance, filename):
    return f"certificates/{uuid.uuid4()}/{filename}"


class Memory(models.Model):
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True, blank=True)
    # date = models.DateField(null=True, blank=True, input_formats=["%Y-%m-%d"])
    date = models.DateTimeField(null=True, blank=True, default='Once upon a time...')
    certificate = models.ImageField(upload_to=upload_certificate, null=True)

    def __str__(self):
        return self.title
