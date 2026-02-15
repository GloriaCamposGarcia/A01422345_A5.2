import sys
import time
import json

def load_json(file_path):
    """Carga archivos JSON y maneja datos inválidos."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        # Muestra el error y continua la ejecución
        print(f"Error procesando '{file_path}': {error}")
        return None

def calculate_total(catalogue, sales):
    """Calcula el costo total de catálogo y ventas."""
    total = 0.0
    # Crea mapa de precios para eficiencia
    price_map = {item['title']: item['price'] for item in catalogue if 'title' in item}

    for sale in sales:
        product = sale.get('product')
        quantity = sale.get('quantity', 0)
        
        if product in price_map:
            total += price_map[product] * quantity
        else:
            print(f"Advertencia: El producto '{product}' no está en el catálogo.")
    return total

def main():
    start_time = time.time()  # Inicio de tiempo

    """Función principal para coordinar la ejecución."""
    # Validar que se reciban los dos archivos como parámetros: python computeSales.py file1 file2
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    # Simulación de carga de archivos
    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    print(f"Archivos recibidos: {price_file} y {sales_file}")

    elapsed_time = time.time() - start_time  # Tiempo transcurrido
    print(f"Time elapsed: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
