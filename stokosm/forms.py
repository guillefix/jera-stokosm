from django.forms import ModelForm
from stokosm.models import Goal, Requirement, Project, Connection, Link
from admin import connection_creator, link_creator

class GoalForm(ModelForm):
	class Meta:
		model = Goal
		fields = ['name',]

class RequirementForm(ModelForm):
	class Meta:
		model = Requirement
		fields = ['name',]

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['name',]

class GoalConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, goal1=None):
		instance = super(GoalConnectionForm, self).save(commit=False)
		instance.goal1 = goal1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['goal2', 'directed', 'direction']

class RequirementConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, requirement1=None):
		instance = super(RequirementConnectionForm, self).save(commit=False)
		instance.requirement1 = requirement1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['requirement2', 'directed', 'direction']

class ProjectConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, project1=None):
		instance = super(ProjectConnectionForm, self).save(commit=False)
		instance.project1 = project1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['project2', 'directed', 'direction']

class LinkForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, project=None):
		instance = super(LinkForm, self).save(commit=False)
		instance.project = project
		if commit:
			link_creator(instance)
		return instance
	class Meta:
		asbtract = True

class GoalLinkForm(LinkForm):
	class Meta:
		model = Link
		fields = ['goal']

class RequirementLinkForm(LinkForm):
	class Meta:
		model = Link
		fields = ['requirement']