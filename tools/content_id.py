"""Teks bahasa Indonesia (pilot 24.11.2026). Fakta hanya dari aplikasi (lihat docstring build.py).

Pencarian (saran Google, 24.11.2026): "alarm setiap 30 menit", "cara agar tidak ngantuk" (+ saat
kerja malam, saat belajar, saat malam), "cara begadang" (+ sampai pagi, tanpa kopi, agar tidak
ngantuk).

Nama di aplikasi seperti di app/src/main/res/values-in: Tanpa batas, Timer, Mulai sesi,
Masih terjaga?, Akhiri sesi, Jadwal, Keandalan, Uji alarm. Sapaan "Anda" seperti di Google Play.
Tangkapan layar menampilkan aplikasi berbahasa Inggris.
Dilarang: mengemudi (kecuali kalimat batasan, disalin persis dari halaman Google Play), janji
keselamatan kerja, "mencegah tertidur", nasihat medis.
"""

APP = "Stay Awake"
NOTE_EN = " (tangkapan layar aplikasi berbahasa Inggris)"

C = {
    "app_name": APP,
    "lang_name": "Bahasa Indonesia",
    "og_locale": "id_ID",
    "ui": {
        "skip": "Langsung ke konten",
        "nav": "Navigasi utama",
        "guides": "Panduan",
        "privacy": "Privasi",
        "imprint": "Informasi hukum",
        "faq": "Tanya jawab",
        "toc": "Di halaman ini",
        "crumbs": "Jejak navigasi",
        "updated": "Diperbarui:",
        "with_app": "Dengan aplikasi",
        "more_guides": "Panduan lainnya",
        "play_cta": "Temukan di Google Play",
        "play_note": "Gratis untuk Android · tanpa akun",
        "moreapps": "Aplikasi lain dari Nice Developments",
        "footer_tag": "Alarm yang bertanya apakah Anda masih terjaga. Untuk Android.",
        "trademark": "Google Play dan Android adalah merek dagang Google LLC.",
    },

    "home": {
        "title": "Stay Awake – alarm yang terus bertanya apakah Anda masih terjaga",
        "desc": "Alarm berbunyi sekali, Anda mematikannya lalu tertidur lagi. Stay Awake terus bertanya apakah Anda masih terjaga – dan berbunyi sampai Anda menjawab.",
        "kicker": "Untuk siapa saja yang harus tetap terjaga",
        "h1": "Alarm berbunyi sekali. Stay Awake terus bertanya.",
        "lead": "Anda pasti pernah mengalaminya: alarm berbunyi, Anda mematikannya – dan lima menit kemudian Anda tertidur lagi. Stay Awake tidak berhenti setelah sekali berbunyi. Setiap 30 menit, atau pada interval pilihan Anda, aplikasi ini bertanya: **Masih terjaga?** Guncang ponsel atau ketuk Ya, dan putaran berikutnya dimulai. Tidak ada jawaban? Ponsel bergetar setelah 10 detik, dan setelah 20 detik alarm berbunyi – sampai Anda menjawab.",
        "who": "Shift malam · piket · belajar sampai larut · menunggu sepanjang malam",
        "why_h2": "Mengapa alarm biasa tidak cukup",
        "why_lead": "Alarm dibuat untuk membangunkan Anda sekali. Tetap terjaga berarti bertahan jam demi jam – dan bagian tersulitnya adalah saat tidak ada yang mengecek Anda.",
        "why": [["Alarm biasa", ["Berbunyi sekali – pada jam yang Anda atur sebelumnya.", "Dimatikan sambil setengah tidur, lalu tidak ada apa-apa lagi.", "Tidak pernah bertanya apakah Anda masih terjaga."]], ["Stay Awake", ["Bertanya lagi dan lagi, sepanjang malam – pada interval Anda, dari satu menit sampai dua belas jam.", "Bertanya dulu tanpa suara. Baru bergetar, lalu berbunyi, kalau Anda tidak menjawab.", "Alarm berbunyi sampai Anda menjawab. Lalu putaran berikutnya dimulai."]]],
        "hero_shot": "en-session.webp",
        "shots": {
            "en-session.webp": "Sesi berjalan: cincin kuning keemasan di sekeliling hitung mundur 29:50, di bawahnya “sampai cek berikutnya”, “Tanpa batas”, “Setiap 30 menit · Ketuk atau guncang”, tombol “Saya terjaga”, dan “Akhiri sesi”.",
            "en-home.webp": "Layar utama: Tanpa batas atau Timer, dial putar di 30 menit, dan tombol Mulai sesi" + NOTE_EN + ".",
            "en-check.webp": "Cek: “Masih terjaga?”, di bawahnya “atau guncang ponsel”, garis kemajuan tipis, tombol Ya besar, dan Akhiri sesi" + NOTE_EN + ".",
            "en-alarm.webp": "Setelah 20 detik tanpa jawaban: cek yang sama, kini dengan tulisan “Cek terlewat” dan garis merah; alarm sedang berbunyi" + NOTE_EN + ".",
            "en-schedules.webp": "Jadwal: 22.00–06.00, Senin sampai Jumat, setiap 30 menit, aktif" + NOTE_EN + ".",
            "en-reliability.webp": "Pemeriksaan keandalan: “Siap” dengan sembilan poin hijau, dari notifikasi sampai baterai" + NOTE_EN + ".",
            "en-timer.webp": "Mode Timer: selama 2:00 jam, cek setiap 30 menit" + NOTE_EN + ".",
            "en-settings.webp": "Setelan: mengetuk Ya selalu berfungsi; selain itu guncang ponsel, balik ponsel, atau tombol volume" + NOTE_EN + ".",
        },
        "steps_h2": "Apa yang terjadi saat waktunya cek",
        "steps_lead": "Pelan dulu, keras hanya kalau perlu. Setiap langkah berhenti begitu Anda menjawab.",
        "steps": [
            ["0 dtk", "Pertanyaan", "Layar menyala – juga di atas layar kunci – dan bertanya: Masih terjaga?"],
            ["10 dtk", "Getar", "Belum ada jawaban? Ponsel mulai bergetar."],
            ["20 dtk", "Alarm", "Masih belum ada jawaban: alarm sungguhan dengan suara alarm ponsel Anda."],
            ["Ya", "Putaran berikutnya", "Satu ketukan atau satu guncangan: semua berhenti dan interval penuh dimulai lagi."],
        ],
        "features_h2": "Mulai, konfirmasi, jadwalkan, periksa",
        "features": [
            {"kicker": "Mulai", "h2": "Dua pilihan, satu tombol",
             "body": ["**Tanpa batas** atau **Timer**, dan seberapa sering Anda ingin ditanya. Putar dialnya – dari satu menit sampai dua belas jam, awalnya 30 menit. Aplikasi mengingat pilihan terakhir Anda.",
                      "Timer berjalan selama waktu tertentu (“selama 2 jam”) atau sampai jam tertentu (“sampai 05.30”)."],
             "shot": "en-home.webp"},
            {"kicker": "Konfirmasi", "h2": "Ketuk, guncang, balik – terserah Anda",
             "body": ["Tombol **Ya** yang besar selalu berfungsi. Di setelan Anda bisa menambahkan guncang ponsel, balik ponsel, atau tombol volume, dalam kombinasi apa pun. Guncang dan balik juga berfungsi saat layar mati.",
                      "Anda tidak perlu menunggu pertanyaan: konfirmasi kapan saja, dan interval dimulai lagi dari saat itu."],
             "shot": "en-check.webp"},
            {"kicker": "Shift", "h2": "Jadwal yang mulai sendiri",
             "body": ["Untuk malam yang berulang: jam mulai dan selesai, hari opsional, interval. Sesi dimulai sendiri pada jam yang diatur dan berakhir pada jam selesai.",
                      "Tanpa hari yang dipilih, jadwal berjalan sekali, pada waktu mulai berikutnya."],
             "shot": "en-schedules.webp"},
            {"kicker": "Keandalan", "h2": "Tahu apa yang diizinkan ponsel Anda",
             "body": ["Ponsel Android bisa menunda atau memblokir alarm – penghemat baterai, Jangan Ganggu, izin yang kurang. Pemeriksaan **Keandalan** meninjau setiap poin dengan bahasa sederhana dan menunjukkan cara memperbaiki yang belum benar.",
                      "Dengan **Uji alarm** Anda bisa mendengar dan merasakan alarm selama lima detik, sebelum malam pertama yang sesungguhnya."],
             "shot": "en-reliability.webp"},
        ],
        "limits_h2": "Batasan yang jujur",
        "limits": "Stay Awake membantu Anda tetap terjaga. Aplikasi ini tidak menggantikan tidur atau istirahat, dan bukan sistem keselamatan untuk bekerja atau berkendara. Tepat tidaknya waktu cek juga bergantung pada ponsel – pemeriksaan keandalan menunjukkan apa yang diizinkan ponsel Anda.",
        "nots_h2": "Tidak perlu mendaftar",
        "nots": [
            "**Tanpa akun, tanpa login.** Sesi, jadwal, dan setelan tetap di ponsel Anda.",
            "**Berfungsi offline.** Cek dan alarm tidak memerlukan internet.",
            "**Sesi tetap berjalan setelah ponsel dimulai ulang.**",
            "**Gratis dengan banner iklan kecil.** Tanpa iklan pada cek dan alarm. Stay Awake Pro menghapus banner – bulanan atau sekali bayar.",
            "**20 bahasa**, dari bahasa Arab sampai bahasa Vietnam.",
        ],
        "privacy_link": "Baca kebijakan privasi (dalam bahasa Inggris)",
        "guides_h2": "Panduan untuk malam panjang",
        "guides_lead": "Berguna juga tanpa aplikasi: alarm setiap 30 menit, shift malam, dan begadang sampai pagi.",
        "faq": [
            ["Apa bedanya dengan alarm biasa?",
             ["Alarm biasa berbunyi pada jam tertentu, entah Anda terjaga atau tidak. Stay Awake bertanya dulu dan baru berbunyi keras kalau Anda tidak menjawab. Aplikasi ini dibuat untuk tetap terjaga, bukan untuk bangun pagi."]],
            ["Apakah layar harus tetap menyala?",
             ["Tidak. Letakkan ponsel, kunci, biarkan layar mati. Cek muncul di atas layar kunci. Kalau Anda memilih guncang, satu guncangan sudah mengonfirmasi meski layar mati."]],
            ["Suara alarm apa yang dipakai?",
             ["Secara bawaan, suara alarm ponsel Anda sendiri. Di setelan Anda bisa beralih ke melodi Stay Awake atau memilih suara lain."]],
            ["Apakah berfungsi tanpa internet?",
             ["Ya. Cek, getar, dan alarm berjalan sepenuhnya di ponsel."]],
            ["Berapa biayanya?",
             ["Semua yang membuat Anda tetap terjaga gratis. Versi gratis menampilkan banner kecil di layar biasa, tidak pernah pada cek atau alarm. Stay Awake Pro menghapusnya, bulanan atau sekali bayar; harganya tertera di Google Play."]],
            ["Apakah ada versi iPhone?",
             ["Tidak, Stay Awake hanya tersedia untuk Android."]],
        ],
        "final_h2": "Kalau Anda harus tetap terjaga, inilah aplikasinya.",
        "final_body": "Mulai sesi, letakkan ponsel. Stay Awake terus bertanya sampai Anda mengakhiri sesi.",
    },

    "guides_index": {
        "title": "Panduan: alarm setiap 30 menit, shift malam, begadang sampai pagi",
        "desc": "Panduan praktis untuk malam panjang: memasang alarm setiap 30 menit di Android, tidak ngantuk saat kerja malam, dan begadang sampai pagi.",
        "h1": "Panduan untuk malam panjang",
        "lead": "Jawaban singkat dan praktis – berguna dengan atau tanpa aplikasi.",
        "app": "**Stay Awake** bertanya pada interval Anda apakah Anda masih terjaga, dan membunyikan alarm kalau tidak ada jawaban.",
    },

    "guides": [
        {
            "id": "every30",
            "slug": "alarm-setiap-30-menit-android",
            "title": "Cara memasang alarm setiap 30 menit di Android",
            "desc": "Aplikasi Jam di Android tidak punya pilihan “setiap 30 menit”. Tiga cara yang berhasil: beberapa alarm, timer yang dimulai ulang, atau aplikasi alarm interval.",
            "h1": "Cara memasang alarm setiap 30 menit di Android",
            "teaser": "Beberapa alarm, timer yang dimulai ulang, atau aplikasi alarm interval – tiga cara.",
            "answer": "Aplikasi Jam di kebanyakan ponsel Android hanya bisa mengulang alarm **per hari dalam seminggu**, bukan setiap X menit. Anda punya tiga pilihan: **membuat beberapa alarm**, **memulai ulang timer** setiap kali, atau memakai **aplikasi alarm interval**.",
            "updated": "2026-11-24",
            "updated_label": "24 November 2026",
            "sections": [
                ["several", "Cara 1: beberapa alarm", [
                    "Buat satu alarm untuk setiap setengah jam di aplikasi Jam. Untuk satu sore tidak masalah; untuk semalaman jadi merepotkan:",
                    {"table": [
                        ["Lama", "Interval", "Jumlah alarm"],
                        ["2 jam", "30 menit", "4"],
                        ["8 jam (22.00–06.00)", "30 menit", "16"],
                        ["8 jam", "15 menit", "32"],
                    ]},
                    "Kekurangannya: harus dibuat satu per satu, dan alarm tetap berbunyi pada jam tetap meski Anda sudah benar-benar terjaga. Setelah itu Anda harus mematikan semuanya lagi.",
                ]],
                ["timer", "Cara 2: memulai ulang timer", [
                    {"steps": [
                        "Buka aplikasi Jam dan masuk ke **Timer**.",
                        "Atur **30:00** lalu mulai.",
                        "Saat berbunyi, hentikan lalu mulai lagi.",
                    ]},
                    "Sederhana, tapi harus dimulai ulang setiap kali. Kalau sekali saja lupa, tidak ada apa-apa lagi sampai pagi.",
                ]],
                ["app", "Cara 3: aplikasi alarm interval", [
                    "Aplikasi alarm interval berulang sendiri. Sebelum memilih, periksa tiga hal:",
                    {"list": [
                        "**Apakah berbunyi saat layar mati dan ponsel terkunci?** Banyak aplikasi hanya berfungsi saat dibuka.",
                        "**Apakah memakai alarm yang tepat waktu (exact alarm)?** Kalau tidak, Android bisa menundanya dalam mode hemat daya.",
                        "**Apa yang terjadi kalau Anda tidak bereaksi?** Alarm berulang biasa berbunyi sebentar lalu berhenti.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Alarm interval yang bertanya dulu",
                "body": [
                    "Stay Awake berulang pada interval Anda – nilai apa pun dari satu menit sampai dua belas jam – dan memakai alarm yang tepat waktu. Tidak langsung berbunyi: aplikasi ini bertanya dulu tanpa suara apakah Anda masih terjaga. Jawab, dan interval dimulai lagi dari saat itu. Tanpa jawaban: getar setelah 10 detik, alarm setelah 20.",
                    "Jadi Anda tidak dikagetkan saat masih terjaga – dan tidak dibiarkan begitu saja saat tertidur.",
                ],
                "shot": "en-home.webp",
                "alt": "Dial di 30 menit, Tanpa batas atau Timer, Mulai sesi" + NOTE_EN + ".",
            },
            "faq": [
                ["Bisakah aplikasi Jam Android mengulang alarm setiap 30 menit?",
                 ["Aplikasi Jam di kebanyakan ponsel Android hanya mengulang per hari dalam seminggu. Untuk setiap 30 menit Anda perlu beberapa alarm, timer, atau aplikasi terpisah."]],
                ["Kenapa alarm interval saya tidak berbunyi saat layar mati?",
                 ["Sering kali penyebabnya pengoptimalan baterai atau izin alarm tepat waktu yang belum diberikan. Periksa di setelan Android apakah penggunaan baterai aplikasi itu tidak dibatasi."]],
                ["Bisakah intervalnya 15 atau 45 menit?",
                 ["Di Stay Awake bisa: dialnya bisa diatur dari satu menit sampai dua belas jam. Tanpa aplikasi, setiap 15 menit berarti 32 alarm untuk malam 8 jam."]],
            ],
        },
        {
            "id": "nightshift",
            "slug": "cara-agar-tidak-ngantuk-saat-kerja-malam",
            "title": "Cara agar tidak ngantuk saat kerja malam: 9 tips praktis",
            "desc": "Tetap waspada saat shift malam: cahaya, gerak, tugas kecil untuk jam-jam sepi sekitar pukul 3 dini hari, makan, dan ritme cek.",
            "h1": "Cara agar tidak ngantuk saat kerja malam",
            "teaser": "Cahaya, gerak, dan rencana untuk jam-jam sepi dini hari.",
            "answer": "Bagian tersulit shift malam jarang ada di awal, melainkan di jam-jam sepi dini hari ketika tidak ada yang terjadi. Yang paling membantu adalah **cahaya, gerak, dan ritme**: bagi malam menjadi blok-blok pendek, beri setiap blok sesuatu untuk dikerjakan, dan jangan lama diam di tempat yang redup.",
            "updated": "2026-11-24",
            "updated_label": "24 November 2026",
            "sections": [
                ["dead-hours", "Rencana untuk jam-jam sepi", [
                    "Siapa pun yang bekerja malam pasti kenal momen ini: antara pukul 2 dan 5 dini hari semuanya sepi, efek kopi sudah hilang, dan mata terasa berat. Jangan biarkan saat itu berjalan begitu saja.",
                    {"list": [
                        "**Simpan tugas yang aktif untuk saat itu.** Mengisi stok, merapikan berkas, berkeliling, memeriksa peralatan – apa pun yang membuat Anda berdiri dan berjalan.",
                        "**Bagi malam menjadi blok** 30 sampai 60 menit. Setiap blok diakhiri dengan tindakan kecil: berdiri, minum air, menulis satu baris di catatan.",
                        "**Hindari waktu pasif yang lama**, seperti membaca atau menatap layar sambil bersandar di kursi.",
                    ]},
                ]],
                ["tips", "9 tips yang berhasil bagi banyak orang", [
                    {"steps": [
                        "**Jaga ruangan tetap terang.** Cahaya redup membuat mengantuk. Nyalakan lampu utama, bukan hanya satu lampu kecil, kalau tempat kerja Anda mengizinkan.",
                        "**Bergerak setiap setengah jam.** Berjalan di lorong, naik beberapa anak tangga, peregangan – beberapa menit sudah cukup.",
                        "**Kerjakan tugas rutin sambil berdiri.** Kalau duduk, mudah terkantuk-kantuk.",
                        "**Minum air secara teratur.** Itu juga memberi alasan untuk berdiri.",
                        "**Makan dalam porsi kecil.** Banyak orang merasa berat setelah makan besar di tengah malam; beberapa camilan kecil lebih nyaman.",
                        "**Pakai air dingin.** Basuh wajah atau tangan saat kantuk datang.",
                        "**Mengobrol dengan seseorang.** Percakapan singkat dengan rekan kerja memecah saat sepi – bagi Anda berdua.",
                        "**Udara segar.** Beberapa menit di jendela yang terbuka atau di luar.",
                        "**Lakukan cek pada jam tetap.** Pengingat rutin – setiap 20 atau 30 menit – yang meminta jawaban secara sadar membantu Anda menyadari saat menit-menit mulai berubah menjadi satu jam tanpa terasa.",
                    ]},
                ]],
                ["before", "Sebelum dan sesudah shift", [
                    "Shift malam dimulai lebih awal dari yang ditunjukkan jam: kalau Anda datang sudah lelah, tidak ada tips yang bisa menolong. Rencanakan tidur sebelum malam pertama dan jaga tidur setelah shift – kamar gelap, ponsel senyap, dan orang serumah diberi tahu.",
                    {"note": "Kalau Anda sadar berulang kali tertidur sebentar, itu tanda yang perlu ditanggapi serius. Bicarakan dengan tim atau atasan Anda – tidak ada aplikasi dan tips yang menggantikan tidur."},
                ]],
            ],
            "app": {
                "h2": "Cek setiap 30 menit",
                "body": [
                    "Stay Awake menjadikan tips nomor 9 sebagai rutinitas: aplikasi ini bertanya pada interval Anda apakah Anda masih terjaga. Guncang ponsel atau ketuk Ya, dan putaran berikutnya dimulai. Kalau Anda tidak menjawab, ponsel bergetar setelah 10 detik dan alarm berbunyi setelah 20.",
                    "Untuk shift yang berulang, buat **jadwal** – misalnya 22.00 sampai 06.00, Senin sampai Jumat. Sesi dimulai dan berakhir sendiri.",
                ],
                "shot": "en-schedules.webp",
                "alt": "Jadwal 22.00–06.00, Senin sampai Jumat, setiap 30 menit" + NOTE_EN + ".",
            },
            "faq": [
                ["Kapan paling sulit tetap terjaga saat shift malam?",
                 ["Bagi banyak orang pada dini hari, kira-kira antara pukul 2 dan 5. Rencanakan tugas yang aktif untuk saat itu."]],
                ["Apakah kopi membantu saat shift malam?",
                 ["Banyak orang minum kopi di awal shift. Kopi tidak menggantikan cahaya, gerak, dan ritme – dan berapa banyak yang cocok untuk Anda bukan hal yang bisa dijawab sebuah situs web."]],
                ["Bagaimana agar tidak ngantuk di malam sepi tanpa pekerjaan?",
                 ["Buat tugas kecil yang tetap setiap 30 sampai 60 menit, berdiri secara teratur, dan jaga ruangan tetap terang. Pengingat cek yang rutin membantu Anda menyadari saat Anda mulai kehilangan fokus."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "cara-begadang-sampai-pagi",
            "title": "Cara begadang sampai pagi: rencana jam demi jam",
            "desc": "Kalau Anda harus terjaga semalaman: rencana untuk awal malam, tengah malam, jam-jam sepi, dan pagi – serta cara menyadari kalau Anda tertidur sebentar.",
            "h1": "Cara begadang sampai pagi",
            "teaser": "Rencana untuk awal malam, tengah malam, jam-jam sepi, dan pagi.",
            "answer": "Semalaman penuh lebih mudah dijalani dengan rencana daripada dengan tekad saja. Mulailah malam dalam keadaan cukup istirahat, jaga suasana **terang dan aktif**, simpan tugas paling aktif untuk setelah pukul 2 – dan siapkan sesuatu yang **mengecek Anda** secara rutin dan berbunyi keras kalau tidak ada jawaban.",
            "updated": "2026-11-24",
            "updated_label": "24 November 2026",
            "sections": [
                ["plan", "Rencana untuk semalaman", [
                    {"table": [
                        ["Kapan", "Yang membantu"],
                        ["Awal malam", "Mulai dalam keadaan cukup istirahat kalau bisa. Makan seperti biasa, jangan makan berat larut malam."],
                        ["Sampai tengah malam", "Kerjakan sekarang tugas yang paling butuh kepala jernih."],
                        ["Tengah malam sampai pukul 2", "Bekerja dalam blok; berdiri dan bergerak di antaranya."],
                        ["Pukul 2 sampai 5", "Bagian tersulit bagi banyak orang: tugas aktif, cahaya terang, udara segar."],
                        ["Pagi", "Cahaya matahari pagi membantu banyak orang di bagian terakhir. Jangan lakukan hal yang butuh konsentrasi penuh."],
                    ]},
                ]],
                ["tricks", "Yang membuat Anda bertahan", [
                    {"list": [
                        "**Cahaya:** lampu utama menyala, layar cukup terang.",
                        "**Gerak:** beberapa menit setiap setengah jam.",
                        "**Air dingin** di wajah dan tangan.",
                        "**Sesuatu untuk dikerjakan dengan tangan** daripada hanya menonton.",
                        "**Teman:** telepon atau chat dengan seseorang yang juga masih terjaga.",
                    ]},
                ]],
                ["notice", "Menyadari saat Anda tertidur sebentar", [
                    "Bahaya malam panjang bukan tumbang seketika, melainkan momen-momen kecil: Anda memejamkan mata “sebentar saja”, dan tiba-tiba satu jam sudah lewat. Hal itu baru Anda sadari kalau ada yang bertanya dari luar.",
                    "Tanpa aplikasi: timer yang Anda mulai ulang setiap kali berbunyi, atau teman yang mengecek lewat pesan. Dengan aplikasi: lihat di bawah.",
                ]],
                ["after", "Keesokan harinya", [
                    "Malam tanpa tidur akan terasa akibatnya. Rencanakan hari berikutnya dengan ringan dan ganti waktu tidur Anda sesegera mungkin.",
                    {"note": "Apakah begadang semalaman ide yang baik untuk Anda, hanya Anda – atau dokter – yang bisa menilai. Panduan ini tentang cara melewati malam yang sudah Anda putuskan untuk dijalani."},
                ]],
            ],
            "app": {
                "h2": "Ada yang bertanya setiap 30 menit",
                "body": [
                    "Stay Awake bertanya pada interval Anda apakah Anda masih terjaga. Guncang ponsel atau ketuk Ya, dan putaran berikutnya dimulai. Kalau jawaban tidak datang, ponsel bergetar setelah 10 detik dan alarm berbunyi setelah 20 – dengan suara alarm ponsel Anda sendiri.",
                    "Mulai sesi **Tanpa batas** untuk malam tanpa batas waktu, atau **Timer** “sampai 06.00”.",
                ],
                "shot": "en-alarm.webp",
                "alt": "Cek setelah 20 detik: Cek terlewat, Masih terjaga?, tombol Ya besar" + NOTE_EN + ".",
            },
            "faq": [
                ["Jam berapa paling sulit tetap terjaga?",
                 ["Banyak orang merasa paling sulit antara sekitar pukul 2 dan 5 dini hari. Simpan tugas paling aktif untuk saat itu."]],
                ["Apakah tidur singkat membantu?",
                 ["Sebagian orang merencanakan tidur singkat. Risikonya tidur jauh lebih lama dari rencana – kalau melakukannya, pasang alarm yang tidak bisa Anda abaikan."]],
                ["Bagaimana memastikan saya terbangun kalau tertidur?",
                 ["Pakai sesuatu yang mengecek Anda secara rutin dan berbunyi keras kalau Anda tidak menjawab – teman, timer berulang, atau aplikasi yang bertanya apakah Anda masih terjaga."]],
            ],
        },
    ],
}
