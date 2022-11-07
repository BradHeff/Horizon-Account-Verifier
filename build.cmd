@ECHO off

if '%username%' == 'bheffernan' goto run
if '%username%' == 'brad.heffernan' goto run

goto ender

:run
pyinstaller.exe --noconfirm --clean --onefile --key="BCjrtVKYf4aKSFoBsJ8bifEkG8ubccsPvaHN3NfevxL8uqk5kWzYDFwhjX62Zp8JgZnK6rV5Zr" --collect-data="sv_ttk" --distpath="scrap/dist" --workpath="scrap/build" --name=%1 --hidden-import="pyad" --icon="icon.ico" --version-file="version.rc" %2

:ender
exit
