comuneimola.compensi
====================

Compatibilità
-------------
 * Plone 3.3.5
 * Plone 4.2.1

Note
----
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

Per quello che riguarda il workflow degli oggetti, per ora si decide di restare
il più vicino possibile al simple pubblication wf di plone.

Un manager dovrà creare l'area.
E' consigliato aggiungere all'area delle portlet-cercatore per trovare i compensi
privati e da revisionare, per comodità degli utenti autenticati.

I contributor potranno creare compensi dentro l'area.
Un contributor:
 * può modificare solo i compensi creati da lui;
 * può mandare in revisione i compensi;
 * non può editare fuori dallo stato privato;
 * non può cambiare stato quando il compenso è pubblico/in revisione.

Un revisore può:
 * può pubblicare i documenti;
 * può far tornare i documenti in stato revisione/privato;
 * non può editare i documenti.
 * può vedere documenti privati. Altrimenti se manda indietro un documento, 
   ottiene permessi insufficienti

Il manager potrà fare tutto, ma si intende usarlo solo per momenti in cui non si
può fare a meno di un superuser per sistemare la situazione.

Oltre all'owner, potrà modificare il compenso anche l'editor (solo se privato).
In questo modo si da possibilità di fare modifiche tramite lo sharing; si tratta
di una sorta di delega.
Questa sorta di delega si da tramite sharing (lo possono usare owner e manager)