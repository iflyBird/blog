from django.shortcuts import render,redirect
from django.views import View
from home.models import ArticleCategory, Article
from django.http.response import HttpResponseNotFound
# 导入分页器
from django.core.paginator import Paginator, EmptyPage
from django.urls import  reverse
#导入评论模型
from home.models import Comment
# Create your views here.
class IndexView(View):
    def get(self, request):
        # 获取所有的分类信息
        # 2、根据用户点击的分类id
        # 根据分类id进行分类的查询
        # 4、获取分页参数
        # 5、根据分类信息查询文章数据
        # 7、分页处理
        # 8、组织数据传递模板
        categories = ArticleCategory.objects.all()
        # 没有传递的话默认值是1
        # c从前端获取cat_id,默认是1
        cat_id = request.GET.get('cat_id', 1)
        # 操作数据库
        try:
            # 从数据库中拿出对应的cat_id得值，表示的一行多个属性，获取id属性就是category.id
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound("没有此分类")
        # 组织数据传递给模板
        # 4、获取分页参数
        # 5、根据分类信息查询文章数据
        # 7、分页处理
        # 默认是1
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 8)
        # 根据分类信息查询数据
        articles = Article.objects.filter(category=category)
        pagintor = Paginator(articles, per_page=page_size)
        # 分页处理
        try:
            page_articles = pagintor.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound("empty page")
        # 总页数
        total_page = pagintor.num_pages
        context = {
            'categories': categories,
            'category': category,
            'articles': page_articles,
            'page_size': page_size,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, 'index.html', context=context)


# 详细信息展示
class DetailVIew(View):
    def get(self, request):
        # 1、接收文章的id信息
        # 2、根据文章的id进行查看
        # 3、查询分类的数据
        # 4、组织模板数据


        #5、获取分页请求数据
        #6、根据文章信息查询评论数据
        #7、床架你分页器
        #8、进行分页处理
        id = request.GET.get('id')
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return render(request, '404.html')

            pass
        else:
            # 让浏览量加1
            article.total_views += 1
            article.save()

        categories = ArticleCategory.objects.all()
        # 组织模板数据
        # 查询浏览量前十的文章数据
        # 降序
        hot_article = Article.objects.order_by('-total_views')[:9]
        #5、获取分页请求数据
        #6、根据文章信息查询评论数据
        #7、床架你分页器
        #8、进行分页处理
        page_size=request.GET.get('page_size',10)
        page_num=request.GET.get('page_num',1)
        #根据文章的信息查询评论的数据
        comments=Comment.objects.filter(article=article).order_by('-created')
        #获取评论的总数
        total_count=comments.count()
        #创建分页器
        from django.core.paginator import Paginator,EmptyPage
        paginator=Paginator(comments,page_size)
        #进行分页处理
        try:
            page_comments=paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound("empty page")
        #总页数
        total_page=paginator.num_pages

        context = {
            'categories': categories,
            'category': article.category,
            'article': article,
            'hot_article': hot_article,
            'total_count':total_count,
            'comments':page_comments,
            'page_size':page_size,
            'total_page':total_count,
            'page_num':page_num

        }
        return render(request, "detail.html", context=context)

    def post(self, request):
        #1、接收用户的信息
                # 2、判断用户是否登陆
                # 3、登录用户可以接受form数据
                #     3、1接收评论的数据
                #     3、2验证文章是否存在
                #     3.3保存评论数据
                #     3.4修改文章的评论数量
                # 4、未登录用户则直接跳回登录页面
        user = request.user
        if user and user.is_authenticated:
            #这里的id是从detail传入的一个隐藏的id.value=article.id
            id=request.POST.get('id')
            content=request.POST.get('content')
            #判断文章是否存在
            try:
                article=Article.objects.get(id=id)

            except Article.DoesNotExist:
                return HttpResponseNotFound("没有此文章")
            #保存评论的数据
            Comment.objects.create(
                content=content,
                article=article,
                user=user
            )
            #修改文章的评论数据
            article.comments_count+=1
            article.save()
            #刷新页面，重回到这个页面
            path=reverse('home:detail')+'?id={}'.format(article.id)
           #重定向路由
            return redirect(path)


        else:
            return redirect(reverse('user:login'))

