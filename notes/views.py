from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """ Home page for My Diary """
    return render(request, 'notes/index.html')

@login_required
def topics(request):
    """ Get all Topics. """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = { 'topics': topics }
    return render(request, 'notes/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Get topics by id """
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'notes/topic.html', context)

@login_required
def new_topic(request):
    """ Post a topic """
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # Post Data Submitted; Process Data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('notes:topics')
        
    # Display a blank or invalid form
    context = { 'form': form }
    return render(request, 'notes/new_topic.html', context)
    
@login_required
def new_entry(request, topic_id):
    """ Add a new entry to a topic with id 'topic_id' """
    topic = get_object_or_404(Topic, id=topic_id)
    
    if request.method != 'POST':
        # No data; create a blank form
        check_topic_owner(topic, request)
        form = EntryForm()
    else:
        # Post data submitted; process request
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('notes:topic', topic_id = topic_id)
    # Display a blank or invalid form
    context = { 'topic': topic, 'form': form }
    return render(request, 'notes/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry. """
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    
    check_topic_owner(topic, request)
    
    if request.method != 'POST':
        # initial request; pre-fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # Post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:topic', topic_id=topic.id)
    # Display form with entries to be edited
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'notes/edit_Entry.html', context)

def check_topic_owner(topic, request):
    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
