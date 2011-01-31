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

from tw.api import JSLink, CSSLink, js_function
from tw.jquery import JQuery
from tw.jquery.direction import *
from tw.forms import FormField
from ui_core import jquery_ui_core_js
from ui import ui_widget_js, ui_tabs_js as jquery_ui_tabs_js

__all__ = ["jquery_ui_tabs_js"]

# declare your static resources here

## JS dependencies can be listed at 'javascript' so they'll get included
## before

jquery_ui_tabs_css    = CSSLink(modname=__name__, filename='static/css/flora.tabs.css')
#jquery_ui_tabs_js    = JSLink(modname=__name__, filename='static/javascript/ui/ui.tabs.js', javascript=[jquery_ui_core_js,jquery_direction_js, ui_widget_js])

jQuery = js_function('jQuery')

class JQueryUITabs(FormField):
    css = [jquery_ui_tabs_css
          ]
    javascript = [jquery_ui_tabs_js
                 ]
    params = ["tabdefault"]
    tabdefault__doc="0-based index of the tab to be selected on page load"
    tabdefault=0
#    include_dynamic_js_calls = True #????
    def update_params(self, d):
        super(JQueryUITabs, self).update_params(d)
        if not getattr(d,"id",None):
            raise ValueError, "JQueryUITabs is supposed to have id"
        self.add_call(jQuery("#%s" % d.id).tabs())
        if d.tabdefault > 0:
            self.add_call(jQuery("#%s" % id).tabs("select", d.tabdefault))
