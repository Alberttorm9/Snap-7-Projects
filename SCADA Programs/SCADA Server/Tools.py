import configparser
config = configparser.ConfigParser()
config.read('SCADA Programs\SCADA Server\Caracteristicas_Habitaciones.ini')
def resolucion():
    return config["Ajustes"]["ResolucionX"]+"x"+config["Ajustes"]["ResolucionY"]
def NumHabitaciones():
    return eval(config["Ajustes"]["NumHabitaciones"])
def resolucionX():
    return eval(config["Ajustes"]["ResolucionX"])
def resolucionY():
    return eval(config["Ajustes"]["ResolucionY"])
def info_habs():
    Habitaciones = []
    for i in range(1, eval(config["Ajustes"]["NumHabitaciones"])+1):
        Habitacion = (
            config[f'Habitacion{i}']['Tipo'],
            eval(config[f'Habitacion{i}']['Precio1']),
            eval(config[f'Habitacion{i}']['Precio2']),
            eval(config[f'Habitacion{i}']['Precio3']),
            config[f'Habitacion{i}']['Info']    
        )
        Habitaciones.append(Habitacion)
    return Habitaciones