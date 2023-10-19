import os 

def serveo_sin_dominio():
    os.system("ssh -R 80:localhost:80 serveo.net")

def generar_llave_ssh():
    os.system("ssh-keygen -t rsa -b 4096 ")
    print("Inicia sesión y ctrl + C")
    os.system("ssh -R incubo.serveo.net:80:localhost:8888 serveo.net")
    print("\nYa tienes tu clave, reinicia y funcionará correctamente.")

def serveo_con_dominio(dominio_personalizado):
    dominio_personalizado = input("Ingresa tu dominio personalizado. EJ: vaca (vaca.serveo.net): ")
    os.system(f"ssh -R {dominio_personalizado}.serveo.net:80:localhost:80 serveo.net")
    return dominio_personalizado

def salir_del_programa():
    print("Saliendo del programa...")
    os.system("NET STOP Apache2.4")

def menu():
    print("1) Serveo sin dominio personalizado")
    print("2) Generar llave ssh (NECESARIO PARA UN DOMINIO PERSONALIZADO)")
    print("3) Serveo con dominio personalizado")
    print("4) Salir")

    opciones = {
        1: serveo_sin_dominio,
        2: generar_llave_ssh,
        3: serveo_con_dominio,
        4: salir_del_programa
    }

    while True:
        try:
            opcion = int(input("Ingresa una opción: "))
            if opcion in opciones:
                if opcion == 3:
                    opciones[opcion](None)  
                else:
                    opciones[opcion]()
                break
            else:
                print("Por favor, ingresa una opción válida.")
        except ValueError:
            print("Por favor, ingresa un número.")

def main():
    menu()
    

if __name__ == "__main__":
    main()



