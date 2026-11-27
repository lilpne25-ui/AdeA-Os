# Tres escenarios de inversión de IA y capacidad
Fecha de referencia de precios públicos: 26 noviembre 2026. USD antes de impuestos, tipo de cambio, consumo adicional e infraestructura. Confirmar contratación y elegibilidad. Se interpreta USD 50/mes como presupuesto actual, pendiente de confirmar. Estos niveles son licencias/consumo IA, distintos de los presupuestos de implementación A/B/C en 07-roadmap.md; no sumarlos sin reconciliar gastos ya contemplados.

## Nivel 1 — USD 50/mes (600/año)
Usar presupuesto ya aprobado: si es elegible y TI autoriza, 2 Team Standard a USD 25/mes cada uno, o mantener suscripción actual y utilizar solo saldo libre para API autorizada. No prometer que un presupuesto contratado puede reasignarse. Team permite 2–150 usuarios según página vigente. Cada usuario usa su cuenta; no compartir ni rotar credenciales para eludir límites. Dos Standard pueden aportar USD 40/mes en créditos API si se vincula la organización y cumplen condiciones. No se usan para extender Claude Code.
Alcance: escáner local, benchmark, inventario total por lotes, extracción y reglas locales, mapas preliminares, una demostración de generación documental y diseño de Element; un ingeniero y revisores puntuales. IA comercial solo con contenido sintético/desidentificado o autorizado. No garantizar análisis semántico profundo de todos los documentos ni fechas de cobertura.
Coste humano ilustrativo: 48 h iniciales x MXN 300 = 14,400; 100–180 h humanas para oleada de descubrimiento más amplia = 30–54 mil MXN, no necesariamente desembolso. Separar horas máquina y revisión.

## Nivel 2 — 20 usuarios Claude Team Standard
USD 500/mes, USD 6,000/año en modalidad mensual; anual USD 400/mes equivalente, USD 4,800/año comprometidos. Incremento mensual sobre 50: USD 450 (modalidad mensual). Claude Code incluido en cada asiento Team, límites de uso compartidos con otras funciones de Claude por usuario; no ilimitado. Créditos API elegibles: USD 400/mes agrupados, separados de Claude Code. No contratar anual hasta medir adopción. Capacitar por rol; primero 5 asientos si se justifica (USD 125/mes), luego ampliar a 20. Aplicaciones: desarrollo, pruebas, análisis de requerimientos, documentación, soporte técnico; los no desarrolladores pueden usar Claude sin necesidad de terminal.
Con responsable técnico y tiempo protegido: horizonte 2–4 meses para piloto A/B acotado; las cuentas no reemplazan validación humana ni recursos de infraestructura.

## Nivel 3 — inversión mayor justificada
20 usuarios mixtos: 18 Standard x 25 + 2 Premium x 125 = USD 700/mes (8,400/año); anual equivalente 18 x 20 + 2 x 100 = USD 560/mes, 6,720/año. Premium ofrece mayor uso, asignar solo a perfiles de carga demostrada. Créditos API elegibles: 18 x 20 + 2 x 100 = 560, limitados a USD 500/mes.
Propuesta de techo total IA/infra incremental USD 1,000–1,500/mes incluyendo USD 700 asientos + USD 300–800 para consumo API adicional, infraestructura, observabilidad y contingencia, sujeto a cotizaciones y evitando doble conteo de créditos. No comprometer gasto restante sin autorización. Si se requieren SCIM, auditoría, retención específica y controles empresariales, cotizar Enterprise (USD 20 por asiento/mes facturado anual, mínimo 20, más uso API según página oficial), no asumir que es más barato. Mantener presupuesto de implementación A/B/C separado.
Capacidad: equipo con horas reservadas para AutoRAG, agentes, Document Factory, Element, Academy, mapeo y PWA incremental. Horizonte 4–9 meses sujeto a puertas. No comprar GPU antes del benchmark.

## ROI de licencias, independiente del proyecto
Supuesto ilustrativo FX 18 MXN/USD (no tasa actual), coste empresarial 300 MXN/h, realización 60%, adopción 75%. Umbral bruto de horas productivas recuperables por usuario/mes = coste mensual MXN / (usuarios x coste/h x realización x adopción). Nivel 2: 500x18/(20x300x.6x.75) = 3.33 h por usuario/mes (~0.77 h/semana). Nivel 3 techo 1,000–1,500: 6.67–10 h/usuario/mes. Esto solo cubre suscripciones/techo operativo, no horas de implementación, impuestos ni costes de revisión.
Ejemplo: 20 usuarios x 2 h/semana x 4.33 x .75 x .6 x 300 = MXN 23,382/mes de valor realizado hipotético; coste de 20 asientos MXN 9,000/mes; diferencia 14,382 antes de otros costes. No es ahorro contable automático. Medir 4 semanas de uso: tareas comparables, calidad, tiempo hasta documento aprobado, tasa de adopción, consumo, retrabajo, seguridad; revisar con finanzas. Escalar cuando el valor observado cubra coste total y haya demanda; revisar trimestralmente y retirar licencias inactivas.
## Fuentes oficiales
- https://claude.com/pricing
- https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan
- https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers
- https://platform.claude.com/docs/en/build-with-claude/batch-processing (50% descuento API asíncrona, solo si autorizada)
- https://code.claude.com/docs/en/legal-and-compliance
