Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\Git\config"
WshShell.Run "D:\Git\.venv\Scripts\python.exe manage.py runserver --noreload 0.0.0.0:5173", 1, False