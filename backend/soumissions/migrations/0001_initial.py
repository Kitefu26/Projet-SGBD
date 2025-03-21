# Generated by Django 5.1.7 on 2025-03-20 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='sujets/')),
            ],
        ),
        migrations.CreateModel(
            name='SujetExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='sujets_examen/')),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('fichier', models.FileField(upload_to='exercices/')),
                ('date_depot', models.DateTimeField(auto_now_add=True)),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModeleCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier_correction', models.FileField(upload_to='modeles_correction/')),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('commentaires', models.TextField(blank=True)),
                ('correcteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeles_correcteur_corrections', to=settings.AUTH_USER_MODEL)),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeles_correction', to='soumissions.exercice')),
            ],
        ),
        migrations.CreateModel(
            name='Soumission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier_soumission', models.FileField(upload_to='soumissions/')),
                ('fichier_chiffre', models.BinaryField(blank=True, null=True)),
                ('date_soumission', models.DateTimeField(auto_now_add=True)),
                ('note', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('commentaire', models.TextField(blank=True)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soumissions', to=settings.AUTH_USER_MODEL)),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soumissions', to='soumissions.exercice')),
            ],
        ),
        migrations.CreateModel(
            name='Plagiat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_plagiat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('details', models.TextField(blank=True)),
                ('soumission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plagiats', to='soumissions.soumission')),
            ],
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('feedback', models.TextField(blank=True)),
                ('date_correction', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('validé', 'Validé'), ('à réviser', 'À réviser')], max_length=20)),
                ('correcteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corrections', to=settings.AUTH_USER_MODEL)),
                ('soumission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corrections', to='soumissions.soumission')),
            ],
        ),
    ]
