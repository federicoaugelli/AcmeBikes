# **AcmeBikes**
 **Service Oriented Software Engineering** project


## Consegna 
L’azienda ACMEbikes si occupa di fornire biciclette assemblate su richiesta ed accessori a rivendite che operano direttamente con il pubblico.


Le rivendite inviano ad ACMEbikes ordini composti da cicli e accessori. Per ogni ciclo viene specificato il modello base, la colorazione e le eventuali customizzazioni per gruppo frenante, gruppo sterzo, trasmissione e ammortizzatori.

Una volta ricevuto l’ordine ACMEbikes si accerta che le eventuali customizzazioni richieste siano possibili e procede quindi a presentare un preventivo alla rivendita (vedi sotto), se il preventivo viene accettato ACMEbikes procede all’assemblaggio dei cicli richiesti e alla fornitura degli accessori.

L’assemblaggio prevede una prima fase nella quale si verifica la presenza di tutti componenti necessari nel magazzino principale; nel caso di componenti non presenti si verifica se sono in uno dei magazzini secondari. Se ci sono vengono trasferiti, se non ci sono vengono ordinati (ad un unico fornitore esterno).

L’assemblaggio dei cicli avviene nella sede principale dell’azienda, dove si trova anche il magazzino principale (ma si sta valutando se spostarlo in una nuova sede).

Per maggiore efficienza, se un ordine include accessori che non devono essere assemblati (o che richiedono un assemblaggio elementare, come ad esempio un fanale), questo può essere scomposto in modo che sia possibile che i diversi prodotti vengano inviati al cliente direttamente dai magazzini. A tal fine, per ogni prodotto, il magazzino che viene selezionato è quello che ha il prodotto disponibile e che è geograficamente più vicino alla sede del cliente.

Tutte le spedizioni verso i clienti vengono realizzate tramite un servizio di corriere esterno, le spedizioni fra le sedi di ACMEbikes avvengono con i mezzi dell’azienda.

Il costo dell’ordine viene determinato in funzione del costo dei prodotti e di tutte le spedizioni necessarie. Per ordini superiori ad una certa cifra (che può variare nel tempo) viene valutata l’eventuale applicazione di uno sconto. Tale valutazione viene effettuata da un membro dello staff di ACMEbikes che ha l’autorità per farla.

Una volta determinato il costo finale viene inviato un preventivo al cliente che può accettarlo o rifiutarlo.

In caso di rifiuto l’interazione termina.

In caso di accettazione ACMEbikes si pone in attesa che il cliente invii un riferimento ad un bonifico effettuato per una somma pari almeno ad un decimo del costo dell’ordine a titolo di anticipo.

Una volta verificato con il sistema bancario il pagamento dell’anticipo, ACMEbikes procede alle spedizioni e si pone in attesa che il cliente notifichi il pagamento del saldo. Una volta controllato con il sistema bancario anche questo trasferimento il processo termina.


Si progetti e si realizzi una SOA che supporti le attività di ACMEbikes.

Workflow e artefatti
Si modellino le comunicazioni dello scenario sopra esposto usando una coreografia, si discutano le sue proprietà di connectedness ed eventualmente si raffini la coreografia per migliorare tali proprietà. Si proietti la coreografia in un sistema di ruoli.


Utilizzando uno o più diagrammi di collaborazione BPMN si modelli l’intera realtà descritta compresi i dettagli di ogni partecipante riferibile ad ACMEbikes e delle rivendite. Tale modellazione ha scopo documentativo quindi il livello di dettaglio deve essere consistente con tale scopo. I partecipanti “esterni” (corriere, sistema bancario, ecc…) possono apparire come collapsed pools.


Si progetti una SOA per la realizzazione del sistema e la si documenti utilizzando UML (eventualmente con opportuni profili, ad esempio TinySOA).


Si realizzi il sistema usando come tecnologie un BPMS (si consiglia di utilizzare Camunda), Jolie e API Rest.

Il BPMS deve essere utilizzato per supportare i processi di ACMEbikes e delle rivendite.

La parte di gestione dei magazzini (principale e secondari) deve essere effettuata tramite una SOA di servizi Jolie.

Si assume che il sistema integri sotto forma di servizi (almeno) le seguenti capability esterne:

Calcolo distanze geografiche (preferibilmente con API Rest)
Sistema bancario (preferibilmente API Rest)
Fornitore componenti
Corriere
Tali servizi vanno implementati (con logica elementare) come parte del progetto.


I modelli di processo BPMN da utilizzare per il BPMS devono essere consistenti con la modellazione a scopo documentativo precedentemente realizzata; volendo si può anche scegliere di dettagliare compiutamente già dal primo modello le pool eseguibili. Quindi nel primo caso si avrebbe un modello BPMN documentativo e poi tanti modelli BPMN eseguibili quanti i partecipanti realizzati attraverso BPMS; in alternativa si avrebbe un unico modello BPMN con le pool eseguibili completamente dettagliate e gli altri partecipanti dettagliati a livello documentativo.


Il dialogo fra Jolie e BPMS deve avvenire via SOAP, si veda il sito del corso alla pagina delle risorse per informazioni ulteriori.
