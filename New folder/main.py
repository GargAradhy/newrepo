from flask import Flask
import os
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        
        name = "Aradhy Garg"
        
        # Get system username
        username = subprocess.check_output(['whoami'], text=True).strip()
        
        # Get server time in IST
        ist = pytz.timezone('Asia/Kolkata')
        server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
        
        # Get top output - using ps since top might not work well in some environments
        # Using ps aux to get a snapshot of all processes
        ps_output = subprocess.check_output(['ps', 'aux'], text=True)
        
        # Format the response
        html_response = f"""
        <html>
            <head>
                <title>System Information</title>
                <style>
                    body {{
                        font-family: monospace;
                        margin: 20px;
                        background-color: #f0f0f0;
                    }}
                    .info-block {{
                        background-color: white;
                        padding: 20px;
                        border-radius: 5px;
                        margin-bottom: 20px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }}
                    .info-item {{
                        margin-bottom: 10px;
                    }}
                    pre {{
                        background-color: #f8f8f8;
                        padding: 15px;
                        border-radius: 5px;
                        overflow-x: auto;
                        white-space: pre-wrap;
                    }}
                </style>
            </head>
            <body>
                <div class="info-block">
                    <div class="info-item"><strong>Name:</strong> {name}</div>
                    <div class="info-item"><strong>Username:</strong> {username}</div>
                    <div class="info-item"><strong>Server Time (IST):</strong> {server_time}</div>
                </div>
                <div class="info-block">
                    <strong>Process Information:</strong>
                    <pre>{ps_output}</pre>
                </div>
            </body>
        </html>
        """
        return html_response
        
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)