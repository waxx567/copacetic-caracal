from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # Link a table to another table
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # CASCADE: if the agent is deleted, delete the lead

class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)