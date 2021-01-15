from django.shortcuts import render, redirect
from .forms import Form_Poll
from .models import db
from django.http import HttpResponse


# Homepage


def home(request):
    store = db.objects.all()
    context = {'store': store}
    return render(request, 'Poll/home.html', context)
# create a new poll question


def create(request):
    if request.method == "POST":
        form = Form_Poll(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = Form_Poll()
    context = {'form': form}
    return render(request, 'Poll/create.html', context)
# vote for poll questions


def vote(request, poll_id):
    store2 = db.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['store2']
        if selected_option == 'option1':
            store2.poll_option1_count += 1
        elif selected_option == 'option2':
            store2.poll_option2_count += 1
        elif selected_option == 'option3':
            store2.poll_option3_count += 1
        elif selected_option == 'option4':
            store2.poll_option4_count += 1
        else:
            return HttpResponse(404, "Invalid Form")
        store2.save()
        return redirect('results', poll_id)
    context = {'store2': store2}
    return render(request, 'Poll/vote.html', context)
# results of vote


def results(request, poll_id):
    store3 = db.objects.get(pk=poll_id)
    context = {'store3': store3}
    return render(request, 'Poll/results.html', context)
