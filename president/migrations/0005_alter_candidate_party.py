# Generated by Django 4.2.2 on 2024-02-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0004_alter_candidate_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.CharField(choices=[('Orange', 'Orange'), ('Independent', 'Independent'), ('Banana', 'Banana')], default='Independent', max_length=100),
        ),
    ]
