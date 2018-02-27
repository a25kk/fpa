# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from fpa.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of fpa.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if fpa.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('fpa.buildout'))

    def test_uninstall(self):
        """Test if fpa.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['fpa.buildout'])
        self.assertFalse(self.installer.isProductInstalled('fpa.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IFpaBuildoutLayer is registered."""
        from fpa.buildout.interfaces import IFpaBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IFpaBuildoutLayer in utils.registered_layers())
