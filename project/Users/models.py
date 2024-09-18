from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

COUNTRY_CHOICES = [
        ('MY', 'Malaysia'),
        ('IN', 'India'),
        ('CN', 'China'),
        ('KR', 'South Korea'),
        ('QA', 'Qatar'),
    ]

GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Prefer not to say'),
    ]
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=7, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, null=False, blank=False)
    age = models.PositiveIntegerField()
    # after sigining up then only allow changing
    profile_image = models.ImageField(upload_to='images/', default='images/profilepic.jpg')
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    
    
    def __str__(self):
        return self.username


#history table 
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default='No description')
    keyword = models.CharField(max_length=100, default='No keyword')
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, null=False, blank=False) #new add
    offensive = models.BooleanField(null=True, default=None) #new add
    status = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"History for {self.user.username}"
    
# Base History table that other models will inherit from
class BaseHistory(models.Model):
    realhistoryid = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=500, default='No description')
    offensive = models.BooleanField(null=True, default=None) 
    status = models.PositiveIntegerField(default=0)
    
    class Meta:
        abstract = True  # This will not create a table

    def __str__(self):
        return f"History for {self.user.username}"

# Specific history tables for each country
class HistoryMy(BaseHistory):
    country = models.CharField(max_length=20, default='MY')

class HistoryCn(BaseHistory):
    country = models.CharField(max_length=20, default='CN')

class HistoryIn(BaseHistory):
    country = models.CharField(max_length=20, default='IN')

class HistoryKr(BaseHistory):
    country = models.CharField(max_length=20, default='KR')

class HistoryQa(BaseHistory):
    country = models.CharField(max_length=20, default='QA')

COUNTRY_MAPPING = {
    'Malaysia': 'MY',
    'China': 'CN',
    'India': 'IN',
    'South Korea': 'KR',
    'Qatar': 'QA',
}

@receiver(post_save, sender=History)
def create_or_update_country_specific_history(sender, instance, **kwargs):
    """
    Post-save signal to handle creation or updating of country-specific history tables
    using realhistoryid as the identifier.
    """
    country = COUNTRY_MAPPING.get(instance.country.strip())
    realhistoryid = instance.id  # Using History's ID as the realhistoryid
    description = instance.description
    offensive = instance.offensive
    status = instance.status
    user_country = instance.user.country 

    # Depending on the country, create or update the corresponding history record
    if country == user_country:
        if country == 'MY':
            history_record, created = HistoryMy.objects.get_or_create(
                realhistoryid=realhistoryid,
                defaults={'description': description, 'offensive': offensive, 'status': status}
            )
            if not created:
                history_record.description = description
                history_record.offensive = offensive
                history_record.status = status
                history_record.save()
        
        elif country == 'CN':
            history_record, created = HistoryCn.objects.get_or_create(
                realhistoryid=realhistoryid,
                defaults={'description': description, 'offensive': offensive, 'status': status}
            )
            if not created:
                history_record.description = description
                history_record.offensive = offensive
                history_record.status = status
                history_record.save()

        elif country == 'IN':
            history_record, created = HistoryIn.objects.get_or_create(
                realhistoryid=realhistoryid,
                defaults={'description': description, 'offensive': offensive, 'status': status}
            )
            if not created:
                history_record.description = description
                history_record.offensive = offensive
                history_record.status = status
                history_record.save()

        elif country == 'KR':
            history_record, created = HistoryKr.objects.get_or_create(
                realhistoryid=realhistoryid,
                defaults={'description': description, 'offensive': offensive, 'status': status}
            )
            if not created:
                history_record.description = description
                history_record.offensive = offensive
                history_record.status = status
                history_record.save()

        elif country == 'QA':
            history_record, created = HistoryQa.objects.get_or_create(
                realhistoryid=realhistoryid,
                defaults={'description': description, 'offensive': offensive, 'status': status}
            )
            if not created: #already exists
                history_record.description = description
                history_record.offensive = offensive
                history_record.status = status
                history_record.save()


class WordFrequency(models.Model):
    word = models.CharField(max_length=100, unique=True)
    frequency = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.word}: {self.frequency}"
    
@receiver(post_save, sender=History)
def update_word_frequency_on_save(sender, instance, **kwargs):
    # Split the description into words
    words = instance.description.lower().split()

    # Update the frequency of each word in WordFrequency table
    for word in words:
        if word:  # Ensure word is not an empty string
            word_freq, created = WordFrequency.objects.get_or_create(word=word)
            if not created:
                word_freq.frequency += 1
            else:
                word_freq.frequency = 1
            word_freq.save()


@receiver(post_delete, sender=History)
def update_word_frequency_on_delete(sender, instance, **kwargs):
    # Split the description into words
    words = instance.description.lower().split()

    # Decrease the frequency of each word in WordFrequency table
    for word in words:
        if word:  # Ensure word is not an empty string
            try:
                word_freq = WordFrequency.objects.get(word=word)
                if word_freq.frequency > 1:
                    word_freq.frequency -= 1
                    word_freq.save()
                else:
                    word_freq.delete()  # Remove entry if frequency would be zero
            except WordFrequency.DoesNotExist:
                pass  # No action needed if the word does not exist in the table