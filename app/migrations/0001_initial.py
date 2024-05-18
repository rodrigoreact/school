# Generated by Django 4.2 on 2024-05-17 19:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(default=django.utils.timezone.now)),
                ('modificacion_registro', models.DateField(blank=True, null=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('creacion_registro', models.DateField(default=django.utils.timezone.now)),
                ('modificacion_registro', models.DateField(blank=True, null=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('dpto', models.CharField(blank=True, max_length=10, null=True)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='CursoProfesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(through='app.CursoProfesor', to='app.profesor'),
        ),
    ]