pyinstaller.exe --noconfirm --clean --onefile --distpath="scrap/dist" --workpath="scrap/build" --name=%1 --hidden-import pyad --hidden-import sv_ttk --icon="icon.ico" --version-file="version.rc" %2