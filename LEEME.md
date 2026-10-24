# Laffort · Sistema de Gestión — panel web

EMA Data Analytics · octubre 2026

Panel web del sistema de gestión de **Laffort** sobre Tango Gestión. Se publica con GitHub Pages
(`git push` y listo; `.nojekyll` en la raíz).

## De dónde sale

- **Módulos** (Radar, Ventas, Cobranzas, Compras, Stock, Tesorería, Legajos, Activo Fijo, IVA,
  Seguridad): los de *Empresa Ejemplo* versión 10, sin reescribir. Están en `fuente/modulos/`.
- **Plataforma** (página estática en GitHub, el navegador habla directo con Supabase, menú armado
  desde la tabla `modulos`, bajar a Excel y PDF en toda tabla, menú de celular): la del panel nuevo
  de *DISSAN*.

## Cómo se arma

```
python3 fuente/armar_shell.py   # arma fuente/Index.html desde el Index v10 de Empresa Ejemplo
python3 armar.py                # junta el armazón con los módulos -> index.html (lo que se publica)
```

## Seguridad

En esta página va **solo la clave publicable** de Supabase, hecha para estar a la vista. Lo que
protege los datos es el ingreso de cada usuario y los permisos de la base: cada función exige que
el usuario esté activo y tenga el módulo. La clave de servicio **nunca** va en este repositorio.

La base de datos, sus pruebas y la función de usuarios **no están acá**: están en la carpeta
privada del proyecto (SISTEMA LAFFORT).
