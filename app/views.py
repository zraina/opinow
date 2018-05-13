from django.shortcuts import render, redirect
from .models import Pano
from .models import Tour
from .models import Scene
from .forms import PanoForm
from .forms import TourForm
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_email.html', {})

def log_out(request):
    return render(request, 'registration/logged_out.html', {})

def dashboard(request):
    pano = Pano.objects.all()
    tour = Tour.objects.all()
    return render(request, 'app/dashboard.html', {'pano':pano, 'tour': tour})

def view(request, key_id):
    pano_k = Pano.objects.get(key=key_id)
    return render(request, 'app/view.html', {'pano_k':pano_k})

def viewer(request):
    return render(request, 'app/viewer.html', {})

def scenes(request, id):
    sc = Tour.objects.get(id=id)
    scen = Scene.objects.all()
    if request.method == 'POST' and request.FILES['file']:
        title = request.POST['title']
        caption = request.POST['caption']
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        s = Scene(scene_title=title, scene_caption=caption, scene_url=uploaded_file_url, tour=id)
        s.save()
        return render(request, 'app/scenes.html', {'sc':sc, 'scen':scen, 'uploaded_file_url':uploaded_file_url})
    else:
        return render(request, 'app/scenes.html', {'sc':sc, 'scen':scen})

def panorama(request):
    if request.method == 'POST':
        form = PanoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PanoForm()
    return render(request, 'app/panorama.html', {'form': form})

def tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TourForm()
    return render(request, 'app/tour.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
