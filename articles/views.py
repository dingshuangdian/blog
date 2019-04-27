# _*_ coding:utf-8 _*_
import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger  # 实现分页功能
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Categories, Articles, Jottings, ItsMe, AdminUser, GetMessage, CommenttUser


# Create your views here.

class IndexView(View):
    """显示首页"""

    def get(self, request):
        categories = Categories.objects.all()
        articles = Articles.objects.all()

        # 首页轮播博文
        casoule_articles = articles.filter(is_index=1).order_by('id')
        casoule_articles = casoule_articles[:3] if len(casoule_articles) > 3 else casoule_articles
        # 最多评论
        content_articles = articles.order_by('comment_nums')[:5] if len(articles) > 5 else articles.order_by(
            'comment_nums')
        # 首页博文列表,按照添加时间倒序,分页
        list_articles = articles.order_by('-add_time')
        # 最多浏览
        view_articles = articles.order_by('-click_nums')[:4] if len(articles) > 4 else articles.order_by('-click_nums')
        # 最近更新
        recent_articles = list_articles[:6] if len(list_articles) > 6 else list_articles
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(list_articles, 4, request=request)
        list_articles = p.page(page)
        # It's me
        itsmes = ItsMe.objects.all()
        content = {
            'categories': categories,
            'casoule_articles': casoule_articles,
            'content_articles': content_articles,
            'list_articles': list_articles,
            'itsmes': itsmes,
            'view_articles': view_articles,
            'recent_articles': recent_articles,
        }
        return render(request, 'index.html', content)


class ArticlesListView(View):
    """博客分类列表"""
    def get(self, request, category):
        if not category:
            category = 1
        categories = Categories.objects.all()
        articles = Articles.objects.filter(categorie=category)
        # 最多评论
        # 最多评论
        content_articles = articles.order_by('comment_nums')[:5] if len(articles) > 5 else articles.order_by(
            'comment_nums')
        # 最多浏览
        view_articles = articles.order_by('-click_nums')[:4] if len(articles) > 4 else articles.order_by('-click_nums')
        # 最近更新
        recent_articles = articles.order_by('-add_time')[:6] if len(articles) > 6 else articles.order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(articles, 12, request=request)
        articles = p.page(page)
        # It's me
        itsmes = ItsMe.objects.all()

        content = {
            'categories': categories,
            'articles': articles,
            'itsmes': itsmes,
            'content_articles': content_articles,
            'view_articles': view_articles,
            'recent_articles': recent_articles,
        }
        return render(request, 'articleslist.html', content)


class ArticleDetailView(View):
    """博客详情"""

    def get(self, request, pk):
        if not pk:
            pk = 1
        categories = Categories.objects.all()
        article = get_object_or_404(Articles, id=pk)
        articles = Articles.objects.filter(categorie=article.categorie)
        # 最多评论
        content_articles = articles.order_by('comment_nums')[:5] if len(articles) > 5 else articles.order_by(
            'comment_nums')
        # 最多浏览
        view_articles = articles.order_by('-click_nums')[:4] if len(articles) > 4 else articles.order_by('-click_nums')
        # 最近更新
        recent_articles = articles.order_by('-add_time')[:6] if len(articles) > 6 else articles.order_by('-add_time')
        # It's me
        itsmes = ItsMe.objects.all()
        tags = article.tags.all()

        # 上一篇、下一篇链接
        ids = [article.id for article in articles]  # 获取所有同类的博客文章的id
        id_index = ids.index(article.id)
        prearticle = None
        nextarticle = None
        if len(ids) > 1:
            if not id_index:
                nextid = ids[id_index + 1]
                nextarticle = get_object_or_404(articles, id=nextid)
            elif id_index == (len(ids) - 1):
                preid = ids[id_index - 1]
                prearticle = get_object_or_404(articles, id=preid)
            else:
                preid = ids[id_index - 1]
                prearticle = get_object_or_404(articles, id=preid)
                nextid = ids[id_index + 1]
                nextarticle = get_object_or_404(articles, id=nextid)

        content = {
            'categories': categories,
            'itsmes': itsmes,
            'content_articles': content_articles,
            'view_articles': view_articles,
            'recent_articles': recent_articles,
            'article': article,
            'tags': tags,
            'prearticle': prearticle,
            'nextarticle': nextarticle,
        }
        return render(request, 'articledetail.html', content)


class JottingsListView(View):
    """心情随笔"""

    def get(self, request):
        categories = Categories.objects.all()
        jottings = Jottings.objects.all()
        # 最多评论
        content_jottings = jottings.order_by('comment_nums')[:5] if len(jottings) > 5 else jottings.order_by(
            'comment_nums')
        # 最多浏览
        view_jottings = jottings.order_by('-click_nums')[:4] if len(jottings) > 4 else jottings.order_by('-click_nums')
        # 最近更新
        recent_jottings = jottings.order_by('-add_time')[:6] if len(jottings) > 6 else jottings.order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(jottings, 4, request=request)
        jottings = p.page(page)
        # It's me
        itsmes = ItsMe.objects.all()

        content = {
            'categories': categories,
            'jottings': jottings,
            'itsmes': itsmes,
            'content_jottings': content_jottings,
            'view_jottings': view_jottings,
            'recent_jottings': recent_jottings,
        }
        return render(request, 'jottings.html', content)


class JottingsDetailView(View):
    """心情随笔详情"""

    def get(self, request, pk):
        if not pk:
            pk = 1
        categories = Categories.objects.all()
        jottings = Jottings.objects.all()
        jotting = get_object_or_404(jottings, id=pk)
        # 最多评论
        content_articles = jottings.order_by('comment_nums')[:5] if len(jottings) > 5 else jottings.order_by(
            'comment_nums')
        # 最多浏览
        view_articles = jottings.order_by('-click_nums')[:4] if len(jottings) > 4 else jottings.order_by('-click_nums')
        # 最近更新
        recent_articles = jottings.order_by('-add_time')[:6] if len(jottings) > 6 else jottings.order_by('-add_time')
        # It's me
        itsmes = ItsMe.objects.all()
        tags = jotting.tags.all()

        # 上一篇、下一篇链接
        ids = [jotting.id for jotting in jottings]  # 获取所有同类的博客文章的id
        id_index = ids.index(jotting.id)
        prearticle = None
        nextarticle = None
        if len(ids) > 1:
            if not id_index:
                nextid = ids[id_index + 1]
                nextarticle = get_object_or_404(jottings, id=nextid)
            elif id_index == (len(ids) - 1):
                preid = ids[id_index - 1]
                prearticle = get_object_or_404(jottings, id=preid)
            else:
                preid = ids[id_index - 1]
                prearticle = get_object_or_404(jottings, id=preid)
                nextid = ids[id_index + 1]
                nextarticle = get_object_or_404(jottings, id=nextid)

        content = {
            'categories': categories,
            'itsmes': itsmes,
            'content_articles': content_articles,
            'view_articles': view_articles,
            'recent_articles': recent_articles,
            'jotting': jotting,
            'tags': tags,
            'prearticle': prearticle,
            'nextarticle': nextarticle,
        }
        return render(request, 'jottingdetail.html', content)


class ContactView(View):
    """联系我"""

    def get(self, request):
        categories = Categories.objects.all()
        admin = AdminUser.objects.all()[0]

        content = {
            'categories': categories,
            'address': json.dumps(admin.address),
            'admin': admin,
        }
        return render(request, 'contact.html', content)


class SearchView(View):
    """搜索功能"""

    def get(self, request):
        search = request.GET.get('search', '')
        categories = Categories.objects.all()
        articles = Articles.objects.all()
        # 最多评论
        # 最多评论
        content_articles = articles.order_by('comment_nums')[:5] if len(articles) > 5 else articles.order_by(
            'comment_nums')
        # 最多浏览
        view_articles = articles.order_by('-click_nums')[:4] if len(articles) > 4 else articles.order_by(
            '-click_nums')
        # 最近更新
        recent_articles = articles.order_by('-add_time')[:6] if len(articles) > 6 else articles.order_by(
            '-add_time')

        search_article = articles.filter(title__contains=search)
        if not search_article:
            search_article = articles
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(search_article, 12, request=request)
        search_article = p.page(page)
        # It's me
        itsmes = ItsMe.objects.all()

        content = {
            'categories': categories,
            'articles': search_article,
            'itsmes': itsmes,
            'content_articles': content_articles,
            'view_articles': view_articles,
            'recent_articles': recent_articles,
        }
        return render(request, 'articleslist.html', content)


class MsgView(View):
    """留言处理"""

    def post(self, request):
        msg = GetMessage()
        msg.name = request.POST.get('name', '')
        msg.email = request.POST.get('email', '')
        msg.subject = request.POST.get('subject', '')
        msg.message = request.POST.get('message', '')
        msg.save()
        res = {'status': 'success'}
        return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
def GetComment(request):
    """接收评论回推，并导入数据库中，后台可见，用于二次开发备用"""

    arg = request.POST
    data = arg.get('data')
    data = json.loads(data)
    comments = data.get('comments', '')[0]
    nickname = comments.get('user').get('nickname', '')
    usericon = comments.get('user').get('usericon', '')
    area = comments.get('user').get('usermetadata').get('area', '')
    gender = comments.get('user').get('usermetadata').get('gender', '')
    sourceid = data.get('sourceid')
    articles = Articles.objects.filter(id=sourceid)
    title = ''
    if not articles:
        return JsonResponse({"status": "failed"})
    else:
        for article in articles:
            title = article.title
            break
    comment = comments.get('content')
    CommenttUser(nickname=nickname, usericon=usericon, area=area, gender=gender, article=title, comment=comment).save()

    return JsonResponse({"status": "ok"})

