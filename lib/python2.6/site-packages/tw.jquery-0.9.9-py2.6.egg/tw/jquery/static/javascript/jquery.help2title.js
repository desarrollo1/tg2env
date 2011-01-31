
/* move help to title
 *
 * copyright (c) 2008 Alex Bodnaru <alexbodn@012.net.il>
 *
 * help2title is currently available for use in all personal or commercial 
 * projects under both MIT and GPL licenses. This means that you can choose 
 * the license that best suits your project, and use it accordingly.
 *
 * this function will take fieldhelp class strings from toscawidgets fields
 * and move them to the field as a title (tooltip).
 *
*/

jQuery.fn.help2title = function (o) {
	o = (o||"").toLowerCase();
	var inputs = jQuery(o).find(':input');
	for (var c = 0; c < inputs.length; ++c) {
		var input = jQuery(inputs[c]);
		var fieldhelp = jQuery(input).siblings();
		for (var hf = 0; hf < fieldhelp.length; ++hf) {
			if (jQuery(fieldhelp[hf]).hasClass('fieldhelp')) {
				jQuery(input).attr('title', jQuery(fieldhelp[hf]).text());
				jQuery(fieldhelp).remove();
			}
		}
	}
	return this;
};
