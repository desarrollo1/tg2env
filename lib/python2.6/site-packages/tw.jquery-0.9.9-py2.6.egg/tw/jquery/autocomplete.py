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

from tw.api import Widget, JSLink, CSSLink, js_function, js_callback

from tw.jquery.base import *
from tw.jquery.direction import *
from tw.forms import FormField

jquery_autocomplete_js    = JSLink(modname=__name__, filename='static/javascript/jquery.autocomplete.js', javascript=[jquery_dimensions_js,jquery_bgiframe_js,jquery_direction_js])
jQuery= js_function('$')
jquery_autocomplete_css=CSSLink(modname=__name__, filename='static/css/jquery.autocomplete.css')

class AutoCompleteField(FormField):
        params = ["minChars","completionURL", "fetchJSON","selectFirst", "cacheLength", "extraFields"]
        minChars__doc="minChars The minimum number of characters a user has to type before the autocompleter activates."
        selectFirst__doc="If this is set to true, the first autocomplete value will be automatically selected on tab/return, even if it has not been handpicked by keyboard or mouse action. If there is a handpicked (highlighted) result, that result will take precedence."
        extraFields__doc="A list of field #ids or names to be added to the url invokation as id=#id.value"
        completionURL__doc=""
        fetchJSON_doc=""
        cacheLength__doc="number of queries to perform from the cache"
        extraFields__doc="A list of field #ids or names(from the same form) to be added to the url invokation as field.(id|name)=field.value"
        minChars=3
        fetchJSON=False
        selectFirst=False
        extraFields=[]
        cacheLength=10
        include_dynamic_js_calls = True
        template="genshi:tw.jquery.templates.autocompletefield"
        javascript=[jquery_autocomplete_js]
        css=[jquery_autocomplete_css]
        def update_params(self, d):
            super(AutoCompleteField, self).update_params(d)
            if not getattr(d,"id",None):
                raise ValueError, "AutocompleteField is supposed to have id"
            
            if (self.fetchJSON):
                json_callback = js_callback('function(data) {$("#%s").autocomplete(data["data"]);}' % d.id)
                call = js_function('$.getJSON')(self.completionURL, json_callback)
                self.add_call(call)
            else:
                self.add_call(
                jQuery('#%s' % d.id).autocomplete(self.completionURL,dict(minChars=self.minChars,selectFirst=self.selectFirst,cacheLength=self.cacheLength,extraFields=self.extraFields))
                )
