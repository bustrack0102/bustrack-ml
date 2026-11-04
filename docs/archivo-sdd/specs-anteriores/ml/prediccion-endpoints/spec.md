# Endpoints internos de inferencia

> Repositorio: BusTrack ML · Ruta: `specs/ml/prediccion-endpoints/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `ml/prediccion-endpoints`
- **Nombre:** Endpoints internos de inferencia
- **Repositorio:** BusTrack ML

## 2. Objetivo

Especificar los endpoints internos de salud e inferencia del servicio ML.

## 3. Contexto

El servicio será consumido por la API, no por clientes.

## 4. Alcance

**Incluye:**

- Health interno.
- Inferencia por lote.
- Esquema de entrada/salida.
- Errores y límites.

**No incluye:**

- Endpoints públicos.
- Login de usuario.
- Acceso desde Flutter/Angular.

## 5. Requisitos funcionales

1. Solo la API puede invocar el servicio.
2. Validar esquema y tamaño.
3. Devolver resultados con confianza.
4. No exponer PII.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Contrato documentado.
- [ ] 401/403 sin credencial interna.
- [ ] Lote inválido 422.
- [ ] Resultado con score.

## 9. Restricciones

- No inventar endpoints implementados.
- No exponer el servicio a Internet.

## 10. Dependencias

- specs/ml/pipeline-acelerometro/
- docs/contratos-integracion.md

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
