django-bitrix
=============

1c-Bitrix models inside django

Support models

* Search Phrase
* User

        from bitrix.models import User as BUser
        from django.contrib.auth.models import User
        
        for b_user in BUser.objects.iterator():
            User.objects.create(username=slugify(b_user.login),
                                password='md5:' + b_user.password)
       

TODO

* group and auth tables
* iblock, iblocksection and iblockelement
