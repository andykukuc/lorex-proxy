# lorex-proxy

A [mitmproxy](https://mitmproxy.org/) addon that bypasses the ActiveX/plugin requirement on Lorex IP camera web interfaces. Lorex cameras ship with a web UI that refuses to display the live feed unless a legacy browser plugin is detected — this proxy intercepts the response and injects JavaScript to spoof the plugin check, letting you view the stream in any modern browser.

## How it works

The addon intercepts every HTTP response. When it finds an HTML page, it injects a small script into the `<head>` that:
- Sets `window.hasPlugin` to always return `true`
- Creates a `Proxy` object for `window.g_ocx` that returns `true` for any method call
- Sets `window.g_previewLoaded = true`

This satisfies the camera's plugin detection without requiring any legacy software.

## Requirements

- Python 3.8+
- [mitmproxy](https://mitmproxy.org/) (`pip install mitmproxy`)

## Usage

```bash
# Install mitmproxy
pip install mitmproxy

# Run the proxy with the addon
mitmproxy -s lorex.py --listen-port 8080

# Or in headless mode
mitmdump -s lorex.py --listen-port 8080
```

Then configure your browser to use `127.0.0.1:8080` as an HTTP proxy and navigate to your Lorex camera's IP address.

## Notes

- Tested against Lorex cameras that require `g_ocx` plugin detection
- You may need to accept the mitmproxy CA certificate in your browser for HTTPS camera interfaces
- This is for local network use only — your camera traffic stays on your LAN

## License

MIT
