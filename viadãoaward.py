#Modulos
from random import choice
from pygame import mixer, init, event
from time import sleep

#Apresentação
init()
mixer.music.load('Introdução.mp3')
mixer.music.play(loops=10)

print('\033[1;33;m-=-\033[m' *29)
print('\033[1;32;mSENHORAS E SENHORES, BEM VINDOS A GRANDE PREMIAÇÃO, DO VIADÃO TÚ ÈS!!!\033[m')
print('\033[1;33;m-=-\033[m' *29)
print('\033[1;32;mA SEGUIR, TEREMOS O NOME DOS CONCORRENTES DA NOITE!!!\033[m')
print('\033[1;33;m-=-\033[m' *29)
sleep(2)

#Participantes
n1 = str(input('\033[1;34;mNOME DO PRIMEIRO CONCORRENTE: \033[m').upper().strip())
n2 = str(input('\033[1;34;mNOME DO SEGUNDO CONCORRENTE: \033[m').upper().strip())
n3 = str(input('\033[1;34;mNOME DO TERCEIRO CONCORRENTE: \033[m').upper().strip())
n4 = str(input('\033[1;34;mNOME DO QUARTO CONCORRENTE: \033[m').upper().strip())


#Variaveis para o Sorteio
lista = [n1, n2, n3, n4]
vencedor = choice(lista)

#Apresentação²
print('\033[1;33;m-=-\033[m' *29)
print('\033[1;32;mCONCORRENTES LISTADOS, VAMOS DIRETO PARA VOTAÇÃO!!\033[m')
print('\033[1;33;m-=-\033[m' *29)
input('\033[1;32;mPRESSIONE QUALQUER BOTÃO, PARA INICIAR A VOTAÇÃO!\033[m')
print('\033[1;33;m-=-\033[m' *29)

mixer.music.load('tambor.mp3')
mixer.music.play()

#Imprimir na tela o vencedor
print('\033[1;31;mVOTAÇÃO INICIADA...\033[m')
sleep(5)
print('\033[1;31;mVOTAÇÂO ENCERRADA!\033[m')
mixer.music.load('resultado.mp3')
mixer.music.play(loops=5)

#easter egg
if vencedor == 'MISTER':
    print('\033[1;33;m-=-\033[m' *29)
    print('\033[1;32;mWHOU, O QUE É ISSO?...\033[m')
    sleep(1)
    print('\033[1;33;m-=-\033[m' *29)
    print('\033[1;32;mINACREDITAVEL...\033[m')
    sleep(1)
    print('\033[1;33;m-=-\033[m' * 29)
    print('\033[1;32;mO PODER DE VIADAGEM DESSE CARA É + DE 8000...\033[m')
    sleep(1)
    print('\033[1;33;m-=-\033[m' * 29)
    print('\033[1;32;mO GRANDE VENCEDOR DA NOITE É O VIADÃO DO MISTER!!!\033[m ')
    print('\033[1;33;m-=-\033[m' *29)
else:
    print('\033[1;33;m-=-\033[m' *29)
    print(f'\033[1;32;mO NOVO VENCEDOR DO DIGNISSIMO PREMIO VIADÃO TÚ ÈS, É O CONCORRENTE: {vencedor}!\033[m')
    print('\033[1;33;m-=-\033[m' *29)

#CREDITOS
sleep(5)
input('\033[1;37;mPressione Enter para ver os creditos!\033[m')
print('CREDITOS: https://soundcloud.com/nathanfleet/action-drums')
print('Desenvolvido por R3GR3TS')
