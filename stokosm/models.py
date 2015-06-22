from django.db import models

class GeneralContent(models.Model):
  name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __unicode__(self):    #__str__ in Python3
    return self.name
  class Meta:
    abstract = True

class Node(GeneralContent):
  related = models.ManyToManyField("self", through='Connection', symmetrical=False)
  class Meta:
    abstract = True

class Goal(Node):
  pass

class Requirement(Node):
  pass

class Project(Node):
  linked_goals = models.ManyToManyField(Goal, through='Link', related_name='goals')
  linked_req = models.ManyToManyField(Requirement, through='Link', related_name='requirements')

class Connection(GeneralContent):
  goal1 = models.ForeignKey(Goal, related_name='connections', null=True, blank=True)
  goal2 = models.ForeignKey(Goal, related_name='reverse_connections', null=True, blank=True)
  requirement1 = models.ForeignKey(Requirement, related_name='connections', null=True, blank=True)
  requirement2 = models.ForeignKey(Requirement, related_name='reverse_connections', null=True, blank=True)
  project1 = models.ForeignKey(Project, related_name='connections', null=True, blank=True)
  project2 = models.ForeignKey(Project, related_name='reverse_connections', null=True, blank=True)

  DIRECTION_CHOICES = (
    (0, 'Child'),
    (1, 'Parent')
  )
  direction = models.IntegerField(default=0, choices=DIRECTION_CHOICES)
  directed = models.BooleanField(default=False)

class Link(GeneralContent):
  goal = models.ForeignKey(Goal, null=True, blank=True)
  requirement = models.ForeignKey(Requirement, null=True, blank=True)
  project = models.ForeignKey(Project)
