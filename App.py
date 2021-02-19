import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Passo 1: abra o menu Iniciar e vá ao ícone de configurações. Passo 2: na aba de configurações, selecione a opção “Atualização e Segurança”. Passo 3: selecione, no menu lateral esquerdo, a opção “Recuperação”. Passo 4: na parte de “Restaurar o PC”, selecione a opção “Começar”.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Para recuperar arquivos corrompidos, é necessário utilizar programas de diagnóstico próprios. O mais confiável e acessível deles é o EaseUS Data Recovery Wizard, que é fácil de ser utilizado; no entanto, a quantidade de dados que ele pode recuperar gratuitamente é limitada a 500 MB no Windows, e a 2 GB no macOS.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} 1 - Insira o DVD ou o pen drive no computador. 2 - Execute o boot do Windows pelo disco de instalação. Se não souber como iniciar o boot pelo pen drive, siga este guia. 3 - Na tela de instalação, clique em Avançar e, depois, em Reparar o computador. 4 - Clique em Solução de Problemas -> Opções Avançadas -> Reparo de Inicialização. 5 - Clique em Windows 10 e aguarde o reparo.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} 1 - Faça o backup dos arquivos (opcional). ... 2 - Insira a mídia de instalação para o Windows no computador em que deseja instalar o sistema. ... 3 - Ligue o computador. ... 4 - Acesse o menu de inicialização. ... 5 - Selecione o pen drive que está usando como mídia de instalação para o Windows.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresetar o chatbot
    print('Olá bem vindo(a) ao support.com')
    # Pedir nome
    nome = input('Digite seu nome:')
    # Pedir e-mail
    email = input('Digite seu e-mail:')
    while True:
    # Oferecer o menu de opções
        resposta = input(
            f'O que deseja?{os.linesep}[1] - Como formatar um computador win10?{os.linesep}[2] - Como recuperar dados corrompidos?{os.linesep}[3] - Como restaurar sistema win10?{os.linesep}[4] - Como trocar de os?{os.linesep}')
    # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()