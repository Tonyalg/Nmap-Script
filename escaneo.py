import nmap

nm = nmap.PortScanner()

ip_de_red = input ('Dime la IP de red que quieras escanear (EJ: 192.168.1.0/24): ')

def escaneado_de_red():
    nm.scan(hosts=ip_de_red, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    print ('IPs en la red son:')
    for host, status in hosts_list:
        print('    ', host)

def info_principal():
    print ('----------------------------------------------------')
    print (' Host:  ', ip)
    print (' Estado:', nm[ip].state(), '   (', nm[ip].hostname(), ')')
    print ('-----------------------')
    for protocolo in nm[ip].all_protocols():
        print ('Protocolo :', protocolo)
        protocol.append(protocolo)

    for puerto in nm[ip][protocolo].keys():
        print (' Puerto:', puerto, '\t', 'Estado:', nm[ip][protocolo][puerto]['state'])
        print (' ')

def info_puertos():
    print ('-----------------------')
    for protocolo in protocol:
        puertos = nm[ip][protocolo].keys()
        for ports in puertos:
            open_ports.append(ports)
        
            info_ports = nm[ip].tcp(ports)
            ports_information = list(info_ports.values())
            print ('Puerto: ', ports)
            print('- Estado: ', ports_information [0])
            print('- Servicio: ', ports_information [2])
            print('- Producto: ', ports_information [3])
            print('- Versión: ', ports_information [4])
            print('- Información extra: ', ports_information [5])
            print('- Conf: ', ports_information [6])
            print(' ')

protocol = []
open_ports = []

escaneado_de_red()

print (' ')
ip = str (input ("IP a escanear: "))

nm.scan (ip, '0-1024')

info_principal()

mas_pregunta = input ('¿Quieres más info de los puertos? (Y/N): ')
mas = mas_pregunta.lower()
mas2 = mas_pregunta.lower()

if mas == 'y':
    info_puertos()
elif mas == 'n':
    exit
else:
    print ('Opción incorrecta.')
    mas2 = input ('¿Quieres más info de los puertos? (Y/N): ')
    if mas2 == 'y':
        info_puertos()
    else:
        exit
