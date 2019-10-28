# Generated by Django 2.2.6 on 2019-10-28 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sportsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('about', models.TextField()),
                ('sportsman', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='sport.Sportsman')),
            ],
        ),
        migrations.CreateModel(
            name='KindOfSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('Street Workout', 'Street Workout'), ('Athletics', 'Athletics'), ('Power Lifting', 'Power Lifting'), ('ESports', 'ESports')], max_length=20)),
                ('sportsmen', models.ManyToManyField(related_name='kinds_of_sport', to='sport.Sportsman')),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_name', models.CharField(max_length=20)),
                ('size', models.CharField(choices=[('Big', 'Big'), ('Medium', 'Medium'), ('Small', 'Small')], max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sportsman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gyms', to='sport.Sportsman')),
            ],
        ),
    ]