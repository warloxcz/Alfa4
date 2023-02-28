ip 0.0.0.0  = naslouchá na  všech adresách.
port 8088 = port na kterém běží.
ip_range = definuje rozsah ip adres které se mají prohledat (proscanovat) ipčko musí být adresa sítě/prefix jinak nebude fungovat!!!
port_range = rozsah portů mezi kterými se hledá.


words = metoda ve které je definováno 5 slov EN/CZ (co slovo v EN to překlad daného slova do CZ).

mode = zkušební metoda kde jsem zkoušel ze začátku vypisování. Musí být nastavena na mode = 1 !!! jinak nebude zapisovat do souborů.
 
Log.out = slouží podobně jako print() akorát Log.out zapisuje do souborů a je efektivnější.


MANUÁLNÍ INSTALACE

Požadavky
Před instalací aplikace se ujistěte, že jsou splněny následující požadavky:

Operační systém Linux, distribuce Debian
Přístup k příkazové řádce
Nainstalovaný balíček python3
Nainstalovaný balíček pip3

1) je třeba vytvořit nějaký python script, který bude zároveň sloužit jako service script.
2) script následně můžeme executnout tím, že ho spustíme (nazev_souboru.py) pomocí ctrl+c ho zastavíme.
3) uložíme tento soubor podle jeho jména do domovského adresáře (home/pi/).
4) Nyní se musí zadefinovat service který rozběhne script. (např.  cd/lib/systemd/system/
                                                                   sudo nano example.service
definice service musí být v /lib/systemd/system  v tomto případě se service jmenuje "example.service"


[Unit]
Description=Hello World
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/nazev_souboru.py
Restart=on-abort

[Install]
WantedBy=multi-user.target


5) zde je vytvořená jednoduchá service která běží na nazev_souboru scriptu a pokud je z nějakého důvodu přerušena tak dojde k restartu.
6) když už máme service tak je potřeba ji zprovoznit.

7) pokaždé co se provede změna v adresáři /lib/systemd/system  je potřeba executnout daemon-reload.


FAQ: pokud chceme zkontrolovat stav servici
      sudo systemctl status "nazev.service"
      
       start servici 
 sudo systemctl start "nazev.servici"

       zastavení servici
sudo systemctl stop "nazev.servici"

 kontrola service logu

sudo journalctl -f -u "nazev.service".
