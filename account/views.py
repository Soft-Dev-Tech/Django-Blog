from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldsMixin,  FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin, AuthorsAccessMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article
from .forms import ProfileForm

# Create your views here.

class ArticleListView(AuthorsAccessMixin, ListView):
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
    template_name = "registration/home.html"

class ArticleCreateView(AuthorsAccessMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdateView(AuthorAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"

class ArticleDeleteView(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = "registration/article_confirm_delete.html"


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            "user": self.request.user
        })
        return kwargs
    

class LoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")