#!/usr/bin/env python3
"""Genera operaciones.html desde data/obra.json. Los gráficos son SVG dibujado, no imágenes."""
import json, collections, html

D = json.load(open('data/obra.json'))
CAN, TL, R = D['canales'], D['timeline'], D['resumen']
R['medido_el'] = D['medido_el']

CASAS = [('TheSoul','#2B3A67','TheSoul Publishing','2015 – 2016'),
         ('Bored Panda','#A8432B','Bored Panda','2019 – 2023'),
         ('Hype On Media','#1F5F4B','Hype On Media','2024 – hoy')]
COLOR = {k:c for k,c,_,_ in CASAS}

def esc(s): return html.escape(str(s))

# ── GRÁFICO 1 · EL LIBRO DE CADENCIA ────────────────────────────────────────
def libro():
    maxc = max(c['porMes'] for c in CAN)
    ANCHO, FILA = 760, 26
    out, y = [], 0
    for casa, col, nom, periodo in CASAS:
        fs = [c for c in CAN if c['casa']==casa]
        if not fs: continue
        sub = sum(c['porMes'] for c in fs)
        out.append(f'<text x="0" y="{y+11}" class="casa" fill="{col}">{esc(nom)}</text>'
                   f'<text x="196" y="{y+11}" class="casa-meta">{periodo} · {len(fs)} canales</text>'
                   f'<text x="{ANCHO}" y="{y+11}" class="casa-sum" fill="{col}" text-anchor="end">{sub:,.0f} / mes</text>'
                   f'<line x1="0" y1="{y+20}" x2="{ANCHO}" y2="{y+20}" class="regla"/>')
        y += 32
        for c in fs:
            w = (c['porMes']/maxc) * 404
            out.append(
              f'<text x="0" y="{y+12}" class="can">{esc(c["titulo"][:30])}</text>'
              f'<text x="196" y="{y+12}" class="rol">{esc(c["rol"][:40])}</text>'
              f'<rect x="438" y="{y+3}" width="{w:.1f}" height="12" fill="{col}" opacity=".82"/>'
              f'<text x="{ANCHO}" y="{y+12}" class="cifra" text-anchor="end">{c["porMes"]:.0f}</text>')
            y += FILA
        y += 14
    tot = R['cadencia_mes_total']
    out.append(f'<line x1="0" y1="{y}" x2="{ANCHO}" y2="{y}" class="regla-gorda"/>'
               f'<text x="0" y="{y+26}" class="total">Vídeos publicados al mes, solo YouTube</text>'
               f'<text x="{ANCHO}" y="{y+28}" class="total-n" text-anchor="end">{tot:,}</text>')
    return f'<svg viewBox="0 0 {ANCHO} {y+44}" class="g" role="img" aria-label="Cadencia medida de 39 canales">{"".join(out)}</svg>'

# ── GRÁFICO 2 · LA DÉCADA ───────────────────────────────────────────────────
def decada():
    W, H, PAD = 760, 190, 22
    mx = max(sum(m[k] for k in COLOR) for m in TL)
    bw = W/len(TL)
    out = []
    for i, m in enumerate(TL):
        x, acc = i*bw, 0
        for casa in ('TheSoul','Bored Panda','Hype On Media'):
            v = m.get(casa,0)
            if not v: continue
            hh = (v/mx)*(H-PAD)
            out.append(f'<rect x="{x:.2f}" y="{H-PAD-acc-hh:.2f}" width="{bw*0.82:.2f}" height="{hh:.2f}" fill="{COLOR[casa]}"/>')
            acc += hh
    out.append(f'<line x1="0" y1="{H-PAD}" x2="{W}" y2="{H-PAD}" class="regla"/>')
    for i, m in enumerate(TL):
        if m['mes'].endswith('-01'):
            out.append(f'<text x="{i*bw:.1f}" y="{H-6}" class="eje">{m["mes"][:4]}</text>')
    return f'<svg viewBox="0 0 {W} {H}" class="g" role="img" aria-label="Piezas publicadas por mes, 2017 a 2026">{"".join(out)}</svg>'

PAGINA = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Operaciones — Julian Rinta</title><meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
<style>
:root{{--papel:#FBFAF7;--tinta:#16140F;--suave:#6C6659;--regla:#E2DED5;
 --soul:#2B3A67;--panda:#A8432B;--hom:#1F5F4B;
 --d:'Fraunces',Georgia,serif;--t:'Satoshi',system-ui,sans-serif;--m:'JetBrains Mono',monospace}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--papel);color:var(--tinta);font-family:var(--t);font-size:17px;line-height:1.55;
 -webkit-font-smoothing:antialiased}}
.w{{max-width:860px;margin:0 auto;padding:0 clamp(20px,4vw,50px)}}
.marca{{padding:clamp(40px,6vw,76px) 0 0;font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--suave)}}
h1{{font-family:var(--d);font-weight:600;font-size:clamp(44px,7.4vw,86px);line-height:.94;
 letter-spacing:-.025em;margin:18px 0 0;max-width:13ch}}
.bajada{{margin-top:22px;max-width:60ch;font-size:clamp(19px,2.1vw,22px);line-height:1.45;color:#38342C}}
.bajada b{{font-weight:700;color:var(--tinta)}}
.cap{{margin-top:12px;font-family:var(--m);font-size:12.5px;color:var(--suave);letter-spacing:.01em}}
section{{margin-top:clamp(56px,8vw,96px)}}
h2{{font-family:var(--d);font-weight:600;font-size:clamp(27px,3.4vw,38px);letter-spacing:-.02em;line-height:1.08}}
.pre{{font-family:var(--m);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--suave);margin-bottom:10px}}
.dice{{margin-top:14px;max-width:62ch;color:#38342C}}
.g{{width:100%;height:auto;margin-top:30px;display:block}}
.casa{{font-family:var(--d);font-size:15.5px;font-weight:600}}
.casa-meta,.rol{{font-family:var(--t);font-size:11.5px;fill:#8C8578}}
.casa-sum{{font-family:var(--m);font-size:12.5px;font-weight:500}}
.can{{font-family:var(--t);font-size:13px;fill:var(--tinta)}}
.cifra{{font-family:var(--m);font-size:13px;fill:var(--tinta)}}
.regla{{stroke:var(--regla);stroke-width:1}} .regla-gorda{{stroke:var(--tinta);stroke-width:1.5}}
.total{{font-family:var(--t);font-size:14px;font-weight:700;fill:var(--tinta)}}
.total-n{{font-family:var(--m);font-size:26px;font-weight:500;fill:var(--tinta)}}
.eje{{font-family:var(--m);font-size:10.5px;fill:#9A9385}}
.cifras{{display:grid;grid-template-columns:repeat(auto-fit,minmax(176px,1fr));gap:1px;background:var(--regla);
 border:1px solid var(--regla);margin-top:34px}}
.cifras div{{background:var(--papel);padding:22px 20px}}
.cifras b{{display:block;font-family:var(--d);font-size:clamp(31px,4.4vw,44px);font-weight:600;
 letter-spacing:-.03em;line-height:1}}
.cifras span{{display:block;margin-top:9px;font-size:13.5px;color:var(--suave);line-height:1.4}}
.leyenda{{display:flex;gap:22px;flex-wrap:wrap;margin-top:18px;font-family:var(--m);font-size:12px;color:var(--suave)}}
.leyenda i{{display:inline-block;width:9px;height:9px;margin-right:7px}}
footer{{margin:clamp(60px,8vw,100px) 0 70px;padding-top:22px;border-top:1px solid var(--regla);
 font-size:13px;color:var(--suave);max-width:72ch}}
@media(max-width:620px){{.g{{overflow-x:auto}}}}
</style></head>
<body><div class="w">

<p class="marca">Julian Rinta · Operaciones</p>
<h1>Tres operaciones construidas desde cero.</h1>
<p class="bajada">Equipos de <b>80 a 100 personas</b> en varios países, uno de <b>más de 100</b>,
 y la maquinaria que los hizo publicar todos los días durante una década.</p>
<p class="cap">Medido el {R['medido_el']} · {R['canales']} canales con rol declarado · {R['piezas_fechadas']:,} piezas fechadas</p>

<section>
 <p class="pre">El volumen</p>
 <h2>Lo que una operación produce no se dice: se cuenta.</h2>
 <p class="dice">Cada barra es la cadencia medida de un canal: sus vídeos publicados dividido entre
  los meses que lleva vivo. No es una estimación ni una cifra de folleto. Es lo que hay en YouTube hoy.</p>
 {libro()}
 <p class="cap">Y esto es solo YouTube. La red de Bored Panda sumaba además 70+ páginas de Facebook
  publicando a diario, en 15+ idiomas.</p>
</section>

<section>
 <p class="pre">La década</p>
 <h2>Una casa detrás de otra, sin que la máquina parara.</h2>
 <p class="dice">Piezas publicadas por mes entre enero de 2017 y noviembre de 2026, con su casa.
  La forma del gráfico es el relevo: cuando una operación madura, la siguiente ya está arrancando.</p>
 {decada()}
 <div class="leyenda">
  <span><i style="background:var(--soul)"></i>TheSoul Publishing</span>
  <span><i style="background:var(--panda)"></i>Bored Panda</span>
  <span><i style="background:var(--hom)"></i>Hype On Media</span>
 </div>
</section>

<section>
 <p class="pre">El dinero y la gente</p>
 <h2>Lo que distingue a un director de operaciones de un coordinador.</h2>
 <div class="cifras">
  <div><b>~$2,5M</b><span>al año, el P&amp;L independiente de la unidad de Bored Panda</span></div>
  <div><b>$80&ndash;150K</b><span>al mes de presupuesto operativo: producción, talento y marketing</span></div>
  <div><b>70%</b><span>de recorte de coste operativo en Bored Panda, 2022: de $80K a $25K al mes</span></div>
  <div><b>100+</b><span>personas en el equipo multinacional construido desde cero en TheSoul</span></div>
  <div><b>80&ndash;100</b><span>personas dirigidas en Bored Panda, por sus gerentes de operaciones</span></div>
  <div><b>{R['paises']}</b><span>países con canal propio en la red medida</span></div>
 </div>
 <p class="cap">El recorte de 2022 rediseñó el pipeline con IA, un año antes de que ChatGPT fuera
  público. No fue recortar producción: fue producir igual por menos.</p>
</section>

<footer>Las cifras de cadencia y de reparto salen de los datos públicos de YouTube medidos el
 {R['medido_el']} sobre {R['canales']} canales con rol declarado, y de {R['piezas_fechadas']:,} piezas con fecha de
 publicación entre {R['rango'][0]} y {R['rango'][1]}. Las cifras de dinero y de equipo provienen del expediente.
 La atribución sigue el registro: construido, dirigido o hecho crecer, nunca fundado.</footer>

</div></body></html>"""

open('operaciones.html','w').write(PAGINA)
print(f"operaciones.html · {len(PAGINA):,} bytes · {R['canales']} canales · {len(TL)} meses")
