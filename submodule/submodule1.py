#-------------------------------------------------------------------------------
# Name:        Submódulo 1 da aplicação
# Purpose:
#
# Author:      Marcus Sacramento
#
# Created:     14/07/2019
# Copyright:   (c) dev89 2019
# Licence:     OpenSource
#-------------------------------------------------------------------------------



def initiate_submodule(arguments,configuration,handler_logger):
    """Inicialização de submodulo da aplicação
        Parameters
        ----------
        arguments : list, required
            Lista dos argumentos informados na linha de comando
        configuration : list, required
            Lista dos argumentos informados no arquivo de propriedades
        handler_logger : Object, required
            Objeto para gravação de Log
        Raises
        ------
        Nenhuma exceção lançada

        Returns
        -------
        Retono de um objeto logger
    """
    global args
    global config
    global logger
    args=arguments
    config=configuration
    logger=handler_logger
    if args.ajuda:
        help(initiate_submodule)
    logger.info('Executou initiate_submodule')

