# Document Factory
Convertir materiales existentes en borradores verificables: código, manuales, plantillas, casos, entrevistas consentidas, esquemas SQL y registros autorizados. No inventar reglas, datos o responsables.

Documentos: diagnóstico tecnológico; arquitectura AS-IS/TO-BE; especificación funcional/SDD; BPMN; manual usuario/técnico; RACI validada; diccionario de datos; plan de pruebas; riesgos; propuesta de modernización; material didáctico; informe de productividad y ROI.

Flujo: seleccionar plantilla aprobada -> recuperar fuentes con permisos -> generar borrador con citas -> revisar evidencias y datos sensibles -> revisión técnica/funcional -> aprobar y publicar versión -> detectar cambios que requieren revisión. Guardar ID, versión, fuente, fecha, responsable por rol, aprobador y estado. Borrador no equivale a documento oficial.

Herramientas: Pandoc, docxtpl, python-docx, Apache POI, WeasyPrint, Mermaid, PlantUML, MkDocs. A: dos plantillas simples. B: ampliar hasta cinco tipos y exportación DOCX/PDF. C: gestión de ciclo de vida y dependencias. Medir tiempo hasta documento aprobado, correcciones y exactitud, no solo borradores generados.
