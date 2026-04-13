# Validador de Entregas Java

Este repositorio permite validar automáticamente una entrega en Java considerando:

1. Presencia de documentación obligatoria tipo Javadoc
2. Compilación del archivo
3. Ejecución correcta con salida en consola

---

## 📌 Requisitos

- Python 3
- Java JDK instalado (javac y java en consola)

---

## 🚀 Uso

Ubique el archivo `validar_java.py` en la misma carpeta del archivo `.java` y ejecute:

```bash
python validar_java.py MiClase.java

---

## ⚠️ Regla de ejecución obligatoria

El programa debe ejecutarse completamente **sin requerir entrada manual por teclado**.

En caso de utilizar estructuras de entrada como `Scanner`, el estudiante deberá implementar:

- valores por defecto, o  
- validaciones que permitan la ejecución automática del programa  

La ausencia de salida en consola o la dependencia exclusiva de entrada manual impedirá la evaluación automática de la entrega.
