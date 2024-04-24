from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def Levels(data):
	Log("Levels postvalidator ...")
	for levelId in data.levels:
		level = data.levels[levelId]
		level.validate()

		if level.levelSceneIds != None:
			levelSceneId = level.levelSceneIds[0]
			levelScene = data.levelScenes[levelSceneId]
			__Check.IsTrue(levelScene.fanTransitionPath == None, 'Level <%s> - first level scene cannot have a fan transition' % levelId)

__validators = [Levels]
