fichier=open("file.txt", "r")
text=fichier.readlines()
nblignes = len(text)
ipsource=''
ipdestination=''
longueur=''
flag=''

for ligne in text:
    if not ligne.startswith('\t'):
        tabl=ligne.split(" ")
        long=len(tabl)
        for i in range(long):
            if tabl[2].startswith('ns') or tabl[4].startswith('ns') or 'OK' in tabl[long-1] or 'HTTP' in tabl[long-1]:
                break
            else:
                ipsource=ipsource+tabl[2][0:21]+';'
                ipdestination=ipdestination+tabl[4][0:21]+';'
                if tabl[5]=='Flags':
                    flag=flag+tabl[6]+';'
                else:
                    flag=flag+'none;'
                break
                
                
fichier.close()
fichier = open("project.csv", "w")
fichier.write("Source IP :;"+ipsource+'\nDestination IP :;'+ipdestination+'\nFlag :;'+flag+'\n\nThe file has been successfully processed !')
fichier.close()