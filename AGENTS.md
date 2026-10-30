# AGENTS.md — Manual Operativo para Agentes de IA (BusTrack ML)

> Este manual define las directrices que los agentes de IA (OpenCode / WARP) deben seguir para interactuar con este repositorio.

---

## 1. Reglas Fundamentales de SDD
1. **Spec First:** Ningún código en `src/` o `tests/` se escribe sin una especificación previa aprobada en `specs/`.
2. **Cero Datos Sensibles:** Nunca exponer PII ni credenciales en código, logs o conjuntos de prueba.
3. **Reproducibilidad:** Fijar semillas aleatorias en todo preprocesamiento o división de datos (`random_state=42`).
4. **Validación Pydantic:** Todas las cargas útiles entrantes al microservicio FastAPI deben validarse con modelos estrictos de Pydantic.

---

## 2. Flujo de Trabajo
1. Seleccionar o redactar la especificación en `specs/`.
2. Crear los esquemas de datos y validadores en `src/data/` y `src/api/`.
3. Escribir pruebas unitarias y de integración en `UnitTest/` e `IntegrationTest/`.
4. Implementar el pipeline de procesamiento o modelo en `src/models/` o `src/pipelines/`.
5. Ejecutar suites de pruebas y validar métricas con `pytest`.
6. Actualizar `Memoria.md` y completar `CHECKLIST_PR.md`.
