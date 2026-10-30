---
version: 1.0.0
ratified: 2026-10-29
last_amended: 2026-10-29
status: active
source_of_truth: .specify/memory/constitution.md
mirror: ./constitution.md
methodology: SDD
project: BusTrack - Machine Learning
team:
  - Fátima Ximena García González
  - Diego Parra Cruz
  - José De Jesús López Islas
  - Melanie Joliee Bonilla Domínguez
institution: Universidad Tecnológica de Tula-Tepeji
---

# Constitución — BusTrack Machine Learning

> Rector técnico del microservicio de ML. Ante conflicto con otro artefacto, **manda esta constitución**.
> Filosofía madre: ningún modelo ni pipeline se promueve sin pruebas de reproducibilidad, validación de métricas y cumplimiento de gates de DevSecOps.

## 1. Propósito y alcance

- Microservicio en Python (FastAPI + scikit-learn) para el análisis de series de tiempo de sensores inerciales (acelerómetro).
- Detección de paradas candidatas mediante clasificación de secuencias de aceleración, frenado y reposo.
- Toda funcionalidad se deriva de especificaciones formales en `/specs`.
- Comunicación exclusiva con la API principal (`bustrack-api`) mediante autenticación con tokens de servicio.

## 2. Principios no negociables

1. **Privacidad y Anonimización**:
   - Prohibido ingerir o persistir identificadores personales directos de usuarios en los conjuntos de datos de entrenamiento o inferencia.
   - Los datos de sensores no deben cruzarse con rastreo GPS continuo en tiempo real.
2. **Reproducibilidad y Versionamiento**:
   - Semillas aleatorias (`random_state`) fijadas para garantizar reproducibilidad en entrenamientos y validaciones.
   - Prohibido subir archivos pesados binarios de modelos (`.pkl`, `.h5`, `.pt`) directamente al repositorio Git (deben gestionarse en almacenamiento externo, ej. Azure Blob Storage).
3. **Validación de Datos en Frontera**:
   - Validación estricta de esquemas de entrada mediante esquemas Pydantic antes de ingresar a los pipelines de inferencia.
4. **Gates de Desempeño del Modelo**:
   - Cada nuevo modelo en `ModelTest/` debe superar umbrales mínimos documentados de precisión y F1-score antes de su integración.
5. **Fail-safe en Producción**:
   - Las paradas candidatas generadas por el modelo son recomendaciones que requieren validación de consistencia antes de publicarse a los usuarios finales.
6. **Bitácora en Memoria**:
   - Toda experimentación, hiperparámetros y lecciones aprendidas se registran en `Memoria.md`.

## 3. Gobernanza SDD y DevSecOps

- Cada PR debe cumplir la lista de comprobación de `CHECKLIST_PR.md`.
- CI configurado en `.github/workflows/` con `pytest`, `flake8` y escaneo SAST con Semgrep.
