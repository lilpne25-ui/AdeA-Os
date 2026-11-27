# SGCI Full Business Discovery — v0.3
Propuesta conceptual independiente. SGCI es la denominación indicada por el solicitante; confirmar nombre oficial, alcance y lista maestra con responsables. El objetivo es cubrir TODO el SGCI autorizado, no toda la red corporativa ni carpetas ajenas. No se han escaneado datos reales. Este repositorio público no almacena rutas, nombres de documentos, clientes, reglas internas ni resultados reales.

## Decisión y viabilidad antes de ejecutar
Con un ingeniero responsable y apoyo puntual de SGCI, TI, seguridad y dueños de proceso, iniciar con inventario local reproducible. No contratar 20 licencias ni construir el OS completo para descubrir el negocio. Confirmar presupuesto mensual USD 50 (interpretación, no dato verificado), capacidad de PC/servidor, ventanas de lectura SMB, alcance, formatos, lista maestra, restricciones de clientes, almacenamiento privado y tiempo reservado. Si no hay autorización de contenido, avanzar solo con inventario de metadatos. Si no hay autorización de proveedor IA, usar extracción y análisis local; ningún dato real sale a nube.
  
## Alcance: cobertura total progresiva
500 archivos y 30 documentos son una prueba técnica inicial, NO límite del proyecto. La cobertura objetivo es 100% de raíces/archivos dentro del universo aprobado, con reconciliación contra lista maestra. Registrar cada archivo como inventariado, extraído, excluido con motivo, inaccesible, corrupto, cifrado, no soportado o pendiente. No considerar excluidos/inaccesibles como analizados; no afirmar cobertura 100% si el denominador es desconocido. Escanear por lotes, checkpoint y reanudación, sin límite global arbitrario, con límites por lote y aprobación de carga. Evitar reparse points, DFS referrals no aprobados, archivos cambiantes y rutas fuera de alcance; tratar alias DFS con TI. No seguir accesos directos, no descubrir shares, no elevar privilegios, no escribir en origen.

## Flujo
0. Gate: autorización y capacidad; ejecutar pruebas sintéticas primero.
1. Enumerar metadatos en raíces UNC explícitas. Usar worker interno con cuenta de lectura. Catálogo local SQLite; rutas y errores privados.
2. Reconciliar conteos y lista maestra por raíz, formato, macroproceso, revisión. Duplicados candidatos por tamaño y nombre; SHA-256 para lectura autorizada. No considerar duplicado semántico sin validación.
3. Extraer localmente todo documento elegible: Tika/POI para texto y metadatos, Docling para estructura, tablas y páginas; Tesseract/RapidOCR solo en páginas necesarias. Aislar parsers, no macros/scripts/enlaces externos, límites de tamaño y tiempo, cuarentena de corruptos.
4. Normalizar código, versión, vigencia, aprobación, referencias, roles y proceso. Mantener texto extraído y hashes privados. Clasificar con reglas, regex, búsqueda FTS5/BM25 y taxonomía SGCI aprobada. Modelos locales opcionales sujetos a licencia y hardware.
5. Extraer reglas de negocio con evidencia: condición, acción, excepción, datos, responsable, sistema, fuente doc_id/revisión/página/sección, estado y revisión. Separar normativa, observado, inferido, desconocido y contradictorio. Distinguir versiones históricas de vigentes.
6. Consolidar mapa macroproceso > proceso > actividad > regla > documento > sistema > rol; identificar entradas, salidas, controles, handoffs y relaciones. BPMN/Mermaid y grafo SQL; GraphRAG opcional posterior. Priorizar core según impacto validado, no número de documentos.
7. Cuellos de botella: hipótesis desde documentos/entrevistas; comprobar mediante eventos autorizados con case_id, actividad, timestamp, inicio/fin cuando existan, volumen, espera, retrabajo. PM4Py solo si hay eventos suficientes y revisión de licencia AGPL. Sin eventos, muestreo manual; no inferir tiempos de mtime ni vigilar individuos.
8. Validar con especialistas y SGCI. Cada regla crítica requiere revisión; muestra estratificada para clasificación/extracción, registrar precisión, omisiones y contradicciones. Entregar backlog de automatización, documentación, capacitación, Element y legacy. AutoRAG solo tras aprobación de contenido y ACL; indexación incremental y borrado/revocación.

## Herramientas, elección mínima
| Función | Inicial | Escalamiento |
|---|---|---|
| UNC inventario | PowerShell o Python os.scandir | Worker interno con cola y checkpoints |
| Catálogo y búsqueda | SQLite + FTS5, CSV privado | PostgreSQL/pgvector |
| Texto/Office | Apache Tika/POI | Docling para estructura |
| OCR | Tesseract/RapidOCR local | Workers paralelos autorizados |
| Clasificación | regex, reglas, scikit-learn opcional | modelo local o API aprobada |
| Procesos y reglas | Mermaid, bpmn.io, JSON/CSV | PM4Py con eventos, grafo SQL/GraphRAG |
| Interfaz | informe HTML local y React si procede | Control Center |
| Legacy | JavaParser/Spoon/Vineflower/REA evaluado | OpenRewrite, pruebas de paridad |
No instalar toda la lista. Versiones, licencias, soporte, SBOM y vulnerabilidades deben verificarse; modelos locales también tienen licencia. Referencias: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem ; https://tika.apache.org/ ; https://github.com/docling-project/docling ; https://github.com/docling-project/docling-pipelines ; https://processintelligence.solutions/pm4py/examples/process-discovery/ ; https://www.sqlite.org/fts5.html ; https://github.com/tesseract-ocr/tesseract ; https://github.com/bpmn-io .

## Roadmap realista y estimación
Semanas 1–2 (48 h agregadas dentro del Plan A original, 14,400 MXN valorizados): permisos, inventario piloto, reconciliación, benchmark 30 documentos estratificados, catálogo y primer mapa. Gate: aprobar seguridad, medir volumen, velocidad, errores y horas de revisión; decidir capacidad. Si el SGCI es grande, descubrimiento completo es una línea paralela, no compromiso de 2 semanas.
Semanas 3–6: inventario completo autorizado por lotes y extracción local elegible; automatizar clasificación y priorizar macroprocesos. Objetivo indicativo, sujeto a benchmark.
Semanas 5–10: consolidar reglas, relaciones, contradicciones y entrevistas; validar core por dominio. Semanas 8–12+: procesos reales, cuellos de botella y backlog, continuar por oleadas. No prometer plazo fijo hasta conocer universo. Con solo 5–10 h/semana disponibles, 100–180 h de trabajo humano equivalen a 10–36 semanas; reservar tiempo formal o reducir concurrencia de otros proyectos. No exigir revisión manual de cada archivo, sí de reglas críticas y muestras por familia. Estimación de procesamiento: N documentos elegibles / documentos por hora medidos + reintentos, OCR y ventanas de ejecución; revisión humana = documentos/reglas a revisar × minutos por revisión /60. Ejemplo sintético 10,000 documentos a 200/h = 50 horas máquina; 300 revisiones × 10 min = 50 horas humanas, además de preparación, entrevistas y QA. No es medición real.

## Entregables privados
manifest de raíces; scan_runs; inventory CSV/SQLite; error ledger; document_versions; process_catalog; rules_catalog; process_document_links; BPMN AS-IS y propuestas TO-BE separadas; hipótesis de cuellos de botella con evidencia; backlog con frecuencia, tiempo, impacto, riesgo, esfuerzo, dependencia, responsable; informe cobertura; catálogo de fuentes aprobadas para AutoRAG; requisitos para Document Factory, Academy, Element y modernización. Exportaciones públicas solo sintéticas.
