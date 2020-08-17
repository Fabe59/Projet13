# Generated by Django 3.1 on 2020-08-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddAccomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addAccomodation_name', models.CharField(max_length=128, verbose_name='Nom')),
                ('addAccomodation_category', models.CharField(choices=[('hotel', 'Hotel'), ('gite', 'Gite'), ('bnb', 'BnB')], max_length=16, verbose_name='Catégorie')),
                ('addAccomodation_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Numéro')),
                ('addAccomodation_road', models.CharField(max_length=250, verbose_name='Adresse')),
                ('addAccomodation_zipcode', models.PositiveIntegerField(verbose_name='Code Postal')),
                ('addAccomodation_city', models.CharField(max_length=50, verbose_name='Ville')),
                ('addAccomodation_phone', models.BigIntegerField(verbose_name='Téléphone')),
                ('addAccomodation_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('addAccomodation_url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('addAccomodation_parking', models.CharField(choices=[('garage', 'Garage'), ('couvert', 'Couvert'), ('ferme', 'Fermé')], max_length=16, verbose_name='Type de parking')),
                ('addAccomodation_statut', models.CharField(choices=[('Non_lu', 'Non lu'), ('Lu', 'Lu'), ('Archive', 'Archivé')], default='Non_lu', max_length=16, verbose_name='Statut de la demande')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=200)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('road', models.CharField(max_length=250)),
                ('zipcode', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accomodation.category')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accomodation.parking')),
            ],
        ),
    ]
