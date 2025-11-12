playlists=[]
def login():
   login_inicial=bool(input("""Você está acessando este aplicativo pela primeira vez?
   Se sim, digite True.
   Caso contrário, digite False
   """))
   if login_inicial == True:
      usuario=input("Qual nome de usúario você deseja? ")
      senha=input("Digite a senha desejada: ")
      print(f"Seu nome de usuário é: {usuario} e sua senha é: {senha}")
   elif login_inicial == False:
      usuário_tentativa = input("Digite seu login: ")
      senha_tentativa = input("Digite sua senha: ")
      if usuário_tentativa == usuario and senha_tentativa == senha:
         print("Login aceito")
         entrar = True
def nova_playlist():
      nova_playlist=bool(input("""Você deseja adicionar uma nova playlist?
True para sim
False para não
 """))
      if nova_playlist==True:
         nome_playlist=input("Digite o nome da sua nova playlist: ")
         playlists.append(nome_playlist)
def main_site():
   if len(playlists)== 0:
      print("Você não possui nenhuma playlist salva!")
      nova_playlist()
while True:
   print("Bem vindo a sla aplicativo de música")
   login()
   main_site()
   break