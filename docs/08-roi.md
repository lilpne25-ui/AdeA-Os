# ROI Intelligence — modelo de decisión
Modelo hipotético sin impuestos, descuento ni inflación. Meses iniciales sin beneficio; operación desde mes 1. Costes y beneficios en MXN. Capacidad liberada no equivale a ahorro monetario.

Horas liberadas/mes = usuarios × horas recuperables por usuario/semana × 4.33 × adopción.
Beneficio mensual = horas liberadas × coste/h × realización económica.
Coste año 1 = inversión inicial + 12 × operación mensual.
Beneficio año 1 = beneficio mensual × (12 − meses de implementación).
ROI = (beneficio año 1 − coste año 1) / coste año 1.
Recuperación = meses de implementación + (inversión + meses de implementación × operación) / (beneficio mensual − operación), si beneficio supera operación.

| Supuesto | A | B | C |
|---|---:|---:|---:|
| Usuarios | 10 | 20 | 40 |
| Horas/semana | 4 | 5 | 6 |
| Adopción | 75% | 75% | 80% |
| Realización | 60% | 65% | 70% |
| Coste/h | 300 | 300 | 300 |
| Meses sin beneficio | 2 | 4 | 7 |
| Beneficio mensual aproximado | 23,382 | 63,326 | 174,586 |
| Beneficio año 1 aproximado | 233,820 | 506,610 | 872,928 |
| Coste año 1 | 152,000 | 344,000 | 800,000 |
| ROI año 1 | 53.8% | 47.3% | 9.1% |
| Recuperación meses | 7.3 | 8.8 | 11.5 |

Con realización económica a la mitad del supuesto, los tres ROI del primer año son negativos. No sumar beneficios por actividad si corresponden a las mismas horas. Realización = proporción de horas que genera valor demostrable (capacidad reasignada a demanda real, horas extra evitadas o costes evitados); separar ahorro contable de capacidad.

## Instrumentación
Dos semanas de línea base y muestra comparable posterior: duración de tareas por complejidad, tiempo hasta documento aprobado, tiempo de respuesta a cliente, retrabajo, defectos, coste IA por tarea, horas de capacitación, paridad funcional y adopción. Registrar denominador, fechas, fuente, mediana/variabilidad y excepciones. No atribuir causalidad si cambió el volumen o dificultad. Responsable de negocio y finanzas revisan supuestos y valor realizado. No utilizar datos de personas reales en este repositorio.

Ejecutar tools/roi.py para reproducir resultados y sensibilidad. Para análisis de escenarios, variar usuarios, horas, coste, adopción y realización con evidencia; no considerar estas cifras una promesa.
