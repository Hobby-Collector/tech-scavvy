from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Match(models.Model):
  name = models.CharField(max_length=100)
  judge = models.ForeignKey(User, on_delete=models.CASCADE)
  def get_absolute_url(self):
    return reverse('detail', kwargs={'match_id': self.id})
  def __str__(self):
    return f"name is: {self.name} and judge is: {self.judge}"



class MatchAndWinner(models.Model):
  match = models.ForeignKey(Match,on_delete=models.CASCADE)
  winner = models.BooleanField(default='False')

class Team(models.Model):
  team_name = models.CharField(max_length=100)
  matchAndWinner = models.ForeignKey(MatchAndWinner,on_delete=models.CASCADE, default = None)
  ready = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.team_name}"

  def get_absolute_url(self):
    return reverse('teams_create')
  
  

class Player(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  # designates team leader can only be one per team
  leader = models.BooleanField(default='False')

  def __str__(self):
    return f"{self.name} on team {self.team}"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'player_id': self.id})


# this is to allow the task to have multiple teams attached to it and each of those teams is attached to the task
class whoAndWhat(models.Model):
  complete = models.BooleanField(default=False)
  # this is unique so a team can only be on a task once
  team = models.ForeignKey(Team,on_delete=models.CASCADE)

class Task(models.Model):
  task = models.CharField(max_length=250,unique=True)
  whoAndWhat = models.ManyToManyField(whoAndWhat)
  match = models.ForeignKey(Match, on_delete=models.CASCADE)
  # this allows us to know the order of the tasks and programatically work on them in that order
  task_number = models.IntegerField(default=-1)

  def new_game_reset(self):
    # needs to also reset the whoAndWhats 
    self.task_number = -1


class Photo(models.Model):
    url = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for task_id: {self.task_id} @{self.url}"