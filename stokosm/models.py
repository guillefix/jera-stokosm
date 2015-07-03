from django.db import models
from datetime import datetime

class GeneralContent(models.Model):
  name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published', default=datetime.now)
  def __unicode__(self):    #__str__ in Python3
    return self.name
  class Meta:
    abstract = True

class Node(GeneralContent):
  related = models.ManyToManyField("self", through='Connection', symmetrical=False, related_name='reverse_related')
  description = models.CharField(max_length=2000, blank=True)
  ranking = models.IntegerField(default=0)

class Goal(Node):
  pass

class Requirement(Node):
  pass

class Project(Node):
  linked_goals = models.ManyToManyField(Goal, through='Link', related_name='linked_projects')
  linked_req = models.ManyToManyField(Requirement, through='Link', related_name='linked_projects')

class Connection(GeneralContent):
  description = models.CharField(max_length=2000, blank=True)
  goal1 = models.ForeignKey(Goal, related_name='connections', null=True, blank=True)
  goal2 = models.ForeignKey(Goal, related_name='reverse_connections', null=True, blank=True)
  requirement1 = models.ForeignKey(Requirement, related_name='connections', null=True, blank=True)
  requirement2 = models.ForeignKey(Requirement, related_name='reverse_connections', null=True, blank=True)
  project1 = models.ForeignKey(Project, related_name='connections', null=True, blank=True)
  project2 = models.ForeignKey(Project, related_name='reverse_connections', null=True, blank=True)

  DIRECTION_CHOICES = (
    (0, 'Child'), #goal2 is child of goal1
    (1, 'Parent') #goal2 is parent of goal1
  )
  direction = models.IntegerField(default=0, choices=DIRECTION_CHOICES)
  directed = models.BooleanField(default=False)
  ranking = models.IntegerField(default=0)

class Link(GeneralContent):
  description = models.CharField(max_length=2000, blank=True)
  goal = models.ForeignKey(Goal, related_name="links", null=True, blank=True)
  requirement = models.ForeignKey(Requirement, related_name="links", null=True, blank=True)
  project = models.ForeignKey(Project, related_name="links")
  ranking = models.IntegerField(default=0)
