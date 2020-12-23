# Generated by Django 3.1.4 on 2020-12-23 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('production_date', models.DateTimeField(auto_now_add=True)),
                ('model', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('gear_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=245)),
                ('last_name', models.CharField(max_length=245)),
                ('email', models.CharField(max_length=45)),
                ('phone_num', models.IntegerField()),
                ('password', models.CharField(max_length=245)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('days', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_app.car')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='users_rent',
            field=models.ManyToManyField(through='rent_app.Rental', to='rent_app.User'),
        ),
    ]
