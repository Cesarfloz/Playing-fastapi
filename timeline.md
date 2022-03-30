importe fastapi, despues cree una instancia llamada FastAPI

cree el primer metodo (tipo:get), que devuelve un saludo
lo implemete por primera vez con "uvircorn main:app"
por defecto lo ace en el puerto 8000 (todo ok)

NOTA: utilizar "--reload" para cargar la api cada vez que se actualice automaticamente
(comando completo : uvicorn main:app --reload)
 
posteriormente cree otro metodo (tipo:get) llamado about, 
lo implemete y me tiro el siguiente error:
ERROR:  [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000): 
solo se permite un uso de cada dirección de socket (protocolo/dirección de red/puerto)

entonces cambie el puerto del 8000 (el que estaba por defecto) al 8001 con el siguiente comando
(uvicorn main:app --reload --port 8001)
y funcionar

por ultimo cree otro metodo (tipo:get) para visualiza usuarios con su id y recibe el user id en "user_id"
