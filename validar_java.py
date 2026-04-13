import re
import sys
import subprocess
from pathlib import Path

CAMPOS_OBLIGATORIOS = [
    "Nombre del estudiante:",
    "Fecha de creación:",
    "Asignatura:",
    "Descripción del archivo:",
    "Aspectos relevantes:",
    "Peer Review",
    "Co-evaluador:",
    "Fecha de co-evaluación:",
    "Diferencia principal frente a mi solución:",
    "Aspecto más relevante en el código revisado:"
]

def obtener_archivo_java():
    if len(sys.argv) > 1:
        archivo = Path(sys.argv[1])
        if archivo.exists() and archivo.suffix == ".java":
            return archivo
        print("No se encontró el archivo indicado o no es .java")
        sys.exit(1)

    archivos = list(Path(".").glob("*.java"))
    if len(archivos) == 1:
        return archivos[0]

    print("Debe existir un único archivo .java o indicar uno explícitamente.")
    sys.exit(1)

def validar_documentacion(contenido):
    bloque = re.search(r"/\*\*([\s\S]*?)\*/", contenido)
    faltantes = []

    if not bloque:
        return False, ["No se encontró bloque de documentación tipo Javadoc"]

    texto = bloque.group(1)

    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in texto:
            faltantes.append(campo)

    return len(faltantes) == 0, faltantes

def obtener_clase(contenido):
    m = re.search(r"public\s+class\s+(\w+)", contenido)
    return m.group(1) if m else None

def compilar(archivo):
    proc = subprocess.run(["javac", str(archivo)], capture_output=True, text=True)
    return proc.returncode == 0, proc.stderr

def ejecutar(clase):
    try:
        proc = subprocess.run(["java", clase], capture_output=True, text=True, timeout=8)
        salida = proc.stdout.strip()
        if proc.returncode != 0:
            return False, proc.stderr
        if not salida:
            return False, "No genera salida en consola"
        return True, salida
    except:
        return False, "Error en ejecución o timeout"

def main():
    archivo = obtener_archivo_java()
    contenido = archivo.read_text(encoding="utf-8", errors="ignore")

    print("\nVALIDACIÓN DE ENTREGA JAVA\n")

    # 1 Documentación
    doc_ok, faltantes = validar_documentacion(contenido)
    print("1- Documentación requerida:", "SÍ CUMPLE" if doc_ok else "NO CUMPLE")
    if faltantes:
        for f in faltantes:
            print("   - Falta:", f)

    # 2 Compilación
    compila, error = compilar(archivo)
    print("2- Compilación:", "SÍ" if compila else "NO")
    if error:
        print(error)

    # 3 Ejecución
    ejecuta = False
    if compila:
        clase = obtener_clase(contenido)
        if clase:
            ejecuta, salida = ejecutar(clase)
            print("3- Ejecución:", "SÍ" if ejecuta else "NO")
            print("   -", salida)
        else:
            print("3- Ejecución: NO (sin clase pública)")
    else:
        print("3- Ejecución: NO")

    # Resultado final
    print()
    if doc_ok and compila and ejecuta:
        print("RESULTADO FINAL: ENTREGA VÁLIDA")
    else:
        print("RESULTADO FINAL: ENTREGA NO VÁLIDA")

main()