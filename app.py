import streamlit as st

st.set_page_config(
    page_title/consultoria_uan/app.py
)

st.markdown("""
<style>
    .stApp #f5fbf8 100%);
    }

block-container {
        max-width: 1180px34px;
        border-radius: 22px;
        box-shadow: 0 12px 35 margin-bottom: 28px;
    }

    ..95rem;
        font-weight: 700;
 text-transform: uppercase;
        opacity: .9;
 3.5rem);
        line-height: 1.08;
        margin    .hero p {
        font-size: 1 .section-title {
        color: #0d6 1.8rem;
        font-weight:  8px;
    }

    .section-subtitle        font-size: 1rem;
        margin-bottomce6;
        border-radius: 18px;
 padding: 22px;
        height: 100%;
        box-shadow: 0 7px 22 75, 63, .07);
    }

   0;
        font-size: 1.15rem;
    }

    .service {
        padding:f1;
    }

    .service:last-child {
        border-bottom: 0;
    }

    .check {
        color: #0d806b;
        font-weight:  inline-block;
        background: #e9f7f2;
        color: #0d6b: 10px 15px;
        border-radius:: center0faf6;
        border: 1px solid 35px;
        padding: 34px;
       1rem;
            padding-right: 1rem;
 Hero
st.markdown("""
<div class="hero">
 empresas e estabelecimentos de alimentação.</strong><br>
# Intro
st.markdown('<div class="section-title">🏢 Consult Alimentação</div>', unsafe_allow_html=True)
st? Ofereço serviços de Nutrição em Alimentação Coletiva (UAN) "
   _uan/app.py
)

# Services
st.markdown('<div class="section-title">✅>', unsafe_allow_html=True)

services = [
    "RT)",
    "Consultoria em UAN",
    "Adequação às Boas Práticas e exigências sanitárias",
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPsinamento de manipuladores de alimentos",
    "El    "Auditorias e visitas técnicas",
    "Organização da documentação sanitária",
    "Acompanhamento e visitas periódicas",
]

cols = st.columns(3, gap="medium")
for i, service in enumerate(services):
    with cols.markdown(
            f'<div class="card"><🍽️ Atendimento para</div>', unsafe_allow_html=Trueetes", "Padarias", "Cozinhas industriaisEscolas", "Empresas e instituições",
    "Out]
st.markdown(
    "".join(f'<span class="audience">{x}</span>'
)

# Documentation
st.markdown('<div class="section de:</div>', unsafe_allow_html=True)

docs = [
    "Manual de Boas Práticas",
    "POPs",
    "ária",
    "Procedimentos de higiene e segurança dosc1, c2 = st.columns(2, gap="large")
for i, item in with (c1 if i % 2 == 0 else c2):
        st.markdown(
            f'<div class="card"><span class="companhamento</div>', unsafe_allow_html=True)
st.write("At(4, gap="medium")
for col, plan in zip(plan_cols, ["Mensal", "Trimestral", "Semestral", "Anual"]):
    with col:
        st="plans">📅 {plan}</div>', unsafe_allow)

st.info("Consultoria, acompanhamento técnico e visitas periódicas.")

#
st.markdown("""
<div class="cta">
    <📲 Fale agora com uma Especialista</h2>Agende uma avaliação do seu estabelecimento.</p>
    <p><whatsapp" href="https://wa.me/556199="noopener noreferrer">
        💬 Chamar no WhatsApp unsafe_allow_html=True)

st.markdown(
    '<div class="footer">🥗 Consultoria UAN • Responsabilidade Técnica • • Segurança dos Alimentos</div>',
    unsafe_allow_html=True
