from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
#from django.db.transaction import set_autocommit
#from django.template import	RequestContext, loader

from .models import Node, Goal, Requirement, Project, Connection, Link

from .forms import GoalForm, RequirementForm, ProjectForm, GoalConnectionForm, RequirementConnectionForm, ProjectConnectionForm, RequirementLinkForm, GoalLinkForm, ProjectLinkForm

def index(request, error_message=""):
	pages = {'goal_page': 1, 'requirement_page': 1, 'project_page': 1, }
	if "goal_page" in request.GET:
		pages["goal_page"] = request.GET.get("goal_page")
	if "requirement_page" in request.GET:
		pages["requirement_page"] = request.GET.get("requirement_page")
	if "project_page" in request.GET:
		pages["project_page"] = request.GET.get("project_page")



	goal_paginator = Paginator(Goal.objects.order_by('-pub_date'), 10)
	requirement_paginator = Paginator(Requirement.objects.order_by('-pub_date'), 10)
	project_paginator = Paginator(Project.objects.order_by('-pub_date'), 10)

	try:
		goals = goal_paginator.page(pages["goal_page"])
		requirements = requirement_paginator.page(pages["requirement_page"])
		projects = project_paginator.page(pages["project_page"])
	except PageNotAnInteger:
		goals = goal_paginator.page(1)
		requirements = requirement_paginator.page(1)
		projects = project_paginator.page(1)
	except EmptyPage:
		goals = goal_paginator.page(goal_paginator.num_pages)
		requirements = requirement_paginator.page(requirement_paginator.num_pages)
		projects = project_paginator.page(project_paginator.num_pages)
	for goal in goals:
		if request.method == 'POST' and ( str(goal.id)+"_vote" in request.POST):
			vote = request.POST.get(str(goal.id)+"_vote")
			if vote == "upvote":
				goal.ranking+=1
				goal.save()
			elif vote == "downvote":
				goal.ranking-=1
				goal.save()
	for requirement in requirements:
		if request.method == 'POST' and ( str(requirement.id)+"_vote" in request.POST):
			vote = request.POST.get(str(requirement.id)+"_vote")
			if vote == "upvote":
				requirement.ranking+=1
				requirement.save()
			elif vote == "downvote":
				requirement.ranking-=1
				requirement.save()
	for project in projects:
		if request.method == 'POST' and ( str(project.id)+"_vote" in request.POST):
			vote = request.POST.get(str(project.id)+"_vote")
			if vote == "upvote":
				project.ranking+=1
				project.save()
			elif vote == "downvote":
				project.ranking-=1
				project.save()

	context = {'goals': goals,
	'requirements': requirements,
	'projects': projects,
	'error_message': error_message}
	return render(request, 'stokosm/index.html', context)

#NODES (DETAIL, CREATE, EDIT)

def detail(request, node_type, node_id):
	if node_type == "goal":
		goal = get_object_or_404(Goal, pk=node_id)
		if request.method == 'POST' and ('delete' in request.POST):
			goal.delete()
			return HttpResponseRedirect(reverse('stokosm:index'))
		if request.method == 'POST' and ('add_connected_goal' in request.POST):
			form = GoalConnectionForm(request.POST)
			if form.is_valid():
				form.save(goal1=goal)
				return HttpResponseRedirect(reverse('stokosm:index'))
		elif request.method == 'POST' and ('add_linked_project' in request.POST):
			form = ProjectLinkForm(request.POST)
			if form.is_valid():
				context = {'goal': goal}
				form.save(context)
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			connections_form = GoalConnectionForm()
			linked_projects_form = ProjectLinkForm()
			context = {'node': goal, 
			'node_type': node_type, 
			'connections_form': connections_form, 
			'linked_projects_form': linked_projects_form}
	if node_type == "requirement":
		requirement = get_object_or_404(Requirement, pk=node_id)
		if request.method == 'POST' and ('delete' in request.POST):
			requirement.delete()
			return HttpResponseRedirect(reverse('stokosm:index'))
		if request.method == 'POST' and ('add_connected_requirement' in request.POST):
			form = RequirementConnectionForm(request.POST)
			if form.is_valid():
				form.save(requirement1=requirement)
				return HttpResponseRedirect(reverse('stokosm:index'))
		elif request.method == 'POST' and ('add_linked_project' in request.POST):
			form = ProjectLinkForm(request.POST)
			if form.is_valid():
				context = {'requirement': requirement}
				form.save(context)
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			connections_form = RequirementConnectionForm()
			linked_projects_form = ProjectLinkForm()
			context = {'node': requirement, 
			'node_type': node_type, 
			'connections_form': connections_form, 
			'linked_projects_form': linked_projects_form}
	if node_type == "project":
		project = get_object_or_404(Project, pk=node_id)
		if request.method == 'POST' and ('delete' in request.POST):
			project.delete()
			return HttpResponseRedirect(reverse('stokosm:index'))
		if request.method == 'POST' and ('add_connected_project' in request.POST):
			form = ProjectConnectionForm(request.POST)
			if form.is_valid():
				form.save(project1=project)
				return HttpResponseRedirect(reverse('stokosm:index'))
		elif request.method == 'POST' and ('add_linked_goal' in request.POST):
			form = GoalLinkForm(request.POST)
			if form.is_valid():
				context = {'project': project}
				form.save(context)
				return HttpResponseRedirect(reverse('stokosm:index'))
		elif request.method == 'POST' and ('add_linked_requirement' in request.POST):
			form = ProjectConnectionForm(request.POST)
			if form.is_valid():
				context = {'project': project}
				form.save(context)
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			connections_form = ProjectConnectionForm()
			linked_goals_form = GoalLinkForm()
			linked_requirements_form = RequirementLinkForm()
			context = {'node': project, 
			'node_type': node_type, 
			'connections_form': connections_form, 
			'linked_goals_form': linked_goals_form, 
			'linked_requirements_form': linked_requirements_form}
	return render(request, 'stokosm/detail/node_detail.html', context)

def create_node(request, node_type):
	if node_type == "goal":
		if request.method == 'POST':
			form = GoalForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = GoalForm()
		return render(request, 'stokosm/create_node.html', {'node_type': node_type, 'form': form})
	if node_type == "requirement":
		if request.method == 'POST':
			form = RequirementForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = RequirementForm()
		return render(request, 'stokosm/create_node.html', {'node_type': node_type, 'form': form})
	if node_type == "project":
		if request.method == 'POST':
			form = ProjectForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = ProjectForm()
		return render(request, 'stokosm/create_node.html', {'node_type': node_type, 'form': form})

def edit_node(request, node_type, node_id):
	node = get_object_or_404(Node, pk=node_id)
	if node_type == "goal":
		if request.method == 'POST':
			form = GoalForm(request.POST, instance=node)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = GoalForm(initial={'name': node.name, 'description': node.description})
	if node_type == "requirement":
		if request.method == 'POST':
			form = RequirementForm(request.POST, instance=node)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = RequirementForm(initial={'name': node.name, 'description': node.description})
	if node_type == "project":
		if request.method == 'POST':
			form = ProjectForm(request.POST, instance=node)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = ProjectForm(initial={'name': node.name, 'description': node.description})
	return render(request, 'stokosm/edit/edit_node.html', {'node': node, 'node_type': node_type, 'form': form})

#CONNECTIONS (DETAIL, EDIT)

def connection_detail(request, connection_id):
	connection = get_object_or_404(Connection, pk=connection_id)
	if request.method == 'POST' and ('delete' in request.POST):
		connection.delete()
		return HttpResponseRedirect(reverse('stokosm:index'))
	return render(request, 'stokosm/detail/connection_detail.html', {'connection': connection})

def edit_connection(request, connection_id):
	connection = get_object_or_404(Connection, pk=connection_id)
	connection_initial = {'name': connection.name, 
	'directed': connection.directed, 
	'direction': connection.direction,
	'description': connection.description}
	if connection.goal1:
		connection_initial['goal1']=connection.goal1
		connection_initial['goal2']=connection.goal2
		if request.method == 'POST':
			form = GoalConnectionForm(request.POST, instance=connection)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = GoalConnectionForm(initial=connection_initial)
	if connection.requirement1:
		connection_initial['requirement1']=connection.requirement1
		connection_initial['requirement2']=connection.requirement2
		if request.method == 'POST':
			form = RequirementConnectionForm(request.POST, instance=connection)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = RequirementConnectionForm(initial=connection_initial)
	if connection.project1:
		connection_initial['project1']=connection.project1
		connection_initial['project2']=connection.project2
		if request.method == 'POST':
			form = ProjectConnectionForm(request.POST, instance=connection)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = ProjectConnectionForm(initial=connection_initial)
	return render(request, 'stokosm/edit/edit_connection.html', {'connection': connection, 'form': form})

#LINKS(DETAIL, LINK)

def link_detail(request, link_id):
	link = get_object_or_404(Link, pk=link_id)
	if request.method == 'POST' and ('delete' in request.POST):
		link.delete()
		return HttpResponseRedirect(reverse('stokosm:index'))
	return render(request, 'stokosm/detail/link_detail.html', {'link': link})

def edit_link(request, link_id):
	link = get_object_or_404(Link, pk=link_id)
	link_initial = {'name': link.name, 
	'project': link.project,
	'description': link.description}
	if link.goal:
		link_initial['goal'] = link.goal
		if request.method == 'POST':
			form = GoalLinkForm(request.POST, instance=link)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = GoalLinkForm(initial=link_initial)
	if link.requirement:
		link_initial['requirement'] = link.requirement
		if request.method == 'POST':
			form = RequirementLinkForm(request.POST, instance=link)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('stokosm:index'))
		else:
			form = RequirementLinkForm(initial=link_initial)
	return render(request, 'stokosm/edit/edit_link.html', {'link': link, 'form': form})


# Create your views here.
