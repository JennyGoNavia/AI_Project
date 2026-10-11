# AI_Project — Sistema de recomendación

## 1. Introducción

El proyecto consiste en desarrollar un sistema de recomendación de películas utilizando Python y GitHub Copilot como herramienta de apoyo a la programación.

## 2. Objetivo

Explorar las capacidades de la inteligencia artificial generativa para apoyar la creación de código y desarrollar un programa que recomiende películas según los géneros favoritos del usuario.

## 3. Herramientas utilizadas

- GitHub.
- GitHub Copilot.
- Visual Studio Code.
- Python.
- Git.

## 4. Desarrollo de la actividad

### 4.1 Cuenta de GitHub

Se ingresó a https://github.com con una cuenta de GitHub ya existente.

![Cuenta de GitHub](Capturas/01.cuenta.png)

### 4.2 Plan gratuito de GitHub Copilot

Se seleccionó el plan gratuito en la sección de precios y se activó GitHub Copilot Free, verificando su estado en Visual Studio Code.

![Plan gratuito](Capturas/02.plan_gratis.png)

![Copilot activo](Capturas/03.Copilot_activo.png)

### 4.3 Creación del repositorio

Se creó un repositorio llamado AI_Project, de visibilidad pública, con un archivo README y un archivo .gitignore para Python.

![Formulario del repositorio](Capturas/04.formulario_repo.png)

![Repositorio creado](Capturas/05.repo_creado.png)

### 4.4 Clonación del repositorio

Se instaló la extensión de GitHub Copilot en Visual Studio Code, se inició sesión y se clonó el repositorio con el comando `git clone` desde la terminal integrada.

![Extensión y sesión en VS Code](Capturas/06.extension_copilot.png)

![Repositorio clonado](Capturas/07.clonado.png)

### 4.5 Generación del código con Copilot

Se creó el archivo recommendation_system.py y se utilizó GitHub Copilot Chat con un prompt que solicitaba un sistema de recomendación de películas por géneros favoritos, usando funciones, listas y diccionarios, sin librerías externas.

![Archivo creado](Capturas/08.archivo_creado.png)

![Prompt y respuesta de Copilot](Capturas/09.copilot_chat.png)

![Código final](Capturas/10.codigo_final.png)

### 4.6 Ejecución y pruebas

Se ejecutó el programa desde la terminal de Visual Studio Code. Como prueba, se ingresaron los géneros acción, comedia y ciencia ficción. El sistema mostró las películas Risas en la oficina y Un día inesperado, ambas asociadas al género comedia.

![Ejecución](Capturas/11.ejecucion.png)

### 4.7 Documentación

Se documentó el proceso en el archivo README.md, con descripciones de cada paso y capturas de pantalla.

![README en VS Code](Capturas/13.Readme.png)

### 4.8 Commit y push

Los cambios se subieron a GitHub con los comandos:

```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

![Commit y push](Capturas/12.commit_push.png)

## 5. Evidencias

Las capturas de pantalla de cada paso se incluyen en la sección 4 y se encuentran en la carpeta `Capturas` del repositorio.

## 6. Conclusión

La actividad permitió aplicar GitHub Copilot como herramienta de apoyo al desarrollo de software. Se comprobó que puede ayudar a generar código inicial, pero que es necesario ejecutar y revisar el programa para verificar sus resultados.