# Arma index.html (lo que publica GitHub Pages): el armazon fuente/Index.html con cada modulo de fuente/modulos/ adentro.
# Es el mismo metodo de Empresa Ejemplo (armar_publicado.py). Despues: python3 pruebas/ids_unicos.py
import re, hashlib
src = open('fuente/Index.html', encoding='utf-8').read()
out = re.sub(r"<\?!= incluir_\('(\w+)'\); \?>", lambda m: open('fuente/modulos/%s.html' % m.group(1), encoding='utf-8').read(), src)
assert 'incluir_(' not in out and '<?' not in out
open('index.html', 'w', encoding='utf-8').write(out)
print('index.html', len(out), 'bytes · sha256', hashlib.sha256(out.encode()).hexdigest()[:16])
