from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, \
     RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView, \
     RetrieveDestroyAPIView 
from.serializer import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, {'error_message': error_message})
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, {'form': form})



class GetCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class GetAuthor(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class GetPosts(ListAPIView):
    queryset = Posts.objects.all()[:3]
    serializer_class = PostsSerializer



class GetPopularPosts(ListAPIView):
    queryset = Posts.objects.all().order_by('-views')
    serializer_class = PostsSerializer



class GetPostsid(ListAPIView):
    queryset = Posts.objects.all().order_by('-id')[:6]
    serializer_class = PostsSerializer



class GetVideo(ListAPIView):
    queryset = Video.objects.all().order_by('-id')[:2]
    serializer_class = VideoSerializer



class GetRelated(ListAPIView):
    category = Category.objects.get(id=1)
    queryset = Posts.objects.filter(category=category)
    serializer_class = PostsSerializer



class GetAboutUs(ListAPIView):
    queryset = AboutUs.objects.last()
    serializer_class = AboutUsSerializer



class GetNewsTeam(ListAPIView):
    queryset = NewsTeam.objects.all()[:6]
    serializer_class = NewsTeamSerializer



class GetContactUs(CreateAPIView):
    queryset = ContactUs.objects.last()
    serializer_class = ContactUsSerializer



class GetSendPost(CreateAPIView):
    queryset = SendPost.objects.last()
    serializer_class = SendPostSerializer



class GetSendVideo(CreateAPIView):
    queryset = SendVideo.objects.last()
    serializer_class = SendVideoSerializer