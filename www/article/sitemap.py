# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap

from article.models import Item

####################################################################################################
####################################################################################################


#Для карты сайта
class ArticleSitemap(Sitemap):
    def items(self):
        return Item.activs.all()

    def location(self, obj):
        return obj.get_absolute_url()

####################################################################################################
####################################################################################################