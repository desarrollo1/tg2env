# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tw.api import Widget, JSLink, CSSLink

#__all__ = ["JQuery", "JQueryCompressed"]

# declare your static resources here

## JS dependencies can be listed at 'javascript' so they'll get included
## before

jquery_js    = JSLink(modname=__name__,
                      filename=dict(normal='static/javascript/jquery-1.4.2.js',
                                    min='static/javascript/jquery-1.4.2.min.js',
                                    ),
                      javascript=[])
jquery_cookie_js    = JSLink(modname=__name__, filename='static/javascript/jquery.cookie.js', javascript=[jquery_js])
jquery_treeview_js    = JSLink(modname=__name__, filename='static/javascript/jquery.treeview.pack.js', javascript=[jquery_cookie_js])
jquery_treeview_css   = CSSLink(modname=__name__, filename='static/css/jquery.treeview.css')
jquery_dimensions_js    = JSLink(modname=__name__, filename=dict(normal='static/javascript/jquery.dimensions.js',
                                                                 packed='static/javascript/jquery.dimensions.pack.js',
                                                                 min='static/javascript/jquery.dimensions.min.js',
                                                                 ),
                                                                 javascript=[jquery_js])
jquery_bgiframe_js    = JSLink(modname=__name__, filename='static/javascript/jquery.bgiframe.js', javascript=[jquery_js])

#dynacloud_js=JSLink(modname=__name__,filename='static/javascript/jquery.dynacloud-2.pack.js')
#my_css = CSSLink(modname=__name__, filename='static/twtools.css')

class JQuery(Widget):
    template = ""
    ## You can also define the template in a separate package and refer to it
    ## using Buffet style uris
    #template = "tw.twtools.templates.twtools"

    javascript = [jquery_js,
                 ]
    #css = [my_css]



