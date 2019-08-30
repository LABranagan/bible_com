from django.contrib import admin
from .models import KeyWord, Post

# Register your models here.
@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('transliteration', 'word', 'language')
    list_filter = ('transliteration', 'word', 'language')
    search_fields = ('transliteration', 'word', 'language')
    ordering = ('transliteration', 'word', 'language')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'reference', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

