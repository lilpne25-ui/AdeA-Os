# People Intelligence, AutoRAG y agentes especializados
Capturar conocimiento profesional, no replicar identidad ni evaluar personas mediante vigilancia. Ejemplo: una especialista de análisis tecnológico aporta plantillas, decisiones, procedimientos, casos anonimizados y entrevistas consentidas. Su agente propone diagnósticos, matrices, preguntas y documentación; la especialista valida y conserva autoridad.

## Fuente inicial: SGI UNC
El [escaneo inicial de negocio](00-sgi-business-discovery.md) genera un catálogo privado de documentos y relaciones con procesos. Solo fuentes y versiones explícitamente aprobadas pasan a AutoRAG en el Plan B; conservar permisos efectivos y trazabilidad a doc_id, versión y ubicación autorizada. El inventario de metadatos no constituye autorización de indexación.

## Ciclo AutoRAG
1. Registrar fuente, finalidad, permiso, responsable y versión.
2. Extraer con Docling, clasificar y detectar datos sensibles/duplicados.
3. Segmentar y adjuntar metadatos, ACL y fecha; indexar texto y vectores.
4. Detectar contradicciones y fuentes caducadas; revisión humana para conocimiento nuevo.
5. Publicar versión aprobada; recuperar únicamente contenido permitido al usuario y cliente.
6. Responder con citas y abstenerse si falta evidencia. Registrar correcciones como propuestas, no aprendizaje automático sin revisión.
7. Propagar bajas, cambios de permisos y retención a índices y cachés; medir recuperación y calidad.

Fuentes: manuales, repositorios autorizados, plantillas, tickets, entrevistas y salas expresamente autorizadas. No copiar conversaciones indiscriminadamente. No enviar información confidencial a proveedores no aprobados.

## Agente por especialidad
Contrato: rol, alcance, conocimiento (RAG), procedimientos (Skills), herramientas (API/MCP), contexto de tarea, políticas y pruebas. Ejemplo: AI Business Analyst, Document Engineer y Legacy Engineer. Cada Skill registra entradas, pasos, salida, restricciones, evidencia y responsable. Herramientas de lectura por defecto; escrituras y acciones externas requieren aprobación.

## Process Intelligence y grafo
Inventario de actividades, roles responsables, entradas/salidas, frecuencia, excepciones, tiempos y sistemas. BPMN validado por el dueño del proceso. En C, usar registros autorizados con case_id, actividad y timestamp; PM4Py permite estudiar variantes y cuellos de botella, no puntuar empleados. Grafo: rol CONOCE procedimiento, proceso USA sistema, sistema DEPENDE_DE componente, documento DESCRIBE proceso, agente ASISTE rol. Primero relaciones SQL; ampliar a grafo dedicado solo si aporta valor.

Piloto B: hasta tres especialistas, cinco a diez procedimientos y 2–3 agentes. Casos históricos anonimizados, conjunto de prueba separado, revisión de calidad, tiempo y omisiones. No entrenar modelos con datos personales sin autorización.
