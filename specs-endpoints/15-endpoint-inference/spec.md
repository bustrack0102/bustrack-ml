# 15-endpoint-inference — Endpoint interno de inferencia

> Repositorio: BusTrack ML · Endpoint: `POST /inference` · Estado: Implementado · Fecha: 2026-11-11.

## 1. Objetivo

Clasificar un lote de acelerómetro y devolver paradas detectadas.

## 2. Contrato

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/inference` |
| Autenticación | Token interno o identidad administrada; sin login público. |
| Consumidor | API central |
| Estado | Implementado |

**Parámetros / entrada:**

- Body: lote anonimizado, frecuencia y ventanas.

**Respuesta:**

- 200: paradas + score.
- 401/403: sin credencial interna.
- 422: lote inválido.
- 413: lote demasiado grande.

## 3. Códigos HTTP

- 200/201: éxito.
- 400/422: validación.
- 401/403: autenticación/autorización.
- 404: recurso inexistente.
- 409: conflicto.
- 429: rate limit.
- 500: error interno sin detalles.

## 4. Validaciones

1. Esquema Pydantic.
2. Límite de tamaño.
3. Sin PII.

## 5. Seguridad

- Validación Pydantic, anonimización, límites de tamaño, sin secretos y sin pickle de origen no confiable.
- No registrar tokens, credenciales ni PII.

## 6. Criterios de aceptación

- [ ] La tarea tiene criterios verificables y evidencia asociada.
- [ ] No se declara implementado lo que no existe en código o pruebas.
- [ ] Los contratos consumidos o expuestos quedan documentados.
- [ ] `Memoria.md` refleja el estado resultante.

## 7. Dependencias

- `docs/contratos-integracion.md`
- `spec.md` de la tarea funcional asociada

## Aprobación

- [x] Revisión de arquitectura y contrato realizada — fecha: 2026-11-11
- [x] CHECKLIST_PR.md validado
- [x] Sin conflicto con constitution.md
