# Práctica MLOps & LLMOps (Despliegue de algoritmos) - Fabián López

Este repositorio contiene el desarrollo integral de la práctica final de MLOps y LLMOps, dividida en dos fases principales: el procesamiento de datos masivos de reseñas de Amazon y el despliegue de una API funcional con modelos de **Hugging Face**.

## 📂 Estructura del Repositorio

Siguiendo la organización del entorno de trabajo:

*   **`data/`**: Almacenamiento de datasets locales. Incluye el archivo **`Musical_Instruments_5.json`** utilizado para el análisis inicial.
*   **`notebooks/`**: Directorio con los archivos de desarrollo principal:
    *   **`mlops-llmops-practica-final-fabian-lopez.ipynb`**: Notebook con la **Fase 1** (Análisis exploratorio y procesamiento del dataset de instrumentos musicales, incluyendo el script para actulizar el modelo definitivo en Mlflow).
    *   **`practicafcll_fastapi.py`**: Script de la API en **FastAPI** con los 5 módulos requeridos de la **Fase 2**.
*   **`mlruns/`**: Registros y logs de experimentos generados durante el ciclo de vida de los modelos.
*   **`Segunda parte práctica MLops MLLops.docx`**: Documento de entrega que contiene las capturas de pantalla de la API y las evidencias de funcionamiento.

---
## Parte 1

## 🛠️ Fase 1: Procesamiento de Datos (NLP)

En esta etapa se trabajó con el dataset de reseñas de Amazon **`Musical_Instruments_5.json`**, realizando las siguientes tareas documentadas en el notebook:
1.  **Ingesta de Datos:** Carga y normalización de estructuras JSON.
2.  **Limpieza y Preprocesamiento:** Tratamiento de valores nulos y tokenización inicial de textos.
3.  **Análisis Exploratorio:** Visualización de tendencias en las valoraciones de los usuarios sobre instrumentos musicales.

## 📈 Fase 2: Gestión del Ciclo de Vida con MLflow

Para el seguimiento de experimentos y la reproducibilidad del modelo, se ha integrado **MLflow**, cuyos registros se almacenan en el directorio local `/mlruns`.

### 🔬 Análisis y Registro de Experimentos
En el notebook `mlops-llmops-practica-final-fabian-lopez.ipynb` se han documentado las siguientes acciones:

1.  **Tracking de Parámetros:** Registro de hiperparámetros utilizados en el preprocesamiento y entrenamiento de los modelos de clasificación.
2.  **Métricas de Rendimiento:** Almacenamiento de métricas clave como *Accuracy* y *Recall* para comparar diferentes versiones de modelos.
3.  **Registro de Artefactos:** Guardado de los modelos entrenados y visualizaciones generadas directamente en el servidor de MLflow.
4.  **Análisis de Resultados:** Evaluación de la eficacia de los modelos de análisis de sentimientos aplicados al dataset de instrumentos musicales.
5.  **Nota:** El dataset fue el mismo que en la práctica de NLP, el cual estaba desbalanceado, gracias al procesamiento de las muestras y de capturar los sentimientos de las opiniones adecuadamente (stopwords sin negaciones)
   el modelo mejoró sus métricas.
---

## 🚀 Parte 2: Despliegue de API (FastAPI + Hugging Face)

Se ha desarrollado una API en **`practicafcll_fastapi.py`** que expone **5 módulos (`app.get`)** funcionales e integrados:

1.  **`/status`**: Diagnóstico de conexión y metadatos del autor.
2.  **`/hello`**: Endpoint interactivo con parámetros de consulta opcionales.
3.  **`/get-dataframe/`**: Integración con **Pandas** para la consulta dinámica de filas del dataset *Iris*.
4.  **`/text-classification`**: **Pipeline de Hugging Face** para clasificación de sentimientos (Análisis de reseñas).
5.  **`/generate-text`**: **Pipeline de Hugging Face** (GPT-2) para generación de texto autocompletado mediante *prompts*.

---

## ⚙️ Instalación y Ejecución

Para garantizar la reproducibilidad del proyecto, se ha incluido un archivo **`requirements.txt`** con todas las dependencias y versiones específicas necesarias (FastAPI, Transformers, MLflow, Pandas, etc.).

### 1. Configuración del entorno
Se recomienda el uso de un entorno virtual (Conda o venv) con **Python 3.10** para evitar conflictos de librerías:

```bash
# Crear y activar el entorno (ejemplo con Conda)
conda create -n llmops python=3.10 -y
conda activate llmops #"Nombre sugerido porque asi se llama el entorno"


---

**Autor:** Fabián López  
**Materia:** MLOps & LLMOps - BD16
**Fecha:** Marzo 2026
