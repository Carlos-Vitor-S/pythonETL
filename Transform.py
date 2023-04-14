from Extract import listAlunos,listProfessores,listDisciplinas,listTurmas,listCursos,listHistoricoTempo,listHistoricoEscolar

listAlunosTransformada = []
listProfessorTransformada = []
listDisciplinasTransformada = []
listTurmasTransformada = []
listCursosTransformada = []
listTempoTransformada = []
listHistoricoEscolarTransformada = []


#chaves
sk_turmas = 0
sk_tempo = 0


nk_alunos = 0
nk_disc = 0
nk_professores = 0
nk_turmas = 0
nk_cursos = 0
nk_tempo=0




#Transformação da tabela de disciplinas

for index in listDisciplinas:
    nk_disc = index[0]
    values = index[0],index[1],index[2],nk_disc
    listDisciplinasTransformada.append(values)
#Transformação da tabela de professores

for index in listProfessores:
    nk_professores = index[0]
    values = index[0],index[1],nk_professores
    listProfessorTransformada.append(values)
#Transformação da tabela alunos

for index in listAlunos:
    nk_alunos = index[0]
    values = index[0],index[1],index[2],index[3],index[4], nk_alunos
    listAlunosTransformada.append(values)
#Transformação da tabela turmas

for index in listTurmas:
    sk_turmas+=1
    nk_turmas+=1
    values= sk_turmas,index[0],index[1],nk_turmas
    listTurmasTransformada.append(values)
#Transformação da tabela cursos

for index in listCursos:
    nk_cursos = index[0]
    values = index[0],index[1],index[2],nk_cursos
    listCursosTransformada.append(values)
#Transformação da tabela tempo

for index in listHistoricoTempo:
    sk_tempo +=1
    nk_tempo +=1
    values = sk_tempo,index[0],index[1],nk_tempo
    listTempoTransformada.append(values)
#Transformação da tabela fatos

for index in listHistoricoEscolar:
    #situacao,faltas,media
    values = index[0],index[1],index[2]
    listHistoricoEscolarTransformada.append(values)

print(listHistoricoEscolarTransformada)
print(listTempoTransformada)
print(f"Lista turmas transform: {listTurmasTransformada}")
print(f"lista alunos: {listAlunosTransformada}")
print(f"Disciplinas Transformadas: {listDisciplinasTransformada}")
print(f"Professores Transformados: {listProfessorTransformada}")






