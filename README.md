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



## 📄 Documentación obligatoria en el archivo Java

El archivo `.java` debe incluir obligatoriamente un bloque de documentación tipo Javadoc (`/** ... */`) al inicio del archivo.

Este bloque debe contener la siguiente información completa:

- Nombre del estudiante: [Nombre completo]  
- Fecha de creación: [DD/MM/AAAA]  
- Asignatura: Programación de Computadores  
- Descripción del archivo: [Propósito general del programa]  
- Aspectos relevantes: [Elementos clave del ejercicio]  

### Peer Review

- Co-evaluador: [Nombre del compañero]  
- Fecha de co-evaluación: [DD/MM/AAAA]  
- Diferencia principal frente a mi solución: [Comparación breve]  
- Aspecto más relevante en el código revisado: [Elemento clave identificado]  

La ausencia total o parcial de esta información será considerada como **incumplimiento de los requisitos de entrega**.

---
## ⚠️ Regla de ejecución obligatoria

El programa debe ejecutarse completamente **sin requerir entrada manual por teclado**.

En caso de utilizar estructuras de entrada como `Scanner`, el estudiante deberá implementar:

- valores por defecto, o  
- validaciones que permitan la ejecución automática del programa  

La ausencia de salida en consola o la dependencia exclusiva de entrada manual impedirá la evaluación automática de la entrega.
---

## 🚀 Uso

Ubique el archivo `validar_java.py` en la misma carpeta del archivo `.java` y ejecute:

```bash
python validar_java.py MiClase.java

---

