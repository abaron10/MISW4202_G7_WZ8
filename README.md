# Experimento 2 Detención DDos Attack y renderizado hoja de paciente
1. En el puerto 5000 ejecutamos el servidor de pacientes 

![image](https://user-images.githubusercontent.com/64280930/135738589-9d34e5f1-5952-4763-b414-4e2b4a82be43.png)

2. Creamos el registro usando  Postman, este perfil de usuario con las siguientes credenciales: 

![image](https://user-images.githubusercontent.com/64280930/135738623-02804db1-1113-430d-8ea0-4a61321179e0.png)

3. El usuario es creado exitosamente con su respectivo token de acceso 
![image](https://user-images.githubusercontent.com/64280930/135738664-9b9946ff-3412-40d9-bffe-0f438e8c4909.png)

4. El acceso es concedido para el usuario Miguel: 
Con ID: 2   Y su respectivo token 
![image](https://user-images.githubusercontent.com/64280930/135738689-49e101a2-a1f2-4a48-9c63-f75f5a3ec84e.png)

5. Con la ayuda de Postman accedemos con este ID:2 a la información médica. 
![image](https://user-images.githubusercontent.com/64280930/135738778-9b4b4196-1e85-4b94-a3ff-5981450e903c.png)


6. Validación de la historia medica del paciente
![image](https://user-images.githubusercontent.com/64280930/135738766-cf231a11-1365-4abe-9f19-cb4c31295591.png)

7. Correr ataque 
![image](https://user-images.githubusercontent.com/64280930/135738756-80e86bc2-d6b6-483a-8189-e140d0132d93.png)


# Experimento Voting/Leader election asociado a clínica ABC

1. Crear ambiente virtual python3 -m venv/venv.
2. Activar ambiente virtual.
3. Instalar requerimientos pip install -r requirements.txt. 

4. Iniciamos el servidor de pacientes en el puerto 4000 y se espera hasta que este se encuentre disponible: 

```cd experiment```

```flask run -p 4000```
![image](https://user-images.githubusercontent.com/64280930/132992552-9a523439-3005-41ec-8a3d-3fb3040a30f3.png)

	 

5. Iniciamos el monitor en el puerto 5000 (Puerto por defecto de flask), en este momento se puede evidenciar que los servidores destinados para realizar el servicio de pagos no se encuentran disponibles. Esto: 

```cd experiment/monitor```

```flask run```

![image](https://user-images.githubusercontent.com/64280930/132992740-faac9506-bcbd-4521-a916-c6736e98cfb3.png)



6. Iniciamos los tres componentes de pagos, estos son desplegados en los puertos 5001, 5002, 5003 respectivamente, se espera que hasta que el servidor se encuentre disponible: 

```cd experiment/pagos1```

```flask run - p 5001```


```cd experiment/pagos2```

```flask run - p 5002```


```cd experiment/pagos3```

```flask run - p 5003```

Pagos1 
![image](https://user-images.githubusercontent.com/64280930/132992831-ef210b61-67b3-4d8c-8589-599ed72d4434.png)

Pagos2 
![image](https://user-images.githubusercontent.com/64280930/132992851-e1a6deb0-cfc3-41c1-bdb1-ae137a386c6f.png)
 
Pagos3 
![image](https://user-images.githubusercontent.com/64280930/132992865-74bfe3b8-694d-43e4-bb73-df9c96f431a6.png)

 
7. En este momento se evidencia que el monitor ha asignado un líder al servidor que se encuentra disponible y atendiendo solicitudes, en este caso es el server_3 (pagos2) :  

 ![image](https://user-images.githubusercontent.com/64280930/132992905-8963566b-b148-42fe-b563-23e11f192472.png)

8. Levantar servidor de Redis y cola respectiva 
En una terminal adicional para el server
```cd experiment/tareas```

```redis-server```

![image](https://user-images.githubusercontent.com/64280930/132993136-1fad36bf-8c33-4d7d-9214-6077a0653ca6.png)

En una terminal adicional para la cola
```cd experiment/tareas```

```celery -A tareas worker --pool=solo -l info -Q logs```
![image](https://user-images.githubusercontent.com/64280930/132993167-e2c034b9-f795-4184-9e29-bff5498b0677.png) 

9. Forzamos la caída de la sesión del server_2 y validamos que aleatoriamente el monitor realizó la asignación de un nuevo líder, que en este caso es el server_1 (pagos1): 
![image](https://user-images.githubusercontent.com/64280930/132993019-4d7a5e2e-a1c3-4fa9-8c57-83dcdd78ed18.png)

10. Para concluir la prueba, realizamos una solicitud via Postman al servidor de pacientes que se encuentra desplegado en el puerto 4000,  invocando el servicio de pagos: Este queda enviando request hasta que termine de procesar las 230. 
 ![image](https://user-images.githubusercontent.com/64280930/132993054-869a3d7f-729b-4bfb-b57d-761b91fd16fa.png)

11. Ver patients.db en herramienta de visualización de preferencia para comprobar la persistencia de los datos.
![image](https://user-images.githubusercontent.com/64280930/132993103-1bc4dc7c-2450-4032-a221-f5c10dfb4bf3.png)


 
