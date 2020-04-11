# Generated by Django 2.1 on 2020-04-11 07:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=20)),
                ('blog_content', models.TextField()),
                ('blog_summary', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
            ],
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TagInfo'),
        ),
    ]
