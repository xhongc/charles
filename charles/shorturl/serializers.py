from django.conf import settings
from rest_framework import serializers
import time
from charles.shorturl.models import ShortUrl
from utils.base_descrpt import _md5, base64decode


class ShortUrlCreateSerilizer(serializers.ModelSerializer):
    paste_path = serializers.URLField()
    short_link = serializers.CharField(read_only=True)

    def validate(self, attrs):
        pp = ShortUrl.objects.filter(paste_path=attrs['paste_path']).first()
        if pp:
            attrs['short_link'] = pp.pk
            # 重复short_link 设置一个字段判断要 更新还是创建
            self._context['create_or_update'] = 'update'
        else:
            if settings.DEBUG:
                ip_address = self._context.get('request')._request.META.get('REMOTE_ADDR')
            else:
                ip_address = self._context.get('request')._request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0]
            timestamp = time.time()

            ret = base64decode(_md5(ip_address + str(timestamp)))[:7].replace('+', 'A').replace('/', 'B').replace('=',
                                                                                                                  'C')
            while ShortUrl.objects.filter(short_link=ret).exists():
                timestamp = time.time()
                ret = base64decode(_md5(ip_address + str(timestamp)))[:7] \
                    .replace('+', 'A').replace('/', 'B').replace('=', 'C')
            attrs['short_link'] = ret.upper()
            self._context['create_or_update'] = 'create'
        return attrs

    def save(self, **kwargs):
        if self._context['create_or_update'] == 'create':
            super(ShortUrlCreateSerilizer, self).save()

    class Meta:
        model = ShortUrl
        fields = ('paste_path', 'short_link')
