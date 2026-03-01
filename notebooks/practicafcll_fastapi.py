from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional
import pandas as pd 
from transformers import pipeline

# Esta variable DEBE llamarse 'app' en minúsculas
app = FastAPI()

#Estado del sistema
@app.get('/status')
def get_status():
    return {
        "status": "online", 
        "owner": "Fabian Lopez", 
        "file": "practicafcll_fastapi.py"
    }

#Saludo simple
@app.get('/hello')
def say_hello(name: Optional[str] = "Student"):
    return {"message": f"Hola {name}, bienvenido a la practica"}

#Lectura de dataframe
@app.get('/get-dataframe/')
def read_dataframe_properties(position: int = 0): 
    try:
        # Añadimos 'on_bad_lines' para saltar errores de formato en el CSV
        url = 'https://raw.githubusercontent.com'
        df = pd.read_csv(url, on_bad_lines='skip')
        
        # Validación de rango
        if position < 0 or position >= len(df):
            return {"error": f"Posicion {position} fuera de rango (0 a {len(df)-1})"}
        
        # Convertimos la fila a un diccionario estándar
        return {"posicion": position, "datos": df.iloc[position].to_dict()}
        
    except Exception as e:
        return {"error": f"Error crítico al procesar el CSV: {str(e)}"}



#Detecta idioma. Pipeline de Hugging Face
@app.get('/detect-language')
def detect_lang(text: str = "Hola mundo"):
    # Identifica el idioma del texto proporcionado
    lang_pipe = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
    return {"input": text, "detection": lang_pipe(text)}

#Generación de Texto. Pipeline Hugging Face
@app.get('/generate-text')
def generate_text(prompt: str = "Once upon a time"):
    try:
        # Usamos 'text-generation' que sí aparece en tu lista de tareas disponibles
        generator = pipeline("text-generation", model="sshleifer/tiny-gpt2")
        
        # Generamos la continuación del texto
        result = generator(prompt, max_length=30, num_return_sequences=1)
        
        # Retornamos el texto generado (accediendo correctamente a la lista del pipeline)
        return {"input": prompt, "generated": result[0]['generated_text']}
    except Exception as e:
        return {"error": str(e)}
    


