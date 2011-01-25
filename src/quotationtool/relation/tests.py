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
        # we also made sure that there is an IntIds utility:
        from zope.intid.interfaces import IIntIds
        intids = zope.component.queryUtility(
            IIntIds,
            context = site,
            default = None)
        self.assertTrue(intids is not None)


def test_suite():
    return unittest.TestSuite((
            doctest.DocTestSuite(setUp = setUp, tearDown = tearDown),
            doctest.DocFileSuite('README.txt',
                                 setUp = setUp,
                                 tearDown = tearDown),
            unittest.makeSuite(SiteCreationTests),
            ))
