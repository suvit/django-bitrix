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

    class Meta(BitrixModel.Meta):
        db_table = btxsettings.DB_PREFIX + 'user'

    def __unicode__(self):
        return self.login


class IBlock(BitrixModel):

    timestamp_x = models.DateTimeField(u'Добавлен')

    type = models.CharField(u'Тип', max_length=50,
                            db_column='IBLOCK_TYPE_ID')

    code = models.CharField(u'Код', max_length=50,
                            null=True)
    name = models.CharField(u'Название', max_length=255)

    active = models.CharField(_('active'),
                              max_length=1,
                              choices=(('Y', _('Yes')), ('N', _('No'))),
                              default='Y')

    sort = models.IntegerField(u'Порядок')

    sections_name = models.CharField(u'Название секций', max_length=100,
                                     null=True)
    section_name = models.CharField(u'Название секции', max_length=100,
                                     null=True)
    elements_name = models.CharField(u'Название элементов', max_length=100,
                                     null=True)
    element_name = models.CharField(u'Название элемента', max_length=100,
                                     null=True)

    class Meta(BitrixModel.Meta):
        db_table = btxsettings.DB_PREFIX + 'iblock'


class IBlockSection(BitrixModel):
    timestamp_x = models.DateTimeField(u'Добавлен')

    class Meta(BitrixModel.Meta):
        db_table = btxsettings.DB_PREFIX + 'iblock_section'


class IBlockElement(BitrixModel):

    timestamp_x = models.DateTimeField(u'Добавлен')

    class Meta(BitrixModel.Meta):
        db_table = btxsettings.DB_PREFIX + 'iblock_element'

