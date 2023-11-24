from django.contrib import admin

# Register your models here.
from .models import Post, Author, Comment


class PostInstanceInline(admin.TabularInline):
    model = Comment
    extra = 2


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_display_links = ['timestamp', 'updated']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    list_editable = ['title']
    exclude = ('post_likes',)
    inlines = [PostInstanceInline]

    class Meta:
        model = Post


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email']
    list_display_links = ['first_name', 'second_name']
    search_fields = ['first_name', 'second_name']
    list_editable = ['email']
    fields = ('first_name', 'second_name', 'email')

    class Meta:
        model = Author


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'comment_article']
    list_display_links = ['comment_text', 'comment_article']
    search_fields = ['comment_text', 'comment_article']

    class Meta:
        model = Comment


admin.site.register(Post, PostModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
