from mitmproxy import http


class InjectPlugin:
    def response(self, flow: http.HTTPFlow):
        if flow.response and "text/html" in flow.response.headers.get("content-type", ""):
            inject = b'<script>Object.defineProperty(window,"hasPlugin",{get:function(){return true;},set:function(){},configurable:false});window.g_ocx=new Proxy({},{get:function(t,n){return function(){return true;}}});window.g_previewLoaded=true;</script>'
            flow.response.content = flow.response.content.replace(b"<head>", b"<head>" + inject)


addons = [InjectPlugin()]
