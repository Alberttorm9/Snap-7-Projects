from opcua import Server

def cargar_valor():
    try:
        with open("valor_guardado.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return None

def guardar_valor(valor):
    with open("valor_guardado.txt", "w") as file:
        file.write(str(valor))

def iniciar_servidor():
    print ("Initializing OPC")
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    server.set_server_name("Servidor OPC UA de ejemplo")
    uri = "http://example.org"
    idx = server.register_namespace(uri)
    print ("OPC Server Initialized")
    # Agregar nodos al servidor
    node = server.nodes.objects.add_object(idx, "MiObjeto")

    # Intentar cargar el valor guardado
    valor_guardado = cargar_valor()
    if valor_guardado is not None:
        var = node.add_variable(idx, "MiVariable", valor_guardado)
    else:
        var = node.add_variable(idx, "MiVariable", 1)

    var.set_writable()  # Para que sea escribible

    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # Guardar el valor antes de detener el servidor
        valor_actual = var.get_value()
        guardar_valor(valor_actual)
        server.stop()

if __name__ == "__main__":
    print ("Opening")
    iniciar_servidor()
