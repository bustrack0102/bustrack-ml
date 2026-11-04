# Specs por tarea — BusTrack ML

> Cada carpeta numerada representa una tarea o funcionalidad concreta y contiene
> `spec.md`, `plan.md`, `task.md` y `chart.md`. Las categorías técnicas generales
> ya no viven aquí: CI/CD está en `../cicd/` y Azure en `../azure/`.
> El historial se conserva en `../docs/archivo-sdd/specs-anteriores/`.

## Tareas

| ID | Tarea | Estado |
|---|---|---|
| `01-configuracion-inicial-del-proyecto` | Configuración inicial del proyecto | Parcial |
| `02-arquitectura-base-fastapi` | Arquitectura base FastAPI | Pendiente |
| `03-contrato-de-lotes-de-acelerometro` | Contrato de lotes de acelerómetro | Pendiente |
| `04-validacion-y-anonimizacion` | Validación y anonimización de lotes | Pendiente |
| `05-limpieza-y-ventaneo` | Limpieza y ventaneo de señales | Pendiente |
| `06-extraccion-de-caracteristicas` | Extracción de características | Pendiente |
| `07-dataset-y-etiquetado` | Dataset y etiquetado | Pendiente |
| `08-entrenamiento-del-modelo` | Entrenamiento del modelo | Pendiente |
| `09-evaluacion-del-modelo` | Evaluación del modelo | Pendiente |
| `10-versionado-de-modelos` | Versionado de modelos | Pendiente |
| `11-inferencia-de-paradas` | Inferencia de paradas | Pendiente |
| `12-observabilidad-y-limites` | Observabilidad y límites del servicio | Pendiente |
| `13-empaquetado-docker` | Empaquetado Docker | Pendiente |

## Reglas

- No crear carpetas vacías ni specs genéricas para completar la estructura.
- No dividir una tarea en varias specs ni agrupar funcionalidades independientes.
- Una tarea pasa a `Implementado` solo con código y pruebas verificables.
- Los endpoints se documentan aparte, en `../specs-endpoints/`.
