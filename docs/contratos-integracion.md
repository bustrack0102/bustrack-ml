# Contratos de integración — BusTrack ML

> Vista de los contratos que este repositorio expone o consume. Solo login/logout están
> implementados en los clientes y la API; el resto es **propuesta** hasta que exista código.

## 1. Principios

- La API central es la única fuente autorizada de datos de transporte.
- Ningún cliente accede a Cosmos DB ni a ML/GenAI directamente.
- ML y GenAI son servicios internos autenticados; no exponen login público.
- Toda integración usa HTTPS, timeouts y errores tipados.
- Lo propuesto se marca como tal; no se declaran endpoints inexistentes.

## 2. Expone (solo API)

| Método | Ruta | Estado | Auth |
|---|---|---|---|
| GET | `/health` | Propuesta | Interno. |
| POST | `/inference` | Propuesta | Token interno / identidad administrada. |

## 3. Consume

- No consume otros servicios en el MVP.
- Recibe lotes de acelerómetro anonimizados desde la API.

## 4. Reglas

- Sin login público.
- Sin acceso a Cosmos DB.
- Sin PII en entradas, salidas ni logs.

## 5. Errores uniformes

| Código | Significado |
|---|---|
| 400 | Petición mal formada. |
| 401 | Credencial ausente o inválida. |
| 403 | Sin permiso. |
| 404 | Recurso inexistente. |
| 409 | Conflicto de concurrencia/unicidad. |
| 422 | Validación de dominio/esquema. |
| 429 | Rate limit. |
| 500 | Error interno sin detalles sensibles. |
