# Diagramas — Pipeline de procesamiento de acelerómetro

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Lote] --> B[Validar]
  B -->|inválido| C[Rechazar]
  B -->|válido| D[Anonimizar]
  D --> E[Limpieza]
  E --> F[Ventanas]
  F --> G[Features]
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  API[API] --> ML[ML]
  ML --> P[Pipeline]
  P --> M[Modelo]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant P as Pipeline
  participant M as Modelo
  A->>P: lote
  P->>P: validar + anonimizar + features
  P->>M: features
  M-->>P: predicción
  P-->>A: resultado
```

## 4. Notas

Contrato pendiente de confirmación con Mobile.
