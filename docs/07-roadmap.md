# Roadmap e inversión — tres niveles
Estimaciones MXN, con horas internas valorizadas a 300 MXN/h como promedio ilustrativo. No son desembolsos necesariamente. Supone infraestructura existente y tiempo reservado. No incluye nuevos servidores GPU, migración masiva ni licencias especiales no cotizadas.

| | A | B | C |
|---|---:|---:|---:|
| Tiempo desde inicio | 8 semanas | 4 meses | 6–9 meses (modelo 7) |
| Horas totales presupuestadas | 240 | 600 | 1500 |
| Valor de horas | 72,000 | 180,000 | 450,000 |
| Otros costes/contingencia | 8,000 | 20,000 | 50,000 |
| Inicial | 80,000 | 200,000 | 500,000 |
| Operación mensual | 6,000 | 12,000 | 25,000 |
| Usuarios objetivo | 5–10 | 10–20 | 25–40 |
| Coste 12 meses | 152,000 | 344,000 | 800,000 |

El esfuerzo incluye ingeniería, transferencia, formación, seguridad y QA. Reservar capacidad: A ~30 h/semana agregadas; B ~35 h/semana; C ~49–50 h/semana en 7 meses (equipo, no una sola persona). Si faltan horas de especialistas o asistentes, ajustar alcance o presupuesto. Operación cubre licencias/consumo, alojamiento y mantenimiento según cotización real; acceso interactivo a Claude/Codex no presupone API incluida.

## A — Development & Connect (8 semanas)
1–2: diagnóstico, línea base, gobierno, herramientas y acceso. 3–4: cursos seleccionados, SDD y pruebas. 5: inventario/análisis legacy. 6: bot Element en laboratorio. 7: dos plantillas documentales. 8: demo, medición y decisión.
Distribución: ingeniería 42k, Element 12k, formación 9k, QA/seguridad 9k, configuración/contingencia 8k. Alcance: una aplicación, una integración, 5–10 usuarios, panel básico. No construir RAG completo.

## B — Knowledge & Automation (4 meses acumulados)
Meses 1–2: A. Mes 3: AutoRAG acotado, transferencia de hasta tres especialistas y agentes en lectura. Mes 4: 2–3 agentes, documentación, centro de control básico ampliado y PWA de módulo pequeño si existe capacidad. Priorizar AutoRAG/agente y aplazar PWA si los accesos o paridad no están listos.
Distribución: plataforma 54k, RAG 36k, agentes 24k, legacy/PWA 24k, integración 15k, formación 12k, QA/seguridad 15k, infraestructura/contingencia 20k. Aprobación incremental indicativa 120k.

## C — Enterprise Intelligence (6–9 meses acumulados)
Meses 1–4: A y B. Meses 5–6: ampliar frontend y permisos, grafo si necesario, minería con eventos, agentes adicionales y procesos. Mes 7: validación, adopción, operación y evaluación; extender a 9 meses si dependencias lo requieren.
Distribución: frontend 72k, backend 78k, RAG/grafo 72k, agentes 48k, legacy 60k, documentos/Academy 42k, minería 30k, QA/gobierno 48k, infraestructura/contingencia 50k. Aprobación adicional indicativa 300k.
Alcance: 5–8 agentes, hasta diez procesos y uno o dos módulos legacy acotados. No compromiso de producción sin pruebas.

## Puertas de decisión
A: línea base + piloto comparable, objetivo preliminar ≥20% menor tiempo en tareas seleccionadas, calidad no inferior, seguridad aprobada, coste registrado y canal cliente autorizado. B: recuperación con citas y permisos comprobados, agentes evaluados, documentación aprobada y paridad de módulo si se ejecuta. C: ROI recalculado con adopción y realización, soporte operativo y responsable por módulo. Detener, reducir o rediseñar si no se cumplen. Recalcular inversiones incrementales: reutilización completa no garantizada.
