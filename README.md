# Law firm website demo — UX CIRCLES

A fictional law firm website built by [UX CIRCLES](https://ux-circles.com/professionals) as a design sample.
**Kelvin Chan (陳嘉信) and every case, fee and article on this site are made up.** It is not the
website of any real solicitor or law firm, and no legal services are offered through it.

- Every page carries a "Demo" stripe saying the content is fictional.
- All WhatsApp links go to UX CIRCLES (+44 7343 132461) with a pre-filled web-design enquiry.
- Every page is `noindex, nofollow`, so search engines won't list a fictional solicitor.

## Languages

| Path    | Version                    | Source                                  |
|---------|----------------------------|-----------------------------------------|
| `/`     | 繁體中文（書面語） default | `zh` text in `_build/`                  |
| `/yue/` | 粵語                       | `yue` text in `_build/`                 |
| `/sc/`  | 简体中文                   | auto-converted from 繁體中文 (OpenCC)   |
| `/en/`  | English                    | `en` text in `_build/`                  |

Text is written with `L(繁體, 粵語, English)`; if the 粵語 argument is `None`, the 繁體 text is used.

## Editing

The HTML is generated so the header, footer and navigation stay consistent:

- Page content: `_build/pages.py`
- Articles: `_build/posts.py`
- Header, footer, WhatsApp number: `_build/layout.py`

```
pip install opencc-python-reimplemented
python3 _build/pages.py
```

## Credits

Portrait: [Pexels photo 5673486](https://www.pexels.com/photo/mature-asian-lawyer-in-formal-outfit-sitting-at-table-5673486/)
(Pexels licence; the person shown is a model, not a solicitor).
