from django.contrib import admin
from .models import Category, Article, Comment, SubscribeContent, Subscription


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'image_tag', 'is_interesting', 'is_mysterious', 'most_read', 'most_shared', 'get_date')
    list_filter = ('title', 'category', 'date_published',)
    list_editable = ('is_interesting', 'is_mysterious')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article, ArticleAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'description')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(SubscribeContent)
admin.site.register(Subscription)
