import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from . import options
# Create your models here.


class Author(models.Model):
    authorId = models.AutoField(primary_key=True)
    name = models.CharField("Author", max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    title = models.CharField("Post Title", max_length=50)
    content = models.TextField("Content", max_length=1000)
    author = models.ForeignKey(Author)
    datePub = models.DateField(verbose_name="Published Date")

    def __str__(self):
        return " Post Title : " + self.title

    def was_published_recently(self):
        # return self.datePub >= (timezone.now() - datetime.timedelta(days=10)).date()
        now = timezone.now();
        return (now - datetime.timedelta(days=30)).date() <= self.datePub <= now.date()

    was_published_recently.admin_order_field = 'datePub'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Property(models.Model):

    # Fields
    property_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=100)
    owner_type = models.CharField(max_length=1, choices=options.OWNER_TYPE)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    property_type = models.CharField(max_length=2, choices=options.PROPERTY_TYPE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    contact_start_time = models.TimeField()
    contact_end_time = models.TimeField()
    property_condition = models.BooleanField()
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    block = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    buildup_area = models.PositiveIntegerField()
    carpat_area = models.PositiveIntegerField()
    no_of_bedroom = models.PositiveIntegerField()
    no_of_bathroom = models.PositiveIntegerField()
    no_of_balconies = models.PositiveIntegerField()
    property_value = models.IntegerField()
    property_rent = models.PositiveIntegerField()
    security_deposit = models.PositiveIntegerField()
    maintenance_charges = models.PositiveIntegerField()
    bachelors_allowed = models.BooleanField()
    non_veg_allowed = models.BooleanField(max_length=100)
    pets_allowed = models.BooleanField()
    registration_fee_included = models.NullBooleanField(max_length=100)
    description = models.TextField(max_length=500)
    possession_date = models.DateField()
    year_of_construction = models.PositiveIntegerField()
    property_status = models.CharField(max_length=100, choices=options.PROPERTY_STATUS)
    total_floors = models.PositiveIntegerField()
    floor_no = models.PositiveIntegerField()
    property_facing = models.CharField(max_length=1, choices=options.DIRECTION)
    separate_dining_space = models.BooleanField()
    servant_room = models.BooleanField()
    furnishing_type = models.CharField(max_length=1, choices=options.FURNISHING_TYPE)
    amenities = models.TextField(max_length=100)
    listing_status = models.CharField(max_length=1, choices=options.LISTING_STATUS)
    property_for = models.CharField(max_length=1, choices=options.PROPERTY_FOR)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s %s %s' % (self.owner_name, self.property_rent, self.address)

    def __str__(self):
        return '%s %s %s' % (self.owner_name, self.property_rent, self.address)

    def get_absolute_url(self):
        return reverse('happPortal_property_detail', args=(self.property_id,))

    def get_update_url(self):
        return reverse('happPortal_property_update', args=(self.property_id,))





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