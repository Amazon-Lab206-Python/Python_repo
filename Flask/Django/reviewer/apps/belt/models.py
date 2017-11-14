# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models

class UserManager(models.Manager):
    
    def login(self, POST):
        errors = []
        if len(POST['email']) == 0:
            errors.append('Please enter a valid email')
        if len(POST['password']) == 0:
            errors.append('Please enter a valid password')
        if len(User.objects.filter(email = POST['email'])) < 1 or not bcrypt.checkpw(POST['password'].encode(), User.objects.get(email = POST['email']).password.encode()):
            errors.append('wrong email and password combo')
        if len(errors) > 0:
            return (False, errors) # return the list of errors
        else:
            return (True, errors)

    def validate(self, POST):
        errors = []
        if len(POST['name']) == 0:
            errors.append('First Name is required')
        if len(POST['username']) == 0:
            errors.append('Username is required')
        if len(User.objects.filter(username = POST['username'])) > 0:
            errors.append('Username already in use')
        if len(POST['email']) == 0:
            errors.append('Email is required')
        if len(POST['password']) == 0:
            errors.append('Password is required')
        if POST['password'] != POST['confirm_password']:
            errors.append('Passwords do not match')
        # user_check = User.objects.get(email = POST['email'])
        if len(User.objects.filter(email = POST['email'])) > 0:
            errors.append('duplicate email')
        # if len(user_check) == 0:
        if len(errors) > 0:
            return (False, errors) # return the list of errors
        else:
            # save the information
            new_user = User.objects.create(
                name = POST['name'],
                username = POST['username'],
                email = POST['email'],
                password = bcrypt.hashpw(POST['password'].encode(), bcrypt.gensalt()),
            )
            # then what?
            return (True, new_user)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return '<User object: {} {} {} {}>'.format(self.name, self.username, self.email, self.password)
