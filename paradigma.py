import json

class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def ingresar_nota(self, nota):
        self.notas.append(nota)

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def modificar_datos(self, notas=None, faltas=None, amonestaciones=None):
        if notas is not None:
            self.notas = notas
        if faltas is not None:
            self.faltas = faltas
        if amonestaciones is not None:
            self.amonestaciones = amonestaciones

    def expulsar(self):
        print(f"Alumno {self.nombre} {self.apellido} expulsado.")

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nDNI: {self.dni}\nFecha de nacimiento: {self.fecha_nacimiento}\nTutor: {self.tutor}\nNotas: {self.notas}\nFaltas: {self.faltas}\nAmonestaciones: {self.amonestaciones}"

def cargar():
    try:
        with open("alumnos.json", "r") as archivoalumnos:
            data = json.load(archivoalumnos)
            alumnos = []
            for alumno_data in data:
                alumno = Alumno(alumno_data["Nombre"], alumno_data["Apellido"], alumno_data["DNI"], alumno_data["Fecha de nacimiento"], alumno_data["Tutor"])
                alumno.notas = alumno_data["Notas"]
                alumno.faltas = alumno_data["Faltas"]
                alumno.amonestaciones = alumno_data["amonestaciones"]
                alumnos.append(alumno)
            return alumnos
    except FileNotFoundError:
        return []

def guardar(alumnos):
    data = []
    for alumno in alumnos:
        alumno_data = {
            "Nombre": alumno.nombre,
            "Apellido": alumno.apellido,
            "DNI": alumno.dni,
            "Fecha de nacimiento": alumno.fecha_nacimiento,
            "Tutor": alumno.tutor,
            "Notas": alumno.notas,
            "Faltas": alumno.faltas,
            "amonestaciones": alumno.amonestaciones
        }
        data.append(alumno_data)
    with open("alumnos.json", 'w') as archivoalumnos:
        json.dump(data, archivoalumnos)

alumnos = cargar()

if not alumnos:
    alumnos.append(Alumno("Estefania", "Guzman", "46532123", "19/11/1990", "Yolanda Jaime"))
    alumnos.append(Alumno("Carolina", "Reynaga", "25571412", "27/09/1985", "Cristina Lopez"))

alumnos[0].ingresar_nota(4)
alumnos[0].ingresar_nota(7)
alumnos[0].ingresar_nota(6)
alumnos[0].asignar_falta()
alumnos[0].asignar_amonestacion()

alumnos[1].ingresar_nota(9)
alumnos[1].ingresar_nota(7)
alumnos[1].ingresar_nota(6)
alumnos[1].asignar_falta()

guardar(alumnos)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i}:")
    print(alumno)

alumnos[0].modificar_datos(notas=[6, 8, 7], faltas=9, amonestaciones=4)
alumnos[1].modificar_datos(notas=[10, 5, 9], faltas=3, amonestaciones=1)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i} después de modificar datos:")
    print(alumno)

alumnos[0].expulsar()
alumnos.pop(0)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i} después de expulsar:")
    print(alumno)
