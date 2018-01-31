# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class teacher_post(models.Model):
    question = models.CharField(max_length = 100)

    def __str__(self):
        return self.question

class Stdent_anwser(models.Model):
    question = models.ForeignKey(teacher_post,on_delete=models.CASCADE)
    anwser = models.CharField(max_length =100)
    def __str__(self):
        return self.anwser



