from django.db import models


# Create your models here.
class Categories(models.Model):
    cate_name = models.CharField(max_length=50, unique=True, verbose_name='Category')
    priority = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ('priority',)

    def __str__(self):
        return self.cate_name


class Projects(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Project title')
    description = models.TextField(verbose_name='Description')
    github_link = models.CharField(max_length=100, blank=True, null=True, default='',
                                   verbose_name="Github link of the projects")
    url = models.CharField(max_length=100, blank=True, null=True, default='',
                           verbose_name='The url of the launched projects')

    # null 是针对数据库而言，如果 null = True, 表示数据库的该字段可以为空；blank 是针对表单的，如果 blank = True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    image = models.ImageField(upload_to='projects/image', blank=True, null=True)
    video = models.FileField(upload_to='projects/video', blank=True, null=True)
    cate = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, default='', verbose_name='Tags for the projects')
    published = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = 'Project info'
        verbose_name_plural = 'Projects Info'
        ordering = ('cate', 'priority',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Projects.objects.get(id=self.id)
            if this.image != self.image:
                this.image.storage.delete(this.image.name)
                super().delete()
            if this.video != self.video:
                this.video.storage.delete(this.video.name)
                super().delete()
        except:
            pass  # when new photo then we do nothing, normal case
        super(Projects, self).save(*args, **kwargs)

    def tags_as_list(self):
        return self.tags.split(',')

    def desc_count(self):
        return len(self.description)