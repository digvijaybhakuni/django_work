import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    authorId = models.AutoField(primary_key=True)
    name = models.CharField("Author", max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    title = models.CharField("Post Title", max_length=50)
    content = models.CharField("Content", max_length=1000)
    author = models.ForeignKey(Author)
    datePub = models.DateField(verbose_name="Published Date")

    def __str__(self):
        return " Post Title : " + self.title

    def was_published_recently(self):
        return self.datePub >= (timezone.now() - datetime.timedelta(days=10)).date()

    was_published_recently.admin_order_field = 'datePub'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

"""
    Using database models
    to query on Models we get methods

    ALL
        > Give all object from db
         Example ' Post.objects.all() '

    GET
        > Get Return Only One Object
        > If zero or more then one result is found then error is thrown

        Example ' Post.objects.get(title="Test") '
        Example ' Post.objects.get(1) ' # by default args is primary field

    FILTER
        > Return Multiple object
        > Technically a QuerySet, allowing more complex queries
        > Chaining for filter is also there

        Example 'Post.objects.filter(title__startswith = "Tes")' # Two undersorce
        Example 'Post.objects.filter(title__istartswith = "Tes")' # i for case insensitive
        Example 'Post.objects.filter(title__iexact = "Tes")' # i for case insensitive exact match can use with get
        Example 'Post.objects.filter(title__exact = "Tes")' # case sensitive exact match can use with get
        Example 'Post.objects.filter(title__exact = "Tes")' # case sensitive exact match can use with get
        Example 'Post.objects.filter(author__name='Digvijay')' # Querying on forgin key property use with get


    EXCLUDE #TODO
        Example 'Post.objects.filter(author__name='Digvijay').exclude(title='Java')' # Querying filter all record which has author and exclude remove by matching title



"""