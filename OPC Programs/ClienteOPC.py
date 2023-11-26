from opcua import Client

def listar_nodos(client):
    root = client.get_root_node()

    print("Nodos disponibles en el servidor:")
    for node in root.get_children():
        print(f"{node.get_browse_name()} - NodeId: {node.nodeid}")

def modificar_valor(client):
    while True:
        listar_nodos(client)  # Listar nodos disponibles

        # Pedir al usuario que introduzca el NodeId
        node_id = input("Introduce el NodeId de la variable (o 'q' para salir): ")

        if node_id.lower() == 'q':
            break

        # Obtener la variable
        var = client.get_node(node_id)

        # Leer el valor actual
        value = var.get_value()
        print("Valor actual de la variable:", value)

        # Pedir al usuario que introduzca un nuevo valor
        nuevo_valor = int(input("Introduce un nuevo valor: "))

        # Cambiar el valor
        var.set_value(nuevo_valor)

        # Verificar que el valor haya sido actualizado
        updated_value = var.get_value()
        print("Valor actualizado de la variable:", updated_value)

def main():
    # Dirección del servidor OPC UA
    server_url = "opc.tcp://localhost:4840/freeopcua/server/"

    # Crear instancia del cliente
    client = Client(server_url)

    try:
        # Conectarse al servidor
        client.connect()

        modificar_valor(client)

    finally:
        # Desconectar del servidor
        client.disconnect()

if __name__ == "__main__":
    main()
