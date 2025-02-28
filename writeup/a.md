KRIPTANALISIS CIPHER SUBSTITUSI ABJAD-TUNGGAL (MONOALPHABETIC CIPHER)

pertama-tama, akan dilakukan analisis frekuensi huruf, bigram dan trigram dalam bahasa inggris

data yang dimiliki untuk frekuensi dalam bahasa inggris ([sumber](https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html))

frekuensi huruf:
Letters (3,104,375,038 letters scanned):
1. e (390395169, 12.575645%)
2. t (282039486, 9.085226%)
3. a (248362256, 8.000395%)
4. o (235661502, 7.591270%)
5. i (214822972, 6.920007%)
6. n (214319386, 6.903785%)
7. s (196844692, 6.340880%)
8. h (193607737, 6.236609%)
9. r (184990759, 5.959034%)
10. d (134044565, 4.317924%)
11. l (125951672, 4.057231%)
12. u (88219598, 2.841783%)
13. c (79962026, 2.575785%)
14. m (79502870, 2.560994%)
15. f (72967175, 2.350463%)
16. w (69069021, 2.224893%)
17. g (61549736, 1.982677%)
18. y (59010696, 1.900888%)
19. p (55746578, 1.795742%)
20. b (47673928, 1.535701%)
21. v (30476191, 0.981717%)
22. k (22969448, 0.739906%)
23. x (5574077, 0.179556%)
24. j (4507165, 0.145188%)
25. q (3649838, 0.117571%)
26. z (2456495, 0.079130%)

Bigrams (2,383,373,483 bigrams scanned):
1. th (92535489, 3.882543%)
2. he (87741289, 3.681391%)
3. in (54433847, 2.283899%)
4. er (51910883, 2.178042%)
5. an (51015163, 2.140460%)
6. re (41694599, 1.749394%)
7. nd (37466077, 1.571977%)
8. on (33802063, 1.418244%)
9. en (32967758, 1.383239%)
10. at (31830493, 1.335523%)
11. ou (30637892, 1.285484%)
12. ed (30406590, 1.275779%)
13. ha (30381856, 1.274742%)
14. to (27877259, 1.169655%)
15. or (27434858, 1.151094%)
16. it (27048699, 1.134891%)
17. is (26452510, 1.109877%)
18. hi (26033632, 1.092302%)
19. es (26033602, 1.092301%)
20. ng (25106109, 1.053385%)

Trigrams (1,699,542,842 trigrams scanned):
1. the (59623899, 3.508232%)
2. and (27088636, 1.593878%)
3. ing (19494469, 1.147042%)
4. her (13977786, 0.822444%)
5. hat (11059185, 0.650715%)
6. his (10141992, 0.596748%)
7. tha (10088372, 0.593593%)
8. ere (9527535, 0.560594%)
9. for (9438784, 0.555372%)
10. ent (9020688, 0.530771%)
11. ion (8607405, 0.506454%)
12. ter (7836576, 0.461099%)
13. was (7826182, 0.460487%)
14. you (7430619, 0.437213%)
15. ith (7329285, 0.431250%)
16. ver (7320472, 0.430732%)
17. all (7184955, 0.422758%)
18. wit (6752112, 0.397290%)
19. thi (6709729, 0.394796%)
20. tio (6425262, 0.378058%)

Hasil dari analisis frekuensi dari ciphertext adalah sebagai berikut:

Letters:
1. E : 667 -> e
2. V : 463 -> t
3. Y : 407
4. U : 403 
5. P : 376 
6. I : 345 
7. M : 318 
8. B : 287 
9. A : 210 
10. N : 206 
11. K : 193 
12. X : 178 
13. G : 176 
14. O : 162 
15. F : 136 
16. R : 118 
17. H : 112 
18. T : 83 
19. S : 80 
20. L : 79 
21. Z : 52 
22. W : 46 
23. C : 9 
24. J : 7 
25. Q : 4 

Bigram:
1. VA : 127 -> karena kemungkinan th dan he serupa, dapat dicurigai bahwa VA adalah th. karena AE, terutama E adalah e pada plainteks
2. AE : 118 -> he
3. EY : 90 -> dari letters, didapatkan EY adalah "e.", berdasarkan bigram adalah "in", sehingga diabaikan
4. VE : 84 
5. PV : 79
6. EM : 76
7. IM : 76
8. YV : 76
9. UM : 75
10. VU : 75
11. EB : 65
12. LE : 64
13. UY : 64
14. IX : 62
15. YE : 59
16. EO : 58
17. UN : 57
18. PM : 56
19. BE : 55
20. GU : 53

Trigram:
1. VAE : 89 -> the
2. LEO : 58 -> and, tetapi tidak cocok dengan kemungkinan E -> e, sehingga diabaikan
3. XIX : 43 
4. GUN : 40
5. VUI : 40
6. UIM : 40
7. PVE : 37
8. BOK : 32
9. NBO : 31
10. OKV : 31
11. UMS : 31
12. AUY : 26
13. YVE : 25
14. PUG : 24
15. EMN : 23
16. KRX : 22
17. RXG : 22
18. XGU : 22
19. UNL : 22
20. NLE : 22

Sampai saat ini, didapatkan bahwa 
- V -> t
- A -> h
- E -> e

Terdapat kata kunci `thPt`, yang dapat dipetakan menjadi `that`. sehingga didapatkan P -> a.

Sehingga dimiliki:
- V -> t
- A -> h
- E -> e
- P -> a

Dilakukan beberapa pencarian menggunakan RegEx berikutnya untuk mencari kemungkinan:

pencarian the.[A-Z]e:
- theBe, B -> r, s
- theYe, Y -> r, s
- theKe, K -> r, s
- theMe, M -> r, s
- theHe, H -> r, s

kemungkinan:
- there
- these

pada teks, terdapat kata `theYeaBe` yang kemungkinan adalah `these are`

Sehingga, didapatkan:
- Y -> s
- B -> r

Sehingga dimiliki:
- V -> t
- A -> h
- E -> e
- P -> a
- Y -> s
- B -> r

Selanjutnya, terdapat kata `haWe` yang kemungkinan adalah kata `have`, sehingga:
- W -> v

Sehingga dimiliki:
- V -> t
- A -> h
- E -> e
- P -> a
- Y -> s 
- B -> r 
- W -> v


Selanjutnya, terdapat kata `Faster`, yang memiliki kemungkinan:
- master
- caster

dipilih master karena memiliki kemungkinan yang lebih besar:
- F -> m

Sehingga dimiliki:
- V -> t
- A -> h
- E -> e
- P -> a
- Y -> s 
- B -> r 
- W -> v
- F -> m

Selanjutnya, terdapat beberapa kata beserta kemungkinannya, yang menghasilkan kemungkinan kunci:

messaSe -> message
- S -> g

maMagemeMt -> management
- M -> n

teNh -> tech
- N -> c

technUcaG -> technical
- U -> i
- G -> l

inteBesting -> interesting
- B -> r

encrOKtiIn -> encryption
- O -> y
- K -> p
- I -> o

sRmmary -> summary
- R -> u

certiTicate -> certificate
- T -> f

calleH -> called
- H -> d

Xased -> based
- X -> b

Zhich -> which
- Z -> w

reJuire -> require
- J -> q

public Ley -> public key
- L -> k

eCisting -> existing
- C -> x

subQect -> subject
- Q -> j

Sehingga mendapatkan hasil akhir:
- V -> t
- A -> h
- E -> e
- P -> a
- Y -> s 
- B -> r 
- W -> v
- F -> m
- S -> g
- M -> n
- N -> c
- U -> i
- G -> l
- B -> r
- O -> y
- K -> p
- I -> o
- R -> u
- T -> f
- H -> d
- X -> b
- Z -> w
- J -> q
- L -> k
- C -> x
- Q -> j

yang menghasilkan teks akhir:
```
technicalsummaryinshamiraskedforapublickeyencryptionschemeinwhichthepublickeycanbeanarbitrarystringencryptionschemesofthistypearecalledidentitybasedencryptionibeshamirsoriginalmotivationforidentitybasedencryptionwastosimplifycertificatemanagementinemailsystemswhenalicesendsmailtobobatbobhotmailcomshesimplyencryptshermessageusingthepublickeystringbobhotmailcomthereisnoneedforalicetoobtainbobspublickeycertificatewhenbobreceivestheencryptedmailhecontactsathirdpartywhichwecalltheprivatekeygeneratorpkgbobauthenticateshimselftothepkginthesamewayhewouldauthenticatehimselftoacaandobtainshisprivatekeyfromthepkgbobcanthenreadhisemailnotethatunliketheexistingsecureemailinfrastructurealicecansendencryptedmailtobobevenifbobhasnotyetsetuphispublickeycertificatehoweverinthisscenariotheibesystemprovideskeyescrowsincethepkgknowsbobsprivatekeyotherapplicationsdiscussedbelowdonotrequirekeyescrowinmoredetailanibeschemeconsistsoffouralgorithmssetupgeneratesglobalsystemparametersandamasterkeyextractusesthemasterkeytogeneratetheprivatekeycorrespondingtoanarbitrarypublickeystringidencryptencryptsmessagesusingthepublickeyidanddecryptdecryptsmessagesusingthecorrespondingprivatekeysincetheproblemwasposedintherehavebeenseveralproposalsforibeschemeshowevernoneofthesearefullysatisfactorysomesolutionsrequirethatusersnotcolludeothersolutionsrequirethepkgtospendalongtimeforeachprivatekeygenerationrequestsomesolutionsrequiretamperresistanthardwareitisfairtosaythatuntilnowconstructingausableibesystemwasanopenproblemtheibeemailsystemusesanewfullyfunctionalidentitybasedencryptionschemetheperformanceofthecryptosystemiscomparabletotheperformanceofelgamalencryptionthesecurityofthesystemisbasedonanaturalanalogueofthecomputationaldiffiehellmanassumptiononellipticcurvesbasedonthisassumptionweshowthatthenewsystemhaschosenciphertextsecurityintherandomoraclemodelusingstandardtechniquesfromthresholdcryptographythepkginthesystemcanbedistributedsothatthemasterkeyisneveravailableinasinglelocationthisenhancessecurityofthemasterkeystoredatthepkgapplicationsforidentitybasedencryptiontheoriginalmotivationforidentitybasedencryptionistohelpthedeploymentofapublickeyinfrastructuremoregenerallyibecansimplifysystemsthatmanagealargenumberofpublickeysratherthanstoringabigdatabaseofpublickeysthesystemcaneitherderivethesepublickeysfromusernamesorsimplyusetheintegersnasdistinctpublickeyswediscussseveralspecificapplicationsbelowrevocationofpublickeyspublickeycertificatescontainapresetexpirationdateinanibesystemkeyexpirationcanbedonebyhavingaliceencryptemailsenttobobusingthepublickeybobhotmailcomcurrentyearindoingsobobcanusehisprivatekeyduringthecurrentyearonlyonceayearbobneedstoobtainanewprivatekeyfromthepkghencewegettheeffectofannualprivatekeyexpirationnotethatunliketheexistingpkialicedoesnotneedtoobtainanewcertificatefrombobeverytimebobrefresheshiscertificateonecouldpotentiallymakethisapproachmoregranularbyencryptingemailforbobusingbobhotmailcomcurrentdatethisforcesbobtoobtainanewprivatekeyeverydaythismightbefeasibleinacorporatepkiwherethepkgismaintainedbythecorporationwiththisapproachkeyrevocationisquitesimplewhenbobleavesthecompanyandhiskeyneedstoberevokedthecorporatepkgisinstructedtostopissuingprivatekeysforbobsemailaddresstheinterestingpropertyisthatalicedoesnotneedtocommunicatewithanythirdpartytoobtainbobsdailypublickeythisapproachenablesalicetosendmessagesintothefuturebobwillonlybeabletodecrypttheemailonthedatespecifiedbyalicedelegationofdecryptionkeysanotherapplicationforibesystemsisdelegationofdecryptioncapabilitieswegivetwoexampleapplicationsinbothapplicationstheuserbobplaystheroleofthepkgbobrunsthesetupalgorithmtogeneratehisownibesystemparametersparamsandhisownmasterkeyhereweviewparamsasbobspublickeybobobtainsacertificatefromacaforhispublickeyparamswhenalicewishestosendmailtobobshefirstobtainsbobspublickeyparamsfrombobspublickeycertificatenotethatbobistheonlyonewhoknowshismasterkeyandhencethereisnokeyescrowwiththissetupdelegationtoalaptopsupposealiceencryptsmailtobobusingthecurrentdateastheibeencryptionkeysheusesbobsparamsastheibesystemparameterssincebobhasthemasterkeyhecanextracttheprivatekeycorrespondingtothisibeencryptionkeyandthendecryptthemessagenowsupposebobgoesonatripforsevendaysnormallybobwouldputhisprivatekeyonhislaptopifthelaptopisstolentheprivatekeyiscompromisedwhenusingtheibesystembobcouldsimplyinstallonhislaptopthesevenprivatekeyscorrespondingtothesevendaysofthetripifthelaptopisstolenonlytheprivatekeysforthosesevendaysarecompromisedthemasterkeyisunharmeddelegationofdutiessupposealiceencryptsmailtobobusingthesubjectlineastheibeencryptionkeybobcandecryptmailusinghismasterkeynowsupposebobhasseveralassistantseachresponsibleforadifferenttaskegoneispurchasinganotherishumanresourcesetcbobgivesoneprivatekeytoeachofhisassistantscorrespondingtotheassistantsresponsibilityeachassistantcanthendecryptmessageswhosesubjectlinefallswithinitsresponsibilitiesbutitcannotdecryptmessagesintendedforotherassistantsnotethataliceonlyobtainsasinglepublickeyfrombobparamsandsheusesthatpublickeytosendmailwithanysubjectlineofherchoicethemailcanonlybereadbytheassistantresponsibleforthatsubject
```

dengan hasil tanda baca didapatkan dari [sumber](https://crypto.stanford.edu/ibe/#:~:text=%2D229%2C%202001.-,Technical%20Summary,management%20in%20e%2Dmail%20systems.)

```
Technical Summary
In 1984 Shamir asked for a public key encryption scheme in which the public key can be an arbitrary string. Encryption schemes of this type are called Identity Based Encryption (IBE). Shamir's original motivation for identity-based encryption was to simplify certificate management in e-mail systems. When Alice sends mail to Bob at bob@hotmail.com she simply encrypts her message using the public key string ``bob@hotmail.com''. There is no need for Alice to obtain Bob's public key certificate. When Bob receives the encrypted mail he contacts a third party, which we call the Private Key Generator (PKG). Bob authenticates himself to the PKG in the same way he would authenticate himself to a CA and obtains his private key from the PKG. Bob can then read his e-mail. Note that unlike the existing secure e-mail infrastructure, Alice can send encrypted mail to Bob even if Bob has not yet setup his public key certificate. However, in this scenario the IBE system provides key escrow since the PKG knows Bob's private key. Other applications (discussed below) do not require key escrow. In more detail, an IBE scheme consists of four algorithms: (1) Setup generates global system parameters and a master-key, (2) Extract uses the master-key to generate the private key corresponding to an arbitrary public key string ID, (3) Encrypt encrypts messages using the public key ID, and (4) Decrypt decrypts messages using the corresponding private key.
Since the problem was posed in 1984 there have been several proposals for IBE schemes. However, none of these are fully satisfactory. Some solutions require that users not collude. Other solutions require the PKG to spend a long time for each private key generation request. Some solutions require tamper resistant hardware. It is fair to say that, until now, constructing a usable IBE system was an open problem.

The IBE email system uses a new fully functional identity-based encryption scheme. The performance of the cryptosystem is comparable to the performance of ElGamal encryption. The security of the system is based on a natural analogue of the computational Diffie-Hellman assumption on elliptic curves. Based on this assumption we show that the new system has chosen ciphertext security in the random oracle model. Using standard techniques from threshold cryptography the PKG in the system can be distributed so that the master-key is never available in a single location. This enhances security of the master-key stored at the PKG.

Applications for Identity-Based Encryption
The original motivation for identity-based encryption is to help the deployment of a public key infrastructure. More generally, IBE can simplify systems that manage a large number of public keys. Rather than storing a big database of public keys the system can either derive these public keys from usernames, or simply use the integers {1, ... ,n} as distinct public keys. We discuss several specific applications below.
Revocation of Public Keys
Public key certificates contain a preset expiration date. In an IBE system key expiration can be done by having Alice encrypt e-mail sent to Bob using the public key: bob@hotmail.com || current-year . In doing so Bob can use his private key during the current year only. Once a year Bob needs to obtain a new private key from the PKG. Hence, we get the effect of annual private key expiration. Note that unlike the existing PKI, Alice does not need to obtain a new certificate from Bob every time Bob refreshes his certificate.
One could potentially make this approach more granular by encrypting e-mail for Bob using bob@hotmail.com || current-date . This forces Bob to obtain a new private key every day. This might be feasible in a corporate PKI where the PKG is maintained by the corporation. With this approach key revocation is quite simple: when Bob leaves the company and his key needs to be revoked, the corporate PKG is instructed to stop issuing private keys for Bob's e-mail address. The interesting property is that Alice does not need to communicate with any third party to obtain Bob's daily public key. This approach enables Alice to send messages into the future: Bob will only be able to decrypt the e-mail on the date specified by Alice.

Delegation of Decryption Keys
Another application for IBE systems is delegation of decryption capabilities. We give two example applications. In both applications the user Bob plays the role of the PKG. Bob runs the setup algorithm to generate his own IBE system parameters params and his own master-key. Here we view params as Bob's public key. Bob obtains a certificate from a CA for his public key params. When Alice wishes to send mail to Bob she first obtains Bob's public key params from Bob's public key certificate. Note that Bob is the only one who knows his master-key and hence there is no key-escrow with this setup.
Delegation to a laptop. Suppose Alice encrypts mail to Bob using the current date as the IBE encryption key (she uses Bob's params as the IBE system parameters). Since Bob has the master-key he can extract the private key corresponding to this IBE encryption key and then decrypt the message. Now, suppose Bob goes on a trip for seven days. Normally, Bob would put his private key on his laptop. If the laptop is stolen the private key is compromised. When using the IBE system Bob could simply install on his laptop the seven private keys corresponding to the seven days of the trip. If the laptop is stolen, only the private keys for those seven days are compromised. The master-key is unharmed.

Delegation of duties. Suppose Alice encrypts mail to Bob using the subject line as the IBE encryption key. Bob can decrypt mail using his master-key. Now, suppose Bob has several assistants each responsible for a different task (e.g. one is `purchasing', another is `human-resources', etc.). Bob gives one private key to each of his assistants corresponding to the assistant's responsibility. Each assistant can then decrypt messages whose subject line falls within its responsibilities, but it cannot decrypt messages intended for other assistants. Note that Alice only obtains a single public key from Bob (params) and she uses that public key to send mail with any subject line of her choice. The mail can only be read by the assistant responsible for that subject.
```