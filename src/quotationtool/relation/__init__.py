import zope.component
from zope.intid.interfaces import IIntIds
from zope.intid.interfaces import IIntIdAddedEvent, IIntIdRemovedEvent
import zc.relation

from quotationtool.site.interfaces import INewQuotationtoolSiteEvent


def dump(obj, catalog, cache):
    """ Dump an object."""
    intids_ut = cache.get('intids_ut')
    if not intids_ut:
        intids_ut = zope.component.getUtility(IIntIds)
        cache['intids_ut'] = intids_ut
    return intids_ut.getId(obj)

def load(token, catalog, cache):
    """Load an object."""
    intids_ut = cache.get('intids_ut')
    if not intids_ut:
        intids_ut = zope.component.getUtility(IIntIds)
        cache['intids_ut'] = intids_ut
    return intids_ut.getObject(token)


@zope.component.adapter(IIntIdAddedEvent)
def indexSubscriber(event):
    """index an object in the relation catalog """
    cat = zope.component.queryUtility(
        zc.relation.interfaces.ICatalog,
        context = event.object)
    if cat is not None:
        cat.index(event.object)


@zope.component.adapter(IIntIdRemovedEvent)
def unindexSubscriber(event):
    """unindex an object in the relation catalog."""
    cat = zope.component.queryUtility(
        zc.relation.interfaces.ICatalog,
        context = event.object)
    if cat is not None:
        cat.unindex(event.object)


@zope.component.adapter(INewQuotationtoolSiteEvent)
def createRelationCatalog(event):
    """Create a new relation catalog and ensure that there is an IntId
    utility."""
    sm = event.object.getSiteManager()
    from zope.intid.interfaces import IIntIds
    intids = zope.component.queryUtility(
        IIntIds, 
        context = event.object, 
        default = None)
    if intids is None:
        from zope.intid import IntIds
        sm['default']['IntIds'] = intids = IntIds()
        sm.registerUtility(intids, IIntIds)
    sm['default']['RealtionCatalog'] = cat = zc.relation.catalog.Catalog(
        dump, load)
    sm.registerUtility(cat, zc.relation.interfaces.ICatalog)
    
