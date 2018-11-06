# Generated by Django 2.1.3 on 2018-11-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='类别名称')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.CharField(max_length=240, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='标签名称')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogspost',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogspost',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='blogspost',
            name='author',
            field=models.CharField(max_length=16, null=True, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='blogspost',
            name='content',
            field=models.TextField(null=True, verbose_name='博客正文'),
        ),
        migrations.AddField(
            model_name='blogspost',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='title',
            field=models.CharField(max_length=32, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogsPost', verbose_name='博客'),
        ),
        migrations.AddField(
            model_name='blogspost',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Catagory', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blogspost',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]
