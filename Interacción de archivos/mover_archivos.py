import os
import shutil

class MoverArchivos:
    def __init__(self, carpeta_padre, carpeta_nueva):
        self.carpeta_padre = carpeta_padre
        self.carpeta_nueva = carpeta_nueva

    def mover_csv(self):
        # Verificar si la carpeta nueva existe
        if not os.path.exists(self.carpeta_nueva):
            os.makedirs(self.carpeta_nueva)
            print(f'Se creó la carpeta {self.carpeta_nueva}')
        else:
            print(f'La carpeta {self.carpeta_nueva} ya existe')

        # Obtener la lista de archivos en la carpeta padre
        archivos = os.listdir(self.carpeta_padre)

        # Mover los archivos CSV a la carpeta nueva
        for archivo in archivos:
            if archivo.endswith('.csv'):
                ruta_archivo = os.path.join(self.carpeta_padre, archivo)
                shutil.move(ruta_archivo, self.carpeta_nueva)
                print(f'Se movió el archivo {archivo} a {self.carpeta_nueva}')

if __name__ == '__main__':
    # Ruta carpeta padre
    carpeta_padre = 'path_destiny'
    # Ruta de la carpeta nueva
    carpeta_nueva = 'path_destiny'
    # Crear instancia de la clase MoverArchivos
    mover = MoverArchivos(carpeta_padre, carpeta_nueva)
    # Llamar al método mover_csv()
    mover.mover_csv()                