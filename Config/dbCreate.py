import pandas as pd

# Falta criar um Schema

user ={
    'Nome': [],
    'Idade': [],
    'Cidade': [],
    'Status': [],
    'Telefone':[],
    'Email': [],
    'CEP':[]
}

# Criando o Data frame
df_user =pd.Datarame(user)
 
# Cadastro de Objetos
cadastro={
    'Andar': [],
    'Bloco': [],
    'Mesa': [],
    'Status': [],
    'Data':[]
}
df_cadastro = pd.DataFrame(cadastro)

# Historico
data={
    'Data': [],
    'Status': [],
}

df_data=pd.DataFrame(data)

print(df_user,df_cadastro,df_data)


