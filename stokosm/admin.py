from django.contrib import admin
from django import forms
from stokosm.models import Goal, Project, Requirement, Connection, Link, Node

def connection_creator(obj):
	if ((obj.goal1 is not None) & (obj.goal2 is not None)):
		obj.name = obj.goal1.name + "-" + obj.goal2.name
		obj2 = Connection(goal1=obj.goal2, goal2=obj.goal1)
		obj2.name = obj.goal2.name + "-" + obj.goal1.name
		if obj.directed:
			obj2.directed = True
			obj2.direction = (obj.direction+1)%2
		else:
			obj2.directed = False
	elif ((obj.requirement1 is not None) & (obj.requirement2 is not None)):
		obj.name = obj.requirement1.name + "-" + obj.requirement2.name
		obj2 = Connection(requirement1=obj.requirement2, requirement2=obj.requirement1)
		obj2.name = obj.requirement2.name + "-" + obj.requirement1.name
		if obj.directed:
			obj2.directed = True
			obj2.direction = (obj.direction+1)%2
		else:
			obj2.directed = False
	elif ((obj.project1 is not None) & (obj.project2 is not None)):
		obj.name = obj.project1.name + "-" + obj.project2.name
		obj2 = Connection(project1=obj.project2, project2=obj.project1)
		obj2.name = obj.project2.name + "-" + obj.project1.name
		if obj.directed:
			obj2.directed = True
			obj2.direction = (obj.direction+1)%2
		else:
			obj2.directed = False
	else:
		raise Exception("Need to select two nodes of the same type for connection")
	obj.save()
	obj2.save()

def link_creator(obj):
	if (obj.goal is not None):
		obj.name = obj.project.name + "-" + obj.goal.name
	elif (obj.requirement is not None):
		obj.name = obj.project.name + "-" + obj.requirement.name
	else:
		raise Exception("Need to select two nodes for connection")
	obj.save()


class ConnectionInline(admin.TabularInline):
	model = Connection
	extra = 1
	readonly_fields = ('name',)

class ProjectLinkInline(admin.TabularInline):
	fk_name = "project"
	model = Link
	extra = 1
	readonly_fields = ('name',)

class GoalConnectionInline(ConnectionInline):
	fk_name = "goal1"
	fields = ['goal2', "direction", "directed", "pub_date"]

class RequirementConnectionInline(ConnectionInline):
	fk_name = "requirement1"
	fields = ['requirement2', "direction", "directed", "pub_date"]

class ProjectConnectionInline(ConnectionInline):
	fk_name = "project1"
	fields = ['project2', "direction", "directed", "pub_date"]


class NodeAdmin(admin.ModelAdmin):

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		
		if formset.model == Connection:
			for instance in instances:
				connection_creator(instance)
		elif formset.model == Link:
			for instance in instances:
				link_creator(instance)
		else:
			return formset.save()

class GoalAdmin(NodeAdmin):
	inlines = [GoalConnectionInline, ]

class RequierementAdmin(NodeAdmin):
	inlines = [RequirementConnectionInline, ]

class ProjectAdmin(NodeAdmin):
	inlines = [ProjectConnectionInline,
	ProjectLinkInline, ]


class ConnectionAdmin(admin.ModelAdmin):
	readonly_fields = ('name',)
	def save_model(self, request, obj, form, change):
		connection_creator(obj)


class LinkAdmin(admin.ModelAdmin):
	readonly_fields = ('name',)
	def save_model(self, request, obj, form, change):
		link_creator(obj)


admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Link, LinkAdmin)

admin.site.register(Goal, GoalAdmin)
admin.site.register(Requirement, RequierementAdmin)
admin.site.register(Project, ProjectAdmin)
