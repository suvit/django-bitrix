# -*- coding: utf-8 -
from django.db import models
from django.db.models.base import ModelBase
from django.utils.translation import ugettext_lazy as _

from bitrix.conf import BitrixConf as btxsettings


class BitrixManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return (super(BitrixManager, self).get_query_set(*args, **kwargs)
                                          .using(btxsettings.DATABASE)
                )


class BitrixModel(models.Model):

    objects = BitrixManager()

    class Meta:
        abstract = True
        managed = False
        #app_label = 'bitrix'


class SearchPhrase(BitrixModel):
    phrase = models.CharField(u'Фраза', max_length=250)

    timestamp_x = models.DateTimeField(u'Добавлен')

    class Meta(BitrixModel.Meta):
        db_table = btxsettings.DB_PREFIX + 'search_phrase'

    def __unicode__(self):
        return self.phrase


class User(BitrixModel):
    login = models.CharField(_('username'), max_length=50)
    password = models.CharField(_('password'), max_length=50)

    active = models.CharField(_('active'),
                              max_length=1,
                              choices=(('Y', _('Yes')), ('N', _('No'))),
                              default='Y')

    name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('e-mail address'), max_length=255)

    last_login = models.DateTimeField(_('last login'))
    date_register = models.DateTimeField(_('date joined'))

    def __unicode__(self):
        return self.username

