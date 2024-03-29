# Generated by Django 5.0.1 on 2024-02-11 14:55

import django.db.models.deletion
import president.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballotName', models.CharField(max_length=50)),
                ('party', models.CharField(choices=[('Orange', 'Orange'), ('Independent', 'Independent'), ('Banana', 'Banana')], default='Independent', max_length=100)),
                ('seat', models.CharField(choices=[('MEN_REP', 'MenRep'), ('PRESIDENT', 'President'), ('SCHOOL_REP', 'SchoolRep'), ('WOMENS_REP', 'WomenRep')], max_length=200)),
                ('image', models.ImageField(upload_to=president.models.upload_location)),
                ('school', models.CharField(blank=True, choices=[('SED', 'SED'), ('SAFS', 'SAFS'), ('SPAS', 'SPAS'), ('SCI', 'SCI'), ('SBE', 'SBE'), ('SON', 'SON'), ('SEA', 'SEA')], max_length=200, null=True)),
                ('description', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
