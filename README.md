# Prueba Técnica: Orquestación de Agentes y Automatización

Este repositorio contiene la solución a la prueba técnica para el rol de Analista de Inteligencia Artificial.

## Reto 1: Lógica y Orquestación de Agentes (Recursos Humanos)
A continuación se presenta la arquitectura del agente conversacional diseñado en Microsoft Copilot Studio para atender la solicitud de certificados laborales.

### 1. Desencadenador (Reconocimiento de Intención)
El agente utiliza un modelo generativo entrenado con frases clave para enrutar la solicitud del usuario correctamente.
![Desencadenador](diagramas/reto1_1.png)

### 2. Extracción de Entidades y Validación
Se solicitan dos datos clave (Número de documento y Área). El sistema valida que el documento contenga únicamente caracteres numéricos.
![Validación de Datos](diagramas/reto1_2.png)

### 3. Llamada a Acción Externa (API Rest)
El agente consume una API a través de una solicitud HTTP POST, enviando los datos recolectados de forma segura en el cuerpo de la petición.
![Solicitud HTTP](diagramas/reto1_3.png)

### 4. Manejo de Errores y Respuesta Final (Fallback)
Se evalúa la respuesta del servidor. Si es exitosa, se entrega el PDF; si falla, se realiza una transferencia (handoff) a un agente humano.
![Fallback](diagramas/reto1_4.png)