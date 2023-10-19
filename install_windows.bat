@echo off
SETLOCAL

:: Cambia esto por la URL de tu archivo
set "url=https://github.com/17biel06/PescaDatos/raw/main/dependencias/Apache24.zip"

:: Cambia esto por la URL de tu archivo PHP
set "php_url=https://windows.php.net/downloads/releases/php-8.2.11-Win32-vs16-x64.zip"

:: Cambia esto por la ruta de tu archivo descargado
set "downloaded_file=%TEMP%\Apache24.zip"

:: Cambia esto por la ruta de tu archivo PHP descargado
set "php_downloaded_file=%TEMP%\php.zip"

:: Cambia esto por la ruta de tu carpeta descomprimida
set "unzipped_folder=%TEMP%\Apache24"

:: Descarga el archivo con curl
powershell -Command "& {curl '%url%' -o '%downloaded_file%'}"

:: Descarga el archivo PHP con curl
powershell -Command "& {curl '%php_url%' -o '%php_downloaded_file%'}"

:: Descomprime el archivo
powershell -Command "& {Expand-Archive -Path '%downloaded_file%' -force -DestinationPath '%unzipped_folder%'}"

:: Descomprime el archivo PHP
powershell -Command "& {Expand-Archive -Path '%php_downloaded_file%' -force -DestinationPath 'C:\'}"

:: Elimina la carpeta existente en C:\
if exist "C:\Apache24" rmdir /S /Q "C:\Apache24"

:: Mueve la carpeta descomprimida a C:\
move /Y "%unzipped_folder%" "C:\PHP"

:: Entra en la carpeta bin y ejecuta el comando
cd "C:\Apache24\bin"
httpd -k install

:: Añade las líneas al archivo httpd.conf
echo LoadModule php_module "C:/PHP/php8apache2_4.dll" >> "C:\Apache24\conf\httpd.conf"
echo AddType application/x-httpd-php .php >> "C:\Apache24\conf\httpd.conf"
echo PHPIniDir "C:/PHP" >> "C:\Apache24\conf\httpd.conf"
echo LoadFile "C:/PHP/php8ts.dll" >> "C:\Apache24\conf\httpd.conf"

:: Elimina los archivos zip descargados
del /F "%downloaded_file%"
del /F "%php_downloaded_file%"

ENDLOCAL
