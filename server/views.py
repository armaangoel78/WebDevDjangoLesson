from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as dt

@csrf_exempt
def home(request):
    return JsonResponse("Hello World!", safe=False)

@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category = Category(title=data['name'])
        category.save()
        return JsonResponse("Created category: " + str(data['name']), safe=False)

@csrf_exempt
def get_categories(request):
    if request.method == "GET":
        data = [category.to_dict() for category in Category.objects.all()]
        return JsonResponse(data, safe=False)

@csrf_exempt
def write_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post(title=data['title'], content=data['content'], datetime=dt.now())

        if 'category' in data:
            post.category = Category.objects.get(id=int(data['category']))

        post.save()
        return JsonResponse("Created post: " + str(data['title']), safe=False)

@csrf_exempt
def get_posts(request):
    if request.method == "GET":
        data = [post.to_dict() for post in Post.objects.all()]
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_post(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)
        to_dict = post.to_dict()
        return JsonResponse(to_dict)












