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
import os

from tw.api import JSLink, CSSLink
from tw.jquery import jquery_js
from tw.jquery.ui_core import jquery_ui_core_js as ui_core_js

modname = __name__

import pkg_resources

basedir = "static/javascript/ui"

def collect_variants(filename):
    """
    Gathers the various variants of the ui-js-files.
    """
    normal_variant = "/".join([basedir, filename])
    if not pkg_resources.resource_exists(modname, normal_variant):
        raise Exception("No such resoucre: %s.%s" % (modname, normal_variant))
    res = dict(normal=normal_variant)
    filebase = os.path.splitext(filename)[0]
    min_filename = "%s.min.js" % filebase
    min_variant = "/".join([basedir, "minified", min_filename])
    if pkg_resources.resource_exists(modname, min_variant):
        res["min"] = min_variant

    packed_filename = "%s.packed.js" % filebase
    packed_variant = "/".join([basedir, "packed", packed_filename])
    if pkg_resources.resource_exists(modname, packed_variant):
        res["packed"] = packed_variant

    if len(res.keys()) == 1:
        return res["normal"]
    return res

##
## jQuery UI
##

jquery_ui_all_js = JSLink(filename=collect_variants('jquery.ui.all.js'), modname=modname)
ui_widget_js = JSLink(filename=collect_variants('ui.widget.js'), javascript=[ui_core_js], modname=modname)
ui_mouse_js = JSLink(filename=collect_variants('ui.mouse.js'), javascript=[ui_core_js, ui_widget_js], modname=modname)

ui_accordion_js = JSLink(filename=collect_variants('ui.accordion.js'), javascript=[ui_core_js, ui_widget_js], modname=modname)

ui_datepicker_css = CSSLink(filename='static/css/ui/ui.datepicker.css', modname=modname)
ui_datepicker_js = JSLink(filename=collect_variants('ui.datepicker.js'), javascript=[ui_core_js],
                          css=[ui_datepicker_css],
                          modname=modname)
ui_draggable_js = JSLink(filename=collect_variants('ui.draggable.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js], modname=modname)
ui_droppable_js = JSLink(filename=collect_variants('ui.droppable.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js, ui_draggable_js], modname=modname)
ui_resizable_js = JSLink(filename=collect_variants('ui.resizable.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js], modname=modname)
ui_selectable_js = JSLink(filename=collect_variants('ui.selectable.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js], modname=modname)
ui_slider_js = JSLink(filename=collect_variants('ui.slider.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js], modname=modname)
ui_sortable_js = JSLink(filename=collect_variants('ui.sortable.js'), javascript=[ui_core_js, ui_mouse_js, ui_widget_js], modname=modname)
ui_tabs_js = JSLink(filename=collect_variants('ui.tabs.js'), javascript=[ui_core_js, ui_widget_js], modname=modname)
ui_progressbar_js = JSLink(filename=collect_variants('ui.progressbar.js'), javascript=[ui_core_js, ui_widget_js], modname=modname)
ui_position_js = JSLink(filename=collect_variants('ui.position.js'), javascript=[ui_core_js], modname=modname)
ui_autocomplete_js = JSLink(filename=collect_variants('ui.autocomplete.js'), javascript=[ui_core_js, ui_widget_js, ui_position_js], modname=modname)
ui_button_js = JSLink(filename=collect_variants('ui.button.js'), javascript=[ui_core_js, ui_widget_js], modname=modname)
ui_dialog_js = JSLink(filename=collect_variants('ui.dialog.js'), javascript=[ui_core_js, ui_widget_js, ui_button_js, ui_draggable_js, ui_position_js, ui_resizable_js], modname=modname)


##
## Effects
##

effects_core_js = JSLink(filename=collect_variants('effects.core.js'), javascript=[ui_core_js], modname=modname)
effects_blind_js = JSLink(filename=collect_variants('effects.blind.js'), javascript=[effects_core_js], modname=modname)
effects_bounce_js = JSLink(filename=collect_variants('effects.bounce.js'), javascript=[effects_core_js], modname=modname)
effects_clip_js = JSLink(filename=collect_variants('effects.clip.js'), javascript=[effects_core_js], modname=modname)
effects_drop_js = JSLink(filename=collect_variants('effects.drop.js'), javascript=[effects_core_js], modname=modname)
effects_explode_js = JSLink(filename=collect_variants('effects.explode.js'), javascript=[effects_core_js], modname=modname)
effects_fold_js = JSLink(filename=collect_variants('effects.fold.js'), javascript=[effects_core_js], modname=modname)
effects_highlight_js = JSLink(filename=collect_variants('effects.highlight.js'), javascript=[effects_core_js], modname=modname)
effects_pulsate_js = JSLink(filename=collect_variants('effects.pulsate.js'), javascript=[effects_core_js], modname=modname)
effects_scale_js = JSLink(filename=collect_variants('effects.scale.js'), javascript=[effects_core_js], modname=modname)
effects_shake_js = JSLink(filename=collect_variants('effects.shake.js'), javascript=[effects_core_js], modname=modname)
effects_slide_js = JSLink(filename=collect_variants('effects.slide.js'), javascript=[effects_core_js], modname=modname)
effects_transfer_js = JSLink(filename=collect_variants('effects.transfer.js'), javascript=[effects_core_js], modname=modname)

##
## i18n
##

jquery_ui_i18n_js = JSLink(filename=collect_variants('i18n/jquery-ui-i18n.js'), modname=modname)
jquery_ui_i18n_all_js = JSLink(filename=collect_variants('i18n/jquery.ui.i18n.all.js'), modname=modname)

ui_datepicker_ar_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ar.js'), modname=modname)
ui_datepicker_bg_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-bg.js'), modname=modname)
ui_datepicker_ca_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ca.js'), modname=modname)
ui_datepicker_cs_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-cs.js'), modname=modname)
ui_datepicker_da_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-da.js'), modname=modname)
ui_datepicker_de_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-de.js'), modname=modname)
ui_datepicker_es_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-es.js'), modname=modname)
ui_datepicker_fi_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-fi.js'), modname=modname)
ui_datepicker_fr_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-fr.js'), modname=modname)
ui_datepicker_he_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-he.js'), modname=modname)
ui_datepicker_hu_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-hu.js'), modname=modname)
ui_datepicker_hy_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-hy.js'), modname=modname)
ui_datepicker_id_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-id.js'), modname=modname)
ui_datepicker_is_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-is.js'), modname=modname)
ui_datepicker_it_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-it.js'), modname=modname)
ui_datepicker_ja_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ja.js'), modname=modname)
ui_datepicker_ko_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ko.js'), modname=modname)
ui_datepicker_lt_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-lt.js'), modname=modname)
ui_datepicker_lv_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-lv.js'), modname=modname)
ui_datepicker_nl_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-nl.js'), modname=modname)
ui_datepicker_no_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-no.js'), modname=modname)
ui_datepicker_pl_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-pl.js'), modname=modname)
ui_datepicker_pt_BR_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-pt-BR.js'), modname=modname)
ui_datepicker_ro_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ro.js'), modname=modname)
ui_datepicker_ru_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ru.js'), modname=modname)
ui_datepicker_sk_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sk.js'), modname=modname)
ui_datepicker_sv_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sv.js'), modname=modname)
ui_datepicker_th_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-th.js'), modname=modname)
ui_datepicker_tr_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-tr.js'), modname=modname)
ui_datepicker_uk_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-uk.js'), modname=modname)
ui_datepicker_zh_CN_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-zh-CN.js'), modname=modname)
ui_datepicker_zh_TW_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-zh-TW.js'), modname=modname)
ui_datepicker_el_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-el.js'), modname=modname)
ui_datepicker_sk_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sk.js'), modname=modname)
ui_datepicker_eo_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-eo.js'), modname=modname)
ui_datepicker_hr_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-hr.js'), modname=modname)
ui_datepicker_ms_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ms.js'), modname=modname)
ui_datepicker_sl_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sl.js'), modname=modname)
ui_datepicker_sq_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sq.js'), modname=modname)
ui_datepicker_sr_SR_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sr-SR.js'), modname=modname)
ui_datepicker_sr_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-sr.js'), modname=modname)
ui_datepicker_af_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-af.js'), modname=modname)
ui_datepicker_az_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-az.js'), modname=modname)
ui_datepicker_bs_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-bs.js'), modname=modname)
ui_datepicker_en_GB_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-en-GB.js'), modname=modname)
ui_datepicker_et_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-et.js'), modname=modname)
ui_datepicker_eu_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-eu.js'), modname=modname)
ui_datepicker_fo_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-fo.js'), modname=modname)
ui_datepicker_fr_CH_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-fr-CH.js'), modname=modname)
ui_datepicker_ta_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-ta.js'), modname=modname)
ui_datepicker_vi_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-vi.js'), modname=modname)
ui_datepicker_zh_HK_js = JSLink(javascript=[ui_datepicker_js], filename=collect_variants('i18n/ui.datepicker-zh-HK.js'), modname=modname)

