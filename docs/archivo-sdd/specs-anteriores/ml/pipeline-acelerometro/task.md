# Tareas — Pipeline de procesamiento de acelerómetro

> Spec: `spec.md` · Plan: `plan.md` · Estado: Pendiente.
> Marcar solo con evidencia. No marcar por documentar.

## Dependencias entre tareas

1. T01 antes de T02
2. T02 antes de T03

## Tareas

### T01. Definir esquema de lote

- Campos.
- Unidades.
- Límites.

**Archivos:** spec.md

**Terminado cuando:** Esquema validado con Pydantic.

### T02. Definir preprocesamiento

- Limpieza.
- Ventanas.
- Features.

**Archivos:** plan.md

**Terminado cuando:** Pipeline reproducible documentado.

### T03. Definir pruebas

- Válidos.
- Inválidos.
- Reproducibilidad.

**Archivos:** task.md

**Terminado cuando:** Casos verificables.

## Cierre

- [ ] Todas las tareas con evidencia.
- [ ] `Memoria.md` actualizado.
- [ ] Pruebas y gates ejecutados.
- [ ] Sin afirmaciones de implementación no verificadas.
