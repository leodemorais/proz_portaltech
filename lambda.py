from src.utils.logging import logging, logging_dynamodb
from scr.service import atualizacao_service
from src.exception.field_validation_exception import FieldValidationException

NOME_APP = "validaatualizacaolancamento"
# A variável NOME_APP é definida como uma string com
# o valor "validaatualizacaolancamento".



@logging.inject_lambda_context(clear_state=True)
@logging_dynamodb.inject_lambda_context(clear_state=True)
#A função lambda_handler é decorada com os decoradores
# @logging.inject_lambda_context e @logging_dynamodb.inject_lambda_context,
# que provavelmente são usados para fins de registro.

def lambda_handler(event, context):
    return executa_logica(event)
#A função lambda_handler é definida como o ponto de entrada
# para a função Lambda.
#Dentro da função lambda_handler, ela chama a função executa_logica
# e passa o parâmetro event para ela.


def executa_logica(event):
#A função executa_logica é definida e recebe um parâmetro event.
    try:
       event, validar_para_atualizacao = atualizacao_service \
           .validar_atualizacao_debito(event)
       event = constroi_consistencia_sucesso(event, validar_para_atualizacao)
       return event
    except FieldValidationException as e:
       logging.append_keys(erro_validacao=e)
       logging.error("Erro validacao consistencia logica para "
		     "atualizacao")
       motivo = e.motivo
       codigo = e.codigo
       event = constroi_inconsistencia(event, codigo, motivo)
       return event
    except Exception as e:
       mensagem = str(e)
       logging.append_keys(error=mensagem)
       logging.error("Falha na execucao de atualizacao - " + NOME_APP)
       raise e


def constroi_consistencia_sucesso(event, validar_para_atualizacao):
    consistencia = event["consistencia"]

    if (consistencia.get("etapas" is None):
        consistencia["etapas"] = []
   consistencia["etapas"].append(NOME_APP)

   consistencia["validar_para_atualizacao"] = validar_para_atualizacao

   consistencia["consistido"] = True
   event["consistencia"] = consistencia
   return event


def constroi_inconsistencia(event, codigo_rejeicao, motivo_rejeicao):
   consistencia = event["consistencia"]

   if (consistencia.get("etapas") is None):
       consistencia["etapas"] = []
   consistencia["etapas"].append(NOME_APP)

   consistencia["consistido"] = False
   consistencia["codigo_rejeicao"] = codigo_rejeicao
   consistencia["motivo_rejeicao"] = motivo_rejeicao

   event["consistencia"] = consistencia
   return event
