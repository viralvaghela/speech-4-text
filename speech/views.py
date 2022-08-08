import random
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from speech.models import CorrectWord, Paragrap


def index(request):
  return render(request, 'index.html')  # display home page of site


# if user is logged in then allow to visit profile page
@login_required(login_url='index')
def profile(request):
    print(request.user)
    correct_words = CorrectWord.objects.all().filter(user=request.user)
    print(correct_words)

    return render(request, 'profile.html', {'correct_words': correct_words})


def login(request):
    if request.method == 'POST':
        # get data from html from
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user, if user is authenticated then redirect to profile page else return to homepage
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return redirect('index')


def register(request):
    if request.method == 'POST':  # if user submits form then create new user
        name = request.POST['name']  # get data from html from
        email = request.POST['email']  # get data from html from
        password = request.POST['password']  # get password from html

        # create new user and then redirect to profile page
        user = User.objects.create_user(
            username=name, email=email, password=password)
        user.save()
        return redirect('profile')  # redirect to profile page


@login_required(login_url='index')
def practice(request):
    # select all the paragrap from database
    all_paragraphs = Paragrap.objects.all()
    # check the length of all_paragraphs

    random_int = random.randint(0, len(all_paragraphs) - 1)
    title = all_paragraphs[random_int].title
    random_paragraph = all_paragraphs[random_int].text
    # print("Random Paragraph =>>>",random_paragraph)

    return render(request, 'practice.html', {'random_paragraph': random_paragraph, 'title': title})


def submitpoint(request):
    if request.method == 'POST':
        # get data from html from
        username = request.user
        points = request.POST['points']
        correctwords = request.POST['correctwords']
        title = request.POST['title']
        addword = CorrectWord.objects.filter(user=username)
        grade = request.POST['grade']
        if addword is not None:
            print("addword is not None")
            addword = CorrectWord.objects.create(
                user=username, words=correctwords, points=points, title=title, grade=grade)
            addword.save()

        else:
            addword.update(
                user=username, words=correctwords, points=points, title=title, grade=grade)

        return redirect('practice')  # redirect to practice page

# create logout function


def logout(request):
    auth.logout(request)
    return redirect('index')
