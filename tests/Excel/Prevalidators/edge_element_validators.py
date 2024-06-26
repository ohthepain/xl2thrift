from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def EdgeElements(data):
	Log("EdgeElements prevalidator ...")
	if hasattr(data, 'edgeElements'):
		for edgeElementId in data.edgeElements:
			edgeElement = data.edgeElements[edgeElementId]
			__Check.Contains(data.skillStatProfiles, edgeElement.skillStatProfileId, 'EdgeElement <%s>: skillStatProfile <%s> does not exist' % (edgeElement.edgeElementId, edgeElement.skillStatProfileId))
			__Check.Contains(data.effectLists, edgeElement.collisionEffectListId, 'EdgeElement <%s>: undefined Collision Effect List Id <%s> does not exist' % (edgeElement.edgeElementId, edgeElement.collisionEffectListId))
			__Check.PrefabAssetExists(edgeElement.controllerPath, 'Edge element <%s>' % edgeElementId)
			__Check.PrefabAssetExists(edgeElement.effectPath, 'Edge element <%s>' % edgeElementId)
			__Check.ImageAssetExists(edgeElement.heroBadgePath, 'Edge element <%s>' % edgeElementId)
			if edgeElement.appearSoundId != None:
				__Check.SoundExists(edgeElement.appearSoundId, 'Edge element <%s>' % edgeElementId)
			if edgeElement.launchSoundId != None:
				__Check.SoundExists(edgeElement.launchSoundId, 'Edge element <%s>' % edgeElementId)

__validators = [EdgeElements]
