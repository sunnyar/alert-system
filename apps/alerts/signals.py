from .models import Alert
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Alert)
def index_post(sender, instance, **kwargs):
    instance.indexing()