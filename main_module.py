#-------------------------------------------------------------------------------
# Name:        Aplicação Base
# Purpose:
#
# Author:      Marcus Sacramento
#
# Created:     14/07/2019
# Copyright:   (c) dev89 2019
# Licence:     OpenSource
#-------------------------------------------------------------------------------
import configparser
import argparse
import logging
import submodule

from submodule.submodule1 import initiate_submodule


def manager_log(args):
    """Gerencia os logs da aplicação

        Deve-se informar o nível de log da aplicação de acordo com os argumentos
        * --cl: Console Log
        * --fl: File Log

        Os níeis de log para ambos:
        * CRITICAL
        * ERROR
        * WARNING
        * INFO
        * DEBUG
        * NOTSET

        Parameters
        ----------
        args : list, required
            Lista dos argumentos informados na linha de comando
        Raises
        ------
        Nenhuma exceção lançada

        Returns
        -------
        Objeto Logger
    """
    if args.ajuda:
        help(manager_log)

    global logger
    global fh
    global ch
    logger = logging.getLogger('Application Log')
    fh = logging.FileHandler(args.log_file)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s]' +
                                  '[%(module)s][%(threadName)s][%(funcName)s]' +
                                  '[%(lineno)d] %(message)s')

    logger.setLevel(logging.DEBUG)

    fh.setLevel(logging.ERROR)
    if args.file_log == 'NOTSET':
        fh.setLevel(logging.NOTSET)
    if args.file_log == 'CRITICAL':
        fh.setLevel(logging.CRITICAL)
    if args.file_log == 'WARNING':
        fh.setLevel(logging.WARNING)
    if args.file_log == 'INFO':
        fh.setLevel(logging.INFO)
    if args.file_log == 'DEBUG':
        fh.setLevel(logging.DEBUG)


    ch.setLevel(logging.ERROR)
    if args.console_log == 'NOTSET':
        ch.setLevel(logging.NOTSET)
    if args.console_log == 'CRITICAL':
        ch.setLevel(logging.CRITICAL)
    if args.console_log == 'WARNING':
        ch.setLevel(logging.WARNING)
    if args.console_log == 'INFO':
        ch.setLevel(logging.INFO)
    if args.console_log == 'DEBUG':
        ch.setLevel(logging.DEBUG)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger



def teste_arg(args):
    """Imprime os argumentos

        Se os argumentos forem passados a função imprime algo na tela

        Parameters
        ----------
        args : list, required
            Lista dos argumentos informados na linha de comando

        Raises
        ------
        Nenhuma exceção lançada

        Returns
        -------
        Nenhum retorno
        """
    if args.ajuda:
        help(teste_arg)
        logger.info('Executou Ajuda')
    if args.required:
        print(args.required)
        logger.debug('Executou Required')
    if(args.without_parameter):
        print('Resultado falso')
        logger.critical('Executou Without Parameter')


def load_config(args):
    """Carrega Arquivo de configuração

        Carrega o arquivo de configuração informado nos parametros.

        Parameters
        ----------
        args : list, required
            Lista dos argumentos informados na linha de comando

        Raises
        ------
        Nenhuma exceção lançada

        Returns
        -------
        Lista de configurações
    """
    if args.ajuda:
        help(teste_arg)
    logger.debug('Loading Config')
    global config
    config=configparser.ConfigParser()
    config.read(args.properties)
    logger.debug('Sections into '+args.properties+':'+str(config.sections()))
    for i in (config['FIRST_LEVEL_SECTION|SECOND_LEVEL_SECTION|' +
                     'THIRD_LEVEL_SECTION']):
        logger.debug(i+'='+config.get('FIRST_LEVEL_SECTION|' +
                                      'SECOND_LEVEL_SECTION|'+
                                      'THIRD_LEVEL_SECTION',i))
    logger.info('Config loaded')

    return config



def arguments_application():
    """Carregamento dos argumentos passados por linha de comando"""
    parser = argparse.ArgumentParser(description='Programa para testar os \
    argumentos que são passados')
    parser._action_groups.pop()
    required = parser.add_argument_group('Obrigatório')
    optional = parser.add_argument_group('Opcional')
    required.add_argument("-r", "--required",
                        help="Argumento obrigatório",required=True)
    optional.add_argument("-p", "--properties", default='files/properties',
                        help="Arquivo de propriedades")

    optional.add_argument("-o", "--optional", default=10,
                        help="Argumento Opcional")

    optional.add_argument("-wp", "--without_parameter",
                        help="Sem parametro",
                        action="store_true")
    optional.add_argument("-w", help="Parametro contado",
                        action="count")
    optional.add_argument("-a","--ajuda", help="Exibe ajuda para o script",
                        action="store_true")
    optional.add_argument("-l", "--log_file", default='files/application.log',
                        help="Arquivo de propriedades")
    optional.add_argument("-cl", "--console_log", default='ERROR',
                        help="Definição de log de console da aplicação: DEBUG,"+
                              "INFO, WARNING, ERROR, CRITICAL")
    optional.add_argument("-fl", "--file_log", default='ERROR',
                        help="Definição de log em arquivo da aplicação: DEBUG,"+
                             "INFO, WARNING, ERROR, CRITICAL")

    return parser.parse_args()


if __name__ == '__main__':
    args = arguments_application()
    manager_log(args)
    logger.info('Start Application')
    load_config(args)
    teste_arg(args)
    initiate_submodule(args,config,logger)
    logger.info('End Application')