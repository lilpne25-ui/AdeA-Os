# AI Engineering Cell — piloto de 90 días
Propuesta organizacional hipotética, no nombramiento ni autorización. En este repositorio público se usan roles, no nombres de empleados ni detalles de tickets. Objetivo: crear una célula transversal de ingeniería Python e IA con capacidad protegida y supervisión del responsable de sistemas.

## Mandato y estructura
Patrocinador/gerente: aprueba personas, reasignación de tickets, presupuesto, accesos, alcance y puertas; conserva responsabilidad por SLAs. Líder técnico propuesto (solicitante): selecciona candidatos con gerente, dirige backlog, arquitectura, formación, revisiones, métricas y demo semanal. Dos ingenieros candidatos: (1) Python, extracción, SGCI y RAG; (2) Python/APIs, Element, QA e integraciones. Especialistas SGCI, seguridad y operaciones aportan conocimiento y validación puntual. No desplazar unilateralmente personas ni abandonar incidencias; acuerdo de transición y respaldo operativo.

## Capacidad y delegación
Piloto preferido: líder 20 h/semana + 2 ingenieros x 20 h = 60 h/semana agregadas, 720 h en 12 semanas; reservar 20% (144 h) para coordinación, formación, revisión, imprevistos, dejando 576 h de ejecución, no promesa de entrega. Alternativa mínima: líder 10 h + 1 ingeniero 10 h = 20 h/semana, 240 h/12 semanas antes de reserva (192 h ejecución). Alternativa intensiva: liberar 2 ingenieros a 30 h cada uno y líder 30 h, 90 h/semana, solo si el área puede absorber carga. Estas horas son ejemplos, no capacidad medida.
Coste de oportunidad ilustrativo a MXN 300/h: mínima 72,000, preferida 216,000, intensiva 324,000 por 12 semanas, antes de infraestructura. No sumar estos valores nuevamente a las horas de los planes A/B/C: recalcular según alcance y capacidad. A USD 50/mes, solo usar asientos personales autorizados disponibles; no compartir cuentas. Integrantes sin asiento pueden programar localmente, revisar, usar material formativo y pruebas sintéticas. Priorizar un desarrollador con asiento si ya está asignado; verificar licencias antes de ampliar.

## Protocolo de tickets
1. Medir dos semanas de volumen, horas, severidad, SLA, pendientes y competencias de respaldo (no vigilancia individual). Clasificar P1/P2 críticos, P3/P4 rutinarios, proyectos.
2. Gerente elige candidatos y acuerda transferencia; cada ticket abierto tiene propietario, respaldo, fecha, documentación y aceptación. Transferir solo cuando el receptor tenga capacidad. No simplemente redistribuir sobrecarga.
3. Proteger bloques de tiempo en agenda y excluir a la célula de nuevas asignaciones rutinarias durante bloques. Mantener guardia crítica rotativa, definida por el gerente, con escalamiento y capacidad de reemplazo. Revisar demanda semanal.
4. Umbral orientativo: capacidad de tickets retirada = horas protegidas menos capacidad ociosa real; si faltan horas, reducir alcance, automatizar tickets repetitivos previamente validados o ampliar soporte. Si empeoran SLAs críticos, pausar/reasignar temporalmente.
5. Backlog separado, máximo 2 tareas activas por ingeniero, revisión semanal y demo quincenal. Toda tarea: objetivo, entradas autorizadas, entregable, pruebas, estimación, propietario, dependencias, aprobación.

## Selección transparente y transición Python
Candidatos voluntarios/evaluados por evidencia laboral relevante, no edad ni características personales. Ejercicio de 60–90 min con dataset sintético: leer archivos, manejar errores, tests pytest, Git y explicar decisiones. Valorar fundamentos (30%), resolución y pruebas (25%), conocimiento de negocio (20%), aprendizaje y colaboración (15%), seguridad (10%). Usar rúbrica como apoyo a decisión humana, no selección automatizada. Conservar Java como competencia; Python para automatización/IA si estándar interno autoriza. Mentoría, pair programming, revisión de código y documentación.
Stack inicial: Python aprobado, venv, pytest, Ruff, mypy opcional, SQLite, Git, Tika/Docling local. No construir agentes autónomos en producción. Mantener RAG y REA sujetos a autorización.

## Plan 90 días
Semanas 1–2: capacidad, autorización SGCI, benchmark sintético, Academy fundamentos y primer Skill. Semanas 3–4: scanner de metadatos, pruebas y benchmark autorizado; demo. Semanas 5–8: inventario por lotes, extracción autorizada y primer mapa de core; prototipo documental. Semanas 9–12: validar reglas prioritarias, hipótesis de cuellos, informe de cobertura, demo Element sandbox solo si capacidad; decidir AutoRAG y ampliación. No comprometer cobertura total en 90 días hasta conocer volumen y accesos.
Puertas: cero cambios al origen; trazabilidad y cobertura reconciliada; calidad de extracción; evaluación por especialistas; tickets críticos sin degradación atribuible; productividad y costes comparables. Informar resultados semanales, bloqueos y consumo. No presentar estimaciones como hechos.

## Preguntas pendientes para el líder y gerente
- ¿Cuántos integrantes tiene el equipo actual y qué perfiles/tecnologías dominan?
- ¿Cuántos tickets por semana, horas y SLAs por prioridad existen? ¿Quién absorbe la carga liberada?
- ¿Puede reservarse 20 h/semana al líder y a dos colaboradores? ¿O dedicación completa de seleccionados?
- ¿Qué candidatos están interesados en Python/IA? ¿Quién valida su disponibilidad y conocimientos?
- ¿Qué suscripciones exactas cubren USD 50, a quién están asignadas y qué restricciones de datos/API existen?
- ¿Qué hardware, permisos, repositorios, estándar Python/Java y fuentes SGCI están autorizados?
- ¿Qué resultados espera el patrocinador a 30, 60 y 90 días? ¿Quién aprueba gastos, seguridad y cambios?
