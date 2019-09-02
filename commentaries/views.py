from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostCreationForm, PostUpdateForm


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'commentaries/post_list.html', {'posts':posts})


def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostUpdateForm(request.POST or None, instance=post)
    # form = PostUpdateForm(request.POST, instance=post)

    if form.is_valid():
        form.save()
        return redirect('list_posts')

    return render(request, 'commentaries/post_form.html', {'form':form})


class PostListView(ListView):
    form_class = PostCreationForm
    # fields = ('title', 'reference', 'verseText', 'body', 'status', 'keyWords')
    template_name = 'commentaries/post_form.html'


class PostCreateView(CreateView):
    form_class = PostCreationForm
    # fields = ('title', 'reference', 'verseText', 'body', 'status', 'keyWords')
    template_name = 'post_form.html'



# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

#TODO:  CRUD (create, read, update, delete) for each entry
