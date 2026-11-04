# Diagramas — Endpoints internos de inferencia

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart LR
  API[API] -->|token| ML[ML]
  ML --> V[Validar]
  V --> P[Predecir]
  P --> R[Responder]
```

## 2. Relación entre componentes

```mermaid
flowchart TD
  C[Cliente] --> API[API]
  API --> ML[ML]
  API --> DB[(Cosmos)]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant M as ML
  A->>M: POST /inference + token
  M->>M: validar + predecir
  M-->>A: paradas + score
```

## 4. Notas

El servicio ML no expone login público.
