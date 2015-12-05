from django.db import models
from django.utils import timezone

class UserCustom(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()


class Risk(models.Model):
    name = models.TextField()
    category = models.TextField()
    description = models.TextField()
    type = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.TextField()
    id_categroy = models.ForeignKey('Category')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    id_owner = models.ForeignKey('UserCustom', related_name='owner')
    members = models.ManyToManyField('UserCustom', related_name='members')
    risks = models.ManyToManyField('Risk', through='RiskProject')
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class RiskProject(models.Model):
    id_project = models.ForeignKey('Project')
    id_risk = models.ForeignKey('Risk')
    probability = models.TextField()
    impact = models.TextField()
    factors = models.TextField()
    reduction = models.TextField()
    supervision = models.TextField()
