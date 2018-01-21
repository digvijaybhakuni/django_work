from django.contrib import admin
from .models import Post, Author, Property
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.


class AuthorInline(admin.StackedInline):
    """
    This make Author to be create in any form as
    part of it self not as separate form
    it was like open new pop-up with using this
    """
    model = Author


class AuthorFilter(admin.SimpleListFilter):
    title = 'Select Author'
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        authors = set([c for c in Author.objects.all()])
        return [(c.authorId, c.name) for c in authors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(author__authorId=self.value())
        else:
            return queryset


@admin.register(Post)
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

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 4})},
    }

    """
    This help to add more columns in this list view of post
    """
    list_display = ('title', 'datePub', 'author', 'was_published_recently')

    """
    This add filter to list view
    """
    # list_filter = ('datePub', AuthorFilter)
    list_filter = ('datePub', ('author', admin.ChoicesFieldListFilter))

    # filter_horizontal = ('datePub', 'title') #ManyToManyField

    search_fields = ('title', 'content')


# admin.site.register(Post, PostAdmin)

# admin.site.register(Post)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 30})},
    }

    fieldsets = [
        ('Owner Info', {'fields': ['owner_name', 'owner_type', 'email', 'mobile']}),
        ('Best to time contact', {'fields': ['contact_start_time', 'contact_end_time']}),
        ('Property Info', {'fields': ['property_for', 'property_condition']}),
        ('Meta Info', {'fields': ['project_name', 'buildup_area'], 'classes': ['collapse', 'not-me']}),
    ]

    pass

