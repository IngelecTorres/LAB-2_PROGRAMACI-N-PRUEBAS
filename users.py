# Se deben codificar las siguientes funciones y replicar la funcionalidad descrita en los comentarios
# Además, para la gestión de usuarios y preguntas se debe hacer uso de archivos

# La función recibe name y password
# Si el usuario ya existe deber retornar  "User already registered"
# Si el usuario no existe debe registrarlo y retornar  "User succesfully registered"
try:
    
    # Crea archivo my_data.txt
    file=open('C:\\Users\\Andresito Albaran\\Desktop\\Data.txt','xt')
    file.close()
except:
    # El bloque except se ejecuta si hay 
    # excepción, el archivo ya existe
    print('El archivo ya existe')

def load_users():
    users = {}
    with open('C:\\Users\\Andresito Albaran\\Desktop\\Data.txt', 'r') as file:
        for line in file:
            name, password, score = line.strip().split(',')
            users[name] = {'password': password, 'score': int(score)}
    return users

# Función para guardar usuarios en el archivo
def save_users(users):
    with open('C:\\Users\\Andresito Albaran\\Desktop\\Data.txt', 'w') as file:
        for name, data in users.items():
            file.write(f"{name},{data['password']},{data['score']}\n")

# Cargar usuarios al iniciar
registered_users = load_users()

#registered_users = {
    #"Andres": "123", "Juan": "123"
#}

def registerUser(name, password):
    # Se verifica si el usuario esta registrado en el archivo
    if name in registered_users:
        return "User already registered"
    else:
        # Aca se registra al usuario y se le asigna un puntaje inicial 
        registered_users[name] = {'password': password, 'score': 0}
        save_users(registered_users)  # Guardar cambios en el archivo
        return "User successfully registered"
# Función que abre o cierra una sesión
# Abre/cierra una sesión del usuario dependiendo del valor de flag 
# lo hace si el nombre de usuario y la contraseña son correctos
def openCloseSession(name, password, flag):
    if name not in registered_users:
        return "The name is incorrect"
    
    elif registered_users[name] != password:
        return "The password is incorrect"
    
    else:
        #Cuando el usuario no esta logeado la flag entra como false, lo que quiere decir que apenas va a iniciar sesion, cambiando la flag a True indicando que ya inicio sesion
        #Cuando la flag esta en estado true quiere decir que el usuario ya estaba logeado, por lo tanto la flag cambiara a false para referir que la sesion cerró 
        flag = not flag  # Cambia el estado de la sesión
        if flag:
            return "Login successful"
        else:
            return "Session closed"
  

# Función que actualiza el puntaje
# Actualiza el puntaje del usuario con el valor de score si el nombre de usuario y la contraseña 
# son correctos y si el usuario se encuentra con sesión abierta
def updateScore(name, password, score, flag):
    # Aca se verifica si el usuario puede iniciar o cerrar sesión
    # Luego lo que se hace es cambiar el estado de flag dentro de esta función
    flag = not flag  
    
    # Verifico si los datos que se dieron son correctos y estan almacenados
    if name in registered_users and registered_users[name] == password:
        if flag:
            # SI se inicio sesion correctamente se actualiza el puntaje
            score += 100
            return score, flag
        else:
            # Si la sesión está cerrada, no actualizamos el puntaje
            return "Session closed", flag
    else:
        # Si los datos que se dieron son incorrectos se genera un "error"
        return "Invalid credentials", flag

    
# Función que lee el puntaje
# Retorna el puntaje del usuario si el nombre de usuario y la contraseña 
# son correctos y si el usuario se encuentra con sesión abierta
def getScore(name, password):

    if name in registered_users and registered_users[name] == password:

        if openCloseSession(name, password, False) == "Login successful":
           
            return updateScore
        else:
           
            return "Session is closed"
    else:
        
        return "Invalid credentials"


# Función que lee la lista de usuarios conectados
# retorna una lista con los usuarios conectados, solo debe devolver nombre y puntaje
# si el nombre de usuario y la contraseña  son correctos y si el usuario se encuentra con sesión abierta
def usersList(name,password):
    pass
            
    
# Función que genera una pregunta en una categoría cat
# retorna la pregunta si el nombre de usuario y la contraseña  son correctos y si el usuario se encuentra con sesión abierta
def question(name,password,cat):
    pass
                
print(openCloseSession("Juan", "123", False))       
#print(registerUser("Juan", "123"))
#print(updateScore("Andres","123", 200))
#print(getScore("Andres","123", ))
    
            
    