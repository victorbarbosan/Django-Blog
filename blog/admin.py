from django.contrib import admin


from .models import Commentary, Post, Author, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("author", "date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)


admin.site.register(Author)
admin.site.register(Tag)


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "date")
    list_filter = ("author", "date")

admin.site.register(Commentary, CommentaryAdmin)
