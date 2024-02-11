# Generated by Django 4.2.5 on 2024-02-11 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('president', '0005_alter_candidate_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.CharField(choices=[('Banana', 'Banana'), ('Orange', 'Orange'), ('Independent', 'Independent')], default='Independent', max_length=100),
        ),
        migrations.DeleteModel(
            name='Voter',
        ),
    ]
