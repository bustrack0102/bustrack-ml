# Diagramas — Entrenamiento, evaluación y versionado del modelo

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Dataset] --> B[Preprocesar]
  B --> C[Entrenar]
  C --> D[Evaluar]
  D -->|umbral ok| E[Versionar]
  D -->|no| F[Ajustar]
  F --> C
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  D[(Datos)] --> T[Train]
  T --> M[Modelo]
  M --> E[Evaluación]
  E --> R[Registro]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant D as Dataset
  participant T as Trainer
  participant E as Evaluator
  participant R as Registry
  D->>T: features + labels
  T->>E: modelo
  E->>R: métricas + artefacto
  R-->>T: versión
```

## 4. Notas

No se declaran métricas ni modelos existentes.
