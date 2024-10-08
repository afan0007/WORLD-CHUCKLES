# Generated by Django 5.0.6 on 2024-09-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_wordfrequency'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryCn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realhistoryid', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('offensive', models.BooleanField(default=None, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default='CN', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realhistoryid', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('offensive', models.BooleanField(default=None, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default='IN', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryKr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realhistoryid', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('offensive', models.BooleanField(default=None, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default='KR', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryMy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realhistoryid', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('offensive', models.BooleanField(default=None, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default='MY', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryQa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realhistoryid', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('offensive', models.BooleanField(default=None, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default='QA', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
