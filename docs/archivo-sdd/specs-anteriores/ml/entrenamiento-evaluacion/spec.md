# Entrenamiento, evaluación y versionado del modelo

> Repositorio: BusTrack ML · Ruta: `specs/ml/entrenamiento-evaluacion/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `ml/entrenamiento-evaluacion`
- **Nombre:** Entrenamiento, evaluación y versionado del modelo
- **Repositorio:** BusTrack ML

## 2. Objetivo

Especificar entrenamiento, evaluación, selección y versionado del modelo de detección de paradas.

## 3. Contexto

No existe modelo ni dataset.

## 4. Alcance

**Incluye:**

- Dataset y etiquetado.
- Algoritmos candidatos.
- Métricas F1/precisión/recall.
- Validación cruzada.
- Versionado de artefactos.

**No incluye:**

- Entrenar con datos sin consentimiento.
- Publicar modelos sin evaluación.
- Usar datos personales.

## 5. Requisitos funcionales

1. Documentar dataset y licencia.
2. Fijar semillas y parámetros.
3. Registrar métricas y artefactos.
4. No promover modelos bajo el umbral.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.

## 8. Criterios de aceptación

- [ ] Pipeline de entrenamiento ejecutable.
- [ ] Métricas reportadas.
- [ ] Modelo versionado.
- [ ] Umbral de promoción definido.

## 9. Restricciones

- No declarar métricas no medidas.
- No inventar dataset.

## 10. Dependencias

- specs/ml/pipeline-acelerometro/
- specs/azure/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
