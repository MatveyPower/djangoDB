# Generated by Django 3.2 on 2021-04-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0003_alter_driver_have_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_area', models.CharField(max_length=20, verbose_name='Марка машины')),
            ],
            options={
                'verbose_name': ('Район',),
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_bid', models.CharField(max_length=20, verbose_name='Код заявки')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('time_bid', models.DateTimeField(auto_now=True, verbose_name='Время заявки')),
                ('landing_area', models.CharField(max_length=20, verbose_name='Район посадки')),
                ('end_landing_area', models.CharField(max_length=20, verbose_name='Район высадки')),
                ('status', models.BooleanField(verbose_name='Выполнен')),
            ],
            options={
                'verbose_name': ('Заявка',),
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_street', models.CharField(max_length=20, verbose_name='Марка машины')),
                ('code_street', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bid.bid')),
            ],
            options={
                'verbose_name': ('Улица',),
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bid.area')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.driver')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='code_area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bid.bid'),
        ),
    ]
