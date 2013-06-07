# -*- coding: utf-8 -
from django.db import models
from django.db.models.base import ModelBase

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

