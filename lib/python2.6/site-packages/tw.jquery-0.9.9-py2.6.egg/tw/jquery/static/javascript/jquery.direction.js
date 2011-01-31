
/* calculate the object's effective direction
 *
 * copyright (c) 2008 Alex Bodnaru <alexbodn@012.net.il>
 *
 * jquery.direction is currently available for use in all personal or 
 * commercial projects under both MIT and GPL licenses. This means that 
 * you can choose the license that best suits your project, and use it 
 * accordingly.
 *
 * this function will check the given object's effective direction, whether
 * set specifically on it, or in either of it's parents.
 *
*/

jQuery.fn.effectivedirection = function () {
	o = this[0];
	var dirsetter = null;
	if ( jQuery(o).attr('dir') == '' ) {
		var dirsetters = jQuery(o).parents().filter('[dir*=r]');
		if (dirsetters.length == 0) {
			dirsetters = jQuery(o).parents().filter('[dir*=R]');
		}
		if (dirsetters.length > 0) {
			dirsetter = dirsetters[0];
		}
	} else {
		dirsetter = jQuery(o);
	}
	if (dirsetter != null ) {
		return jQuery(dirsetter).attr('dir').toLowerCase();
	} else {
		return 'ltr';
	}
};
