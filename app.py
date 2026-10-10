```python
import streamlit as st

st.set_page_config(
    page_title="GM Consultoria UAN",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f7fffc, #ffffff, #f5fbf8);
}
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero, .company-band {
    background: linear-gradient(135deg, #0d6b5b, #168b73);
    color: white;
    padding: 35px 25px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 25px;
}
.hero h1, .hero p, .company-band h3 {
    color: white !important;
}
.hero p {
    line-height: 1.7;
}
.section-title {
    color: #0d6b5b;
    font-size: 27px;
    font-weight: 800;
    text-align: center;
    margin: 35px 0 12px;
}
.section-subtitle {
    color: #53635e;
    text-align: center;
    line-height: 1.7;
    margin: 0 auto 25px;
    max-width: 850px;
}
.service-card, .plan, .document-card {
    background: white;
    border: 1px solid #dcefe7;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(13, 107, 91, .05);
}
.service-card {
    min-height: 220px;
}
.service-card h3, .plan h3 {
    color: #0d6b5b;
}
.service-card p, .plan p {
    color: #53635e;
    line-height: 1.7;
}
.audience {
    background: #e8f7f0;
    border: 1px solid #cfe9df;
    color: #0d6b5b;
    padding: 18px 10px;
    border-radius: 12px;
    text-align: center;
    font-weight: 700;
    margin-bottom: 12px;
}
.plan {
    text-align: center;
    min-height: 180px;
}
.check {
    color: #0d806b;
    font-weight: bold;
    margin-right: 8px;
}
.company-band {
    margin-top: 28px;
}
.cta {
    background: #e8f7f0;
    border: 1px solid #cfe9df;
    padding: 30px 20px;
    border-radius: 16px;
    text-align: center;
    margin: 30px 0 25px;
}
.cta h2 {
    color: #0d6b5b;
}
.cta p {
    color: #33423e;
    line-height: 1.8;
}
.whatsapp {
    display: inline-block;
    background: #25D366;
    color: white !important;
    padding: 13px 24px;
    border-radius: 9px;
    text-decoration: none !important;
    font-weight: 800;
    margin-top: 12px;
}
.whatsapp:hover {
    background: #1eaf54;
}
.footer {
    text-align: center;
    color: #53635e;
    font-size: 13px;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)


def titulo(texto, subtitulo=None):
    st.markdown(
        f'<div class="section-title">{texto}</div>',
        unsafe_allow_html=True,
    )
    if subtitulo:
        st.markdown(
            f'<div class="section-subtitle">{subtitulo}</div>',
            unsafe_allow_html=True,
        )


def cartao(classe, titulo, descricao=None):
    conteudo = f"<h3>{titulo}</h3>"
    if descricao:
        conteudo += f"<p>{descricao}</p>"
    st.markdown(
        f'<div class="{classe}">{conteudo}</div>',
        unsafe_allow_html=True,
    )


# Cabeçalho
st.markdown("""
<div class="hero">
    <div><strong>🥗 Nutrição em Alimentação Coletiva</strong></div>
    <h1>GM CONSULTORIA ALIMENTAR</h1>
    <p>
        <strong>Consultoria UAN para empresas e estabelecimentos
        de alimentação.</strong><br>
        Responsabilidade Técnica, organização, segurança alimentar
        e adequação às Boas Práticas.
    </p>
</div>
""", unsafe_allow_html=True)


# Apresentação
titulo(
    "🥗 Consultoria especializada",
    "A GM Consultoria Alimentar oferece suporte técnico para "
    "empresas do setor de alimentação, auxiliando na organização "
    "dos processos, na qualidade e nas boas práticas de manipulação."
)


# Serviços
titulo("Nossos serviços")

servicos = [
    ("👩‍⚕️ Responsabilidade Técnica (RT)",
     "Atuação conforme as atribuições legais e o escopo contratado."),
    ("📋 Manual de Boas Práticas e POPs",
     "Elaboração, revisão e orientação para implantação de documentos."),
    ("🍽️ Cardápios e Fichas Técnicas",
     "Padronização de preparações, custos e aproveitamento dos alimentos."),
    ("🔍 Auditorias e Visitas Técnicas",
     "Avaliação de rotinas e orientação para melhorias."),
    ("🧑‍🍳 Treinamento de Manipuladores",
     "Orientação sobre higiene, manipulação segura e prevenção de contaminação."),
    ("📊 Qualidade e Desperdício",
     "Apoio ao controle de perdas e à melhoria dos processos."),
]

colunas = st.columns(3, gap="medium")
for i, (nome, descricao) in enumerate(servicos):
    with colunas[i % 3]:
        cartao("service-card", nome, descricao)


# Público atendido
titulo(
    "Para quem trabalhamos?",
    "Atendimento para estabelecimentos que desejam melhorar "
    "seus processos e fortalecer a segurança dos alimentos."
)

publicos = [
    "🍞 Padarias", "🍔 Lanchonetes", "🍴 Restaurantes",
    "🏭 Cozinhas industriais", "🏨 Hotéis", "🏫 Escolas e instituições",
]

colunas = st.columns(3, gap="medium")
for i, publico in enumerate(publicos):
    with colunas[i % 3]:
        st.markdown(
            f'<div class="audience">{publico}</div>',
            unsafe_allow_html=True,
        )


# Documentação
titulo(
    "📋 Documentação e adequação sanitária",
    "Apoio à organização documental e às rotinas de higiene, "
    "considerando as características do estabelecimento e as normas aplicáveis."
)

documentos = [
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPs",
    "Orientação sobre documentação sanitária",
    "Controle de qualidade",
    "Treinamento de manipuladores",
    "Verificação de higiene e manipulação",
]

colunas = st.columns(2, gap="medium")
for i, documento in enumerate(documentos):
    with colunas[i % 2]:
        st.markdown(
            f'<div class="document-card">'
            f'<span class="check">✓</span>{documento}</div>',
            unsafe_allow_html=True,
        )


# Planos
titulo(
    "📅 Planos de acompanhamento",
    "A frequência das visitas e as atividades são definidas "
    "conforme as necessidades e o contrato."
)

planos = [
    ("Mensal", "Acompanhamento contínuo e visitas programadas."),
    ("Trimestral", "Avaliação periódica e planejamento de melhorias."),
    ("Semestral", "Revisão de rotinas, documentos e adequações."),
    ("Anual", "Planejamento e acompanhamento conforme o contrato."),
]

colunas = st.columns(4, gap="medium")
for coluna, (periodo, descricao) in zip(colunas, planos):
    with coluna:
        cartao("plan", periodo, descricao)


# Diferenciais
titulo("Nossos diferenciais")

diferenciais = [
    "Atendimento conforme as necessidades do estabelecimento",
    "Foco na segurança dos alimentos",
    "Organização de documentos e procedimentos",
    "Apoio à melhoria contínua dos processos",
]

for item in diferenciais:
    st.markdown(
        f'<div class="document-card">'
        f'<span class="check">✓</span>{item}</div>',
        unsafe_allow_html=True,
    )


# Faixa institucional
st.markdown("""
<div class="company-band">
    <h3>GM CONSULTORIA ALIMENTAR</h3>
    <p>
        Responsabilidade Técnica • Consultoria UAN •
        Boas Práticas • Segurança dos Alimentos
    </p>
</div>
""", unsafe_allow_html=True)


# Contato
st.markdown("""
<div class="cta">
    <h2>📲 Fale agora com uma Especialista</h2>
    <p>Agende uma avaliação do seu estabelecimento.</p>
    <p><strong>📞 Telefone/WhatsApp: (61) 99927-7063</strong></p>
    <a class="whatsapp"
       href="https://wa.me/5561999277063"
       target="_blank"
       rel="noopener noreferrer">
       💬 Chamar no WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)


# Rodapé
st.markdown("""
<div class="footer">
    <p><strong>GM Consultoria Alimentar</strong></p>
    <p>Nutricionista RT | Consultoria em Unidade de Alimentação e Nutrição (UAN)</p>
    <p>© 2026 — Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
```
