@ECHO off

if '%username%' == 'bheffernan' goto work
if '%username%' == 'brad.heffernan' goto home

goto ender

:home
pyinstaller.exe --clean --noconfirm --onefile --key="BCjrtVKYf4aKSFoBsJ8bifEkG8ubccsPvaHN3NfevxL8uqk5kWzYDFwhjX62Zp8JgZnK6rV5Zr" --add-data="C:\Users\brad.heffernan\AppData\Local\Programs\Python\Python311\Lib\site-packages\sv_ttk";"sv_ttk" --distpath="scrap/dist" --workpath="scrap/build" --name=%1 --hidden-import="pyad" --hidden-import="sv_ttk" --icon="icon.ico" --version-file="version.rc" %2
exit

:work
pyinstaller.exe --clean --noconfirm --onefile --key="BCjrtVKYf4aKSFoBsJ8bifEkG8ubccsPvaHN3NfevxL8uqk5kWzYDFwhjX62Zp8JgZnK6rV5Zr" --add-data="C:\Users\bheffernan\AppData\Local\Programs\Python\Python311\Lib\site-packages\sv_ttk";"sv_ttk" --distpath="scrap/dist" --workpath="scrap/build" --name=%1 --hidden-import="pyad" --hidden-import="sv_ttk" --icon="icon.ico" --version-file="version.rc" %2


:ender
exit
