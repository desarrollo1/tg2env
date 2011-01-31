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

from tw.api import Widget, JSLink, CSSLink,js_function
from tw.forms.fields import TableForm

__all__ = [	"JQValidate",
			"JQValidatePacked",
			'validate_js',
			'validate_css',
			'JQTableForm',
			'JQTableForm_ES']

# JS Links

validate_js = JSLink(	modname=__name__,
						filename=dict(normal='static/javascript/validate/jquery.validate.js',
							      packed='static/javascript/validate/jquery.validate.pack.js',
							      min='static/javascript/validate/jquery.validate.min.js',
							      ),
						javascript=[])

validate_es_js = JSLink(	modname=__name__,
							filename='static/javascript/validate/localization/messages_es.js',
							javascript=[])

# CSS Links

validate_css   = CSSLink(	modname=__name__,
							filename='static/css/validation_form.css')

class JQValidate(Widget):
	javascript = [validate_js]
	css = [validate_css]

class JQValidatePacked(Widget):
	javascript = [validate_js]
	css = [validate_css]

class JQTableForm(TableForm):
	javascript = [validate_js]
	css = [validate_css]
	def update_params(self, d):
		super(JQTableForm, self).update_params(d)
		if not getattr(d,"id",None):
			raise ValueError, "JQTableForm is supposed to have id"
		call = js_function("$('#%s').validate" % d.id)()
		self.add_call(call)
		self.css.append(validate_css)

class JQTableForm_ES(JQTableForm):
	javascript = [validate_js, validate_es_js]

# JQuery Validate Plugin implemented by Laureano Arcanio 2008
