# Modernization Factory: Java escritorio a PWA
El objetivo es equivalencia funcional demostrada, no traducir cada clase a JavaScript. Priorizar código fuente y observación autorizada; ingeniería inversa de binarios únicamente con permiso y licencia.

## Método
1. Inventario de Java, Swing/AWT, JDBC, JAR, librerías, SQL, interfaces, periféricos y configuración.
2. Análisis estático: jdeps, JavaParser/Spoon, jQAssistant y OpenRewrite. Evaluar REA (Reverse Engineer Anything) como integración experimental con agentes, no asumir cobertura de Java; Vineflower para bytecode autorizado, Ghidra solo si hay binarios nativos relevantes.
3. Levantamiento funcional por pantalla, evento, método, regla, tabla, entrada, salida y excepción. Contrastar con operador y casos reales anonimizados.
4. Matriz de decisión: migración directa, rediseño, puente nativo, aplazar o retirar con aprobación.
5. Especificación SDD independiente, contratos OpenAPI, pruebas de caracterización del sistema anterior.
6. Implementación incremental: backend Java autorizado, APIs y PWA React/TypeScript; conservar base existente inicialmente si es seguro.
7. Comparar resultados, permisos, rendimiento, accesibilidad, errores y transacciones; pruebas JUnit/Playwright y aceptación funcional. Despliegue gradual con rollback.

| Función | Estrategia |
|---|---|
| Formularios, tablas, búsquedas | Web directa con pruebas |
| Reglas Java | Reutilizar en backend cuando sea viable |
| JDBC desde escritorio | Encapsular en servicios |
| Reportes PDF | Generación backend |
| Archivos locales / offline | Rediseñar almacenamiento y sincronización |
| Escáner TWAIN/WIA, impresión silenciosa | Evaluar puente local firmado y autenticado |
| JNI/hardware especializado | Analizar individualmente |

Ejemplo sintético de trazabilidad: F001 login -> Login.java -> POST /auth -> prueba RBAC; F002 búsqueda -> Search.java -> GET /documents -> prueba filtros; F003 escáner -> Scanner.java -> puente nativo -> prueba hardware. Ningún caso se considera validado sin ejecución.

A: diagnóstico de una aplicación, sin migración productiva. B: módulo pequeño no crítico y demostración PWA; C: uno o dos módulos, liberación incremental solo si aprobada. No sustituir todo el catálogo legacy.
