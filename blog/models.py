from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Author(models.Model):        
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True)

    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])

class Post(models.Model):
    title = models.CharField(_('Title'),max_length=200)
    slug = models.SlugField(_('Slug'), unique=True, help_text=_("Slug will be generated automatically from the title of the post"))
    content = RichTextUploadingField(_('Content'))
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
      return reverse('post_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(_('Name of the sender'), max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(_('Subject'), max_length=200)
    message = models.TextField(_('Message'))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _("Feedback")

    def __str__(self):
        return self.name + "-" + self.email


