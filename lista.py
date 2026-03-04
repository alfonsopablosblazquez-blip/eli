import os

# Carpeta donde están tus fotos y vídeos
CARPETA = "imagenes"

# Extensiones permitidas
EXTENSIONES = (".jpg", ".jpeg", ".png", ".gif", ".mp4", ".webm", ".mov")

# Lista de archivos válidos
archivos = [f"{CARPETA}/{f}" for f in os.listdir(CARPETA) if f.lower().endswith(EXTENSIONES)]

# Generar array JS
js_array = "const archivos = [\n"
for f in archivos:
    js_array += f'    "{f}",\n'
js_array += "];"

# Guardar en un archivo JS opcional
with open("archivos.js", "w") as archivo_js:
    archivo_js.write(js_array)

print("Lista generada:\n")
print("\n¡También se ha guardado en 'archivos.js' listo para usar en tu HTML!")