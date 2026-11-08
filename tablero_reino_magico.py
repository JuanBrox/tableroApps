import streamlit as st

st.set_page_config(page_title="Reino Mágico de Carla", page_icon="🦄", layout="wide")

# Asignaturas en orden, con su emoji. Cada app: (emoji, título, descripción, url)
# Las apps con url "" aparecen como "Próximamente": pega la URL cuando la tengas.
MATERIAS = [
    ("🔢 Matemáticas", [
        ("🔢", "Unidad 1", "Números de cuatro cifras, comparar y aproximar.", "https://matematicasu1.streamlit.app/"),
        ("➕", "Unidad 2", "Sumas y restas.", "https://matematicasu2.streamlit.app/"),
        ("✖️", "Tablas de multiplicar", "Todas las tablas del 1 al 10.", "https://tablasmultiplicar.streamlit.app/"),
        ("🏛️", "Números romanos", "Aprende y practica los ejercicios de la libreta.", "https://numerosromanos.streamlit.app/"),
        ("🎲", "Tu tablero de juego", "Tablero mágico con puntos y normas.", "https://juegomates.streamlit.app/"),
    ]),
    ("📚 Lengua", [
        ("📣", "Elementos de la comunicación", "Emisor, receptor, mensaje, canal, código y contexto.", "https://lengua3p-l1.streamlit.app/"),
        ("📝", "Unidad 2", "Diminutivos, aumentativos, punto y adjetivo.", "https://unidad2lengua3p.streamlit.app/"),
        ("✨", "Sinónimos y antónimos", "El reino de las palabras mágicas.", "https://antonimossinonimos.streamlit.app/"),
    ]),
    ("🏰 Valenciano", [
        ("🏰", "Oracions i ordre alfabètic", "Repaso para la Proba de València.", "https://valenciano-1.streamlit.app/"),
    ]),
    ("🇬🇧 Inglés", [
        ("🔤", "Abecedario en inglés", "Aprende el ABC y deletrea tu nombre.", "https://abcenglish.streamlit.app/"),
    ]),
    ("🌿 Conocimiento del Medio", [
        ("🌿", "Unidad 1", "Seres vivos, reinos y paisajes.", "https://conocimientodelmediou1.streamlit.app/"),
        ("📖", "Página 38", "Repaso de la página 38 del libro.", "https://conocimientopag38.streamlit.app/"),
    ]),
    ("🧚 Mente ágil", [
        ("🧚", "Reino de la Mente Ágil", "Emociones, concentración y juegos de memoria.", "https://agilidadmental.streamlit.app/"),
    ]),
]

st.markdown(
    """
<style>
.stApp {background: linear-gradient(160deg,#fff0fb 0%,#ece6ff 50%,#e0f7ff 100%);}
h1.titulo {text-align:center; color:#9b3fd0; font-size:2.6rem; margin-bottom:0;}
p.sub {text-align:center; color:#6b5b95; font-size:1.1rem; margin-bottom:1rem;}
h2.materia {color:#a0267f; border-bottom:3px dashed #f3c6ef; padding-bottom:4px; margin-top:1.5rem;}
.card {background:#fffffff2; border:3px solid #f3c6ef; border-radius:24px; padding:18px;
       min-height:170px; box-shadow:0 6px 18px #c58be655; margin-bottom:8px;}
.card .emo {font-size:2.4rem;}
.card h3 {color:#7a2fb0; margin:.2rem 0;}
.card p {color:#4b4565; margin-top:.4rem;}
</style>
<h1 class="titulo">🦄 Reino Mágico de Carla 🧚</h1>
<p class="sub">Elige una asignatura y ¡a aprender jugando!</p>
""",
    unsafe_allow_html=True,
)

for materia, apps in MATERIAS:
    st.markdown(f'<h2 class="materia">{materia}</h2>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (emo, titulo, desc, url) in enumerate(apps):
        with cols[i % 3]:
            st.markdown(
                f'<div class="card"><div class="emo">{emo}</div><h3>{titulo}</h3><p>{desc}</p></div>',
                unsafe_allow_html=True,
            )
            if url:
                st.link_button("✨ Abrir", url, use_container_width=True)
            else:
                st.button("🔒 Próximamente", disabled=True, key=f"{materia}{i}", use_container_width=True)

st.caption("🌈 Hecho con magia para Carla")
