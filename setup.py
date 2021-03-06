from setuptools import setup
from setuptools import find_packages

version = '1.0.3.dev0'

name = "collective.sitelogo"
namespace = ['collective', ]
baseurl = "http://github.com/collective"

setup(
    name=name,
    version=version,
    description="Set the site logo through the web.",
    long_description="{0}{1}".format(
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone viewlet',
    author='Johannes Raggam',
    author_email='johannes@raggam.co.at',
    url='%s/%s' % (baseurl, name),
    license='GPL',
    namespace_packages=namespace,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'Products.CMFPlone',
        'plone.formwidget.namedfile >= 1.0.12'
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
            'plone.app.testing [robot] >=4.2.2',
            'plone.browserlayer',
            'plone.testing',
            'robotsuite',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
