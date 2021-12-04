from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, SubscribeContent
from .forms import CommentForm, SubscriptionForm


def home_view(request):
    articles = Article.objects.all().order_by('-id')
    interesting_articles = Article.objects.filter(is_interesting=True).order_by('-id')
    mysterious_articles = Article.objects.filter(is_mysterious=True).order_by('-id')
    flower_articles = Article.objects.filter(category__title="Flower").order_by('-id')
    fruit_articles = Article.objects.filter(category__title="Fruit").order_by('-id')
    vegetable_articles = Article.objects.filter(category__title="Vegetable").order_by('-id')
    spice_articles = Article.objects.filter(category__title="Spice").order_by('-id')
    herb_articles = Article.objects.filter(category__title="Herb").order_by('-id')

    context = {
        'articles': articles,
        'interesting_articles': interesting_articles,
        'mysterious_articles': mysterious_articles,
        'flower_articles': flower_articles,
        'fruit_articles': fruit_articles,
        'vegetable_articles': vegetable_articles,
        'spice_articles': spice_articles,
        'herb_articles': herb_articles,
    }
    return render(request, 'index.html', context)


def news_list(request):
    articles = Article.objects.all().order_by('-date_published')
    paginator = Paginator(articles, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    most_read_articles = Article.objects.filter(most_read=True).order_by('-id')
    most_shared_articles = Article.objects.filter(most_shared=True).order_by('-id')
    contents = SubscribeContent.objects.all()
    
    if request.method == 'POST':
        subscription_form = SubscriptionForm(data=request.POST)
        if subscription_form.is_valid():
            subscription_form.save()
            return render(request, 'subscribe_success.html')
    else:
        subscription_form = SubscriptionForm()

    context = {
        'page_obj': page_obj,
        'most_read_articles': most_read_articles,
        'most_shared_articles': most_shared_articles,
        'contents': contents,
        'subscription_form': subscription_form
    }
    return render(request, 'news_list.html', context)


def category_news_list(request, slug):
    articles = Article.objects.filter(category__slug=slug).order_by('-id')
    paginator = Paginator(articles, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    most_read_articles = Article.objects.filter(category__slug=slug, most_read=True).order_by('-id')
    most_shared_articles = Article.objects.filter(category__slug=slug, most_shared=True).order_by('-id')
    contents = SubscribeContent.objects.all()

    if request.method == 'POST':
        subscription_form = SubscriptionForm(data=request.POST)
        if subscription_form.is_valid():
            subscription_form.save()
            return render(request, 'subscribe_success.html')
    else:
        subscription_form = SubscriptionForm()

    context = {
        'page_obj': page_obj,
        'most_read_articles': most_read_articles,
        'most_shared_articles': most_shared_articles,
        'contents': contents,
        'subscription_form': subscription_form
    }
    return render(request, 'category_news_list.html', context)


def news_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.filter(category=article.category, is_interesting=True).order_by('-id')
    comments = article.comments.filter(active=True)

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'article': article,
        'related_articles': related_articles,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'news_detail.html', context)


def privacy_policy(request):
    pass 
    return render(request, 'privacy_policy.html', {})


