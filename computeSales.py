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
    price_map = {}
    # Soporta tanto 'title'/'price' como 'Product'/'Price'
    for item in catalogue:
        name = item.get('title') or item.get('Product')
        price = item.get('price') or item.get('Price')
        if name is not None:
            price_map[name] = price

    for sale in sales:
        # Intenta obtener el nombre del producto en ambos formatos
        product = sale.get('product') or sale.get('Product')
        quantity = sale.get('quantity') or sale.get('Quantity') or 0
        
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

    # Llamar a las funciones
    catalogue_data = load_json(price_file)
    sales_data = load_json(sales_file)

    if catalogue_data is None or sales_data is None:
        print("Error: No se pudieron cargar los datos necesarios.")
        return

    # Asignar a total_cost para evitar NameError
    total_cost = calculate_total(catalogue_data, sales_data)

    print(f"Archivos recibidos: {price_file} y {sales_file}")
    elapsed_time = time.time() - start_time  # Tiempo transcurrido

    results = (
        "---------- Sales Results ----------\n"
        f"Total Sales Cost: ${total_cost:,.2f}\n"
        f"Execution Time: {elapsed_time:.4f} seconds\n"
        "-----------------------------------\n"
    )

    # Req 2: Imprimir en pantalla y en archivo
    print(results)

    try:
        file_name = r"results\SalesResults.txt"
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(results)
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

if __name__ == "__main__":
    main()
