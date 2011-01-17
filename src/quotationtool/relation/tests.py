import unittest
import doctest
from zope.component.testing import setUp, tearDown, PlacelessSetup
from zope.configuration.xmlconfig import XMLConfig

import quotationtool.relation


def testZCML(test):
    """
        >>> XMLConfig('configure.zcml', quotationtool.relation)()

    """

def test_suite():
    return unittest.TestSuite((
            doctest.DocTestSuite(setUp = setUp, tearDown = tearDown),
            doctest.DocFileSuite('README.txt',
                                 setUp = setUp,
                                 tearDown = tearDown),
            ))
