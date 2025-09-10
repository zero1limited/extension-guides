# RumVision

https://insights.rumvision.com/dashboard/






## Currently setup for

### extensions.zero1.co.uk
not working yet, possible domain issue, ticket raised with RUM


### ibottles.co.uk

```
<script>
window.rumv = window.rumv || function() { (window.rumv.q = window.rumv.q || []).push(arguments) };
(function(rum, vi,si,on) {
	var s = JSON.parse( sessionStorage.getItem('rumv') || '{"pageviews":0}' ); s.pageviews++;
	if ( s.urls && s.regex && ( s.page = eval('('+s.regex+')')( s.urls, vi.location.pathname ) ) && !s.page.type ) {
			return sessionStorage.setItem('rumv', JSON.stringify( s ) );
		}
	
	vi.rumv.storage = s;
	var head = si.querySelector('head'), js = si.createElement('script');
	js.src = 'https://d5yoctgpv4cpx.cloudfront.net/'+rum+'/v4-'+vi.location.hostname+'.js';
	head.appendChild(js);
})( 'RUM-3F049F263C', window, document, 'ibottles.co.uk' );
</script>
```
