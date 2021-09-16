import  requests as req
from requests.models import Response



def main () :
    URL_API_TELEGRAM = 'https://api.telegram.org/'
    BOT = '1979238987: AAGfKjPse40vmLJUFS40hoPAemj5m4z49Qc'
    ENDPOINT = 'sendMessage'
    ID_CHAT ='-510378649'
    TEXTO ='hola buenas noches'
    URL_MENSAJE_TELEGRAM = f"{URL_API_TELEGRAM}/bot{BOT}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"

    Consulta = req.get (URL_MENSAJE_TELEGRAM)
    if (Consulta.status_code == 200):
        Response_json = Response.json
        print ('Response_json') 
#else :
# print ('mensaje no enviado')



if (__name__ == "_main_"):
    main() 
 

#codigo de ingreso de peoducto
#codigos_de_productos = f "id_lavandina{"
#while (true):
#ingreso = int ( input ("codigos_de _productos"))
