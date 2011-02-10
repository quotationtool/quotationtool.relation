import unittest
import doctest
import zope.component
from zope.component.testing import setUp, tearDown, PlacelessSetup
from zope.configuration.xmlconfig import XMLConfig

import quotationtool.relation


def testZCML(test):
    """
        >>> XMLConfig('configure.zcml', quotationtool.relation)()

    """

def setUpSome(test):
    """ There are subscribers that need intid in the dependencies
    (zope.catalog)"""
    import zope
    # some dependencies
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.security)()
    XMLConfig('meta.zcml', zope.securitypolicy)()
    
    XMLConfig('configure.zcml', zope.component)()
    XMLConfig('configure.zcml', zope.security)()
    XMLConfig('configure.zcml', zope.site)()
    XMLConfig('configure.zcml', quotationtool.site)()
    # subscribers
    from quotationtool.site.interfaces import INewQuotationtoolSiteEvent
    zope.component.provideHandler(
        quotationtool.relation.createRelationCatalog,
        adapts=[INewQuotationtoolSiteEvent])


class SiteCreationTests(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super(SiteCreationTests, self).setUp()
        XMLConfig('configure.zcml', quotationtool.relation)()
        
    def test_CatalogCreation(self):
        from zope.container.btree import BTreeContainer
        from quotationtool.site.site import QuotationtoolSite
        root = BTreeContainer()
        root['site'] = site = QuotationtoolSite()
        from zc.relation.interfaces import ICatalog
        cat = zope.component.queryUtility(
            ICatalog,
            context = site, 
            default = None)
        self.assertTrue(cat is not None)


def test_suite():
    return unittest.TestSuite((
            doctest.DocTestSuite(setUp = setUp, tearDown = tearDown),
            doctest.DocFileSuite('README.txt',
                                 setUp = setUp,
                                 tearDown = tearDown),
            unittest.makeSuite(SiteCreationTests),
            ))
