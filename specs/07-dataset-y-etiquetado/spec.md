# 07-dataset-y-etiquetado — Dataset y etiquetado

> Repositorio: BusTrack ML · Estado: Parcial · Fecha: 2026-11-11.

## 1. Objetivo

Definir origen, consentimiento, etiquetado y calidad del dataset.

## 2. Contexto

No existe dataset ni proceso de etiquetado.

## 3. Alcance

**Incluye:**

- Fuente de datos.
- Consentimiento.
- Etiquetado.
- Calidad y licencia.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. Datos con consentimiento.
2. Etiquetas documentadas.
3. Licencia compatible.
4. Sin PII.

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

## Aprobación

- [x] Revisión de arquitectura y contrato realizada — fecha: 2026-11-11
- [x] CHECKLIST_PR.md validado
- [x] Sin conflicto con constitution.md
