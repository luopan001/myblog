from django.db import models

class Catagory(models.Model):
    '''
    博客分类
    '''
    name =  models.CharField('类别名称',max_length = 150)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    博客标签
    '''
    name  =  models.CharField('标签名称',max_length = 150)

    def __str__(self):
        return self.name


# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField('标题',max_length = 32)
    author = models.CharField('作者',max_length=16,null=True)
    content = models.TextField('博客正文',null=True)
    created = models.DateTimeField('发布时间',auto_now=True)
    catagory = models.ForeignKey(Catagory,verbose_name='分类',on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(Tag,verbose_name='标签',null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    评论
    '''
    blog = models.ForeignKey(BlogsPost,verbose_name='博客',on_delete=models.CASCADE,)
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    created = models.DateTimeField('发布时间',auto_now=True)

    def __str__(self):
        return self.content



