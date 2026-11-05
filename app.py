import streamlit as st

# ============================================================
# GM CONSULTORIA ALIMENTAR - SITE INSTITUCIONAL
# Execute com: streamlit run app.py
# ============================================================
<h1></h1>

st.set_page_config(
    page_title="GM Consultoria Alimentar",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

WHATSAPP_NUMBER = "5561999277063"

# CSS do novo layout
st.markdown(
    """
    <style>
      :root {
        --verde: #0d6b5b;
        --verde-escuro: #084b40;
        --verde-claro: #eaf5f0;
        --lima: #c8df75;
        --texto: #263b35;
        --cinza: #60716b;
        --branco: #ffffff;
      }

      html { scroll-behavior: smooth; }
      .stApp {
        background: #f5faf7;
        color: var(--texto);
      }
      [data-testid="stHeader"] { background: rgba(245,250,247,.92); }
      [data-testid="stToolbar"] { right: 1rem; }
      .block-container {
        max-width: 1160px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
      }
      #MainMenu, footer { visibility: hidden; }

      .site-header {
        position: sticky;
        top: 20px;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        padding: 14px 20px;
        margin-bottom: 22px;
        background: rgba(255,255,255,.97);
        border: 1px solid #e2eee8;
        border-radius: 16px;
        box-shadow: 0 5px 20px rgba(8,75,64,.08);
      }
      .logo-text {
        color: var(--verde);
        font-size: 21px;
        font-weight: 800;
        line-height: 1.2;
      }
      .logo-sub {
        color: var(--cinza);
        font-size: 12px;
        margin-top: 4px;
      }
      .site-nav {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 8px;
      }
      .site-nav a {
        color: var(--verde-escuro);
        text-decoration: none;
        font-size: 13px;
        font-weight: 700;
        padding: 9px 12px;
        border-radius: 30px;
      }
      .site-nav a:hover {
        background: var(--verde-claro);
        color: var(--verde);
      }

      section { scroll-margin-top: 125px; }
      .hero {
        overflow: hidden;
        background: linear-gradient(120deg, #ffffff 0%, #eaf5f0 100%);
        border: 1px solid #e1eee7;
        border-radius: 22px;
        padding: 34px;
        margin-bottom: 22px;
        box-shadow: 0 8px 28px rgba(8,75,64,.07);
      }
      .eyebrow {
        color: var(--verde);
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 12px;
      }
      .hero h1 {
        color: var(--verde-escuro);
        font-size: clamp(30px, 4.5vw, 48px);
        line-height: 1.12;
        margin: 0 0 15px 0;
      }
      .hero p {
        color: #52665e;
        font-size: 17px;
        line-height: 1.7;
        max-width: 620px;
      }
      .hero-image {
        width: 100%;
        min-height: 270px;
        max-height: 340px;
        object-fit: cover;
        border-radius: 17px;
      }
      .btn {
        display: inline-block;
        background: var(--verde);
        color: #fff !important;
        text-decoration: none !important;
        font-weight: 800;
        padding: 13px 19px;
        border-radius: 30px;
        margin-top: 12px;
        box-shadow: 0 5px 14px rgba(13,107,91,.2);
      }
      .btn:hover { background: var(--verde-escuro); }

      .content-card {
        background: #fff;
        border: 1px solid #e4eee9;
        border-radius: 19px;
        padding: 27px;
        margin: 18px 0;
        box-shadow: 0 5px 20px rgba(8,75,64,.045);
      }
      .section-kicker {
        color: #789087;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 5px;
      }
      .section-title {
        color: var(--verde-escuro);
        font-size: 27px;
        font-weight: 800;
        margin: 0 0 13px 0;
      }
      .section-copy {
        color: #52665e;
        line-height: 1.75;
        font-size: 15px;
      }
      .highlight {
        background: var(--verde-claro);
        border-left: 4px solid var(--verde);
        padding: 17px 19px;
        border-radius: 10px;
        margin-top: 18px;
        color: #35564b;
        line-height: 1.65;
      }

      .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 15px;
        margin-top: 18px;
      }
      .service-card {
        background: #f6fbf8;
        border: 1px solid #e2eee8;
        border-radius: 15px;
        padding: 20px;
        min-height: 175px;
      }
      .service-icon { font-size: 29px; margin-bottom: 10px; }
      .service-card h3 {
        color: var(--verde-escuro);
        font-size: 17px;
        margin: 0 0 8px 0;
      }
      .service-card p {
        color: #60716b;
        font-size: 13px;
        line-height: 1.6;
        margin: 0;
      }
      .segment-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
        gap: 12px;
        margin-top: 18px;
      }
      .segment-card {
        text-align: center;
        background: var(--verde-claro);
        border: 1px solid #dcece4;
        padding: 18px 10px;
        border-radius: 14px;
        color: var(--verde-escuro);
        font-weight: 750;
      }
      .segment-card span {
        display: block;
        font-size: 27px;
        margin-bottom: 7px;
      }
      .site-footer {
        text-align: center;
        color: #6c8077;
        font-size: 12px;
        padding: 25px 10px 12px;
      }
      .whatsapp-float {
        position: fixed;
        right: 20px;
        bottom: 20px;
        z-index: 1000;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 13px 17px;
        border-radius: 40px;
        background: #25d366;
        color: #fff !important;
        text-decoration: none !important;
        font-size: 14px;
        font-weight: 800;
        box-shadow: 0 5px 18px rgba(0,0,0,.2);
      }

      /* Formulário Streamlit */
      [data-testid="stForm"] {
        background: #fff;
        border: 1px solid #e2eee8;
        border-radius: 16px;
        padding: 20px;
      }
      div[data-testid="stFormSubmitButton"] button {
        background: var(--verde);
        color: white;
        border: 0;
        border-radius: 30px;
        font-weight: 800;
        min-height: 45px;
      }
      div[data-testid="stFormSubmitButton"] button:hover {
        background: var(--verde-escuro);
        color: white;
      }

      @media (max-width: 760px) {
        .block-container { padding: 0.7rem 0.8rem 1.5rem; }
        .site-header {
          position: sticky;
          top: 12px;
          align-items: flex-start;
          flex-direction: column;
          padding: 14px;
        }
        .site-nav { justify-content: flex-start; gap: 3px; }
        .site-nav a { padding: 8px 9px; font-size: 12px; }
        .hero { padding: 22px 18px; }
        .content-card { padding: 21px 17px; }
        .hero-image { min-height: 190px; }
        .whatsapp-float { right: 12px; bottom: 12px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Cabeçalho e navegação
st.markdown(
    """
    <header class="site-header">
      <div>
        <div class="logo-text">GM Consultoria Alimentar</div>
        <div class="logo-sub">Gestão • Qualidade • Segurança Alimentar</div>
      </div>
      <nav class="site-nav">
        <a href="#inicio">Início</a>
        <a href="#empresa">Quem somos</a>
        <a href="#servicos">Serviços</a>
        <a href="#segmentos">Segmentos</a>
        <a href="#contato">Orçamento</a>
      </nav>
    </header>
    """,
    unsafe_allow_html=True,
)

# Início / apresentação
st.markdown(
    f"""
    <section id="inicio" class="hero">
      <div class="eyebrow">Consultoria • Assessoria • Responsabilidade técnica</div>
      <div class="hero-content">
        <div>
          <h1>Seu negócio mais seguro. Sua gestão mais eficiente.</h1>
          <p>
            Consultoria especializada em segurança dos alimentos para
            restaurantes, lanchonetes, padarias e empresas do setor alimentício.
            Mais qualidade, organização e tranquilidade para o seu negócio.
          </p>
          <a class="btn" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank"
             rel="noopener noreferrer">Fale conosco pelo WhatsApp</a>
        </div>
        <div style="margin-top:18px">
          <img class="hero-image"
            src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&w=1100&q=85"
            alt="Cozinha profissional organizada e preparada para manipulação de alimentos">
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Quem somos
st.markdown(
    """
    <section id="empresa" class="content-card">
      <div class="section-kicker">Conheça a GM</div>
      <h2 class="section-title">Quem somos</h2>
      <p class="section-copy">
        A <strong>GM Consultoria Alimentar</strong> é especializada em
        consultoria e assessoria para estabelecimentos do setor alimentício.
        Atuamos para fortalecer a segurança dos alimentos, a organização,
        a padronização dos processos e a conformidade com a legislação
        sanitária aplicável.
      </p>
      <p class="section-copy">
        Nosso trabalho é direcionado à realidade de cada estabelecimento,
        com orientação técnica, acompanhamento e soluções práticas para
        melhorar a rotina e os resultados da operação.
      </p>
      <div class="highlight">
        <strong>Nosso propósito</strong><br>
        Cuidar da segurança dos alimentos e da conformidade do seu
        estabelecimento, para que você possa focar no crescimento do seu negócio.
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Serviços
st.markdown(
    """
    <section id="servicos" class="content-card">
      <div class="section-kicker">Como podemos ajudar</div>
      <h2 class="section-title">Nossos serviços</h2>
      <div class="service-grid">
        <article class="service-card">
          <div class="service-icon">🛡️</div>
          <h3>Segurança dos alimentos e RT</h3>
          <p>Responsabilidade técnica e orientação para alimentos seguros e conformidade sanitária.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">📋</div>
          <h3>MBP, POPs e BPF</h3>
          <p>Elaboração, implantação e acompanhamento de documentos e boas práticas.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">👩‍🍳</div>
          <h3>Treinamento de equipe</h3>
          <p>Capacitação dos manipuladores com foco na prática e na segurança dos alimentos.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">📑</div>
          <h3>Licença sanitária</h3>
          <p>Orientação e suporte durante o processo de regularização sanitária.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">🔎</div>
          <h3>Diagnóstico e plano de ação</h3>
          <p>Identificação de oportunidades de melhoria e planejamento de soluções.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">📊</div>
          <h3>Relatórios e acompanhamento</h3>
          <p>Acompanhamento técnico e avaliação contínua dos processos.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">🍽️</div>
          <h3>Fichas técnicas</h3>
          <p>Padronização de preparações, ingredientes, rendimento e processos.</p>
        </article>
        <article class="service-card">
          <div class="service-icon">📉</div>
          <h3>Controle de desperdícios</h3>
          <p>Apoio na identificação de perdas e oportunidades de melhoria operacional.</p>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Segmentos atendidos
st.markdown(
    """
    <section id="segmentos" class="content-card">
      <div class="section-kicker">Soluções para o seu ramo</div>
      <h2 class="section-title">Quem atendemos</h2>
      <div class="segment-grid">
        <div class="segment-card"><span>🍽️</span>Restaurantes</div>
        <div class="segment-card"><span>🥪</span>Lanchonetes</div>
        <div class="segment-card"><span>🍞</span>Padarias</div>
        <div class="segment-card"><span>🍔</span>Hamburguerias</div>
        <div class="segment-card"><span>🚚</span>Food trucks</div>
        <div class="segment-card"><span>🛒</span>Mercados</div>
        <div class="segment-card"><span>🧁</span>Confeitarias</div>
        <div class="segment-card"><span>☕</span>Cafeterias</div>
        <div class="segment-card"><span>🏫</span>Escolas e creches</div>
        <div class="segment-card"><span>🏨</span>Hotéis e cozinhas</div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Contato e orçamento
st.markdown(
    """
    <section id="contato" class="content-card">
      <div class="section-kicker">Vamos conversar?</div>
      <h2 class="section-title">Solicite um orçamento</h2>
      <p class="section-copy">
        Conte um pouco sobre sua empresa. Ao enviar, o WhatsApp será aberto
        com a solicitação preenchida para você revisar e encaminhar.
      </p>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.form("form_orcamento", clear_on_submit=False):
    nome = st.text_input("Seu nome *", placeholder="Digite seu nome")
    empresa = st.text_input("Nome do estabelecimento", placeholder="Nome da empresa (opcional)")
    telefone = st.text_input("Seu telefone *", placeholder="(61) 99999-9999")
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
            "Escola ou creche",
            "Hotel ou cozinha industrial",
            "Outro",
        ],
        index=0,
    )
    mensagem = st.text_area(
        "Como podemos ajudar?",
        placeholder="Descreva brevemente sua necessidade...",
        height=110,
    )
    enviar = st.form_submit_button("Preparar solicitação no WhatsApp", use_container_width=True)

if enviar:
    if not nome.strip() or not telefone.strip() or not segmento:
        st.error("Preencha os campos obrigatórios: nome, telefone e segmento.")
    else:
        texto = "\n".join(
            [
                "Olá! Gostaria de solicitar um orçamento da GM Consultoria Alimentar.",
                "",
                f"Nome: {nome.strip()}",
                f"Estabelecimento: {empresa.strip() or 'Não informado'}",
                f"Telefone: {telefone.strip()}",
                f"Segmento: {segmento}",
                f"Solicitação: {mensagem.strip() or 'Não informado'}",
            ]
        )
        url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(texto)}"
        st.success("Solicitação preparada. Clique no botão abaixo para abrir o WhatsApp.")
        st.markdown(
            f'<a class="btn" href="{url}" target="_blank" rel="noopener noreferrer">'
            'Abrir WhatsApp e enviar solicitação</a>',
            unsafe_allow_html=True,
        )

# Rodapé e botão flutuante
st.markdown(
    f"""
    <div class="site-footer">
      <strong>GM Consultoria Alimentar</strong><br>
      Gestão • Qualidade • Segurança Alimentar<br>
      Atendimento mediante agendamento.
    </div>
    <a class="whatsapp-float" href="https://wa.me/{WHATSAPP_NUMBER}"
       target="_blank" rel="noopener noreferrer">
       <span>●</span> WhatsApp
    </a>
    """,
    unsafe_allow_html=True,
)
