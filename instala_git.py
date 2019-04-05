
import os
import argparse
from distutils.dir_util import copy_tree

URL_GIT_CONTEUDO = 'https://github.com/conquer-x/AprendaProgramar1Semana-Conteudo.git'
DIR_EXEMPLO = 'Exercícios'


def diretorio_from_repositorio(url_git):
    """
    Acha o nome do diretorio atraves do url do git
    :param url_git: git do repositorio
    :return: diretorio que o repositorio será baixado
    """
    assert '.git' in url_git, 'URL do git passado não possui final ".git". O endereço deve ser buscado do github, no botão clone'
    partes = url_git.split('/')
    return partes[-1].split('.')[-2]

def get_repo(repo_url, login_object):
    """
    Baixa o repo para a máquina
    :param repo_url: git do repositorio
    :param login_object: um objeto com nome e senha
    :return: nada
    """
    print('Baixando o conteudo de {}'.format(repo_url))
    string_senha = 'https://' + login_object.nome_usuario + ':' + login_object.senha +'@'
    repo_moddedURL = repo_url.replace('https://', string_senha)
    os.system('git clone '+ repo_moddedURL)

    print('\nTudo pronto pra decolar.\n')

def createParser():
    parser = argparse.ArgumentParser(description='Script que baixa os gits para a sua maquina.')
    parser.add_argument('nome_usuario',  type=str,
                        help='Seu nome de usuario')
    parser.add_argument('senha', type=str,
                        help='sua senha do github')
    parser.add_argument('repositorio_aluno', type=str, help='url do seu github conforme help')
    return parser


vaiouvoa ="""
   ____  __  __   _    _____    ____   ____  __  __   _    ______  ___ 
  / __ \/ / / /  | |  / /   |  /  _/  / __ \/ / / /  | |  / / __ \/   |
 / / / / / / /   | | / / /| |  / /   / / / / / / /   | | / / / / / /| |
/ /_/ / /_/ /    | |/ / ___ |_/ /   / /_/ / /_/ /    | |/ / /_/ / ___ |
\____/\____/     |___/_/  |_/___/   \____/\____/     |___/\____/_/  |_|


"""

if __name__ == '__main__':

    print("/n/n/n")
    # cria um parser para pegar as informacoes do usuario
    parser = createParser()
    args = parser.parse_args()
    print(args)

    # verifica os parâmetros
    dir_origem = diretorio_from_repositorio(URL_GIT_CONTEUDO)
    dir_destino = diretorio_from_repositorio(args.repositorio_aluno)
    dir_origem = os.path.join(dir_origem, DIR_EXEMPLO)

    # busca repositorio do conteudo
    get_repo(URL_GIT_CONTEUDO, args)

    # busca repositorio do aluno
    get_repo(args.repositorio_aluno, args)

    # copia o diretório de exercícios para o novo diretório
    copy_tree(dir_origem, dir_destino)

    # print o motivador
    print(vaiouvoa)



