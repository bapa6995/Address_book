# Generated by Django 2.2.5 on 2019-11-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20191107_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontacts',
            name='email_address',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='last_name',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=150),
        ),
    ]
