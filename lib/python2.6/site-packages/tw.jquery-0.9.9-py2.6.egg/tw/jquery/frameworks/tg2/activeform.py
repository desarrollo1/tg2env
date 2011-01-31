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

from decorator import decorator
import pylons
from tg import validate, TGController, expose
from tg.controllers import object_dispatch

class ajax_validate(validate):
    def __init__(self, error_handler=None, *args,**kw):
        self.error_handler = error_handler
        super(validate,self).__init__(*args,**kw)
        class Validators(object):
            def validate(self, params):
                controller = pylons.request.environ["pylons.controller"]
                url_path = pylons.request.path.split('/')[1:]
                controller, remainder = object_dispatch(controller, url_path)
                res = controller.im_self.form.validate(params)
                return res
        self.validators=Validators()
        
class AjaxFormResponseHandler(TGController):
    def __init__(self, form, onSuccessFunc=None, *args, **kw):
        """(form, onSuccessFunc=None, *args, **kw)
        This class creates a handler which handles all of the 
        
        
        """
        self.form = form
        self.onSuccessFunc = onSuccessFunc
        TGController.__init__(self, args, kw)
        
    @expose('json')
    def ajax_error(self, **kw):
        pylons.response.status = '406 FAILED_VALIDATION'
        return dict(form_errors=pylons.c.form_errors)
    
    @expose('json')
    @ajax_validate(error_handler=ajax_error)
    def ajax_submit(self, **kw):
        controller = pylons.request.environ["pylons.controller"]
        
        #get the controller up the controller before the last one
        url_path = pylons.request.path.split('/')[1:-1]
        for item in url_path:
            controller = getattr(controller, item)

        if self.onSuccessFunc:
            self.onSuccessFunc(controller, **kw)
        return {'response':'successful submit'}
