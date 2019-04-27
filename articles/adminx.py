#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "版权所有@源码商城：https://shop530346312.taobao.com/?spm=a1z10.1-c.0.0.1c1f6daeeNP5VM"
__date__ = "2019/04/12 14:46"

import xadmin
from xadmin import views
from .models import AdminUser, CommenttUser, Categories, Tags, Articles,Jottings,ItsMe,GetMessage


class BaseSetting:
    """
    后台修改需要的配置
    """
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSettings:
    """
    后台修改
    """
    site_title = '博客后台管理'
    site_footer = '博客后台管理'


class ArticlesAdmin:
    list_display = ['title', 'img', 'author', 'categorie', 'tags', 'add_time', 'click_nums', 'comment_nums', 'fav_nums']
    list_filter = ['title', 'img', 'author', 'categorie', 'tags', 'click_nums', 'comment_nums', 'fav_nums']
    search_fields = ['title', 'img', 'author', 'categorie', 'tags', 'click_nums', 'comment_nums', 'fav_nums']
    readonly_fields = ['click_nums', 'comment_nums', 'fav_nums']
    style_fields = {"content": "ueditor"}
    model_icon = 'fa fa-book'

class JottingsAdmin:
    list_display = ['title', 'img', 'author', 'tags', 'add_time', 'click_nums', 'comment_nums', 'fav_nums']
    list_filter = ['title', 'img', 'author', 'tags', 'click_nums', 'comment_nums', 'fav_nums']
    search_fields = ['title', 'img', 'author', 'tags', 'click_nums', 'comment_nums', 'fav_nums']
    readonly_fields = ['click_nums', 'comment_nums', 'fav_nums']
    style_fields = {"content": "ueditor"}
    model_icon = 'fa fa-heart'


class CommenttUserAdmin:
    model_icon = 'fa fa-users'
    pass


class CategoriesAdmin:
    model_icon = 'fa fa-bars'
    pass


class TagsAdmin:
    model_icon = 'fa fa-tags'
    pass


class AdminUserAdmin:
    list_display = ['name', 'address', 'phone', 'email']
    model_icon = 'fa fa-user'


class ItsMeAdmin:
    model_icon = 'fa fa-address-card'

class GetMessageAdmin:
    model_icon = 'fa fa-envelope-o'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Categories, CategoriesAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(Jottings, JottingsAdmin)
xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(ItsMe, ItsMeAdmin)
xadmin.site.register(AdminUser, AdminUserAdmin)
xadmin.site.register(CommenttUser, CommenttUserAdmin)
xadmin.site.register(GetMessage, GetMessageAdmin)

