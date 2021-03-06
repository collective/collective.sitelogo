collective.sitelogo
===================

Set the site logo through the web. Works with ``lineage.registry``, so you can
define site logos for Lineage subsites also.

You have a "Site Logo" menu entry in the user menu and also a configlet in the
``@@overview-controlpanel`` form.

This is a backport of the Plone 5 site logo feature. Also see:
https://github.com/plone/Products.CMFPlone/pull/355

Translations
------------

This product has been translated into

- German (thanks, Johannes Raggam).

- Spanish (thanks, Leonardo J. Caballero G.).

Installation
------------

Install collective.sitelogo by adding it to your buildout: ::

   [buildout]

    ...

    eggs =
        collective.sitelogo


and then running "bin/buildout".

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.sitelogo/issues
- Source Code: https://github.com/collective/collective.sitelogo

License
-------

The project is licensed under the GPLv2.
