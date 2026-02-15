import sys

def main():
    """Función principal para coordinar la ejecución."""
    # Validar que se reciban los dos archivos como parámetros: python computeSales.py file1 file2
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    # Simulación de carga de archivos
    price_file = sys.argv[5]
    sales_file = sys.argv[6]

    print(f"Archivos recibidos: {price_file} y {sales_file}")

if __name__ == "__main__":
    main()
