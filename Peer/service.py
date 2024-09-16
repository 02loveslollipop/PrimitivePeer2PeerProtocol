import os
import subprocess
import getpass

# Determine the path to the current script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Define the service name and path
service_name = "peer.service"
service_path = f"/etc/systemd/system/{service_name}"

# Create the content of the service file
service_content = f"""
[Unit]
Description=Peer Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 {script_path} --server
WorkingDirectory={script_dir}
Restart=always
User={getpass.getuser()}
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"""

# Write the service file
with open(service_path, "w") as service_file:
    service_file.write(service_content)

# Reload systemd daemon
subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

# Start the service
subprocess.run(["sudo", "systemctl", "start", service_name], check=True)

# Enable the service to start on boot
subprocess.run(["sudo", "systemctl", "enable", service_name], check=True)

# Check the status of the service
subprocess.run(["sudo", "systemctl", "status", service_name], check=True)