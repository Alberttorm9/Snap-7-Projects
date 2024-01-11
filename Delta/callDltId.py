import win32com.client
import re
from datetime import datetime

#Confs
patron = r"\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{4}\b"
provincias = ["Álava", "Albacete", "Alicante", "Almería", "Ávila", "Badajoz", "Barcelona", "Burgos", "Cáceres", "Cádiz", "Castellón", "Ciudad Real", "Córdoba", "La Coruña", "Cuenca", "Gerona", "Granada", "Guadalajara", "Guipúzcoa", "Huelva", "Huesca", "Islas Baleares", "Jaén", "León", "Lérida", "Lugo", "Madrid", "Málaga", "Murcia", "Navarra", "Orense", "Palencia", "Las Palmas", "Pontevedra", "La Rioja", "Salamanca", "Segovia", "Sevilla", "Soria", "Tarragona", "Santa Cruz de Tenerife", "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza", "Ceuta", "Melilla"]
localidades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia", "Palma", "Bilbao", "Alicante", "Córdoba", "Valladolid", "Vigo", "Gijón", "Hospitalet de Llobregat", "La Coruña", "Granada", "Vitoria", "Elche", "Santa Cruz de Tenerife", "Oviedo", "Badalona", "Cartagena", "Terrassa", "Jerez de la Frontera", "Sabadell", "Móstoles", "Santander", "Pamplona", "Almería"]

def comprobar_provincia(texto):
    for provincia in provincias:
        if provincia.lower() in texto.lower():
            return True
    return False

def comprobar_localidad(texto):
    for localidad in localidades:
        if localidad.lower() in texto.lower():
            return True
    return False

dltid = win32com.client.Dispatch("DltIdAx4.DltIdAx")
retval = dltid.DLTGetDocument(0, 1)


while retval < 0:
    print(f"Error -> {retval} ({dltid.DLTGetError(retval)})")
    retval = dltid.DLTGetDocument(0, 1, )

else:
    if len(dltid.DLTGetNumeroDocumento())==9:
        print(f"NumeroDocumento : {dltid.DLTGetNumeroDocumento()}")
    elif(len(dltid.DLTGetNumeroDocumento())!=9 and len(dltid.DLTGetNumeroDocumento())!=0):
        print("ERROR EN EL NUMERO DE DNI")
    else:
        print(f"NumeroPassaporte : {dltid.DLTGetNumeroPassaporte()}")
    print(f"TipoDocumento : {dltid.DLTGetTipoDocumento()}")
    print(f"Apellido1 : {dltid.DLTGetApellido1()}")
    print(f"Apellido2 : {dltid.DLTGetApellido2()}")
    print(f"Nombre : {dltid.DLTGetNombre()}")
    if len(dltid.DLTGetSexo())=="M" or len(dltid.DLTGetSexo())=="F":
        print(f"Sexo : {dltid.DLTGetSexo()}")
    print(f"Pais : {dltid.DLTGetPais()}")
    if len(dltid.DLTGetNacionalidad())==3:
        print(f"Nacionalidad : {dltid.DLTGetNacionalidad()}")
    else:
        print("ERROR EN LA NACIONALIDAD")

    print(f"Domicilio1 : {dltid.DLTGetDomicilio1()}")

    print(f"Domicilio2 : {dltid.DLTGetDomicilio2()}")

    print(f"Domicilio3 : {dltid.DLTGetDomicilio3()}")

    if comprobar_localidad(dltid.DLTGetProvinciaNacimiento()):
        print(f"LocalidadNacimiento : {dltid.DLTGetLocalidadNacimiento()}")
    else:
        print("ERROR EN LA LOCALIDAD")

    if comprobar_provincia(dltid.DLTGetProvinciaNacimiento()):
        print(f"ProvinciaNacimiento : {dltid.DLTGetProvinciaNacimiento()}")
    else:
        print("ERROR EN LA PROVINCIA")

    if "/" in dltid.DLTGetHijoDe():
        print(f"Hijo De : {dltid.DLTGetHijoDe()}")
    else:
        print("ERROR EN PROGENITORES")

    try:
        datetime.strptime(dltid.DLTGetFechaNacimiento(), '%d%m%Y')
        print(f"FechaNacimiento : {dltid.DLTGetFechaNacimiento()}")
    except Exception:
        print("ERROR EN LA FECHA DE NACIMIENTO")

    try:
        datetime.strptime(dltid.DLTGetFechaValidez(), '%d%m%Y')
        print(f"FechaNacimiento : {dltid.DLTGetFechaValidez()}")
    except Exception:
        print("ERROR EN LA FECHA DE VALIDEZ")

    try:
        datetime.strptime(dltid.DLTGetFechaExpedicion(), '%d%m%Y')
        print(f"FechaNacimiento : {dltid.DLTGetFechaExpedicion()}")
    except Exception:
        print("ERROR EN LA FECHA DE EXPEDICION") 

    print(f"OCRB : {dltid.DLTGetOCRB()}")


# if re.match(patron, dltid.DLTGetFechaNacimiento()):
#         print(f"FechaNacimiento : {dltid.DLTGetFechaNacimiento()}")
#     else:
#         print("ERROR EN LA FECHA DE NACIMIENTO")