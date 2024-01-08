import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

def generar_dieta(ingredientes):
  prompt = f"Genera una dieta semanal con los siguientes ingredientes: {ingredientes}"

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ]
  )

  dieta = response.choices[0].message.content

  return dieta

def crear_dieta_semanal():
    st.title("Creador de Dieta Semanal")

    # Preguntar al usuario por los ingredientes
    st.header("Ingresa los ingredientes sugeridos:")
    ingredientes = st.text_area("Ingrese los ingredientes, separados por comas")
    if ingredientes :
      # Generar la dieta
      dieta = generar_dieta(ingredientes)
      st.header("Dieta Semanal:")
      st.write(dieta)

if __name__ == "__main__":
    crear_dieta_semanal()
