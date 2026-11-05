
import streamlit as st
import urllib.parse

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="GM Consultoria Alimentar",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

WHATSAPP = "5561999277063"

# ==========================================================
# CSS GLOBAL
# ==========================================================

st.markdown("""
<style>

:root {
    --verde-escuro: #075c49;
    --verde: #0d8065;
    --verde-claro: #e9f7ed;
    --lima: #b5d96b;
    --fundo: #f5faf7;
    --texto: #34443d;
}

/* Página */

.stApp {
    background: var(--fundo);
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 5rem;
}

/* Remove elementos padrão */

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* Cabeçalho */

.site-header {
    background: white;
    padding: 16px 24px;
    border-radius: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    box-shadow: 0 3px 14px #00000010;
    margin-bottom: 25px;
    flex-wrap: wrap;
}

.logo-text {
    font-size: 22px;
    font-weight: 800;
    color: var(--verde-escuro);
}

.logo-subtitle {
    color: #718078;
    font-size: 11px;
    letter-spacing: 2px;
}

.site-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
}

.site-nav a {
    color: var(--verde-escuro);
    font-weight: 600;
    text-decoration: none;
    font-size: 14px;
}

.site-nav a:hover {
    color: var(--verde);
}

/* Hero */

.hero {
    background: linear-gradient(135deg, #075c49, #168b73);
    color: white;
    padding: 48px 35px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 5px 18px #00000015;
}

.hero-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    align-items: center;
}

.hero h1 {
    font-size: clamp(30px, 4vw, 43px);
    line-height: 1.2;
    margin-bottom: 18px;
    color: white;
}

.hero p {
    font-size: 17px;
    line-height: 1.7;
}

.hero-label {
    color: var(--lima);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero img {
    width: 100%;
    border-radius: 16px;
    object-fit: cover;
}

.hero-button {
    display: inline-block;
    background: var(--lima);
    color: var(--verde-escuro) !important;
    padding: 13px 22px;
    border-radius: 30px;
    font-weight: 800;
    text-decoration: none;
    margin-top: 12px;
}

/* Seções */

section {
    scroll-margin-top: 25px;
    margin-bottom: 25px;
}

.content-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 3px 15px #00000009;
}

h2 {
    color: var(--verde-escuro);
    font-size: 28px;
    margin-bottom: 18px;
}

h3 {
    color: var(--verde-escuro);
    font-size: 18px;
}

.content-card p {
    color: var(--texto);
    line-height: 1.8;
}

/* Grid de serviços */

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-top: 20px;
}

.card {
    background: var(--verde-claro);
    padding: 22px;
    border-radius: 15px;
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 5px 15px #00000012;
}

.card p {
    font-size: 14px;
    line-height: 1.7;
}

.emoji {
    font-size: 30px;
    margin-bottom: 12px;
}

.card.segmento {
    text-align: center;
    font-size: 18px;
    font-weight: 700;
    color: var(--verde-escuro);
}

/* Formulário */

.form-area {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 3px 15px #00000009;
}

/* Botão WhatsApp */

.whatsapp-float {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background: #25d366;
    color: white !important;
    border-radius: 40px;
    padding: 13px 19px;
    font-weight: 700;
    text-decoration: none !important;
    box-shadow: 0 4px 14px #00000030;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 99999;
    font-size: 14px;
    transition: 0.2s;
}

.whatsapp-float:hover {
    transform: scale(1.06);
}

/* Menu flutuante inferior esquerdo */

.floating-menu {
    position: fixed;
    left: 18px;
    bottom: 90px;
    display: flex;
    flex-direction: column;
    gap: 9px;
    z-index: 99999;
}

.floating-menu a {
    display: block;
    background: var(--verde-escuro);
    color: white !important;
    padding: 11px 17px;
    border-radius: 30px;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 700;
    text-align: center;
    box-shadow: 0 3px 10px #00000025;
    transition: 0.2s;
}

.floating-menu a:hover {
    background: var(--verde);
    transform: translateX(4px);
}

/* Rodapé */

.site-footer {
    background: var(--verde-escuro);
    color: white;
    text-align: center;
    padding: 28px 15px;
    border-radius: 16px;
    margin-top: 25px;
}

.site-footer p {
    margin: 5px;
    font-size: 13px;
}

/* Responsividade */

@media (max-width: 768px) {

    .hero-content {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 30px 22px;
    }

    .site-header {
        flex-direction: column;
        align-items: flex-start;
    }

    .site-nav {
        gap: 12px;
    }

    .content-card {
        padding: 20px;
    }

    .floating-menu {
        left: 10px;
        bottom: 85px;
        gap: 7px;
    }

    .floating-menu a {
        padding: 9px 12px;
        font-size: 11px;
    }

    .whatsapp-float {
        right: 10px;
        bottom: 15px;
        padding: 11px 14px;
        font-size: 12px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# CABEÇALHO
# ==========================================================

st.markdown("""
<div class="site-header">

    <div>
        <div class="logo-text">GM Consultoria Alimentar</div>
        <div class="logo-subtitle">
            GESTÃO • QUALIDADE • SEGURANÇA ALIMENTAR
        </div>
    </div>

    <nav class="site-nav">
        <a href="#empresa">Quem somos</a>
        <a href="#servicos">Serviços</a>
        <a href="#segmentos">Segmentos</a>
        <a href="#contato">Contato</a>
    </nav>

</div>
""", unsafe_allow_html=True)


# ==========================================================
# INÍCIO / HERO
# ==========================================================

st.markdown("""
<section id="inicio">

    <div class="hero">

        <div class="hero-content">

            <div>

                <div class="hero-label">
                    CONSULTORIA • GESTÃO • QUALIDADE
                </div>

                <h1>
                    Seu negócio mais seguro!
                </h1>

                <p>
                    Consultoria e assessoria especializada em
                    segurança dos alimentos para sua empresa.
                    Mais qualidade, organização e tranquilidade
                    para você crescer.
                </p>

                <a class="hero-button"
                   href="https://wa.me/5561999277063"
                   target="_blank"
                   rel="noopener">
                    Fale conosco pelo WhatsApp
                </a>

            </div>

            <div>
                <img
                    src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=900"
                    alt="Cozinha profissional e segurança alimentar">
            </div>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ==========================================================
# EMPRESA
# ==========================================================

st.markdown("""
<section id="empresa">

    <div class="content-card">

        <h2>Quem somos</h2>

        <p>
            A <strong>GM Consultoria Alimentar</strong> é especializada
            em consultoria e assessoria para estabelecimentos
            do setor alimentício.
        </p>

        <p>
            Nosso trabalho busca garantir a segurança dos alimentos,
            organização, padronização dos processos e melhoria
            contínua do seu estabelecimento, para que você possa
            focar no crescimento do seu negócio.
        </p>

        <p>
            Atuamos com responsabilidade técnica, boas práticas
            de fabricação, controle de qualidade e orientação
            para o cumprimento das exigências sanitárias.
        </p>

    </div>

</section>
""", unsafe_allow_html=True)


# ==========================================================
# SERVIÇOS
# ==========================================================

st.markdown("""
<section id="servicos">

    <div class="content-card">

        <h2>Nossos serviços</h2>

        <p>
            Soluções completas para melhorar a gestão,
            qualidade e segurança alimentar da sua empresa.
        </p>

        <div class="grid">

            <article class="card">
                <div class="emoji">🛡️</div>
                <h3>Segurança dos alimentos e RT</h3>
                <p>
                    Responsabilidade técnica e orientação para
                    alimentos seguros e conformidade sanitária.
                </p>
            </article>

            <article class="card">
                <div class="emoji">📋</div>
                <h3>MBP, POPs e BPF</h3>
                <p>
                    Elaboração, implantação e acompanhamento
                    de documentos e boas práticas.
                </p>
            </article>

            <article class="card">
                <div class="emoji">👩‍🍳</div>
                <h3>Treinamento de equipe</h3>
                <p>
                    Capacitação da equipe com foco na prática
                    e na segurança dos alimentos.
                </p>
            </article>

            <article class="card">
                <div class="emoji">📈</div>
                <h3>Gestão de UAN</h3>
                <p>
                    Organização eficiente, segura e produtiva
                    para o seu estabelecimento.
                </p>
            </article>

            <article class="card">
                <div class="emoji">📑</div>
                <h3>Apoio na licença sanitária</h3>
                <p>
                    Orientação e suporte durante o processo
                    de regularização sanitária.
                </p>
            </article>

            <article class="card">
                <div class="emoji">🔎</div>
                <h3>Diagnóstico e plano de ação</h3>
                <p>
                    Identificação de oportunidades de melhoria
                    e planejamento de soluções.
                </p>
            </article>

            <article class="card">
                <div class="emoji">📊</div>
                <h3>Relatórios mensais</h3>
                <p>
                    Acompanhamento técnico e avaliação
                    contínua dos processos.
                </p>
            </article>

            <article class="card">
                <div class="emoji">🍽️</div>
                <h3>Fichas técnicas</h3>
                <p>
                    Padronização de preparações, ingredientes,
                    rendimento e processos.
                </p>
            </article>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ==========================================================
# SEGMENTOS
# ==========================================================

st.markdown("""
<section id="segmentos">

    <div class="content-card">

        <h2>Quem atendemos</h2>

        <p>
            Atendemos diferentes tipos de estabelecimentos
            que trabalham com produção, armazenamento e
            comercialização de alimentos.
        </p>

        <div class="grid">

            <div class="card segmento">🍽️<p>Restaurantes</p></div>
            <div class="card segmento">🥪<p>Lanchonetes</p></div>
            <div class="card segmento">🥖<p>Padarias</p></div>
            <div class="card segmento">🍔<p>Hamburguerias</p></div>
            <div class="card segmento">🚚<p>Food Trucks</p></div>
            <div class="card segmento">🛒<p>Mercados</p></div>
            <div class="card segmento">🧸<p>Creches</p></div>
            <div class="card segmento">🏪<p>Mercearias</p></div>
            <div class="card segmento">☕<p>Cafeterias</p></div>
            <div class="card segmento">🏨<p>Hotéis</p></div>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ==========================================================
# CONTATO
# ==========================================================

st.markdown("""
<section id="contato">

    <div class="content-card">

        <h2>Vamos encontrar a solução para sua empresa?</h2>

        <p>
            Entre em contato pelo WhatsApp ou preencha os dados
            abaixo. Sua solicitação será preparada para envio
            direto pelo WhatsApp.
        </p>

    </div>

</section>
""", unsafe_allow_html=True)


# ==========================================================
# FORMULÁRIO DE ORÇAMENTO
# ==========================================================

st.markdown('<div class="form-area">', unsafe_allow_html=True)

with st.form("form_orcamento"):

    st.subheader("Solicite um orçamento")

    nome = st.text_input("Seu nome *")

    empresa = st.text_input("Nome do estabelecimento")

    telefone = st.text_input("Seu telefone *")

    segmento = st.selectbox(
        "Segmento *",
        [
            "",
            "Restaurante",
            "Lanchonete",
            "Padaria",
            "Hamburgueria",
            "Food Truck",
            "Mercado",
            "Confeitaria",
            "Cafeteria",
            "Creche",
            "Hotel",
            "Outro"
        ]
    )

    mensagem = st.text_area(
        "Conte como podemos ajudar"
    )

    enviar = st.form_submit_button(
        "Preparar solicitação no WhatsApp",
        use_container_width=True
    )

st.markdown('</div>', unsafe_allow_html=True)


# ==========================================================
# PROCESSAMENTO DO FORMULÁRIO
# ==========================================================

if enviar:

    if not nome.strip() or not telefone.strip() or not segmento:

        st.error("Preencha nome, telefone e segmento.")

    else:

        texto = "\n".join([
            "Olá! Gostaria de solicitar um orçamento da GM Consultoria Alimentar.",
            "",
            f"Nome: {nome.strip()}",
            f"Estabelecimento: {empresa.strip() or 'Não informado'}",
            f"Telefone: {telefone.strip()}",
            f"Segmento: {segmento}",
            f"Solicitação: {mensagem.strip() or 'Não informado'}"
        ])

        link_whatsapp = (
            f"https://wa.me/{WHATSAPP}?text="
            + urllib.parse.quote(texto)
        )

        st.success("Solicitação preparada com sucesso!")

        st.markdown(
            f"""
            <a href="{link_whatsapp}"
               target="_blank"
               rel="noopener"
               style="
                   display:block;
                   background:#25d366;
                   color:white;
                   text-align:center;
                   padding:15px;
                   border-radius:12px;
                   text-decoration:none;
                   font-weight:bold;
                   margin-top:12px;
               ">
                💬 ABRIR WHATSAPP E ENVIAR SOLICITAÇÃO
            </a>
            """,
            unsafe_allow_html=True
        )


# ==========================================================
# MENU FLUTUANTE
# ==========================================================

st.markdown("""
<div class="floating-menu">

    <a href="#inicio">⌂ INÍCIO</a>

    <a href="#servicos">▣ SERVIÇOS</a>

    <a href="#contato">✉ ORÇAMENTO</a>

</div>
""", unsafe_allow_html=True)


# ==========================================================
# BOTÃO FLUTUANTE WHATSAPP
# ==========================================================

st.markdown("""
<a class="whatsapp-float"
   href="https://wa.me/5561999277063"
   target="_blank"
   rel="noopener">

    💬 WhatsApp

</a>
""", unsafe_allow_html=True)


# ==========================================================
# RODAPÉ
# ==========================================================

st.markdown("""
<footer class="site-footer">

    <p><strong>GM CONSULTORIA ALIMENTAR</strong></p>

    <p>
        Gestão • Qualidade • Segurança Alimentar
    </p>

    <p>
        Consultoria e Assessoria em Segurança dos Alimentos
    </p>

    <p>
        © 2026 GM Consultoria Alimentar - Todos os direitos reservados.
    </p>

</footer>
""", unsafe_allow_html=True)
