import streamlit as st

st.set_page_config(
    page_title="SOCOVAL | Automatizaciones",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

automatizaciones = [
    {
        "nombre": "Control de Facturas",
        "descripcion": "Procesa el CSV de SAP y genera un Excel con facturas vencidas y por vencer.",
        "pagina": "pages/01_transformacion_excel.py",
        "icono": "📊",
        "departamento": "Compras",
        "activa": True
    },
]

colores_depto = {
    "Compras":     "#1B3A6B",
    "Operaciones": "#E87722",
    "Mantencion":  "#2D9E5F",
    "RRHH":        "#7B3FA0",
    "Bodega":      "#C0392B",
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap');
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], .main, .block-container {
    background-color: #F4F6F9 !important;
    font-family: 'DM Sans', 'Segoe UI', sans-serif !important;
}
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stHeader"] { display: none !important; }
.stDeployButton { display: none !important; }
.block-container { padding: 2rem 3rem !important; max-width: 1100px !important; }

.firma {
    position: fixed;
    bottom: 14px;
    right: 18px;
    font-size: 0.68rem;
    color: #1B3A6B;
    opacity: 0.25;
    letter-spacing: 0.02em;
    pointer-events: none;
}

.topbar {
    background: #1B3A6B;
    padding: 24px 32px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 32px;
}
.topbar-left { display: flex; align-items: center; gap: 16px; }
.topbar-accent { width: 4px; height: 44px; background: #E87722; border-radius: 4px; }
.topbar-title { color: #fff; font-size: 1.3rem; font-weight: 600; margin: 0; }
.topbar-sub { color: #7A9BC4; font-size: 0.82rem; margin-top: 3px; }
.topbar-badge {
    background: rgba(232,119,34,0.15);
    color: #E87722;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 5px 14px;
    border-radius: 20px;
    border: 1px solid rgba(232,119,34,0.3);
}
.depto-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 24px 0 14px 0;
}
.depto-dot { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; }
.depto-name {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: #8A96A8;
    white-space: nowrap;
}
.depto-line { flex: 1; height: 1px; background: #E2E8F0; }

.card-wrapper {
    background: #FFFFFF;
    border: 1px solid #E8ECF2;
    border-radius: 14px 14px 0 0;
    padding: 22px 16px 16px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    margin-bottom: 0;
}
.card-icon { font-size: 2.2rem; }
.card-title { font-size: 0.92rem; font-weight: 600; color: #1B3A6B; margin: 0; }
.card-desc { font-size: 0.78rem; color: #8A96A8; line-height: 1.55; margin: 0; }
.tag-activa {
    background: #EAF2FF;
    color: #1B3A6B;
    font-size: 0.68rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
}
.tag-pronto {
    background: #F1F3F6;
    color: #A0A8B4;
    font-size: 0.68rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
}
.card-pronto {
    background: #FFFFFF;
    border: 1px solid #E8ECF2;
    border-radius: 14px;
    padding: 22px 16px 16px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
}

/* Botón ancho completo pegado a la tarjeta */
div[data-testid="stButton"] button {
    width: 100% !important;
    background-color: #1B3A6B !important;
    color: #fff !important;
    border: none !important;
    border-radius: 0 0 14px 14px !important;
    padding: 10px 0 !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    margin-top: 0 !important;
    cursor: pointer !important;
    letter-spacing: 0.3px !important;
}
div[data-testid="stButton"] button:hover {
    background-color: #E87722 !important;
    color: #fff !important;
    border: none !important;
}
div[data-testid="stButton"] {
    margin-top: -8px !important;
}
</style>
""", unsafe_allow_html=True)

total = len(automatizaciones)
activas = sum(1 for a in automatizaciones if a["activa"])

st.markdown(f"""
<div class="topbar">
    <div class="topbar-left">
        <div class="topbar-accent"></div>
        <div>
            <div class="topbar-title">⚙️ SOCOVAL</div>
            <div class="topbar-sub">Panel de automatizaciones internas</div>
        </div>
    </div>
    <div class="topbar-badge">{activas} activa{"s" if activas != 1 else ""} de {total}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="firma">Automatizaciones desarrolladas por Pedro Muñoz Ballier</div>', unsafe_allow_html=True)

departamentos = {}
for auto in automatizaciones:
    depto = auto["departamento"]
    if depto not in departamentos:
        departamentos[depto] = []
    departamentos[depto].append(auto)

for depto, items in departamentos.items():
    color = colores_depto.get(depto, "#1B3A6B")
    st.markdown(f"""
    <div class="depto-header">
        <div class="depto-dot" style="background:{color};"></div>
        <div class="depto-name">{depto}</div>
        <div class="depto-line"></div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4, gap="small")
    for i, auto in enumerate(items):
        with cols[i % 4]:
            tag = '<span class="tag-activa">● Disponible</span>' if auto["activa"] else '<span class="tag-pronto">Proximamente</span>'
            border_top = color if auto["activa"] else "#E8ECF2"

            if auto["activa"]:
                st.markdown(f"""
                <div class="card-wrapper" style="border-top: 3px solid {border_top};">
                    <div class="card-icon">{auto['icono']}</div>
                    <div class="card-title">{auto['nombre']}</div>
                    <div class="card-desc">{auto['descripcion']}</div>
                    {tag}
                </div>
                """, unsafe_allow_html=True)
                if st.button("Abrir →", key=f"btn_{i}"):
                    st.switch_page(auto["pagina"])
            else:
                st.markdown(f"""
                <div class="card-pronto" style="border-top: 3px solid {border_top};">
                    <div class="card-icon">{auto['icono']}</div>
                    <div class="card-title">{auto['nombre']}</div>
                    <div class="card-desc">{auto['descripcion']}</div>
                    {tag}
                </div>
                """, unsafe_allow_html=True)
