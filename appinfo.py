import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------
st.set_page_config(
    page_title="Distância ERB - Comunidades Quilombolas",
    layout="wide",
    page_icon="📍"
)
# --------------------------
# FUNÇÕES AUXILIARES
# --------------------------
@st.cache_data
def carregar_dados():
    return pd.read_excel("Metadados_28_Infovias_modeladas.xlsx")

def exibir_tela_inicial():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/ASSINATURA-MCOM-2.png", width=400)

    st.markdown("# Cálculo de Distância ERB - Comunidades Quilombolas")
    st.markdown("""
        **Bem-vindo(a) ao painel interativo para análise geoespacial da distância entre ERBs e Comunidades Quilombolas.**

        **Navegue pelo menu lateral para**:
        - **Explorar mapas interativos**

        ---
    """)

# Descrições de cada Infovia
descricao_infovias = {
    "Distância ERBs - Comunidades Quilombolas":  "Análise geoespacial da distância entre ERBs e Comunidades Quilombolas ",
     
}



def exibir_mapa(df):
    # --------------------------
    # FILTROS NA BARRA LATERAL
    # --------------------------
    with st.sidebar:
        st.header("🎚️ Seleção de Mapas")
        with st.expander("Mapas", expanded=True):
            opcoes_distancia = [
                "Distância ERBs - Comunidades Quilombolas"
            ]
            filtro_distancia = st.radio("Selecione:", opcoes_distancia)

    # Mostra a descrição da Infovia selecionada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/ASSINATURA-MCOM-2.png", width=400)
    st.markdown(f"### ℹ️ Análise {filtro_distancia}")
    st.markdown(descricao_infovias.get(filtro_distancia, "Descrição não disponível."))

    # --------------------------
    # MAPA INTERATIVO
    # --------------------------
    st.subheader("🗺️ Mapa Interativo")

    # Caminho do arquivo HTML correspondente à Infovia selecionada
    caminho_html = f"mapas/{filtro_distancia}.html"

    try:
        with open(caminho_html, "r", encoding="utf-8") as f:
            mapa_html = f.read()
        components.html(mapa_html, height=800, width=1100, scrolling=False)
    except FileNotFoundError:
        st.error(f"Mapa HTML para '{filtro_distancia}' não encontrado. Verifique se o arquivo '{caminho_html}' existe.")

# --------------------------
# EXECUÇÃO
# --------------------------
df = carregar_dados()

# Menu de navegação
st.sidebar.title("📁 Navegação")
pagina = st.sidebar.radio("Ir para:", ["🏠 Início", "🗺️ Mapa Interativo"])

if pagina == "🏠 Início":
    exibir_tela_inicial()
elif pagina == "🗺️ Mapa Interativo":
    exibir_mapa(df)

