
/*
 * A tiny jQuery extension that logs the current jQuery selection 
 * to the firebug console (http://getfirebug.com/console.html).
 * copyright:  dom
 * downloaded at: http://happygiraffe.net/blog/2007/09/26/jquery-logging
 *
 * You can just stuff a call to .log() in the middle of what you're doing 
 * to see what you're currently addressing. e.g.
 * $(root).find('li.source > input:checkbox').log("sources to uncheck").removeAttr("checked");
 * The nice thing about logging to firebug is that each node becomes 
 * clickable in the console, so you can immediately see the context.
*/

jQuery.fn.log = function (msg) {
	console.log("%s: %o", msg, this);
	return this;
};
