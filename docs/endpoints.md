# Endpoints — BusTrack ML (FastAPI interno)

> Fuente de contratos internos del servicio ML. Ningún cliente público (Flutter/React) accede directamente; solo la API central consume estos endpoints.

| Método | Ruta | Auth | Rate | Códigos | Spec |
|---|---|---|---|---|---|
| GET | `/health` | Interno | — | 200/503 | 14-endpoint-health |
| POST | `/inference` | X-Internal-Key / Bearer | — | 200/401/403/413/422/500 | 15-endpoint-inference |
