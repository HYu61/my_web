from django.db import models


class HomePageFooterContent(models.Model):
    name = models.CharField(max_length=50, default='home_page_and_footer_info', verbose_name='Name')
    content = models.TextField(verbose_name='Content', help_text='The content display on the home page')
    footer = models.TextField(default='', verbose_name='Footer Content')

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=50, verbose_name='Certification name')
    certificate = models.FileField(upload_to='certificate', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Certification.objects.get(id=self.id)
            if this.certificate != self.certificate:
                this.certificate.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Certification, self).save(*args, **kwargs)
