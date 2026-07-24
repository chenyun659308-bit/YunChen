from django.db import models

class Contract(models.Model):
    name = models.CharField('姓名', max_length=50)
    phone = models.CharField('手机号', max_length=20)
    email = models.EmailField('邮箱', max_length=100, blank=True, null=True)
    title = models.CharField('主题', max_length=200)
    content = models.TextField('留言内容')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '留言表单'
        verbose_name_plural = '留言管理'

    def __str__(self):
        return f'{self.name} - {self.title}'