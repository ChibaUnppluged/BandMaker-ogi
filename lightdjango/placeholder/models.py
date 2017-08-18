# coding:utf-8
from django.db import models
from django import forms
from PIL import Image,ImageDraw
from io import BytesIO
from django.core.cache import cache

# Create your models here.

class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1,max_value=2000)
    width = forms.IntegerField(min_value=1,max_value=2000)
    def generate(self,image_format='PNG'):
        # validation済のheightとwidthを取得する
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        # キャッシュに保存,読み込みをする際のkeyの生成
        key = '{}.{}.{}'.format(width,height,image_format)
        # keyがすでにキャッシュに存在しない場合if内を実行
        content = cache.get(key)
        if content is None:
            # Imageの生成
            image = Image.new('RGB',(width,height))
            # 描画を準備
            draw = ImageDraw.Draw(image)
            text = '{}x{}'.format(width,height)
            textwidth,textheight = draw.textsize(text)
            # 画像の幅より文字の大きさが小さいなら文字を描画
            if textwidth < width and textheight < height:
                texttop = (height - textheight)
                textleft = (width - textwidth)
                draw.text((textleft,texttop),text,fill=(255,255,255))
            content = BytesIO()
            image.save(content,image_format)
            content.seek(0)
            #このif文が実行されているということはキャッシュが存在しないので保存
            cache.set(key,content,60 * 60)
        return content
