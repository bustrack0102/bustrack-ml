# Diagramas — 09-evaluacion-del-modelo — Evaluación del modelo

> Spec: `spec.md` · Plan: `plan.md`.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Modelo] --> B[Evaluar]
  B --> C{¿Umbral?}
  C -->|sí| D[Promover]
  C -->|no| E[Ajustar]
```

## 2. Componentes

```mermaid
flowchart LR
  C[Cliente] --> A[Servicio]
  A --> D[(Datos)]
```

## 3. Secuencia

```mermaid
sequenceDiagram
  participant D as Dev
  participant C as CI
  D->>C: push
  C-->>D: lint + pruebas
```

## 4. Notas

Diagramas de proceso; no representan recursos desplegados.
