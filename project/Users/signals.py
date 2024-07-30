# #add
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import User, History

# @receiver(post_save, sender=User)
# def create_user_history(sender, instance, created, **kwargs):
#     if created:
#         History.objects.create(user=instance)
# #add