"""
Date: 23rd April 2015
Author: Anthony Dempsey

Description:
    This module holds the database tables for a simple poll app.

    This file is created from the django tutorials.
"""
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    """
    Database table for Questions.

    This table holds questions and their publication dates
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
            Check if the question was published in the last day.

            Return: Boolean
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    """
    Database table for Choices.

    This holds the possible answers to a question
    """
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
