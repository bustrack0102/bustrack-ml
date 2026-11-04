# CI/CD y gates de calidad

> Repositorio: BusTrack ML · Ruta: `specs/cicd/` · Estado: Parcial · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `cicd`
- **Nombre:** CI/CD y gates de calidad
- **Repositorio:** BusTrack ML

## 2. Objetivo

Definir el pipeline de BusTrack ML con gates bloqueantes y artefactos verificables.

## 3. Contexto

Herramientas objetivo: GitHub Actions, black --check, flake8, pytest, cobertura, Semgrep (Python) y pip-audit.

## 4. Alcance

**Incluye:**

- Lint, formato, pruebas, SAST, SCA y secretos.
- Artefactos y cobertura.
- Reglas de rama y PR.
- Sin despliegue real en esta fase.

**No incluye:**

- Despliegue automático a Azure.
- Servicios de pago.

## 5. Requisitos funcionales

1. Todo PR ejecuta lint + pruebas + SAST.
2. Los fallos bloquean la fusión.
3. No se usan secretos productivos en PR.
4. Se conservan artefactos útiles.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] El workflow se ejecuta en PR.
- [ ] Un fallo de lint/test/SAST pone el check en rojo.
- [ ] La cobertura se genera o se documenta su ausencia.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- .github/workflows/
- specs/pruebas/
- specs/seguridad/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
