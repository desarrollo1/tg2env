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

from tw.jquery.widgets import FlotWidget

class DemoFlotWidget(FlotWidget):
    demo_for = FlotWidget
    @staticmethod
    def data():
        """
        This is a static method that calculates data to feed the demo
        widget. Since data is a parameter (listed at :attr:`params`) and
        can be called without parameters it wiill be called by
        :meth:`update_params` to provide fresh values on every request.
        """
        import math
        from datetime import datetime
        d1 = []
        i = 0
        for x in range(26):
            d1.append((i, math.sin(i)))
            i += 0.5

        d2 = [[0, 3], [4, 8], [8, 5], [9, 13]]

        d3 = []
        i = 0
        for x in range(26):
            d3.append((i, math.cos(i)))
            i += 0.5

        d4 = []
        i = 0
        for x in range(26):
            d4.append((i, math.sqrt(i * 10)))
            i += 0.5

        d5 = []
        i = 0
        for x in range(26):
            d5.append((i, math.sqrt(i)))
            i += 0.5

        return [
            { 'data'  : d1, 'lines' : { 'show' : 'true', 'fill' : 'true' } },
            { 'data' : d2, 'bars' : { 'show' : 'true' } },
            { 'data'   : d3, 'points' : { 'show' : 'true' } },
            { 'data'  : d4, 'lines' : { 'show' : 'true' } },
            { 'data'   : d5, 'lines'  : { 'show' : 'true' }, 'points' : { 'show' : 'true' } }
        ]
