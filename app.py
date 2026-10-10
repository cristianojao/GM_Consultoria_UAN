import streamlit as st

st.set_page_config(
    page_title/consultoria_uan/app.py

    initial_sidebar_state="collapsed",
)

st.mark<style>
    .stApp {
        background: linear-gradient(180deg, #f748%, #f5fbf8 100%);
   0d6b5b, #168b73-shadow: 0 12px 35px rgba(13, 107, 91, .18);
        margin-bottom:  .08em;
        text-transform: uppercase;
        opacity: .9;
        margin-bottom: 10px;
    }

    .hero h1 {
        font-size: clamp(2rem,5vw, 3.5rem);
        line-height: 1.08;
        margin: 0 0 14px  .hero p {
        font-size: 1.: 1.65;
        max-width: 850px;
        margin-bottom: 0 1.8rem;
        font-weight: 800;
        margin: 34px 8px;
    }

    .section-subtitle;
        font-size: 1rem;
        margin-bottom: 20px;
    }

    .card {
        background: white;
        border: 1px #dcece6;
        border-radius: 18px;
        margin-top: 0;
        font-size: 1.15rem;
    }

    .service {
 0;
        color: #33423e;
    }

    .service:last-child {
        border-bottom: 0;
    }

        display: inline-block;
        background: #e9        color: #0d6b5b;
        padding: 10px 15px;
        border-radius: 999px;
        margin: 5 text-align: center;
        background: #f0 #cfe9df;
        border-radius: 18 24px 18px;
        font-weight:;
        color: #0d6b5b;
        font-size: 1.05rem;
    }

    .cta {
        34px;
        border-radius: 22px;
        background: #103f37;
        color: }

    .cta h #e3f3ee;
    }

    .footer {
        text-align: center;
        color: #6b7b76;
        font-size: .9rem;
        padding-top: 30px;
    }

    a #25D366;
        color: white !important;
;
        margin-top: 8px;
    }

    @media (max-width: 700 {
        .hero {
            padding: 30px .block-container {
            padding-left: 1rem;
            padding-right:""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-kicker">🥗 Nutrição em Alimentação Coletiva</div>
    <>
        <strong>Consultoria UAN para empresas>
        Responsabilidade Técnica, organização, segurança alimentar e às Boas Práticas.
    </p>
</>
""", unsafe_allow_html=True)

# Intro
st.markcimentos de Alimentação</div>', unsafe_allow_html=True Práticas? Ofereço serviços de Nutrição em Alimentação Coletiva (UAN) "
    "para empresas e estabelecimentos de alimentação."
)

# Services
st.markdown('<div class="section-title">✅ Serviços</div>', unsafe_allow_html=True)

services = [
    "Responsabilidade Técnica (RT)",
    "Consultoria em UAN",
    "Adequação às Boas Práticas e exigências sanitárias",
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPs",
    "Treinamento de manipuladores de alimentos",
    "Elaboração e avaliação de cardápios",
    "Fichas técnicas de preparação",
    "Controle de desperdícios",
    "Controle de qualidade",
    "Auditorias e visitas "Organização da documentação sanitária",
    "Acompanhamento e visitas periódicas",
]

cols = st.columns(3, gap="medium")
for i,    with cols[i % 3]:
        st.markdown(
            f'<></div>',
            unsafe_allow_html=True,
        )

 Atendimento para</div>', unsafe_allow_html=True)

aud "Padarias", "Cozinhas industriais",
    "colas", "Empresas e instituições",
    "Out estabelecimentos de alimentação"
]
st.markdown(
    "".join(f'<span class="audience">{
)

# Documentation
st.markdown('<div class="section-title">📋 Documentação e Adequação</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Elaboração, revisão e organização de:</div>', unsafe_allow_html=True)

docs = [
    " de Boas Práticas",
    "POPs",
    "Registros e controles",
    "Documentação sanitária",
    "Procedimentos de higiene e segurança dos alimentos",
]

c1, c2 = st.columns(2, gap="large")
for i, item in enumerate(d):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(
            f'<div class="card"><span class="check">✔</span>{item}</div>',
            unsafe_allow_html=True,
        )

div>', unsafe_allow_html=True)
st.write("Atendimento        st.markdown(f'<div class="plans"> {plan}</div>', unsafe_allow_html=True)

st visitas periódicas.")

# Contact
st.markdown("""
<div class="cta">
    <hp>Agende uma avaliação do seu estabelecimento.</p>
    <p><strong>📞 Telefone/WhatsApp: (61) 99927-7063</strong></p>
    <a class="whatsapp" href="://wa.me/5561999277063" target="_blank"div class="footer">🥗 Consultoria UAN • Responsabilidade Técnica • Boas Práticas • Segurança dos Alimentos</div>',
    unsafe_allow_html=True,
)
