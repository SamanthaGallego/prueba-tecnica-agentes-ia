import json
import os

def procesar_tickets_txt(ruta_entrada, ruta_salida):
    tickets_criticos = []
    
    if not os.path.exists(ruta_entrada):
        print(f"Error: El archivo '{ruta_entrada}' no se encontró en el directorio.")
        return

    try:
        with open(ruta_entrada, mode='r', encoding='utf-8') as archivo_txt:
            lineas = archivo_txt.readlines()
            
            if not lineas:
                print("Error: El archivo de texto está vacío.")
                return
            
            encabezados = [h.strip().lower() for h in lineas[0].split(';')]
            
            for linea in lineas[1:]:
                if not linea.strip():
                    continue 
                
                valores = [v.strip() for v in linea.split(';')]
                fila = dict(zip(encabezados, valores))
                
                if fila.get('estado', '').lower() == 'pendiente' and \
                   fila.get('prioridad', '').lower() == 'alta':
                    tickets_criticos.append(fila)
        
        with open(ruta_salida, mode='w', encoding='utf-8') as archivo_json:
            json.dump(tickets_criticos, archivo_json, indent=4, ensure_ascii=False)
            
        print(f"Éxito: Se filtraron {len(tickets_criticos)} tickets críticos. Archivo guardado como '{ruta_salida}'.")

    except Exception as e:
        print(f"Error crítico durante el procesamiento de los datos: {e}")

if __name__ == "__main__":
    archivo_input = "tickets.txt"
    archivo_output = "tickets_criticos.json"
    procesar_tickets_txt(archivo_input, archivo_output)