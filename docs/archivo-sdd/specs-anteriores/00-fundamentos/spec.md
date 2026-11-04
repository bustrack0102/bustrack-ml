# 00 — Fundamentos y gobernanza SDD

> Repositorio: BusTrack ML · Ruta: `specs/00-fundamentos/` · Estado: Implementado · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `00-fundamentos`
- **Nombre:** 00 — Fundamentos y gobernanza SDD
- **Repositorio:** BusTrack ML

## 2. Objetivo

Fijar los principios, límites y flujo SDD de BusTrack ML.

## 3. Contexto

La documentación previa no reflejaba el estado real del repositorio. Esta spec establece la fuente de verdad.

## 4. Alcance

**Incluye:**

- Constitución, AGENTS, Memoria, CHECKLIST y README.
- Tecnología actual vs objetivo.
- Flujo spec→plan→task→chart→pruebas.
- Prohibición de declarar avances sin evidencia.

**No incluye:**

- Implementar funcionalidad de negocio.
- Cambiar la tecnología objetivo.
- Desplegar recursos.

## 5. Requisitos funcionales

1. Describir el stack actual: Python 3.11, FastAPI, scikit-learn, pandas/numpy/scipy, joblib (esqueleto sin código).
2. Fijar el stack objetivo: Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.
3. Definir criterios de terminado y trazabilidad.
4. Registrar decisiones pendientes sin inventar respuestas.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] El documento existe y es coherente con el código.
- [ ] Las tareas tienen criterio de terminado verificable.
- [ ] No se declaran implementaciones inexistentes.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- `Memoria.md`
- `docs/contratos-integracion.md`

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
