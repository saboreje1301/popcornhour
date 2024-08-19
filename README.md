PopcornHour

# PopcornHour

## Descripción

PopcornHour es una aplicación web que permite a los usuarios buscar y explorar contenido multimedia. Los usuarios pueden realizar búsquedas de títulos en español y en su idioma original, y ver los resultados en una interfaz amigable y visualmente atractiva.

## Características

- **Búsqueda de Contenido**: Los usuarios pueden buscar contenido utilizando palabras clave. Los resultados de la búsqueda se muestran en tarjetas con información relevante.
- **Interfaz Responsiva**: La aplicación está diseñada para ser responsiva y funcionar bien en dispositivos móviles y de escritorio.
- **Modo Oscuro**: Soporte para modo oscuro para una mejor experiencia de usuario en condiciones de poca luz.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/popcornhour.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd popcornhour
    ```
3. Crea un entorno virtual:
    ```bash
    python3 -m venv .venv
    ```
4. Activa el entorno virtual:
    ```bash
    source .venv/bin/activate
    ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicia la aplicación:
    ```bash
    flask run
    ```
2. Abre tu navegador web y navega a `http://127.0.0.1:5000`.

## Estructura del Proyecto

- `app/`: Contiene el código principal de la aplicación.
  - `__init__.py`: Inicializa la aplicación Flask.
  - `routes.py`: Define las rutas de la aplicación.
  - `templates/`: Contiene las plantillas HTML.
  - `static/`: Contiene archivos estáticos como CSS y JavaScript.
- `run.py`: Archivo principal para ejecutar la aplicación.

## Ejemplo de Uso

1. En la página principal, utiliza la barra de búsqueda para buscar contenido.
2. Los resultados de la búsqueda se mostrarán en tarjetas con información como el título en español, el título original y el año de lanzamiento.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
