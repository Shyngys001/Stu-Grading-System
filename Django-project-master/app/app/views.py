from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# noinspection PyUnresolvedReferences
from login.models import Subject
from .forms import AddGrade


def index(request):
    if request.method == 'POST':
        if 'delete_card' in request.POST:
            card_name = request.POST['delete_card']
            Subject.objects.filter(name=card_name).delete()
        else:
            student_name = request.POST['student_name']
            grade = request.POST['grade']
            professor_name = request.POST['professor_name']
            date = request.POST['date']
            observations = request.POST['observations']
            card_name = request.POST['card_name']

            subject = Subject(name=card_name, student=student_name, grade=grade, professor=professor_name, date=date, observations=observations)
            subject.save()

    cards = Subject.objects.order_by('name').values_list('name', flat=True).distinct()
    subjects = Subject.objects.order_by('name')

    return render(request, 'index.html', {'cards': cards, 'subjects': subjects})


def home1(request):
    return render(request, 'index.html')


def home(request):
    user = request.session.get('user', 'Guest')
    subjects = Subject.objects.all()
    d = []

    for subject in subjects:
        if subject.name not in d:
            d.append(subject.name)

    context = {'user': user, 'subjects': subjects, 'd': d}
    return render(request, "home.html", context)

@login_required
def add(request):
    form = AddGrade(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, "add.html", context)


# def delete_card(request, card_id):
#     card = Card.objects.get(id=card_id)
#     card.delete()
#     return redirect('name_of_your_view_that_renders_this_template')