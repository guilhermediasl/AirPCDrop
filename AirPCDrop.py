import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from PIL import ImageGrab, Image
import pyperclip
import io
import time
import hashlib

PORT = 8001
SLEEP_INTERVAL = 3  # seconds
latest_content = None
content_type = None

def hash_content(content):
    """Calculate the hash of the content using a faster hashing algorithm."""
    return hashlib.blake2b(content).hexdigest() if isinstance(content, bytes) else hashlib.blake2b(content.encode()).hexdigest()

class ClipboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global latest_content, content_type
        self.send_response(200)
        
        if content_type == 'image':
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(latest_content.getvalue())
        elif content_type == 'text':
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(latest_content.encode())
        else:
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"No content in clipboard")

def serve_on_thread(port):
    """Serve HTTP requests in a separate thread."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, ClipboardHandler)
    print(f"Serving at http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

def continuously_update_content(sleep_interval):
    """Continuously update the content from the clipboard."""
    global latest_content, content_type
    last_hash = None

    while True:
        try:
            clipboard_content = ImageGrab.grabclipboard()
            if isinstance(clipboard_content, Image.Image):
                content_stream = io.BytesIO()
                clipboard_content.save(content_stream, format='PNG')
                content_stream.seek(0)
                current_hash = hash_content(content_stream.getvalue())

                if current_hash != last_hash:
                    last_hash = current_hash
                    latest_content = content_stream
                    content_type = 'image'
                    print("Updated image from clipboard")

            else:
                text = pyperclip.paste()
                current_hash = hash_content(text)

                if current_hash != last_hash:
                    last_hash = current_hash
                    latest_content = text
                    content_type = 'text'
                    print("Updated text from clipboard")

        except (pyperclip.PyperclipException, Image.DecompressionBombError) as e:
            print(f"Error: {e}")

        time.sleep(sleep_interval)

def main():
    """Main function to start server and content updating loop."""
    server_thread = threading.Thread(target=serve_on_thread, args=(PORT,))
    server_thread.daemon = True
    server_thread.start()

    continuously_update_content(SLEEP_INTERVAL)

if __name__ == '__main__':
    main()
