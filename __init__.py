# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Telegram" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

import telegram
global bot_rb

module = GetParams("module")
if module == "connect":
    token = GetParams("token")
    option = GetParams("option")
    bot_rb = telegram.Bot(token=token)


if module == "example_view":
    textarea = GetParams("iframe")
    print(textarea['input'])

if module == "example_html":
    textarea = GetParams("iframe")
    print(textarea['input'])