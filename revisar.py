#!/usr/bin/env python3
"""COMPUERTA (Julian, 2026-11-10): no se publica una imagen en su portafolio sin mirarla.
   Extrae TODO lo que index-v3.html referencia y monta hojas de contactos para revisarlas.
   Uso: python3 revisar.py   →  /tmp/rev_banners.jpg, /tmp/rev_avatares.jpg, /tmp/rev_minis.jpg"""
import re, os
from PIL import Image

t = open('index-v3.html').read()
srcs = re.findall(r'src="([^"]+\.jpg)"', t)
vistos, orden = set(), []
for s in srcs:
    if s not in vistos: vistos.add(s); orden.append(s)
grupos = {
 'banners'  : [s for s in orden if '/bn/' in s],
 'avatares' : [s for s in orden if '/av/' in s or '/ch/' in s],
 'minis'    : [s for s in orden if '/th' in s],
}
for nombre, paths in grupos.items():
    if not paths: continue
    if nombre=='banners':   W,H,C = 620, 92, 3
    elif nombre=='avatares':W,H,C = 120,120, 10
    else:                   W,H,C = 150, 85, 12
    filas=(len(paths)+C-1)//C; G=5
    hoja=Image.new('RGB',(C*(W+G)+G, filas*(H+G)+G),(251,250,247))
    faltan=[]
    for i,p in enumerate(paths):
        try:
            im=Image.open(p).convert('RGB'); im.thumbnail((W,H))
            hoja.paste(im,(G+(i%C)*(W+G), G+(i//C)*(H+G)))
        except Exception: faltan.append(p)
    hoja.save(f'/tmp/rev_{nombre}.jpg', quality=84)
    print(f"{nombre:9s} {len(paths):4d} imagenes -> /tmp/rev_{nombre}.jpg {hoja.size}"
          + (f"  ⚠ {len(faltan)} rotas: {faltan[:3]}" if faltan else ""))
