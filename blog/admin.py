from django.contrib import admin
from .models import Article, Category
from .actions import Publish, Draft, Pending, Back, Active, Passive

# Register your models here.

# admin.site.disable_action("delete_selected") for disabling delete action from admin panel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", "title", "slug", "parent", "status")
    list_filter = (["status"])
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    actions = [Active.active, Passive.passive]

admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_tag", "slug", "author", 
                    "publish", "is_special", "status", "category_to_str")
    list_filter = ("publish", "status", "author")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "publish"]
    # actions = ["make_published", "make_draft"] if use action in this class like bellow
    actions = [Publish.make_published, Draft.make_draft, Pending.make_pending, Back.make_back]



    # if use actions in this class

    # @admin.action(description="Mark selected articles as Published")
    # def make_published(self, request, queryset):
    #     updated = queryset.update(status="p")
    #     if updated == 1:
    #         message = "1 Article"
    #     else:
    #         message = "%s Articles were" % updated
    #     self.message_user(
    #         request, "%s Successfully marked as Published." % message)

    # @admin.action(description="Mark selected articles as Draft")
    # def make_draft(self, request, queryset):
    #     updated = queryset.update(status="d")
    #     if updated == 1:
    #         message = "1 Article"
    #     else:
    #         message = "%s Articles were" % updated
    #     self.message_user(
    #         request, "%s Successfully marked as Draft." % message)


admin.site.register(Article, ArticleAdmin)
