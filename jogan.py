#!/usr/bin/env python
# encoding: utf-8
######### We Start with a shit xD  #########
#Coded By M4rkWalker
#youtube : M4rkWAlker 
#Github : Github.com/m4rktn
#########  End Coffee  #########
import os,sys,re,os.path
from platform import system
#########   Some Kind   #########
DIR =os.getcwd()
jogandicc = len([name for name in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, name))])
#########   Some Colors   #########
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
starend = '\033[24m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
cyan    = '\033[0;96m'
logo="""
      ██╗ ██████╗  ██████╗  █████╗ ███╗   ██╗
      ██║██╔═══██╗██╔════╝ ██╔══██╗████╗  ██║
      ██║██║   ██║██║  ███╗███████║██╔██╗ ██║
 ██   ██║██║   ██║██║   ██║██╔══██║██║╚██╗██║
 ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║
  ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                              
"""
def nigga():
#########   Menu   #########
	os.system('clear')
	print """%s%s
 %s
 #JoGanInstaller                                       	
 #Coded By \033[94mM4rkWalker\033[91m (\033[93mGithub.com\033[91m/\033[93mM4rktn\033[91m)        	
	%s
 [%s!%s] U Should Run it With r00t 
 (1)  %sInstall Python-Pip %s
 (2)  %sInstall Important Packages To Ur Linux%s(%sOr Termux%s)
 (3)  %sInstall Modules%s(%sPython %s&%s Perl%s) 
 (4)  %sInstall Pentest tools%s 
 (5)  %sUpdate And Upgrade %s
 (6)  %sServices %s
 (7)  %sTermux'sTouch Keyboard%s
 (8)  %sAbout Th3Coder & Exit%s
 (9)  %sUpdate Jogan%s
	 """%(blid,lasfar,logo,lazra9,la7mar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,la7mar,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9)
#########   SYsT3M   #########
	poop =['requests','setuptools','pymssql','crypto','openssl','mechanize','stem','pysocks','fuzzywuzzy','validate_email','wheel','python-Levenshtein','SleekXMPP','xmppy','beautifulsoup4','','','prettytable','colorama','lxml','bs4','dnspython','httplib2']
	home=['Parallel/ForkManager.pm','WWW::Mechanize;','DBI','HTTP::Response','HTTP::Request','Net::SSLeay','YAML','MIME::Base64','LWP::UserAgent','Getopt::Std','Moose','threads','threads::shared'] 
	mark =raw_input("%s%sjogan%s > %s"%(star,ramadi,starend,lazra9))
	if mark =='1':
		print "%s Python 2x # \033[00m"%la7mar
		if system() == 'Linux':
		 os.system("sudo apt-get install python-pip")
		else:
			os.system("pkg install python-pip")
		print " #%s Python 3x # \033[00m"%la7mar
		if system() == 'Linux':
		 os.system("sudo apt-get install python-pip3")
		else:
			os.system("pkg install python-pip3")
	elif mark =='2':
		if system() == 'Linux':#for Debien/UbuntU
			os.system('sudo apt-get install python2 python3 git ruby perl php nano vim')
		else:#4 termux
			os.system('pkg install python2 python3 git ruby perl php nano vim wget sudo')
	elif mark =='3':
		os.system('clear')
		print """ 
		[1] > Perl 
		[2] > Python
		"""
		conan =raw_input("%s%sjogan%s > %s"%(star,ramadi,starend,lazra9))
		if conan =='1':
			if system() == 'Linux':
			 os.system('sudo apt-get install build-essential')
			else:
				os.system('pkg install build-essential')
			for me in home:
				print "\033[91m[+] Install "+me
				os.system("sudo cpan "+me)#need root acess ofc
		elif conan =='2':
			for keke in poop:
			 print "\033[91m[+] Install "+keke+' ...'
			 os.system("pip install "+keke)
		
	elif mark =='4':
	#### I Think thats Good Tools And Helpful ####
		print """%s
 %sJoGan Installer%s \033[92m.\033[93m.\033[92m.\033[91m %sCoded By M4rkWalker%s
 Karma is a shiit \033[92m^\033[93m_\033[92m^\033[91m Boruto is Our Sun \033[92m.\033[93m.\033[92m.\033[91m
 [%s!%s] Some Tools Not 4 Termux 
 %s%sChoice%s :%s 
	[\033[91m1\033[92m]  AutoSploit [AutoExploit] 
	[\033[91m2\033[92m]  Nikto [Pentesting]
	[\033[91m3\033[92m]  SQlMap [SQLI Scanner]
	[\033[91m4\033[92m]  Nmap [Info Scanner]
	[\033[91m5\033[92m]  Zenmap [nmap with gui]
	[\033[91m6\033[92m]  Hydra [Bruter]
	[\033[91m7\033[92m]  Ophcrack [Bruter]
	[\033[91m8\033[92m]  Whatweb [Pentesting]
	[\033[91m9\033[92m]  W3af [Pentesting]
	[\033[91m10\033[92m] Wireshark 
	[\033[91m11\033[92m] John [Bruter]
	[\033[91m12\033[92m] Netsniff-ng [Sniffing]
	[\033[91m13\033[92m] Ettercap [sniffing]
	[\033[91m14\033[92m] Droopescan [Pentesting]
	[\033[91m15\033[92m] WPscan [Pentesting]
	[\033[91m16\033[92m] Parse [Pentesting]
	[\033[91m17\033[92m] ZeroEye [Key Generator] 
	[\033[91m18\033[92m] X-Smash (Passlistmaker)
	[\033[91m19\033[92m] Facebook [Bruter]
	[\033[91m20\033[92m] Instagram [Checker]
	[\033[91m21\033[92m] Osif [FbInfo]
	[\033[91m22\033[92m] RedHawk [Pentesting]
	[\033[91m23\033[92m] HttpLiveProxyGrabber 
	[\033[91m24\033[92m] ToolB0x [Pentesting]
	[\033[91m25\033[92m] A-Rat [RatMaker]
	[\033[91m26\033[92m] Metasploit Framawork 
	[\033[91m27\033[92m] Slowloris [DDOsAttacker]
	[\033[91m28\033[92m] IP-Tracker
	[\033[91m29\033[92m] XXstrike [Pentesting]
	[\033[91m30\033[92m] Hash Bruster 
	[\033[91m31\033[92m] Strike [Pentesting]
	[\033[91m32\033[92m] SqlMate [Mini Salmap]
	[\033[91m33\033[92m] Blazy [Brute Page Page]
	[\033[91m34\033[92m] RouterSploit [Pentesting]
	[\033[91m35\033[92m] Wifite [WPSAttacker]
	[\033[91m36\033[92m] Fluxion [WifiAttacker]
	[\033[91m37\033[92m] Airgeddon [WifiAttacker]
	[\033[91m38\033[92m] Raccoon [Pentesting] 
	[\033[91m39\033[92m] Kadabra [LFI Scanner]
	[\033[91m40\033[92m] Hashcat [identify&hasher]
	[\033[91m41\033[92m] RarCracker [Bruter]
	[\033[91m42\033[92m] SocialFish [phishing]
	[\033[91m43\033[92m] Evilginx [MITM] 
	[\033[91m44\033[92m] TheHarvester [MailGrabber]
	[\033[91m45\033[92m] Recon-ng
	[\033[91m46\033[92m] BingGo [Dorker]
	[\033[91m47\033[92m] Spammer-mail [Sender]
	[\033[91m48\033[92m] FBI [FbInfo]
	[\033[91m49\033[92m] D-Tect [Pentesting]
	[\033[91m50\033[92m] MisterSpyV5 [AutoExploit]
	[\033[91m51\033[92m] Facebook SpamMessanger 
	[\033[91m52\033[92m] BruterFacebook [VIP]
	[\033[91m53\033[92m] Facebook Bot 
	[\033[91m54\033[92m] Fsociety [Pentesting]
	[\033[91m55\033[92m] Shell-scan 
	[\033[91m56\033[92m] Myserver [ServerBeginner]
	[\033[91m57\033[92m] Bypass Recaptcha [Nice One xD]
	[\033[91m58\033[92m] Kali Nethunter
	[\033[91m59\033[92m] Metasploit Termux
	[\033[91m60\033[92m] Devploit [Pentesting]
	[\033[91m61\033[92m] Santet [Pentesting]
%s<=====================================>
	%s[666] Back
	[ %s ] Tool Installed In Jogan's Dict 
%s<=====================================>	
		"""%(la7mar,hell,saker,hell,saker,lazra9,la7mar,bigas,lazra9,bigbbs,la5dhar,la7mar,lazra9,jogandicc,la7mar)
		msf=raw_input("%s%sjogan%s > %s"%(star,ramadi,starend,lazra9))
		if msf =='666':
			nigga()
		elif msf =='1':
			if not os.path.isdir('AutoSploit'):
			 os.system('git clone https://github.com/NullArray/AutoSploit && cd AutoSploit && chmod +x install.sh && python2 autosploit.py')
  			else: 
  				os.system('cd AutoSploit && python2 autosploit.py')
  		elif msf =='2':
  			 os.system('sudo apt-get install nikto')
		elif msf =='3':
			 os.system('pip install sqlmap')
		elif msf =='4':
			 os.system('sudo apt-get install nmap')
		elif msf =='5':
			 os.system('apt-get install zenmap')
		elif msf =='6':
				os.system('apt-get install hydra hydra-gtk')
 		elif msf =='7':
			 os.system('apt-get install ophcrack')
		elif msf =='8':
			 os.system('apt-get install whatweb')
		elif msf =='9':
			 os.system('sudo apt-get install w3af w3af-console')
		elif msf =='10':
			 os.system('sudo apt-get install wireshark')
		elif msf =='11':
			 os.system('sudo apt-get install john')
		elif msf =='12':
			 os.system('sudo apt-get install netsniff-ng')
		elif msf =='13':
			 os.system('sudo apt-get install ettercap-graphical && apt-get install ettercap-common && apt-get install ettercap-dbg')
  		elif msf =='14':
			 os.system('sudo apt-get droopescan')
		elif msf =='15':
			if not os.path.isdir('wpscan'):
			 os.system('sudo apt-get install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev')
			 os.system('pkg install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev')
			 os.system('git clone https://github.com/wpscanteam/wpscan.git && cd wpscan && sudo gem install bundler && bundle install --without test')
  			else: 
  				os.system('wpscan')
		elif msf =='16':
			 os.system('pip install parse')
		elif msf =='17':
			if not os.path.isdir('zeroeye'):
			 os.system('git clone https://github.com/m4rktn/zeroeye && cd zeroeye && python3 dream.py')
  			else: 
  				os.system('cd zeroeye && python3 dream.py')
		elif msf =='18':
			if not os.path.isdir('xsmash'):
			 os.system('git clone https://github.com/m4rktn/xsmash && cd xsmash && python2 xsmash.py')
  			else: 
  				os.system('cd xsmash && python2 xsmash.py')
		elif msf =='19':
			if not os.path.isdir('xsmash'):
			 os.system('git clone https://github.com/m4rktn/xsmash && cd xsmash && perl facebook.pl')
  			else: 
  				os.system('cd xsmash && perl facebook.pl')
		elif msf =='20':
			if not os.path.isdir('instagramCracker'):
			 os.system('git clone https://github.com/04x/instagramCracker && cd instagramCracker && clear && ls -l && echo You Need 2 Lists : list Combo user:pass and list proxy')
  			else: 
  				os.system('cd instagramCracker && clear && ls -l && echo You Need 2 Lists : list Combo user:pass and list proxy ')
		elif msf =='21':
			if not os.path.isdir('OSIF'):
			 os.system('git clone https://github.com/CiKu370/OSIF && cd OSIF && pip2 install -r requirements.txt && python2 osif.py')
  			else: 
  				os.system('cd OSIF && python2 osif.py')
		elif msf =='22':
			if not os.path.isdir('RED_HAWK'):
			 os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK && cd RED_HAWK && php rhawk.php')
  			else: 
  				os.system('cd RED_HAWK && php rhawk.php')
		elif msf =='23':
			if not os.path.isdir('HttpLiveProxyGrabber'):
			 os.system('git clone https://github.com/04x/HttpLiveProxyGrabber && cd HttpLiveProxyGrabber && python2 ProxGrab.py')
  			else: 
  				os.system('cd HttpLiveProxyGrabber && python2 ProxGrab.py')
		elif msf =='24':
			if not os.path.isdir('ToolB0x'):
			 os.system('git clone https://github.com/04x/ToolB0x && cd ToolB0x && python2 ToolB0x.py')
  			else: 
  				os.system('cd ToolB0x && python2 ToolB0x.py')
		elif msf =='25':
			if not os.path.isdir('A-Rat'):
			 os.system('git clone https://github.com/Xi4u7/A-Rat.git && cd A-Rat &&  chmod +x A-Rat.py && python2 A-Rat.py')
  			else: 
  				os.system('cd A-Rat && python2 A-Rat.py')
		elif msf =='26':
			if not os.path.isdir('metasploit'):
			 os.system('cd metasploit && wget https://Auxilus.github.io/metasploit.sh && echo run bash metasploit.sh Or ./msfconsole ^^ ')
  			else: 
  				os.system('cd metasploit && ./msfconsole')
		elif msf =='27':
			if not os.path.isdir('slowloris'):
			 os.system('pip3 install PySocks && git clone https://github.com/gkbrk/slowloris && cd slowloris && echo run python3 slowloris.py www.site.tn ')
  			else: 
  				os.system('cd slowloris && python3 slowloris.py')
		elif msf =='28':
			if not os.path.isdir('IP-Tracer'):
			 os.system('git clone https://github.com/Rajkumrdusad/Tracer && cd IP-Tracer && chmod +x install && ./install && ip-tracer')
  			else: 
  				os.system('cd IP-Tracer && ip-tracer ')
		elif msf =='29':
			if not os.path.isdir('XSStrike'):
			 os.system('git clone https://github.com/s0md3v/XSStrike && cd XSStrike && pip install -r requirements.txt && python xsstrike.py')
  			else: 
  				os.system('cd XSStrike && python xsstrike.py')
		elif msf =='30':
			if not os.path.isdir('Hash-Buster'):
			 os.system('git clone https://github.com/s0md3v/Hash-Buster && cd Hash-Buster && make install && echo run : buster -s <hash>')
  			else: 
  				os.system('cd Hash-Buster && echo run : buster -s <hash>')
		elif msf =='31':
			if not os.path.isdir('Striker'):
			 os.system('git clone https://github.com/UltimateHackers/Striker && cd Striker && pip install -r requirements.txt && python striker.py')
  			else: 
  				os.system('cd Striker && python striker.py')
		elif msf =='32':
			if not os.path.isdir('sqlmate'):
			 os.system('git clone https://github.com/s0md3v/sqlmate && cd sqlmap && pip install -r requirements.txt && python sqlmap')
  			else: 
  				os.system('cd sqlmate && python sqlmap')
		elif msf =='33':
			if not os.path.isdir('Blazy'):
			 os.system('git clone https://github.com/s0md3v/Blazy && cd Blazy && pip install -r requirements.txt && python blazy.py')
  			else: 
  				os.system('cd Blazy && python blazy.py')
		elif msf =='34':
			if not os.path.isdir('routersploit'):
			 os.system('git clone https://www.github.com/threat9/routersploit && cd routersploit && pip3 install -r requirements.txt && apt-get install libglib2.0-dev && pip3 install bluepy && python3 rsf.py')
  			else: 
  				os.system('cd routersploit && python3 rsf.py')
		elif msf =='35':
			if not os.path.isdir('wifite'):
			 os.system('wget https://raw.github.com/derv82/wifite/master/wifite.py && chmod +x wifite.py && ./wifite.py')
  			else: 
  				os.system('cd wifite && ./wifite.py')
		elif msf =='36':
			if not os.path.isdir('fluxion'):
			 os.system('git clone https://www.github.com/FluxionNetwork/fluxion.git && cd fluxion && ./fluxion.sh ')
  			else: 
  				os.system('cd fluxion && ./fluxion.sh')
		elif msf =='37':
			if not os.path.isdir('airgeddon'):
			 os.system('git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git && cd airgeddon && clear && echo use : bash airgeddon.sh')
  			else: 
  				os.system('cd airgeddon && bash airgeddon.sh')
		elif msf =='38':
			 os.system('pip install raccoon-scanner')
		elif msf =='39':
			if not os.path.isdir('Kadabra'):
			 os.system('git clone https://github.com/D35m0nd142/Kadabra && cd Kadabra && bash make.bash')
  			else: 
  				os.system('cd Kadabra && bash make.bash')
		elif msf =='40':
			if not os.path.isdir('hashcat-4.2.1'):
			 os.system('wget https://hashcat.net/files/hashcat-4.2.1.tar.gz && tar -xzvf hashcat-4.2.1.tar.gz && cd hashcat-4.2.1 && bash makefile')
  			else: 
  				os.system('cd hashcat-4.2.1 && bash makefile')
		elif msf =='41':
			if not os.path.isdir('rarcrack-0.2'):
			 os.system('wget https://netix.dl.sourceforge.net/project/rarcrack/rarcrack-0.2/%5BUnnamed%20release%5D/rarcrack-0.2.tar.bz2 && tar - xzvf rarcrack-0.2.tar.bz2 && cd rarcrack-0.2 && bash makefile')
  			else: 
  				os.system('')
		elif msf =='42':
			if not os.path.isdir('SocialFish'):
			 os.system('git clone https://github.com/UndeadSec/SocialFish && cd SocialFish && pip3 install -r requirements.txt && echo usage : python3 SocialFish.py')
  			else: 
  				os.system('cd SocialFish && python3 SocialFish.py')
		elif msf =='43':
			if not os.path.isdir('evilginx2'):
			 os.system('git clone https://github.com/kgretzky/evilginx2 && cd evilginx2 && make install && evilginx ')
  			else: 
  				os.system('cd evilginx2 && evilginx')
		elif msf =='44':
			if not os.path.isdir('theHarvester'):
			 os.system('git clone https://github.com/laramies/theHarvester && cd theHarvester && chmod +x theHarvester.py && ./theHarvester.py')
  			else: 
  				os.system('cd theHarvester && ./theHarvester.py')
		elif msf =='45':
			if not os.path.isdir('recon-ng'):
			 os.system('git clone git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/recon-ng.git && cd recon-ng && pip install -r REQUIREMENTS && ./recon-ng -h')
  			else: 
  				os.system('cd recon-ng && ./recon-ng')
		elif msf =='46':
			if not os.path.isdir('BinGoo'):
			 os.system('git clone https://github.com/Hood3dRob1n/BinGoo && cd binGoo && chmod +x bingoo && ./bingoo')
  			else: 
  				os.system('cd BinGoo && ./bingoo')
		elif msf =='47':
			if not os.path.isdir('Spammer-Email'):
			 os.system('git clone https://github.com/p4kl0nc4t/Spammer-Email && cd Spammer-Email && echo usage : python spammer_email.py')
  			else: 
  				os.system('cd Spammer-Email && python spammer_email.py')
		elif msf =='48':
			if not os.path.isdir('fbi'):
			 os.system('git clone https://github.com/xHak9x/fbi && cd fbi && pip2 install -r requirements.txt && python2 fbi.py')
  			else: 
  				os.system('cd fbi && python2 fbi.py')
		elif msf =='49':
			if not os.path.isdir('d-tect'):
			 os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT-1 d-tect && cd d-tect && ls')
  			else: 
  				os.system('cd d-tect && python2 d-tect.py ')
		elif msf =='50':
			if not os.path.isdir('mrspyv5'):
			 os.system('git clone https://github.com/m4rktn/mrspyv5/ && clear && cd mrspyv5 && ls -l && echo Enjoy ^^')
  			else: 
  				os.system('cd mrspyv5 && ls -l')
		elif msf=='51':
			if not os.path.isdir('spamchat'):
			 os.system('git clone https://github.com/errorBrain/spamchat.git && cd Spamchat && pip2 install -r requirements.txt && python2 messenger.py')
  			else: 
  				os.system('cd spamchat && python2 messenger.py')
		elif msf=='52':
			if not os.path.isdir('fbbrute'):
			 os.system('git clone https://github.com/Senitopeng/fbbrute && cd fbbrute && python2 MBF.py')
  			else: 
  				os.system('cd fbbrute && python2 MBF.py')
		elif msf=='53':
			if not os.path.isdir('kojawafft'):
			 os.system('git clone https://github.com/sandalpenyok/kojawafft && cd kojawafft && nzip node_modules.zip && echo usage : node index.js')
  			else: 
  				os.system('cd kojawafft && node index.js')
		elif msf=='54':
			if not os.path.isdir('fsociety'):
			 os.system('git clone https://github.com/Manisso/fsociety.git && cd fsociety && chmod +x fsociety.py && python2 fsociety.py ')
  			else: 
  				os.system('cd fsociety && python2 fsociety.py')
		elif msf=='55':
			if not os.path.isdir('shell-scan'):
			 os.system('git clone https://github.com/Rhi7/shell-scan && cd shell-scan && chmod +x shell.py && echo usage :  python shell.py -u site.tn -w wordlist.txt')
  			else: 
  				os.system('cd shell-scan && python shell.py')
		elif msf=='56':
			if not os.path.isdir('MyServer'):
			 os.system('git clone https://github.com/Rajkumrdusad/MyServer.git && cd MyServer && chmod +x install && ./install && clear && echo just run : myserver ')
  			else: 
  				os.system('cd MyServer && myserver')
		elif msf=='57':
			if not os.path.isdir('GoogleSearch-CLI'):
			 os.system('git clone https://github.com/GoogleX133/GoogleSearch-CLI.git && cd GoogleSearch-CLI && php GoogleSearch.php')
  			else: 
  				os.system('cd GoogleSearch-CLI && php GoogleSearch.php')
		elif msf=='58':
			if not os.path.isdir('kalinethunter'):
			 os.system('curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter && chmod +x kalinethunter && bash kalinethunter && clear && startkali')
  			else: 
  				os.system('cd kalinethunter && startkali')
		elif msf=='59':
			if not os.path.isdir('Metasploit_termux'):
			 os.system('git clone https://github.com/Hax4us/Metasploit_termux && cd Metasploit_termux &&  bash metasploit.sh && clear && echo usage : msfconsole ')
  			else: 
  				os.system('cd Metasploit_termux && msfconsole')
		elif msf=='60':
			if not os.path.isdir('Devploit'):
			 os.system('git clone https://github.com/joker25000/Devploit.git && cd Devploit && clear && echo usage : \npython2 Devploit.py')
  			else: 
  				os.system('cd Devploit && python2 Devploit.py')
		elif msf=='61':
			if not os.path.isdir('santet-online'):
			 os.system('git clone https://github.com/Gameye98/santet-online && cd santet-online && python2 santet.py')		
  			else: 
  				os.system('cd santet-online && python2 santet.py')
		else:
			baka=raw_input("%sNani Sir ?? Do u need To return ?[Y/n]: \033[00m"%cyan)
			if baka.upper() =='Y':
				nigga()
			else:
				print "%sOkk Senpai ... Thnx To Use JoGanInstaller\033[00m"%la5dhar
				exit()

	elif mark =='5':
		if not system() == 'Linux':
			os.system('apt Update && apt upgrade')
			os.system('clear')
		else:
			os.system('sudo apt-get update && sudo apt-get upgrade')
			os.system('clear')
	elif mark =='6':
	 print """
	Install & Fix Services
	1) Xampp (Apache2/Php/mysql/...)
	2) Tor 
	3) Postmgrsql(kali)
	4) Beef
	5) Dradis
	6) Openvas
	7) other (ssh/ftp...)
	666) Back"""
	 sasuke=raw_input("%s%sjogan%s > %s"%(star,ramadi,starend,lazra9))
	 if sasuke =='1':
			os.system('wget https://www.apachefriends.org/xampp-files/7.2.9/xampp-linux-x64-7.2.9-0-installer.run && chmod +x xampp-linux-x64-7.2.9-0-installer.run && ./xampp-linux-x64-7.2.9-0-installer.run')
	 elif sasuke=='2':
			os.system('mkdir torBrowser && cd torBrowser && wget https://www.torproject.org/dist/torbrowser/8.0/tor-browser-linux64-8.0_en-US.tar.xz && cd tor-browser-linux64-8.0_en-US/Browser && chmod +x start-tor-browser && echo usage : run click To start-tor-browser or rdream@zack:~$./start-tor-browser')
	 elif sasuke=='3':
			os.system('sudo apt-get install postgresql postgresql-contrib')
	 elif sasuke=='4':
			os.system('git clone https://github.com/beefproject/beef && chmod +x install && ./install')
	 elif sasuke=='5':
			os.system('git clone https://github.com/dradis/dradis-ce.git && cd dradis-ce/ && ./bin/setup')
	 elif sasuke=='6':
			os.system('apt-get install python-software-properties && apt-get install sqlite3 && sudo add-apt-repository ppa:mrazavi/openvas && apt-get update && apt-get install openvas') 
	 elif sasuke=='7':
			os.system('apt-get install ftp ssh filezila openvpn rdesktop sudo ')
	 elif sasuke=='666':
	 	nigga()
	 else:
	 	baka=raw_input("%sNani Sir ?? Do u need To return ?[Y/n]: \033[00m"%cyan)
		if baka.upper() =='Y':
			nigga()
		else:
			print "%sOkk Senpai ... Thnx To Use JoGanInstaller\033[00m"%la5dhar
			exit()
	elif mark =='7':
		print"======= Source : https://wiki.termux.com/wiki/Touch_Keyboard =======\n====================================================================+with ctrl \n Ctrl+A → Move cursor to the beginning of line\n Ctrl+C → Abort (send SIGINT to) current process\n Ctrl+D → Logout of a terminal session\n Ctrl+E → Move cursor to the end of line\n Ctrl+K → Delete from cursor to the end of line\n Ctrl+L → Clear the terminal\n Ctrl+Z → Suspend (send SIGTSTP to) current process\n Ctrl+alt+C → Open new session (only work in Hacker's Keyboard)\n+ With Volume\n Volume Up+E → Escape key\n Volume Up+T → Tab key\n Volume Up+1 → F1 (and Volume Up+2 → F2, etc)\n Volume Up+0 → F10\n Volume Up+B → Alt+B, back a word when using readline\n Volume Up+F → Alt+F, forward a word when using readline\n Volume Up+X → Alt+X\n Volume Up+W → Up arrow key\n Volume Up+A → Left arrow key\n Volume Up+S → Down arrow key\n Volume Up+D → Right arrow key\n Volume Up+L → | (the pipe character)\n Volume Up+H → ~ (the tilde character)\n Volume Up+U → _ (underscore)\n Volume Up+P → Page Up\n Volume Up+N → Page Down\n Volume Up+. → Ctrl+\ (SIGQUIT)\n Volume Up+V → Show the volume control\n Volume Up+Q → Show extra keys view"
	elif mark =='8':
		print """%s
Name :%szack%s
Nickname : %sM4rkWalker%s
Country : %sTN%s
Age : %s19yo%s
FaceBook : %s[Not Avaible]%s
Mail : %sDream0@protonmail.com%s
Youtube : %sM4rkWalker%s
Github : %s/m4rktn%s
Message : %si Wr0te This Script In My First 10days coding ... 
Thnx To Use JoGanInstaller .. i Wish That This Tool Help U ^.^ %s"""%(la5dhar,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs,bigas,bigbbs)
		exit()	
	elif mark =='9':
		os.system('chmod +x update.sh && ./update.sh')
	else:
			print "%sOkk Senpai ... Thnx To Use JoGanInstaller\033[00m"%la5dhar
			exit()
#########    END    #########
if __name__ == '__main__':
	try:
		nigga()
	except KeyboardInterrupt:
		print "\n%sOkk Senpai ... Thnx To Use JoGanInstaller\033[00m"%la5dhar
sys.exit()                     #########
#################   M4RKWALKER #[o] [o]#  ZAKARYA ADDALA   #################
#							   <  ''   >								   #
#								|wwwww|								  	   #
#								  vvv								  	   #
#														  				   #
############################################################################
