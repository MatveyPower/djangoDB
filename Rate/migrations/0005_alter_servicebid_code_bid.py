# Generated by Django 3.2 on 2021-04-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0002_auto_20210415_2035'),
        ('Rate', '0004_rename_tarif_taximetertarif_tarif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebid',
            name='code_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bid.bid'),
        ),
    ]