#!/bin/sh
I18NDUDE=i18ndude
I18NPATH=src/collective/sitelogo
DOMAIN=collective.sitelogo
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --create $DOMAIN $I18NPATH
$I18NDUDE sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/plone.pot --create plone $I18NPATH/profiles
$I18NDUDE sync --pot $I18NPATH/locales/plone.pot $I18NPATH/locales/*/LC_MESSAGES/plone.po
