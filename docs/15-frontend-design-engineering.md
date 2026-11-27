# Frontend Design Engineering — v0.3.3
Objetivo: interfaces empresariales elegantes, rápidas y accesibles, que faciliten tareas reales. Inspiración Apple, no clonación de marcas, fuentes propietarias, logos o recursos. El diseño debe proteger datos y preservar funcionalidades. Este repositorio público contiene solo ejemplos sintéticos.

## Skills externas candidatas (evaluación, no instalación)
| Recurso | Uso recomendado | Referencia visual / fuente |
|---|---|---|
| Anthropic frontend-design | Dirección visual y primera implementación | https://github.com/anthropics/skills/tree/main/skills/frontend-design |
| Emil Kowalski apple-design | Interacción fluida, gestos, continuidad, feedback | https://github.com/emilkowalski/skills ; https://animations.dev/gallery |
| Emil Kowalski emil-design-eng | Refinamiento de componentes y movimiento | https://github.com/emilkowalski/skills |
| Impeccable | Crítica, auditoría, iteración y pulido | https://github.com/pbakaus/impeccable ; https://impeccable.style/gallery/ |
| UI/UX Pro Max | Selección de patrones, paletas, tipografía y arquitectura visual | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| Vercel web-design-guidelines | Revisión de accesibilidad, interacción y buenas prácticas | https://github.com/vercel-labs/web-interface-guidelines |
| Apple HIG | Principios de jerarquía, layout, materiales y tipografía | https://developer.apple.com/design/human-interface-guidelines/ |
| shadcn/ui | Componentes React reutilizables y ejemplos funcionales | https://ui.shadcn.com/examples/dashboard |
Fuentes públicas consultadas 26 nov 2026. Revisar licencias y código exacto, fijar commit, comprobar dependencias, hooks, egress y scripts antes de instalación en entorno de empresa. No ejecutar comandos de instalación automáticamente. Apple Design de Emil es una Skill comunitaria, no oficial de Apple. Las guías oficiales de Apple son referencia conceptual para web, no especificación web ni autorización de copiar activos.

## Pipeline recomendado con presupuesto limitado
1. Definir tarea, usuario, datos, restricciones, estado actual y criterios de aceptación; conservar reglas y flujos.
2. Elegir una dirección visual con frontend-design o UI/UX Pro Max, no activar ambas por defecto. Usar diseño propio de AdeA y componentes compartidos.
3. Implementar primero un flujo vertical con React/TypeScript, shadcn/ui y tokens CSS; sin backend inventado.
4. Aplicar apple-design/emil-design-eng solo donde ayude a entender estados, transiciones y feedback. Animaciones discretas, respetar prefers-reduced-motion.
5. Auditar con Impeccable o web-design-guidelines; Playwright y axe-core en local, teclado, foco, contraste WCAG 2.2 AA, viewport 360/768/1440, errores, carga, vacío, permisos, tablas grandes. No afirmar conformidad sin pruebas.
6. Capturar evidencia antes/después y medir éxito de tarea, tiempo, errores y rendimiento; revisión humana.
Con USD 50/mes, una Skill principal + auditoría puntual y herramientas locales; no ejecutar múltiples agentes visuales por defecto. Instalar externas únicamente tras revisión institucional. No enviar capturas privadas a proveedores sin aprobación.

## Direcciones visuales propuestas
A — Precision Light: inspirada en Apple, jerarquía editorial, superficies claras, acento azul, navegación estable, panel de detalle, espacio generoso. Preferida para analistas, Academy, documentos.
B — Operations Dark: consola operativa, fondo oscuro sobrio, datos tabulares, foco en incidencias y trazabilidad; no efectos neón decorativos.
C — Enterprise Compact: densidad controlada, filtros y tablas de alta productividad, columnas configurables, buena lectura a escala.
No son resultados de ejecutar Skills externas. Comparar con el prototipo sintético local en prototypes/frontend-lab/index.html.

## Sistema de diseño
Tokens: superficies, texto, borde, acento, semántica de estados, espaciado 4/8/12/16/24/32/48, radios 8/12/16, tipografía system-ui, escala de títulos, foco visible. Controles de al menos 24px con objetivos de 44px donde viable; navegación por teclado, contraste comprobado. Evitar cristal/transparencia sobre contenido crítico. Tablas con encabezados, filtros, paginación, estados de error y detalle; no depender de color para comunicar estado. Mostrar fuentes y fecha de corte, cobertura real, permisos, acciones auditables y etiquetas de simulación.
Stack objetivo: React, TypeScript, Tailwind o CSS tokens, shadcn/ui/Radix, Lucide, TanStack Table, React Flow, bpmn.io, Recharts o equivalente, Playwright, axe-core. No imponer todos los paquetes; evaluar licencias, accesibilidad y compatibilidad.

## Flujos prioritarios
1. SGCI: cobertura por raíz aprobada, extracción, errores, búsqueda y filtros, evidencia, versiones, detalle de reglas y aprobación.
2. Clientes y Element: solicitudes, timeline, responsables, SLA, actualizaciones autorizadas.
3. Agent Studio: Skills, herramientas, permisos, fuentes, pruebas, coste y trazabilidad.
4. Document Factory: borrador, citas, comparación, revisión, aprobación/exportación.
5. Modernización: matriz Java/PWA, reglas y casos de paridad.
6. Academy y ROI: progreso, credenciales, tiempo, costes y retorno con supuestos visibles.
Orden inicial: SGCI y documentación. Demo no implica integración real ni acceso a UNC. 
