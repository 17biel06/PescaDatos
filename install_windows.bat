@echo off
SETLOCAL

:: Copiar la carpeta PHP a C:\PHP
xcopy /E /I /H "dependencias\PHP" "C:\PHP"

:: Añadir configuración a httpd.conf
echo LoadModule php_module "C:/PHP/php8apache2_4.dll" >> "C:\Apache24\conf\httpd.conf"
echo AddType application/x-httpd-php .php >> "C:\Apache24\conf\httpd.conf"
echo PHPIniDir "C:/PHP" >> "C:\Apache24\conf\httpd.conf"
echo LoadFile "C:/PHP/php8ts.dll" >> "C:\Apache24\conf\httpd.conf"

:: Cambia esto por la URL de tu archivo
set "url=https://github.com/17biel06/PescaDatos/raw/main/dependencias/Apache24.zip"

:: Cambia esto por la ruta de tu archivo descargado
set "downloaded_file=%TEMP%\Apache24.zip"

:: Cambia esto por la ruta de tu carpeta descomprimida
set "unzipped_folder=%TEMP%\Apache24"

:: Descarga el archivo con curl
powershell -Command "& {curl '%url%' -o '%downloaded_file%'}"

:: Descomprime el archivo
powershell -Command "& {Expand-Archive -Path '%downloaded_file%' -force -DestinationPath '%unzipped_folder%'}"

:: Elimina la carpeta existente en C:\
if exist "C:\Apache24" rmdir /S /Q "C:\Apache24"

:: Mueve la carpeta descomprimida a C:\
move /Y "%unzipped_folder%" "C:\"

:: Entra en la carpeta bin y ejecuta el comando
cd "C:\Apache24\bin"
httpd -k install

:: Elimina el archivo zip descargado
del /F "%downloaded_file%"

ENDLOCAL
