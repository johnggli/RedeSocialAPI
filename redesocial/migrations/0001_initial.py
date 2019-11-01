# Generated by Django 2.0 on 2019-11-01 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='redesocial.Address')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='redesocial.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='redesocial.Post'),
        ),
    ]
