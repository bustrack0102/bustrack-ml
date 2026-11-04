# 08-entrenamiento-del-modelo — Entrenamiento del modelo

> Repositorio: BusTrack ML · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Objetivo

Entrenar el modelo de detección de paradas con un protocolo reproducible.

## 2. Contexto

No existe modelo.

## 3. Alcance

**Incluye:**

- Algoritmos candidatos.
- Semillas.
- Particiones.
- Artefactos.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. Semillas fijas.
2. Particiones train/validation/test.
3. Sin fuga de datos.
4. Registrar parámetros.

## 5. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad tarea -> prueba -> evidencia.

## 6. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 7. Criterios de aceptación

- [ ] La tarea tiene criterios verificables y evidencia asociada.
- [ ] No se declara implementado lo que no existe en código o pruebas.
- [ ] Los contratos consumidos o expuestos quedan documentados.
- [ ] `Memoria.md` refleja el estado resultante.

## 8. Dependencias

- `constitution.md`
- `docs/contratos-integracion.md`

## 9. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
