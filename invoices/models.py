from django.db import models

from storages.backends.s3 import S3File
from django.core.files.storage import storages # to specify a storage config

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from uuid import uuid4

"""
Model Helpers
"""

def get_invoice_s3_file_path(instance: "Invoice", filename: str):
    """generate a file path and keep file type"""
    print(f"{uuid4().hex}.{filename.split(".")[-1]}")
    return f"{uuid4().hex}.{filename.split(".")[-1]}"

"""
Invoice Model
"""

class Invoice(models.Model):
    cost_center = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)  

    file = models.FileField(
        max_length=100,
        storage=storages['invoices'],
        upload_to=get_invoice_s3_file_path,
    )
    
    def __str__(self):
        return f"Invoice no.{self.id}"
    
    def open(self) -> S3File:
        return self.file.open(self.file.name, mode="rb")
    
"""
Helper handlers
"""
   
@receiver(post_delete, sender=Invoice)
def delete_invoice_file(sender, instance, **kwargs):
    """Delte the file from s3 if Invoice-Object gets deleted"""
    if instance.file:
        instance.file.delete(save=False)

@receiver(pre_save, sender=Invoice)
def delete_old_file_on_update(sender, instance, **kwargs):
    """Deletes the old file from s3 if a new is uplaoded"""
    if not instance.pk:
        return  # New oject, do not delte
    
    try:
        old_instance = Invoice.objects.get(pk=instance.pk)
    except Invoice.DoesNotExist:
        return
    
    if old_instance.file and old_instance.file != instance.file:
        old_instance.file.delete(save=False)