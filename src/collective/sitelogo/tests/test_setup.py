# -*- coding: utf-8 -*-

""" This is an integration "unit" test. """

from collective.sitelogo.testing import INTEGRATION_TESTING
from collective.sitelogo.testing import PROFILE_ID
from collective.sitelogo.testing import PROJECTNAME

# from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

import unittest

DEPENDENCIES = [
    'Products.CMFPlone',
    'plone.formwidget.namedfile',
]


class BaseTestCase(unittest.TestCase):
    """ Base test case to be used by other tests. """

    layer = INTEGRATION_TESTING

    profile = PROFILE_ID

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.p_properties = self.portal['portal_properties']
        self.wt = self.portal['portal_workflow']
        self.st = self.portal['portal_setup']


class InstallTestCase(BaseTestCase):
    """ Ensure product is properly installed. """

    def test_installed(self):
        """ This method test the default GenericSetup profile of this package. """
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        """ This method test that dependencies products are installed of this package. """
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)

        self.assertTrue(
            result,
            'These dependencies are not installed: ' + ', '.join(result)
        )

    def test_version(self):
        """ This method test that last version for profile of this package. """
        self.assertEqual(
            self.st.getLastVersionForProfile(PROFILE_ID), (u'1',))


class UninstallTestCase(BaseTestCase):
    """ Ensure product is properly uninstalled. """

    def setUp(self):
        BaseTestCase.setUp(self)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        """ This method test the uninstall GenericSetup profile of this package. """
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_uninstalled(self):
        """ This method test that dependencies products are uninstalled. """
        pass
