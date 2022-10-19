from django.db import models
from django.contrib.auth import get_user_model
#from tinymce.models import HTMLfield
from django_resized import ResizedImageField
from django.utils.text import slugify
#from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from users.models import CustomUser

# Create your models here.

CustomUser = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    fullname = models.CharField(max_length=400, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = models.TextField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50, 80], quality = 100, upload_to= "authors",  null=True, blank=True, default = "authors/indir.jpg")

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"
    

class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    replies = models.ManyToManyField(Reply, blank=True)
    
    def __str__(self):
        return self.content[:100]
    
class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = RichTextField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    #hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")


