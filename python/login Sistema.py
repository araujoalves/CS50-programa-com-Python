import hashlib
import time

# Banco de dados de usuários (apenas para fins de demonstração)
database = {
    "usuario1": "5f4dcc3b5aa765d61d8327deb882cf99",  # senha1 em MD5
    "usuario2": "202cb962ac59075b964b07152d234b70",  # senha2 em MD5
    "usuario3": "81dc9bdb52d04dc20036dbd8313ed055",  # senha3 em MD5
    "daniel": hashlib.md5("4141".encode()).hexdigest()  # nova entrada para o usuário "daniel"
}

def login():
    while True:
        username = input("Usuário: ")
        password = input("Senha: ")
        
        if username in database and database[username] == hashlib.md5(password.encode('utf-8')).hexdigest():
            print("Bem-vindo, " + username + "!")
            change_password = input("Deseja alterar sua senha? (s/n) ")
            if change_password == "s":
                new_password = input("Digite sua nova senha: ")
                database[username] = hashlib.md5(new_password.encode('utf-8')).hexdigest()
                print("Senha alterada com sucesso!")
            return
        else:
            print("Usuário ou senha inválidos.")
            time.sleep(2)

login()
