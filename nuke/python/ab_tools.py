############# AB TOOLS TESTING #############

""" Throwing some ideas around, trying to get OOP tools out of our current mltools """

import sys
import os


import shotgun_api3 as shotgun
import sg_globals
import tank




# Putting shotgun global variables into local namespace for easier reading. Bad idea or good idea?


class Project(object):
	""" Project knows how many sequences are within it, initializes said sequence objects """
	def __init__(self):
		super(Project, self).__init__()


		# class global values
		self.projectName = self.findProjectName()
		self.seqDir = 'P:/projects/'+self.projectName+'/sequences'

	def __str__(self):
		return "Project is " + self.projectName


	# class methods

	def findProjectName(self):
		# return name of the project
		projectName = ''
		for p in sys.path:
			if 'nuke' in p and 'scripts' in p and 'projects' in p:
				projectName = p.replace('\\', '/')
		projectName = projectName.split('/')[2]
		return projectName

	def getSeqCount(self, seqDir):
		# return how many sequences in the project
		seqCount = len(os.listdir(seqDir))
		return seqCount

	def getSeqNames(self, seqDir):
		# return list of names of sequences
		seqNames = []
		for i in os.listdir(seqDir):
			seqNames.append(i)
		return seqNames

	def createSeqObjects(self, seqDir):
		allSeqObjects = []
		for x in self.getSeqNames(seqDir):
			



class Sequence(object):
	""" Sequence object knows how many shots are within it, initializes said shots """
	def __init__(self, sequenceName):
		#super(Sequence, self).__init__()
		self.sequenceName = sequenceName
		self.shotDir = self.seqDir+'/shots'


	# class methods

	def getShotCount(self, shotDir):
		shotCount = len(os.listdir(shotDir))
		return shotCount

	def getShotNames(self, shotDir):
		shotNames = []
		for i in os.listdir(shotDir):
			shotNames.append(i)
		return shotNames



class Shot(object):
	""" Shot objects know where shot lives, everything about the shots """
	def __init__(self, arg):
		#super(Shot, self).__init__()
		self.arg = arg
		




# class Shot(object):
# 	"""create a basic shot object, hold variables related to the shot within
# 		variables include:
# 			shot number
# 			assignment
# 			comp status
# 			lighting status
# 			list of publishes
# 			comp notes
# 	"""
# 	def __init__(self, sg_comp_dict, sg_lighting_dict):
# 		super(Shot, self).__init__()
# 		self.sg_comp_dict = sg_comp_dict
# 		self.sg_lighting_dict = sg_lighting_dict



# 	def getCompDict(sg_globals.PROJECT_ID):
#     sg = shotgun.Shotgun(sg_globals.SERVER_PATH, sg_globals.SCRIPT_USER, sg_globals.SCRIPT_KEY)
#     fields = ['id', 'entity', 'code', 'sg_status_list','open_notes','task_assignees','content']
#     filters = [
#                 ['project', 'is', {"type": 'Project', 'id': sg_globals.PROJECT_ID}],
#                     {
#                         "filter_operator": "any",
#                         "filters": [
#                             ['content','is', 'comp'],
#                             #['content','is', 'lighting']
#                         ]
#                     }
#                 ]
#     tasks = sg.find('Task',filters,fields)
#     shotNotes={}
#     shotData={}
#     for t in tasks:
#         name=t['entity']['name']
#         if not name in shotData.keys():
#             shotData[name]=['','','','']
#         if t['content']=='Composite':
#             if len(t['task_assignees']):
#                  shotData[name][0]=t['task_assignees'][0]['name']
#             shotData[name][1]=t['sg_status_list']
#         if t['content']=='Lighting':
#             if len(t['task_assignees']):
#                 shotData[name][2]=t['task_assignees'][0]['name']
#             shotData[name][3]=t['sg_status_list']
#         #only keep comp notes
#         if t['content']=='Composite':
#             notes= t['open_notes']
#             for note in notes:
#                 if not name in shotNotes.keys():
#                     shotNotes[name]=[]
#                 nt=note['name']
#                 noteFormatted=str(note['id'])+'###'+nt.decode("ascii","ignore")
#                 if not noteFormatted in shotNotes[name]:
#                     shotNotes[name].append(noteFormatted)

#     return shotNotes,shotData





# OK so apparently, I was originally working off of a deprecated version of getShotgunData.
# this newer version splits the tasks of querying shotgun off into a few different ways
# and rights everything to a text file called shotData.txt
# after it wrights that shotData.txt, it then parses through it to create the data needed elsewhere.
# I'm not sure why it writes to the text file, because it seems to update and write to it every single time.
# Maybe the text file is being used elsewhere?
#

# if I'm reading this correctly, getShotgunData is called once, which writes out the file, and after that
# the file is manipulated by other commands. So if you do this once, and wreite the key data down, you don't have to
# call those shotgun commands later? Or parse the hard to read dictionaries?



# def getShotgunData(self,*args):
#         import tank
#         PROJECT_ID=tank.platform.current_engine().context.project['id']
#         import shotgun_api3 as shotgun
#         SERVER_PATH = "https://psyop.shotgunstudio.com"
#         SCRIPT_USER = "mlTools"
#         SCRIPT_KEY  = "e0078c0e80f09ee7a76de2c25afce6bd34a5bc601f598d446daf6a8e848d9089"
#         sg = shotgun.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)

#         fields = ['id', 'code','name','tasks']
#         filters = [['project','is', {'type':'Project','id':PROJECT_ID}]]
#         shotsReturn = sg.find('Shot',filters,fields)
#         shots=[]
#         for sr in shotsReturn:
#             tasks=[]
#             for  t in sr['tasks']:
#                 tasks.append(t['id'])
#             shots.append([sr['code'].replace("_",""),sr['id'],sr['code'],tasks])


#         fields = ['id','code', 'sg_status_list','task_assignees','content']
#         filters = [
#             ['project', 'is', {"type": 'Project', 'id': PROJECT_ID}],
#             ]
#         tasks = sg.find('Task',filters,fields)

#         for sh in shots:
#             for t in tasks:
#                 if t['id'] in sh[3]:
#                     idx=sh[3].index(t['id'])
#                     users=[]
#                     for us in t['task_assignees']:
#                         users.append(us['name']+":"+str(us['id']))
#                     users="<USER>".join(users)
#                     sh[3][idx]= [t['content'],t['sg_status_list'],str(t['id']),users]

#         shotDataText=""
#         for sh in shots:
#             taskDataText=[]
#             for tasks in sh[3]:
#                 if tasks[0]:#if task has name
#                     taskDataText.append(",".join(tasks))
#             shotDataText+=sh[0]+","+str(sh[1])+","+sh[2]+"<TASK>"+"<TASK>".join(taskDataText)+"\n"

#         #update notesData for offline
#         fileObject=open(self.shotData,"w")
#         fileObject.write(shotDataText)
#         fileObject.close()

#         shotsData={}
#         for shot in shotDataText.split("\n")[:-1]:
#             tasks=shot.split("<TASK>")
#             info=tasks[0]
#             tasks=tasks[1:]
#             shotName,id,sgName=info.split(",")
#             shotDict={}
#             shotDict['name']=shotName
#             shotDict['shotId']=id
#             shotDict['sgName']=sgName
#             tasksDicts={}
#             for task in tasks:
#                 taskDict={}
#                 taskType,taskStatus,taskId,TaskUser=task.split(",")
#                 taskDict['type']=taskType
#                 taskDict['status']=taskStatus
#                 taskDict['id']=taskId
#                 taskDict['users']=TaskUser.split("<USER>")
#                 tasksDicts[taskType]=taskDict
#             shotDict['tasks']=tasksDicts
#             shotsData[shotName]=shotDict
#         return shotsData