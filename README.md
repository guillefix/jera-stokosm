# jera-specs
Specs created for Jera in Checkvist. CC BY-NC license. Jera was in reality a bigger enterprise than what it's found here. To distinguish them this should be refered to as Jera Community Platform, also code-named 'stokosm' (from greek στόχος (aim) and κόσμος (order)).

This is an idea called Jera. Ignore the "Community v1" as it's an old version. Also, I would check the "Data structure" section first to get an idea of what it is about. The overarching idea, reached after a lot of discussions and brain storming, is that the objective of the platform is to facilitate the purposeful creative process; and that this is divided in three main aspects:

*Identifying the things that people want (i.e. specific goals"to
improve society),
*Finding ways of achieving these goals (through
projects), and
*Identifying and organizing the requirements of these projects.

These correspond to the main data types, and each of them can be further sub-organized into categories, via tags (like transportation, health, IT, etc.), although these don't give the main structure (they are actually ancillary) to the system, but connections. So the proper way to implement a typical structure is to have a big goal called "Improving transportation" with a lot of children goals (more details about the type of connections in the document).

The important thing is that people should find what they are looking for as readily as possible. However, most people don't know what to look for other than "improve the world", so having a way to explore ideas is useful. That is why we put a lot of emphasis on connections between ideas (which was inspired by some other guys working on something called "Rhizi" as well as a set of idea tools like this one: http://hackathonideas.tk/).

People exploring the "goals section", whether in "list view" or "graph view", would be able to find the goals people are more interested in, as well as related goals. They will then find projects that people are proposing/working on to solve that goal, and also find the requisites that that project is looking for. Maybe they will even offer themselves for help if they have that requisite (could be a skill).

Some other user could be exploring the "requisites section" directly, to look for things to help in, if they had a certain skill/resource they wanted to offer/use. They could even filter the requisites for requisites used for projects that are aimed to solving a certain goal, or goals.

Basically, what we tried to design is the best way in which people with the intention of improving the world could find what they wanted to, no matter from which angle they came.

For each of the "goals", "projects", "requisites", there is a corresponding page that holds information about it, as well as a "newsfeed" (a name that maybe isn't that good, as it reminds me of Facebook's) that basically has the "blog" and "discussion" features you talk about for the creative process (I actually put this "blog" and "discussion" features separately but a friend said maybe it's best together, although I am not convinced).

So that people that want to discuss about a certain goal, will go to that goal's page (which will load the "newsfeed"/thread page) by default, and they will post a new thread, like in a forum, or they will search for threads (sorted by date or vote-ranking), and discuss in it etc.

That should give an idea of what this is. The details are below

# Community Specification #

## Top bar

### Links

Campaign

Community

Active projects

User profile

## Community v1

### News Feed

Display news, actions and posts from things and people you follow.

Comments side bar

- Appears when clicking a newsfeed element

### Project/Idea explorer

Categories

- Goals
- Projects
- Requirements ("Cogs")

Graph View

- Connection Rules
  - IntraCategory Connections
    - Hierarchical Connections (Parent/Child)
    - **Child Node** is contained within a **Parent Node** if they have a single Parent relationship.
    - **Child Node** related to 2 or more **Parent Nodes** lies outside both parents but is connected by lines.
  - CrossCategory Connections
    - Non-Hierarchical
    - Traced between **Goals** and **Projects**
      - A single **Project** can be connected to one or more Parent/Child **Goals**
    - Traced between **Projects** and **Requirements**
      - A single **Project** can be connected to one or more Parent/Child **Goals**
- Filtering/Search Rules
  - Double Click/Drag-n-Drop on Node applies Filter to Intracategory and InterCategory views.
  - Restricts view to nodes directly connected to the filter term/node.
  - Keyword filtering/search
    - Keyword/Tag Search in **section search bar** which is on the graph/list view. This search bar can also be selected by pressing Ctrl+F
- Views
  - Single Category
  - Goal+Project View
  - Global View (Goals+Projects+Requirements)
- Display Rules
  - Minimum Node Display Size (So new nodes may appear upon zooming)
  - Maximum Connections (10 highest ranking)
    - Maybe there's a way to navigate through further connections, maybe some "More connections" button will display the next 10 connections under the ranking.
  - Node Size dependent on **Ranking**
- Ranking Rules
  - Newest
  - Trending (Growth speed) TBC
  - Popularity (Average Rating) (Maybe, takes into account rating of children nodes) TBC
- Actions
  - Choose Ranking system
    - The kind of ranking is selected from a drop-down menu on the top.
  - New Connections
    - Initiated by Drag-n-Drop across any node.
      - Drag existing node to another existing node establishes connection. For interCategory connections see Actions->New Project.
      - Drag existing node to empty space establishes connection to a new node in destination space. This will prompt you with an input box to name the new node, unless the new node is in a different category, in which case the New Project page opens (See Actions->New Project).
  - New Goals or Requirements
    - "Add Goal/Requirement" Text Box
    - Can be added to the requirement pool without connections initially.
    - If filter is applied, filtering nodes are automatically connected to new nodes.
  - New Project
    - New Project Submission system
    - Also initiated when making a cross category connection, with the nodes involved in the new connection already included in the "New Project". If making connection to an empty space, obviously only one node will be initially connected to the "New Project".
  - Navigation
    - Left click and drag to pan around
    - Scroll to zoom in and out. A zooming slider is also available.

List view (Default view (TBC))

- Visually, it could be displayed as a list, or as a grid of elements.
- Displays same hierarchy described in "Graph View", by listing children in a sub-branch in a tree-like structure. Elements with more than one parent will appear duplicated (below each parent) in this view.
- Actions
  - Follow Node element
  - Create new Node element
  - All actions in the graph view which are compatible with this view

Wiki/Discussion side-window

- Wiki-like collaborative description of object followed by list of Discussion threads on top division
- Tags of selected object also appear here
- Appears when clicking on a node/object (Goal, Project, Requirement) wether in Graph or List view
- Disappear if clicking outside highlighted node, or if clicking some "back arrow" button.
- Comments for the selected section/discussion thread in bottom division

### User

Profile page

Associated resources and skills (requisites in general)

Short bio/contact info etc.

Projects in which it has participated

Affiliation tags

## Community v2

### The Community/ProjectXplorer webapp

The webapp is mainly structured into a Toolbar, a Main Panel, a Connections Bar, and a Preview Sidebar.

**Toolbar**

- Situated on top
- Contains:
  - **"Sort by" dropdown** (Only when in Newsfeed or Discussion tabs in *Main View* or when in *Connections Explorer*) - Selects from the different kinds of *Ranking* and *sorts* the currently displayed data by it.
  - **Current-Screen Search Box** - Searches (by only showing matching elements) the currently displayed data.
  - "New" menu button. Which opens a menu with:
    - "New Project"
    - "New Goal"
    - "New Requesite"
  - Other elements, dependent on context. Details in the specific place below.
    -  In the *Connections Explorer* only
      - *Filter by* button when having some nodes selected
      - *View switch button* between *Graph View* and *Node View*
    - In the *Newsfeed* only
      - Activity/Posts/Discussions checkboxes to select which to see

**Main Panel**

- Filtering / Search Rules (Several alternatives)
  - **Filtering** restricts view to data elements directly connected to the filter node (See data types and structure). Filtering is done through the *Connections Explorer*.  
  
A _second alternative_ is that browsing is like folders in *List View*, so that when you double click on a node (or highlight and "Enter" many nodes) you loose previous filtering.  
  
The rest of the specification explores the first alternative
  - Keyword filtering/search
    - Keyword Search in *Current-Screen Search Box* in the *Toolbar*. This search bar can also be selected by pressing Ctrl+F
- **Main view**
  - Section tabs
    - Newsfeed / Discussion
    - Description/Wiki
  - Newsfeed
    - A *sorted* list of *Newsfeed activity*, *Discussion threads*, *Newsfeed posts* which can have associated *Likes*, *Shares* and *Comments*, shown in a social-newtork-like fashion
    - Discussion threads

JeanMiCarter's note: I think this should be merged into newsfeed. The Newsfeed effectively contains everything that the current filter status allows. And you can have a big entry bar at the top to enter either a simple post or a question/beginning of a discussion thread. So in the newsfeed you can see new discussions appear as they are started. There should simply be a filter round the top to display only events/questions(discussions)/user status updates/comments or any combination of these.  
guillefix's note: Ok, yeah.  

      - Each discussion thread can be opened if clicked on, and is composed of *discussion thread posts*, working similarly to a forum.
      - Actions
        - Vote discussion thread up or down (Once per user)
        - Post a new *discussion thread post*
          - If opened to you (as some discussion threads may be private)
        - Open a new *discussion thread* (Button in *Toolbar*) - Will open the *New discussion thread page*
        - Edit a *discussion thread post* - Requires certain priviledges
    - Actions
      - Make a new *Newsfeed post* using the New post box (TBC)
      - Like, Share or Comment on a Newsfeed post or activity.
  - Description/Wiki
    - Features:
      - The Wiki *Document* will have, as its base, the same features as a Wiki.
      - A Requisites Plug-in which will automatically create a list of the requisites and allow to say if they have them, or if they are looking for them. It allows to add little description space for each requisite, in which it can also say how it is planned to be gotten. People can comment on these  to offer the requisite if they have them, for example.
      - Other **Project Management Plugins** which should be researched.
    - Wiki-like collaborative (moderated) description of *Projects*, *Goals* and *Requesites*.
    - It is structured in **sections**. Each of these sections can be connected to any number of *Goals*, *Projects* and *Requesites*, effectively working like tags. They also have one *Parent Node*, which is the *Node* with to which they primarily belong.
    - The *sections* are structured by the editing users. They only have a definite structure relative to other *sections* of the same *Parent node*. The (well-structured) document formed by all the sections with the same *Parent node* is called the *Node Document*
    - Sections have comments, initially, contracted which can be expanded to read.
    - Display Rules
      - The document will be grouped in **groups** corresponding to the same *Parent Node*. The structure within a *group* is defined by the *Node Document*. The *groups* themselves are sorted by showing first the *Parent Node* corresponding to the last *Node Document* visited, if any. The rest of *groups* are sorted by their *Parent Node*, according to the *sorting*.
      - If you are filtering only through one *Node*, this opens the **Node Document View**, in which the group corresponding to it is shown first. In this view, all the information about the project is shown, even some *other information* which isn't a *Wiki/Description section*
    - Actions
      - Edit (Button in *Toolbar*) - Requires certain privileges. Only the *Node Document* can be edited.
      - Add comment to a section - Requires less or no privileges.
- **Connections Explorer** (a.k.a. **Expanded Connections Bar**, a.k.a. **Quest Explorer** or **QXplore**)
  - A webapp to navigate and explore the data in the *Quest Explorer Categories*, which include individual data (**Nodes**) and **Connections**.
  - **List View**
    - Contains three (scrollable column) sections:
      - Goals
      - Projects
      - Requesites
    - Display Rules
      - Filtering elements are shown on top and highlighted in a different colour
      - The relationship (parent/child) of the filtering elements with the highlighted element is shown as an indentation of the filtering elements (To the left if parent; to the right if child) if the highlighted element isn't a filtering element. If you highlight a filtering element, all the rest indent to show the relation. If none, or more than one elements are highlighted this isn't shown.
    - Actions
      - New Project
        - *Toolbar->New->New Project* will bring you to the *New Project Submission Page*
        - Also initiated when making a cross category connection, with the nodes involved in the new connection already included in the "New Project".
        - If filter is applied, filtering nodes are automatically connected to new node, as children by default (this is later editable in *New Goal/RequirementSubmission Page*). If no filtering is applied, the goal/requirement is created without connections.
      - New Goals or Requirements
        - *Toolbar->New->New Goal/Requirement* will bring you to the *New Goal/RequirementSubmission Page*
        - If filter is applied, filtering nodes are automatically connected to new node, as children by default (this is later editable in *New Goal/RequirementSubmission Page*). If no filtering is applied, the goal/requirement is created without connections.
      - Highlighting
        - Single left click to *highlight*
        - "Shift"+click to select more than one element
      - Filtering
        - Double click to *filter* by element
        - If more than one *node* is selected, one can click the "Filter by" button, to filter by all of them.
        - Add new *node* to filter by in a textbox at the end of the row in each column
      - New Connections
        - Highlight two nodes
          - If you have two modes selected, the "Create New connection" button on the *Toolbar* will un-grey-out, and if clicked will create a new connection.
          - If the connection is Intra-Category and (thus) hierarchical, there will be a little button to swap the direction of the arrow before clicking the "create New connection" button. By default, the first one you selected will be the *Parent Node*, and the second one the *Child Node*.
  - **Graph View**
    - Contains: A graphical visualization of *Nodes* and *Connections*
    - Views - Switching between them is done through three checkboxes. The nodes of each category are placed on different regions (separated by dotted lines, for example).The allowed views are:
      - Single Category
      - Goal+Project View
      - Project+Requisites View
      - Global View (Goals+Projects+Requirements)
    - Display Rules
      - Connections - They are represented by lines if non-hierarchical, and arrows if hierarchical.
      - Nodes, and nodes within nodes
        - *Child Node* is contained within a *Parent Node* if they have a single Parent relationship.
        - *Child Node* related to 2 or more *Parent Nodes* lies outside both parents but is still connected by arrows.
      - Minimum Node Size for Display (So new nodes may appear upon zooming) - Only nodes up to a certain size will be shown. This size will probably depend on the number of nodes that would appear if that size was chosen. An algorithm will have to be tested to avoid cluttering. I would propose the algorithm choosing the size by the area occupied by the nodes.   
Additionally, cluttering may be avoided by "extending the map" if there are many nodes of the same size, so that exploring would require panning through it.
      - Maximum displayed Connections per node (for e.g., 10 highest in the current *sorting*)
        - Maybe there's a way to navigate through further connections, maybe some "More connections" button will display the next 10 connections under the *sorting*.
      - Node Size dependent on current *sorting*.
    - Actions
      - New Project
        - *Toolbar->New->New Project* will bring you to the *New Project Submission Page*
        - Also initiated when making a cross category connection, with the nodes involved in the new connection already included in the "New Project". If making connection to an empty space, obviously only one node will be initially connected to the "New Project".
        - If filter is applied, filtering nodes are automatically connected to new node, as children by default (this is later editable in *New Goal/RequirementSubmission Page*). If no filtering is applied, the goal/requirement is created without connections.
      - New Goals or Requirements
        - *Toolbar->New->New Goal/Requirement* will bring you to the *New Goal/RequirementSubmission Page*
        - If filter is applied, filtering nodes are automatically connected to new node, as children by default (this is later editable in *New Goal/RequirementSubmission Page*). If no filtering is applied, the goal/requirement is created without connections.
      - New Connections
        - Method 1: Drag-n-Drop across any node.
          - Drag existing node to another existing node establishes connection. For interCategory connections see Actions->New Project.
          - Drag existing node to empty space establishes connection to a new node in destination space. This will prompt you with an input box to name the new node, unless the new node is in a different category, in which case the New Project page opens (See Actions->New Project).
        - Method 2: Highlight two nodes
          - If you have one node highlighted, and you highlight another one (single click) while having "Shift" pressed, you will be prompted by a pop up, asking you if you want to create a new connection between the two nodes.
          - If the connection is Intra-Category and (thus) hierarchical, there will be a little button to swap the direction of the arrow. By default, the first one you selected will be the *Parent Node*, and the second one the *Child Node*.
      - Single click to *highlight*
      - Double click to *filter* by element
      - Navigation
        - Left click and drag to pan around
        - Scroll to zoom in and out. A **zooming slider** is also available.
- User Profile Page

**Connections Bar**

- Situated on the bottom
- Shows a truncated version of the List View of the Connections Explorer (Keeping the three column format, but listing horizontally to reduce space)
- Actions
  - Can navigate the list via two small arrows in the side of each column
  - Single and double click perform same actions than in the expanded view
  - Click an upwards arrow button to expand to the *Expanded Connections Bar*
  - Add new *node* to filter by in a textbox at the end of the row in each column

**Preview Sidebar**

- Situated on the right. C.f. Wikipedia's
- Shows a summary of a node when highlighted.

### Data types and structure

**Quest Explorer Categories**

- **Goals**
- **Projects**
- **Requirements**

Other data types

- Newsfeed data
  - Newsfeed activity
  - Newsfeed post (TBC)
  - Discussion thread
    - Discussion thread post
- Description/Wiki section
- Comments and Likes

Ranking/Sorting

- **Ranking**
  - Types
    - Newest
    - Trending (Growth speed) TBC
    - Popularity (Average Rating) (Maybe, takes into account rating of children nodes) TBC
  - Applies to: Newsfeed data, Discussion threads, QXplore data
- The **sorting** is the name for the ordering in one instance of the app, which is done with one the three rankings. It is chosen through the *"Sort by" dropdown*

Connections

- Intra-Category Connections
  - Hierarchical Connections (**Parent Node** -> **Child Node**)
- Cross-Category Connections
  - Non-Hierarchical
  - Traced between *Goals* and *Projects*
    - A single **Project** can be connected to one or more Parent/Child **Goals**
  - Traced between *Projects* and *Requirements*
    - A single **Project** can be connected to one or more Parent/Child **Goals**
- Other connections
  - The data types *Newsfeed data*, *Discussion thread* and *Description/Wiki section* can be (unhierachically) connected with *Nodes* (data from the *Quest Explorer Categories*)
    - *Description/Wiki sections* should be connected to at least one *Node*. And one and only one of the nodes should have the status of the *Parent Node*.
  - *Newsfeed data* can be connected to *Comments*, *Likes* and *Users*
  - *Users* can be connected to *Discussion thread posts*, *Projects*, and *Newsfeed data*

User data

- Profile data
- Priviledges
- Following Nodes

### New _____ page

Register page

New Project/Goal/Requesite Submission Page

New discussion thread page
