from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Image(models.Model):
    title = models.CharField(max_length=200, default='None')
    image = models.ImageField(upload_to='face', default='../media/james.jpg')
    
    
    def __str__(self):
        return self.title
