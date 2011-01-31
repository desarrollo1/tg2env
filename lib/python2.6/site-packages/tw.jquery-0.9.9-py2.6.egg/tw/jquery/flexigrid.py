# A Grid Widget based on jQuery FlexiGrid
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
jquery_flexigrid_js    = JSLink(modname=__name__, filename='static/javascript/flexigrid.pack.js', javascript=[jquery_js])
jQuery= js_function('$')
jquery_flexigrid_css=CSSLink(modname=__name__, filename='static/css/flexigrid/flexigrid.css')

class FlexiGrid(Widget):
        params = ["fetchURL", "title", "colModel", "buttons", 
                  "searchitems", "sortname", "sortorder", "usepager", 
                  "useRp", "rp", "showTableToggleButton", "width", "height",
                  "resizable"]

        fetchURL_doc = ""
        title_doc = ""
        colModel_doc = ""
        buttons_doc = ""
        searchItems_doc = ""
        sortname_doc = ""
        sortorder_doc = ""
        usePager_doc = ""
        useRp_doc = ""
        rp_doc = ""
        showTableToggleButton_doc = ""
        width_doc = ""
        height_doc = ""

        title = "FlexiGrid Table"
        colModel = []
        buttons = []
        searchItems = []
        sortname = ""
        sortorder = "asc"
        usePager = True
        useRp = True
        rp = 25
        showTableToggleButton = False
        resizable=True

        include_dynamic_js_calls = True
        template = """
                 <table id="${id}" style="display:none"></table>
                 """
        javascript=[jquery_flexigrid_js]
        css=[jquery_flexigrid_css]
        def update_params(self, d):
                super(FlexiGrid, self).update_params(d)
                if not getattr(d,"id",None):
                        raise ValueError, "FlexiGrid is supposed to have id"
                if not getattr(d,"fetchURL",None):
                        raise ValueError, "FlexiGrid must have fetchURL for fetching data"
                if not getattr(d,"colModel",None):
                        raise ValueError, "FlexiGrid must have colModel for setting up the columns"

                flexi_params = dict(dataType='json',
                                    url=self.fetchURL,
                                    title=self.title,
                                    colModel=self.colModel,
                                    buttons=self.buttons,
                                    searchitems=self.searchitems,
                                    sortname=self.sortname,
                                    sortorder=self.sortorder,
                                    usepager=self.usepager,
                                    useRp=self.useRp,
                                    rp=self.rp,
                                    showTableToggleBtn=self.showTableToggleButton,
                                    width=self.width,
                                    height=self.height,
                                    resizable=self.resizable)
                print 'resizable', self.resizable
                call = js_function('$("#%s").flexigrid' % d.id)(flexi_params)
                self.add_call(call)
