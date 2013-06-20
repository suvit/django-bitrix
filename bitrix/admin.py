from django.contrib import admin

from bitrix.models import (User, SearchPhrase,
                           IBlock, IBlockSection, IBlockElement)

admin.site.register(User)
admin.site.register(SearchPhrase)
admin.site.register(IBlock)
