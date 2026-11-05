import urllib.parse

import streamlit as st
st.set_page_config(
  page_title="GM Consultoria Alimentar",
  page_icon="🥗",
st.markdown(
  """
  <style>
      :root {
        --verde: #006b50;
        --verde-escuro: #003f32;
        --verde-claro: #e9f7ed;
        --lima: #b7df57;
      }
  .stApp { background: #f5faf6; color: #23332d; }
  header[data-testid="stHeader"] { background: transparent; }
  .site-header {
        background: white; padding: 18px 24px; border-radius: 14px;
        box-shadow: 0 2px 12px #0001; text-align: center;
      }
  .logo { color: var(--verde); font-size: 25px; font-weight: 800; }
  .site-header small { color: #53665e; }
  .site-nav {
  background: var(--verde-escuro); display: flex; overflow-x: auto;
  gap: 24px; padding: 14px 20px; margin: 12px 0 22px;
  border-radius: 10px;
  .site-nav a { color: white; text-decoration: none; white-space: nowrap; }
  .site-nav a:hover { color: var(--lima); }
  .hero, .content-card {
        background: white; padding: 34px; border-radius: 14px;
        box-shadow: 0 4px 16px #003f3210; margin-bottom: 20px;
      }
  .hero { text-align: center; }
  h1, h2, h3 { color: var(--verde); }
  h1 { font-size: clamp(28px, 5vw, 42px); }
      p { line-height: 1.7; }
      .btn {
        display: inline-block; background: #20a85a; color: white !important;
        padding: 12px 22px; margin-top: 12px; border-radius: 30px;
        text-decoration: none !important; font-weight: bold;
      }
      .grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
        gap: 16px; margin: 18px 0;
  .card { background: var(--verde-claro); padding: 20px; border-radius: 14px; }
  .emoji { font-size: 30px; }
  .segment { text-align: center; font-size: 20px; }
      .site-footer { text-align: center; color: #53665e; padding: 28px 10px; }
    </style>
    """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="site-header">
      <div class="logo">GM Consultoria Alimentar</div>
      <small>Especialistas em segurança alimentar</small>
    </header>
    <nav class="site-nav">
  <a href="#inicio">Início</a>
  <a href="#empresa">Quem somos</a>
  <a href="#servicos">Serviços</a>
      <a href="#segmentos">Segmentos</a>
      <a href="#contato">Orçamento</a>
    </nav>
  """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="hero" id="inicio">
      <h1>Seu negócio mais seguro!</h1>
      <p>Consultoria e assessoria especializada em segurança dos alimentos para sua empresa.</p>
      <a class="btn" href="https://wa.me/5561999277063" target="_blank" rel="noopener">
        Fale conosco pelo WhatsApp
      </a>
    </section>
    """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="content-card" id="empresa">
      <h2>Quem somos</h2>
  <p>A GM Consultoria Alimentar é especializada em consultoria e assessoria para estabelecimentos do setor alimentício.</p>
  <p>Nosso trabalho busca garantir segurança dos alimentos, organização, padronização dos processos e conformidade com a legislação sanitária aplicável.</p>
  <div class="card">
        <h3>Nosso propósito</h3>
        <p>Cuidar da segurança dos alimentos e da conformidade do seu estabelecimento, para que você possa focar no crescimento do seu negócio.</p>
      </div>
  </section>
  """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="content-card" id="servicos">
      <h2>Nossos serviços</h2>
      <div class="grid">
        <article class="card"><div class="emoji">🛡️</div><h3>Segurança dos alimentos e RT</h3><p>Responsabilidade técnica e orientação para alimentos seguros e conformidade sanitária.</p></article>
        <article class="card"><div class="emoji">📋</div><h3>MBP, POPs e BPF</h3><p>Elaboração, implantação e acompanhamento de documentos e boas práticas.</p></article>
  <article class="card"><div class="emoji">👩‍🍳</div><h3>Treinamento de equipe</h3><p>Capacitação da equipe com foco na prática e na segurança dos alimentos.</p></article>
  <article class="card"><div class="emoji">📈</div><h3>Gestão de processos</h3><p>Organização eficiente, segura e produtiva para o seu estabelecimento.</p></article>
  <article class="card"><div class="emoji">📑</div><h3>Apoio na licença sanitária</h3><p>Orientação e suporte durante o processo de regularização sanitária.</p></article>
  <article class="card"><div class="emoji">🔎</div><h3>Diagnóstico e plano de ação</h3><p>Identificação de oportunidades de melhoria e planejamento de soluções.</p></article>
  <article class="card"><div class="emoji">📊</div><h3>Relatórios mensais</h3><p>Acompanhamento técnico e avaliação contínua dos processos.</p></article>
  <article class="card"><div class="emoji">🍽️</div><h3>Fichas técnicas</h3><p>Padronização de preparações, ingredientes, rendimento e processos.</p></article>
      </div>
    </section>
    """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="content-card" id="segmentos">
      <h2>Quem atendemos</h2>
      <div class="grid">
        <div class="card segment">🍽️<p>Restaurantes</p></div>
        <div class="card segment">🥪<p>Lanchonetes</p></div>
  <div class="card segment">🥖<p>Padarias</p></div>
  <div class="card segment">🍔<p>Hamburguerias</p></div>
  <div class="card segment">🚚<p>Food Trucks</p></div>
  <div class="card segment">🛒<p>Mercados</p></div>
  <div class="card segment">🧸<p>Creches</p></div>
  <div class="card segment">🏪<p>Mercearias</p></div>
      </div>
    </section>
    """,
  unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="content-card" id="contato">
      <h2>Vamos encontrar a solução para sua empresa?</h2>
      <p>Preencha os dados abaixo. Sua solicitação será preparada para envio pelo WhatsApp.</p>
    </section>
    """,
  unsafe_allow_html=True,
)

with st.form("form_orcamento"):
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
      "Outro",
    ],
    index=0,
  )
  mensagem = st.text_area("Conte como podemos ajudar")
  enviar = st.form_submit_button("Preparar solicitação no WhatsApp")

if enviar:
  if not nome.strip() or not telefone.strip() or not segmento:
    st.error("Preencha nome, telefone e segmento.")
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
    url = "https://wa.me/5561999277063?text=" + urllib.parse.quote(texto)
    st.markdown(
      f'<a class="btn" href="{url}" target="_blank" rel="noopener">Abrir conversa no WhatsApp</a>',
      unsafe_allow_html=True,
  )

st.markdown(
  '<footer class="site-footer"><strong>GM Consultoria Alimentar</strong><br>Especialistas em segurança alimentar</footer>',
  unsafe_allow_html=True,
)
import streamlit as st
# CONFIGURAÇÃO BÁSICA
st.set_page_configescuro: #003f32;
      --verde-claro: #e9f7ed position: sticky;
      top: 0;
      20;
      box-shadow: 0 2px 12px #0001;
    }

    .logo {
      900;
      color: var(--verde);
    font-size: 10px;
      font-weight: 500;
      margin-top: 4px;
      background: var(--verde-escuro);
      display: flex;
      overflow-x: auto;
      gap      position: sticky;
      top: 58px;
      z-index: 19;
    }

    nav a {
      color: white      text-decoration: none;
      font-size:  white-space: nowrap;
    }

    nav a:hover(--lima);
    }

    section {
      padding: 38px hero {
      background: white;
      text-align: center;
      display: block;
      width: 100%;
      max-width: 1000px;
      margin: auto;
      border-radius: 14px;
    }

    h1 {
      color: var(--verde);
      font-size: clamp(26px, 6vw, 40px);
    }

    h2 {
      color: var(--verde);
      font-size: 25px;
    }

    p {
      line-height: 1.7;
    }

    border-radius: 30px;
      background: #20bd61;
      color: white;
      padding:px 23px;
      margin-top: 12px;
      text-decoration: none;
      font-weight: bold;
      cursor: pointer;
      font-size: 15px;
    }

    .: auto;
    }

    .grid {
      display-template-columns: repeat(auto-fit, minmax(220, 1fr));
      gap: 16px;
         padding: 22px;
      border-radius: 15px;
      box-shadow: 0 4px 16-top: 8px;
    }

    .emoji {
      font-size: 32px;
    }

 background: var(--verde-claro);
      padding: 25px;
      border-radius: 18px;
    }

    .px;
      text-align: center;
    }

    16px;
      bottom: 20px;
 none;
      border-radius: 40px;
     0003;
    }

    .status {
      text      section {
        padding: 55px 8 """,
    unsafe_allow_html=True,
)

# CABEÇALHO E MENU
st.markdown(
    """
    <header>
      <divEspecialistas em segurança alimentar</small>
      </div    </header>

    <nav>
      <a href="#inicio">Início</a>
      <a href="#empresa">Quem somos</a>
      <aservicos">Serviços</a>
      <a href="#segmentos">Segmentos</a>
      <a href="#contato">Orçamento</a>
    </nav>

    <ativo GM Consultoria Alimentar
    </div>
    """,
    unsafe_allow_html=True,
)

# INÍCIO
st.markdown(
    """
    <section class="hero" id="inicio">
      <div class="container">
        <!-- Troque o src abaixo pelo caminho correto da sua imagem -->
       img class="banner"
             src="assets/banner-horizontal             alt="GM Consultoria Alimentar">

        <h1>Seu negócio mais sempre!</h1>

        <p>
          Consultoria e assessoria especializada em segurança
          dos alimentos para sua empresa.
        </p>

        <a class="btn target="_blank">
           Fale conosco pelo WhatsApp
        </a>
      EMPRESA
st.markdown(
    """
    <section id="empresa">
      <div class="container">
        <h2>Quem somos</h2>

        <!-- Troque o src abaixo pelo caminho correto da sua imagem -->
        <img
          src="assets/banner-vertical.jpg"
Serviços da GM Consultoria Alimentar"
          style="
            width:100%;
            max-width:550px;
            display:block;
            margin:20px auto:16px;
          "
        >

        <p>
          A GM Consultoria Alimentar é especializada em
          consultoria e assessoria para estabelecimentos do
          setor alimentício.
        </p>

        <          Nosso trabalho busca garantir segurança dos alimentos,
          organização, padron dos processos e conformidade
          com a legislação sanitária aplicável.
        </p>

        <div class="destaque">
          <h3>Nosh3>
          <p>
            Cuidar da segurança dos alimentos e da conformidade
            do seu estabelecimento, para que você possa focar
            no crescimento do seu negócio.
          </p>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

OS
st.markdown(
    """
    <section id="servicos">
      <div class="container">
        <h2>Nossos serviços</ <article class="card">
            <div class="emoji">🛡️</div>
h3>Segurança dos alimentos e RT</h3>
            <p técnica e orientação para
              alimentos seguros e conformidade sanitária.
            </p>
          </article>

          <article class="card">
            <div class="emoji">📋</ <h3>MBP, POPs e BPF</h3>
            <p>
              Elaboração, implantação e acompanhamento
              de documentos">
            <div class="emoji">👩‍🍳</div>
            <h3              Capacitação da equipe com foco na prática
              e na segurança dos alimentos.
            </p>
          </article>

          <article class="card">
            <div class="emoji">📈</div>
            <h3>Organização eficiente, segura e produtiva.
            </p>
          </article>

          <article class="card">
            <div class="emoji">📑</div>
            <io na licença sanitária</h3>
            <ação e suporte durante o processo
              de regularização sanitária.
            </p>
          </article>

          <article class="card">
            <div class="emoji">🔎</div>
            <h3>Diagnóstico e plano de ação</h3>
            < melhoria e
              planejamento de soluções.
            </p3>Relatórios mensais</h3>
            <p>
              Acompanhamento técnico e avaliação
              contínua </article>

          <article class="card">
           as técnicas</h3>
            <p>
              Padronização de preparações, ingredientes,
              rendimento e processos.
            </p>
          </article>

        </div>
      </div>
    </",
    unsafe_allow_html=True,
)

# SEGMENT(
    """
    <section id="segmentos">
      <div class="container">
        <h2>Quem atendemos</h2>

        <div class="grid">
          <div class="card segmento">🍽️<p>Restaurantes</p></div>
          < segmento">🥪<p>Lanchonetes</p="card segmento">🥖<p>Padarias</p></div>
          <div class="card segmento">🍔<p>Hamburguerias</p></div>
          <div class="card segmento">🚚<p>Food Trucks</p></div>
          <div class="card segmento">🛒<p>Mercados</p></div>
          <div class<p>Creches</p></div>
          class="card segmento">🏪<p>Mercearias</p></div>
        </div>
    unsafe_allow_html=True,
)

# CONTATO (TEXTO SUPERIOR)
st.markdown(
    """
    <section id="contato">
      <div class="container">

        <div class="destaque">
          <h2>Vamos encontrar a solução para sua empresa?</h2>

          <p>
            Entre em
            do seu estabelecimento.
          </p>

          <a class="btn"
             href="wa.me/5561999277063"
             target="_blank">
             WhatsApp: (61) 99927-7063 <h2>Solicite seu orçamento</h2>

        <p>
          Preencha os dados abaixo. Sua solicitação será
          preparada para envio pelo WhatsApp.
        </p>

         </section>
    """,
    unsafe_allow_html=True,
)

# FORMULÁRIO (Streamlit)
st.markdown('<div class="container">', unsafe_allow_html=True)

with st.form("form_orcamento"):
    nome =.text_input("Seu nome *")
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
            "Creche            "Outro",
        ],
        index=0,
    )
    mensagem = st.text_area("Conte como podemos ajudar",")

st.markdown("</div>", unsafe_allow_html=True not nome or not telefone or not segmento:
        st.error("Preencha nome, telefone e segmento.")
    else:
        texto = "\n".join(
Olá! Gostaria de solicitar um orçamento da GM Consultoria Alimentar.",
                "",
                f"Nome                f"Estabelecimento: {empresa}",
                f"Telefone: {telefone}",
                f"Segmento: {segmento}",
                f"Solicitação: {mensagem}",
            ]
        )
        url = "https://wa.me/5561999277063?text=" + urllib.parse.quote(texto)
        st.success("Clique no botão abaixo para abrir o WhatsApp:")
        st.markdown(
            f'<a class="btn btn-dark target="_blank">'
            "Abrir conversa no WhatsApp</a>",
            CONSULTORIA ALIMENTAR</h3>
      <p>Especialistas em </footer>

    <a class="whatsapp-float"
       href="https://wa.me/5561999277063"
       target="_blank">
       WhatsApp
    </a>
    """,
    unsafe_allow_html=True,
)
