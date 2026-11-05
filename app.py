import urllib.parse
import streamlit as st

# CONFIGURAÇÃO .stApp {
        background: #f5faf 16px;
        box-shadow: 0 2px 12px #        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
      }

      .logo-text {
        font-size: 22px;
        font-weight: 800;
        color: var(--verde);
      }

      .logo-sub {
        font-size: 13px: #53665e;
      }

      /* Menu fixo (logo + nav) */
      .site-nav {
        display: flex;
        gap: 18px;
        background: var(--verde-escuro);
        padding: 10px 18px;
        border-radius: 999px;
        box 10px #0002;
        white-space: nowrap: white;
        text-decoration: none;
        font }

      .site-nav a:hover {
        color: var(--lima);
      }

     36px 10px;
      }

      .container {
        max-width: 1100px;
        margin: 0 auto;
      }

      .hero {
        background: white;
        border-radius: 14px;
        padding: 26px 28px;
        box-shadow: 0 4px 16px #0001;
        margin 16px;
      }

      .hero-content {
        display: grid;
        grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
        gap: 24px;
        align-items: center;
      }

      .hero img {
        width: 100%;
        border-radius: 14px;
        object-fit: cover;
      }

      h1, h2, h3 {
        color: var(--verde);
      }

      h1 {
        font-size: clamp(26px, 5vw, 40px);
        margin-bottom: 10px;
      }

      h2 {
        font-size: 24px;
 filter: brightness(1.05);
      }

             background: white;
        border-radius: 14px;
        padding: 26px 22px;
        box-shadow: 0 4px 16px #0001;
        margin: 16px;
      }

      .destaque {
        background: var(--verde-claro);
        padding: 18px 18px 16px;
        border-radius: 14px;
        margin-top: 16px;
      }

      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1));
        gap: 16px;
        margin-top: 18px;
      }

      .card {
        background: var(--verde-claro);
        padding: 18px;
        border-radius: 15px;
      }

      .card.segmento {
        text-align: center;
        font-size: 18px;
      }

      .emoji {
        font-size: 28px;
        margin-bottompx;
      }

      .site-footer {
        text-align: center;
        color: #53665e;
        padding: 28px 10px 34px;
        font-size: 14px;
      }

      /* Botão flutuante do WhatsApp */
      .whatsapp-float {
        position: 18px;
        bottom: 18px;
        background: #25d366;
        color: white !important;
        border-radius: 40px;
       px 16px;
        font-weight: 6000 3px 10px #0003;
        display: flex;
        align-items: center;
        gap: 8px;
        z-index: 200;
        font-size: 14px;
      }

      .whatsapp-float:hover {
        filter: brightness(1.07);
      }

      .whats-icon {
        font-size: 18px;
      }

      @media (max-width: 768px) {
        .hero-content {
          grid-template-columns: 1fr;
        }

                 flex-direction: column;
          align-items: flex-start;
          gap: 8px;
        }

        .site-nav {
          width: 100%;
          justify-content: space-between;
          overflow-x: auto;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

 CABEÇALHO + MENU
st.markdown(
   -header-wrap">
      <header class="site-header">
        <div>
          <div class="logo-text">GM Consultoria Alimentar</div>
          <div class="logo-sub">Especialistas em segurança alimentar</div>
        </div>
        <nav class="site-nav">
          <a href="#inicio">Início</a>
          <a href="#empresa">Quem somos</a>
          <a href="#servicos">Serviços</a>
          <a href="#segmentos">Segmentos</a>
          <a href="#contato">Orçamento</a>
        </nav>
      </header>
    </ INÍCIO (HERO)
st.markdown(
section id="inicio">
      <div class="container">
        <div class="hero">
          <div class="hero-content">
            <div>
              <h1>Seu negócio mais seguro!</h1>
              <p>
                Consultoria e assessoria especializada em segurança
                dos alimentos para sua empresa.
              </p>
              <a class="btn"
                 href="https://wa.me/5561999277063"
                 target="_blank"
                 rel="noopener">
                 Fale conosco pelo WhatsApp
              </a>
            </div>
            <div>
              <!-- Troque o src abaixo pelo caminho correto da sua imagem -->
              < src="https://via.placeholder.com/800x400?text=Banner+GM+Consultoria"
                   alt="GM Consultoria Alimentar - banner">
            </div>
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# EMPRESA
st.markdown(
    """
    <section id="empresa">
      <div class="container">
        <div class="content-card">
          <h2>Quem somos</h2>

          <img
           600?text=Banner+Vertical+GM"
            alt="Serviços da GM Consultoria Alimentar"
            style="
              width: 100%;
              max-width: 450px;
              display: block;
              margin: 18px auto;
              border-radius: 18px;
            "
          >

          <p>
            A GM Consultoria Alimentar é especializada em consultoria
            e assessoria para estabelecimentos do setor alimentício.
          </p>

          <p>
            Nosso trabalho busca garantir segurança dos alimentos,
            organização, padronização dos processos e conformidade
            com a legislação sanitária aplicável.
          </p>

          <div class="destaque">
3>Nosso propósito</h3>
            <p>
              Cuidar da segurança dos alimentos e da conformidade
              do seu estabelecimento, para que você possa focar
              no crescimento do seu negócio.
            </p>
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# SERVIÇOS
st.markdown(
    """
    <section id="servicos">
      <div class="container">
        <div class-card          <h2>Nossos serviços</h2>

          <div class="grid">
            <article class="card">
             ">🛡️</div>
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
             iva
                                      <article="">
             div classemoji"></div              <h3 licença sanitária</h3>
              <p>
                Orientação e suporte durante o processo
                de regularização sanitária.
              </p>
            </article>

            <article class="card">
              <div class="emoji">🔎</div>
              <h3>Diagnóstico e plano de ação</h3>
              <p>
                Identificação de oportunidades de melhoria e
                planejamento de soluções.
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
                Padronização de prepar,,
                rendimento e processos.
              </p>
            </article>
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# SEGMENTOS
st.markdown(
    """
    <section id="segmentos">
      <div class="container">
        <div class="content-card">
          <h2>Quem atendemos</h2>

          <div class="grid">
            <div class="card segmento">🍽️<p>Restaurantes</p></div>
            <div class="card segmento">p>Lanchonetes</p></div>
            <div class="card segmento">>
            <div class="card segmento">🍔<p>Hamburguerias</p></div>
            <div class="card segmento">🚚<p>Food Trucks</p></div>
            <div class="card segmento">🛒<p>Merc <div class="card segmento">🧸<p>div class="card segmento">🏪<p>Mercearias <div class="content-card">
          <h2>Vamos encontrar a solução para sua empresa?</ em contato pelo WhatsApp ou preencha os dados
            abaixo. Sua solicitação será preparada para envio
            direto WhatsApp.
          </p>
        </div>
      </div>
    </section>
    """,
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

st.markdown("</div>", unsafe_allow_html=True:
    if not nome.strip() or not telefone.strip() or not segmento:
        nome, telefone e segmento.")
    else:
        textoaria de solicitar um orçamento da GM Consultoria Alimentar.",
                "",
                f"Nome: {nomeEstabelecimento: {empresa.strip() or 'Não informado'}",
                f"Telefone: {telefone.strip()}",
                f"Segmento}",
                f"Solicitação: {mensagem.strip() or 'Não informado'}",
            ]
        )
        url = "https://wa.me/7063?text=" + urllib.parse.quote(texto)
        st.success("Clique abaixo para abrir o WhatsApp:")
        st.markdown(
            f'<a class="btn" href="{url}" target_allow_html=True,
        )

# RODAPÉ
