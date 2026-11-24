"""Textos en español (piloto 24.11.2026). Hechos solo de la app (ver docstring de build.py).

Búsquedas (sugerencias de Google, 24.11.2026): "alarma cada 30 minutos" (+ poner, programar),
"alarma cada hora android", "como mantenerse despierto" (+ para trabajar de noche, toda la
noche, para estudiar, sin café), "como no dormirse en el turno de noche".

Nombres de la app como en app/src/main/res/values-es: Sin límite, Temporizador, Empezar sesión,
¿Sigues despierto?, Finalizar sesión, Horarios, Fiabilidad, Probar alarma.
Las capturas muestran la app en inglés (no hay capturas en español todavía).
Prohibido: conducir (salvo la frase de límites, copiada literalmente de la ficha de Google Play),
promesas de seguridad laboral, "evita que te duermas", consejos médicos.
"""

APP = "Stay Awake"
NOTE_EN = " (captura de la app en inglés)"

C = {
    "app_name": APP,
    "lang_name": "Español",
    "og_locale": "es_ES",
    "ui": {
        "skip": "Ir al contenido",
        "nav": "Navegación principal",
        "guides": "Guías",
        "privacy": "Privacidad",
        "imprint": "Aviso legal",
        "faq": "Preguntas frecuentes",
        "toc": "En esta página",
        "crumbs": "Ruta de navegación",
        "updated": "Actualizado:",
        "with_app": "Con la app",
        "more_guides": "Más guías",
        "play_cta": "Disponible en Google Play",
        "play_note": "Gratis para Android · sin cuenta",
        "moreapps": "Más apps de Nice Developments",
        "footer_tag": "La alarma que pregunta si sigues despierto. Para Android.",
        "trademark": "Google Play y Android son marcas de Google LLC.",
    },

    "home": {
        "title": "Stay Awake: la alarma que pregunta si sigues despierto",
        "desc": "Una alarma suena una vez, la apagas y te vuelves a dormir. Stay Awake pregunta una y otra vez si sigues despierto, y suena hasta que respondes.",
        "kicker": "Para quien tiene que mantenerse despierto",
        "h1": "Una alarma suena una vez. Stay Awake sigue preguntando.",
        "lead": "Seguro que te ha pasado: suena la alarma, la apagas y a los cinco minutos te has vuelto a dormir. Stay Awake no se queda en un solo aviso. Cada 30 minutos, o en el intervalo que elijas, pregunta: **¿Sigues despierto?** Agita el teléfono o toca Sí, y empieza la siguiente ronda. ¿Sin respuesta? A los 10 segundos vibra y a los 20 suena una alarma, hasta que respondas.",
        "who": "Turnos de noche · guardias · noches de estudio · esperas de madrugada",
        "why_h2": "Por qué no basta con una alarma normal",
        "why_lead": "Una alarma está hecha para despertarte una vez. Mantenerse despierto significa aguantar hora tras hora, y lo difícil es el momento en que nadie comprueba si sigues ahí.",
        "why": [["Una alarma normal", ["Suena una vez, a la hora que fijaste antes.", "La apagas medio dormido y ya no viene nada más.", "Nunca pregunta si sigues despierto."]], ["Stay Awake", ["Pregunta una y otra vez, toda la noche, con el intervalo que elijas: de un minuto a doce horas.", "Primero pregunta en silencio. Solo si no respondes vibra y luego suena.", "La alarma suena hasta que respondes. Después empieza la siguiente ronda."]]],
        "hero_shot": "en-session.webp",
        "shots": {
            "en-session.webp": "Sesión en curso: un anillo ámbar alrededor de la cuenta atrás 29:50, debajo «hasta el próximo control», «Sin límite», «Cada 30 minutos · Tocar o agitar», el botón «Estoy despierto» y «Finalizar sesión».",
            "en-home.webp": "Pantalla de inicio: Sin límite o Temporizador, un selector redondo en 30 minutos y el botón Empezar sesión" + NOTE_EN + ".",
            "en-check.webp": "El control: «¿Sigues despierto?», debajo «o agita el teléfono», una línea de progreso, un botón grande Sí y, debajo, Finalizar sesión" + NOTE_EN + ".",
            "en-alarm.webp": "Tras 20 segundos sin respuesta: el mismo control, ahora con «Control sin responder» y una línea roja; la alarma está sonando" + NOTE_EN + ".",
            "en-schedules.webp": "Horarios: de 22:00 a 6:00, de lunes a viernes, cada 30 minutos, activado" + NOTE_EN + ".",
            "en-reliability.webp": "Comprobación de fiabilidad: «Listo» con nueve puntos en verde, de las notificaciones a la batería" + NOTE_EN + ".",
            "en-timer.webp": "Modo Temporizador: durante 2:00 h, control cada 30 minutos" + NOTE_EN + ".",
            "en-settings.webp": "Ajustes: tocar Sí siempre funciona; además, agitar el teléfono, darle la vuelta o un botón de volumen" + NOTE_EN + ".",
        },
        "steps_h2": "Qué pasa cuando toca un control",
        "steps_lead": "Primero suave, fuerte solo si hace falta. Cada paso se detiene en cuanto respondes.",
        "steps": [
            ["0 s", "La pregunta", "La pantalla se enciende, también sobre la pantalla de bloqueo, y pregunta: ¿Sigues despierto?"],
            ["10 s", "Vibración", "¿Aún sin respuesta? El teléfono empieza a vibrar."],
            ["20 s", "Alarma", "Sigue sin respuesta: una alarma de verdad con el sonido de alarma de tu teléfono."],
            ["Sí", "Siguiente ronda", "Un toque o una sacudida: todo se detiene y empieza de nuevo el intervalo completo."],
        ],
        "features_h2": "Empezar, confirmar, programar, comprobar",
        "features": [
            {"kicker": "Empezar", "h2": "Dos decisiones, un botón",
             "body": ["**Sin límite** o **Temporizador**, y cada cuánto quieres que te pregunte. Gira el selector: de un minuto a doce horas, para empezar 30 minutos. La app recuerda tu última elección.",
                      "El temporizador dura un tiempo fijo («durante 2 horas») o hasta una hora concreta («hasta las 5:30»)."],
             "shot": "en-home.webp"},
            {"kicker": "Confirmar", "h2": "Tocar, agitar, dar la vuelta: tú eliges",
             "body": ["El botón grande **Sí** siempre funciona. En los ajustes puedes añadir agitar el teléfono, darle la vuelta o un botón de volumen, en cualquier combinación. Agitar y dar la vuelta también funcionan con la pantalla apagada.",
                      "No hace falta esperar a la pregunta: confirma cuando quieras y el intervalo vuelve a empezar desde ese momento."],
             "shot": "en-check.webp"},
            {"kicker": "Turnos", "h2": "Horarios que empiezan solos",
             "body": ["Para noches que se repiten: hora de inicio y de fin, días de la semana opcionales, intervalo. La sesión empieza sola a la hora fijada y termina a la hora de fin.",
                      "Si no eliges ningún día, el horario se ejecuta una sola vez, en el próximo inicio."],
             "shot": "en-schedules.webp"},
            {"kicker": "Fiabilidad", "h2": "Sabe lo que permite tu teléfono",
             "body": ["Los teléfonos Android pueden retrasar o bloquear las alarmas: ahorro de batería, No molestar, permisos que faltan. La comprobación de **Fiabilidad** revisa cada punto en lenguaje claro y muestra cómo arreglar lo que no está bien.",
                      "Con **Probar alarma** oyes y sientes la alarma durante cinco segundos, antes de la primera noche de verdad."],
             "shot": "en-reliability.webp"},
        ],
        "limits_h2": "Límites honestos",
        "limits": "Stay Awake te ayuda a mantenerte despierto. No sustituye al sueño ni a las pausas, y no es un sistema de seguridad para el trabajo ni para conducir. Que un control llegue a tiempo depende también del teléfono: la comprobación de fiabilidad muestra lo que permite el tuyo.",
        "nots_h2": "Sin registro",
        "nots": [
            "**Sin cuenta, sin inicio de sesión.** Sesiones, horarios y ajustes se quedan en tu teléfono.",
            "**Funciona sin conexión.** Los controles y la alarma no necesitan internet.",
            "**Las sesiones sobreviven a un reinicio** del teléfono.",
            "**Gratis con un pequeño banner.** Sin anuncios en el control ni en la alarma. Stay Awake Pro quita el banner, con suscripción mensual o con un pago único.",
            "**20 idiomas**, del árabe al vietnamita.",
        ],
        "privacy_link": "Leer la política de privacidad (en inglés)",
        "guides_h2": "Guías para noches largas",
        "guides_lead": "Útiles también sin la app: una alarma cada 30 minutos, turnos de noche y noches enteras sin dormir.",
        "faq": [
            ["¿En qué se diferencia de un despertador normal?",
             ["Un despertador suena a una hora, estés despierto o no. Stay Awake pregunta primero y solo suena fuerte si no respondes. Está hecho para mantenerse despierto, no para despertarse por la mañana."]],
            ["¿Tengo que dejar la pantalla encendida?",
             ["No. Deja el teléfono a un lado, bloquéalo, deja que la pantalla se apague. El control aparece sobre la pantalla de bloqueo. Si elegiste agitar, una sacudida confirma incluso con la pantalla apagada."]],
            ["¿Qué sonido de alarma usa?",
             ["Por defecto, el sonido de alarma de tu propio teléfono. En los ajustes puedes cambiar a la melodía de Stay Awake o elegir otro sonido."]],
            ["¿Funciona sin internet?",
             ["Sí. Los controles, la vibración y la alarma funcionan por completo en el teléfono."]],
            ["¿Cuánto cuesta?",
             ["Todo lo que te mantiene despierto es gratis. La versión gratuita muestra un pequeño banner en las pantallas normales, nunca en el control ni en la alarma. Stay Awake Pro lo quita, con suscripción mensual o con un pago único; el precio aparece en Google Play."]],
            ["¿Hay versión para iPhone?",
             ["No, Stay Awake solo está disponible para Android."]],
        ],
        "final_h2": "Si tienes que mantenerte despierto, esta es tu app.",
        "final_body": "Empieza una sesión y deja el teléfono a un lado. Stay Awake sigue preguntando hasta que finalices la sesión.",
    },

    "guides_index": {
        "title": "Guías: alarma cada 30 minutos, turno de noche, toda la noche despierto",
        "desc": "Guías prácticas para noches largas: poner una alarma cada 30 minutos en Android, mantenerse despierto en el turno de noche y aguantar toda la noche.",
        "h1": "Guías para noches largas",
        "lead": "Respuestas cortas y prácticas, útiles con o sin app.",
        "app": "**Stay Awake** pregunta, con el intervalo que elijas, si sigues despierto y hace sonar una alarma si no llega respuesta.",
    },

    "guides": [
        {
            "id": "every30",
            "slug": "alarma-cada-30-minutos-android",
            "title": "Cómo poner una alarma cada 30 minutos en Android",
            "desc": "El reloj de Android no tiene la opción «cada 30 minutos». Tres formas que funcionan: varias alarmas, un temporizador reiniciado o una app de intervalos.",
            "h1": "Cómo poner una alarma cada 30 minutos en Android",
            "teaser": "Varias alarmas, un temporizador reiniciado o una app de intervalos: tres formas.",
            "answer": "Las apps de reloj de la mayoría de los teléfonos Android repiten una alarma solo **por días de la semana**, no cada X minutos. Tienes tres opciones: **crear varias alarmas**, **reiniciar un temporizador** cada vez o usar una **app de alarma por intervalos**.",
            "updated": "2026-11-24",
            "updated_label": "24 de noviembre de 2026",
            "sections": [
                ["several", "Opción 1: varias alarmas", [
                    "Crea en la app de reloj una alarma por cada media hora. Para una tarde está bien; para una noche entera se hace largo:",
                    {"table": [
                        ["Periodo", "Intervalo", "Alarmas necesarias"],
                        ["2 horas", "30 min", "4"],
                        ["8 horas (22:00–06:00)", "30 min", "16"],
                        ["8 horas", "15 min", "32"],
                    ]},
                    "Inconvenientes: hay que crearlas una a una, y las alarmas siguen sonando a horas fijas aunque estés bien despierto. Después tienes que desactivarlas todas otra vez.",
                ]],
                ["timer", "Opción 2: reiniciar un temporizador", [
                    {"steps": [
                        "Abre la app de reloj y ve a **Temporizador**.",
                        "Pon **30:00** e inícialo.",
                        "Cuando suene, detenlo y vuelve a iniciarlo.",
                    ]},
                    "Sencillo, pero tienes que reiniciarlo cada vez. Si se te olvida una sola vez, ya no pasa nada el resto de la noche.",
                ]],
                ["app", "Opción 3: una app de alarma por intervalos", [
                    "Las apps de alarma por intervalos se repiten solas. Antes de elegir una, comprueba tres cosas:",
                    {"list": [
                        "**¿Suena con la pantalla apagada y el teléfono bloqueado?** Muchas apps solo funcionan en primer plano.",
                        "**¿Usa alarmas exactas?** Si no, Android puede retrasarla en modo de ahorro de batería.",
                        "**¿Qué pasa si no reaccionas?** Una alarma repetida simple suena un rato y luego se detiene.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Una alarma por intervalos que pregunta primero",
                "body": [
                    "Stay Awake se repite con el intervalo que elijas, cualquier valor de un minuto a doce horas, y usa alarmas exactas. No suena de golpe: primero pregunta en silencio si sigues despierto. Responde y el intervalo vuelve a empezar desde ese momento. Sin respuesta: vibración a los 10 segundos, alarma a los 20.",
                    "Así no te sobresalta cuando estás despierto, y no te deja solo cuando no lo estás.",
                ],
                "shot": "en-home.webp",
                "alt": "Selector en 30 minutos, Sin límite o Temporizador, Empezar sesión" + NOTE_EN + ".",
            },
            "faq": [
                ["¿Puede el reloj de Android repetir una alarma cada 30 minutos?",
                 ["Las apps de reloj de la mayoría de los teléfonos Android solo repiten por días de la semana. Para cada 30 minutos necesitas varias alarmas, un temporizador o una app aparte."]],
                ["¿Por qué no suena mi alarma por intervalos con la pantalla apagada?",
                 ["A menudo la causa es la optimización de batería o que falta el permiso para alarmas exactas. Revisa en los ajustes de Android que la app no tenga restringido el uso de la batería."]],
                ["¿Se puede poner un intervalo de 15 o 45 minutos?",
                 ["En Stay Awake, sí: el selector va de un minuto a doce horas. Sin app, para cada 15 minutos necesitarías 32 alarmas en una noche de 8 horas."]],
            ],
        },
        {
            "id": "nightshift",
            "slug": "como-mantenerse-despierto-turno-de-noche",
            "title": "Cómo mantenerse despierto para trabajar de noche: 9 consejos",
            "desc": "Cómo no dormirse en el turno de noche: luz, movimiento, tareas pequeñas para las horas muertas hacia las 3 de la madrugada, comida y un ritmo de controles.",
            "h1": "Cómo mantenerse despierto para trabajar de noche",
            "teaser": "Luz, movimiento y un plan para las horas muertas de la madrugada.",
            "answer": "Lo difícil de un turno de noche casi nunca es el principio, sino el tramo tranquilo de la madrugada en el que no pasa nada. Lo que más ayuda es **luz, movimiento y un ritmo**: divide la noche en bloques cortos, dale a cada bloque algo que hacer y no te quedes mucho rato quieto con poca luz.",
            "updated": "2026-11-24",
            "updated_label": "24 de noviembre de 2026",
            "sections": [
                ["dead-hours", "Un plan para las horas muertas", [
                    "Quien trabaja de noche conoce el momento: en algún punto entre las 2 y las 5 todo se calma, el café ya no hace efecto y pesan los párpados. No dejes ese tramo al azar.",
                    {"list": [
                        "**Guarda para entonces las tareas activas.** Reponer, archivar, hacer rondas, revisar equipos: todo lo que te obligue a levantarte y caminar.",
                        "**Divide la noche en bloques** de 30 a 60 minutos. Cada bloque termina con una acción pequeña: levantarte, beber agua, escribir una línea en el registro.",
                        "**Evita tramos largos pasivos**, como leer o mirar una pantalla hundido en una silla.",
                    ]},
                ]],
                ["tips", "9 consejos que a mucha gente le funcionan", [
                    {"steps": [
                        "**Mantén la sala iluminada.** La luz tenue da sueño. Enciende la luz principal en vez de una sola lámpara, si tu puesto lo permite.",
                        "**Muévete cada media hora.** Un paseo por el pasillo, unas escaleras, estiramientos: bastan unos minutos.",
                        "**Haz de pie el trabajo rutinario.** Sentado es fácil dar una cabezada.",
                        "**Bebe agua con regularidad.** También te da un motivo para levantarte.",
                        "**Come en raciones pequeñas.** Mucha gente se siente pesada tras una comida grande en mitad de la noche; varios tentempiés pequeños sientan mejor.",
                        "**Usa agua fría.** En la cara o en las manos cuando llegue la pesadez.",
                        "**Habla con alguien.** Una conversación corta con un compañero rompe el tramo tranquilo, para los dos.",
                        "**Aire fresco.** Unos minutos junto a una ventana abierta o fuera.",
                        "**Haz controles a horas fijas.** Un aviso regular, cada 20 o 30 minutos, que pida una respuesta consciente te ayuda a notar cuando los minutos empiezan a convertirse en una hora sin darte cuenta.",
                    ]},
                ]],
                ["before", "Antes y después del turno", [
                    "Un turno de noche empieza antes de lo que dice el reloj: si llegas ya cansado, ningún consejo te va a salvar. Planifica tu sueño antes de la primera noche y protégelo después del turno: habitación a oscuras, teléfono en silencio y aviso a las personas con las que vives.",
                    {"note": "Si notas que das cabezadas una y otra vez, es una señal que hay que tomar en serio. Habla con tu equipo o con tu empresa: ninguna app ni ningún consejo sustituye al sueño."},
                ]],
            ],
            "app": {
                "h2": "Un control cada 30 minutos",
                "body": [
                    "Stay Awake convierte el consejo 9 en rutina: pregunta, con el intervalo que elijas, si sigues despierto. Agita el teléfono o toca Sí y empieza la siguiente ronda. Si no respondes, vibra a los 10 segundos y hace sonar una alarma a los 20.",
                    "Para turnos que se repiten, crea un **horario**, por ejemplo de 22:00 a 6:00, de lunes a viernes. La sesión empieza y termina sola.",
                ],
                "shot": "en-schedules.webp",
                "alt": "Horario de 22:00 a 6:00, de lunes a viernes, cada 30 minutos" + NOTE_EN + ".",
            },
            "faq": [
                ["¿Cuándo cuesta más mantenerse despierto en el turno de noche?",
                 ["A mucha gente le cuesta más de madrugada, más o menos entre las 2 y las 5. Planifica tareas activas para ese tramo."]],
                ["¿Ayuda el café en el turno de noche?",
                 ["Mucha gente toma café al empezar el turno. No sustituye a la luz, el movimiento y un ritmo, y cuánto es adecuado para ti no te lo puede decir una página web."]],
                ["¿Cómo no dormirse en una noche tranquila en la que no hay nada que hacer?",
                 ["Ponte pequeñas tareas fijas cada 30 a 60 minutos, levántate con regularidad y mantén la sala iluminada. Un aviso de control regular te ayuda a notar cuando empiezas a desconectar."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "como-mantenerse-despierto-toda-la-noche",
            "title": "Cómo mantenerse despierto toda la noche: un plan hora a hora",
            "desc": "Cuando tienes que pasar la noche en vela: un plan para el anochecer, la medianoche, las horas muertas y la mañana, y cómo notar si das una cabezada.",
            "h1": "Cómo mantenerse despierto toda la noche",
            "teaser": "Un plan para el anochecer, la medianoche, las horas muertas y la mañana.",
            "answer": "Una noche entera se lleva mejor con un plan que a base de fuerza de voluntad. Empieza la noche descansado, mantén **la luz encendida y el cuerpo activo**, deja para después de las 2 las tareas más activas y prepara algo que **compruebe cómo estás** con regularidad y suene fuerte si no llega respuesta.",
            "updated": "2026-11-24",
            "updated_label": "24 de noviembre de 2026",
            "sections": [
                ["plan", "Un plan para la noche", [
                    {"table": [
                        ["Cuándo", "Qué ayuda"],
                        ["Al anochecer", "Empieza descansado si puedes. Cena normal, nada pesado a última hora."],
                        ["Hasta medianoche", "Haz ahora el trabajo que necesita la cabeza más despejada."],
                        ["De medianoche a las 2", "Trabaja en bloques; levántate y muévete entre ellos."],
                        ["De 2 a 5", "El tramo más duro para mucha gente: tareas activas, mucha luz, aire fresco."],
                        ["Mañana", "La luz del día ayuda a mucha gente en el último tramo. No hagas nada que exija plena concentración."],
                    ]},
                ]],
                ["tricks", "Lo que te mantiene en marcha", [
                    {"list": [
                        "**Luz:** la luz principal encendida, la pantalla con suficiente brillo.",
                        "**Movimiento:** unos minutos cada media hora.",
                        "**Agua fría** en la cara y las manos.",
                        "**Algo que hacer con las manos** en vez de mirar sin más.",
                        "**Compañía:** una llamada o un chat con alguien que también esté despierto.",
                    ]},
                ]],
                ["notice", "Notar cuando das una cabezada", [
                    "El peligro de una noche larga no es caer rendido de golpe, sino los pequeños momentos: cierras los ojos «solo un minuto» y de repente ha pasado una hora. Eso solo lo notas cuando algo te pregunta desde fuera.",
                    "Sin app: un temporizador que reinicias cada vez que suena, o un amigo que te escribe para ver cómo estás. Con app: sigue leyendo.",
                ]],
                ["after", "El día siguiente", [
                    "Una noche sin dormir pasa factura. Planifica el día siguiente con calma y recupera el sueño en cuanto puedas.",
                    {"note": "Si pasar la noche en vela es buena idea para ti, solo puedes juzgarlo tú, o un médico. Esta guía trata de cómo aguantar una noche que ya has decidido pasar despierto."},
                ]],
            ],
            "app": {
                "h2": "Alguien que pregunta cada 30 minutos",
                "body": [
                    "Stay Awake pregunta, con el intervalo que elijas, si sigues despierto. Agita el teléfono o toca Sí y empieza la siguiente ronda. Si la respuesta no llega, el teléfono vibra a los 10 segundos y a los 20 suena una alarma, con el sonido de alarma de tu propio teléfono.",
                    "Empieza una sesión **Sin límite** para una noche sin hora de fin, o un **Temporizador** «hasta las 6:00».",
                ],
                "shot": "en-alarm.webp",
                "alt": "Control tras 20 segundos: Control sin responder, ¿Sigues despierto?, un botón grande Sí" + NOTE_EN + ".",
            },
            "faq": [
                ["¿A qué hora cuesta más mantenerse despierto?",
                 ["A mucha gente le cuesta más el tramo entre las 2 y las 5 de la madrugada, aproximadamente. Guarda para entonces las tareas más activas."]],
                ["¿Ayuda una siesta corta?",
                 ["Hay quien planifica una siesta corta. El riesgo es dormir mucho más de lo previsto; si lo haces, pon una alarma que no puedas ignorar."]],
                ["¿Cómo me aseguro de despertarme si doy una cabezada?",
                 ["Usa algo que compruebe cómo estás con regularidad y suene fuerte cuando no respondes: un amigo, un temporizador repetido o una app que pregunte si sigues despierto."]],
            ],
        },
    ],
}
