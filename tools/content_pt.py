"""Textos em português do Brasil (piloto 24.11.2026). Fatos só do app (ver docstring de build.py).

Buscas (sugestões do Google, 24.11.2026): "alarme a cada 30 minutos" (+ como colocar),
"despertador de 30 em 30 minutos", "como ficar acordado" (+ a noite toda, no trabalho, mesmo com
sono, de madrugada).

Nomes do app como em app/src/main/res/values-pt-rBR: Sem limite, Timer, Começar sessão,
Você ainda está acordado?, Encerrar sessão, Agendamentos, Confiabilidade, Testar alarme.
As capturas mostram o app em inglês. Aspas “ ” (Brasil), não « ».
Proibido: dirigir (exceto a frase de limites, copiada literalmente da página do Google Play),
promessas de segurança do trabalho, "impede de dormir", conselhos médicos.
"""

APP = "Stay Awake"
NOTE_EN = " (captura do app em inglês)"

C = {
    "app_name": APP,
    "lang_name": "Português",
    "og_locale": "pt_BR",
    "ui": {
        "skip": "Ir para o conteúdo",
        "nav": "Navegação principal",
        "guides": "Guias",
        "privacy": "Privacidade",
        "imprint": "Informações legais",
        "faq": "Perguntas frequentes",
        "toc": "Nesta página",
        "crumbs": "Trilha de navegação",
        "updated": "Atualizado:",
        "with_app": "Com o app",
        "more_guides": "Mais guias",
        "play_cta": "Disponível no Google Play",
        "play_note": "Grátis para Android · sem conta",
        "moreapps": "Mais apps da Nice Developments",
        "footer_tag": "O alarme que pergunta se você ainda está acordado. Para Android.",
        "trademark": "Google Play e Android são marcas da Google LLC.",
    },

    "home": {
        "title": "Stay Awake: o alarme que pergunta se você ainda está acordado",
        "desc": "Um alarme toca uma vez, você desliga e dorme de novo. O Stay Awake continua perguntando se você ainda está acordado – e toca até você responder.",
        "kicker": "Para quem precisa ficar acordado",
        "h1": "Um alarme toca uma vez. O Stay Awake continua perguntando.",
        "lead": "Você conhece a cena: o alarme toca, você desliga – e cinco minutos depois já está dormindo de novo. O Stay Awake não fica em um aviso só. A cada 30 minutos, ou no intervalo que você escolher, ele pergunta: **Você ainda está acordado?** Agite o celular ou toque em Sim, e a próxima rodada começa. Sem resposta? O celular vibra após 10 segundos e, após 20, toca um alarme – até você responder.",
        "who": "Turnos da noite · plantões · noites de estudo · esperas de madrugada",
        "why_h2": "Por que um alarme comum não basta",
        "why_lead": "Um alarme é feito para acordar você uma vez. Ficar acordado é aguentar hora após hora – e o difícil é o momento em que ninguém confere se você ainda está aí.",
        "why": [["Um alarme comum", ["Toca uma vez – no horário que você definiu antes.", "Você desliga meio dormindo, e depois não vem mais nada.", "Nunca pergunta se você ainda está acordado."]], ["Stay Awake", ["Pergunta de novo e de novo, a noite toda – no intervalo que você escolher, de um minuto a doze horas.", "Primeiro pergunta em silêncio. Só se você não responder ele vibra e depois toca.", "O alarme toca até você responder. Depois começa a próxima rodada."]]],
        "hero_shot": "en-session.webp",
        "shots": {
            "en-session.webp": "Sessão em andamento: um anel âmbar em volta da contagem regressiva 29:50, abaixo “até a próxima verificação”, “Sem limite”, “A cada 30 minutos · Tocar ou agitar”, o botão “Estou acordado” e “Encerrar sessão”.",
            "en-home.webp": "Tela inicial: Sem limite ou Timer, um seletor redondo em 30 minutos e o botão Começar sessão" + NOTE_EN + ".",
            "en-check.webp": "A verificação: “Você ainda está acordado?”, abaixo “ou agite o celular”, uma linha de progresso, um botão grande Sim e, embaixo, Encerrar sessão" + NOTE_EN + ".",
            "en-alarm.webp": "Após 20 segundos sem resposta: a mesma verificação, agora com “Verificação perdida” e uma linha vermelha; o alarme está tocando" + NOTE_EN + ".",
            "en-schedules.webp": "Agendamentos: das 22:00 às 6:00, de segunda a sexta, a cada 30 minutos, ativado" + NOTE_EN + ".",
            "en-reliability.webp": "Checagem de confiabilidade: “Pronto” com nove itens verdes, das notificações à bateria" + NOTE_EN + ".",
            "en-timer.webp": "Modo Timer: por 2:00 h, verificação a cada 30 minutos" + NOTE_EN + ".",
            "en-settings.webp": "Configurações: tocar em Sim sempre funciona; além disso, agitar o celular, virá-lo ou um botão de volume" + NOTE_EN + ".",
        },
        "steps_h2": "O que acontece quando chega uma verificação",
        "steps_lead": "Primeiro de leve, alto só se for preciso. Cada etapa para no momento em que você responde.",
        "steps": [
            ["0 s", "A pergunta", "A tela acende – também sobre a tela de bloqueio – e pergunta: Você ainda está acordado?"],
            ["10 s", "Vibração", "Ainda sem resposta? O celular começa a vibrar."],
            ["20 s", "Alarme", "Ainda nada: um alarme de verdade com o som de alarme do seu celular."],
            ["Sim", "Próxima rodada", "Um toque ou uma sacudida: tudo para e o intervalo inteiro começa de novo."],
        ],
        "features_h2": "Começar, confirmar, agendar, conferir",
        "features": [
            {"kicker": "Começar", "h2": "Duas decisões, um botão",
             "body": ["**Sem limite** ou **Timer**, e de quanto em quanto tempo o app deve perguntar. Gire o seletor – de um minuto a doze horas, 30 minutos para começar. O app lembra a sua última escolha.",
                      "O timer dura um tempo fixo (“por 2 horas”) ou até um horário (“até 5:30”)."],
             "shot": "en-home.webp"},
            {"kicker": "Confirmar", "h2": "Tocar, agitar, virar – você escolhe",
             "body": ["O botão grande **Sim** sempre funciona. Nas configurações você pode adicionar agitar o celular, virá-lo ou um botão de volume, em qualquer combinação. Agitar e virar funcionam também com a tela apagada.",
                      "Não precisa esperar a pergunta: confirme quando quiser, e o intervalo recomeça a partir daquele momento."],
             "shot": "en-check.webp"},
            {"kicker": "Turnos", "h2": "Agendamentos que começam sozinhos",
             "body": ["Para noites que se repetem: horário de início e de fim, dias da semana opcionais, intervalo. A sessão começa sozinha no horário definido e termina no horário de fim.",
                      "Sem nenhum dia selecionado, o agendamento roda uma única vez, no próximo início."],
             "shot": "en-schedules.webp"},
            {"kicker": "Confiabilidade", "h2": "Sabe o que o seu celular permite",
             "body": ["Celulares Android podem atrasar ou bloquear alarmes – economia de bateria, Não perturbe, permissões que faltam. A checagem de **Confiabilidade** passa por cada ponto em linguagem simples e mostra como corrigir o que não está certo.",
                      "Com **Testar alarme** você ouve e sente o alarme por cinco segundos, antes da primeira noite de verdade."],
             "shot": "en-reliability.webp"},
        ],
        "limits_h2": "Limites honestos",
        "limits": "O Stay Awake ajuda você a ficar acordado. Ele não substitui o sono nem as pausas e não é um sistema de segurança para o trabalho ou para dirigir. Se uma verificação chega na hora, isso também depende do celular – a checagem de confiabilidade mostra o que o seu permite.",
        "nots_h2": "Sem cadastro",
        "nots": [
            "**Sem conta, sem login.** Sessões, agendamentos e configurações ficam no seu celular.",
            "**Funciona offline.** As verificações e o alarme não precisam de internet.",
            "**As sessões sobrevivem a uma reinicialização** do celular.",
            "**Grátis com um pequeno banner.** Sem anúncios na verificação nem no alarme. O Stay Awake Pro remove o banner – com assinatura mensal ou pagamento único.",
            "**20 idiomas**, do árabe ao vietnamita.",
        ],
        "privacy_link": "Ler a política de privacidade (em inglês)",
        "guides_h2": "Guias para noites longas",
        "guides_lead": "Úteis também sem o app: um alarme a cada 30 minutos, o turno da noite e a noite toda acordado.",
        "faq": [
            ["Qual é a diferença para um despertador comum?",
             ["Um despertador toca num horário, você estando acordado ou não. O Stay Awake pergunta primeiro e só toca alto se você não responder. Ele é feito para ficar acordado, não para acordar de manhã."]],
            ["Preciso deixar a tela ligada?",
             ["Não. Deixe o celular de lado, bloqueie, deixe a tela apagar. A verificação aparece sobre a tela de bloqueio. Se você escolheu agitar, basta sacudir o celular para confirmar, mesmo com a tela apagada."]],
            ["Qual som de alarme ele usa?",
             ["Por padrão, o som de alarme do seu próprio celular. Nas configurações você pode trocar para a melodia do Stay Awake ou escolher outro som."]],
            ["Funciona sem internet?",
             ["Sim. Verificações, vibração e alarme rodam inteiramente no celular."]],
            ["Quanto custa?",
             ["Tudo o que mantém você acordado é grátis. A versão gratuita mostra um pequeno banner nas telas normais, nunca na verificação nem no alarme. O Stay Awake Pro remove o banner, com assinatura mensal ou pagamento único; o preço aparece no Google Play."]],
            ["Existe versão para iPhone?",
             ["Não, o Stay Awake só está disponível para Android."]],
        ],
        "final_h2": "Se você precisa ficar acordado, este é o seu app.",
        "final_body": "Comece uma sessão e deixe o celular de lado. O Stay Awake continua perguntando até você encerrar a sessão.",
    },

    "guides_index": {
        "title": "Guias: alarme a cada 30 minutos, turno da noite, a noite toda acordado",
        "desc": "Guias práticos para noites longas: colocar um alarme a cada 30 minutos no Android, ficar acordado no turno da noite e aguentar a noite toda.",
        "h1": "Guias para noites longas",
        "lead": "Respostas curtas e práticas, úteis com ou sem app.",
        "app": "O **Stay Awake** pergunta, no intervalo que você escolher, se você ainda está acordado e toca um alarme se não vier resposta.",
    },

    "guides": [
        {
            "id": "every30",
            "slug": "alarme-a-cada-30-minutos-android",
            "title": "Como colocar um alarme a cada 30 minutos no Android",
            "desc": "O relógio do Android não tem a opção “a cada 30 minutos”. Três jeitos que funcionam: vários alarmes, um timer reiniciado ou um app de alarme por intervalo.",
            "h1": "Como colocar um alarme a cada 30 minutos no Android",
            "teaser": "Vários alarmes, um timer reiniciado ou um app de intervalos – três jeitos.",
            "answer": "Os apps de relógio da maioria dos celulares Android repetem um alarme só **por dia da semana**, não a cada X minutos. Você tem três opções: **criar vários alarmes**, **reiniciar um timer** toda vez ou usar um **app de alarme por intervalo**.",
            "updated": "2026-11-24",
            "updated_label": "24 de novembro de 2026",
            "sections": [
                ["several", "Opção 1: vários alarmes", [
                    "Crie no app de relógio um alarme para cada meia hora. Para uma tarde, tudo bem; para uma noite inteira, dá trabalho:",
                    {"table": [
                        ["Período", "Intervalo", "Alarmes necessários"],
                        ["2 horas", "30 min", "4"],
                        ["8 horas (22:00–06:00)", "30 min", "16"],
                        ["8 horas", "15 min", "32"],
                    ]},
                    "Desvantagens: é preciso criar um por um, e os alarmes continuam tocando em horários fixos mesmo que você esteja bem acordado. Depois você precisa desligar todos de novo.",
                ]],
                ["timer", "Opção 2: reiniciar um timer", [
                    {"steps": [
                        "Abra o app de relógio e vá em **Timer**.",
                        "Defina **30:00** e inicie.",
                        "Quando tocar, pare e inicie de novo.",
                    ]},
                    "Simples, mas você precisa reiniciar toda vez. Se esquecer uma única vez, não acontece mais nada pelo resto da noite.",
                ]],
                ["app", "Opção 3: um app de alarme por intervalo", [
                    "Apps de alarme por intervalo se repetem sozinhos. Antes de escolher um, confira três coisas:",
                    {"list": [
                        "**Ele toca com a tela apagada e o celular bloqueado?** Muitos apps só funcionam em primeiro plano.",
                        "**Ele usa alarmes exatos?** Se não, o Android pode atrasá-lo no modo de economia de bateria.",
                        "**O que acontece se você não reagir?** Um alarme repetido simples toca por um tempo e depois para.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Um alarme por intervalo que pergunta primeiro",
                "body": [
                    "O Stay Awake se repete no intervalo que você escolher – qualquer valor de um minuto a doze horas – e usa alarmes exatos. Ele não toca de cara: primeiro pergunta em silêncio se você ainda está acordado. Responda, e o intervalo recomeça a partir desse momento. Sem resposta: vibração após 10 segundos, alarme após 20.",
                    "Assim ele não assusta você quando você está acordado – e não deixa você sozinho quando não está.",
                ],
                "shot": "en-home.webp",
                "alt": "Seletor em 30 minutos, Sem limite ou Timer, Começar sessão" + NOTE_EN + ".",
            },
            "faq": [
                ["O relógio do Android consegue repetir um alarme a cada 30 minutos?",
                 ["Os apps de relógio da maioria dos celulares Android só repetem por dia da semana. Para tocar a cada 30 minutos, você precisa de vários alarmes, de um timer ou de um app separado."]],
                ["Por que meu alarme por intervalo não toca com a tela apagada?",
                 ["Muitas vezes a causa é a otimização de bateria ou a falta da permissão para alarmes exatos. Confira nas configurações do Android se o uso de bateria do app não está restrito."]],
                ["Dá para usar um intervalo de 15 ou 45 minutos?",
                 ["No Stay Awake, sim: o seletor vai de um minuto a doze horas. Sem app, para tocar a cada 15 minutos você precisaria de 32 alarmes numa noite de 8 horas."]],
            ],
        },
        {
            "id": "nightshift",
            "slug": "como-ficar-acordado-no-turno-da-noite",
            "title": "Como ficar acordado no trabalho à noite: 9 dicas práticas",
            "desc": "Como ficar acordado no turno da noite: luz, movimento, pequenas tarefas para as horas mortas por volta das 3 da manhã, comida e um ritmo de verificações.",
            "h1": "Como ficar acordado no trabalho à noite",
            "teaser": "Luz, movimento e um plano para as horas mortas da madrugada.",
            "answer": "O difícil de um turno da noite quase nunca é o começo – é o período parado da madrugada, quando nada acontece. O que mais ajuda é **luz, movimento e um ritmo**: divida a noite em blocos curtos, dê a cada bloco algo para fazer e não fique muito tempo parado com pouca luz.",
            "updated": "2026-11-24",
            "updated_label": "24 de novembro de 2026",
            "sections": [
                ["dead-hours", "Um plano para as horas mortas", [
                    "Quem trabalha à noite conhece o momento: em algum ponto entre 2 e 5 da manhã tudo fica quieto, o efeito do café já passou e os olhos pesam. Não deixe esse período ao acaso.",
                    {"list": [
                        "**Guarde as tarefas ativas para essa hora.** Repor estoque, arquivar, fazer rondas, conferir equipamentos – tudo o que faz você levantar e andar.",
                        "**Divida a noite em blocos** de 30 a 60 minutos. Cada bloco termina com uma ação pequena: levantar, beber água, escrever uma linha no registro.",
                        "**Evite períodos longos e passivos**, como ler ou olhar uma tela afundado numa cadeira.",
                    ]},
                ]],
                ["tips", "9 dicas que funcionam para muita gente", [
                    {"steps": [
                        "**Mantenha o ambiente claro.** Luz fraca dá sono. Acenda a luz principal em vez de um abajur só, se o seu local de trabalho permitir.",
                        "**Mexa-se a cada meia hora.** Uma volta pelo corredor, alguns degraus, alongamento – alguns minutos bastam.",
                        "**Faça o trabalho de rotina em pé.** Sentado é fácil cochilar.",
                        "**Beba água com regularidade.** Isso também dá um motivo para levantar.",
                        "**Coma em porções pequenas.** Muita gente se sente pesada depois de uma refeição grande no meio da noite; alguns lanches pequenos caem melhor.",
                        "**Use água fria.** No rosto ou nas mãos quando o sono pesar.",
                        "**Converse com alguém.** Uma conversa curta com um colega quebra a monotonia – para os dois.",
                        "**Ar fresco.** Alguns minutos numa janela aberta ou do lado de fora.",
                        "**Faça verificações em horários fixos.** Um lembrete regular – a cada 20 ou 30 minutos – que pede uma resposta consciente ajuda você a perceber quando os minutos começam a virar uma hora sem você notar.",
                    ]},
                ]],
                ["before", "Antes e depois do turno", [
                    "Um turno da noite começa antes do que diz o relógio: se você já chega cansado, nenhuma dica resolve. Planeje o sono antes da primeira noite e proteja-o depois do turno – quarto escuro, celular no silencioso e as pessoas com quem você mora avisadas.",
                    {"note": "Se você percebe que cochila várias vezes, é um sinal para levar a sério. Fale com a sua equipe ou com o seu empregador – nenhum app e nenhuma dica substituem o sono."},
                ]],
            ],
            "app": {
                "h2": "Uma verificação a cada 30 minutos",
                "body": [
                    "O Stay Awake transforma a dica 9 em rotina: pergunta, no intervalo que você escolher, se você ainda está acordado. Agite o celular ou toque em Sim e a próxima rodada começa. Se você não responder, ele vibra após 10 segundos e toca um alarme após 20.",
                    "Para turnos que se repetem, crie um **agendamento** – por exemplo das 22:00 às 6:00, de segunda a sexta. A sessão começa e termina sozinha.",
                ],
                "shot": "en-schedules.webp",
                "alt": "Agendamento das 22:00 às 6:00, de segunda a sexta, a cada 30 minutos" + NOTE_EN + ".",
            },
            "faq": [
                ["Quando é mais difícil ficar acordado no turno da noite?",
                 ["Para muita gente, de madrugada, mais ou menos entre 2 e 5 da manhã. Planeje tarefas ativas para esse período."]],
                ["Café ajuda no turno da noite?",
                 ["Muita gente toma café no começo do turno. Ele não substitui luz, movimento e um ritmo – e quanto é certo para você não é algo que um site possa dizer."]],
                ["Como ficar acordado numa noite tranquila em que não há nada para fazer?",
                 ["Defina pequenas tarefas fixas a cada 30 a 60 minutos, levante-se com regularidade e mantenha o ambiente claro. Um lembrete de verificação regular ajuda você a perceber quando começa a se desligar."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "como-ficar-acordado-a-noite-toda",
            "title": "Como ficar acordado a noite toda: um plano hora a hora",
            "desc": "Quando você precisa virar a noite: um plano para o começo da noite, a meia-noite, as horas mortas e a manhã – e como perceber se você cochilar.",
            "h1": "Como ficar acordado a noite toda",
            "teaser": "Um plano para o começo da noite, a meia-noite, as horas mortas e a manhã.",
            "answer": "Uma noite inteira vai melhor com um plano do que só com força de vontade. Comece a noite descansado, mantenha **a luz acesa e o corpo ativo**, deixe para depois das 2 da manhã as tarefas mais ativas – e prepare algo que **confira como você está** de tempos em tempos e toque alto se a resposta não vier.",
            "updated": "2026-11-24",
            "updated_label": "24 de novembro de 2026",
            "sections": [
                ["plan", "Um plano para a noite", [
                    {"table": [
                        ["Quando", "O que ajuda"],
                        ["Começo da noite", "Comece descansado, se puder. Faça uma refeição normal, nada pesado tarde da noite."],
                        ["Até a meia-noite", "Faça agora o trabalho que precisa da cabeça mais fresca."],
                        ["Da meia-noite às 2", "Trabalhe em blocos; levante e se mexa entre eles."],
                        ["Das 2 às 5", "A parte mais difícil para muita gente: tarefas ativas, muita luz, ar fresco."],
                        ["Manhã", "A luz do dia ajuda muita gente na reta final. Não faça nada que exija concentração total."],
                    ]},
                ]],
                ["tricks", "O que mantém você de pé", [
                    {"list": [
                        "**Luz:** a luz principal acesa, a tela com brilho suficiente.",
                        "**Movimento:** alguns minutos a cada meia hora.",
                        "**Água fria** no rosto e nas mãos.",
                        "**Algo para fazer com as mãos** em vez de só assistir.",
                        "**Companhia:** uma ligação ou uma conversa por mensagem com alguém que também esteja acordado.",
                    ]},
                ]],
                ["notice", "Perceber quando você cochila", [
                    "O perigo de uma noite longa não é um grande apagão, e sim os pequenos momentos: você fecha os olhos “só um minuto” e de repente passou uma hora. Isso você só percebe quando alguma coisa de fora pergunta.",
                    "Sem app: um timer que você reinicia toda vez que toca, ou um amigo que manda mensagem para saber como você está. Com app: veja abaixo.",
                ]],
                ["after", "O dia seguinte", [
                    "Uma noite sem dormir cobra o seu preço. Pegue leve no dia seguinte e recupere o sono assim que puder.",
                    {"note": "Se virar a noite é uma boa ideia para você, só você – ou um médico – pode avaliar. Este guia é sobre aguentar uma noite que você já decidiu passar acordado."},
                ]],
            ],
            "app": {
                "h2": "Alguém que pergunta a cada 30 minutos",
                "body": [
                    "O Stay Awake pergunta, no intervalo que você escolher, se você ainda está acordado. Agite o celular ou toque em Sim e a próxima rodada começa. Se a resposta não vier, o celular vibra após 10 segundos e um alarme toca após 20 – com o som de alarme do seu próprio celular.",
                    "Comece uma sessão **Sem limite** para uma noite sem hora para acabar, ou um **Timer** “até 6:00”.",
                ],
                "shot": "en-alarm.webp",
                "alt": "Verificação após 20 segundos: Verificação perdida, Você ainda está acordado?, um botão grande Sim" + NOTE_EN + ".",
            },
            "faq": [
                ["Em que horário é mais difícil ficar acordado?",
                 ["Muita gente acha mais difícil o período entre 2 e 5 da manhã, mais ou menos. Guarde para essa hora as tarefas mais ativas."]],
                ["Um cochilo curto ajuda?",
                 ["Algumas pessoas planejam um cochilo curto. O risco é dormir muito mais do que o planejado – se fizer isso, coloque um alarme que você não consiga ignorar."]],
                ["Como garantir que eu acorde se cochilar?",
                 ["Use algo que confira como você está de tempos em tempos e toque alto quando você não responder – um amigo, um timer repetido ou um app que pergunte se você ainda está acordado."]],
            ],
        },
    ],
}
