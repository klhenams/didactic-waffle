# Generated by Django 4.0.8 on 2022-12-27 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addressbooks', '0002_remove_contact_email_remove_contact_msisdn_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together={('contact', 'email')},
        ),
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together={('contact', 'phone_number')},
        ),
    ]
