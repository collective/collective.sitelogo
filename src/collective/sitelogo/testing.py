# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

PROJECTNAME = 'collective.sitelogo'
PROFILE_ID = '{0}:default'.format(PROJECTNAME)


class Fixture(PloneSandboxLayer):

    """
    This layer is the Test class base.

    Check out all tests on this package:

    ./bin/test -s collective.sitelogo --list-tests
    """

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.sitelogo
        self.loadZCML(package=collective.sitelogo)

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'collective.sitelogo')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.sitelogo:default')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'collective.sitelogo')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='collective.sitelogo:Integration'
)

"""
We use this for functional integration tests. Again, we can put basic
common utility or setup code in here.
"""
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='collective.sitelogo:Functional'
)

"""
We use this for functional integration tests with robot framework. Again,
we can put basic common utility or setup code in here.
"""
ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.sitelogo:Robot',
)
