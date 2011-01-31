# Simple Tree View based on jQuery
#
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
#
# Author: Sanjiv Singh <SinghSanjivK@gmail.com>

from tw.api import Widget, JSLink, CSSLink, js_function, js_callback

from tw.jquery.base import *

jQuery = js_function('$')

class TreeView(Widget):
        params = ["treeDiv"]
        treeDiv__doc=""
        treeDiv="treeView"
        include_dynamic_js_calls = True
        template="""
        """
        javascript=[jquery_treeview_js]
        css=[jquery_treeview_css]
        def update_params(self, d):
            super(TreeView, self).update_params(d)
            self.add_call(
                jQuery('#%s' % d.treeDiv).treeview()
            )
