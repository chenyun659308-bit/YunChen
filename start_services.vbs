Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\Git\config"
WshShell.Run "D:\Git\.venv\Scripts\python.exe manage.py runserver --noreload 0.0.0.0:8001", 0, False
WshShell.CurrentDirectory = "D:\Git\frontend"
WshShell.Run "D:\Git\.venv\Scripts\python.exe spa_server.py", 0, False