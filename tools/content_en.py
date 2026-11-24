"""English texts. Facts only from the app (see build.py docstring).

Search queries the guides aim at (Google suggestions, 21 Nov 2026):
- how to stay awake on night shift (+ nurse, without coffee, graveyard shift)
- how to stay awake while studying (+ at night, all night)
- how to stay awake all night
- how to stay awake without caffeine (+ at night, at work, to study)
- alarm every 30 minutes (+ android, app) / interval alarm app / repeating alarm android
- interval alarm / alarm that checks if you are awake (no suggestions, but the app's core idea)
- android alarm not going off (+ samsung, sometimes, after update)

Forbidden in every text: driving/road traffic, workplace-safety promises, "prevents falling
asleep", medical advice. The only mention of driving is the honest-limits line on the home page,
which repeats the Play listing word for word.
"""

APP = "Stay Awake"

C = {
    "app_name": APP,
    "lang_name": "English",
    "og_locale": "en_US",
    "ui": {
        "skip": "Skip to content",
        "nav": "Main navigation",
        "guides": "Guides",
        "privacy": "Privacy",
        "imprint": "Imprint",
        "faq": "Questions and answers",
        "toc": "On this page",
        "crumbs": "Breadcrumbs",
        "updated": "Updated:",
        "with_app": "With the app",
        "more_guides": "More guides",
        "play_cta": "Get it on Google Play",
        "play_note": "Free for Android · no account",
        "moreapps": "More apps by Nice Developments",
        "footer_tag": "Wake check timer for Android.",
        "trademark": "Google Play and Android are trademarks of Google LLC.",
    },

    # ------------------------------------------------------------ Home
    "home": {
        "title": "Stay Awake – the alarm that keeps asking if you’re still awake",
        "desc": "A normal alarm rings once, you switch it off and fall asleep again. Stay Awake keeps asking whether you’re still awake – and rings until you answer.",
        "kicker": "For everyone who has to stay awake",
        "h1": "An alarm rings once. Stay Awake keeps asking.",
        "lead": "You know it: the alarm goes off, you switch it off – and five minutes later you’re asleep again. Stay Awake doesn’t stop after one ring. Every 30 minutes, or at whatever interval you set, it asks: **Are you still awake?** One shake or one tap and the next round begins. No answer? It vibrates after 10 seconds, and after 20 an alarm rings – until you answer.",
        "who": "Night shifts · standby · study nights · waiting through the night",
        "why_h2": "Why a normal alarm isn’t enough",
        "why_lead": "An alarm is built to wake you up once. Staying awake means getting through hour after hour – and the hard part is the moment nobody checks on you.",
        "why": [["A normal alarm", ["Rings once – at a time you set in advance.", "Switched off half asleep, and nothing comes after it.", "Never asks whether you’re still awake."]], ["Stay Awake", ["Asks again and again, all night – at your interval, from one minute to twelve hours.", "Asks quietly first. Only if you don’t answer does it vibrate, then ring.", "The alarm rings until you answer. Then the next round starts."]]],
        "hero_shot": "en-session.webp",
        "shots": {
            "en-session.webp": "Running session: an amber ring around the countdown 29:50, below it “until next check”, “Unlimited”, “Every 30 minutes · Tap or shake”, the button “I am awake” and “End session”.",
            "en-home.webp": "Home screen: Unlimited or Timer, a round dial set to 30 minutes and the button Start session.",
            "en-check.webp": "The check: “Are you still awake?”, below it “or shake the phone”, a thin progress line and a large Yes button, End session underneath.",
            "en-alarm.webp": "After 20 seconds without an answer: the same check, now with “Check missed” and a red line. The alarm is sounding.",
            "en-schedules.webp": "Schedules: 10:00 PM – 6:00 AM, Monday to Friday, every 30 minutes, switched on.",
            "en-reliability.webp": "Reliability check: “Ready” with nine green items – notifications, check and alarm alerts, on-time wake-ups, over the lock screen, alarm volume, Do Not Disturb, vibration, background and battery, chosen actions.",
            "en-timer.webp": "Timer mode: For 2:00 h, check interval 30 minutes.",
            "en-settings.webp": "Settings: tapping Yes always works; in addition shake the phone, flip the phone or volume button.",
        },
        "steps_h2": "What happens when a check is due",
        "steps_lead": "Soft first, loud only if needed. Every step stops the moment you answer.",
        "steps": [
            ["0 s", "The question", "The screen lights up – over the lock screen too – and asks: Are you still awake?"],
            ["10 s", "Vibration", "No answer yet? The phone starts to vibrate."],
            ["20 s", "Alarm", "Still nothing: a real alarm with your phone’s alarm sound."],
            ["Yes", "Next round", "One tap or one shake: everything stops and the full interval starts again."],
        ],
        "features_h2": "Start, confirm, schedule, check",
        "features": [
            {"kicker": "Start", "h2": "Two decisions, one button",
             "body": ["Unlimited or Timer, and how often you want to be asked. Turn the dial – from one minute up to twelve hours, 30 minutes to start with. The app remembers your last choice.",
                      "The timer runs for a set time (“for 2 hours”) or until a clock time (“until 5:30”)."],
             "shot": "en-home.webp"},
            {"kicker": "Confirm", "h2": "Tap, shake, flip – your choice",
             "body": ["The big **Yes** always works. In Settings you can add shaking the phone, flipping it face down and back, or a volume button – in any combination. Shake and flip also work with the screen off.",
                      "You don’t have to wait for the question: confirm whenever you like, and the interval starts over from that moment. The session notification has an **I am awake** button too."],
             "shot": "en-check.webp"},
            {"kicker": "Shifts", "h2": "Schedules that start on their own",
             "body": ["For nights that repeat: start and end time, optional weekdays, interval. The session starts by itself at the set time and ends at the end time.",
                      "Without a weekday it runs once, at the next start."],
             "shot": "en-schedules.webp"},
            {"kicker": "Reliability", "h2": "Knows what your phone allows",
             "body": ["Android phones can hold back alarms – battery saving, Do Not Disturb, missing permissions. The reliability check goes through every point in plain language and shows how to fix what is not right.",
                      "**Test alarm** lets you hear and feel the alarm for five seconds before the first real night."],
             "shot": "en-reliability.webp"},
        ],
        "limits_h2": "Honest limits",
        "limits": "Stay Awake helps you stay awake. It does not replace sleep or breaks, and it is not a safety system for work or driving. Whether a check arrives on time also depends on the phone – the reliability check shows what yours allows.",
        "nots_h2": "Nothing to sign up for",
        "nots": [
            "**No account, no login.** Sessions, schedules and settings stay on your phone.",
            "**Works offline.** Checks and the alarm need no internet connection.",
            "**Sessions survive a restart** of the phone.",
            "**Free with a small banner.** No ads on the check or the alarm. Stay Awake Pro removes the banner – monthly or as a one-time purchase.",
            "**20 languages**, from Arabic to Vietnamese.",
        ],
        "privacy_link": "Read the privacy policy",
        "guides_h2": "Guides for long nights",
        "guides_lead": "Useful without the app: night shifts, study nights, staying up without coffee, interval alarms.",
        "faq": [
            ["How is this different from a normal alarm clock?",
             ["An alarm clock rings at a time, whether you are awake or not. Stay Awake asks first and only gets loud if you do not answer. It is built for staying awake, not for waking up in the morning."]],
            ["Do I have to keep the screen on?",
             ["No. Put the phone down, lock it, let the screen go dark. The check appears over the lock screen. If you chose shaking, a shake confirms even with the screen off."]],
            ["Which alarm sound does it use?",
             ["By default your phone’s own alarm sound – the one you are used to waking up to. In Settings you can switch to the Stay Awake melody or pick another sound."]],
            ["Does it work without internet?",
             ["Yes. Checks, vibration and the alarm run entirely on the phone."]],
            ["What does it cost?",
             ["Everything that keeps you awake is free. The free version shows a small banner on normal screens, never on the check or the alarm. Stay Awake Pro removes it, monthly or once; the price is shown in Google Play."]],
            ["Is there an iPhone version?",
             ["No, Stay Awake is only available for Android."]],
        ],
        "final_h2": "If you have to stay awake, this is your app.",
        "final_body": "Start a session, put the phone down. Stay Awake keeps asking until you end the session.",
    },

    "guides_index": {
        "title": "Guides: staying awake at night, on shift and while studying",
        "desc": "Practical guides for long nights: night shifts, studying late, staying up without caffeine, an alarm every 30 minutes and alarms that do not go off on Android.",
        "h1": "Guides for long nights",
        "lead": "Short, practical answers – each one useful with or without an app.",
        "app": "**Stay Awake** asks at your interval whether you are still awake and sounds an alarm if no answer comes.",
    },

    # ------------------------------------------------------------ Guides
    "guides": [
        {
            "id": "nightshift",
            "slug": "how-to-stay-awake-on-night-shift",
            "title": "How to stay awake on a night shift: 9 practical tips",
            "desc": "Staying alert through a night shift: light, movement, small tasks for the dead hours around 3 a.m., food and a check-in rhythm. Practical, no gimmicks.",
            "h1": "How to stay awake on a night shift",
            "teaser": "Light, movement and a plan for the dead hours around 3 a.m.",
            "answer": "The hard part of a night shift is rarely the start – it is the quiet stretch in the small hours when nothing happens. What helps most is **light, movement and a rhythm**: break the night into short blocks, give each block something to do, and do not sit still in dim light for long.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["dead-hours", "Plan for the dead hours", [
                    "Most people who work nights know the moment: somewhere between 2 and 5 a.m. it gets quiet, the coffee has worn off and your eyes get heavy. Do not leave this stretch to chance.",
                    {"list": [
                        "**Save active tasks for it.** Restocking, filing, rounds, checking equipment – anything that makes you stand up and walk.",
                        "**Split the night into blocks** of 30 to 60 minutes. A block ends with a small action: stand up, drink water, write a line in the log.",
                        "**Avoid long passive stretches** like reading or watching a screen while sitting deep in a chair.",
                    ]},
                ]],
                ["tips", "9 tips that work for many people", [
                    {"steps": [
                        "**Keep the room bright.** Dim light makes you drowsy. Switch on the main light instead of a single lamp, where your workplace allows it.",
                        "**Move every half hour.** A walk down the corridor, a few stairs, stretching – a few minutes are enough.",
                        "**Stand up for routine work.** Sitting makes nodding off easy.",
                        "**Drink water regularly.** It gives you a reason to get up as well.",
                        "**Eat small portions.** Many people feel sluggish after a big meal in the middle of the night; a few small snacks are easier.",
                        "**Use cold water.** Splash it on your face or hands when the heaviness comes.",
                        "**Talk to someone.** A short conversation with a colleague breaks up the quiet stretch – for both of you.",
                        "**Fresh air.** A few minutes at an open window or outside.",
                        "**Check in at fixed times.** A regular reminder – every 20 or 30 minutes – that asks for a deliberate response helps you notice when minutes start quietly turning into an hour.",
                    ]},
                ]],
                ["before", "Before and after the shift", [
                    "A night shift starts earlier than the clock says: if you arrive already tired, no tip will carry you through. Plan your sleep before the first night and protect it after the shift – dark room, phone on silent, the people you live with in the loop.",
                    {"note": "If you notice you keep nodding off, that is a signal to take seriously. Talk to your team or your employer – no app and no tip replaces sleep."},
                ]],
            ],
            "app": {
                "h2": "A check-in every 30 minutes",
                "body": [
                    "Stay Awake turns tip 9 into a routine: it asks at your interval whether you are still awake. Shake the phone or tap Yes and the next round starts. If you do not answer, it vibrates after 10 seconds and sounds an alarm after 20.",
                    "For repeating shifts, set up a **schedule** – for example 10 p.m. to 6 a.m., Monday to Friday. The session then starts and ends on its own.",
                ],
                "shot": "en-schedules.webp",
                "alt": "Schedule 10:00 PM – 6:00 AM, Monday to Friday, every 30 minutes.",
            },
            "faq": [
                ["When is it hardest to stay awake on a night shift?",
                 ["For many people in the early morning hours, roughly between 2 and 5 a.m. Plan active tasks for that stretch."]],
                ["Does coffee help on a night shift?",
                 ["Many people drink coffee at the start of a shift. It does not replace light, movement and a rhythm – and how much is right for you is not something a website can tell you."]],
                ["How do I stay awake on a quiet night when there is nothing to do?",
                 ["Give yourself small fixed tasks every 30 to 60 minutes, stand up regularly and keep the room bright. A regular check-in reminder helps you notice when you start drifting."]],
            ],
        },
        {
            "id": "study",
            "slug": "how-to-stay-awake-while-studying",
            "title": "How to stay awake while studying at night",
            "desc": "Studying late without nodding off over your notes: work in short blocks, study actively, keep the room bright and use a check-in timer.",
            "h1": "How to stay awake while studying at night",
            "teaser": "Short blocks, active studying and a timer that checks on you.",
            "answer": "Reading is the fastest way to fall asleep over your notes. You stay awake longer when you **study actively in short blocks**: write, explain, test yourself – and get up between blocks.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["active", "Study actively, not passively", [
                    "Your eyes can keep moving over a page while your mind has long switched off. Active methods keep you busy:",
                    {"list": [
                        "**Test yourself** instead of rereading: cover the page, write down what you remember, then check.",
                        "**Explain it out loud**, as if to someone else.",
                        "**Write by hand** – summaries, mind maps, flash cards.",
                        "**Work through exercises** instead of reading the solutions.",
                    ]},
                ]],
                ["blocks", "Work in blocks", [
                    "Set a fixed rhythm, for example 25 to 50 minutes of work and five minutes off. In the break, stand up: walk, stretch, get water, open the window. Do not spend the break lying on the bed – that is how a five-minute break becomes a two-hour nap.",
                    {"table": [
                        ["Time", "Block"],
                        ["22:00 – 22:45", "Exercises chapter 4"],
                        ["22:45 – 22:50", "Stand up, water, window open"],
                        ["22:50 – 23:35", "Flash cards chapter 4, test yourself"],
                        ["23:35 – 23:40", "Short walk through the flat"],
                    ]},
                ]],
                ["room", "Set up the room", [
                    {"list": [
                        "**Bright light** on the desk and in the room, not just a reading lamp.",
                        "**Sit at a desk**, not on the bed or sofa.",
                        "**Cool rather than warm** – a stuffy room makes you drowsy.",
                        "**Phone out of reach**, except as a timer.",
                    ]},
                ]],
                ["limits", "When it is time to stop", [
                    "When you read the same paragraph for the third time, the night has usually paid off as much as it will. What you study while half asleep rarely sticks. Sometimes the better plan is to sleep and start early.",
                ]],
            ],
            "app": {
                "h2": "A timer that checks on you",
                "body": [
                    "A normal timer rings when the block is over – even if you fell asleep over your notes ten minutes earlier. Stay Awake asks at your interval whether you are still awake. Shake the phone or tap Yes and you keep going. No answer: vibration after 10 seconds, alarm after 20.",
                    "Use the **Timer** mode to say how long the session runs, for example “for 3 hours” or “until 1:00”.",
                ],
                "shot": "en-timer.webp",
                "alt": "Timer mode: For 2:00 h, check interval 30 minutes, Start session.",
            },
            "faq": [
                ["How long should a study block be at night?",
                 ["Many people work well with 25 to 50 minutes and a short break. Try what suits you – what matters is that the break includes standing up."]],
                ["Is it better to study late or get up early?",
                 ["That depends on you. If you notice that nothing sticks any more, going to bed and studying in the morning is often more productive."]],
                ["How do I stop falling asleep while reading?",
                 ["Turn reading into an active task: take notes, ask yourself questions, explain the content out loud. And sit at a desk in bright light."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "how-to-stay-awake-all-night",
            "title": "How to stay awake all night – a plan hour by hour",
            "desc": "When you have to stay up all night: a plan for evening, midnight, the dead hours and the morning, plus how to make sure you notice if you nod off.",
            "h1": "How to stay awake all night",
            "teaser": "A plan for evening, midnight, the dead hours and the morning.",
            "answer": "A whole night works better with a plan than with willpower. Start the night rested, keep it **bright and active**, give the hours after 2 a.m. the most active tasks – and set up something that **checks on you** regularly and gets loud if no answer comes.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["plan", "A plan for the night", [
                    {"table": [
                        ["When", "What helps"],
                        ["Evening", "Start rested if you can. Eat a normal meal, not a heavy one late at night."],
                        ["Until midnight", "Do the work that needs the clearest head now."],
                        ["Midnight to 2 a.m.", "Work in blocks; stand up and move between them."],
                        ["2 to 5 a.m.", "The hardest stretch for many people: active tasks, bright light, fresh air."],
                        ["Morning", "Daylight helps many people over the last stretch. Do nothing that needs full concentration."],
                    ]},
                ]],
                ["tricks", "What keeps you going", [
                    {"list": [
                        "**Light:** main light on, screen bright enough.",
                        "**Movement:** a few minutes every half hour.",
                        "**Cold water** on face and hands.",
                        "**Something to do with your hands** instead of passive watching.",
                        "**Company:** a call or a chat with someone who is also up.",
                    ]},
                ]],
                ["notice", "Notice when you nod off", [
                    "The danger in a long night is not one big collapse but the small moments: eyes closed “just for a minute”, and suddenly it is an hour later. You notice that only when something asks you from outside.",
                    "Without an app: a timer you restart every time it rings, or a friend who checks in by message. With an app: see below.",
                ]],
                ["after", "The day after", [
                    "A night without sleep catches up with you. Plan the next day lightly and catch up on sleep as soon as you can.",
                    {"note": "Whether staying up all night is a good idea for you is something only you – or a doctor – can judge. This guide is about getting through a night you have already decided on."},
                ]],
            ],
            "app": {
                "h2": "Someone who asks every 30 minutes",
                "body": [
                    "Stay Awake asks at your interval whether you are still awake. One shake or one tap and the next round begins. If the answer does not come, the phone vibrates after 10 seconds and an alarm sounds after 20 – with your phone’s own alarm sound.",
                    "Start an **unlimited** session for a night with an open end, or a **timer** “until 6:00”.",
                ],
                "shot": "en-alarm.webp",
                "alt": "Check after 20 seconds: Check missed, Are you still awake?, a large Yes button.",
            },
            "faq": [
                ["What time is it hardest to stay awake?",
                 ["Many people find the stretch between about 2 and 5 a.m. the hardest. Keep the most active tasks for then."]],
                ["Does a short nap help?",
                 ["Some people plan a short nap. The risk is sleeping far longer than planned – if you do it, set an alarm you cannot ignore."]],
                ["How do I make sure I wake up if I nod off?",
                 ["Use something that checks on you regularly and gets loud when you do not respond – a friend, a repeating timer or a wake-check app."]],
            ],
        },
        {
            "id": "nocaffeine",
            "slug": "how-to-stay-awake-without-caffeine",
            "title": "How to stay awake without caffeine: 10 ways",
            "desc": "Staying awake without coffee or energy drinks: light, cold, movement, posture, conversation, chewing and a check-in rhythm. Simple ways you can try tonight.",
            "h1": "How to stay awake without caffeine",
            "teaser": "Light, cold, movement and rhythm instead of coffee.",
            "answer": "Without caffeine you have to use other signals: **bright light, cool air, movement and something to do.** None of it works miracles, and each signal only lasts a short while – so what counts in the end is the **rhythm** in which you repeat them.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["ten", "10 ways to try", [
                    {"steps": [
                        "**Bright light.** Main light on; in the morning go into daylight.",
                        "**Cool air.** Open the window, turn the heating down a little.",
                        "**Cold water** on your face, wrists and neck.",
                        "**Stand up.** Work standing for a while, at a counter or shelf.",
                        "**Move briefly.** Stairs, a walk round the block, a few squats.",
                        "**Sit upright**, feet on the floor – not curled up on the sofa.",
                        "**Chew something**: gum, an apple, raw vegetables.",
                        "**Talk.** A call, a conversation, explaining something out loud.",
                        "**Music with a beat**, if your surroundings allow it.",
                        "**Change tasks** when one starts to make you drowsy.",
                    ]},
                ]],
                ["rhythm", "Rhythm beats willpower", [
                    "Each of these works for a few minutes. What carries you through hours is a rhythm: every 20 to 30 minutes a small action that interrupts the drift. Set it from outside – a timer, an appointment, a reminder – because the drowsier you are, the less you notice the time.",
                ]],
                ["honest", "Honestly", [
                    "Nothing replaces sleep. If you are so tired that none of this helps, your body is telling you something – and the best decision may be to sleep.",
                ]],
            ],
            "app": {
                "h2": "A reminder that wants an answer",
                "body": [
                    "Stay Awake gives you the rhythm without coffee: at your interval it asks whether you are still awake. Shaking the phone is enough as an answer – and it moves you a little, too. No answer: vibration after 10 seconds, alarm after 20.",
                ],
                "shot": "en-check.webp",
                "alt": "Check screen: Are you still awake?, or shake the phone, large Yes button.",
            },
            "faq": [
                ["What is the quickest way to wake up without coffee?",
                 ["For many people: stand up, cold water on the face, a few minutes of fresh air or movement."]],
                ["Do energy drinks count as caffeine-free?",
                 ["No, most energy drinks contain caffeine. Check the label."]],
                ["Why do I get tired again after a few minutes?",
                 ["Most of these tricks work only briefly. That is why a regular rhythm of small interruptions helps more than one big effort."]],
            ],
        },
        {
            "id": "every30",
            "slug": "alarm-every-30-minutes-android",
            "title": "How to set an alarm every 30 minutes on Android",
            "desc": "Android’s clock app has no “every 30 minutes” option. Three ways that work: several alarms, a timer you restart, or an interval alarm app.",
            "h1": "How to set an alarm every 30 minutes on Android",
            "teaser": "Several alarms, a restarted timer or an interval alarm – three ways.",
            "answer": "The clock apps on most Android phones repeat an alarm only **by weekday**, not every X minutes. You have three options: **create several alarms**, **restart a timer** each time, or use an **interval alarm app**.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["several", "Option 1: several alarms", [
                    "Create one alarm for every half hour in the clock app. For one evening that is fine; for a whole night it gets long:",
                    {"table": [
                        ["Period", "Interval", "Alarms needed"],
                        ["2 hours", "30 min", "4"],
                        ["8 hours (22:00–06:00)", "30 min", "16"],
                        ["8 hours", "15 min", "32"],
                    ]},
                    "Downsides: lots of tapping, and the alarms keep ringing at fixed times even if you are wide awake. Afterwards you have to switch them all off again.",
                ]],
                ["timer", "Option 2: restart a timer", [
                    {"steps": [
                        "Open the clock app and go to **Timer**.",
                        "Set **30:00** and start.",
                        "When it rings, stop it and start it again.",
                    ]},
                    "Simple, but you have to restart it every time. If you forget once, nothing happens for the rest of the night.",
                ]],
                ["app", "Option 3: an interval alarm app", [
                    "Interval alarm apps repeat on their own. Before you choose one, check three things:",
                    {"list": [
                        "**Does it ring with the screen off and the phone locked?** Many apps only work in the foreground.",
                        "**Does it use exact alarms?** Otherwise Android may delay it in power saving mode.",
                        "**What happens when you do not react?** A simple repeating alarm rings for a while and then stops.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "An interval alarm that asks first",
                "body": [
                    "Stay Awake repeats at your interval – any value from one minute to twelve hours – and uses exact alarms. It does not ring straight away: first it asks quietly whether you are still awake. Answer, and the interval starts over from that moment. No answer: vibration after 10 seconds, alarm after 20.",
                    "So you are not woken up when you are awake – and you are not left alone when you are not.",
                ],
                "shot": "en-home.webp",
                "alt": "Dial set to 30 minutes, Unlimited or Timer, Start session.",
            },
            "faq": [
                ["Can the Android clock app repeat an alarm every 30 minutes?",
                 ["The clock apps on most Android phones repeat alarms by weekday only. For every 30 minutes you need several alarms, a timer or a separate app."]],
                ["Why doesn’t my interval alarm ring when the screen is off?",
                 ["Often battery optimisation or a missing permission for exact alarms is the cause. See [Android alarm not going off](/guides/android-alarm-not-going-off/)."]],
                ["Can I set an interval of 15 or 45 minutes?",
                 ["In Stay Awake, yes: the dial goes from one minute to twelve hours. Other intervals without an app: [interval alarm on Android](/guides/interval-alarm-android/)."]],
            ],
        },
        {
            "id": "wakecheck",
            "slug": "alarm-that-checks-if-you-are-awake",
            "title": "An alarm that checks if you are still awake – how it works",
            "desc": "A wake check asks at an interval whether you are still awake and only sounds an alarm if you do not answer. How it differs from a normal alarm, and when it helps.",
            "h1": "An alarm that checks if you are still awake",
            "teaser": "Ask first, get loud only if needed – the idea behind a wake check.",
            "answer": "A normal alarm rings at a fixed time. A **wake check** asks at an interval whether you are still awake – and only gets loud if you do not answer. You confirm with a tap or a movement, and the next interval begins.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["difference", "Alarm clock, repeating alarm, wake check", [
                    {"table": [
                        ["", "Alarm clock", "Repeating alarm", "Wake check"],
                        ["Rings when", "At a fixed time", "Every X minutes", "Only without an answer"],
                        ["When you are awake", "Rings anyway", "Rings anyway", "Quiet question, one tap"],
                        ["When you have nodded off", "Rings once", "Rings, then stops", "Vibration, then alarm"],
                        ["Made for", "Waking up", "Reminders", "Staying awake"],
                    ]},
                ]],
                ["when", "When a wake check helps", [
                    {"list": [
                        "**Night shifts and standby** with long quiet stretches.",
                        "**Study nights** before an exam.",
                        "**Waiting through the night**, for example for an early departure or a call.",
                        "**Watching over something** – a process, a download, a sick pet.",
                    ]},
                    "In all these cases the risk is the same: you do not notice yourself drifting off. A wake check asks from outside – and gets loud when the answer does not come.",
                ]],
                ["diy", "Without an app", [
                    "You can build a simple version yourself: ask someone who is also awake to message you every 30 minutes and call if you do not answer. That works – as long as the other person stays awake.",
                ]],
                ["what-not", "What a wake check is not", [
                    "It does not measure how tired you are, does not detect sleep and does not replace rest. It asks – the answer comes from you.",
                ]],
            ],
            "app": {
                "h2": "Stay Awake is a wake check",
                "body": [
                    {"steps": [
                        "**0 seconds:** the screen asks “Are you still awake?” – over the lock screen too.",
                        "**10 seconds:** vibration.",
                        "**20 seconds:** alarm with your phone’s alarm sound.",
                    ]},
                    "Confirm with the big Yes button or – if you enable it in Settings – by shaking, flipping the phone or a volume button. Then the full interval starts again.",
                ],
                "shot": "en-check.webp",
                "alt": "Check screen: Are you still awake?, or shake the phone, large Yes button, End session.",
            },
            "faq": [
                ["Does a wake check app detect when I fall asleep?",
                 ["No. Stay Awake does not use the camera or the microphone and measures nothing about you. It asks, and gets loud if no answer comes."]],
                ["What if I confirm by accident?",
                 ["A single jolt does not count as a shake – it takes a deliberate shake with at least two movements. You can also adjust the shake sensitivity in Settings."]],
                ["Can I confirm before the question comes?",
                 ["Yes. In Stay Awake you can confirm at any time; the interval then starts over from that moment."]],
            ],
        },
        {
            "id": "notringing",
            "slug": "android-alarm-not-going-off",
            "title": "Android alarm not going off? 7 causes and fixes",
            "desc": "Alarm silent or late on Android: alarm volume, Do Not Disturb, battery optimisation, exact alarms, notifications and full-screen permission. How to check each.",
            "h1": "Android alarm not going off? 7 causes and fixes",
            "teaser": "Volume, Do Not Disturb, battery saving, permissions – what to check.",
            "answer": "If an alarm on Android stays silent or comes late, it is usually one of seven settings: **alarm volume, Do Not Disturb, battery optimisation, exact alarms, notifications, full-screen permission** – or the phone was off. Check them one by one and then set a test alarm two minutes ahead.",
            "updated": "2026-11-21",
            "updated_label": "21 November 2026",
            "sections": [
                ["causes", "7 causes", [
                    {"steps": [
                        "**Alarm volume at zero.** Android has a separate volume for alarms. Press a volume button, open the volume panel and check the alarm slider.",
                        "**Do Not Disturb blocks alarms.** Alarms are usually allowed in Do Not Disturb, but this can be switched off. Look in *Settings → Sound → Do Not Disturb* (names vary by manufacturer).",
                        "**Battery optimisation stops the app.** Some manufacturers put apps to sleep aggressively. In the app info under *Battery*, allow unrestricted use.",
                        "**No permission for exact alarms.** Since Android 12, other apps need the special access “Alarms & reminders” to ring on time. Without it, Android may delay the alarm.",
                        "**Notifications switched off.** Since Android 13, apps must ask for permission to send notifications; many alarm apps show their alarm through one.",
                        "**Full-screen permission missing.** On Android 14 and later, an app may need permission to show itself full screen over the lock screen.",
                        "**Phone switched off.** Most Android phones do not ring when they are switched off.",
                    ]},
                ]],
                ["test", "Test it properly", [
                    {"steps": [
                        "Set an alarm for two minutes from now.",
                        "Lock the phone and put it down.",
                        "Wait – do not touch it.",
                    ]},
                    "If it rings, the basic setup is fine. If you need the alarm at night, test once with the phone on the charger as you would use it then.",
                ]],
                ["manufacturer", "Phones with strict battery saving", [
                    "Some manufacturers have their own lists of apps that may run in the background or start automatically. If an alarm app keeps being late, look in the battery or app launch settings for an entry for that app and allow it everything.",
                ]],
            ],
            "app": {
                "h2": "Stay Awake checks this for you",
                "body": [
                    "The **reliability check** in Stay Awake goes through these points – notifications, check and alarm alerts, on-time wake-ups, over the lock screen, alarm volume, Do Not Disturb, vibration, background and battery – and shows how to fix what is not right.",
                    "With **Test alarm** you hear and feel the alarm for five seconds before you rely on it.",
                ],
                "shot": "en-reliability.webp",
                "alt": "Reliability check: Ready, all nine items green.",
            },
            "faq": [
                ["Why does my alarm ring late?",
                 ["Usually because of battery optimisation or because the app is not allowed to use exact alarms. Android then bundles the alarm with other wake-ups."]],
                ["Does an alarm ring when the phone is on silent?",
                 ["On most Android phones alarms ring even in silent mode, as long as the alarm volume is not at zero and Do Not Disturb allows alarms."]],
                ["Does my alarm ring when the phone is off?",
                 ["On most Android phones, no. Leave the phone on and charging."]],
            ],
        },
    ],
}

# Neu 24.11.2026 (SEO-Fahrplan). Suchvorschlaege (Google, 23./24.11.): "interval alarm android",
# "repeating alarm android/app", "alarm every 10/15 minutes android", "alarm every hour android",
# "set alarm every hour android", "hourly alarm android" -> interval page. "how to stay awake after
# alarm goes off", "how to not fall asleep after turning off alarm", "why do i keep falling asleep
# after my alarm" -> after-alarm page. App rule: Stay Awake is made for staying awake, not for
# waking up - the page says so.
#
# Abgrenzung (Lektorat 24.11.2026), damit sich die Seiten nicht gegenseitig die Suchanfragen nehmen:
# - interval-alarm-android = Ueberblick NACH INTERVALL: welcher Weg zu welchem Intervall passt,
#   Schritt fuer Schritt "jede Stunde", kurze Intervalle, Schlummern, Auswahl einer App.
# - alarm-every-30-minutes-android = Schritt-fuer-Schritt fuer genau dieses eine Intervall
#   (drei Wege). Die drei Wege hier nicht noch einmal ausbreiten, nur verlinken.
# - alarm-that-checks-if-you-are-awake = das Prinzip Wach-Check. Hier nur verlinken.
# Die Tabelle "Reminder / Interval timer / Interval alarm" darf der Tabelle auf der Wach-Check-Seite
# nicht widersprechen (dort: ein einfacher Wiederholungswecker klingelt und hoert dann auf).
C["guides"] += [
    {
        "id": "interval",
        "slug": "interval-alarm-android",
        "title": "Interval alarm on Android: every 10 or 15 minutes, or every hour",
        "desc": "Interval alarm on Android: an alarm every hour with the clock app, every 10 or 15 minutes with a timer or an app – and why snooze is not the same thing.",
        "h1": "Interval alarm on Android: every 10 or 15 minutes, or every hour",
        "teaser": "Every hour with the clock app, shorter intervals with a timer or an app.",
        "answer": "An **interval alarm** (or repeating alarm) rings every few minutes or every hour instead of once at a set time. The clock apps on most Android phones have no setting for that – they repeat by **weekday**. Which workaround fits depends on the interval: for **every hour or longer**, a handful of single alarms does the job; for **every 10 or 15 minutes** you need a timer you restart or an **interval alarm app**.",
        "updated": "2026-11-24",
        "updated_label": "24 November 2026",
        "sections": [
            ["which", "Which way fits which interval", [
                "Without an app you need one alarm per ring. Counted for eight hours:",
                {"table": [
                    ["Interval", "Alarms for 8 hours", "With the clock app alone"],
                    ["10 minutes", "48", "Too many – timer or app"],
                    ["15 minutes", "32", "Too many – timer or app"],
                    ["20 minutes", "24", "Too many – timer or app"],
                    ["30 minutes", "16", "Possible, but tedious"],
                    ["Every hour", "8", "Works well"],
                    ["Every 2 hours", "4", "Works well"],
                ]},
                "For exactly 30 minutes there is a separate step-by-step guide: [alarm every 30 minutes on Android](/guides/alarm-every-30-minutes-android/).",
            ]],
            ["hourly", "How to set an alarm every hour", [
                {"steps": [
                    "Open the clock app and go to **Alarm**.",
                    "Add an alarm for the first hour you need, for example 10 p.m.",
                    "Add one more for each following hour – 11 p.m., midnight and so on.",
                    "If it should come back on certain days, pick the same **weekdays** for all of them.",
                    "Give them a label such as “hourly”, if your clock app offers labels – that makes them easier to find later.",
                ]},
                "Two things to know: the alarms ring at fixed times whether you are awake or not, and afterwards you switch them off again one by one.",
                "Many digital watches and some smartwatches have an **hourly chime** – a short beep on the hour. That is a time signal, not an alarm: it does not wait for a reaction.",
            ]],
            ["short", "An alarm every 10 or 15 minutes", [
                "At these intervals single alarms are out – 32 or 48 of them for one night. That leaves two ways:",
                {"list": [
                    "**Restart a timer.** Set the clock app’s timer to 10:00 or 15:00 and start it again each time it rings. Enough for an hour or two while you are busy anyway; miss one restart and the series is over.",
                    "**An interval alarm app.** It repeats by itself. What to look for is further down.",
                ]},
            ]],
            ["snooze", "Is snooze an interval alarm?", [
                "Snooze repeats an alarm after a few minutes. On some phones you can set the snooze interval and the number of repeats – on Samsung phones, for example, right in each alarm. It still is not an interval alarm: snooze belongs to one single alarm and is meant for getting up. As soon as you dismiss the alarm, the series is over.",
            ]],
            ["kinds", "Reminder, interval timer or interval alarm?", [
                {"table": [
                    ["", "Repeating reminder", "Interval timer", "Interval alarm"],
                    ["Signal", "Notification, often with a short sound", "Sound at the end of each round", "Rings like an alarm"],
                    ["Locked screen", "Shows as a notification", "Depends on the app", "Should show over the lock screen"],
                    ["Next round", "At fixed times", "Right away, by itself", "By itself – at fixed times or from your reaction, depending on the app"],
                    ["Typical use", "Drink water, stretch", "Workouts, focus blocks", "Recurring things you don’t want to miss"],
                ]},
                "If missing a ring would matter, pick an alarm, not a reminder: a notification is easy to overlook. And if the point is to stay awake, there is a fourth kind – a wake check, which asks first and only rings when no answer comes: [an alarm that checks if you are still awake](/guides/alarm-that-checks-if-you-are-awake/).",
            ]],
            ["check", "What to look for in an interval alarm app", [
                {"list": [
                    "**Can you set any interval** – or only fixed steps such as 15, 30 and 60 minutes?",
                    "**Does the next interval start at fixed times or from your reaction?** From your reaction means you get the full time again after every ring.",
                    "**Does it end by itself** – after a set duration, at a clock time or by schedule – so it doesn’t ring on into the next day?",
                    "**Does it still ring with the screen off and the phone locked?** That takes exact alarms and the right permissions; how to check them is in [Android alarm not going off](/guides/android-alarm-not-going-off/).",
                ]},
            ]],
        ],
        "app": {
            "h2": "Stay Awake: any interval from 1 minute to 12 hours",
            "body": [
                "Stay Awake is an interval app made for staying awake. You set the interval with a dial – any value from one minute to twelve hours – and it uses exact alarms. It does not ring straight away: each round starts with a quiet question on the screen, “Are you still awake?”. One tap and the next interval starts from that moment. No answer: vibration after 10 seconds, alarm after 20.",
                "Three ways to run it: **Unlimited** until you end it, as a **Timer** for a set time (“for 2 hours”) or until a clock time (“until 6:00”), or as a **schedule** that starts by itself on the weekdays you choose.",
                "If all you want is a short beep every hour that needs no answer, a reminder app or an hourly chime is the better fit.",
            ],
            "shot": "en-timer.webp",
            "alt": "Timer mode: for 2:00 h, check interval 30 minutes.",
        },
        "faq": [
            ["Can Android set an alarm every hour?",
             ["Not with a single alarm: the clock apps on most Android phones repeat by weekday only. Create one alarm per hour – eight for an eight-hour night – or use an interval alarm app."]],
            ["How do I set an alarm every 10 or 15 minutes on Android?",
             ["Single alarms make no sense at that pace (32 to 48 for eight hours). Restart the clock app’s timer each time it rings, or use an interval alarm app that repeats by itself."]],
            ["Is snooze the same as an interval alarm?",
             ["No. Snooze repeats one single alarm for a while and ends as soon as you dismiss it. An interval alarm keeps its rhythm until the end you set."]],
            ["Which interval makes sense for staying awake?",
             ["That depends on how quickly you drift off. Stay Awake starts with 30 minutes; if that feels too long, go shorter. Any value from one minute to twelve hours works."]],
        ],
    },
    {
        "id": "afteralarm",
        "slug": "how-to-stay-awake-after-alarm",
        "title": "How to stay awake after your alarm goes off (and not fall back asleep)",
        "desc": "Why you fall back asleep after turning off the alarm, and how to stay up: alarm out of reach, light, a fixed first step and a second check minutes later.",
        "h1": "How to stay awake after your alarm goes off",
        "teaser": "Why the alarm is not enough, and how to get past the first ten minutes.",
        "answer": "Falling back asleep after the alarm is rarely about the alarm being too quiet. More often you turn it off **half asleep, lie back down** – and nothing comes after it. What helps is making the first ten minutes hard to sleep through: put the alarm **out of reach** so you have to stand up, switch on **bright light**, have a **fixed first step** ready – and let something **ask again a few minutes later** whether you are really up.",
        "updated": "2026-11-24",
        "updated_label": "24 November 2026",
        "sections": [
            ["why", "Why it happens", [
                "Turning off an alarm takes one hand and no thought. If the phone is next to your pillow, you can do it without opening your eyes properly – and then nothing follows. For many people snoozing does not help either: every snooze is another chance to doze off for real.",
                "An alarm is built to wake you once. Staying up afterwards is a different job – and nobody checks whether you actually got out of bed.",
            ]],
            ["tips", "Ways that work for many people", [
                {"steps": [
                    "**Alarm out of reach.** Put the phone on the other side of the room. Once you are standing, lying back down takes a decision.",
                    "**Light straight away.** Switch on the main light or open the curtains before you do anything else.",
                    "**A fixed first step.** The same thing every morning: glass of water, bathroom, kettle on. The less you have to decide, the less you negotiate with yourself.",
                    "**No lying down “for a minute”.** Sitting back down on the edge of the bed is how many people end up asleep again.",
                    "**One alarm, not five.** If you want a backup, set one a few minutes later – not a chain of snoozes.",
                    "**A second check.** Something that asks again after five or ten minutes whether you are still up, and gets loud if no answer comes.",
                ]},
            ]],
            ["plan", "A plan for the first ten minutes", [
                {"table": [
                    ["When", "What you do"],
                    ["Alarm rings", "Stand up to turn it off – it is on the other side of the room."],
                    ["Minute 1", "Main light on or curtains open."],
                    ["Minutes 2 to 5", "Your fixed first step: glass of water, bathroom, kettle on."],
                    ["Minutes 5 to 10", "The second check asks whether you are still up."],
                ]},
            ]],
            ["second", "The second check", [
                "A second alarm at a fixed time rings whether you are up or not – in the shower, at breakfast – and it is just as easy to turn off half asleep as the first one. A check that **asks first** is different: if you are up, one tap and it stays quiet; if you have dozed off again and do not answer, it gets loud.",
                "Without an app: ask someone who is up at that time to message you a few minutes after your alarm, and to call if you do not answer.",
                {"note": "No trick and no app replaces sleep. If you are short on sleep night after night, getting up stays hard whatever you set up."},
            ]],
        ],
        "app": {
            "h2": "Stay Awake as the second check",
            "body": [
                "Stay Awake is not an alarm clock – it is made for staying awake, not for waking up, and it cannot get you out of bed. What it can do is ask in the minutes after your alarm.",
                "Set up a **schedule** that starts by itself: if your alarm rings at 6:30, for example from 6:35 to 7:05 on your workdays, with a five-minute interval. Or start a **Timer** session for half an hour by hand once you are up.",
                "Five minutes after the session starts, and every five minutes from your last answer, the screen asks whether you are still awake. One tap and the next round starts; no answer, and the phone vibrates after 10 seconds and sounds an alarm after 20. At the end time the session ends by itself.",
            ],
            "shot": "en-check.webp",
            "alt": "Check screen: Are you still awake?, or shake the phone, large Yes button, End session.",
        },
        "faq": [
            ["Why do I keep falling asleep after my alarm?",
             ["Often because turning it off is too easy: the phone is within reach, the room is dark, and nothing happens afterwards. Moving the alarm away and adding a second check a few minutes later breaks that pattern for many people."]],
            ["How do I not fall asleep after turning off my alarm?",
             ["Stand up before you turn it off, switch on bright light, and do the same first step every morning. A check a few minutes later asks again – and gets loud if you do not answer."]],
            ["Is snoozing bad?",
             ["For many people snoozing just means several short dozes instead of getting up. If you want a backup, one second alarm or one check a few minutes later is simpler than a chain of snoozes."]],
            ["Can Stay Awake replace my alarm clock?",
             ["No. Stay Awake is made for staying awake, not for waking up. Keep your alarm clock and let Stay Awake ask in the minutes after it."]],
        ],
    },
]
