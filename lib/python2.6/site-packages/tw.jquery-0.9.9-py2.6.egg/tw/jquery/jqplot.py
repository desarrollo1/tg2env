""" A jQuery jqPlot Widget

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Authors: Ralph Bean <ralph.bean@gmail.com>

(Inspired by Luke Macken's FlotWidget)
"""

from base import jquery_js
from random import random
from tw.api import Widget, JSLink, CSSLink, js_function, js_callback

jQuery      = js_function('$')
excanvas_js = JSLink(modname=__name__, filename='static/javascript/excanvas.js')
jqplot_css              = CSSLink(modname=__name__,
    filename='static/css/jquery.jqplot.css')
jqplot_js               = JSLink(modname=__name__,
    filename='static/javascript/jquery.jqplot.js')
# Javascript Links for Default Plugins:
jqp_plugins_prefix = 'static/javascript/jqplugins'
jqp_bar_js                 = JSLink(modname=__name__,
    filename='%s/jqplot.barRenderer.min.js'            % jqp_plugins_prefix)
jqp_canvasAxis_js          = JSLink(modname=__name__,
    filename='%s/jqplot.canvasAxisTickRenderer.min.js' % jqp_plugins_prefix)
jqp_canvasText_js          = JSLink(modname=__name__,
    filename='%s/jqplot.canvasTextRenderer.min.js'     % jqp_plugins_prefix)
jqp_categoryAxis_js        = JSLink(modname=__name__,
    filename='%s/jqplot.categoryAxisRenderer.min.js'   % jqp_plugins_prefix)
jqp_cursor_js              = JSLink(modname=__name__,
    filename='%s/jqplot.cursor.min.js'                 % jqp_plugins_prefix)
jqp_dateAxis_js            = JSLink(modname=__name__,
    filename='%s/jqplot.dateAxisRenderer.min.js'       % jqp_plugins_prefix)
jqp_dragable_js            = JSLink(modname=__name__,
    filename='%s/jqplot.dragable.min.js'               % jqp_plugins_prefix)
jqp_highlighter_js         = JSLink(modname=__name__,
    filename='%s/jqplot.highlighter.min.js'            % jqp_plugins_prefix)
jqp_logAxis_js             = JSLink(modname=__name__,
    filename='%s/jqplot.logAxisRenderer.min.js'        % jqp_plugins_prefix)
jqp_ohlc_js                = JSLink(modname=__name__,
    filename='%s/jqplot.ohlcRenderer.min.js'           % jqp_plugins_prefix)
jqp_pie_js                 = JSLink(modname=__name__,
    filename='%s/jqplot.pieRenderer.min.js'            % jqp_plugins_prefix)
jqp_pointLabels_js         = JSLink(modname=__name__,
    filename='%s/jqplot.pointLabels.min.js'            % jqp_plugins_prefix)
jqp_trendline_js           = JSLink(modname=__name__,
    filename='%s/jqplot.trendline.min.js'              % jqp_plugins_prefix)

class JQPlotWidget(Widget):
    """ A versatile and expandable jQuery plotting widget.

    INTRODUCTION:
    Using jqPlot, a pure Javascript plotting library for jQuery,
    this widget produces client-side graphical plots of arbitrary datasets
    on-the-fly.  jqPlot is inspired by and similar to flot and is designed
    to be expanded.

    From the the jqPlot homepage:
        "Computation and drawing of lines, axes, shadows even the grid
        itself is handled by pluggable "renderers". Not only are the plot
        elements customizable, plugins can expand functionality of the plot
        too! There are plenty of hooks into the core jqPlot code allowing
        for custom event handlers, creation of new plot types, adding
        canvases to the plot, and more!"

    For detailed documentation of the jqPlot API, visit the jqPlot project
    homepage:  http://www.jqplot.com/

    USAGE:
        USING ONLY CORE RENDERERS
    To use only the basic core renderers of jqPlot, simply define
    instances of JQPlotWidget, pass them to your template and invoke
    display() like any other widget.  JQPlotWidget's constructor requires
    the named keyword 'data'.

    To use renderer plugins, pass JSLink resources to the JQPlotWidget
    constructor under the keyword argument extra_js=[...]

    jqPlot renderers (like $.jqplot.DateAxisRenderer) must be objects
    created by tw.api.js_function.  Be aware that these objects cannot be
    jsonified (javascript function pointers have no representation in json).

    The list of available plugins can be found as data members of this
    module beginning with 'jqp_' and ending with '_js'.  You can also
    define your own.
    """
    template = "genshi:tw.jquery.templates.jqplot"
    params = {
            "data"    : "Data to plot (required)",
            "options" : "A dictionary of options for jqPlot",
            "height"  : "The height of the graph",
            "width"   : "The width of the graph",
            "label"   : "Label for the graph",
            "id"      : "An optional ID for the graph"
    }
    javascript = [jquery_js, jqplot_js, excanvas_js]
    css = [jqplot_css]
    height = '300px'
    width = '600px'
    label = ''

    def __init__(self, id, extra_js=None, *args, **kw):
        super(JQPlotWidget, self).__init__(id, *args, **kw)
        if extra_js:
            self.javascript.extend(extra_js)

    def update_params(self, d):
        super(JQPlotWidget, self).update_params(d)
        if not d.get('data'):
            raise ValueError, "JQPlotWidget must have data to graph"
        if not d.get('id'):
            d['id'] = 'jqplot_%s' % str(int(random() * 999))
        data = d.get('data', [])
        options = d.get('options', {})
        self.add_call(
            js_function('%s =' % d.id)(
                js_function('$.jqplot')(
                    "%s" % d.id, data, options)))
        return d


class AsynchronousJQPlotWidget(Widget):
    template = "genshi:tw.jquery.templates.jqplot"
    params = {
            "src_url" : "A string url that will return data and plot options",
            "url_kw"  : "A dictionary of 'argument':'value' pairs for src_url",
            "interval": "Time in mseconds between polls (-1 = only on load)",
            "data"    : "Data for an initial plotting pass.",
            "options" : "A dictionary of options for jqPlot",
            "height"  : "The height of the graph",
            "width"   : "The width of the graph",
            "label"   : "Label for the graph",
            "id"      : "An optional ID for the graph"
    }
    javascript = [jquery_js, jqplot_js, excanvas_js]
    css = [jqplot_css]
    height = '300px'
    width = '600px'
    label = ''
    callback_reset = u"""
          pl=%s;
          for ( _i = 0; _i < json.data.length; _i++ ) {
                pl.series[_i].data = json.data[_i] ;
          }
          for (ax in json.options.axes) {
                  pl.axes[ax]._ticks = []
                  if ( 'axes' in json.options &&
                        ax in json.options.axes &&
                        'min' in json.options.axes[ax] ) {
                        pl.axes[ax].min = json.options['axes'][ax].min;
                        pl.axes[ax].max = json.options['axes'][ax].max;
                  }
                  pl.axes[ax].numberTicks = null
                  pl.axes[ax].tickInterval = null
                  pl.axes[ax]._tickInterval = null
          }
          pl.redraw();
    """

    def __init__(self, id, extra_js=None, *args, **kw):
        super(AsynchronousJQPlotWidget, self).__init__(id, *args, **kw)
        if extra_js:
            self.javascript.extend(extra_js)

    def update_params(self, d):
        super(AsynchronousJQPlotWidget, self).update_params(d)
        if not d.get('id'):
            d['id'] = 'asynch_jqplot_%s' % str(int(random() * 999))
        if not d.get('src_url'):
            raise ValueError, "AsynchronousJQPlotWidget must have a data url"
        src_url = d.get('src_url')
        url_kw = d.get('url_kw')
        if not url_kw:
            url_kw = {}
        data = d.get('data')
        if not data:
            data = [[[0,0]]]
        options = d.get('options')
        if not options:
            options = {}
        interval = d.get('interval')
        if not interval:
            interval = -1

        callback = js_callback('function (json){%s}' % self.callback_reset % d.id)
        ajres = '$.getJSON(\'%s\', %s, %s)' % (src_url, url_kw, callback)

        self.add_call(
            js_function('%s ='%d.id)(
                js_function('$.jqplot')(
                    "%s" % d.id, data, options)))

        if interval > 0 :
            self.add_call(js_function('setInterval')(ajres, interval)) 
