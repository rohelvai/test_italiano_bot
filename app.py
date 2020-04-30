import telebot
from telebot import types
from time import sleep
from keybords import *
bot = telebot.TeleBot('1152808321:AAErN3rTJKvbM_Ov6AWSlIFk9Cg5pMOJKS4')

#setto il mio account per farmi arrivare delle risposte in privato
manager = '281817250'

#domande da fare botta e risposta

#domanda 1
questions_1_text = 'Sei pronto ad iniziare ?',

#risposte alla domanda 1
questions_1_answers =['Diventa Utente Premium','Guarda i Piani','Help','Esci']

#domanda 2
questions_2_text = 'Ecco i nostri pacchetti',

#risposte alla domanda 2
questions_2_answers =['Premium Base','Premium Advanced','Premium VIP','Help','Torna Indietro','Esci']

#domanda di pagamento pacchetto base
questions_3_text = 'Okay paga qui il tuo pacchetto BASE (ricordati di fare lo screen del pagamento serve per la fase successiva)',

#risposta alla domanda di pagamento del primo pacchetto base 
questions_3_answers =['payment button','vai avanti']

#domanda di pagamento pacchetto advanced
questions_18_text = 'Okay paga qui il tuo pacchetto ADAVNCED (ricordati di fare lo screen del pagamento serve per la fase successiva)',

#risposta pagamento link advanced
questions_18_answers =['payment button1']

#domanda pagamento 3 vip
questions_19_text = 'Okay paga qui il tuo pacchetto VIP (ricordati di fare lo screen del pagamento serve per la fase successiva)',

#risposta al pagamento 3 vip
questions_19_answers = ['payment button']

#domanda post pagamento 
questions_20_text = ' HAI PAGATO ? PROCEDIAMO ',

#risposta post pagamento
questions_20_answers = ['Andiamo avanti','Torna Inietro','Esci']

#fine della procedura
questions_21_text = 'Ultimo passo',

#risposta finale 
questions_21_answers = ['Fatto']

#domanda spiegazione gruppi 
questions_22_text = 'Scegli il tipo di pachhetto del quale vuoi sapere le informazioni',

#risposta spiegazione pacchetti
questions_22_answers = ['Base','Advanced','Vip','Diventa Premium','Torna Indietro','Esci']

#domanda post visionato pacchetti premium
questions_23_text = 'Cosa vuoi fare ora ?',

#risposta alla domanda 23
questions_23_answers = ['Acquista pacchetto Base','Torna Indietro','Esci']

#domanda post visionato pacchetti premium
questions_24_text = 'Cosa vuoi fare ora ?',

#risposta alla domanda 24
questions_24_answers = ['Acquista pacchetto Advanced','Torna Indietro','Esci']

#domanda post visionato pacchetti premium
questions_25_text = 'Cosa vuoi fare ora ?',

#risposta alla domanda 25
questions_25_answers = ['Acquista pacchetto Vip','Torna Indietro','Esci']

#domanda 4
questions_4_text ='Ecco i nostri gruppi',

#risposte alla domanda 4
questions_4_answers =['Gruppo Likes + Commenti','Gruppo solo Likes','Diventa Premium','Torna Indietro','Esci']

#domanda 5
questions_5_text ='Ecco il nostro programma di affiliazione',

#risposte alla domanda 5
questions_5_answers =['Diventa Premium','Vediamo i gruppi','Affiliati','Esci']

#domanda 11
questions_11_text =' Vuoi parlare di nuovo con Mimmo ?',

#risposte alla domanda 11
questions_11_answers = ['Ciao Mimmo']

#domanda 12 (help)
questions_12_text='Dopo aver chiesto aiuto, vuoi ricominciare?',

#risposte domanda 12
questions_12_answers =['Ricomincia a parlare con Mimmo','Esci']

#payment keybord
#insert your link instead of 'link'
markup_inline = types.InlineKeyboardMarkup(row_width=1)
markup_inline_btn = types.InlineKeyboardButton('Paga ora il pacchetto BASE',url='https://www.paypal.me/crossmedia772/15')
markup_inline.add(markup_inline_btn)

#insert second link of payment
markup_inline1 = types.InlineKeyboardMarkup(row_width=2)
markup_inline_btn1 = types.InlineKeyboardButton('Paga ora il pacchetto ADVANCED',url='https://www.paypal.me/crossmedia772/28')
markup_inline1.add(markup_inline_btn1)

#insert third link of payment
markup_inline2 = types.InlineKeyboardMarkup(row_width=3)
markup_inline_btn2 = types.InlineKeyboardButton('Paga ora il pacchetto VIP',url='https://www.paypal.me/crossmedia772/40')
markup_inline2.add(markup_inline_btn2)

#insert link inva a dj natale
markup_inline3 = types.InlineKeyboardMarkup(row_width=1)
markup_inline_btn3 = types.InlineKeyboardButton('Invia il messaggio a @officialdjnatale',url='https://t.me/officialdjnatale')
markup_inline3.add(markup_inline_btn3)

#setto come deve rispondere il bot quando si avvia la prima volta
@bot.message_handler(commands=['start'])
def start(message):
     
     bot.send_message(message.chat.id, text=
"""
Ciao io sono Mimmo.
Il bot creato da Instagram Power per facilitarti la registrazione come utente premium.
Sei pronto ad iniziare ?
""",reply_markup=INLINE(2,*questions_1_answers).inline())



#richiami alle funzioni in base alla risposta cliccata sulle domande di sopra
@bot.callback_query_handler(func=lambda call:True)
def cc(call):
    if call.data == questions_1_answers[0]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_2_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_2_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_1_answers[1]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_22_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_22_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_1_answers[4]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
Hai cambiato idea? Capita.
Torna a trovarmi :)
Se vuoi parlare di nuovo con Mimmo
premi il tasto sotto
""", \
                              parse_mode='html',reply_markup=INLINE(1,*questions_11_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)
    
    elif call.data == questions_1_answers[2]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_4_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_4_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)


#se clicca su Help setto la risposta del bot



    elif call.data == questions_1_answers[3]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
Hai bisogno di assistenza?
Contatta 
@officialdjnatale 
su telegram :)
""", \
                              parse_mode='html',reply_markup=INLINE(1,*questions_12_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)

   
    elif call.data == questions_11_answers[0]:
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_1_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_1_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)
      
  

# impost link per il pagamento 


    elif call.data == questions_2_answers[0]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_3_text, \
                              parse_mode='html',reply_markup=markup_inline)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
        bot.answer_callback_query(callback_query_id=call.id)

    elif call.data == questions_2_answers[1]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_18_text, \
                              parse_mode='html',reply_markup=markup_inline1)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
       
        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_2_answers[2]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_19_text, \
                              parse_mode='html',reply_markup=markup_inline2)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
       
        bot.answer_callback_query(callback_query_id=call.id)


#setto le risposte di quando schiaccia su help
         
    elif call.data == questions_12_answers[0]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_1_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_1_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_12_answers[1]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_11_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)



    elif call.data == questions_20_answers[0]:

        bot.send_message(chat_id=call.message.chat.id,text=
"""
INVIA QUESTO 
Ciao io sono (inserisci il tuo nome) 
ho appnea concluso con Mimmo la procedura per diventare utente premium 
Ho scleto il pacchetto 
(INSERISCI IL PACCHETTO SCELTO). 
Ora inserisco il mio codice di invito che mi hanno dato per registrarmi 
(inserisci codice solo se lo tieni).
Quando e come posso postare ?
""", \
                              parse_mode='html',reply_markup=markup_inline3)
        
 
        bot.send_message(chat_id=call.message.chat.id,text=
"""
Per concludere la procedura 
invia lo screen del pagamento e il messaggio con scritto
INVIA QUESTO
(modificando le parti indicate nelle parentesi)
a @officialdjnatale
poi torna da me e clicca il tasto FATTO
""",\
                              parse_mode='html',reply_markup=INLINE(1,*questions_21_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_20_answers[1]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_2_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_2_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)

    elif call.data == questions_20_answers[2]:
   
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
Hai cambiato idea? Capita.
Torna a trovarmi :)
Se vuoi parlare di nuovo con Mimmo
premi il tasto sotto
""", \
                              parse_mode='html',reply_markup=INLINE(1,*questions_11_answers).inline())
        bot.answer_callback_query(callback_query_id=call.id)
        

    elif call.data == questions_21_answers[0]:
  
        bot.send_message(chat_id=call.message.chat.id,text=
"""
Perfetto, hai completato con successo
la procedura di registrazione
ora sei ufficialmente
UN UTENTE PREMIUM
""",\
                              parse_mode='html')

        bot.send_message(chat_id=call.message.chat.id,text=
"""
Ora non resta che aspettare una risposta da
@officialdjnatale
cosi che possa darti le utlime dritte
su come postare correttamente.
Spero che la tua esperienza con me
sia stata positiva.
Grazie e ci vediamo presto.
""",\
                              parse_mode='html')

        bot.send_message(chat_id=call.message.chat.id,text=
"""
Se vuoi parlare di nuovo con Mimmo 
premi il tasto sotto
""", \
                              parse_mode='html',reply_markup=INLINE(1,*questions_11_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_22_answers[0]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
1) premium pack normal 15 euro al mese
- riceverai ad ogni post 20 commenti e 20 likes italiani

- Puoi inviare 5 foto/post al mese

- sei escluso dal commentare o mettere like agli altri 
""",\
                              parse_mode='html',reply_markup=INLINE(1,*questions_23_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_22_answers[1]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
2) premium fast pack avanced 28 euro al mese

- riceverai ad ogni post 22 commenti e 22 likes italiani

- Puoi inviare 8 foto/post al mese

- sei escluso dal commentare o mettere like agli altri 
""",\
                              parse_mode='html',reply_markup=INLINE(1,*questions_24_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_22_answers[2]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
3) premium vip pack unlimited 40 euro al mese

- riceverai ad ogni post 25 commenti e 25 likes italiani

- Puoi inviare 10 foto/post al mese

- sei escluso dal commentare o mettere like agli altri 

- auto caricamento delle foto (ovvero non dovrai inviare il link al gruppo ma ci pensa in automatico il nostro bot)
""",\
                              parse_mode='html',reply_markup=INLINE(1,*questions_25_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_22_answers[3]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_2_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_2_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)



    elif call.data == questions_22_answers[4]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions_1_text,\
                              parse_mode='html',reply_markup=INLINE(1,*questions_1_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_22_answers[5]:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
"""
Hai bisogno di assistenza?
Contatta 
@officialdjnatale 
su telegram :)
""", \
                              parse_mode='html',reply_markup=INLINE(1,*questions_12_answers).inline())

        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_23_answers[0]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_3_text, \
                              parse_mode='html',reply_markup=markup_inline)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
        bot.answer_callback_query(callback_query_id=call.id)

    elif call.data == questions_24_answers[0]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_18_text, \
                              parse_mode='html',reply_markup=markup_inline1)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
       
        bot.answer_callback_query(callback_query_id=call.id)


    elif call.data == questions_25_answers[0]:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= questions_19_text, \
                              parse_mode='html',reply_markup=markup_inline2)

        bot.send_message(chat_id=call.message.chat.id,text= questions_20_text, \
                              parse_mode='html',reply_markup=INLINE(1,*questions_20_answers).inline())

        bot.send_message(manager,
                         f'An user have chosen  <b>{call.data}</b>\n<a href="tg://user?id={call.message.chat.id}">Press to start chatting</a>',
                         parse_mode='html')
       
        bot.answer_callback_query(callback_query_id=call.id)




while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        # print(e)
        sleep(15)
