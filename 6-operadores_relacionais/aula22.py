# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira será invalidada naquele valor
# São considerados falsy (Que você já viu)
# 0 0.0 '' False
# Tambem existe o tipo None que é
# usado para representar ou não valor

#entrada = input('[E] entrar [S] sair: ')
#senha_digitada = input('Senha: ')
 
#senha_permitida = '123456'
 
#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
#else:
#    print('Sair')


# senha = 0 or False or 0 or 'abc' or True

senha = input('Senha: ') or 'Sem senha'
print(senha)