#!/usr/bin/env python3
"""
Simple HTTP server to serve the simulation HTML file
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

PORT = 8080
DIRECTORY = "/home/rawnakjain/Desktop/Projects/Dev/POC-Marketing-Agent"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serving simulation at http://localhost:{PORT}")
        print("Open your browser and go to the above URL to view the simulation")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    # Change to the directory containing our files
    os.chdir(DIRECTORY)

    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(1)

    # Open the browser
    url = f"http://localhost:{PORT}/simulation.html"
    print(f"Opening {url} in your default browser...")
    webbrowser.open(url)

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")