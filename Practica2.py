import os
#ANALISI DE CONEXION
hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 " + hostname)

if respuesta == 0:
    print(hostname + ": está en funcionamiento!")
else:
    print(hostname +": no funciona!")   

#DETECTAR COMPUTADORAS ACTIVADAS
red = "200.33.171.0/24"
os.system("nmap -sP " + red)

"""
#DETECTAR PUESRTOS ABIERTOS
computadora = "192.168.0.6"
os.system("nmap -sT" + computadora)

#DECTAR SISTEMAS OPERATIVOS
os.system("nmap -0" + computadora)"""
#IMPRESIÓN
"""
mauricio@debian:~/Documentos/PYTHON$ /usr/bin/python3 /home/mauricio/Documentos/PYTHON/Practica2.py
PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=63 time=0.845 ms

--- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.845/0.845/0.845/0.000 ms
www.itmorelia.edu.mx: está en funcionamiento!


Starting Nmap 7.70 ( https://nmap.org ) at 2020-02-27 11:55 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.00085s latency).
Nmap scan report for 200.33.171.13
Host is up (0.00063s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.00089s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.00078s latency).
Nmap scan report for 200.33.171.86
Host is up (0.0010s latency).
Nmap scan report for 200.33.171.115
Host is up (0.00043s latency).
Nmap scan report for 200.33.171.120
Host is up (0.00090s latency).
Nmap scan report for 200.33.171.125
Host is up (0.00080s latency).
Nmap scan report for 200.33.171.127
Host is up (0.00069s latency).
Nmap done: 256 IP addresses (9 hosts up) scanned in 11.42 seconds
"""