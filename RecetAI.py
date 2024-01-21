import streamlit as st
from openai import OpenAI
from env import API_KEY

if API_KEY == "" : 
  key =st.secrets["APIKEY"]
# en el repo viene vacía, la cargo desde streamlit
if API_KEY != "" : 
  key = API_KEY
# si estoy desde Github Codespaces la pego en env.py
client = OpenAI(api_key=key)

def generar_dieta(ingredientes, sexo, edad):
  prompt = f"Genera una dieta semanal para un persona de sexo {sexo} y {edad} años con los siguientes ingredientes: {ingredientes}"
  print(prompt)
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
    sexo = st.selectbox('Indica tu sexo', ('masculino', 'femenino'))
    edad = st.slider('Indica tu edad', 0, 110, 41)
    # Preguntar al usuario por los ingredientes
    st.header("Ingresa los ingredientes sugeridos:")
    ingredientes = st.text_area("Ingrese los ingredientes, separados por comas", placeholder="Ingresa tus ingredientes aquí")
    if st.button('Confirmar'):
      # Generar la dieta
      if ingredientes:
        dieta = generar_dieta(ingredientes, sexo, edad)
        st.header("Dieta Semanal:")
        st.write(dieta)

if __name__ == "__main__":
    crear_dieta_semanal()
