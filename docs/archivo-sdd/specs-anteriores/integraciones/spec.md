# Integraciones con el ecosistema BusTrack

> Repositorio: BusTrack ML · Ruta: `specs/integraciones/` · Estado: Parcial · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `integraciones`
- **Nombre:** Integraciones con el ecosistema BusTrack
- **Repositorio:** BusTrack ML

## 2. Objetivo

Definir los contratos de entrada/salida de Servicio de Machine Learning con los demás repositorios.

## 3. Contexto

API central -> ML por HTTP interno; ML devuelve clasificaciones y características.

## 4. Alcance

**Incluye:**

- Contratos HTTP y esquemas.
- Autenticación y errores.
- Timeouts y responsabilidades.
- Lo existente y lo propuesto.

**No incluye:**

- Implementar endpoints pendientes.
- Acceso directo a Cosmos.
- Rastreo GPS.

## 5. Requisitos funcionales

1. Distinguir endpoints implementados de propuestos.
2. Documentar autenticación y errores.
3. Definir timeouts y reintentos.
4. No duplicar la fuente autorizada.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Cada integración tiene contrato documentado.
- [ ] Los endpoints propuestos están marcados como tales.
- [ ] Errores y timeouts definidos.
- [ ] Sin contradicciones con otros repos.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- `docs/contratos-integracion.md`
- specs de endpoints

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
