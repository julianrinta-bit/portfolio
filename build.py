#!/usr/bin/env python3
"""Builds index-v3.html.

REGLA DE FUENTES (2026-11-10, tras tres versiones con errores):
  · TODA cifra sale del EXPEDIENTE — Channel_Portfolio_Reference.md / Julian_Master_Profile.json.
    Están escritas a mano aquí abajo, con su procedencia al lado, para que se puedan auditar.
  · El scrape de YouTube (_assets/work/*.json) NO aporta ni una cifra. Solo da FOTOS:
    avatares y miniaturas, que sí son reales.
  · Voz: PRIMERA PERSONA. Es su portafolio, no una ficha sobre él.
"""
import json, html, os

MIN = json.load(open('data/minis.json'))   # solo para las fotos
MEDIDO = '2026-11-10'
def e(s): return html.escape(str(s))

# ── LAS CIFRAS. Cada una con su origen. Nada derivado del scrape. ──────────
LENS = {
 'ops': dict(
  k='Operations',
  h='I have built three content operations from zero.',
  l='Teams of <b>80 to 100 people</b> across several countries, one of <b>more than 100</b>, and the machinery that kept them publishing every day for a decade.',
  f=[('~$2.5M','a year. The independent P&amp;L I owned at Bored Panda'),
     ('$80&ndash;150K','a month, and I decided where it went: production, talent, marketing. Cost per piece held flat while the bar held'),
     ('70%','operating cost cut at Bored Panda in 2022. $80K to $25K a month'),
     ('3&times;','operations staffed from zero: 100+ people at TheSoul, 80&ndash;100 at Bored Panda, 80&ndash;100 at Hype On Media'),
     ('50+','properties governed by KPI dashboards on click-through, retention and revenue per channel'),
     ('3','delivery models in one house: desk, field, and licensed content')]),
 'str': dict(
  k='Strategy',
  h='The test of a strategy is whether it still works when I am not there.',
  l='Nothing on YouTube means anything on its own. Every decision is made against the four or five channels actually setting the trend in that niche. <b>If the algorithm cannot classify you, you do not exist.</b>',
  f=[('120B+','cross-platform views across the networks I built and directed'),
     ('20B+','on YouTube alone. My conservative, directly attributable floor'),
     ('50+','YouTube Play Buttons across those networks'),
     ('#1','worldwide in its category: Gotcha!, 57 channels in 15 languages'),
     ('#1','worldwide on Facebook by monthly views: Crafty Panda, 2.1B in one month'),
     ('$380K','pipeline and 85 qualified demos a month, from one B2B funnel')]),
 'cre': dict(
  k='Creative direction',
  h='Formats that travelled, and one that reached Netflix.',
  l='Three animated IPs directed in house. <b>Fire Spike: Season 1</b> premiered worldwide in October 2026. The character was born on a channel I built at Bored Panda.',
  f=[('Netflix','Fire Spike: Season 1. Worldwide premiere, October 2026'),
     ('13K &rarr; 1.14M','subscribers on Fire Spike, 610M views, entirely organic'),
     ('3','animated IPs directed in house: Fire Spike, Dear Diary, Bamboo!'),
     ('5','language versions of Dear Diary. Its Spanish page reached 12M'),
     ('16','properties in the portfolio behind the Studio71 licensing deal'),
     ('Award','Prêmio Influenciadores Digitais 2016, by popular vote')]),
}


# ── IMÁGENES · 855 miniaturas, 39 banners, 39 avatares. Todo real, cero cifras ──
V = json.load(open('data/visual.json'))
PR = json.load(open('data/pruebas.json'))
VALIDOS = set(PR['canales_validos'])          # compuerta de fecha: nacidos antes de mi salida
for _mk in list(V['marcas']):
    _m = V['marcas'][_mk]
    _m['avatares'] = [a for a in _m['avatares'] if a in VALIDOS]
    if _m['banner'] not in VALIDOS:
        _m['banner'] = _m['avatares'][0] if _m['avatares'] else None
    if not _m['banner'] and not _m['avatares']: del V['marcas'][_mk]
MARCAS_V, MINIS_V = V['marcas'], V['minis']
COL={'TheSoul':'#2B3A67','Bored Panda':'#A8432B','Hype On Media':'#1F5F4B'}
ORDEN=['Gotcha!','Crafty Panda','Bright Side','5-Minute Crafts','Kaboom!','Fire Spike','Bamboo!','Unscripted World']

def hero():
    """Mosaico a sangre: tres filas de trabajo real antes de una sola palabra."""
    xs=[m['src'] for m in MINIS_V]
    filas=[xs[i::3][:30] for i in range(3)]
    o=''.join('<div class="hr">'+''.join(f'<img src="{x}" alt="" loading="eager">' for x in f)+'</div>' for f in filas)
    return f'<div class="hero">{o}</div>'

NOTA_SIN_PIEZAS = {}   # Bamboo! SÍ tiene largos: 20 comprobados contra el canal, 2026-11-10

def marca_bloque(marca, n_min=24, con_banner=True):
    m=MARCAS_V.get(marca)
    if not m: return ''
    col=COL.get(m['casa'],'#777')
    ban=f'<img class="ban" src="assets/work/bn/{m["banner"]}.jpg" alt="" loading="lazy">' if con_banner else ''
    avs=''.join(f'<img src="assets/work/av/{a}.jpg" alt="" loading="lazy">' for a in m['avatares'])
    if m['minis']:
        cuerpo = '<div class="grid">' + ''.join(
            f'<img src="{x}" alt="" loading="lazy">' for x in m['minis'][:n_min]) + '</div>'
    else:
        nota = NOTA_SIN_PIEZAS.get(marca, 'No long-form pieces on this property.')
        cuerpo = f'<p class="nota">{e(nota)}</p>'
    return (f'<section class="mk" style="--h:{col}">{ban}'
            f'<div class="mkh"><h3>{e(marca)}</h3><span>{e(m["casa"])}</span>'
            f'<div class="avs">{avs}</div></div>{cuerpo}</section>')

def catalogo(n_min=24):
    return ''.join(marca_bloque(k,n_min) for k in ORDEN if k in MARCAS_V)

def mosaico(n=120, desde=0):
    xs=[m['src'] for m in MINIS_V][desde:desde+n]
    return '<div class="mosaic">'+''.join(f'<img src="{x}" alt="" loading="lazy">' for x in xs)+'</div>'

def tira(marca, n=12):
    m=MARCAS_V.get(marca)
    if not m or not m['minis']: return ''
    return '<div class="tira">'+''.join(f'<img src="{x}" alt="" loading="lazy">' for x in m['minis'][:n])+'</div>'

def banner(marca):
    m=MARCAS_V.get(marca)
    return f'<img class="ban solo" src="assets/work/bn/{m["banner"]}.jpg" alt="" loading="lazy">' if m else ''

# ── OPERATIONS · la multiplicación. Cada entrada está en su LinkedIn. ──────
def shape():
    def dots(n,c): return ''.join(f'<i style="background:{c};animation-delay:{k*7}ms"></i>' for k in range(n))
    return f"""<div class="shape">
 <div class="ln"><p class="lb"><b>50+</b> YouTube channels</p><div class="dots">{dots(50,'#A8432B')}</div><p class="cad">three videos a week, each</p></div>
 <div class="ln"><p class="lb"><b>70+</b> Facebook pages</p><div class="dots">{dots(70,'#C9714F')}</div><p class="cad">posting daily</p></div>
 <div class="ln"><p class="lb"><b>15+</b> languages</p><div class="dots">{dots(15,'#7E5A3C')}</div><p class="cad">localised, never dubbed</p></div>
 <div class="out"><span>Pieces published every month</span><em>5,000+</em></div>
</div>"""

# ── CREATIVE · las tres IP. Un avatar cada una, nada inventado. ────────────
IPS = [('UCkIrwXDtY_BSkqBKXCG_uSw','Fire Spike','Bored Panda',
        'Built the team and directed production. After I left, it kept climbing on the system: 1.14M subscribers, 610M views, entirely organic, and a Gold Play Button. Season 1 premiered on Netflix in October 2026.'),
       ('deardiary','Dear Diary','Bored Panda',
        'Directed production and built the team. Five language versions; its Spanish page reached 12M.'),
       ('UCumQ4bX4wm-JtH9BM9MBjlA','Bamboo!','Hype On Media',
        'Built from concept for a client: 654 videos in seven months, 538M views, zero marketing spend. The proof that the animation stack is current, not historical.')]
def ips():
    o=''.join(
      f'<article class="ip"><img src="assets/work/{"ch" if i=="deardiary" else "av"}/{i}.jpg" alt="" loading="lazy">'
      f'<div><h3>{e(n)}<span>{e(c)}</span></h3><p>{e(d)}</p>{tira(n,12)}</div></article>' for i,n,c,d in IPS)
    return f'<div class="ips">{o}</div>'

def wall():
    """Sin mosaico anónimo: una rejilla sin afirmación no dice nada. Julian, 2026-11-10."""
    return ''


SINTOMAS_HTML = '<div class="sy"><span>01</span><div><h3>It keeps compounding after the strategist leaves.</h3><p>The hardest proof to fake, because anyone can check it today. Fire Spike went from 13,000 subscribers to 1.14 million and 610 million views after I left Bored Panda, entirely organic, on the system that was already in place. Season 1 premiered on Netflix in October 2026.</p></div></div><div class="sy"><span>02</span><div><h3>It survives the transplant.</h3><p>A translation dies in the new market. A format is rebuilt natively and lives. I opened four markets from zero in eighteen months at TheSoul and took them past 20M followers, then took Bored Panda from one property to more than fifty across fifteen languages. None of it was dubbing.</p></div></div><div class="sy"><span>03</span><div><h3>Growth is even, not spiky.</h3><p>Look at the last ten videos of any channel. Roughly homogeneous growth between consecutive pieces is health. One spike followed by nothing was luck, or it was paid. Strategy produces outliers repeatedly: Gotcha! reached #1 worldwide in its category across 57 channels, and Crafty Panda reached #1 worldwide on Facebook with 2.1 billion views in a single month.</p></div></div><div class="sy"><span>04</span><div><h3>Engagement outranks views, always.</h3><p>Fifty thousand views with five hundred real comments is worth more than five hundred thousand with emoji. Comments with content mean an audience that argues with you, which is an audience you own. Controversy about the topic is fuel; controversy about the creator is a fire.</p></div></div><div class="sy"><span>05</span><div><h3>The unit economics close.</h3><p>Shorts pay a CPM of one to seven cents. Long form pays two to fifteen dollars. Knowing which engine you are running, and why, is the difference between a visibility strategy and a revenue strategy. I have run both, and cut the cost of running one by 70% without losing the output.</p></div></div><div class="sy"><span>06</span><div><h3>It knows what to kill.</h3><p>A strategist who has never killed anything has never chosen anything. I have shut down a channel that was growing, because growing was not the same as working.</p></div></div><div class="sy"><span>07</span><div><h3>It can be handed to somebody else.</h3><p>The test is whether the thing survives your absence, which means it has to be a playbook and not a person. Fifty-plus Play Buttons are spread across networks I built and then handed over.</p></div></div>'



# ── BANNERS REVISADOS A OJO (hoja de contactos, 2026-11-10) ───────────────
# Regla de Julian: no se publica una imagen en su portafolio sin haberla mirado.
RECHAZADOS = {
 'UCRDrtRb-W1to97gTgfoubuA',  # Crafty Panda Technical — muñecos grises 3D, fuera de marca, 81K subs
 'UCXSfaDPuvu5ICSBod822aFg',  # Kreatif Panda — banner de árboles marrones, sin marca visible
}
INSIGNIA = {           # banner elegido a mano por marca, tras mirarlos
 'Crafty Panda'   :'UCcG3GtQaRpG2E_mw-H_M1oA',   # SCHOOL: pizarra con el panda, la mejor del grupo
 '5-Minute Crafts':'UC295-Dw_tDNtZXFeAPAW6Aw',
 'Bright Side'    :'UC4rlAVgAK0SGk-yTfe48Qpw',
 'Gotcha!'        :'UCtxqQnLgj-1rAVtjpSgPS5A',
 'Fire Spike'     :'UCkIrwXDtY_BSkqBKXCG_uSw',
 'Kaboom!'        :'UCutUv2A6NxOyiF0Fk43TRbA',
 'Bamboo!'        :'UCumQ4bX4wm-JtH9BM9MBjlA',
 'Unscripted World':'UCYLON-r_0tW2vsE1z9lht3w',
}
GOTCHA_SET = ['UCtxqQnLgj-1rAVtjpSgPS5A']   # se completa abajo con los hermanos válidos

def _aplicar_picks():
    import os
    for mk, m in list(V['marcas'].items()):
        m['avatares'] = [a for a in m['avatares'] if a not in RECHAZADOS]
        elegido = INSIGNIA.get(mk)
        if elegido and os.path.exists(f'assets/work/bn/{elegido}.jpg'):
            m['banner'] = elegido
        elif m.get('banner') in RECHAZADOS:
            m['banner'] = None
        if not m['banner'] and not m['avatares']:
            del V['marcas'][mk]
_aplicar_picks()

def gotcha_set():
    """Los siete Gotcha!: el mismo diseno en siete mercados. El argumento, sin texto."""
    import os, json as _j
    can=_j.load(open('data/obra.json'))['canales']
    gs=[c for c in can if c['marca']=='Gotcha!' and c['id'] in VALIDOS
        and os.path.exists(f"assets/work/bn/{c['id']}.jpg")]
    gs.sort(key=lambda c:-c['subs'])
    o=''.join(f'<figure><img src="assets/work/bn/{c["id"]}.jpg" alt="" loading="lazy">'
              f'<figcaption>{e(c["titulo"])}</figcaption></figure>' for c in gs)
    return f'<div class="gset">{o}</div>'

def firespike_chart():
    """RETIRADA 2026-11-10. Comparaba el rendimiento con y sin él, y eso le argumenta
    en contra: invita a leer 'su ausencia no cambió nada'. Julian: 'crea una objeción'.
    El gráfico estaba bien medido; el ARGUMENTO era el equivocado."""
    return ''
def _firespike_chart_retirada():
    """Mediana de vistas por vídeo del canal principal, mes a mes, con la salida marcada."""
    S=PR['firespike']['serie']; W,H,PAD=760,210,34
    mx=max(x['mediana'] for x in S); bw=W/len(S)
    o=[]
    for i,x in enumerate(S):
        hh=(x['mediana']/mx)*(H-PAD); suyo = x['mes'] < '2024-02'
        o.append(f'<rect x="{i*bw:.1f}" y="{H-PAD-hh:.1f}" width="{bw*.7:.1f}" height="{hh:.1f}" '
                 f'fill="#A8432B" opacity="{".95" if suyo else ".6"}">'
                 f'<title>{x["mes"]} · median {x["mediana"]:,} views · {x["n"]} pieces</title></rect>')
    ix=[i for i,x in enumerate(S) if x['mes']>='2024-02'][0]
    xl=ix*bw-3
    o.append(f'<line x1="{xl:.1f}" y1="0" x2="{xl:.1f}" y2="{H-PAD}" stroke="#16140F" stroke-width="1.2" stroke-dasharray="3 3"/>'
             f'<text x="{xl+7:.1f}" y="13" class="brk" fill="#16140F">I leave, Feb 2024</text>')
    o.append(f'<line x1="0" y1="{H-PAD}" x2="{W}" y2="{H-PAD}" class="rule"/>')
    for i,x in enumerate(S):
        if x['mes'].endswith(('-01','-07')):
            o.append(f'<text x="{i*bw:.1f}" y="{H-14}" class="ax">{x["mes"]}</text>')
    a,d=PR['firespike']['antes'],PR['firespike']['despues']
    o.append(f'<text x="0" y="{H-1}" class="ax">Median views per video · before {a/1e6:.1f}M · after {d/1e6:.1f}M</text>')
    return f'<svg viewBox="0 0 {W} {H}" class="chart">{"".join(o)}</svg>'

def lenses():
    o=[]
    for k,v in LENS.items():
        f=''.join(f'<div><b>{x[0]}</b><span>{x[1]}</span></div>' for x in v['f'])
        o.append(f'<div class="lens" id="L-{k}"{"" if k=="ops" else " hidden"}>'
                 f'<p class="kick">{v["k"]}</p><h1>{v["h"]}</h1><p class="lede">{v["l"]}</p>'
                 f'<div class="figs">{f}</div></div>')
    return ''.join(o)

P=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julian Rinta</title><meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#FBFAF7;--ink:#16140F;--soft:#6C6659;--rule:#E2DED5;--wash:#F3F0E9;
--d:'Fraunces',Georgia,serif;--t:'Satoshi',system-ui,sans-serif;--m:'JetBrains Mono',monospace;
--ez:cubic-bezier(.22,.8,.3,1)}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--paper);color:var(--ink);font-family:var(--t);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:1040px;margin:0 auto;padding:0 clamp(20px,4vw,52px)}}
.top{{display:flex;justify-content:space-between;align-items:baseline;gap:18px;flex-wrap:wrap;padding:clamp(28px,4vw,50px) 0 0}}
.me{{font-family:var(--m);font-size:13px;letter-spacing:.14em;text-transform:uppercase}}
.me em{{font-style:normal;color:var(--soft);margin-left:14px;letter-spacing:.05em;text-transform:none}}
nav{{display:flex;gap:3px}}
nav button{{all:unset;cursor:pointer;font-family:var(--m);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
 padding:9px 15px;color:var(--soft);border:1px solid transparent;transition:all 220ms var(--ez)}}
nav button:hover{{color:var(--ink)}}
nav button[aria-selected=true]{{color:var(--ink);border-color:var(--ink)}}
nav button:focus-visible{{outline:2px solid var(--ink);outline-offset:2px}}
h1{{font-family:var(--d);font-weight:600;font-size:clamp(40px,6.4vw,78px);line-height:.95;letter-spacing:-.028em;margin:16px 0 0;max-width:16ch}}
.kick{{font-family:var(--m);font-size:12px;letter-spacing:.17em;text-transform:uppercase;color:var(--soft);margin-top:34px}}
.lede{{margin-top:20px;max-width:58ch;font-size:clamp(18px,2vw,21px);line-height:1.45;color:#38342C}}
.lede b{{font-weight:700;color:var(--ink)}}
.lens{{animation:in .46s var(--ez)}}
@keyframes in{{from{{opacity:0;transform:translateY(9px)}}to{{opacity:1;transform:none}}}}
.figs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(192px,1fr));gap:1px;background:var(--rule);border:1px solid var(--rule);margin-top:36px}}
.figs div{{background:var(--paper);padding:21px 19px}}
.figs b{{display:block;font-family:var(--d);font-size:clamp(26px,3.5vw,38px);font-weight:600;letter-spacing:-.03em;line-height:1}}
.figs span{{display:block;margin-top:8px;font-size:13.5px;color:var(--soft);line-height:1.4}}
section{{margin-top:clamp(54px,8vw,100px)}}
h2{{font-family:var(--d);font-weight:600;font-size:clamp(25px,3.2vw,36px);letter-spacing:-.02em;line-height:1.1;max-width:20ch}}
.says{{margin-top:14px;max-width:62ch;color:#38342C}}
.cap{{margin-top:15px;font-family:var(--m);font-size:12.5px;color:var(--soft);line-height:1.65;max-width:76ch}}
.shape{{margin-top:32px;border-top:1.5px solid var(--ink)}}
.ln{{display:grid;grid-template-columns:176px 1fr 176px;gap:0 20px;align-items:center;padding:18px 0;border-bottom:1px solid var(--rule)}}
.lb{{font-size:14px}} .lb b{{font-family:var(--d);font-size:26px;font-weight:600;margin-right:7px;letter-spacing:-.02em}}
.dots{{display:flex;flex-wrap:wrap;gap:4px}}
.dots i{{width:9px;height:9px;border-radius:50%;opacity:0;transform:scale(.4)}}
.seen .dots i{{animation:pop .42s var(--ez) forwards}}
@keyframes pop{{to{{opacity:.85;transform:scale(1)}}}}
.cad{{font-family:var(--m);font-size:12px;color:var(--soft);text-align:right}}
.out{{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:22px 0;border-top:1.5px solid var(--ink)}}
.out span{{font-size:15px;font-weight:500}}
.out em{{font-family:var(--d);font-style:normal;font-size:clamp(40px,6vw,64px);font-weight:600;letter-spacing:-.03em;line-height:1}}
.ips{{margin-top:30px;border-top:1.5px solid var(--ink)}}
.ip{{display:flex;gap:22px;align-items:flex-start;padding:24px 0;border-bottom:1px solid var(--rule)}}
.ip img{{width:92px;height:92px;border-radius:50%;object-fit:cover;flex:none}}
.ip h3{{font-family:var(--d);font-size:23px;font-weight:600;letter-spacing:-.02em;line-height:1}}
.ip h3 span{{display:inline-block;margin-left:12px;font-family:var(--m);font-size:11px;font-weight:400;color:var(--soft);letter-spacing:.06em;vertical-align:middle}}
.ip p{{margin-top:10px;max-width:62ch;font-size:15.5px;color:#38342C}}
.wall{{display:grid;grid-template-columns:repeat(auto-fill,minmax(152px,1fr));gap:4px;margin-top:34px}}
.th img{{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 240ms var(--ez)}}
.th:hover img{{transform:scale(1.05)}}

/* ── IMAGENES ─────────────────────────────────────────── */
.hero{{display:grid;gap:3px;margin-bottom:0;overflow:hidden;
 mask-image:linear-gradient(180deg,#000 72%,transparent)}}
.hr{{display:flex;gap:3px}}
.hr img{{flex:1 1 0;min-width:0;aspect-ratio:16/9;object-fit:cover;display:block;opacity:0;
 animation:fade .8s var(--ez) forwards}}
.hr:nth-child(2) img{{animation-delay:.08s}} .hr:nth-child(3) img{{animation-delay:.16s}}
@keyframes fade{{to{{opacity:1}}}}
.mk{{margin-top:clamp(34px,5vw,58px)}}
.ban{{width:100%;aspect-ratio:1920/280;object-fit:cover;display:block;border-radius:2px}}
.ban.solo{{margin-top:22px}}
.mkh{{display:flex;align-items:center;gap:16px;flex-wrap:wrap;padding:16px 0 14px;
 border-bottom:2px solid var(--h)}}
.mkh h3{{font-family:var(--d);font-size:26px;font-weight:600;letter-spacing:-.02em;color:var(--h)}}
.mkh span{{font-family:var(--m);font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--soft)}}
.avs{{display:flex;gap:7px;margin-left:auto;flex-wrap:wrap}}
.avs img{{width:40px;height:40px;border-radius:50%;object-fit:cover;transition:transform 200ms var(--ez)}}
.avs img:hover{{transform:scale(1.18)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:4px;margin-top:14px}}
.grid img{{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 220ms var(--ez)}}
.grid img:hover{{transform:scale(1.06);position:relative;z-index:3}}
.mosaic{{display:grid;grid-template-columns:repeat(auto-fill,minmax(124px,1fr));gap:3px;margin-top:26px}}
.mosaic img{{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:all 200ms var(--ez)}}
.mosaic img:hover{{transform:scale(1.12);position:relative;z-index:3}}
.tira{{display:grid;grid-template-columns:repeat(auto-fill,minmax(132px,1fr));gap:4px;margin-top:14px}}
.tira img{{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 200ms var(--ez)}}
.tira img:hover{{transform:scale(1.06);position:relative;z-index:2}}

.syms{{margin-top:30px;border-top:1.5px solid var(--ink)}}
.sy{{display:grid;grid-template-columns:62px 1fr;gap:0 20px;padding:26px 0;border-bottom:1px solid var(--rule)}}
.sy span{{font-family:var(--m);font-size:13px;color:var(--soft);padding-top:5px}}
.sy h3{{font-family:var(--d);font-size:clamp(20px,2.5vw,27px);font-weight:600;letter-spacing:-.02em;line-height:1.15;max-width:24ch}}
.sy p{{margin-top:11px;max-width:64ch;font-size:16px;color:#38342C}}
@media(max-width:620px){{.sy{{grid-template-columns:1fr;gap:6px}}}}
.gset{{margin-top:28px;display:grid;gap:10px}}
.gset figure{{position:relative}}
.gset img{{width:100%;aspect-ratio:1920/230;object-fit:cover;display:block;border-radius:2px}}
.gset figcaption{{position:absolute;left:10px;bottom:8px;font-family:var(--m);font-size:10.5px;
 letter-spacing:.1em;text-transform:uppercase;color:#fff;background:rgba(0,0,0,.42);
 padding:3px 8px;border-radius:2px;backdrop-filter:blur(3px)}}
.heropie{{margin:16px 0 0;font-family:var(--m);font-size:12px;color:var(--soft);
 line-height:1.7;max-width:70ch}}
.nota{{margin-top:14px;font-family:var(--m);font-size:12.5px;color:var(--soft);line-height:1.7}}
footer{{margin:clamp(58px,8vw,100px) 0 72px;padding-top:22px;border-top:1px solid var(--rule);font-size:13px;color:var(--soft);max-width:78ch;line-height:1.65}}
@media(max-width:760px){{.ln{{grid-template-columns:1fr;gap:9px}} .cad{{text-align:left}}
 .ip{{flex-direction:column}} }}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}
 .dots i{{opacity:.85;transform:none}}}}
</style></head><body>
{hero()}
<div class="w">
<p class="heropie">Long-form work published by the operations I built. I did not draw these. I set the packaging standard they had to clear, and the review that caught the ones that did not.</p>

<div class="top">
 <p class="me">Julian Rinta <em>Featured in Forbes Russia, 2019</em></p>
 <nav role="tablist" aria-label="Choose a lens">
  <button role="tab" data-l="ops" aria-selected="true">Operations</button>
  <button role="tab" data-l="str" aria-selected="false">Strategy</button>
  <button role="tab" data-l="cre" aria-selected="false">Creative direction</button>
 </nav>
</div>

{lenses()}

<section class="only-ops">
 <p class="kick" style="margin-top:0">The volume</p>
 <h2>I do not claim what an operation produces. I count it.</h2>
 <p class="says">The Bored Panda network, as I ran it: every property with its own cadence, in fifteen
  languages. Count the dots and do the multiplication yourself.</p>
 {shape()}
 <p class="cap">Every line here is on my public record. The agency that advertises "200+ pieces of
  content every month" is running one fiftieth of this.</p>
</section>

<section class="only-ops">
 <p class="kick" style="margin-top:0">The properties</p>
 <h2>Fifty-odd channels. These are some of them.</h2>
 <p class="says">Each logo is a channel I built, directed or grew. The pieces underneath were made by
  eighty to a hundred people across fifteen languages, most of whom I never met. They still read as
  one brand, and that is what the packaging standard and the two-stage review existed to do.</p>
 {catalogo()}
</section>

<section class="only-ops">
 <p class="kick" style="margin-top:0">The systems</p>
 <h2>Volume without a system is just noise.</h2>
 <p class="says">A workflow that tracked every piece from brief to publication, across languages and
  formats, with handoffs and bottlenecks visible in one place. A two-stage quality control process,
  non-native to native to spot-check, applied in every market I shipped into. KPI dashboards
  governing 50+ properties on click-through, retention and revenue per channel. That is how the bar
  held in markets where nobody on the leadership team spoke the language.</p>
</section>

<section class="only-str" hidden>
 <p class="kick" style="margin-top:0">The proof</p>
 <h2>It survives the transplant.</h2>
 <p class="says">A translation dies in the new market. A format is rebuilt natively and lives.
  Four markets opened from zero in eighteen months at TheSoul, past 20M followers. Then Bored Panda
  from one property to more than fifty, across fifteen languages. Same logic each time, different
  market, built from the ground up in each one.</p>
 {gotcha_set()}
 <p class="cap">Gotcha!, as published in each market. Same design language, rebuilt market by
  market rather than captioned. Seven of them here; there were fifty-seven when I left.</p>
 {banner('Bright Side')}{tira('Bright Side',12)}
 {banner('5-Minute Crafts')}{tira('5-Minute Crafts',12)}
</section>

<section class="only-str" hidden>
 <p class="kick" style="margin-top:0">The repeat</p>
 <h2>The outlier repeats.</h2>
 <p class="says">One spike is luck, or it was paid. Strategy shows up as outliers that keep
  arriving. Gotcha! reached number one worldwide in its category, across 57 channels in fifteen
  languages. Crafty Panda reached number one worldwide on Facebook, with 2.1 billion views in a
  single month. Different brands, different platforms, the same hand.</p>
 <p class="says">The same discipline works where the unit is pipeline rather than views: a B2B
  software funnel I rebuilt went from 1,200 to 12,000 subscribers and produced 85 qualified demos
  a month, roughly $380K in pipeline.</p>
</section>

<section class="only-cre" hidden>
 <p class="kick" style="margin-top:0">The IP</p>
 <h2>Three characters, directed in house.</h2>
 {ips()}
 {wall()}
 <p class="cap">These three I directed myself: the characters, the formats and the production.
  Bamboo! publishes short form only, so it has no long-form pieces to show here.</p>
</section>

<footer>Figures come from my record and are sourced and dated. 120B+ is cross-platform, YouTube and
 Facebook together; YouTube alone is 20B+. Channel counts for Gotcha! are the January 2024 snapshot,
 which is where I left it. Attribution follows the record: built, directed or grown, never founded.
 Imagery is taken from the channels themselves, {MEDIDO}.</footer>

</div><script>
const show=l=>{{
 document.querySelectorAll('nav button').forEach(x=>x.setAttribute('aria-selected',x.dataset.l===l));
 document.querySelectorAll('.lens').forEach(x=>x.hidden=x.id!=='L-'+l);
 ['ops','str','cre'].forEach(k=>document.querySelectorAll('.only-'+k).forEach(s=>s.hidden=k!==l));
}};
document.querySelectorAll('nav button').forEach(b=>b.addEventListener('click',()=>show(b.dataset.l)));
const io=new IntersectionObserver(es=>es.forEach(x=>{{if(x.isIntersecting){{x.target.classList.add('seen');io.unobserve(x.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.shape').forEach(x=>io.observe(x));
</script></body></html>"""
open('index-v3.html','w').write(P)
print(f"index-v3.html · {len(P):,} bytes")
