from rest_framework import serializers
from.models import *




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"



class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


    
class NewsTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTeam
        fields = "__all__"



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"



class SendPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendPost
        fields = "__all__"



class SendVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendVideo
        fields = "__all__"