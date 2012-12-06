comuneimola.compensi
====================

Compatibilità
-------------
 * Plone 3.3.5
 * Plone 4.2.1

Note di installazione
---------------------
 * Se si installa il prodotto per usarlo con versioni di plone precedente alla 4
   è necessario fissare la versione di collective.js.datatables alla 1.9.
   * Le funzionalità di traduzione della tabella, mancanti in collective.js.datatables
     1.9 sono state riportate nel pacchetto e messe sotto condizione Plone >= 4.

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

Un contributor:
 * può creare oggetti compensi;
 * può modificare solo i compensi creati da lui;
 * può mandare in revisione i compensi;
 * non può editare fuori dallo stato privato;
 * non può cambiare stato quando il compenso è pubblico/in revisione.

Un editor può:
 * vedere tutti i compensi (in qualunque stato);
 * modificare i compensi in stato privato;
 * mandare in revisione i compensi privati.
In questo modo si da possibilità di fare modifiche ai compensi anche ad altri utenti oltre al creatore del compenso stesso; si tratta di una sorta di delega.
Questa delega si dà tramite lo sharing (sul singolo compenso lo possono fare owner e manager)

Un revisore può:
 * può pubblicare i compensi (privati o in revisone);
 * può far tornare i compensi in stato revisione o privato;
 * non può editare i compensi;
 * può vedere compensi privati (altrimenti se manda indietro un documento, ottiene permessi insufficienti).

"Manager" e "Amministratore del sito" potranno fare tutto, ma si intende usarli solo per momenti in cui non si può fare a meno di un superuser per sistemare la situazione.
Solo utenti con questi due ruoli potranno eseguire azioni di cancella, rinomina, taglia-incolla

Per applicare le azioni di workflow (manda in revisione, pubblicazione, torna indietro, ecc.) all'oggetto "Compenso" e agli allegati di tipo "Collegamento" (i "File" non hanno workflow proprio, sono pubblici ma seguono il workflow dell'oggetto contenitore) contenuti bisogna agire tramite la voce "Avanzate..." dal menu "Stato".
