# Generated by Django 2.2.5 on 2019-11-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=150)),
                ('last_name', models.CharField(db_index=True, max_length=150)),
                ('phone_number', models.CharField(db_index=True, max_length=150)),
                ('email_address', models.CharField(db_index=True, max_length=150)),
                ('street_address', models.CharField(db_index=True, max_length=350)),
            ],
        ),
    ]