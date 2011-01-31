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

from tw.api import Widget, JSLink, CSSLink, js_function
from tw.forms.fields import TextField

__all__ = [
	'UIDatePicker',
	'UIDatePicker_ES']

# JS Links

from tw.jquery.ui import ui_datepicker_js, ui_datepicker_es_js

class UIDatePicker(TextField):
	javascript = [ui_datepicker_js]

	def update_params(self, d):
		super(UIDatePicker, self).update_params(d)
		if not getattr(d,"id",None):
			raise ValueError, "DatePicker is supposed to have id"

		call = js_function("$('#%s').datepicker" % d.id)()
		self.add_call(call)

class UIDatePicker_ES(UIDatePicker):
	javascript = [ui_datepicker_es_js, ui_datepicker_js]

# JQuery UI Date Picker Plugin implemented by Laureano Arcanio 2008
