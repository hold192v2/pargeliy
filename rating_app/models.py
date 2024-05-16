from django.utils import timezone

from PIL import Image
from django.db import models
from map.models import Cardss
from users.models import User


# Create your models here.
class Comment(models.Model):
    image = models.ImageField(
        default="default_foo.png", upload_to="post_picture")
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Cardss, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name="URL")
    def __str__(self):
        return f'{self.author.username}\'s Post- {self.author}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)