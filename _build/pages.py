from layout import page, page_hero, contact_cta, aside_contact, wa_link, ICON, LANGS, L, set_lang, cur
from posts import POSTS


def vat():
    return '<div class="note"><p>' + L(
        "以上收費未計增值稅（VAT）。英格蘭現行增值稅率為 20%。所有收費僅供參考，須按個案複雜程度及雙方書面協議確認。（示範收費）",
        "以上收費未計增值稅（VAT），英格蘭而家係 20%。收費只供參考，要睇過你個案嘅複雜程度、雙方白紙黑字確認先作實。（示範收費）",
        "All fees are subject to VAT, currently 20% in England. Fees are for guidance only and are confirmed in writing after reviewing your matter. (Sample fees.)",
    ) + "</p></div>"


def disclaimer():
    return L(
        "本文為示範網站的範例文章，僅供一般參考，並不構成法律意見。相關法律及規例可能會變更，讀者應就自身情況向具資格的律師尋求意見。",
        None,
        "This is a sample article on a demo website. It is general information only and not legal advice. Laws change; readers should seek advice from a qualified solicitor about their own situation.",
    )


def item(text):
    return f"<li>{text}</li>"


def post_title(p):
    return p["title_en"] if cur() == "en" else p["title"]


def post_excerpt(p):
    return p["excerpt_en"] if cur() == "en" else p["excerpt"]


def post_date(p):
    return p["date_en"] if cur() == "en" else p["date_zh"]


def post_tag(p):
    return p["tag_en"] if cur() == "en" else p["tag"]


def rootp():
    return "../" * LANGS[cur()]["prefix"].count("/")


def wa_btn(cls="btn btn-brass", label=None):
    return f'<a class="{cls}" href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}{label or "WhatsApp"}</a>'


def demo_note():
    return L("* 示範網站：人物、資歷、案例及收費均為虛構。", "* 示範網站：人物、資歷、案例同收費都係虛構。",
             "* Demo website: the person, credentials, cases and fees are fictional.")


# ====================================================================== Home
def home():
    cards = "\n".join(f'''<a class="post-card reveal" href="blog/{p["slug"]}.html">
  <time datetime="{p["date"]}">{post_date(p)}</time>
  <h3>{post_title(p)}</h3>
  <p>{post_excerpt(p)}</p>
</a>''' for p in POSTS[:3])

    areas = [
        ("scale", L("民事糾紛", "民事糾紛", "Civil Disputes"), [
            L("中小企商業及合約糾紛", "中小企生意同合約糾紛", "SME contract &amp; commercial disputes"),
            L("物業及租務糾紛", "物業同租務糾紛", "Property &amp; landlord / tenant disputes"),
            L("英港跨境債務追討", "英港跨境追債", "UK–Hong Kong cross-border debt recovery"),
            L("勞資糾紛", "勞資糾紛", "Employment claims"),
        ], "fees.html#civil", L("了解收費", "睇收費", "View fees")),
        ("passport", L("英國移民服務", "英國移民服務", "UK Immigration"), [
            L("BN(O) 簽證及永居", "BN(O) 簽證同永居", "BN(O) visas &amp; settlement"),
            L("配偶、家庭及工作簽證", "配偶、家庭同工作簽證", "Spouse, family and work visas"),
            L("永居及入籍", "永居同入籍", "Indefinite Leave to Remain (ILR) &amp; citizenship"),
            L("上訴及行政覆核", "上訴同行政覆核", "Appeals &amp; administrative reviews"),
        ], "fees.html#immigration", L("了解收費", "睇收費", "View fees")),
        ("briefcase", L("中小企法律服務", "中小企法律服務", "SME Legal Services"), [
            L("年度法律顧問服務", "年度法律顧問", "Annual retainers"),
            L("商業合約審閱及草擬", "審閱同草擬商業合約", "Commercial contract review &amp; drafting"),
            L("僱傭合約及員工手冊", "僱傭合約同員工手冊", "Employment contracts &amp; staff handbooks"),
            L("合規諮詢", "合規諮詢", "Compliance advice"),
        ], "sme.html", L("了解更多", "睇多啲", "Learn more")),
        ("pen", L("私人客戶", "私人客戶", "Private Client"), [
            L("遺囑及鏡像遺囑", "遺囑同鏡像遺囑", "Wills &amp; mirror wills"),
            L("持久授權書", "持久授權書", "Lasting powers of attorney"),
            L("改名契", "改名契", "Deed poll"),
            L("宣誓及法定聲明", "宣誓同法定聲明", "Oaths &amp; declarations"),
        ], "fees.html#other", L("了解收費", "睇收費", "View fees")),
    ]
    areas_html = "".join(f'''<div class="area">
        <div class="area-icon">{ICON[ic]}</div>
        <h3>{t}</h3>
        <ul>{"".join(item(x) for x in xs)}</ul>
        <a class="more" href="{href}">{more} {ICON["arrow"]}</a>
      </div>''' for ic, t, xs, href, more in areas)

    tl = [
        ("2008", L("取得香港律師資格", "取得香港律師資格", "Admitted as a solicitor in Hong Kong")),
        ("2013", L("移居倫敦，取得英格蘭及威爾斯律師資格", "搬嚟倫敦，取得英格蘭及威爾斯律師資格", "Moved to London; admitted in England &amp; Wales")),
        ("2016", L("於倫敦執業，專注移民及民事糾紛", "喺倫敦執業，專做移民同民事糾紛", "Practising in London, focusing on immigration and civil disputes")),
        (L("現在", "而家", "Today"), L("為在英港人家庭及中小企提供廣東話法律服務", "用廣東話幫在英港人家庭同中小企處理法律問題", "Advising Hong Kong families and SMEs in the UK, in Cantonese")),
    ]
    tl_html = "".join(f'<li><div class="yr">{y}</div><div class="desc">{d}</div></li>' for y, d in tl)

    highlights = [
        (L("BN(O) 家庭永居申請", "BN(O) 家庭永居申請", "BN(O) family settlement"),
         L("協助五口之家整理五年居留紀錄及文件，一次獲批永居", "幫一家五口整理五年居留紀錄同文件，一次過批咗永居", "Organised five years of residence records for a family of five; settlement granted first time")),
        (L("英港跨境追債", "英港跨境追債", "Cross-border debt recovery"),
         L("代表中小企追討香港客戶欠款，三個月內和解收回大部分款項", "代表中小企追討香港客戶欠款，三個月內和解收返大部分錢", "Recovered most of an SME’s unpaid invoices from a Hong Kong client within three months")),
        (L("不公平解僱申索", "不公平解僱申索", "Unfair dismissal claim"),
         L("經 ACAS 早期調解為僱員爭取和解，無需進入審訊", "經 ACAS 早期調解幫僱員爭取到和解，唔使上庭", "Settlement for an employee through ACAS early conciliation, without a hearing")),
        (L("拖欠租金收樓", "拖欠租金收樓", "Rent arrears possession"),
         L("協助業主依法送達通知並取得收樓令", "幫業主依足程序送達通知，攞到收樓令", "Helped a landlord serve the correct notices and obtain a possession order")),
    ]
    hl_html = "".join(f"<li>{t}<span>{d}</span></li>" for t, d in highlights)

    values = [
        (L("以母語溝通", "用廣東話講清講楚", "Advice in your language"),
         L("以廣東話、普通話或英語解釋英國法律程序、風險及選擇，確保您每一步都清楚明白。",
           "用你最熟悉嘅語言解釋英國法律程序、風險同選擇，每一步你都知自己做緊乜。",
           "English legal procedures, risks and options explained in Cantonese, Mandarin or English, so you understand every step.")),
        (L("收費透明", "收費透明", "Transparent fees"),
         L("移民申請設固定收費套餐；民事案件可於初步了解後提供費用估算及不同付款方案。",
           "移民申請有固定收費套餐；民事案件初步了解之後，會俾估價同唔同嘅付款方案你揀。",
           "Fixed-fee packages for immigration applications; fee estimates and flexible funding options for civil disputes.")),
        (L("親自跟進", "親自跟進", "Personal service"),
         L("每宗個案由律師親自處理，不會轉交助理，您隨時知道進度。",
           "每單案都係律師親自處理，唔會掉俾助理，你隨時知道進度。",
           "Every matter is handled by the solicitor personally, so you always know where things stand.")),
    ]
    values_html = "".join(f'<div class="value reveal"><div class="n">0{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(values))

    body = f'''
<section class="hero">
  <div class="container">
    <div class="hero-copy">
      <span class="eyebrow">{L("倫敦 · 廣東話律師", "倫敦 · 廣東話律師", "London · Cantonese speaking solicitor")}</span>
      <h1>{L("以您熟悉的語言，<br>處理英國法律事務", "用你最熟悉嘅語言，<br>搞掂英國法律問題", "English law,<br>explained in your language")}</h1>
      <p class="lead">{L("陳嘉信律師（Kelvin Chan）擁有香港及英格蘭雙重律師資格，執業逾 15 年。立足倫敦，協助在英港人及企業處理移民、民事糾紛、僱傭及商業法律事務。",
                          "陳嘉信律師（Kelvin Chan）有香港同英格蘭雙重律師資格，執業超過 15 年。佢喺倫敦幫在英港人同企業處理移民、民事糾紛、僱傭同商業法律問題。",
                          "Kelvin Chan is a dual-qualified solicitor with over 15 years’ experience. Based in London, he gives clear, practical advice in Cantonese, Mandarin and English to help you protect your rights, business and family in the UK.")}</p>
      <div class="hero-actions">
        {wa_btn("btn btn-brass", L("WhatsApp 預約", "WhatsApp 約時間", "Book on WhatsApp"))}
        <a class="btn btn-light" href="fees.html">{L("查看收費", "睇收費", "View fees")}</a>
      </div>
    </div>
    <figure class="hero-figure" style="margin:0">
      <img src="{rootp()}assets/img/lawyer.jpg" alt="{L("陳嘉信律師（示範人物）", "陳嘉信律師（示範人物）", "Kelvin Chan (fictional)")}" width="900" height="1063">
      <div class="hero-badge"><strong>Kelvin Chan 陳嘉信</strong><span>{L("英格蘭及威爾斯律師（示範人物）", "英格蘭及威爾斯律師（示範人物）", "Solicitor, England &amp; Wales (fictional)")}</span></div>
    </figure>
  </div>
</section>

<section class="creds" aria-label="{L("資歷", "資歷", "Credentials")}">
  <div class="container">
    <div class="cred"><div class="num">15+</div><div class="label">{L("年法律執業經驗", "年執業經驗", "years in legal practice")}</div></div>
    <div class="cred"><div class="num">{L("雙重資格", "雙重資格", "Dual-qualified")}</div><div class="label">{L("香港及英格蘭", "香港同英格蘭", "Hong Kong &amp; England")}</div></div>
    <div class="cred"><div class="num">{L("固定收費", "固定收費", "Fixed fees")}</div><div class="label">{L("BN(O) 簽證及永居套餐", "BN(O) 簽證同永居套餐", "for BN(O) visa &amp; settlement")}</div></div>
    <div class="cred"><div class="num">{L("粵 · 普 · 英", "粵 · 普 · 英", "3 languages")}</div><div class="label">{L("廣東話、普通話及英語", "廣東話、普通話同英文", "Cantonese, Mandarin, English")}</div></div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">{L("服務範疇", "服務範疇", "Practice areas")}</span>
        <h2>{L("我能如何協助您", "我可以點樣幫你", "How I can help")}</h2>
      </div>
      <p class="intro">{L("由個人簽證到企業合約，每宗個案均由律師親自跟進。", "由個人簽證到公司合約，每單案都係律師親自跟。", "From personal visas to commercial contracts, every matter is handled personally.")}</p>
    </div>
    <div class="areas reveal">{areas_html}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container split">
    <div class="case-panel reveal">
      <span class="eyebrow" style="color:var(--brass-light)">{L("近期個案（示範）", "近期個案（示範）", "Recent matters (sample)")}</span>
      <ul>{hl_html}</ul>
    </div>
    <div class="reveal">
      <span class="eyebrow">{L("關於陳律師", "關於陳律師", "About Kelvin")}</span>
      <h2>{L("由香港到倫敦", "由香港到倫敦", "From Hong Kong to London")}</h2>
      <p>{L("陳律師在香港執業五年後移居倫敦，親身經歷在英國重新安家的過程，因此特別明白在英港人家庭面對簽證、工作及生意上的難處。",
            "陳律師喺香港執業五年之後搬嚟倫敦，自己都經歷過喺英國重新起步，所以好明白在英港人家庭喺簽證、工作同生意上面嘅難處。",
            "Kelvin practised in Hong Kong for five years before moving to London. Having rebuilt a life in the UK himself, he understands the visa, work and business challenges Hong Kong families face here.")}</p>
      <ol class="timeline">{tl_html}</ol>
      <a class="btn btn-outline" href="about.html">{L("完整背景", "睇完整背景", "Full profile")} {ICON["arrow"]}</a>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow" style="color:var(--brass-light)">{L("工作方式", "點樣做嘢", "How I work")}</span>
        <h2>{L("專業、透明、清楚易明", "專業、透明、講你聽得明", "Professional, transparent, clear")}</h2>
      </div>
    </div>
    <div class="values">{values_html}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">{L("收費參考", "收費參考", "Fees")}</span>
        <h2>{L("常見服務收費", "常見服務收費", "Popular services")}</h2>
      </div>
      <a class="btn btn-outline" href="fees.html">{L("查看全部收費", "睇晒所有收費", "All fees")} {ICON["arrow"]}</a>
    </div>
    <div class="fee-cards">
      <div class="fee-card reveal"><span class="k">{L("初步諮詢", "初步諮詢", "Initial consultation")}</span><h3>{L("1 小時視像會議", "1 個鐘視像會議", "1-hour video call")}</h3><div class="price">£250<small>{L("起", "起", "from")}</small></div><p>{L("包含會前審閱不多於 20 頁文件。", "包埋開會前睇最多 20 頁文件。", "Includes pre-reading of up to 20 pages of documents.")}</p></div>
      <div class="fee-card featured reveal" data-tag="{L("BN(O) 套餐", "BN(O) 套餐", "BN(O) package")}"><span class="k">{L("BN(O) 簽證／永居／續簽", "BN(O) 簽證／永居／續簽", "BN(O) visa / settlement / extension")}</span><h3>{L("套餐 A · 文件審閱", "套餐 A · 幫你睇文件", "Package A · document review")}</h3><div class="price">£850<small>{L("起 / 每位", "起 / 每位", "from, per applicant")}</small></div><p>{L("電話諮詢、審閱全部文件並提供法律意見、正式申請前覆檢。家庭申請另有優惠。", "電話諮詢、睇晒所有文件再俾法律意見、正式入申請前再覆檢。一家人申請有優惠。", "Telephone consultation, full document review with advice, and a final check before submission. Family discounts available.")}</p></div>
      <div class="fee-card reveal"><span class="k">{L("中小企", "中小企", "SME")}</span><h3>{L("年度法律顧問", "年度法律顧問", "Annual retainer")}</h3><div class="price">£900<small>{L("/ 月", "/ 月", "/ month")}</small></div><p>{L("每月最多 8 小時法律支援，涵蓋合約審閱、策略諮詢及日常僱傭查詢。", "每個月最多 8 個鐘法律支援，包括睇合約、策略諮詢同日常僱傭問題。", "Up to 8 hours a month covering contract reviews, strategy calls and day-to-day employment queries.")}</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">{L("法律專欄", "法律專欄", "Insights")}</span>
        <h2>{L("最新文章", "最新文章", "Latest articles")}</h2>
      </div>
      <a class="btn btn-outline" href="blog/index.html">{L("全部文章", "全部文章", "All articles")} {ICON["arrow"]}</a>
    </div>
    <div class="posts">{cards}</div>
  </div>
</section>
{contact_cta()}
<div class="container" style="padding-top:20px;padding-bottom:20px"><p class="footnote" style="margin:0">{demo_note()}</p></div>
'''
    page("index.html", key="home",
         title=L("廣東話律師 Kelvin Chan｜律師網站範例", "廣東話律師 Kelvin Chan｜律師網站範例", "Kelvin Chan, Cantonese Speaking Solicitor | Law firm website demo"),
         description=L("UX CIRCLES 製作的律師網站設計範例：虛構的倫敦廣東話律師，提供四語版本、固定收費套餐及 WhatsApp 預約。",
                       "UX CIRCLES 製作嘅律師網站設計範例：虛構嘅倫敦廣東話律師，有四語版本、固定收費套餐同 WhatsApp 預約。",
                       "A law firm website demo by UX CIRCLES: a fictional Cantonese speaking solicitor in London, with four language versions, fixed-fee packages and WhatsApp booking."),
         body=body)


# ===================================================================== About
def about_cases():
    return [
        (L("商業及物業", "商業同物業", "Commercial &amp; Property"), [
            L("代表一間倫敦中小企追討香港客戶的長期欠款，透過律師信及和解談判，於三個月內收回大部分款項。",
              "代表一間倫敦中小企追討香港客戶拖咗好耐嘅貨款，靠律師信同和解談判，三個月內收返大部分錢。",
              "Acted for a London SME chasing long-overdue invoices from a Hong Kong customer; most of the debt was recovered within three months through a letter before action and negotiated settlement."),
            L("協助業主處理租客長期欠租，依法送達通知並向法院取得收樓令。",
              "幫業主處理租客長期欠租，依足程序送達通知，再向法院攞到收樓令。",
              "Helped a landlord with long-running rent arrears serve the correct notices and obtain a possession order."),
            L("代表多名批租業權持有人（leaseholders）申請延長租約，並成功議定補價。",
              "代表幾位 leaseholders 申請延長租約，成功傾掂補價。",
              "Represented a group of leaseholders in lease extension claims and negotiated the premium."),
        ]),
        (L("移民及入籍", "移民同入籍", "Immigration &amp; Nationality"), [
            L("協助一個五口 BN(O) 家庭整理五年居留紀錄及證明文件，一次獲批永居。",
              "幫一個五口 BN(O) 家庭整理五年居留紀錄同證明文件，一次過批咗永居。",
              "Prepared five years of residence records and evidence for a BN(O) family of five; settlement was granted first time."),
            L("就配偶簽證被拒提出行政覆核，補充關係證據後獲批。",
              "配偶簽證被拒之後提出行政覆核，補充埋關係證據之後獲批。",
              "Brought an administrative review after a spouse visa refusal; the visa was granted once further relationship evidence was provided."),
            L("協助一名曾有輕微交通違例紀錄的申請人入籍，就「良好品格」要求提交詳細陳述。",
              "幫一位有輕微交通違例紀錄嘅申請人入籍，就「良好品格」要求寫詳細陳述。",
              "Assisted a naturalisation applicant with a minor motoring conviction, preparing detailed representations on the good character requirement."),
        ]),
        (L("僱傭", "僱傭", "Employment"), [
            L("代表一名僱員就不公平解僱提出申索，經 ACAS 早期調解達成和解。",
              "代表一位僱員就不公平解僱提出申索，經 ACAS 早期調解達成和解。",
              "Acted for an employee in an unfair dismissal claim, settled through ACAS early conciliation."),
            L("為一間餐飲集團草擬僱傭合約及員工手冊，並協助處理裁員諮詢程序。",
              "幫一間餐飲集團草擬僱傭合約同員工手冊，仲協助處理裁員諮詢程序。",
              "Drafted employment contracts and a staff handbook for a restaurant group and advised on a redundancy consultation."),
        ]),
    ]


def about():
    n = 0
    blocks = []
    for title, items in about_cases():
        blocks.append(f'<div class="case-group-title"><h3>{title}</h3></div><div class="cases">')
        for it in items:
            n += 1
            blocks.append(f'<div class="case"><span class="idx">{n:02d}</span><p>{it}</p></div>')
        blocks.append("</div>")

    body = f'''
{page_hero(L("關於我", "關於我", "About"), "Kelvin Chan 陳嘉信",
           L("香港及英格蘭雙重律師資格，執業逾 15 年，為在英港人家庭及中小企提供清晰、務實的法律意見。",
             "有香港同英格蘭雙重律師資格，執業超過 15 年，幫在英港人家庭同中小企處理法律問題，講得清楚、做得實際。",
             "A dual-qualified solicitor with over 15 years’ practice, giving clear, practical advice to Hong Kong families and SMEs in the UK."),
           f'<a href="index.html">{L("首頁", "主頁", "Home")}</a> / {L("關於我", "關於我", "About")}')}
<section class="section">
  <div class="container layout-aside">
    <div class="prose">
      <div class="note" style="margin-bottom:28px"><p>{demo_note()}</p></div>
      <h2 style="margin-top:0">{L("陳嘉信律師", "陳嘉信律師", "Kelvin Chan")}</h2>
      <p>{L("陳律師擁有香港及英格蘭雙重律師資格，在兩地累積逾 15 年執業經驗，主要處理英國移民、民事糾紛及僱傭事務，並為中小企擔任常年法律顧問。",
            "陳律師有香港同英格蘭雙重律師資格，喺兩地做咗超過 15 年，主要處理英國移民、民事糾紛同僱傭問題，亦幫中小企做常年法律顧問。",
            "Kelvin is qualified in both Hong Kong and England, with over 15 years’ practice across the two. His work focuses on UK immigration, civil disputes and employment, and he acts as retained counsel for a number of SMEs.")}</p>
      <h2>{L("專業背景", "專業背景", "Background")}</h2>
      <p>{L("陳律師於 2008 年取得香港律師資格，在香港一家商業律師行處理合約及物業糾紛。2013 年移居倫敦並取得英格蘭及威爾斯律師資格，其後專注為華人社群提供移民及民事法律服務。",
            "陳律師 2008 年取得香港律師資格，喺香港一間商業律師行處理合約同物業糾紛。2013 年搬嚟倫敦，取得英格蘭及威爾斯律師資格，之後專心幫華人社群處理移民同民事法律問題。",
            "Kelvin qualified in Hong Kong in 2008 and handled contract and property disputes at a Hong Kong commercial firm. He moved to London in 2013, qualified in England &amp; Wales, and has since focused on immigration and civil work for the Chinese-speaking community.")}</p>
      <p>{L("自 BN(O) 簽證計劃推出以來，陳律師協助了大量香港家庭處理簽證、續簽及永居申請，熟悉申請過程中常見的文件及居留問題。",
            "BN(O) 簽證計劃推出之後，陳律師幫過好多香港家庭處理簽證、續簽同永居申請，好熟悉申請途中常見嘅文件同居留問題。",
            "Since the BN(O) route opened, he has helped many Hong Kong families with visa, extension and settlement applications, and knows the document and residence issues that commonly arise.")}</p>
      <h2>{L("代表個案（示範）", "代表個案（示範）", "Selected matters (sample)")}</h2>
      {"".join(blocks)}
    </div>
    <aside class="aside">
      <div class="aside-card">
        <img src="{rootp()}assets/img/lawyer.jpg" alt="{L("陳嘉信律師（示範人物）", "陳嘉信律師（示範人物）", "Kelvin Chan (fictional)")}" loading="lazy" style="aspect-ratio:1;object-fit:cover;object-position:30% 20%;margin:-26px -24px 20px;width:calc(100% + 48px);max-width:none">
        <dl class="dl">
          <div><dt>{L("英格蘭及威爾斯律師", "英格蘭及威爾斯律師", "Solicitor, England &amp; Wales")}</dt><dd>{L("2013 年取得資格", "2013 年取得資格", "Admitted 2013")}</dd></div>
          <div><dt>{L("香港律師", "香港律師", "Hong Kong solicitor")}</dt><dd>{L("2008 年取得資格", "2008 年取得資格", "Admitted 2008")}</dd></div>
          <div><dt>{L("語言", "語言", "Languages")}</dt><dd>{L("廣東話、普通話、英語", "廣東話、普通話、英文", "Cantonese, Mandarin, English")}</dd></div>
          <div><dt>{L("示範", "示範", "Demo")}</dt><dd>{L("虛構人物，非真實律師", "虛構人物，唔係真律師", "Fictional person, not a real solicitor")}</dd></div>
        </dl>
      </div>
      {aside_contact()}
    </aside>
  </div>
</section>
{contact_cta()}
'''
    page("about.html", key="about",
         title=L("關於我｜廣東話律師 Kelvin Chan（範例）", "關於我｜廣東話律師 Kelvin Chan（範例）", "About | Kelvin Chan, Solicitor (demo)"),
         description=L("虛構人物陳嘉信律師的背景與代表個案，UX CIRCLES 律師網站設計範例。",
                       "虛構人物陳嘉信律師嘅背景同代表個案，UX CIRCLES 律師網站設計範例。",
                       "Background and sample matters for Kelvin Chan, a fictional solicitor in a UX CIRCLES law firm website demo."),
         body=body)


# ====================================================================== Fees
def row(t, v, vsub="", d=""):
    dd = f'<div class="d">{d}</div>' if d else ""
    vs = f"<small>{vsub}</small>" if vsub else ""
    return f'<li class="price-row"><div class="t">{t}{dd}</div><div class="v">{v}{vs}</div></li>'


def fees():
    hour = L("每小時", "每個鐘", "per hour")
    capped = L("每小時，上限 £5,500", "每個鐘，封頂 £5,500", "per hour, capped at £5,500")
    frm = L("起", "起", "from")
    pp = L("每位申請人", "每位申請人", "per applicant")
    body = f'''
{page_hero(L("服務收費", "收費", "Fees"), "",
           L("收費清晰透明。移民申請設固定收費套餐；民事案件可於初步了解案情後提供費用估算及不同付款方案。",
             "收費清清楚楚。移民申請有固定套餐；民事案件初步了解完之後，會俾估價同唔同付款方案你揀。",
             "Clear, upfront pricing. Fixed-fee packages for immigration applications; estimates and flexible funding options for civil disputes."),
           f'<a href="index.html">{L("首頁", "主頁", "Home")}</a> / {L("服務收費", "收費", "Fees")}')}
<section class="section">
  <div class="container layout-aside">
    <div>
      <div class="price-block reveal">
        <h2>{L("初步諮詢", "初步諮詢", "Initial consultation")}</h2>
        <ul class="price-rows">
          {row(L("1 小時視像會議", "1 個鐘視像會議", "1-hour video call"), "£250", frm,
               L("包含會前審閱不多於 20 頁文件", "包埋開會前睇最多 20 頁文件", "Includes pre-reading of up to 20 pages of documents"))}
        </ul>
      </div>
      <div class="price-block reveal" id="civil">
        <h2>{L("民事糾紛", "民事糾紛", "Civil disputes")}</h2>
        <ul class="price-rows">
          {row(L("按時收費", "按鐘收費", "Hourly rate"), "£350", hour,
               L("可於初步了解案情後提供費用估算，並提供不同付款方案。", "初步了解案情之後可以俾估價你，亦有唔同付款方案。", "Fee estimates after an initial review of complexity; different funding options available."))}
        </ul>
      </div>
      <div class="price-block reveal" id="immigration">
        <h2>{L("英國移民服務", "英國移民服務", "UK immigration")}</h2>
        <h3 style="margin-top:28px">{L("BN(O) 簽證、永居或續簽申請", "BN(O) 簽證、永居或者續簽", "BN(O) route — visa, settlement or extension")}</h3>
        <div class="packages">
          <div class="pkg">
            <h3>{L("電話諮詢", "電話諮詢", "Telephone consultation")}</h3><div class="sub">&nbsp;</div>
            <div class="price">£350</div>
            <ul><li>{L("就您的個案提供初步法律意見", "就你個案俾初步法律意見", "Initial advice on your case")}</li></ul>
          </div>
          <div class="pkg">
            <h3>{L("套餐 A", "套餐 A", "Package A")}</h3><div class="sub">{pp}</div>
            <div class="price">£850<small>{frm}</small></div>
            <ul>
              <li>{L("電話諮詢", "電話諮詢", "Telephone consultation")}</li>
              <li>{L("審閱文件並提供法律意見（包括是否需要補充文件）", "睇晒你啲文件再俾意見（包括使唔使補文件）", "Review of supporting documents and advice on any further evidence needed")}</li>
              <li>{L("正式申請前覆檢文件", "正式入申請之前再覆檢", "Final review before submission")}</li>
            </ul>
          </div>
          <div class="pkg featured">
            <h3>{L("套餐 B", "套餐 B", "Package B")}</h3><div class="sub">{pp}</div>
            <div class="price">£2,450<small>{frm}</small></div>
            <ul>
              <li>{L("套餐 A 全部服務", "套餐 A 所有服務", "Everything in Package A")}</li>
              <li>{L("書面陳詞及證人供詞（如需要）", "書面陳詞同證人供詞（如有需要）", "Cover letter and witness statements (if needed)")}</li>
              <li>{L("代辦全部申請表格", "幫你填晒所有申請表", "Completion of all application forms")}</li>
              <li>{L("與移民局聯絡並回覆查詢", "同移民局聯絡、覆佢哋嘅查詢", "Liaising with UKVI and answering queries")}</li>
            </ul>
          </div>
        </div>
        <p class="footnote">{L("套餐以每位申請人計算，家庭申請另有優惠。", "套餐以每位申請人計，一家人申請有優惠。", "Packages are priced per applicant; family discounts are available.")}</p>
        <ul class="price-rows" style="margin-top:12px">
          {row(L("配偶、家庭及工作簽證", "配偶、家庭同工作簽證", "Spouse, family and work visas"), "£2,500")}
          {row(L("永居（非 BN(O) 途徑）及入籍", "永居（非 BN(O)）同入籍", "ILR (other routes) &amp; citizenship"), "£2,800")}
          {row(L("創新創業者簽證", "創新創業者簽證", "Innovator Founder visa"), "£350", capped)}
          {row(L("僱主擔保牌照", "僱主擔保牌照", "Sponsor licence"), "£350", capped)}
          {row(L("上訴及行政覆核", "上訴同行政覆核", "Appeals &amp; administrative reviews"), "£350", hour)}
        </ul>
        <div style="margin-top:24px">
          <h3 style="font-size:1rem">{L("以上收費及套餐不包括", "以上收費同套餐唔包", "Not included in the above")}</h3>
          <ul class="excl">
            <li>{L("簽證費及醫療附加費（IHS）", "簽證費同醫療附加費（IHS）", "Visa fees and the Immigration Health Surcharge")}</li>
            <li>{L("簽證中心費用（例如優先服務）", "簽證中心費用（例如「快證」）", "Visa centre fees (e.g. priority service)")}</li>
            <li>{L("翻譯或專家證據（可另行報價）", "翻譯或者專家證據（可以另外報價）", "Translations or expert evidence (quoted separately)")}</li>
            <li>{L("雜費（身份認證、郵費等）", "雜費（身份認證、郵費等）", "Expenses (ID checks, postage, etc.)")}</li>
          </ul>
        </div>
      </div>
      <div class="price-block reveal" id="other">
        <h2>{L("其他服務", "其他服務", "Other services")}</h2>
        <ul class="price-rows">
          {row(L("夫妻鏡像遺囑", "夫妻鏡像遺囑", "Mirror wills"), "£1,000")}
          {row(L("持久授權書", "持久授權書", "Lasting power of attorney"), "£650", L("每份", "每份", "each"))}
          {row(L("改名契", "改名契", "Deed poll"), "£350")}
          {row(L("宣誓及法定聲明", "宣誓同法定聲明", "Oaths &amp; declarations"), "£25", L("起", "起", "from"))}
        </ul>
      </div>
      {vat()}
    </div>
    <aside class="aside">
      {aside_contact()}
      <div class="aside-card">
        <h3>{L("中小企客戶？", "你係中小企老闆？", "Running a business?")}</h3>
        <p>{L("年度法律顧問服務每月 £900 起，成本固定可預計。", "年度法律顧問每月 £900 起，成本固定、唔怕爆數。", "Annual retainers from £900 a month at a predictable fixed cost.")}</p>
        <a class="btn btn-outline" href="sme.html">{L("中小企服務", "中小企服務", "SME services")} {ICON["arrow"]}</a>
      </div>
    </aside>
  </div>
</section>
{contact_cta()}
'''
    page("fees.html", key="fees",
         title=L("服務收費｜廣東話律師 Kelvin Chan（範例）", "收費｜廣東話律師 Kelvin Chan（範例）", "Fees | Kelvin Chan, Solicitor (demo)"),
         description=L("律師網站範例的收費頁：BN(O) 固定收費套餐、初步諮詢及按時收費。", "律師網站範例嘅收費頁：BN(O) 固定收費套餐、初步諮詢同按鐘收費。",
                       "Fees page from a law firm website demo: BN(O) fixed-fee packages, initial consultations and hourly rates."),
         body=body)


# ======================================================================= SME
def sme():
    body = f'''
{page_hero(L("中小企法律服務", "中小企法律服務", "SME legal services"), "",
           L("以可預計的固定成本，為您的中小企提供專屬法律保障，無需再為難以預計的按時收費帳單煩惱。",
             "用固定、預算得到嘅成本，幫你盤生意請個專屬法律顧問，唔使再驚按鐘收費張單爆煲。",
             "Dedicated legal counsel for your business at a predictable fixed cost — no surprise hourly bills."),
           f'<a href="index.html">{L("首頁", "主頁", "Home")}</a> / {L("中小企服務", "中小企服務", "SME")}')}
<section class="section">
  <div class="container">
    <div class="retainer reveal">
      <div class="retainer-main">
        <span class="eyebrow">{L("年度法律顧問", "年度法律顧問", "Annual retainer")}</span>
        <h2>{L("您企業的常年法律顧問", "你公司嘅常年法律顧問", "Your business’s legal counsel")}</h2>
        <p>{L("按年簽訂的常年法律服務，每月提供最多 8 小時支援——足以審閱標準商業合約、進行策略性電話諮詢，以及處理日常僱傭或營運相關的法律查詢。",
              "按年簽嘅常年法律服務，每個月有最多 8 個鐘支援——夠睇標準商業合約、傾策略電話，仲可以處理日常僱傭同營運上嘅法律問題。",
              "For £900 a month, an annual retainer gives you up to 8 hours of support — enough to review standard commercial contracts, hold strategy calls and handle day-to-day employment or operational queries.")}</p>
        <h3 style="margin-top:28px">{L("需要不同的服務組合？", "想要唔同組合？", "Need a different set-up?")}</h3>
        <p>{L("可按您的業務節奏度身訂造，在每月服務時數及費用上提供充分彈性。",
              "可以跟你盤生意嘅節奏度身訂造，每月時數同收費都好有彈性。",
              "Retainers can be built around your business, with flexibility on monthly hours and price.")}</p>
        <div class="note" style="margin-top:24px"><p>{L("本服務旨在提供預防性的日常法律意見，並不包括訴訟及複雜企業交易（如併購），該等服務可另行報價。",
              "呢個計劃係做預防性嘅日常法律意見，唔包打官司同複雜公司交易（例如併購），呢啲可以另外報價。",
              "The retainer covers proactive day-to-day advice and excludes litigation and complex corporate transactions such as M&amp;A, which are quoted separately.")}</p></div>
      </div>
      <div class="retainer-side">
        <h3>{L("標準方案", "標準方案", "Standard plan")}</h3>
        <div class="price">£900<small>{L("/ 月", "/ 月", "/ month")}</small></div>
        <ul>
          <li><span>{L("每月支援時數", "每月支援時數", "Hours per month")}</span><b>{L("最多 8 小時", "最多 8 個鐘", "up to 8")}</b></li>
          <li><span>{L("商業合約審閱", "睇商業合約", "Contract reviews")}</span><b>✓</b></li>
          <li><span>{L("策略性電話諮詢", "策略電話諮詢", "Strategy calls")}</span><b>✓</b></li>
          <li><span>{L("日常僱傭及營運查詢", "日常僱傭同營運問題", "Day-to-day queries")}</span><b>✓</b></li>
        </ul>
        {wa_btn("btn btn-brass", L("WhatsApp 查詢", "WhatsApp 查詢", "Enquire on WhatsApp"))}
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">{L("按項目收費", "按項目收費", "Project-based")}</span><h2>{L("其他中小企服務", "其他中小企服務", "Other SME services")}</h2></div></div>
    <div class="fee-cards">
      <div class="fee-card reveal"><span class="k">{L("初步諮詢", "初步諮詢", "Initial consultation")}</span><h3>{L("1 小時視像會議", "1 個鐘視像會議", "1-hour video call")}</h3><div class="price">£300<small>{L("起", "起", "from")}</small></div><p>{L("包含會前審閱不多於 20 頁文件。", "包埋開會前睇最多 20 頁文件。", "Includes pre-reading of up to 20 pages of documents.")}</p></div>
      <div class="fee-card reveal"><span class="k">{L("合約", "合約", "Contracts")}</span><h3>{L("商業及僱傭合約審閱及草擬", "審閱同草擬商業及僱傭合約", "Commercial &amp; employment contract review and drafting")}</h3><div class="price">£350<small>{L("/ 小時", "/ 個鐘", "/ hour")}</small></div><p>{L("可按複雜程度提供固定報價。", "可以按複雜程度報實價。", "Fixed-fee quotes available based on complexity.")}</p></div>
      <div class="fee-card reveal"><span class="k">{L("員工手冊", "員工手冊", "Staff handbook")}</span><h3>{L("員工手冊及公司政策", "員工手冊同公司政策", "Staff handbook &amp; policies")}</h3><div class="price">£1,200<small>{L("起", "起", "from")}</small></div><p>{L("涵蓋請假、紀律、投訴及資料保護等常用政策。", "包括請假、紀律、投訴同資料保護等常用政策。", "Covers leave, disciplinary, grievance and data protection policies.")}</p></div>
    </div>
    <div style="margin-top:32px" class="reveal">{vat()}</div>
  </div>
</section>
{contact_cta()}
'''
    page("sme.html", key="sme",
         title=L("中小企法律服務｜廣東話律師 Kelvin Chan（範例）", "中小企法律服務｜廣東話律師 Kelvin Chan（範例）", "SME Legal Services | Kelvin Chan, Solicitor (demo)"),
         description=L("律師網站範例的中小企服務頁：年度法律顧問方案與項目收費。", "律師網站範例嘅中小企服務頁：年度法律顧問方案同項目收費。",
                       "SME page from a law firm website demo: annual retainer plan and project-based fees."),
         body=body)


# ====================================================================== Blog
def render_block(b):
    if isinstance(b, str):
        return f"<p>{b}</p>"
    kind, text = b
    return {"h": f"<h2>{text}</h2>", "q": f"<blockquote>{text}</blockquote>"}[kind]


def blog_note():
    return L(
        "",
        "",
        '<div class="note" style="margin-bottom:28px"><p>Articles are written in Cantonese. Use your browser’s translate feature for an English version.</p></div>',
    )


def blog():
    items = "\n".join(f'''<a class="post-item reveal" href="{p["slug"]}.html">
  <time datetime="{p["date"]}">{post_date(p)}</time>
  <div><h2>{post_title(p)}</h2><p>{post_excerpt(p)}</p><span class="tag" style="margin:12px 0 0">{post_tag(p)}</span></div>
</a>''' for p in POSTS)
    body = f'''
{page_hero(L("法律專欄", "法律專欄", "Insights"), "",
           L("以淺白文字拆解英國移民、僱傭及生活中的法律問題。", "用廣東話拆解英國移民、僱傭同生活上嘅法律問題。", "Plain-language notes on UK immigration, employment and everyday legal questions, written in Cantonese."),
           f'<a href="../index.html">{L("首頁", "主頁", "Home")}</a> / {L("法律專欄", "法律專欄", "Insights")}')}
<section class="section">
  <div class="container layout-aside">
    <div>{blog_note()}<div class="post-list">{items}</div></div>
    <aside class="aside">{aside_contact()}</aside>
  </div>
</section>
'''
    page("blog/index.html", key="blog",
         title=L("法律專欄｜廣東話律師 Kelvin Chan（範例）", "法律專欄｜廣東話律師 Kelvin Chan（範例）", "Insights | Kelvin Chan, Solicitor (demo)"),
         description=L("律師網站範例的專欄頁：BN(O)、永居、入籍及僱傭的範例文章。", "律師網站範例嘅專欄頁：BN(O)、永居、入籍同僱傭嘅範例文章。",
                       "Insights page from a law firm website demo, with sample articles on BN(O), settlement and employment."),
         body=body)

    for i, p in enumerate(POSTS):
        newer = POSTS[i - 1] if i > 0 else None
        older = POSTS[i + 1] if i + 1 < len(POSTS) else None
        nav = '<nav class="post-nav">'
        nav += f'<a href="{older["slug"]}.html"><small>← {L("上一篇", "上一篇", "Previous")}</small>{post_title(older)}</a>' if older else "<span></span>"
        nav += f'<a class="next" href="{newer["slug"]}.html"><small>{L("下一篇", "下一篇", "Next")} →</small>{post_title(newer)}</a>' if newer else "<span></span>"
        nav += "</nav>"
        en_sub = f'<p style="color:#aab4c5;margin-top:10px">{p["title_en"]}</p>' if cur() == "en" else ""
        body = f'''
<section class="page-hero"><div class="container" style="max-width:900px">
  <div class="crumbs"><a href="../index.html">{L("首頁", "主頁", "Home")}</a> / <a href="index.html">{L("法律專欄", "法律專欄", "Insights")}</a></div>
  <h1 style="font-size:clamp(1.8rem,4vw,2.6rem)" lang="yue-Hant-HK">{p["title"]}</h1>{en_sub}
  <div class="article-meta"><time datetime="{p["date"]}">{post_date(p)}</time><span>·</span><span>{L("陳嘉信律師", "陳嘉信律師", "Kelvin Chan")}</span><span>·</span><span>{post_tag(p)}</span></div>
</div></section>
<section class="section" style="padding-top:56px">
  <div class="container layout-aside">
    <article class="prose article" lang="yue-Hant-HK">
      {blog_note()}
      {"".join(render_block(b) for b in p["body"])}
      <p class="disclaimer">{disclaimer()}</p>
      {nav}
    </article>
    <aside class="aside">{aside_contact()}</aside>
  </div>
</section>
'''
        page(f"blog/{p['slug']}.html", key="blog", title=f"{post_title(p)} | {L('法律專欄（範例）', '法律專欄（範例）', 'Insights (demo)')}",
             description=post_excerpt(p), body=body)


# ===================================================================== Terms
EN_TERMS = [
    ("About this website", "This website is a design demo created by UX CIRCLES Ltd to show how a law firm website can be structured. Kelvin Chan and all cases, fees and articles on it are fictional. It is not the website of any real solicitor or law firm."),
    ("No legal advice or legal services", "Nothing on this website is legal advice, and no legal services are offered through it. If you need legal help, please contact a solicitor regulated by the Solicitors Regulation Authority."),
    ("WhatsApp and enquiries", "The WhatsApp links on this website connect you to UX CIRCLES, a web design studio. We can talk to you about website design only and cannot discuss legal matters."),
    ("Sample text", "In a live website, this page would hold the firm’s regulatory information, complaints procedure, professional indemnity insurance details and privacy notice."),
    ("Images", "The portrait photograph is a stock image from Pexels and shows a model, not a solicitor."),
    ("Law", "English law applies to the use of this website."),
]
ZH_TERMS = [
    ("關於本網站", "本網站是 UX CIRCLES Ltd 製作的設計範例，用以展示律師事務所網站的架構與設計。網站中的陳嘉信律師，以及所有案例、收費及文章均為虛構，並非任何真實律師或律師事務所的網站。"),
    ("不構成法律意見，亦不提供法律服務", "本網站任何內容均不構成法律意見，亦不透過本網站提供任何法律服務。如需法律協助，請聯絡受英國律師監管局（SRA）規管的律師。"),
    ("WhatsApp 及查詢", "本網站的 WhatsApp 連結會聯絡網站設計公司 UX CIRCLES。我們只能就網站設計與您溝通，無法討論任何法律事務。"),
    ("示範文字", "正式上線的律師網站會在此頁列出事務所的監管資料、投訴處理程序、專業責任保險及私隱政策。"),
    ("圖片", "網站上的人像照片為 Pexels 圖庫圖片，照片中的人物為模特兒，並非律師。"),
    ("適用法律", "本網站的使用受英格蘭法律管轄。"),
]


def terms():
    items = EN_TERMS if cur() == "en" else ZH_TERMS
    ol = "<ol>" + "".join(f"<li><strong>{t}</strong>{d}</li>" for t, d in items) + "</ol>"
    yue_note = '<div class="note" style="margin-bottom:28px"><p>條款以書面語撰寫，確保用詞準確。</p></div>' if cur() == "yue" else ""
    body = f'''
{page_hero(L("條款及細則", "條款及細則", "Terms &amp; conditions"), "", "",
           f'<a href="index.html">{L("首頁", "主頁", "Home")}</a> / {L("條款及細則", "條款及細則", "Terms")}')}
<section class="section">
  <div class="container layout-aside">
    <div class="prose terms">{yue_note}<h2 style="margin-top:0">{L("網站聲明", "網站聲明", "Website notice")}</h2>{ol}</div>
    <aside class="aside">
      <div class="aside-card"><h3>{L("網站設計", "網站設計", "Website design")}</h3>
        <p>{L("這是 UX CIRCLES 的律師網站設計範例。想為您的事務所建立類似網站？", "呢個係 UX CIRCLES 嘅律師網站設計範例。想幫你間律師行整個類似嘅網站？", "This is a law firm website demo by UX CIRCLES. Want a site like this for your firm?")}</p>
        <a class="btn btn-outline" href="https://ux-circles.com/professionals" target="_blank" rel="noopener">ux-circles.com {ICON["arrow"]}</a>
      </div>
    </aside>
  </div>
</section>
'''
    page("terms.html", key="",
         title=L("條款及細則｜律師網站範例", "條款及細則｜律師網站範例", "Terms &amp; Conditions | Law firm website demo"),
         description=L("本網站為 UX CIRCLES 製作的虛構律師網站設計範例。", "本網站係 UX CIRCLES 製作嘅虛構律師網站設計範例。",
                       "This website is a fictional law firm website demo by UX CIRCLES."),
         body=body)


for lang in LANGS:
    set_lang(lang)
    home()
    about()
    fees()
    sme()
    blog()
    terms()
print("built:", ", ".join(LANGS))
