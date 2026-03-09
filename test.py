import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
preguntas = [
    {
        "texto": "¿En qué año se descubrió América?",
        "opciones": ["2026", "1442", "1492", "América no existe"],
        "correcta": "1492"
    },
    {
        "texto": "¿Cómo se dice night en español?",
        "opciones": ["", "nadie", "noche", "nochaves?"],
        "correcta": "noche"
    },
    {
        "texto": "¿En qué año ganó España el Mundial?",
        "opciones": ["", "2006", "2014", "2010"],
        "correcta": "2010"
    },
    {
        "texto": "¿Cuántos balones de oro ganó Pelé?",
        "opciones": ["", "ninguno", "5", "los balones son de cuero", "1, pero lo rompió"],
        "correcta": "ninguno"
    },
    {
        "texto": "¿Quién ha ganado la copa del rey de baloncesto 2026?",
        "opciones": ["", "Valencia basquet", "Baskonia", "Real Madrid", "Messi"],
        "correcta": "Baskonia"
    },
    {
        "texto": "¿Cómo es conocida la copa de la Champions?",
        "opciones": ["", "La Orejona", "La Narizona", "La Buenorra", "La Copa"],
        "correcta": "La Orejona"
    },
    {
        "texto": "¿Cómo se llama en realidad Koke Resurrección??",
        "opciones": ["", "Pablo", "Jorge", "Roberto", "Antonia"],
        "correcta": "Jorge"
    },
    {
        "texto": "¿Quién ha ganado el SuperBalón de Oro?",
        "opciones": ["", "Di Stefano", "Messi", "Ronaldo", "Oyarzabal"],
        "correcta": "Di Stefano"
    },
    {
        "texto": "¿Quién le llama mono a Vinicius?",
        "opciones": ["", "Maffeo", "Los madridistas", "El Cholo", "Todas son correctas"],
        "correcta": "Todas son correctas"
    },
    {
        "texto": "¿Cuántas preguntas tiene este examen?",
        "opciones": ["", "ninguna, obvio", "10", "9", "11"],
        "correcta": "10"
    }
]

# Configuración visual
st.title("Examen de Cultura General")
st.write("Responde a las preguntas y pulsa el botón para ver tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio(
            "Elige una opción:",
            pregunta["opciones"],
            key=pregunta["texto"]
        )
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

if boton_enviar:

    aciertos = 0
    errores = 0
    informe = []

    total = len(preguntas)

    for i in range(total):

        respuesta = respuestas_usuario[i]
        correcta = preguntas[i]["correcta"]
        texto = preguntas[i]["texto"]

        if respuesta == "":
            informe.append(f"- {texto} → Sin responder")
        elif respuesta == correcta:
            aciertos += 1
            informe.append(f"- {texto} → Correcta")
        else:
            errores += 1
            informe.append(f"- {texto} → Incorrecta (correcta: {correcta})")

    # Penalización por fallos
    puntuacion = aciertos - errores

    # Evitar nota negativa
    if puntuacion < 0:
        puntuacion = 0

    nota = round((puntuacion / total) * 10, 2)

    st.divider()

    # Tabs
    tab1, tab2 = st.tabs(["Resultado", "Informe"])

    with tab1:

        st.header(f"Resultado final: {nota} / 10")

        if nota < 2:
            st.error("Muy insuficiente")
        elif nota < 5:
            st.warning("Insuficiente")
        elif nota < 6:
            st.info("Suficiente")
            st.balloons()
        elif nota < 7:
            st.success("Bien")
            st.balloons()
        elif nota < 9:
            st.success("Notable")
            st.balloons()
        elif nota < 10:
            st.success("Sobresaliente")
            st.balloons()
        else:
            st.success("Excelente")
            st.balloons()

    with tab2:

        st.header("Informe del examen")

        st.markdown("\n".join(informe))
