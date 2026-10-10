```python
import streamlit as st

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Nutric RT | Consultoria UAN",
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

    .hero {
        background: linear-gradient(135deg, #0d6b5b, #168b73);
        color: white;
        padding: 42px 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(13, 107, 91, 0.18);
        margin-bottom: 30px;
    }

    .hero-kicker {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .hero h1 {
        color: white;
        font-size: clamp(2rem, 5vw, 3rem);
        margin-bottom: 18px;
    }

    .hero p {
        color: white;
        font-size: 17px;
        line-height: 1.8;
        max-width: 850px;
        margin: 0 auto;
    }

    .section-title {
        color: #0d6b5b;
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: 32px;
        margin-bottom: 12px;
    }

    .section-subtitle {
        color: #53635e;
        font-size: 1rem;
        line-height: 1.8;
    }

    .card {
        background: white;
        border: 1px solid #e0eee8;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 14px;
        color: #33423e;
        box-shadow: 0 4px 14px rgba(20, 70, 55, 0.05);
        line-height: 1.7;
    }

    .card h3 {
        color: #0d6b5b;
        margin-top: 0;
        font-size: 1.15rem;
    }

    .service {
        padding: 10px 0;
        color: #33423e;
        border-bottom: 1px solid #edf3f1;
    }

    .service:last-child {
        border-bottom: 0;
    }

    .check {
        color: #0d806b;
        font-weight: 800;
        margin-right: 7px;
    }

    .audience {
        display: block;
        text-align: center;
        background: #f0faf6;
        border: 1px solid #cfe9df;
        border-radius: 12px;
        padding: 18px 12px;
        font-weight: 700;
        color: #0d6b5b;
        margin-bottom: 12px;
    }

    .plan {
        background: white;
        border: 1px solid #cfe9df;
        border-radius: 14px;
        padding: 22px 12px;
        text-align: center;
        color: #0d6b5b;
        font-weight: 800;
        box-shadow: 0 4px 14px rgba(20, 70, 55, 0.05);
    }

    .contact {
        background: #f0faf6;
        border: 1px solid #cfe9df;
        padding: 28px 20px;
        border-radius: 16px;
        text-align: center;
        margin-top: 24px;
    }

    .contact h2 {
        color: #0d6b5b;
    }

    .whatsapp {
        display: inline-block;
        background: #25D366;
        color: #ffffff !important;
        padding: 13px 24px;
        border-radius: 9px;
        text-decoration: none !important;
        font-weight: 800;
        margin-top: 12px;
    }

    .an-banner {
        background: linear-gradient(135deg, #0d6b5b, #168b73);
        color: white;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        margin-top: 30px;
    }

    .an-banner strong {
        font-size: 21px;
    }

    .an-banner p {
        margin: 10px 0 0;
        line-height: 1.8;
    }

    .footer {
        text-align: center;
        color: #53635e;
        font-size: 0.9rem;
        padding-top: 24px;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 30px 18px;
        }

        .hero p {
            font-size: 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# HERO - DESTAQUE PRINCIPAL
# ==========================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-kicker">
            🥗 Nutrição em Alimentação Coletiva
        </div>

        <h1>Consultoria em UAN</h1>

        <p>
            Consultoria para empresas e estabelecimentos
            de alimentação, com foco em qualidade,
            segurança dos alimentos e conformidade com
            as Boas Práticas.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# INTRODUÇÃO
# ==========================================================
st.markdown(
    """
    <div class="section-title">
        🏢 Consultoria para Empresas e Estabelecimentos
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Seu estabelecimento precisa de Responsabilidade Técnica,
        organização, segurança dos alimentos e adequação às
        Boas Práticas? Conheça os serviços de Nutrição em
        Alimentação Coletiva (UAN) oferecidos pela GM Consultoria
        Alimentar.
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# SERVIÇOS
# ==========================================================
st.markdown(
    '<div class="section-title">🛠️ Nossos Serviços</div>',
    unsafe_allow_html=True,
)

servicos = [
    (
        "Responsabilidade Técnica (RT)",
        "Acompanhamento técnico e orientação conforme as "
        "atribuições profissionais e as exigências aplicáveis."
    ),
    (
        "Consultoria em UAN",
        "Organização dos processos de produção e dos serviços "
        "de alimentação."
    ),
    (
        "Boas Práticas",
        "Orientação para implantação e manutenção de procedimentos "
        "de higiene e segurança dos alimentos."
    ),
    (
        "Treinamento de Manipuladores",
        "Capacitação da equipe sobre higiene pessoal, manipulação "
        "segura e prevenção de contaminações."
    ),
    (
        "Cardápios e Fichas Técnicas",
        "Elaboração e avaliação de cardápios e fichas técnicas "
        "de preparação."
    ),
    (
        "Controle de Desperdícios",
        "Orientações para acompanhar perdas e melhorar o "
        "aproveitamento dos alimentos."
    ),
]

service_cols = st.columns(3, gap="medium")

for i, (titulo, descricao) in enumerate(servicos):
    with service_cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{titulo}</h3>
                <div>{descricao}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================================
# PÚBLICO ATENDIDO
# ==========================================================
st.markdown(
    '<div class="section-title">🍽️ Para quem é nosso atendimento?</div>',
    unsafe_allow_html=True,
)

audiencias = [
    "🍞 Padarias",
    "🍔 Lanchonetes",
    "🏭 Cozinhas industriais",
    "🏨 Hotéis",
    "🏫 Escolas",
    "🏢 Empresas e instituições",
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
    '<div class="section-title">📋 Documentação e Adequação</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Apoio à organização documental e aos procedimentos
        de higiene e segurança dos alimentos, de acordo com
        as características do estabelecimento e as normas
        sanitárias aplicáveis.
    </div>
    """,
    unsafe_allow_html=True,
)

documentos = [
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPs",
    "Orientação sobre documentação sanitária",
    "Treinamento de manipuladores de alimentos",
    "Fichas técnicas de preparação",
    "Orientação para controle de qualidade",
]

doc_cols = st.columns(2, gap="medium")

for i, item in enumerate(documentos):
    with doc_cols[i % 2]:
        st.markdown(
            f"""
            <div class="card">
                <span class="check">✔</span>{item}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================================
# PLANOS DE ACOMPANHAMENTO
# ==========================================================
st.markdown(
    '<div class="section-title">📆 Planos de Acompanhamento</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        O acompanhamento pode ser planejado conforme as
        necessidades do estabelecimento e os serviços contratados.
    </div>
    """,
    unsafe_allow_html=True,
)

plan_cols = st.columns(4, gap="medium")

planos = [
    "Mensal",
    "Trimestral",
    "Semestral",
    "Anual",
]

for col, plano in zip(plan_cols, planos):
    with col:
        st.markdown(
            f'<div class="plan">📅 Plano {plano}</div>',
            unsafe_allow_html=True,
        )

# ==========================================================
# CONTATO / WHATSAPP
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
        <a
            class="whatsapp"
            href="https://wa.me/5561999277063"
            target="_blank"
            rel="noopener noreferrer">
            💬 Chamar no WhatsApp
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# IDENTIDADE DA EMPRESA
# ==========================================================
st.markdown(
    """
    <div class="an-banner">
        <strong>GM CONSULTORIA ALIMENTAR</strong>
        <p>
            Responsabilidade Técnica • Boas Práticas<br>
            Consultoria em UAN
        </p>
    </div>

    <div class="footer">
        Nutrição em Alimentação Coletiva | Consultoria UAN
    </div>
    """,
    unsafe_allow_html=True,
)
```
