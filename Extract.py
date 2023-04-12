import psycopg2

listAlunos = []
listProfessores = []


#criando conexão com o postgres
connectionDataSource = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "$1790",
    database="dataSource",

)
#criação do cursor para interações com o banco
cursor = connectionDataSource.cursor()
# extraindo dados da tabela alunos


cursorProfessor = cursor.execute("SELECT cod_prof, nom_prof, email FROM professores",connectionDataSource)
getDataProfessor = cursor.fetchall()

cursorAlunos = cursor.execute("SELECT mat_alu,dat_nasc, tot_cred, mgp, nom_alu, email FROM alunos" , connectionDataSource)
getDataAlunos = cursor.fetchall();

for row in getDataProfessor:
    #print(row[0])
    value = row[0],row[1],row[2]
    listProfessores.append(value)

for row in getDataAlunos:
    value = row[0], row[1] , row[2] , row[3] , row[4], row[5]
    listAlunos.append(value)

print(listAlunos)
print(listProfessores)



