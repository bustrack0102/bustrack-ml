# Matriz de Versionamiento SemVer — BusTrack ML (Requisito 11 y 15)

Ver matriz maestra unificada en `bustrack-api/docs/versionamiento.md`.

| Hito | SemVer | Modelo ML | Docker Tag (`bustrackacr0102`) | Contrato Interno |
|---|---|---|---|---|
| Línea Base | `0.1.0` | `1.0.0` (heurístico) | `0.1.0-{sha}` | `GET /health`, `POST /inference` |
| **Etapa 0** | `0.2.0` | `1.0.0` | `0.2.0-{sha}` | CD ACR automatizado + SDD + pytest |
| **Etapa 3** | `0.8.0` | `1.1.0` (`.joblib`) | `0.8.0-{sha}` | Modelo `scikit-learn` entrenado + `ModelTest` F1>=0.85 |
| **Etapa 4** | `0.9.0` | `1.1.0` | `0.9.0-{sha}` | Container App interno + App Insights |
| **Etapa 5** | `1.0.0` | `1.1.0` | `1.0.0-{sha}` | Liberación Evaluación Final |
