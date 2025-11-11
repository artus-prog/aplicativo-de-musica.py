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
while True:
   print("Bem vindo a sla aplicativo de música")
   login()
   break