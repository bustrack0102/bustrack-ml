# 02 — Arquitectura y límites del servicio

> Repositorio: BusTrack ML · Ruta: `specs/02-arquitectura/` · Estado: Parcial · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `02-arquitectura`
- **Nombre:** 02 — Arquitectura y límites del servicio
- **Repositorio:** BusTrack ML

## 2. Objetivo

Definir la arquitectura interna de BusTrack ML y sus límites con BusTrack.

## 3. Contexto

Arquitectura actual: src/{api,core,data,models,pipelines}; suites UnitTest, IntegrationTest, ModelTest, SecurityTest

## 4. Alcance

**Incluye:**

- Componentes y responsabilidades.
- Límites con API, clientes, ML/GenAI y Cosmos.
- Dependencias permitidas.
- Estrategia de evolución.

**No incluye:**

- Implementar features de dominio.
- Desplegar.
- Cambiar contratos públicos sin spec.

## 5. Requisitos funcionales

1. Mantener separación de capas y responsabilidades.
2. No acceder a Cosmos desde clientes.
3. No duplicar la fuente autorizada de datos.
4. Documentar componentes y flujos.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] El diagrama coincide con `chart.md`.
- [ ] Cada componente tiene responsabilidad única.
- [ ] No hay dependencias prohibidas.
- [ ] La transición está documentada.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- `constitution.md`
- `docs/contratos-integracion.md`

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
