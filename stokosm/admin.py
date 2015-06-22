from django.contrib import admin
from django import forms
from stokosm.models import Goal, Project, Requirement, Connection, Link, Node

class ConnectionInline(admin.TabularInline):
  model = Connection
  extra = 1
  readonly_fields = ('name',)
  def save_model(self, request, obj, form, change):
    if ((obj.goal1 is not None) & (obj.goal2 is not None)):
      obj.name = obj.goal1.name + "-" + obj.goal2.name
    elif ((obj.requirement1 is not None) & (obj.requirement2 is not None)):
      obj.name = obj.requirement1.name + "-" + obj.requirement2.name
    elif ((obj.project1 is not None) & (obj.project2 is not None)):
      obj.name = obj.project1.name + "-" + obj.project2.name
    else:
        raise Exception("Need to select two nodes of the same type for connection")
    obj.save()

class ProjectLinkInline(admin.TabularInline):
  fk_name = "project"
  model = Link
  extra = 1
  readonly_fields = ('name',)
  def save_model(self, request, obj, form, change):
    if (obj.goal is not None):
      obj.name = obj.project.name + "-" + obj.goal.name
    elif (obj.requirement is not None):
      obj.name = obj.project.name + "-" + obj.requirement.name
    else:
        raise Exception("Need to select two nodes for connection")
    obj.save()

class GoalConnectionInline(ConnectionInline):
  fk_name = "goal1"

class RequirementConnectionInline(ConnectionInline):
  fk_name = "requirement1"

class ProjectConnectionInline(ConnectionInline):
  fk_name = "project1"

class GoalAdmin(admin.ModelAdmin):
  inlines = [GoalConnectionInline, ]

class RequierementAdmin(admin.ModelAdmin):
  inlines = [RequirementConnectionInline, ]

class ProjectAdmin(admin.ModelAdmin):
  inlines = [ProjectConnectionInline,
    ProjectLinkInline, ]

class ConnectionAdmin(admin.ModelAdmin):
  readonly_fields = ('name',)

  def save_model(self, request, obj, form, change):
    if ((obj.goal1 is not None) & (obj.goal2 is not None)):
      obj.name = obj.goal1.name + "-" + obj.goal2.name
    elif ((obj.requirement1 is not None) & (obj.requirement2 is not None)):
      obj.name = obj.requirement1.name + "-" + obj.requirement2.name
    elif ((obj.project1 is not None) & (obj.project2 is not None)):
      obj.name = obj.project1.name + "-" + obj.project2.name
    else:
        raise Exception("Need to select two nodes of the same type for connection")
    obj.save()

class LinkAdmin(admin.ModelAdmin):
  readonly_fields = ('name',)

  def save_model(self, request, obj, form, change):
    if (obj.goal is not None):
      obj.name = obj.project.name + "-" + obj.goal.name
    elif (obj.requirement is not None):
      obj.name = obj.project.name + "-" + obj.requirement.name
    else:
        raise Exception("Need to select two nodes for connection")
    obj.save()


admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Link, LinkAdmin)

admin.site.register(Goal, GoalAdmin)
admin.site.register(Requirement, RequierementAdmin)
admin.site.register(Project, ProjectAdmin)
