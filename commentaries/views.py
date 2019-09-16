from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView
from .models import Thought,KeyWord
from .forms import ThoughtCreationForm, ThoughtUpdateForm, ThoughtsListForm


class ListKeyword(ListView):
    model=KeyWord
    context_object_name = 'words'
    fields=['transliteration','word','language','definition']
    template_name = 'list_keywords.html'


class CreateWord(CreateView):
    model=KeyWord
    fields=['transliteration','word','language','definition']
    template_name = 'keyword_create.html'

    def form_valid(self, form):
        return super(CreateWord, self).form_valid(form)


def list_thoughts(request):
    thoughts = Thought.objects.all()
    return render(request, 'thought_listall.html', {'thoughts':thoughts})


def update_thought(request, slug):
    thought = Thought.objects.get(slug=slug)
    form = ThoughtUpdateForm(request.POST or None, instance=thought)
    context = {'form': form}
    # form = PostUpdateForm(request.POST, instance=post)

    if form.is_valid():
        form.save()
        return redirect('commentaries:list_thoughts')

    return render(request, 'thought_form.html', context)


class ThoughtsListView(ListView):
    # queryset = Thought.objects.all()
    # form_class = ThoughtsListForm
    model = Thought
    context_object_name = 'thoughts'
    # paginate_by = 5
    template_name = 'thought_list.html'

# TODO:  Some thought detail views find (4) items instead of 1 ??

class ThoughtCreateView(CreateView):
    model = Thought
    # form_class = ThoughtCreationForm
    fields = ('title', 'slug', 'reference', 'verseText', 'body', 'status', 'keyWords')
    template_name = 'thought_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ThoughtCreateView, self).form_valid(form)

class ThoughtDetail(DetailView):
    model = Thought
    queryset = Thought.objects.all()

    def get_object(self):
        # Call superclass
        object = super(ThoughtDetail, self).get_object()
        return object

#TODO:  Create view needs correction

#TODO:  CRUD (create, read, update, delete) for each entry
