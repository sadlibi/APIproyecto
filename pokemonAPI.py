import requests
import json
from pprint import pprint
base='https://pokeapi.co/api/v2/'

#----------------------------FUNCIONES---------------------------------------------/
#Menu principal
def menu():
    print('----------------------------MENU----------------------------------')
    print('¡Bienvenido a la aplicacion para la consulta API de pokemon!')
    print('------------------------------------------------------------------')
    print('1) Pokemons')
    print('2) Bayas')
    print('------------------------------------------------------------------')
    opcion1=input('¿Sobre que te gustaria consultar?[Si ha terminado teclee: salir]: ')
    return opcion1

#Submenu - 1) Pokemons
def menupokemons():
    print('---------------POKEMONS----------------')
    print('1) Tipo')
    print('2) Habilidad/es')
    print('3) Posibles movimientos')
    print('4) Evoluciones')
    print('---------------------------------------')
    opcion2=input('¿Que quieres consultar sobre pokemons?[Si ha terminado teclee: salir]: ')
    return opcion2

#Submenu - 2) Bayas
def menubayas():
    print('---------------BAYAS----------------')
    print('1) Potencia')
    print('2) Tiempo de germinacion')
    print('3) Tamaño')
    print('---------------------------------------')
    opcion3=input('¿Que quieres consultar sobre bayas?[Si ha terminado teclee: salir]: ')
    return opcion3
#----------------------------------------------------------------------------------/

salir='no'
while salir=='no':
    #---------------------------Start menu principal--------------------------------
    opcions1=menu()
    import os
    os.system('clear')
    #------------------------------Opcion1(Principal)-------------------------------
    if opcions1=='1':
        #---------------------------Start menu pokemons-----------------------------
        opcions2=menupokemons()
        import os
        os.system('clear')
        #--------------------Opcion1(Pokemons)---------------------    
        if opcions2=='1':
            print('-----------------------------------------')
            pokemons1 = requests.get(base+'pokemon').json()
            for nombrepk in pokemons1['results']:
                print(nombrepk['name'])
            print('------------------------------------------')
            pjpokemon=input('¿De que pokemon quieres consultar el tipo?: ')
            pokemons = requests.get(base+'pokemon/'+pjpokemon).json()

            import os
            os.system('clear')
            print(' ')
            print('----------------RESULTADOS----------------')
            for tipo in pokemons['types']:
                print (tipo['type']['name'])
            print('------------------------------------------')
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        #--------------------Opcion2(Pokemons)---------------------    
        elif opcions2=='2':
            print('-----------------------------------------')
            pokemons1 = requests.get(base+'pokemon').json()
            for nombrepk in pokemons1['results']:
                print(nombrepk['name'])
            print('------------------------------------------')
            pokemonhab=input('¿De que pokemon quieres consultar las habilidades?: ')
            pokemons2 = requests.get(base+'pokemon/'+pokemonhab).json()
            
            import os
            os.system('clear')
            print(' ')
            print('----------------RESULTADOS----------------')
            for hab in pokemons2['abilities']:
                print (hab['ability']['name'])
            print('------------------------------------------')
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        #--------------------Opcion3(Pokemons)---------------------        
        elif opcions2=='3':
            print('-----------------------------------------')
            pokemons1 = requests.get(base+'pokemon').json()
            for nombrepk in pokemons1['results']:
                print(nombrepk['name'])
            print('------------------------------------------')
            pokemonmov=input('¿De que pokemons quieres consultar los movimientos?: ')
            pokemons3 = requests.get(base+'pokemon/'+pokemonmov).json()
            
            import os
            os.system('clear')
            print(' ')
            print('----------------RESULTADOS----------------')
            for mov in pokemons3['moves']:
                print (mov['move']['name'])
            print('------------------------------------------')
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        #--------------------Opcion4(Pokemons)---------------------    
        elif opcions2=='4':
            print('-----------------------------------------')
            pokemons1 = requests.get(base+'pokemon').json()
            
            for nombrepk in pokemons1['results']:
                print(nombrepk['name'])
            print('------------------------------------------')
            pokemons4 = requests.get(base+'evolution-chain').json()
            pokemonevo=input('¿De que pokemon quieres ver la evolucion/es?: ')
            
            for linea in pokemons4['results']:
                url=linea['url']
                baseurl = requests.get(url).json()
                
                if baseurl['chain']['species']['name']==pokemonevo:
                    import os
                    os.system('clear')
                    print(' ')
                    print('----------------RESULTADOS----------------')
                    print(baseurl['chain']['evolves_to'][0]['species']['name'])
                    print('------------------------------------------')
                
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        
        elif opcions2=='salir' or opcions2=='Salir':
            salir='si'
        #--------------------------------------------------------------
#------------------------------Opcion2(Principal)---------------------------------
    elif opcions1=='2':
        #---------------------------Start menu bayas-----------------------------
        opcions3=menubayas()
        import os
        os.system('clear')
        #--------------------Opcion1(Bayas)---------------------
        if opcions3=='1':
            print('-----------------------------------------')
            baya=input('Dime el tipo de baya: ')
            bayas = requests.get(base+'berry/'+baya).json()
            sino=input('Potenciadora[10]/No potenciadora[0]: ')
            
            if int(sino)==10:
                name=bayas['name']
                for tipo in bayas['flavors']:
                    tip= tipo['flavor']['name']
                    poten= tipo['potency']
                    if int(poten)==10:
                        print(tip,name)
            else:
                name=bayas['name']
                for tipo in bayas['flavors']:
                    tip= tipo['flavor']['name']
                    poten= tipo['potency']
                    if int(poten)==0:
                        print(tip,name)
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        #--------------------------Opcion2(Bayas)-------------------------
        elif opcions3=='2':
            print('-----------------------------------------')
            bayas2 = requests.get(base+'berry').json()
            limitesup=input('Marca un maximo: ')
            limiteinf=input('Marca un minimo: ')

            lista=[]
            for fila in bayas2['results']:
                nombrecomp=fila['name']
                bayas3 = requests.get(base+'berry/'+nombrecomp).json()

                if int(bayas3['growth_time'])<=int(limitesup) and int(bayas3['growth_time'])>=int(limiteinf):
                    growth=bayas3['name']
                    lista.append(growth)

            print('')        
            print('------------------RESLUTADOS-------------------')
            for dato in lista:
                print(dato)
            print('-----------------------------------------------')
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        #--------------------------Opcion3(Bayas)-------------------------    
        elif opcions3=='3':
            print('-----------------------------------------')
            bayas4 = requests.get(base+'berry').json()
            for nombre in bayas4['results']:
                print(nombre['name'])
            print('-----------------------------------------')
            consultartamaño=input('¿De que baya quieres hacer la consulta?: ')
            import os
            os.system('clear')
            bayas5 = requests.get(base+'berry/'+consultartamaño).json()
            tamaño=bayas5['size']
            print(' ')
            print('---------------------RESULTADOS-----------------------')
            print('El tamaño de la baya', consultartamaño, 'es:',tamaño)
            print('------------------------------------------------------')
            
            pregunta1=input('¿Quieres volver al menu principal?[s/n]: ')
            if pregunta1=='S' or pregunta1=='s':
                salir='no'
                import os
                os.system('clear')
            else:
                salir='si'
        
        elif opcions3=='salir' or opcions3=='Salir':
            salir='si'
        #---------------------------------------------------------------------
    elif opcions1=='salir' or opcions1=='Salir':
        salir='si'
        
    else:
        import os
        os.system('clear')
        print('--------------------------------------------------')
        print('No has introducido un dato valido')
        pregunta=input('¿Quieres volver al menu principal?[s/n]: ')
        print('--------------------------------------------------')
        if pregunta=='S' or pregunta=='s':
            salir='no'
            import os
            os.system('clear')
        else:
            salir='si'