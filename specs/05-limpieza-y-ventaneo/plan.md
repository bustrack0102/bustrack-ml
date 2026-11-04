# Plan técnico — 05-limpieza-y-ventaneo — Limpieza y ventaneo de señales

> Spec: `spec.md` · Repositorio: BusTrack ML · Estado: Pendiente.

## 1. Estrategia

Implementar por incrementos, conservando contratos y midiendo con pruebas antes de avanzar.

## 2. Arquitectura y componentes

- Stack objetivo: Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.
- Componentes: componentes del repositorio afectados por la tarea.
- Tecnología: Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.

## 3. Archivos y estructura

```text
src/pipelines/preprocess.py (futuro)
```

## 4. Seguridad

- Validación Pydantic, anonimización, límites de tamaño, sin secretos y sin pickle de origen no confiable.
- Validar entradas y no registrar secretos/PII.

## 5. Riesgos

- Confundir el estado actual con el objetivo.
- Dependencias con otros repositorios no documentadas.
- Ampliar el alcance sin spec aprobada.

## 6. Estrategia de pruebas

Pruebas unitarias y de contrato cuando exista código; revisión documental mientras la tarea sea propuesta.

## 7. Trazabilidad

Cada tarea de `task.md` referencia un requisito de `spec.md`; los diagramas viven en `chart.md`.
