from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Thought
from .forms import ThoughtCreationForm, ThoughtUpdateForm, ThoughtsListForm


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
        return redirect('commentaries:listall_thoughts')

    return render(request, 'thought_form.html', context)


class ThoughtsListView(ListView):
    # queryset = Thought.objects.all()
    # form_class = ThoughtsListForm
    model = Thought
    # context_object_name = 'thoughts'
    # paginate_by = 5
    template_name = 'thought_list.html'


class ThoughtCreateView(CreateView):
    form_class = ThoughtCreationForm
    # fields = ('title', 'reference', 'verseText', 'body', 'status', 'keyWords')
    template_name = 'thought_form.html'
#TODO:  Create view needs correction

#TODO:  CRUD (create, read, update, delete) for each entry
