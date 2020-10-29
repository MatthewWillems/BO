#START
print("Esin wilt graag studeren, maar dat is geen optie. De Taliban staan dat niet toe. Vrouwen mogen van hun niet naar school. Esin:")

#1
print("Maakt PLANNEN om te vluchten. / VERTELT haar ouders over haar dromen.")
choice = input()

if choice == 'PLANNEN':
    print("Ze vraagt zich af of ze haar ouders over haar plannen moet vertellen. Esin:")
    print("Besluit om op EIGEN voet verder te gaan. / VERTELT haar ouders over haar plannen.")

elif choice == 'VERTELT':
    print("Haar ouders besluiten dat ze haar gaan helpen om te studeren. Haar vader heeft contact gezocht met een smokkelaar. De prijs is alleen veel te hoog. Esin stelt voor om:")
    print("De BUURMAN om hulp te vragen. / Een deel van hun LAND te verkopen.")

#2
choice = input()

if choice == 'EIGEN':
    print("Ze moet nu een manier bedenken om het land uit te komen. Ze besluit om:")
    print("De BUURMAN1 om hulp te vragen. / Haar VRIENDEN om hulp te vragen.")

elif choice == 'VERTELT':
    print("Haar ouders besluiten dat ze haar gaan helpen om te studeren. Haar vader heeft contact gezocht met een smokkelaar. De prijs is alleen veel te hoog. Esin stelt voor om:")
    print("De BUURMAN2 om hulp te vragen. / Een deel van hun LAND te verkopen.")

elif choice == 'BUURMAN':
    print("Haar ouders vinden dit een goed idee.")
    print("Ze vragen de buurman om hulp. Hij is bereid geld te lenen. De ouders van Esin vragen of ze ook haar zusje kan meenemen, zodat ook zij een betere toekomst heeft.")
    print("Ze vindt dat een goed idee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:") 
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")

elif choice == 'LAND':
    print("Haar ouders denken dat dit inderdaad de beste optie is. Haar zusje Asmaan kan op deze manier ook mee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:")
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")


#3
choice = input ()

if choice == 'BUURMAN1':
    print("De buurman zegt dat hij haar kan helpen. Hij is bereid om haar naar Kabul te brengen, zodat ze daar het vliegtuig kan nemen.")
    print("Een paar dagen later staat de Taliban voor de deur. De buurman heeft haar verlinkt.")

elif choice == 'VRIENDEN':
    print("Ze heeft het probleem met haar vrienden besproken, maar zij kunnen haar niet helpen.")
    print("Ze heeft steeds minder opties. Esin:")
    print("Besluit om over een paar dagen 's nachts weg te LOPEN richting Kabul. Het plan heeft weinig kans van slagen, maar ze wilt weg uit Afghanistan. / Besluit om toch haar OUDERS in te lichten.")

elif choice == 'BUURMAN2':
    print("Haar ouders vinden dit een goed idee.")
    print("Ze vragen de buurman om hulp. Hij is bereid geld te lenen. De ouders van Esin vragen of ze ook haar zusje kan meenemen, zodat ook zij een betere toekomst heeft.")
    print("Ze vindt dat een goed idee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:") 
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")

elif choice == 'LAND':
    print("Haar ouders denken dat dit inderdaad de beste optie is. Haar zusje Asmaan kan op deze manier ook mee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:")
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")

elif choice == 'DRAGEN':
    print("Ze moet nu een keuze maken waar ze naartoe wilt gaan.")
    print("NEDERLAND / ENGELAND / TURKIJE")

elif choice == 'SYMBOOL':
    print("Ze moet nu een keuze maken waar ze naartoe wilt gaan.")
    print("NEDERLAND / ENGELAND / TURKIJE")

#4
choice = input ()

if choice == 'LOPEN':
    print("Esin wordt dood gevonden door soldaten. Ze heeft het niet gered.")

elif choice == 'OUDERS':
    print("Haar ouders besluiten dat ze haar gaan helpen om te studeren. Haar vader heeft contact gezocht met een smokkelaar. De prijs is alleen veel te hoog. Esin stelt voor om:")
    print("De BUURMAN3 om hulp te vragen. / Een deel van hun LAND te verkopen.")

elif choice == 'DRAGEN':
    print("Ze moet nu een keuze maken waar ze naartoe wilt gaan.")
    print("NEDERLAND / ENGELAND / TURKIJE")

elif choice == 'SYMBOOL':
    print("Ze moet nu een keuze maken waar ze naartoe wilt gaan.")
    print("NEDERLAND / ENGELAND / TURKIJE")

elif choice == 'NEDERLAND':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

elif choice == 'ENGELAND':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

elif choice == 'TURKIJE':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

#5
choice = input ()

if choice == 'BUURMAN3':
    print("Haar ouders vinden dit een goed idee.")
    print("Ze vragen de buurman om hulp. Hij is bereid geld te lenen. De ouders van Esin vragen of ze ook haar zusje kan meenemen, zodat ook zij een betere toekomst heeft.")
    print("Ze vindt dat een goed idee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:") 
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")

elif choice == 'LAND':
    print("Haar ouders denken dat dit inderdaad de beste optie is. Haar zusje Asmaan kan op deze manier ook mee.")
    print("Een week later is het zo ver. De smokkelaar brengt hun naar Kabul en vanuit daar vliegt hij met hun naar Mumbai. Hij heeft valse papieren voor hun gemaakt.")
    print("In Mumbai wacht iemand hen op om hun nieuwe kleding te geven. Esin kiest ervoor om:")
    print("Om haar hoofdoek nog steeds te DRAGEN. Ze blijft haar geloof trouw. / Om haar hoofdoek af te doen, als SYMBOOL voor een nieuw begin.")

elif choice == 'NEDERLAND':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

elif choice == 'ENGELAND':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

elif choice == 'TURKIJE':
    print("Esin kiest ervoor om de volgende studie te volgen.")
    print("MEDISCHE Wetenschap. / NATUURKUNDE. / RECHTEN.")

elif choice == 'MEDISCHE':
    print("In 2055 wint Esin de Nobelprijs voor een medicijn tegen kanker.")

elif choice == 'NATUURKUNDE':
    print("In 2043 is Esin één van de rijkste vrouwen ter wereld dankzij haar uitvinding van zonnepanelen die rond een baan om de aarde vliegen.")

elif choice == 'RECHTEN':
    print("In 2039 werkt ze bij de VN om vrouwen in ontwikkelingslanden meer kansen te geven.")
