Doorgaan naar artikel
adamTa123
/
Vrijdag Userbot
gevorkt van StarkGang / FridayUserbot
Code
Pull-verzoeken
Acties
Projecten
Wiki
Veiligheid
Inzichten
Instellingen
Vrijdag Userbot/userbot/plug-ins/ _helper.py
@ marjolijn1994
adamTa123 Update _helper.py
 1 bijdrager
54 lijnen (52 sloc)  2,06 KB
 
van  userbot  import  CMD_LIST
van  userbot . utils  import  admin_cmd

@ commando ( patroon = "^ .help? (. *)" )
#@borg.on (admin_cmd (patroon = r "help? (. *)"))
async  def  cmd_list ( evenement ):
    zo  niet  evenement . tekst [ 0 ]. isalpha () en  event . tekst [ 0 ] niet  in ( "/" , "#" , "@" , "!" ):
        tgbotusername  =  Var . TG_BOT_USER_NAME_BF_HER
        input_str  =  evenement . pattern_match . groep ( 1 )
        Als  tgbotusername  is  None  of  input_str  ==  "text" :
            string  =  ""
            voor  i  in  CMD_LIST :
                string  + =  "⚡"  +  i  +  " \ n "
                voor  iter_list  in  CMD_LIST [ i ]:
                    string  + =  "` "  +  str ( iter_list ) +  " `"
                    string  + =  " \ n "
                string  + =  " \ n "
            if  len ( string ) >  4095 :
                met  io . BytesIO ( str . Encode ( string )) als  out_file :
                    out_file . name  =  "cmd.txt"
                    wachten op  bot . verzendbestand (
                        evenement . chat_id ,
                        out_file ,
                        force_document = Waar ,
                        allow_cache = False ,
                        caption = "** COMMANDO'S **" ,
                        reply_to = reply_to_id
                    )
                    wachten op  evenement . verwijderen ()
            anders :
                wachten op  evenement . bewerken ( string )
        elif  input_str :
            als  input_str  in  CMD_LIST :
                string  =  "Commando's gevonden in {}:" . formaat ( input_str )
                voor  i  in  CMD_LIST [ input_str ]:
                    string  + =  ""  +  i
                    string  + =  " \ n "
                wachten op  evenement . bewerken ( string )
            anders :
                wachten op  evenement . edit ( input_str  +  "is geen geldige plug-in!" )
        anders :
            help_string  =  "" "DarkHacker😈 Userbot Modules worden hier vermeld! \ n
Voor meer hulp of ondersteuning bezoek @DarkHackerUserbot "" "

            results  =  wachten  bot . inline_query (   # pylint: uitschakelen = E0602
                tgbotusername ,
                help_string
            )
            wacht op  resultaten [ 0 ]. klik (
                evenement . chat_id ,
                reply_to = evenement . reply_to_msg_id ,
                hide_via = Waar
            )
            wachten op  evenement . verwijderen ()