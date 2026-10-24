# Arma fuente/Index.html (el armazon de LAFFORT) a partir del Index v10 de Empresa Ejemplo.
# Cada cambio exige encontrar su ancla EXACTAMENTE la cantidad de veces indicada: si no, aborta
# y no escribe nada (regla de DISSAN: un replace que no encuentra el ancla deja creer que se aplico).
import sys
s = open('fuente/Index.empresa_ejemplo_v10.html', encoding='utf-8').read()
def r(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: sys.exit('ANCLA %d veces (se esperaban %d): %r' % (c, n, a[:90]))
    s = s.replace(a, b)

# ---------- cabecera ----------
r('<head>\n  <base target="_top">\n  <meta charset="UTF-8">',
  '<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>Laffort · Sistema de Gestión</title>\n  <link rel="icon" href="data:,">')

# ---------- estilos ----------
r("    * { box-sizing:border-box; margin:0; padding:0; }",
  "    /* DISSAN: un display: del CSS le gana al atributo hidden. Esta regla va PRIMERO. */\n    [hidden] { display:none !important; }\n    * { box-sizing:border-box; margin:0; padding:0; }")
r("""    @media (max-width: 760px) {
      #shell { flex-direction:column; }
      #sidebar { width:100%; padding:14px 0; }
      nav { display:flex; flex-wrap:wrap; gap:4px; }
      .nav-item { margin:0; }
      #topbar { padding:0 16px; }
      #contenido { padding:16px; }
      #fechaHoy { display:none; }
    }""",
"""    /* ---------- Bajar a Excel y PDF (de DISSAN): la barra que js/bajar.js pone sobre toda tabla ---------- */
    .bajar-barra { display:flex; gap:7px; justify-content:flex-end; margin:10px 0 6px; }
    .bajar-btn { display:inline-flex; align-items:center; gap:6px; background:transparent; color:var(--gray); border:1px solid var(--border); border-radius:7px; padding:5px 11px; font:500 11.5px/1 Inter,sans-serif; cursor:pointer; }
    .bajar-btn:hover:not(:disabled) { color:var(--off-white); border-color:var(--green); background:rgba(8,165,122,.10); }
    .bajar-btn:disabled { opacity:.55; cursor:default; }
    .bajar-btn svg { width:13px; height:13px; flex:none; }
    @media print { .bajar-barra { display:none !important; } }

    /* ---------- Estado de los datos y avisos de modulo ---------- */
    .estado-datos td.num { text-align:right; }
    .aviso-modulo { background:rgba(224,162,59,.10); border:1px solid rgba(224,162,59,.35); color:var(--amber); border-radius:10px; padding:14px 16px; margin-bottom:16px; font-size:13px; line-height:1.5; }

    /* ---------- Celular y tablet (de DISSAN): hasta 900 px el menu sale del flujo y se abre con un boton ---------- */
    #btnMenu { display:none; background:transparent; border:1px solid var(--border); color:var(--off-white); border-radius:8px; width:38px; height:38px; flex:none; align-items:center; justify-content:center; cursor:pointer; margin-right:10px; }
    #btnMenu svg { width:19px; height:19px; }
    #tapaMenu { display:none; }
    @media (max-width: 900px) {
      #btnMenu { display:inline-flex; }
      #sidebar { position:fixed; top:0; bottom:0; left:0; z-index:60; width:252px; max-width:84vw; transform:translateX(-100%); transition:transform .22s ease; overflow-y:auto; }
      body.menu-abierto #sidebar { transform:translateX(0); box-shadow:0 0 40px rgba(0,0,0,.5); }
      #tapaMenu { display:block; position:fixed; inset:0; z-index:55; background:rgba(4,16,27,.62); opacity:0; pointer-events:none; transition:opacity .22s ease; }
      body.menu-abierto #tapaMenu { opacity:1; pointer-events:auto; }
      body.menu-abierto { overflow:hidden; }
      #areaContenido { width:100%; }
      #topbar { height:56px; padding:0 12px; gap:8px; }
      #tituloModulo { font-size:15px; min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; flex:1; }
      #contenido { padding:16px 12px 44px; }
      .tabla-scroll { overflow-x:auto; -webkit-overflow-scrolling:touch; }
      .tabla-scroll > table { min-width:max-content; }
      .bajar-barra { justify-content:flex-start; }
      #btnImprimir span.txt { display:none; }
    }
    @media (max-width: 480px) { #fechaHoy { display:none; } }""")

# ---------- textos ----------
r('<div class="login-titulo">Ingresar a Empresa Ejemplo</div>', '<div class="login-titulo">Ingresar a Laffort</div>')
r('<div class="t2" style="margin-top:8px">Empresa Ejemplo</div>', '<div class="t2" style="margin-top:8px">Laffort · Sistema de Gestión</div>')
r('<b>Empresa Ejemplo · Sistema de Gestión</b>', '<b>Laffort · Sistema de Gestión</b>')
r('<div id="topbar"><div id="tituloModulo">Radar · Tablero central</div>', '<div id="topbar"><div id="tituloModulo">Radar · Tablero central</div>')
r('</svg>Imprimir / PDF</button>', '</svg><span class="txt">Imprimir / PDF</span></button>')

# ---------- tablero: estado de los datos de Tango (cuantas tablas de cada modulo estan cargadas) ----------
r("""            <div class="pie-dato">Fuente: función <code>api_fecha_corte_v2</code>, leída en vivo con tu usuario.</div>
          </div>""",
"""            <div class="pie-dato">Fuente: función <code>api_fecha_corte_v2</code>, leída en vivo con tu usuario.</div>
          </div>
          <div class="panel">
            <h3>Tablas de Tango cargadas, por módulo</h3>
            <div class="tabla-scroll"><table class="estado-datos">
              <thead><tr><th>Módulo</th><th class="num">Tablas cargadas</th><th class="num">Filas</th><th>Faltan</th></tr></thead>
              <tbody id="tablaEstadoDatos"><tr><td colspan="4" class="gris">Cargando…</td></tr></tbody>
            </table></div>
            <div class="pie-dato">Fuente: función <code>api_estado_datos_v2</code>. Un módulo sin sus tablas no puede mostrar datos: lo dice acá y en su pantalla, en vez de dar error.</div>
          </div>""")

# ---------- Seguridad: alta, email y contraseña desde el panel (Edge Function usuarios) ----------
r("""            <h3>Usuarios <button class="btn secundario chico" id="btnRecargarUsuarios">Actualizar</button></h3>
            <div class="mensaje info" style="margin:0 0 14px">Alta de usuarios: en Supabase → Authentication → Users → <b>Add user</b>. El usuario aparece acá <b>inactivo</b> hasta que lo actives y le asignes el rol.</div>""",
"""            <h3>Usuarios <span style="display:flex;gap:8px"><button class="btn chico" id="btnNuevoUsuario" type="button">Nuevo usuario</button><button class="btn secundario chico" id="btnRecargarUsuarios" type="button">Actualizar</button></span></h3>
            <div class="mensaje info" style="margin:0 0 14px">Roles: <b>super</b> (todo, incluido usuarios), <b>admin</b> (todos los módulos y sueldos), <b>usuario</b> (gestión, sin sueldos ni usuarios). Las reglas las controla la base: nadie se saca el rol a sí mismo y siempre queda un super activo. Cada cambio queda en la bitácora.</div>""")

r("""<!-- Ventana: mi contraseña -->""",
"""<!-- Ventana: nuevo usuario -->
<div class="fondo-modal oculto" id="modalNuevo">
  <form class="modal" id="formNuevo" autocomplete="off">
    <h4>Nuevo usuario</h4><div class="gris">La contraseña: mínimo 12 caracteres. Se la pasás a la persona por un canal seguro.</div>
    <label for="nuevoNombre">Nombre</label><input type="text" id="nuevoNombre" required maxlength="80">
    <label for="nuevoEmail">Email</label><input type="email" id="nuevoEmail" required autocomplete="off">
    <label for="nuevoClave">Contraseña</label><input type="password" id="nuevoClave" required minlength="12" autocomplete="new-password">
    <label for="nuevoRol">Rol</label>
    <select id="nuevoRol"><option value="usuario">Usuario</option><option value="admin">Admin</option><option value="super">Super (administra usuarios)</option></select>
    <label class="check"><input type="checkbox" id="nuevoActivo" checked> Activo (puede ingresar)</label>
    <div id="nuevoMensaje" class="mensaje oculto"></div>
    <div class="acciones"><button type="button" class="btn secundario" data-cerrar="modalNuevo">Cancelar</button><button class="btn" id="btnCrearUsuario" type="submit">Crear</button></div>
  </form>
</div>

<!-- Ventana: email o contraseña de otro usuario -->
<div class="fondo-modal oculto" id="modalAcceso">
  <form class="modal" id="formAcceso" autocomplete="off">
    <h4 id="accesoTitulo">Cambiar acceso</h4><div class="gris" id="accesoQuien"></div>
    <label for="accesoEmail">Email nuevo (dejar vacío para no cambiarlo)</label><input type="email" id="accesoEmail" autocomplete="off">
    <label for="accesoClave">Contraseña nueva (dejar vacío para no cambiarla · mínimo 12)</label><input type="password" id="accesoClave" autocomplete="new-password">
    <div id="accesoMensaje" class="mensaje oculto"></div>
    <div class="acciones"><button type="button" class="btn secundario" data-cerrar="modalAcceso">Cancelar</button><button class="btn" id="btnGuardarAcceso" type="submit">Guardar</button></div>
  </form>
</div>

<!-- Ventana: mi contraseña -->""")

r('<h4>Cambiar mi contraseña</h4><div class="gris">Mínimo 8 caracteres.</div>', '<h4>Cambiar mi contraseña</h4><div class="gris">Mínimo 12 caracteres.</div>')
r('<input type="password" id="clave1" autocomplete="new-password" minlength="8" required>', '<input type="password" id="clave1" autocomplete="new-password" minlength="12" required>')
r('<input type="password" id="clave2" autocomplete="new-password" minlength="8" required>', '<input type="password" id="clave2" autocomplete="new-password" minlength="12" required>')

# ---------- script: configuracion y conexion ----------
r("""  var CFG = <?!= cfg ?>;
  var sb = null;      // cliente de Supabase con la sesion de ESTE usuario
  var YO = null;      // mi perfil""",
"""  // LAFFORT: la pagina es publica (GitHub Pages). Aca va SOLO la clave publicable, hecha para estar a la vista:
  // lo que protege los datos es el ingreso de cada usuario y los permisos de la base. La clave de servicio nunca va aca.
  var CFG = { url: 'https://xgwkaqrgbdzzjmuouexr.supabase.co', clave: 'sb_publishable_5SvsfeUJnRCxDPPsIcqL-w_q8STrMB0', aviso: '' };
  if (window.CFG_PRUEBA) CFG = window.CFG_PRUEBA;   // solo el banco de pruebas local lo define
  var sb = null;      // cliente de Supabase con la sesion de ESTE usuario
  var YO = null;      // mi perfil
  var MODS = {};      // modulos que este usuario puede ver (api_mis_modulos): el portero de la pantalla""")

r("""  function textoError(e) {
    var m = (e && (e.message || e.error_description)) || String(e);
    if (/Acceso denegado/.test(m)) return 'Tu usuario no está activo.';
    if (/No autorizado/.test(m)) return 'No tenés permiso para esto.';
    return m; }""",
"""  function textoError(e) {
    var m = (e && (e.message || e.error_description)) || String(e);
    if (/Acceso denegado/.test(m)) return 'Tu usuario no está activo.';
    if (/No autorizado/.test(m)) return 'No tenés permiso para esto.';
    var t = /relation "?(?:public\\.)?([a-z0-9_]+)"? does not exist/i.exec(m);
    if (t) return 'Todavía no están cargados los datos de Tango que usa esta pantalla (falta la tabla ' + t[1] + '). Ver "Tablas de Tango cargadas" en el Radar.';
    if (/statement timeout|canceling statement/i.test(m)) return 'La consulta tardó demasiado y el servidor la cortó. Probá con un período más corto o avisá a EMA.';
    if (/JWT expired|invalid JWT/i.test(m)) return 'La sesión venció. Volvé a ingresar.';
    if (/Failed to fetch|NetworkError/i.test(m)) return 'Sin conexión con el servidor.';
    return m; }""")

r("""    sb = window.supabase.createClient(CFG.url, CFG.clave, { auth: { storage: almacen(), persistSession: true, autoRefreshToken: true, detectSessionInUrl: false } });""",
"""    sb = window.supabase.createClient(CFG.url, CFG.clave, { auth: { storage: almacen(), persistSession: true, autoRefreshToken: true, detectSessionInUrl: false } });
    controlarFilasCortadas(sb);""")

r("""  // ---------- arranque ----------""",
"""  // ---------- control de resultados cortados ----------
  // La API de Supabase devuelve como maximo N filas por pedido (1.000 de fabrica). En Empresa Ejemplo eso corto Legajos
  // en silencio (mostraba solo 2013). Aca, si una respuesta trae un multiplo exacto de 1.000 filas, se le pregunta a la
  // base cuantas hay de verdad; si hay mas, la pantalla muestra un ERROR en vez de una cifra incompleta.
  function controlarFilasCortadas(cli) {
    var original = cli.rpc.bind(cli);
    cli.rpc = function (fn, args, opciones) {
      if (opciones) return original(fn, args, opciones);
      return Promise.resolve(original(fn, args)).then(function (r) {
        if (r && !r.error && Array.isArray(r.data) && r.data.length > 0 && r.data.length % 1000 === 0) {
          return Promise.resolve(original(fn, args, { count: 'exact', head: true })).then(function (c) {
            if (c && !c.error && c.count != null && c.count > r.data.length)
              return { data: null, error: { message: 'Resultado incompleto: ' + fn + ' trajo ' + r.data.length + ' de ' + c.count + ' filas porque el servidor corta las respuestas largas. No se muestra una cifra incompleta. Avisar a EMA.' } };
            return r;
          });
        }
        return r;
      });
    };
  }

  // ---------- menu de celular (de DISSAN) ----------
  function armarBotonMenu() {
    if ($('btnMenu')) return;
    var b = document.createElement('button'); b.id = 'btnMenu'; b.type = 'button';
    b.setAttribute('aria-label', 'Abrir el menú'); b.setAttribute('aria-expanded', 'false');
    b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>';
    $('topbar').insertBefore(b, $('topbar').firstChild);
    var tapa = document.createElement('div'); tapa.id = 'tapaMenu'; document.body.appendChild(tapa);
    function abrir(si) { document.body.classList.toggle('menu-abierto', si); b.setAttribute('aria-expanded', si ? 'true' : 'false'); b.setAttribute('aria-label', si ? 'Cerrar el menú' : 'Abrir el menú'); }
    b.addEventListener('click', function () { abrir(!document.body.classList.contains('menu-abierto')); });
    tapa.addEventListener('click', function () { abrir(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') abrir(false); });
    $('menu').addEventListener('click', function (e) { if (e.target.closest('.nav-item')) abrir(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 900) abrir(false); });
  }

  // ---------- arranque ----------""")

r("""  function iniciar() {
    $('fechaHoy').textContent""", """  function iniciar() {
    armarBotonMenu();
    $('fechaHoy').textContent""")

r("""    if (!CFG.url || !CFG.clave) { mostrarLogin('Falta configurar la conexión: cargar SUPABASE_URL y SUPABASE_PUBLISHABLE_KEY en las Propiedades del Script.'); $('btnEntrar').disabled = true; return; }""",
"""    if (!CFG.url || !CFG.clave) { mostrarLogin('Falta configurar la conexión con la base.'); $('btnEntrar').disabled = true; return; }
    if (/^sb_secret_/i.test(CFG.clave) || /service_role/.test(CFG.clave)) { mostrarLogin('La página tiene cargada una clave SECRETA. Por seguridad no se usa.'); $('btnEntrar').disabled = true; return; }""")

# ---------- perfil + portero de modulos ----------
r("""  function cargarPerfil() {
    return sb.rpc('api_seg_yo').then(function (r) {
      if (r.error || !r.data || !r.data.length) {
        var t = r.error ? textoError(r.error) : 'No se encontró tu perfil.';
        return sb.auth.signOut().then(function () { mostrarLogin(t === 'Tu usuario no está activo.' ? 'Tu usuario todavía no está activo. Pedile a un administrador que lo active.' : t); });
      }
      YO = r.data[0];
      $('nombreUsuario').textContent = YO.nombre; $('rolUsuario').textContent = YO.rol;
      $('avatarInicial').textContent = (YO.nombre || '?').charAt(0).toUpperCase();
      mostrar('navSeguridad', YO.rol === 'super');
      mostrar('zonaLogin', false); mostrar('zonaApp', true);
      irA('Inicio');""",
"""  // El menu NO esta escrito para todos: sale de api_mis_modulos(), que cruza el rol del usuario con la tabla modulos
  // (de DISSAN). Encender o apagar una pantalla es una fila en la base. Y la base tampoco le da datos a quien no tiene el modulo.
  var CLAVE_MODULO = { Inicio: 'Radar' };
  function claveDe(modulo) { return CLAVE_MODULO[modulo] || modulo; }
  function puede(modulo) { return !!MODS[claveDe(modulo)]; }

  function cargarPerfil() {
    return Promise.all([sb.rpc('api_mi_perfil'), sb.rpc('api_mis_modulos')]).then(function (rr) {
      var r = rr[0], m = rr[1];
      if (r.error || !r.data || !r.data.length || !r.data[0].activo) {
        var t = r.error ? textoError(r.error) : (r.data && r.data.length ? 'Tu usuario no está activo.' : 'No se encontró tu perfil.');
        return sb.auth.signOut().then(function () { mostrarLogin(t === 'Tu usuario no está activo.' ? 'Tu usuario todavía no está activo. Pedile a un administrador que lo active.' : t); });
      }
      YO = r.data[0];
      MODS = {}; ((m && m.data) || []).forEach(function (x) { MODS[x.clave] = x; });
      document.querySelectorAll('#menu .nav-item').forEach(function (n) { n.classList.toggle('oculto', !puede(n.dataset.modulo)); });
      $('nombreUsuario').textContent = YO.nombre; $('rolUsuario').textContent = YO.rol;
      $('avatarInicial').textContent = (YO.nombre || '?').charAt(0).toUpperCase();
      mostrar('zonaLogin', false); mostrar('zonaApp', true);
      var primero = null;
      document.querySelectorAll('#menu .nav-item').forEach(function (n) { if (!primero && puede(n.dataset.modulo)) primero = n.dataset.modulo; });
      if (!primero) { document.querySelectorAll('.modulo').forEach(function (x) { x.classList.remove('visible'); }); $('tituloModulo').textContent = 'Sin módulos';
        var a = document.createElement('div'); a.className = 'aviso-modulo'; a.textContent = 'Tu usuario no tiene ningún módulo habilitado. Lo habilita un usuario super desde Seguridad.'; $('contenido').insertBefore(a, $('contenido').firstChild); return; }
      irA(primero);""")

r("""  function irA(modulo) {
    if (modulo === 'Seguridad' && (!YO || YO.rol !== 'super')) modulo = 'Inicio';""",
"""  function irA(modulo) {
    if (!puede(modulo)) return;   // el portero: un modulo que no tenes no se abre (y la base tampoco te da sus datos)""")

# ---------- tablero: estado de los datos ----------
r("""  function cargarInicio() {
    if (window.RADAR) window.RADAR.cargar();""",
"""  function cargarEstadoDatos() {
    var tb = $('tablaEstadoDatos'); tb.innerHTML = '<tr><td colspan="4" class="gris">Cargando…</td></tr>';
    sb.rpc('api_estado_datos_v2').then(function (r) {
      tb.innerHTML = '';
      if (r.error) { var tre = document.createElement('tr'); celda(tre, 'No se pudo leer: ' + textoError(r.error)).colSpan = 4; tb.appendChild(tre); return; }
      var porMod = {}, orden = [];
      (r.data || []).forEach(function (x) { if (!porMod[x.modulo]) { porMod[x.modulo] = { tot: 0, ok: 0, filas: 0, faltan: [] }; orden.push(x.modulo); }
        var p = porMod[x.modulo]; p.tot++; if (x.existe) { p.ok++; p.filas += Number(x.filas || 0); } else p.faltan.push(x.tabla); });
      orden.forEach(function (k) { var p = porMod[k], tr = document.createElement('tr');
        celda(tr, k); celda(tr, p.ok + ' de ' + p.tot, 'num'); celda(tr, p.filas.toLocaleString('es-AR'), 'num'); celda(tr, p.faltan.length ? p.faltan.join(', ') : '—', p.faltan.length ? '' : 'gris'); tb.appendChild(tr); });
    }).catch(function (e) { tb.innerHTML = ''; var tr = document.createElement('tr'); celda(tr, 'Error de conexión: ' + textoError(e)).colSpan = 4; tb.appendChild(tr); });
  }

  function cargarInicio() {
    cargarEstadoDatos();
    if (window.RADAR) window.RADAR.cargar();""")

# ---------- Seguridad: botones y llamadas a la Edge Function ----------
r("""        var td = celda(tr, ''); var b = document.createElement('button'); b.className = 'btn secundario chico'; b.textContent = 'Editar';
        b.addEventListener('click', function () { abrirEditar(u); }); td.appendChild(b);""",
"""        var td = celda(tr, ''); td.style.whiteSpace = 'nowrap'; var b = document.createElement('button'); b.className = 'btn secundario chico'; b.textContent = 'Editar';
        b.addEventListener('click', function () { abrirEditar(u); }); td.appendChild(b);
        var b2 = document.createElement('button'); b2.className = 'btn secundario chico'; b2.style.marginLeft = '6px'; b2.textContent = 'Email / clave';
        b2.addEventListener('click', function () { abrirAcceso(u); }); td.appendChild(b2);""")

r("""  // ---------- Mi contrasena ----------""",
"""  // La clave de servicio NO esta en esta pagina: crear usuarios y cambiar email o contraseña de otro lo hace la
  // Edge Function `usuarios`, con el token del usuario que pide (tiene que ser super activo).
  function llamarUsuarios(cuerpo) {
    return sb.auth.getSession().then(function (s) {
      var tok = s && s.data && s.data.session && s.data.session.access_token;
      if (!tok) throw new Error('La sesión venció. Volvé a ingresar.');
      return fetch(CFG.url + '/functions/v1/usuarios', { method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + tok, 'apikey': CFG.clave }, body: JSON.stringify(cuerpo) })
        .then(function (resp) { return resp.text().then(function (t) { var d = null; try { d = JSON.parse(t); } catch (e) { d = { ok: false, motivo: 'Respuesta ' + resp.status + ' de la función de usuarios.' }; } return d; }); });
    });
  }
  $('btnNuevoUsuario').addEventListener('click', function () { ['nuevoNombre', 'nuevoEmail', 'nuevoClave'].forEach(function (k) { $(k).value = ''; }); $('nuevoRol').value = 'usuario'; $('nuevoActivo').checked = true; limpiarAviso('nuevoMensaje'); mostrar('modalNuevo', true); });
  $('formNuevo').addEventListener('submit', function (ev) {
    ev.preventDefault();
    if ($('nuevoClave').value.length < 12) { aviso('nuevoMensaje', 'La contraseña tiene que tener al menos 12 caracteres.'); return; }
    $('btnCrearUsuario').disabled = true; limpiarAviso('nuevoMensaje');
    llamarUsuarios({ accion: 'crear', nombre: $('nuevoNombre').value, email: $('nuevoEmail').value, password: $('nuevoClave').value, rol: $('nuevoRol').value, activo: $('nuevoActivo').checked })
      .then(function (d) { $('nuevoClave').value = ''; if (!d || !d.ok) { aviso('nuevoMensaje', (d && d.motivo) || 'No se pudo crear.'); return; } mostrar('modalNuevo', false); cargarSeguridad(); })
      .catch(function (e) { aviso('nuevoMensaje', 'Error de conexión: ' + textoError(e)); })
      .then(function () { $('btnCrearUsuario').disabled = false; });
  });
  var accediendo = null;
  function abrirAcceso(u) { accediendo = u; $('accesoQuien').textContent = (u.nombre || '') + ' · ' + (u.email || ''); $('accesoEmail').value = ''; $('accesoClave').value = ''; limpiarAviso('accesoMensaje'); mostrar('modalAcceso', true); }
  $('formAcceso').addEventListener('submit', function (ev) {
    ev.preventDefault(); if (!accediendo) return;
    var em = $('accesoEmail').value.trim(), cl = $('accesoClave').value;
    if (!em && !cl) { aviso('accesoMensaje', 'No hay nada para cambiar.'); return; }
    if (cl && cl.length < 12) { aviso('accesoMensaje', 'La contraseña tiene que tener al menos 12 caracteres.'); return; }
    $('btnGuardarAcceso').disabled = true; limpiarAviso('accesoMensaje');
    var p = Promise.resolve({ ok: true });
    if (em) p = p.then(function (d) { return d.ok ? llamarUsuarios({ accion: 'email', id: accediendo.id, email: em }) : d; });
    if (cl) p = p.then(function (d) { return d.ok ? llamarUsuarios({ accion: 'password', id: accediendo.id, password: cl }) : d; });
    p.then(function (d) { $('accesoClave').value = ''; if (!d || !d.ok) { aviso('accesoMensaje', (d && d.motivo) || 'No se pudo guardar.'); return; } mostrar('modalAcceso', false); cargarSeguridad(); })
      .catch(function (e) { aviso('accesoMensaje', 'Error de conexión: ' + textoError(e)); })
      .then(function () { $('btnGuardarAcceso').disabled = false; });
  });

  // ---------- Mi contrasena ----------""")

r("""    if (a.length < 8) { aviso('claveMensaje', 'Tiene que tener al menos 8 caracteres.'); return; }""",
  """    if (a.length < 12) { aviso('claveMensaje', 'Tiene que tener al menos 12 caracteres.'); return; }""")

# ---------- bitacora: mostrar el detalle de las acciones nuevas ----------
r("""var det = d.despues ? ('rol ' + d.antes.rol + ' → ' + d.despues.rol + ', ' + (d.antes.activo ? 'activo' : 'inactivo') + ' → ' + (d.despues.activo ? 'activo' : 'inactivo')) : (d.email || '');""",
  """var det = d.despues && d.antes ? ('rol ' + d.antes.rol + ' → ' + d.despues.rol + ', ' + (d.antes.activo ? 'activo' : 'inactivo') + ' → ' + (d.despues.activo ? 'activo' : 'inactivo')) : (typeof d.despues === 'string' ? (d.antes + ' → ' + d.despues) : (d.email || ''));""")

# ---------- scripts de bajar a Excel/PDF ----------
r("""  iniciar();
</script>
</body>""", """  iniciar();
</script>
<script src="js/bajar-formatos.js?v=1"></script>
<script src="js/bajar.js?v=1"></script>
</body>""")

import re
resto = re.sub(r"<\?!= incluir_\('\w+'\); \?>", '', s)
assert '<?' not in resto, 'quedo un resto de plantilla de Apps Script'
open('fuente/Index.html', 'w', encoding='utf-8').write(s)
print('armazon OK', len(s))
