from django.urls import path
from.views import *

urlpatterns = [
    path('get-category/', GetCategory.as_view()),
    path('get-author/', GetAuthor.as_view()), 
    path('get-posts/', GetPosts.as_view()),
    path('get-postsid/', GetPostsid.as_view()),
    path('get-popularposts/', GetPopularPosts.as_view()),
    path('get-video/', GetVideo.as_view()),
    path('get-related/', GetRelated.as_view()),
    path('get-aboutus/', GetAboutUs.as_view()),
    path('get-newsteam/', GetNewsTeam.as_view()),
    path('post-contactus/', GetContactUs.as_view()), 
    path('post-sendpost/', GetSendPost.as_view()),
    path('post-sendvideo/', GetSendVideo.as_view())
 ]