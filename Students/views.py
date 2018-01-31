# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import teacher_post
import json
from rest_framework.parsers import JSONParser
from django.core import serializers
import pyrebase

config = {
  "apiKey": "AIzaSyC9XomTqtc82Eg8DAPhPj1D88zx1JB64HE",
  "authDomain": "c-learning-51c36.firebaseapp.com",
  "databaseURL": "https://c-learning-51c36.firebaseio.com",
  "storageBucket": "c-learning-51c36.appspot.com",
  "serviceAccount": "serviceAccountCredentials.json"
}
firebase = pyrebase.initialize_app(config)



# Create your views here.
@csrf_exempt
def insert(request):
    data = JSONParser().parse(request)
    posts= {
        'question' : 'Try again!'
    }
    if request.method == 'POST':
        question_post  = data['question'] 
        questionspost = teacher_post(question= question_post)
        questionspost.save()
        posts = {
            'question' :  question_post
        }
        db = firebase.database()
        db.child("questionId").set(question_post)
    return JsonResponse(posts)

def getall(request): 
    getall = {
         'question' : 'Try again!'
    }
    print "why"
    if request.method == 'GET':
        print "why1"
        questionspost = teacher_post.objects.all()
        data = json.dumps([dict(item) for item in teacher_post.objects.all().values('question')])
        test = json.loads(data)
        
        return JsonResponse(test,safe=False)
    return JsonResponse(getall)

def stuent_anwser(request,id):
    getall = {

         'question' : 'Try again!'
    }




    return JsonResponse(getall)

def view_student_anwser():
    getall = {

       'question' : 'Try again!'
    }




    return JsonResponse(getall)

      
        
