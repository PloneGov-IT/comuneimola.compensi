comuneimola.compensi
====================

Compatibilità
-------------
Sono stati fatti test con:
 * Plone 3.3.5
 * Plone 4.2.1

Note di installazione
---------------------
 * Se si installa il prodotto per usarlo con versioni di plone precedente alla 4 è necessario impostare nel buildout la versione di collective.js.datatables alla 1.9.
 * Le funzionalità di traduzione della tabella, mancanti in collective.js.datatables 1.9 sono state riportate nel pacchetto e messe sotto condizione Plone >= 4.

Funzionamento
-------------
Una volta installato il prodotto è possibile aggiungere oggetti "Area compensi".
Dentro a questi oggetti è possibile aggiungere oggetti compensi.

La visualizzazione dell'area è impostata per utilizzare come la vista con
collective.js.datatables.

E' presente un bottone che permette di scaricare il contenuto della tabella/cartella
in formato csv.

Un manager dovrà creare l'area.
E' consigliato aggiungere all'area delle portlet-cercatore per trovare i compensi
privati e da revisionare, per comodità degli utenti autenticati.

Workflow
--------

Per quello che riguarda il workflow degli oggetti "Compenso" per ora si decide di restare
il più vicino possibile al simple pubblication wf di plone.

L'editore del documento (ruolo contributor)
 * può aggiungere una voce
 * può aggiungere uno o più link/allegati
 * non può modificare elementi privati appartenenti ad altri editori
 * può richiedere la pubblicazione al revisore
 * può pubblicare direttamente
 * una volta pubblicato:

  * non può più revocare la pubblicazione
  * non può aggiungere/togliere link/allegati.


Il ruolo Plone di Editor dato tramite lo sharing, assume le sembianze di un'operazione di delega a lavorare sul compenso.

Un revisore può:
 * può revocare un elemento pubblicato per una rettifica dei capi già inseriti oppure modifica degli stessi solo ove ininfluenti sulla efficacia dell'atto.

"Manager" e "Amministratore del sito" potranno fare tutto, ma si intende usarli solo per momenti in cui non si può fare a meno di un superuser per la situazione.
Solo utenti con questi due ruoli potranno eseguire azioni di cancella, rinomina, taglia-incolla

Per applicare le azioni di workflow (manda in revisione, pubblicazione, torna indietro, ecc.) all'oggetto "Compenso" e agli allegati di tipo "Collegamento" (i "File" non hanno workflow proprio, sono pubblici ma seguono il workflow dell'oggetto contenitore) contenuti bisogna agire tramite la voce "Avanzate..." dal menu "Stato".


Crediti
-------

Sviluppato dal `Comune di Imola`__

Il comune di Imola supporta `l'iniziativa PloneGov`__.

__ http://www.comune.imola.bo.it/
__ http://www.plonegov.it/


Autori
------
Il prodotto è stato sviluppato da RedTurtle Technology.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/
