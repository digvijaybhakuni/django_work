from django.contrib import admin
from .models import Post, Author
# Register your models here.


class AuthorInline(admin.StackedInline):
    """
    This make Author to be create in any form as
    part of it self not as separate form
    it was like open new pop-up with using this
    """
    model = Author


class PostAdmin(admin.ModelAdmin):
    """
    This PostAdmin class extends the admin.ModelAdmin
    to modifiy and customise the look and feel of
    the Admin Panel Form for the Post Model
    """

    # fields = ['title', 'author']
    # To show only fields in the fields list this code uncomment will not work as other fields are also required

    """
    This make from in categories manger
    """
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Post Content', {'fields': ['content']}),
        ('Meta Info', {'fields': ['author', 'datePub'], 'classes': ['collapse']}),
    ]

    """
    This help to add more columns in this list view of post
    """
    list_display = ('title', 'datePub', 'author', 'was_published_recently')
    list_filter = ['datePub']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)

