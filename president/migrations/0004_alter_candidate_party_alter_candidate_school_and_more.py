# Generated by Django 4.2.5 on 2024-02-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0003_alter_candidate_party_alter_candidate_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.CharField(choices=[('Independent', 'Independent'), ('Orange', 'Orange'), ('Banana', 'Banana')], default='Independent', max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='school',
            field=models.CharField(blank=True, choices=[('SPAS', 'SPAS'), ('SBE', 'SBE'), ('SAFS', 'SAFS'), ('SEA', 'SEA'), ('SON', 'SON'), ('SCI', 'SCI'), ('SED', 'SED')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='seat',
            field=models.CharField(choices=[('SCHOOL_REP', 'SchoolRep'), ('PRESIDENT', 'President'), ('WOMENS_REP', 'WomenRep')], max_length=200),
        ),
    ]