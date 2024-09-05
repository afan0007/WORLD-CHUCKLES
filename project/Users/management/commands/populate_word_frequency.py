from django.core.management.base import BaseCommand
from Users.models import History, WordFrequency

class Command(BaseCommand):
    help = 'Populates the WordFrequency table based on existing History records'

    def handle(self, *args, **kwargs):
        # Clear existing word frequencies
        WordFrequency.objects.all().delete()

        # Calculate word frequencies from History records
        histories = History.objects.all()

        word_count = {}
        for history in histories:
            words = history.description.lower().split()
            for word in words:
                if word:  # Ignore empty strings
                    word_count[word] = word_count.get(word, 0) + 1

        # Save the calculated word frequencies to the WordFrequency table
        for word, count in word_count.items():
            WordFrequency.objects.create(word=word, frequency=count)

        self.stdout.write(self.style.SUCCESS('Successfully populated WordFrequency table!'))
