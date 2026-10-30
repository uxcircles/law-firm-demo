import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA_NUMBER = "447343132461"  # UX CIRCLES — the demo's WhatsApp reaches the studio, not a lawyer
WA_TEL = "+44 7343 132461"

# Language versions. "sc" is generated from "zh" by character conversion.
LANGS = {
    "zh": {"prefix": "", "html": "zh-Hant-HK", "label": "繁"},
    "yue": {"prefix": "yue/", "html": "yue-Hant-HK", "label": "粵"},
    "sc": {"prefix": "sc/", "html": "zh-Hans", "label": "简"},
    "en": {"prefix": "en/", "html": "en-GB", "label": "EN"},
}
LANG_NAMES = {"zh": "繁體中文", "yue": "粵語", "sc": "简体中文", "en": "English"}

_lang = {"cur": "zh"}


def set_lang(lang):
    _lang["cur"] = lang


def cur():
    return _lang["cur"]


def L(zh, yue=None, en=None):
    """Pick text for the current language. Simplified Chinese uses the zh text."""
    lang = cur()
    if lang == "en":
        return en if en is not None else zh
    if lang == "yue":
        return yue if yue is not None else zh
    return zh


_cc = None


def to_simplified(html):
    global _cc
    if _cc is None:
        from opencc import OpenCC
        _cc = OpenCC("hk2s")
    return _cc.convert(html)


ICON = {
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m3.5 6 8.5 7 8.5-7"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.950L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm0 18.15a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.250-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.14.16-.29.18-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.050.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.16-.48-.29Z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.87.25-1.46 1.5-1.46h1.6V4.46A21 21 0 0 0 14.3 4.3c-2.3 0-3.8 1.4-3.8 3.97v2.23H7.9v3h2.6V21h3Z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".9" fill="currentColor"/></svg>',
    "threads": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.9 11.3c-.1 0-.2-.1-.3-.1-.2-2.8-1.7-4.4-4.3-4.4h-.1c-1.5 0-2.8.7-3.6 1.9l1.4 1c.6-.9 1.6-1.1 2.2-1.1 .9 0 1.5.3 2 .8.3.4.6.9.7 1.6-.7-.1-1.5-.2-2.3-.1-2.3.1-3.8 1.5-3.7 3.4.1 1 .5 1.8 1.4 2.4.7.5 1.6.7 2.6.6 1.3-.1 2.3-.6 3-1.5.5-.7.9-1.5 1-2.6.6.4 1.1.9 1.3 1.5.4 1 .5 2.6-.9 4-1.2 1.2-2.6 1.7-4.8 1.7-2.4 0-4.2-.8-5.4-2.3-1.1-1.4-1.7-3.4-1.7-6s.6-4.6 1.7-6c1.2-1.5 3-2.3 5.4-2.3 2.4 0 4.2.8 5.5 2.3.6.8 1.1 1.7 1.4 2.8l1.7-.4c-.4-1.4-1-2.6-1.8-3.6C18 2 15.7 1 12.7 1h-.1C9.7 1 7.5 2 6 3.9 4.6 5.6 3.9 8 3.9 11.1s.7 5.5 2.1 7.2C7.5 20.1 9.7 21 12.6 21h.1c2.6 0 4.4-.7 5.900-2.2 2-2 1.9-4.4 1.3-5.9-.5-1-1.5-1.9-3-2.6Zm-4.3 4.1c-1 .1-2.1-.4-2.1-1.4 0-.7.5-1.6 2.2-1.7h.6c.6 0 1.2.1 1.7.2-.2 2.4-1.3 2.8-2.4 2.9Z"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M7 21h10M4 7h16M4 7l-3 7h6zM20 7l-3 7h6z"/></svg>',
    "passport": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="5" y="2.5" width="14" height="19" rx="1.5"/><circle cx="12" cy="10" r="3.5"/><path d="M8.5 10h7M12 6.5c1 1 1.5 2.2 1.5 3.5s-.5 2.5-1.5 3.5M12 6.5c-1 1-1.5 2.2-1.5 3.5s.5 2.5 1.5 3.5M9 17.5h6"/></svg>',
    "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="1.5"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M3 12.5h18M10.5 12.5v1.5h3v-1.5"/></svg>',
    "pen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h9l5 5v13H5z"/><path d="M14 3v5h5M8.5 13h7M8.5 16.5h5"/></svg>',
    "menu": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}


def wa_link():
    """WhatsApp link with a prefilled message, so the visitor knows they are contacting a design studio."""
    import urllib.parse
    msg = L("你好，我在 UX CIRCLES 的律師網站範例看到這個 WhatsApp，想了解網站設計服務。",
            "你好，我喺 UX CIRCLES 嘅律師網站範例見到呢個 WhatsApp，想了解網站設計服務。",
            "Hi, I found this WhatsApp on the UX CIRCLES law firm website demo and I’d like to ask about web design.")
    if cur() == "sc":
        msg = to_simplified(msg)
    return f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(msg)}"


def nav_items():
    return [
        ("index.html", "home", L("首頁", "主頁", "Home")),
        ("about.html", "about", L("關於我", "關於我", "About")),
        ("fees.html", "fees", L("服務收費", "收費", "Fees")),
        ("sme.html", "sme", L("中小企服務", "中小企服務", "SME")),
        ("blog/index.html", "blog", L("法律專欄", "法律專欄", "Insights")),
    ]


def page(rel, *, key, title, description, body):
    """Write one page for the current language. `rel` is the path inside a language root."""
    lang = cur()
    out_path = LANGS[lang]["prefix"] + rel
    depth = out_path.count("/")
    r = "../" * depth  # to site root
    here = r + LANGS[lang]["prefix"]  # to this language's root

    cur_attr = ' aria-current="page"'
    nav = "".join(
        f'<a href="{here}{href}"{cur_attr if k == key else ""}>{label}</a>'
        for href, k, label in nav_items()
    )
    switch = "".join(
        f'<a href="{r}{v["prefix"]}{rel}" hreflang="{v["html"]}" lang="{v["html"]}" title="{LANG_NAMES[k]}"'
        f'{cur_attr if k == lang else ""}>{v["label"]}</a>'
        for k, v in LANGS.items()
    )

    html = f"""<!doctype html>
<html lang="{LANGS[lang]["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0e1f3a">
<link rel="icon" href="{r}assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif:wght@500;600;700&family=Noto+Serif+TC:wght@500;600;700&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">{L("跳至主要內容", "跳去主要內容", "Skip to content")}</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">{L("範例", "範例", "Demo")}</span><span class="concept-long">{L("虛構範例：網站中的律師、案例與收費均為虛構，WhatsApp 會聯絡 UX CIRCLES，不提供法律服務。", "虛構範例：網站入面嘅律師、案例同收費都係虛構，WhatsApp 會聯絡 UX CIRCLES，唔提供法律服務。", "Fictional demo: the solicitor, cases and fees are made up. WhatsApp reaches UX CIRCLES, not a law firm.")}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{L("設計：", "設計：", "Designed by ")}</span><strong>UX CIRCLES</strong> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg></a>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{here}index.html">
      <img class="brand-mark" src="{r}assets/img/logo.svg" alt="">
      <span class="brand-text"><span class="brand-name">{L("廣東話律師 Kelvin Chan", "廣東話律師 Kelvin Chan", "Kelvin Chan, Solicitor")}</span><span class="brand-sub">{L("倫敦 · 廣東話法律服務", "倫敦 · 廣東話法律服務", "Cantonese Speaking Solicitor · London")}</span></span>
    </a>
    <div class="lang-switch" role="navigation" aria-label="Language">@@LANGSWITCH@@</div>
    <button class="nav-toggle" aria-label="{L("選單", "選單", "Menu")}" aria-expanded="false">{ICON["menu"]}</button>
    <nav class="nav" aria-label="{L("主選單", "主選單", "Main")}">
      {nav}
      <a class="btn btn-primary btn-sm" href="{here}index.html#contact">{L("預約諮詢", "約律師傾", "Book a consultation")}</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-main">
      <div>
        <a class="brand" href="{here}index.html"><img class="brand-mark" src="{r}assets/img/logo.svg" alt=""><span class="brand-text"><span class="brand-name">{L("廣東話律師 Kelvin Chan", "廣東話律師 Kelvin Chan", "Kelvin Chan, Solicitor")}</span><span class="brand-sub">Cantonese Speaking Solicitor</span></span></a>
        <p>{L("立足倫敦，以廣東話為在英港人及企業提供清晰、保密、務實的英國法律意見。",
               "喺倫敦，用廣東話幫在英港人同企業處理英國法律問題——講得清楚、絕對保密、實實際際。",
               "London-based, providing clear, confidential and practical English-law advice in Cantonese, Mandarin and English.")}</p>
      </div>
      <div>
        <h4>{L("服務", "服務", "Services")}</h4>
        <ul>
          <li><a href="{here}index.html#services">{L("民事糾紛", "民事糾紛", "Civil disputes")}</a></li>
          <li><a href="{here}index.html#services">{L("英國移民", "英國移民", "UK immigration")}</a></li>
          <li><a href="{here}sme.html">{L("中小企法律服務", "中小企法律服務", "SME legal services")}</a></li>
          <li><a href="{here}index.html#services">{L("私人客戶", "私人客戶", "Private client")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{L("網站", "網站", "Site")}</h4>
        <ul>
          <li><a href="{here}about.html">{L("關於我", "關於我", "About")}</a></li>
          <li><a href="{here}fees.html">{L("服務收費", "收費", "Fees")}</a></li>
          <li><a href="{here}blog/index.html">{L("法律專欄", "法律專欄", "Insights")}</a></li>
          <li><a href="{here}terms.html">{L("條款及細則", "條款及細則", "Terms &amp; conditions")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{L("聯絡", "聯絡", "Contact")}</h4>
        <ul>
          <li><a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp {WA_TEL}</a></li>
          <li>London, United Kingdom</li>
        </ul>
      </div>
    </div>
    <div class="regulatory">
      <p>{L("【示範文字】此處為律師事務所的監管資料：律師姓名、SRA 編號、專業責任保險及投訴處理程序。本網站為 UX CIRCLES 製作的虛構設計範例，人物、案例及收費均為虛構，不構成法律意見，亦不提供法律服務。",
             "【示範文字】呢度係律師事務所嘅監管資料位置：律師姓名、SRA 編號、專業責任保險同投訴處理程序。本網站係 UX CIRCLES 製作嘅虛構設計範例，人物、案例同收費都係虛構，唔構成法律意見，亦唔提供法律服務。",
             "[Sample text] A real firm would list its regulatory details here: solicitor names, SRA number, professional indemnity insurance and complaints procedure. This website is a fictional design demo by UX CIRCLES. The people, cases and fees are made up; nothing here is legal advice and no legal services are offered.")}</p>
      <p>© <span id="year">2026</span> UX CIRCLES · <a href="{here}terms.html">{L("條款及細則", "條款及細則", "Terms &amp; conditions")}</a><br><span class="concept-note">{L("虛構設計範例，由", "虛構設計範例，由", "Fictional design demo by")} <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a>{L(" 設計", " 設計", "")}</span></p>
    </div>
  </div>
</footer>
<a class="fab" href="{wa_link()}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON["wa"]}</a>
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
"""
    if lang == "sc":
        html = to_simplified(html).replace('lang="yue-Hant-HK">', 'lang="zh-Hans">')
    html = html.replace("@@LANGSWITCH@@", switch)
    full = os.path.join(OUT, out_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def page_hero(title, sub="", intro="", crumbs=""):
    c = f'<div class="crumbs">{crumbs}</div>' if crumbs else ""
    p = f"<p>{intro}</p>" if intro else ""
    s = f'<span class="en">{sub}</span>' if sub else ""
    return f"""<section class="page-hero"><div class="container">{c}<h1>{title}{s}</h1>{p}</div></section>"""


def contact_cta():
    return f"""
<section class="cta" id="contact">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">{L("聯絡", "搵我", "Contact")}</span>
      <h2>{L("先了解情況，再決定下一步", "先傾一傾，再決定下一步", "Let’s talk before you decide")}</h2>
      <p>{L("無論是簽證申請、商業糾紛或僱傭問題，歡迎以 WhatsApp 簡述情況。我會盡快回覆，並說明可行方案及預計收費。初步諮詢費用 £250 起。",
            "無論係簽證申請、生意糾紛定係僱傭問題，歡迎用 WhatsApp 講下你嘅情況。我會盡快覆你，話你知有咩做法同大概收費。初步諮詢 £250 起。",
            "Whether it is a visa application, a business dispute or an employment issue, tell me briefly about your matter on WhatsApp. I will reply promptly with the options available and an indication of fees. Initial consultations from £250.")}</p>
      <p class="footnote" style="color:#8f9bb0;margin-top:14px">{L("（示範網站：WhatsApp 會聯絡 UX CIRCLES 網站設計，而非律師。）", "（示範網站：WhatsApp 會聯絡 UX CIRCLES 網站設計，唔係律師。）", "(Demo site: WhatsApp reaches UX CIRCLES web design, not a solicitor.)")}</p>
    </div>
    <ul class="contact-list reveal">
      <li><a href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}<span>{WA_TEL}<small>WhatsApp</small></span></a></li>
    </ul>
  </div>
</section>"""


def aside_contact():
    return f"""<div class="aside-card dark">
  <h3>{L("預約初步諮詢", "約律師初步傾", "Book an initial consultation")}</h3>
  <p>{L("1 小時視像會議，包含會前審閱不多於 20 頁文件，£250 起。",
        "1 個鐘視像會議，開會前會睇埋你最多 20 頁文件，£250 起。",
        "A 1-hour video call, including pre-reading of up to 20 pages, from £250.")}</p>
  <a class="btn btn-brass" href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp</a>
</div>"""
