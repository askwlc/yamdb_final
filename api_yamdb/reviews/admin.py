from django.contrib import admin

from .models import Comment, Review, User, Genre, Category, Title


class GenreTitleInline(admin.TabularInline):
    model = Title.genre.through


class TitleAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'year', 'description')
    search_fields = ('name',)
    list_filter = ('id', )
    inlines = [GenreTitleInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    list_filter = ('id', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    list_filter = ('id', )


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'score', 'title', 'author', 'pub_date', )
    search_fields = ('text', 'author', )
    list_filter = ('pub_date', 'score', 'author', 'title', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'review', 'author', 'pub_date', )
    search_fields = ('text', 'author', )
    list_filter = ('pub_date', 'author', )


admin.site.register(User)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Comment, CommentAdmin)
