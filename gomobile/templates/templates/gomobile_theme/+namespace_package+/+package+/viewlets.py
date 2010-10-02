"""

   This module contains all viewlet overrides and new viewlets
   for the mobile theme. 
   
   For more information about how to deal with Grok viewlets see
   
   * http://vincentfretin.ecreall.com/articles/creating-a-viewlet-with-grok
   
   * http://grok.zope.org/doc/current/reference/directives.html

"""

__author__ = "${author} <${author_email}>"
__docformat__ = "epytext"
__license__ = "${license_name}"

from zope.component import getMultiAdapter

from zope.interface import Interface

from five import grok

from gomobiletheme.basic import viewlets as base
from gomobile.mobile.interfaces import IMobileImageProcessor

from ${namespace_package}.${package} import MessageFactory as _

# Layer for which against all our viewlets are registered
from interfaces import IThemeLayer

# Viewlets are on all content by default.
grok.context(Interface)

# Use templates directory to search for templates.
grok.templatedir('templates')

# Viewlets are active only when gomobiletheme.basic theme layer is activated
grok.layer(IThemeLayer)

grok.viewletmanager(base.MainViewletManager)

class Logo(base.Logo):
    """ Render site logo with link back to the site root.

    Logo will be automatically resized in the case of
    the mobile screen is very small.
    """

    def getLogoPath(self):
        """ Use Zope 3 resource directory mechanism to pick up the logo file from the static media folder registered by Grok """
        return "++resource++${namespace_package}.${package}/logo.png"
