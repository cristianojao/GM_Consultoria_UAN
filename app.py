
import streamlit as st

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Nutricionista RT | Consultoria UAN",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==========================================================
# CSS - IDENTIDADE VISUAL
# ==========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            180deg,
            #f7fffc 0%,
            #ffffff 48%,
            #f5fbf8 100%
        );
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* DESTAQUE PRINCIPAL */
    .hero {
        background: linear-gradient(135deg, #0d6b5b, #168b73);
        color: #ffffff;
        padding: 42px 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(13, 107, 91, 0.18);
        margin-bottom: 28px;
    }

    .hero-kicker {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    .hero h1 {
        color: #ffffff !important;
        font-size: clamp(30px, 5vw, 44px);
        line-height: 1.2;
        margin-bottom: 18px;
    }

    .hero p {
        color: #ffffff !important;
        font-size: 17px;
        max-width: 850px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* TÍTULOS DAS SEÇÕES */
    .section-title {
        color: #0d6b5b;
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        margin-top: 35px;
        margin-bottom: 12px;
    }

    .section-subtitle {
        color: #53635e;
        font-size: 16px;
        text-align: center;
        line-height: 1.7;
        max-width: 850px;
        margin: 0 auto 25px auto;
    }

    /* CARTÕES DE SERVIÇOS */
    .service-card {
        background: #ffffff;
        border: 1px solid #dcefe7;
        border-radius: 16px;
        padding: 24px 20px;
        min-height: 225px;
        margin-bottom: 18px;
        box-shadow: 0 5px 18px rgba(13, 107, 91, 0.06);
    }

    .service-card h3 {
        color: #0d6b5b;
        font-size: 20px;
        margin-bottom: 12px;
    }

    .service-card p {
        color: #53635e;
        font-size: 15px;
        line-height: 1.7;
    }

    /* PÚBLICO ATENDIDO */
    .audience {
        background: #e8f7f0;
        border: 1px solid #cfe9df;
        border-radius: 12px;
        padding: 20px 10px;
        text-align: center;
        color: #0d6b5b;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* DOCUMENTAÇÃO */
    .document-card {
        background: #ffffff;
        border: 1px solid #dcefe7;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        color: #33423e;
        line-height: 1.5;
    }

    .check {
        color: #0d806b;
        font-weight: 800;
        margin-right: 8px;
    }

    /* PLANOS */
    .plan {
        background: #ffffff;
        border: 1px solid #cfe9df;
        border-radius: 16px;
        padding: 28px 12px;
        text-align: center;
        box-shadow: 0 5px 18px rgba(13, 107, 91, 0.06);
        margin-bottom: 16px;
    }

    .plan h3 {
        color: #0d6b5b;
        font-size: 21px;
    }

    .plan p {
        color: #53635e;
        font-size: 14px;
        line-height: 1.6;
    }

    /* CONTATO */
    .contact {
        background: #e8f7f0;
        border: 1px solid #cfe9df;
        padding: 30px 22px;
        border-radius: 16px;
        text-align: center;
        margin-top: 25px;
    }

    .contact h2 {
        color: #0d6b5b;
    }

    .contact p {
        color: #33423e;
        line-height: 1.8;
    }

    .whatsapp-button {
        display: inline-block;
        background: #25D366;
        color: #ffffff !important;
        padding: 13px 24px;
        border-radius: 9px;
        text-decoration: none !important;
        font-weight: 800;
        margin-top: 12px;
    }

    .whatsapp-button:hover {
        background: #1eaf54;
    }

    /* FAIXA DA EMPRESA */
    .company-band {
        background: linear-gradient(135deg, #0d6b5b, #168b73);
        color: #ffffff;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        margin-top: 28px;
    }

    .company-band h3 {
        color: #ffffff !important;
    }

    /* RODAPÉ */
    .footer {
        text-align: center;
        color: #53635e;
        font-size: 13px;
        padding-top: 24px;
    }

    /* AJUSTES DE TEXTO DO STREAMLIT */
    h2, h3 {
        color: #0d6b5b;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# CABEÇALHO PRINCIPAL
# ==========================================================
st.markdown("""
<div class="hero">
    <div class="hero-kicker">🥗 Nutrição em Alimentação Coletiva</div>
    <h1>GM CONSULTORIA ALIMENTAR</h1>
    <p>
        <strong>Consultoria UAN para empresas e estabelecimentos de alimentação.</strong><br>
        Responsabilidade Técnica, organização, segurança alimentar e adequação às Boas Práticas.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# APRESENTAÇÃO
# ==========================================================
st.markdown(
    '<div class="section-title">🥗 Consultoria especializada</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        A GM Consultoria Alimentar oferece suporte técnico para
        empresas e estabelecimentos do setor de alimentação,
        auxiliando na organização dos processos, na melhoria da
        qualidade e na adoção de boas práticas de manipulação.
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# SERVIÇOS
# ==========================================================
st.markdown(
    '<div class="section-title">Nossos serviços</div>',
    unsafe_allow_html=True,
)

servicos = [
    (
        "👩‍⚕️ Responsabilidade Técnica (RT)",
        "Atuação profissional em responsabilidade técnica, conforme "
        "as atribuições legais, as exigências aplicáveis e o escopo "
        "contratado para o estabelecimento."
    ),
    (
        "📋 Manual de Boas Práticas e POPs",
        "Elaboração, revisão e orientação para implantação de "
        "documentos e procedimentos de higiene e segurança dos alimentos."
    ),
    (
        "🍽️ Cardápios e Fichas Técnicas",
        "Elaboração e avaliação de cardápios e fichas técnicas de "
        "preparação, com atenção à padronização, aos custos e ao "
        "aproveitamento dos alimentos."
    ),
    (
        "🔍 Auditorias e Visitas Técnicas",
        "Verificação das rotinas do estabelecimento, identificação "
        "de oportunidades de melhoria e orientação para adequação "
        "dos procedimentos."
    ),
    (
        "🧑‍🍳 Treinamento de Manipuladores",
        "Orientação das equipes sobre higiene pessoal, manipulação "
        "segura, prevenção de contaminação e boas práticas."
    ),
    (
        "📊 Controle de Qualidade e Desperdício",
        "Apoio à organização dos processos, ao controle de perdas "
        "e à melhoria da qualidade na produção de alimentos."
    ),
]

service_cols = st.columns(3, gap="medium")

for i, (titulo, descricao) in enumerate(servicos):
    with service_cols[i % 3]:
        st.markdown(
            f"""
            <div class="service-card">
                <h3>{titulo}</h3>
                <p>{descricao}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================================
# PÚBLICO ATENDIDO
# ==========================================================
st.markdown(
    '<div class="section-title">Para quem trabalhamos?</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Atendimento direcionado a estabelecimentos que desejam
        melhorar seus processos e fortalecer a segurança dos alimentos.
    </div>
    """,
    unsafe_allow_html=True,
)

audiencias = [
    "🍞 Padarias",
    "🍔 Lanchonetes",
    "🍴 Restaurantes",
    "🏭 Cozinhas industriais",
    "🏨 Hotéis",
    "🏫 Escolas e instituições",
]

audience_cols = st.columns(3, gap="medium")

for i, publico in enumerate(audiencias):
    with audience_cols[i % 3]:
        st.markdown(
            f'<div class="audience">{publico}</div>',
            unsafe_allow_html=True,
        )

# ==========================================================
# DOCUMENTAÇÃO E ADEQUAÇÃO
# ==========================================================
st.markdown(
    '<div class="section-title">📋 Documentação e adequação sanitária</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Apoio à organização documental e aos procedimentos de higiene
        e segurança dos alimentos, considerando as características
        do estabelecimento e as normas sanitárias aplicáveis.
    </div>
    """,
    unsafe_allow_html=True,
)

documentos = [
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPs",
    "Orientação sobre documentação sanitária",
    "Orientação para controle de qualidade",
    "Treinamento e orientação dos manipuladores",
    "Verificação das rotinas de higiene e manipulação",
]

doc_cols = st.columns(2, gap="medium")

for i, documento in enumerate(documentos):
    with doc_cols[i % 2]:
        st.markdown(
            f"""
            <div class="document-card">
                <span class="check">✓</span>{documento}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================================
# PLANOS DE ACOMPANHAMENTO
# ==========================================================
st.markdown(
    '<div class="section-title">📅 Planos de acompanhamento</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        O acompanhamento pode ser planejado conforme as necessidades
        do estabelecimento, a frequência das visitas e os serviços
        definidos na proposta comercial.
    </div>
    """,
    unsafe_allow_html=True,
)

planos = [
    (
        "Mensal",
        "Acompanhamento contínuo, com atividades e visitas"
        "definidas conforme o contrato."
    ),
    (
        "Trimestral",
        "Acompanhamento periódico para avaliar processos e"
        "planejar melhorias."
    ),
    (
        "Semestral",
        "Revisão programada das rotinas, documentos e"
        "necessidades de adequação."
    ),
    (
        "Anual",
        "Planejamento de ações e acompanhamento conforme"
        "o escopo contratado."
    ),
]

plan_cols = st.columns(4, gap="medium")

for col, (periodo, descricao) in zip(plan_cols, planos):
    with col:
        st.markdown(
            f"""
            <div class="plan">
                <h3>{periodo}</h3>
                <p>{descricao}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================================
# DIFERENCIAIS
# ==========================================================
st.markdown(
    '<div class="section-title">Nossos diferenciais</div>',
    unsafe_allow_html=True,
)

diferenciais = [
    "Atendimento conforme as necessidades do estabelecimento",
    "Orientação técnica com foco na segurança dos alimentos",
    "Organização de documentos e procedimentos",
    "Apoio à melhoria contínua dos processos",
]

for diferencial in diferenciais:
    st.markdown(
        f"""
        <div class="document-card">
            <span class="check">✓</span>{diferencial}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================================
# FAIXA INSTITUCIONAL
# ==========================================================
st.markdown(
    """
    <div class="company-band">
        <h3>GM CONSULTORIA ALIMENTAR</h3>
        <p>
            Responsabilidade Técnica • Consultoria UAN •
            Boas Práticas • Segurança dos Alimentos
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# CONTATO E WHATSAPP
# ==========================================================
st.markdown(
    """
    <div class="contact">
        <h2>Vamos conversar?</h2>

        <p>
            Entre em contato para conhecer os serviços
            e solicitar uma proposta de consultoria.
        </p>

        <p>
            Consultoria:
            <strong>(61) 99927-7063</strong>
        </p>

        <p>
            class="whatsapp"
            href="https://wa.me/5561999277063"
            target="_blank"
            rel="noopener noreferrer"
            💬 Chamar no WhatsApp
        </p>
    </div>
    """,
    unsafe_allow_html=True)
# ==========================================================
# RODAPÉ
# ==========================================================
st.markdown(
    """
    <div class="footer">
        <p><strong>GM Consultoria Alimentar</strong></p>
        <p>
            Nutricionista RT | Consultoria em Unidade de Alimentação
            e Nutrição (UAN)
        </p>
        <p>© 2026 — Todos os direitos reservados.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
