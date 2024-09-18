from django.core.management.base import BaseCommand
from Users.models import History, HistoryMy, HistoryCn, HistoryIn, HistoryKr, HistoryQa

class Command(BaseCommand):
    help = 'Populates country-specific history tables from the existing History table'

    def handle(self, *args, **kwargs):
        # Get all existing History records
        history_records = History.objects.all()

        for history in history_records:
            realhistoryid = history.id  # Use the existing History ID as realhistoryid
            description = history.description
            offensive = history.offensive
            status = history.status
            country = history.country.strip()

            # Populate the respective country-specific table based on the country field
            if country == 'Malaysia':
                HistoryMy.objects.update_or_create(
                    realhistoryid=realhistoryid,
                    defaults={'description': description, 'offensive': offensive, 'status': status}
                )
            elif country == 'China':
                HistoryCn.objects.update_or_create(
                    realhistoryid=realhistoryid,
                    defaults={'description': description, 'offensive': offensive, 'status': status}
                )
            elif country == 'India':
                HistoryIn.objects.update_or_create(
                    realhistoryid=realhistoryid,
                    defaults={'description': description, 'offensive': offensive, 'status': status}
                )
            elif country == 'South Korea':
                HistoryKr.objects.update_or_create(
                    realhistoryid=realhistoryid,
                    defaults={'description': description, 'offensive': offensive, 'status': status}
                )
            elif country == 'Qatar':
                HistoryQa.objects.update_or_create(
                    realhistoryid=realhistoryid,
                    defaults={'description': description, 'offensive': offensive, 'status': status}
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated country-specific history tables.'))
