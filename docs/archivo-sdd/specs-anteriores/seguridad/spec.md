# Seguridad y privacidad

> Repositorio: BusTrack ML · Ruta: `specs/seguridad/` · Estado: Parcial · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `seguridad`
- **Nombre:** Seguridad y privacidad
- **Repositorio:** BusTrack ML

## 2. Objetivo

Fijar los controles de seguridad y privacidad de Servicio de Machine Learning.

## 3. Contexto

Validación Pydantic, anonimización, límites de tamaño, sin secretos y sin pickle de origen no confiable.

## 4. Alcance

**Incluye:**

- Autenticación/autorización.
- Validación y codificación.
- Gestión de secretos.
- Logs y datos sensibles.
- Consentimiento de sensores cuando aplique.

**No incluye:**

- Implementar controles de otro servicio.
- Desplegar WAF o servicios Azure.

## 5. Requisitos funcionales

1. Validar todas las entradas.
2. No registrar secretos/PII.
3. Aplicar mínimo privilegio.
4. Documentar amenazas y controles.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Controles documentados y probados.
- [ ] Semgrep ejecutable y bloqueante.
- [ ] Pruebas de seguridad en verde.
- [ ] Sin hallazgos críticos abiertos.

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
