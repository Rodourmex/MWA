# MWA

## Descripción

Este script manda el mensaje escrito en el archvio "sms.txt" a cada uno de los números colocados en el archivo "pnbrs.csv".
Es necesario tener una cuenta en Twilio con al menos un sender de WA habilitado así como preconfigurar el account_sid y el auth_token de twilio en las variables del sistema.


## Instrucciones

*1* Instala twilio, (pip install -r requirements.txt).

*2* Crea un archivo csv llamado "pnbrs.csv" y añade los teléfonos a contactar en formato de 10 dígitos.

*3* Abre el archivo "sms.txt" y coloca el mensaje a mandar

*4* Configura las siguientes variables de sistema con las siguientes especificaciones (contacta al administrador de twilio):

  environ['TWILIOSID'] = twilio_account_sid 
  environ['TWILIOAUTHTOKEN'] = twilio_auth_token 
  environ['BOTNBR'] = twilio_wa_nbr

*5* Corre el programa usando python messenger.py

