# Análisis tecnológico de clientes y Element
Levantamiento: aplicaciones y versiones, arquitectura, bases de datos, infraestructura, redes, API, dependencias, seguridad, periféricos, flujos, SLAs, documentación, responsables por rol, problemas y oportunidades. Registrar fuente, fecha, propietario, confianza y estado de validación. Separar AS-IS de TO-BE. No registrar datos reales en este repositorio.

## Flujo de comunicación
Solicitud autorizada -> ticket con folio -> clasificación -> responsable -> análisis -> aprobación -> actualización en Element -> entrega y cierre con evidencia. Element es canal de interacción; el sistema de tickets conserva el registro oficial.

Plan A: bot de solo lectura/notificaciones, una sala de laboratorio, un tipo de ticket, eventos sintéticos; medir latencia de respuesta y mensajes manuales evitados. Plan B: integrar diagnóstico y Document Factory, seguimiento de estados y asistente RAG con permisos. Plan C: ampliar canales por cliente y procesos con aprobación.

Tecnologías candidatas: Matrix Client-Server API, Matrix Hookshot y SDK Matrix, Node-RED, OpenProject o Zammad (elegir uno o reutilizar herramienta actual). Patrón outbox, reintentos, deduplicación, cola de errores, correlación de folio y observabilidad. Identidad de servicio con mínimos permisos; credenciales en gestor de secretos. Respetar E2EE: usar cliente compatible y salas explícitamente autorizadas; no desactivar cifrado ni indexar chats privados. Enviar metadatos mínimos, no expedientes. Acceso externo solo tras autorización y pruebas de aislamiento por cliente.
