from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from . models import UserOptions, UserHiddenAttributes

USER_MODEL = get_user_model()

@receiver(post_save, sender=USER_MODEL)
def create_user_attributes(sender, instance, created, **kwargs):
	if created:
		UserHiddenAttributes.objects.create(user=instance)

@receiver(post_save, sender=USER_MODEL)
def create_user_options(sender, instance, created, **kwargs):
	if created:
		UserOptions.objects.create(user=instance)