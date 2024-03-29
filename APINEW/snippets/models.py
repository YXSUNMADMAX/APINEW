from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


# Create your models here.




class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    class Meta:
        ordering = ['title']



class Match(models.Model):
    name=models.CharField(max_length=100)
    mclass=models.IntegerField(default=0)
    upperamount=models.IntegerField(default=3)
    nowammount=models.IntegerField(default=0)
    owner=models.ForeignKey('auth.User', related_name='mybuilt', on_delete=models.CASCADE)
    introduction=models.CharField(max_length=300)
    class Meta:
        ordering = ['mclass']





class Team(models.Model):
    name=models.CharField(max_length=100)
    upperamount=models.IntegerField(default=3)
    nowammount=models.IntegerField(default=0)
    owner=models.ForeignKey('auth.User', related_name='mybuilt1', on_delete=models.CASCADE)
    formatch = models.ForeignKey('Match', related_name='matchteam', on_delete=models.CASCADE)
    introduction=models.CharField(max_length=300)
    class Meta:
        ordering = ['formatch']


