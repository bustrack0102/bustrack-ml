# Pipeline de procesamiento de acelerómetro

> Repositorio: BusTrack ML · Ruta: `specs/ml/pipeline-acelerometro/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `ml/pipeline-acelerometro`
- **Nombre:** Pipeline de procesamiento de acelerómetro
- **Repositorio:** BusTrack ML

## 2. Objetivo

Especificar ingesta, validación, anonimización y preprocesamiento de lotes de acelerómetro.

## 3. Contexto

El servicio ML no tiene código.

## 4. Alcance

**Incluye:**

- Esquema de lote.
- Validación y límites.
- Anonimización.
- Limpieza, normalización y ventanas.
- Extracción de características.

**No incluye:**

- Captura en el dispositivo.
- Almacenamiento de PII.
- Rastreo GPS.

## 5. Requisitos funcionales

1. Rechazar lotes inválidos.
2. Eliminar identificadores personales.
3. Documentar unidades y frecuencias.
4. Mantener trazabilidad sin PII.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Esquema documentado y validado.
- [ ] Lote inválido rechazado.
- [ ] Características reproducibles.
- [ ] Sin PII en logs.

## 9. Restricciones

- No implementar en esta fase.
- No inventar el esquema del dispositivo.

## 10. Dependencias

- docs/contratos-integracion.md
- specs/ml/entrenamiento-evaluacion/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
