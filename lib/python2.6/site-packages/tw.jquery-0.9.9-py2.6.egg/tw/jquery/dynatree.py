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

"""
:mod:`tw.jquery.dynatree` - A Dynamic Tree Widget
=================================================

.. moduleauthor:: Luke Macken <lmacken@redhat.com>
"""

from tw.api import JSLink, Widget, CSSLink, js_callback
from tw.jquery import jquery_js, jQuery, jquery_cookie_js
from tw.jquery.ui_core import jquery_ui_core_js

jquery_ui_dynatree_js = JSLink(
        filename='static/javascript/jquery.dynatree.js',
        javascript=[jquery_ui_core_js, jquery_cookie_js],
        modname=__name__)

jquery_ui_dynatree_min_js = JSLink(
        filename='static/javascript/jquery.dynatree.min.js',
        javascript=[jquery_ui_core_js, jquery_cookie_js],
        modname=__name__)

jquery_ui_dynatree_css = CSSLink(
        filename='static/css/dynatree/ui.dynatree.css',
        modname=__name__)

class Dynatree(Widget):
    """ A Dynamic Tree Widget.

    Dynatree is a dynamic JavaScript tree view control with support for
    checkboxes and lazy loading. 

    http://wwwendt.de/tech/dynatree/doc/dynatree-doc.html
    """
    params = {
        'id': 'The ID of our Widget, and div',
        'title': 'Name of the root node',
        'rootVisible': 'Set to true, to make the root node visible',
        'minExpandLevel': '1: root node is not collapsible',
        'imagePath': 'Path to a folder containing icons. Defaults to skin/',
        'tree_children': 'Init tree structure from this object array', 
        'initId': 'Init tree structure from a <ul> element with this ID',
        'initAjax': 'Ajax options used to initialize the tree strucuture',
        'autoFocus': 'Set focus to first child, when expanding or lazy-loading',
        'keyboard': 'Support keyboard navigation',
        'persist': 'Persist expand-status to a cookie',
        'autoCollapse':'Automatically collapse all siblings, when a node is expanded.',
        'clickFolderMode': '1:activate, 2:expand, 3:activate and expand',
        'activeVisible': 'Make sure, active nodes are visible (expanded).',
        'checkbox': 'Show checkbox',
        'selectMode': '1:single, 2:multi, 3:multi-hier',
        'fx': 'Animations, e.g. null or { height: "toggle", duration: 200 }',

        # Low level event handlers: onEvent(dtnode, event): return false, to
        # stop default processing
        'onClick': 'null: generate focus, expand, activate, select events.',
        'onDblClick': '(No default actions.)',
        'onKeydown': 'null: generate keyboard navigation (focus, expand, activate).',
        'onKeypress': '(No default actions.)',
        'onFocus': 'null: handle focus.',
        'onBlur': 'null: handle unfocus.',

        # Pre-event handlers onQueryEvent(flag, dtnode): return false, to stop
        # processing
        'onQueryActivate': 'Callback(flag, dtnode) before a node is (de)activated.',
        'onQuerySelect': 'Callback(flag, dtnode) before a node is (de)selected.',
        'onQueryExpand': 'Callback(flag, dtnode) before a node is expanded/collpsed.',
        # High level event handlers
        'onActivate': 'Callback(dtnode) when a node is activated.',
        'onDeactivate': 'Callback(dtnode) when a node is deactivated.',
        'onSelect': 'Callback(flag, dtnode) when a node is (de)selected.',
        'onExpand': 'Callback(dtnode) when a node is expanded.',
        'onCollapse': 'Callback(dtnode) when a node is collapsed.',
        'onLazyRead': 'Callback(dtnode) when a lazy node is expanded for the first time.',
        'ajaxDefaults': 'Used by initAjax option',
        'strings': 'Display strings, like loading/loadError',
        'idPrefix': 'Used to generate node ids like <span id="ui-dynatree-id-<key>">.',
        'cookieId': 'Choose a more unique name, to allow multiple trees.',
    }
    javascript =[jquery_ui_dynatree_js]
    css = [jquery_ui_dynatree_css]
    template = """
        <div id="${id}"></div>
    """
    engine_name = 'mako'

    def update_params(self, d):
        super(Dynatree, self).update_params(d)

        options = {}

        # Hack around ToscaWidgets
        for param in self.params:
            if param in ('css_class', 'css_classes'):
                continue
            if getattr(d, param, None):
                options[param] = d[param]
        if 'tree_children' in options:
            options['children'] = options['tree_children']
            del(options['tree_children'])

        self.add_call(jQuery('#%s' % d.id).dynatree(options))
