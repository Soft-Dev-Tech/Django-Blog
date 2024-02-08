from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
                "title", 
                "slug", 
                "category",
                "description", 
                "thumbnail", 
                "publish",
                "is_special",
                "status",
            ]
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)
    
class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == "pd":
                self.obj.status = "d"
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user and article.status in ["b", "d"] or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404("You can't access to this page")
        
class AuthorsAccessMixin():
    def dispatch(self, request, *are, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *are, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("login")

class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't access to this page")

class CustomLoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()

            if group:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise Http404("You are not logged in")