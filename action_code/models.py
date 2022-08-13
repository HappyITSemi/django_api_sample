from django.db import models
# from django.utils import timezone


class ActionCode(models.Model):
    class Meta:
        managed = True
        verbose_name_plural = 'ActionCode'
        db_table = 'action_code'

    action_code = models.CharField(verbose_name='action_name', max_length=255, )
    tel_on = models.BooleanField(verbose_name='tel_on-off')
    tel_message = models.CharField(verbose_name='tel-message', max_length=255, )
    tel_list = models.CharField(verbose_name='tel-list', max_length=255, default='')
    mail_on = models.BooleanField(verbose_name='mail_on-off')
    mail_message = models.CharField(verbose_name='mail--message', max_length=255, )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    def __str__(self):
        return self.action_code
