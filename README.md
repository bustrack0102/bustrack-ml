# BusTrack ML — BusTrack

> Sistema de consulta y planificación de transporte público — Universidad Tecnológica de Tula-Tepeji.
> SDD + DevSecOps. Este README describe el **estado real** y la **arquitectura objetivo**.

## Estado actual

- **Tecnología real:** Python 3.11, FastAPI, scikit-learn, pandas/numpy/scipy, joblib (esqueleto sin código).
- **Tecnología objetivo:** Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.
- **Implementado:** ver lista en `Memoria.md`.
- **No implementado:** ver pendientes en `Memoria.md`.
- **Recursos Azure:** no desplegados; propuesta en `azure/`.

## Qué hace este repositorio

API central -> ML por HTTP interno; ML devuelve clasificaciones y características.

## Estructura

```text
src/{api,core,data,models,pipelines}; suites UnitTest, IntegrationTest, ModelTest, SecurityTest
```

## Gobernanza SDD

| Documento | Propósito |
|---|---|
| `constitution.md` | Principios inalterables del repositorio. |
| `AGENTS.md` | Instrucciones para agentes de IA. |
| `Memoria.md` | Estado real, decisiones y deuda técnica. |
| `CHECKLIST_PR.md` | Controles obligatorios de PR. |
| `specs/` | Specs canónicas (`spec.md`, `plan.md`, `task.md`, `chart.md`). |
| `docs/contratos-integracion.md` | Contratos con los demás repositorios. |
| `.opencode/` | Agentes y skills específicos. |
| `.semgrep/` | Reglas SAST reales. |
| `.github/workflows/` | CI por stack. |

## Specs por tarea

- `specs/01-configuracion-inicial-del-proyecto/` — Configuración inicial del proyecto (Parcial).
- `specs/02-arquitectura-base-fastapi/` — Arquitectura base FastAPI (Pendiente).
- `specs/03-contrato-de-lotes-de-acelerometro/` — Contrato de lotes de acelerómetro (Pendiente).
- `specs/04-validacion-y-anonimizacion/` — Validación y anonimización de lotes (Pendiente).
- `specs/05-limpieza-y-ventaneo/` — Limpieza y ventaneo de señales (Pendiente).
- `specs/06-extraccion-de-caracteristicas/` — Extracción de características (Pendiente).
- `specs/07-dataset-y-etiquetado/` — Dataset y etiquetado (Pendiente).
- `specs/08-entrenamiento-del-modelo/` — Entrenamiento del modelo (Pendiente).
- `specs/09-evaluacion-del-modelo/` — Evaluación del modelo (Pendiente).
- `specs/10-versionado-de-modelos/` — Versionado de modelos (Pendiente).
- `specs/11-inferencia-de-paradas/` — Inferencia de paradas (Pendiente).
- `specs/12-observabilidad-y-limites/` — Observabilidad y límites del servicio (Pendiente).
- `specs/13-empaquetado-docker/` — Empaquetado Docker (Pendiente).

## Specs de endpoints

- `specs-endpoints/14-endpoint-health/` — `GET /health` (Propuesto).
- `specs-endpoints/15-endpoint-inference/` — `POST /inference` (Propuesto).

## CI/CD y Azure

- `cicd/` — arquitectura del pipeline y gates.
- `azure/` — arquitectura final de despliegue (propuesta).

El historial de la organización anterior está en `docs/archivo-sdd/specs-anteriores/`.

## Comandos

```text
pip install -r requirements.txt
black --check src UnitTest IntegrationTest ModelTest SecurityTest && flake8 src UnitTest IntegrationTest ModelTest SecurityTest
pytest UnitTest IntegrationTest ModelTest SecurityTest
```

## Limitaciones y advertencias

- No se declara funcionalidad terminada sin código y pruebas.
- El árbol está anidado `X-main/X-main`; la raíz real es la carpeta interior.
- No hay repositorio Git local, por lo que tags/releases no son verificables.
- No hay despliegue Azure ni recursos provisionados.

## Equipo

Fátima Ximena García González, Diego Parra Cruz, José de Jesús López Islas, Melanie Joliee Bonilla Domínguez.
