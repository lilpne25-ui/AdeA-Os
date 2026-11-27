# AdeA Intelligence OS — v0.2.1

> Propuesta conceptual independiente de transformación tecnológica. No es una plataforma implantada, una iniciativa oficialmente aprobada ni un presupuesto autorizado. Todos los escenarios son hipotéticos. Este repositorio público contiene únicamente diseños generales y ejemplos sintéticos.

**Discover · Connect · Learn · Automate · Modernize**

Objetivo: mejorar desarrollo de software, comunicación con clientes, transferencia de conocimiento y documentación; modernizar aplicaciones legacy de forma gradual y medible.

La primera etapa de todos los planes es el escaneo documental de negocio del SGI sobre rutas UNC expresamente autorizadas, con inventario privado y mapeo a procesos.

## Planes de inversión (MXN)

| Plan | Alcance | Tiempo desde inicio | Inversión inicial | Operación mensual |
|---|---|---:|---:|---:|
| A — Development & Connect | IA para desarrollo, capacitación, Element, diagnóstico legacy | 8 semanas | 80,000 | 6,000 |
| B — Knowledge & Automation | A + AutoRAG, agentes, documentos y módulo PWA | 4 meses | 200,000 | 12,000 |
| C — Enterprise Intelligence | B + centro de control, grafo y minería de procesos | 6–9 meses | 500,000 | 25,000 |

Los presupuestos incluyen valoración del trabajo interno. No son cotizaciones. Se propone autorizar A primero, B solo tras evaluar A y C solo tras evaluar B. Importes incrementales teóricos: 80,000 + 120,000 + 300,000; recalcular según reutilización real.

## Documentación
- [Fase 0 — Business Discovery / SGI UNC Scanner](docs/00-sgi-business-discovery.md)
- [Arquitectura y centro de control](docs/01-architecture.md)
- [Análisis tecnológico y comunicación](docs/02-client-element.md)
- [Personas, procesos, AutoRAG y agentes](docs/03-knowledge-agents.md)
- [Modernización Java y REA](docs/04-legacy-modernization.md)
- [Document Factory](docs/05-document-factory.md)
- [Academy y cursos](docs/06-academy.md)
- [Roadmap, recursos y presupuesto](docs/07-roadmap.md)
- [ROI y criterios de decisión](docs/08-roi.md)
- [Catálogo de herramientas abiertas](docs/09-open-source.md)
- [Gobierno, seguridad y backlog](docs/10-governance-backlog.md)
- [Plantillas de levantamiento](templates/discovery.md)
- [Calculadora reproducible](tools/roi.py)

## Ejecución del modelo financiero
```sh
python3 tools/roi.py
python3 tools/roi.py --realization-factor 0.5
python3 -m unittest discover -s tools -p 'test_*.py'
```

Estado: especificación v0.2.1, sin conexión a sistemas reales. No contiene código o documentación interna, datos de clientes, credenciales, información individual ni materiales de terceros con licencia restrictiva. Todo uso corporativo requiere autorización y revisión de seguridad, licencias y arquitectura. No se concede licencia sobre marcas o materiales de terceros.
