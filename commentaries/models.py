from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from bible_com.settings import AUTH_USER_MODEL


# Key words:  word, definition
class KeyWord(models.Model):
    """KeyWord: transliteration,
                word,
                language,
                definition
    """
    LANGUAGE_CHOICES = (('hebrew', 'Hebrew'), ('greek', 'Greek'), ('english', 'English'), )
    transliteration: str = models.CharField(max_length=50, default='??')
    word: str = models.CharField(max_length=50)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='english')
    definition = models.TextField()

    class Meta:
        ordering = ('transliteration', 'word',)

    def __str__(self):
        return self.transliteration + " - " + self.word + " - " + self.language


class Thought(models.Model):
    """Model:  title,
               reference,
               verseText,
               slug,
               concept,
               comments,
               created,
               updated,
               status,
               key words
    """
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'), )
    title: str = models.CharField(max_length=250)
    reference = models.CharField(max_length=100)
    verseText = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    keyWords = models.ManyToManyField(KeyWord, related_name='words')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# TODO:  Save and retrieve database to CSV or Excel

# TODO Load and save lists of commentaries
