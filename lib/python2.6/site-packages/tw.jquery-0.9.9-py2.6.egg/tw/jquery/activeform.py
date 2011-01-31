# jQuery based AJAX Form
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

from tw.api import JSLink, js_function
from tw.forms import TableForm
from tw.jquery.base import *

jquery_form_js = JSLink(modname=__name__,
    filename='static/javascript/jquery.form.js', javascript=[])
jQuery = js_function('$')


class AjaxForm(TableForm):

    params = [
        "id", "target", "beforeSubmit", "action"
        "success", "type", "dataType",
        "clearForm", "resetForm", "timeout"]

    target_doc = ""
    beforeSubmit_doc = ""
    action_doc = ""
    success_doc = ""
    type_doc = ""
    dataType_doc = ""
    clearForm_doc = ""
    resetForm_doc = ""
    timeout_doc = ""

    target = "output"
    beforeSubmit = ""
    action = ""
    success = ""
    type = "POST"
    dataType = ""
    clearForm = True
    resetForm = True
    timeout = 5000

    template = "genshi:tw.jquery.templates.activeform"
    javascript = [jquery_js, jquery_form_js]
    include_dynamic_js_calls = True

    def update_params(self, d):
        super(AjaxForm, self).update_params(d)
        if not getattr(d, "id", None):
            raise ValueError("AjaxForm is supposed to have an id")

        options = dict(
            target=('#%s' % self.target),
            beforeSubmit=self.beforeSubmit,
            success=self.success,
            url=self.action,
            type=self.type,
            dataType=self.dataType,
            clearForm=self.clearForm,
            resetForm=self.resetForm,
            timeout=self.timeout)

        call = js_function('$("#%s").ajaxForm' % d.id)(options)
        self.add_call(call)
