# Specs de endpoints — BusTrack ML

> Contratos HTTP que este repositorio expone o consume. Cada endpoint tiene
> `spec.md`, `plan.md`, `task.md` y `chart.md`. La numeración continúa después
> de la última tarea de `../specs/`.

## Endpoints

| ID | Método y ruta | Nombre | Estado |
|---|---|---|---|
| `14-endpoint-health` | `GET /health` | Endpoint de salud del servicio ML | Propuesto |
| `15-endpoint-inference` | `POST /inference` | Endpoint interno de inferencia | Propuesto |

## Reglas

- Diferenciar endpoints implementados de propuestos.
- No inventar endpoints ni métodos.
- Cada endpoint declara autenticación, validaciones, códigos HTTP y pruebas.
