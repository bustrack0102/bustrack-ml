# Autenticación interna (sin login público)

> Repositorio: BusTrack ML · Ruta: `specs/endpoints/login/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `endpoints/login`
- **Nombre:** Autenticación interna (sin login público)
- **Repositorio:** BusTrack ML

## 2. Objetivo

Documentar por qué Servicio de Machine Learning no expone login público y cómo se autentica internamente.

## 3. Contexto

No expone login público; se autentica internamente y solo la API puede invocarlo.

## 4. Alcance

**Incluye:**

- Autenticación servicio-a-servicio.
- Rechazo de llamadas no autorizadas.
- Rotación de credenciales internas.

**No incluye:**

- Login de usuarios finales.
- Gestión de cuentas.
- Sesiones de navegador.

## 5. Requisitos funcionales

1. Solo la API puede invocar el servicio.
2. Rechazar peticiones sin credencial interna válida.
3. No exponer endpoints de autenticación pública.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Petición sin credencial interna devuelve 401/403.
- [ ] Petición válida de la API es aceptada.
- [ ] No hay endpoints de login público.

## 9. Restricciones

- No implementar login genérico por copia de otro repo.

## 10. Dependencias

- API central
- `docs/contratos-integracion.md`

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
