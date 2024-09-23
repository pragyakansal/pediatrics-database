/* HOSPEDSPATIENTS Database
patient (pID, pLast, pFirst, pSSN, pCreationDate, pDOB, pSex, pAddress, pLastAppt, pIllness)
guardian (gID, gLast, gFirst, gSSN, gDOB, gSex, gAddress, gPhoneNum, gInsuranceCo, gInsuranceNum, gBalance)
doctor (dID, dLast, dFirst, dSSN, dCreationDate, dDOB, dSex, dPhoneNum, dAddress)
nurse (nID, nLast, nFirst, nSSN, nCreationDate, nDOB, nSex, nAddress, nPhoneNum)
assignedToNur (pID, nID)
assignedToDoc (pID, dID)
dependentOf (pID, gID, gInsuranceCo, gInsuranceNum)
*/


DROP TABLE IF EXISTS patient CASCADE;
DROP TABLE IF EXISTS guardian CASCADE;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS nurse CASCADE;
DROP TABLE IF EXISTS assignedToNur CASCADE;
DROP TABLE IF EXISTS assignedToDoc CASCADE;
DROP TABLE IF EXISTS dependentOf CASCADE;


CREATE TABLE patient
(pID varchar (10) PRIMARY KEY,
pLast varchar (30) NOT NULL,
pFirst varchar (30) NOT NULL,
pSSN bigint NOT NULL,
pCreationDate varchar (10) NOT NULL,
pDOB varchar (10) NOT NULL,
pSex varchar (10) NOT NULL,
pAddress varchar (100) NOT NULL,
pLastAppt varchar (10) NOT NULL,
pIllness varchar (250) NOT NULL
);


CREATE TABLE guardian
(gID varchar (10) PRIMARY KEY,
gLast varchar (30) NOT NULL,
gFirst varchar (30) NOT NULL,
gSSN bigint NOT NULL,
gDOB varchar (8) NOT NULL,
gSex varchar (10) NOT NULL,
gAddress varchar (100) NOT NULL,
gPhoneNum bigint NOT NULL,
gInsuranceCo varchar (50),
gInsuranceNum varchar (10),
gBalance float NOT NULL,
UNIQUE (gInsuranceCo, gInsuranceNum)
);


CREATE TABLE doctor
(dID varchar (10) PRIMARY KEY,
dLast varchar (30) NOT NULL,
dFirst varchar (30) NOT NULL,
dSSN bigint NOT NULL,
dCreationDate varchar (10) NOT NULL,
dDOB varchar (10) NOT NULL,
dSex varchar (10) NOT NULL,
dPhoneNum bigint NOT NULL,
dAddress varchar (100) NOT NULL
);


CREATE TABLE nurse
(nID varchar (10) PRIMARY KEY,
nLast varchar (30) NOT NULL,
nFirst varchar (30) NOT NULL,
nSSN bigint NOT NULL,
nCreationDate varchar (10) NOT NULL,
nDOB varchar (10) NOT NULL,
nSex varchar (10) NOT NULL,
nAddress varchar (100) NOT NULL,
nPhoneNum bigint NOT NULL
);


CREATE TABLE assignedToNur
(pID varchar (10) NOT NULL,
nID varchar (10) NOT NULL,
PRIMARY KEY (pID, nID),
FOREIGN KEY (pID)
REFERENCES patient(pID),
FOREIGN KEY (nID)
REFERENCES nurse(nID)
);


CREATE TABLE assignedToDoc
(pID varchar (10) PRIMARY KEY,
dID varchar (10) NOT NULL,
FOREIGN KEY (pID)
REFERENCES patient(pID),
FOREIGN KEY (dID)
REFERENCES doctor(dID)
);


CREATE TABLE dependentOf
(pID varchar (10) PRIMARY KEY,
gID varchar (10) NOT NULL,
gInsuranceCo varchar (50) NOT NULL,
gInsuranceNum varchar (20) NOT NULL,
FOREIGN KEY (pID)
REFERENCES patient(pID),
FOREIGN KEY (gID)
REFERENCES guardian(gID),
FOREIGN KEY (gInsuranceCo, gInsuranceNum)
REFERENCES guardian(gInsuranceCo, gInsuranceNum)
);


INSERT INTO patient (pID, pLast, pFirst, pSSN, pCreationDate, pDOB, pSex, pAddress, pLastAppt, pIllness)
VALUES
('5478828149', 'Krystle', 'Carree', 880668772, '05/19/2011', '03/01/2007', 'Female', '123 Elm Street, Chicago, IL 60601', '9/15/2012', 'Pneumonia'),
('2353169554', 'Wilhelmina', 'Muhammad', 289612554, '07/01/2022', '07/12/2018', 'Male', '456 Maple Avenue, Springfield, IL 62701', '7/28/2022', 'Pneumonia'),
('2867034035', 'Vania', 'Marielle', 810946847, '10/26/2019', '03/24/2009', 'Female', '04 Grasskamp Trail, Chicago, IL 60626', '6/7/2020', 'Bronchitis'),
('1608930009', 'Elsie', 'Sayres', 402543798, '10/07/2020', '03/31/2017', 'Male', '101 Pine Lane, Rockford, IL 61101', '9/22/2021', 'Meningitis'),
('1135007012', 'Elsworth', 'Emmeline', 779483273, '01/19/2017', '04/06/2012', 'Female', '234 Birch Road, Aurora, IL 60501', '7/31/2019', 'Strep throat'),
('7487444848', 'Kamilah', 'Annabell', 190434601, '11/16/2015', '05/14/2008', 'Female','567 Cedar Court, Joliet, IL 60401', '10/08/2017', 'Strep throat'),
('9376633717', 'Redsull', 'Sybyl', 458872004, '04/04/2018', '04/08/2016', 'Female', '890 Redwood Place, Naperville, IL 60540', '03/01/2020', 'Ear infection'),
('8343324366', 'Blanko', 'Tamera', 472840421, '03/31/2015', '09/04/2014', 'Female', '111 Willow Lane, Champaign, IL 61820', '09/24/2016', 'Strep throat'),
('3339297274', 'Ronnie', 'Arabelle', 436986178, '10/22/2008', '10/30/2005', 'Female', '30018 Grayhawk Plaza, Hoffman Estates, IL 60010', '03/08/2010', 'Meningitis'),
('1309936374', 'Ortes', 'Link', 113725928, '04/20/2020', '10/13/2004', 'Intersex', '333 Tulip Road, Bloomington, IL 61701', '11/16/2022', 'Bronchitis'),
('0943273102', 'Enrique', 'Erhart', 258626663, '06/13/2023', '04/11/2023', 'Male', '87634 Londonderry Crossing, Naperville, IL 60540', '7/4/2023', 'Pneumonia'),
('6040373601', 'Dyson', 'Fowler', 337648422, '06/26/2018', '10/09/2008', 'Male', '555 Daisy Avenue, Elgin, IL 60120', '11/16/2021', 'Pneumonia'),
('7336237347', 'Burk', 'Rodd', 596023469, '07/20/2016', '01/03/2016', 'Male', '666 Poplar Road, Waukegan, IL 60085', '02/04/2022', 'Strep throat'),
('5737027589', 'Wheeler', 'Gwyn', 377163080, '03/31/2018', '03/18/2005', 'Female', '3 Crowley Junction, Decatur, IL 62521', '8/26/2023', 'Ear infection'),
('9926175422', 'Godden', 'Reg', 123097541, '03/27/2007', '06/06/2004', 'Male', '888 Iris Court, Schaumburg, IL 60173', '02/08/2019', 'Bronchitis'),
('5548366882', 'MacDearmont', 'Ricoriki', 712332074, '07/22/2021', '07/17/2006', 'Male', '7539 Cordelia Place, Arlington Heights, IL 60004', '6/2/2022', 'Meningitis'),
('8652992541', 'Idel', 'Chrisse', 406111109, '04/26/2016', '12/04/2011', 'Male', '121 Magnolia Drive, Bolingbrook, IL 60440', '08/17/2019', 'Strep throat'),
('2439361151', 'Cadany', 'Guenevere', 784677467, '06/10/2018', '07/27/2014', 'Intersex', '232 Jasmine Lane, Arlington Heights, IL 60004', '06/17/2022', 'Ear infection'),
('9575986083', 'Franchyonok', 'Vitoria', 225831527, '05/31/2011', '01/27/2005', 'Female', '40 Arizona Center, Elgin, IL 60120', '04/24/2019', 'Ear infection'),
('0934341656', 'Owlner', 'Margarita', 309447807, '08/04/2014', '08/07/2009', 'Female', '004 Transport Place, Hoffman Estates, IL 60010', '02/28/2018', 'Bronchitis'),
('0184960495', 'Maulkin', 'Ham', 335142985, '10/29/2014', '08/20/2007', 'Male', '565 Orchid Place, Skokie, IL 60076', '05/18/2021', 'Pneumonia'),
('0219096953', 'Krystle', 'Bruce', 573503356, '07/24/2021', '12/25/2011', 'Male', '123 Elm Street, Chicago, IL 60601', '03/19/2022', 'Pneumonia'),
('5348686204', 'Wilhelmina', 'Ody', 574132898, '05/06/2018', '06/11/2005', 'Male', '456 Maple Avenue, Springfield, IL 62701', '04/18/2023', 'Ear infection'),
('7092577144', 'Vania', 'Freddy', 739287636, '01/11/2019', '07/06/2011', 'Male', '24740 Northland Parkway, Bloomington, IL 61701', '04/19/2020', 'Strep throat'),
('0987039997', 'Elsie', 'Tildie', 365855409, '03/31/2006', '09/08/2005', 'Intersex', '101 Pine Lane, Rockford, IL 61101', '07/20/2017', 'Bronchitis'),
('9060291182', 'Elsworth', 'Wayne', 100086560, '06/05/2021', '05/25/2013', 'Male', '234 Birch Road, Aurora, IL 60501', '07/07/2023', 'Ear infection'),
('1345635524', 'Kamilah', 'Donnie', 616587978, '02/19/2020', '01/10/2004', 'Female', '08 Bonner Street, Palatine, IL 60067', '05/19/2020', 'Meningitis'),
('5305876737', 'Hendrik', 'Catriona', 737210291, '04/07/2011', '02/12/2005', 'Female', '890 Redwood Place, Naperville, IL 60540', '07/07/2016', 'Ear infection'),
('9244135949', 'Spear', 'Shaylyn', 287744348, '09/15/2014', '08/18/2005', 'Female', '111 Willow Lane, Champaign, IL 61820', '06/27/2018', 'Pneumonia'),
('4874155030', 'Ronnie', 'Leyla', 658135785, '09/23/2009', '10/12/2006', 'Female', '89 Sunbrook Parkway, Des Plaines, IL 60016', '02/11/2021', 'Strep throat'),
('5246007413', 'Masurel', 'Rosaleen', 647529843, '01/25/2023', '12/30/2009', 'Female', '333 Tulip Road, Bloomington, IL 61701', '4/13/2023', 'Strep throat'),
('0500203431', 'Leak', 'Rriocard', 768438277, '04/25/2014', '09/06/2009', 'Male', '555 Daisy Avenue, Elgin, IL 60120', '06/13/2017', 'Pneumonia'),
('8594054211', 'Burk', 'Jerrylee', 498800658, '07/01/2016', '05/19/2006', 'Female', '666 Poplar Road, Waukegan, IL 60085', '09/04/2017', 'Strep throat'),
('6128926959', 'Wheeler', 'Janith', 628175937, '10/12/2017', '05/25/2009', 'Female', '784 Ramsey Street, Palatine, IL 60067', '11/11/2018', 'Ear infection'),
('0132055368', 'Harries', 'Bettine', 888404986, '01/27/2011', '11/14/2005', 'Female', '565 Orchid Place, Skokie, IL 60076', '08/20/2015', 'Ear infection'),
('0889460949', 'Krystle', 'Malvina', 705867340, '09/09/2021', '01/05/2021', 'Female', '123 Elm Street, Chicago, IL 60601', '06/13/2022', 'Strep throat'),
('0877589380','Wilhelmina', 'Eugine', 878383145, '10/14/2009', '10/02/2006', 'Intersex', '1307 Bellgrove Center, Chicago, IL 60660', '02/28/2016', 'Bronchitis'),
('3272014055', 'Kindleysides', 'Levin', 354339935, '03/30/2013', '08/31/2012', 'Male', '111 Willow Lane, Champaign, IL 61820', '12/01/2022', 'Bronchitis'),
('3250381608', 'Ferrarese', 'Nolana', 202867000, '02/16/2017', '11/08/2008', 'Female', '890 Redwood Place, Naperville, IL 60540', '08/11/2020', 'Meningitis'),
('3322578003', 'Elsworth', 'Corinna', 217236599, '12/26/2021', '10/20/2018', 'Female', '234 Birch Road, Aurora, IL 60501', '03/21/2022', 'Pneumonia'),
('1993446753', 'Dockrill', 'Reinhard', 265976489, '04/08/2012', '08/20/2005', 'Male', '404 Doe Crossing Way, Des Plaines, IL 60016', '02/10/2015', 'Pneumonia'),
('5171542287', 'Bogays', 'Hanson', 440034099, '07/24/2017', '06/15/2004', 'Male', '004 Transport Place, Hoffman Estates, IL 60010', '02/28/2019', 'Ear infection'),
('3023402353', 'Ethersey', 'Regan', 484346757, '07/18/2009', '03/02/2006', 'Male', '444 Lily Lane, Evanston, IL 60201', '09/22/2021', 'Strep throat'),
('7140976783', 'Fancutt', 'Gerry', 463183198, '12/16/2012', '07/29/2011', 'Female', '121 Magnolia Drive, Bolingbrook, IL 60440', '08/01/2020', 'Bronchitis'),
('4647884775', 'Snare', 'Janela', 124304087, '01/03/2016', '02/16/2010', 'Female', '33528 Tony Pass, Champaign, IL 61820', '11/22/2022', 'Pneumonia'),
('7662072894', 'Aberkirder', 'Ardisj', 219675186, '04/27/2022', '06/27/2005', 'Intersex', '234 Birch Road, Aurora, IL 60501', '06/05/2023', 'Ear infection'),
('9055660728', 'Howgego', 'Francklyn', 748293355, '06/27/2020', '10/30/2010', 'Male', '890 Redwood Place, Naperville, IL 60540', '01/28/2023', 'Meningitis'),
('8113174095', 'Boggers', 'Vassili', 417647968, '05/15/2020', '07/02/2014', 'Male', '666 Poplar Road, Waukegan, IL 60085', '01/24/2022', 'Ear infection'),
('0792077342', 'Vania', 'Jere', 500224791, '01/21/2023', '06/03/2011', 'Female', '789 Oak Drive, Peoria, IL 61601', '11/20/2021', 'Strep throat'),
('9517512813', 'Wheeler', 'Jessica', 551855961, '06/09/2020', '04/13/2004', 'Female', '777 Sunflower Drive, Oak Park, IL 60301', '11/17/2022', 'Pneumonia');


INSERT INTO guardian (gID, gLast, gFirst, gSSN, gDOB, gSex, gAddress, gPhoneNum, gInsuranceCo, gInsuranceNum, gBalance)
VALUES
('8520489390', 'Krystle', 'Newlyn', 750817686, 'Female', '06/14/1957', '123 Elm Street, Chicago, IL 60601', 3034941575, 'Hettinger Group', '6891339960', 51666.84),
('7251298740', 'Wilhelmina', 'Standering', 594051136, 'Female', '01/03/1977', '456 Maple Avenue, Springfield, IL 62701', 4618171573, 'Sanford and Sons', '6857558183', 84567.45),
('6445290620', 'Vania', 'Nicolson', 769412787, 'Female', '10/30/1980', '789 Oak Drive, Peoria, IL 61601', 3419702825, 'Macejkovic Inc', '8545278918', 88203.48),
('7483012498', 'Elsie', 'Blacklock', 319616619, 'Female', '12/10/1979', '101 Pine Lane, Rockford, IL 61101', 6479535323, 'King Group', '2921673665', 68576.94),
('3285231780', 'Elsworth', 'Pennrington', 300410599, 'Male', '11/22/1956', '234 Birch Road, Aurora, IL 60501', 6513595804, 'West-Rolfson', '1526907097', 28278.86),
('2443645274', 'Kamilah', 'Ransom', '415449144', 'Female', '03/25/1985', '567 Cedar Court, Joliet, IL 60401', 4917588501, 'Stokes LLC', '8584982', 47155.55),
('2294796667', 'Willyt', 'Davidek', 499751144, 'Intersex', '03/11/1986', '890 Redwood Place, Naperville, IL 60540', 9996224458, 'Sanford and Sons', '5286573428', 65377.63),
('6088659734', 'Ruy', 'Bourdon', 317204627, 'Male', '11/30/1964', '111 Willow Lane, Champaign, IL 61820', 8902001586, 'Sanford and Sons', '1777314038', 69475.15),
('9387481093', 'Ronnie', 'Cham', 298629672, 'Male', '06/26/1947', '222 Rose Street, Decatur, IL 62521', 3093119202, 'Russel and Sons', '6728086994', 89725.46),
('5948730290', 'Coop', 'Oakland', 155279567, 'Male', '01/10/2003', '333 Tulip Road, Bloomington, IL 61701', 4898204438, 'King Group', '6631240743', 97270.26),
('3780291827', 'Bartel', 'Zannotti', 775640521, 'Male', '05/25/1936', '444 Lily Lane, Evanston, IL 60201', 1392838015, 'Hettinger Group', '9117554748', 86619.33),
('2299841340', 'Katharina', 'Dumini', 662248871, 'Female', '05/23/1933', '555 Daisy Avenue, Elgin, IL 60120', 5059969409, 'King Group', '6585379241', 2570.31),
('3008909523', 'Burk', 'Gorhardt', 115802264, 'Male', '04/18/1970', '666 Poplar Road, Waukegan, IL 60085', 5699243872, 'Gislason and Sons', '1708170677', 89896.33),
('1742238351', 'Wheeler', 'McGaraghan', 595118381, 'Male', '07/09/1996', '777 Sunflower Drive, Oak Park, IL 60301', 6376444647, 'Oberbrunner LLC', '402850793', 36708.67),
('4832078828', 'Frasco', 'Deverose', 204854710, 'Male', '01/03/1957', '888 Iris Court, Schaumburg, IL 60173', 8435265180, 'Kihn, Rippin and Littel', '74057065', 65317.42),
('3898341984', 'Grove', 'Dooney', 171953348, 'Male', '11/12/1994', '999 Violet Street, Des Plaines, IL 60016', 8509568818, 'Feeney-Bergstrom', '645316121', 81570.24),
('3487639351', 'Barr', 'MacShirie', 419030415, 'Male', '09/24/1938', '121 Magnolia Drive, Bolingbrook, IL 60440', 4131251880, 'Stoltenberg, Cormier and Wolff', '1547266287', 35918.82),
('1025530853', 'Cedric', 'Corsor', 652313710, 'Male', '05/02/1975', '232 Jasmine Lane, Arlington Heights, IL 60004', 7353921316, 'Turner LLC', '8179605159', 297.79),
('9030078855', 'Eberto', 'Schechter', 136141503, 'Male', '02/01/1973', '343 Camellia Road, Palatine, IL 60067', 8776366732, 'Sanford and Sons', '8667908061', 77961.15),
('3542638560', 'Gaile', 'Phillipp', 120714670, 'Male', '1/20/1967', '004 Transport Place, Hoffman Estates, IL 60010', 8492361075, 'Hettinger Group', '5729813460', 64823.13),
('3759410618', 'Keelia', 'Thomassin', 868415509, 'Female', '10/06/1943', '565 Orchid Place, Skokie, IL 60076', 4981610726, 'King Group', '5163206265', 89931.37);


INSERT INTO doctor (dID, dLast, dFirst, dSSN, dCreationDate, dDOB, dSex, dPhoneNum, dAddress)
VALUES
('2433573130', 'Hannie', 'Brewster', 737633372, '01/31/1998', '04/29/1955', 'Female', 3487007747, '5085 Brickson Park Point, Chicago, IL 60601'),
('4772535918', 'Malanie', 'Sherlock', 428365612, '04/21/2003', '08/13/1952', 'Female', 1605413705, '60 Portage Parkway, Springfield, IL 62701'),
('1550505211', 'Jeff', 'Woodhead', 375677629, '01/03/2022', '09/06/1965', 'Male', 9626948996, '3 Graedel Road, Peoria, IL 61601'),
('1228121907', 'Dante', 'Wrassell', 490999123, '04/05/2014', '08/23/1989', 'Intersex', 5977596025, '5 Mosinee Way, Champaign, IL 61801'),
('3790986631', 'Guendolen', 'Farmery', 327519163, '10/13/1999', '05/11/1954', 'Female', 2848412538, '9753 South Crossing, Rockford, IL 61101'),
('2059515203', 'Milena', 'Kornacki', 641570324, '11/07/2005', '04/21/1956', 'Female', 8437345485, '295 Merchant Pass, Naperville, IL 60540'),
('9800443347', 'Nerti', 'Dorot', 592858526, '10/30/1990', '11/01/1964', 'Female', 1479412914, '626 Esch Crossing, Aurora, IL 60502'),
('0933876661', 'Allissa', 'Gunson', 788826446, '01/29/2008', '09/11/1980', 'Female', 3922342686, '19 Fair Oaks Way, Elgin, IL 60120'),
('9513444856', 'Fancy', 'Mepsted', 379337869, '03/02/2019', '09/12/1994', 'Female', 3119915649, '07529 Oneill Circle, Joliet, IL 60432'),
('8044068996', 'Bord', 'Nys', 656026935, '08/08/2023', '09/19/1983', 'Male', 2566012680, '41013 Elmside Trail, Peoria, IL 61601'),
('7789964631', 'Prince', 'Coon', 781348881, '06/03/1993', '09/09/1959', 'Male', 2647699034, '3964 Alpine Junction, Springfield, IL 62701'),
('8399355941', 'Roseanna', 'Kropach', 440115178, '04/04/1996', '11/15/1962', 'Female', 8992722118, '5577 Mallory Terrace, Chicago, IL 60601'),
('0350061610', 'Audi', 'Caldroni', 610452092, '10/06/2009', '10/18/1951', 'Female', 1494287933, '243 Karstens Point, Rockford, IL 61101'),
('4775744720', 'Tamarah', 'Baybutt', 416983572, '05/05/1997', '03/02/1967', 'Female', 1043354810, '7176 Utah Alley, Naperville, IL 60540'),
('0292475659', 'Ernst', 'Twigger', 170012972, '10/08/2014', '08/07/1963', 'Male', 1583276754, '04116 Cardinal Way,  Aurora, IL 60502'),
('5012485009', 'Geordie', 'Bushell', 613020115, '08/04/2018', '02/25/1958', 'Male', 7023269059, '82464 Rockefeller Point, Elgin, IL 60120'),
('2680882318', 'Darryl', 'Meere', 644948705, '06/21/2007', '04/24/1961', 'Male', 1913324005, '6 Norway Maple Alley, Joliet, IL 60432'),
('5255868604', 'Westley', 'Gasticke', 131381367, '03/10/1981', '04/18/1950', 'Male', 2612489856, '8584 Vernon Way, Peoria, IL 61601'),
('0279554478', 'Rafe', 'Molan', 690722624, '08/22/2004', '08/06/1956', 'Male', 5376546617, '8 Claremont Trail, Springfield, IL 62701'),
('3567879413', 'Decca', 'Duval', 316904838, '02/14/2021', '02/14/1976', 'Male', 4011307663, '6 Mallory Street, Chicago, IL 60601');


INSERT INTO nurse (nID, nLast, nFirst, nSSN, nCreationDate, nDOB, nSex, nAddress, nPhoneNum)
VALUES
('8141746251', 'Cawston', 'Crichton', 133386325, '07/14/1993', '09/07/1941', 'Male', '789 Birch Lane, Elgin, IL 60120', 8607907498),
('0154784443', 'Van de Vlies', 'Neddie', 117903132, '05/02/2016', '08/26/1952', 'Female', '456 Cedar Drive, Schaumburg, IL 60173', 3883137131),
('7312243304', 'Shillington', 'Annice', 607028352, '07/21/2003', '05/10/1976', 'Female', '222 Rosewood Avenue, Champaign, IL 61820', 3511379758),
('8809364287', 'Fellis', 'Ward', 402910166, '06/20/2002', '07/27/1968', 'Male', '777 Maple Road, Joliet, IL 60401', 9866889824),
('2152501608', 'Maidment', 'Heddie', 184403209, '02/01/1993', '12/01/1963', 'Female', '888 Orchid Court, Springfield, IL 62701', 8901433799),
('8014003225', 'Giottini', 'Moise', 613896647, '10/10/2006', '12/06/1977', 'Male', '555 Poplar Street, Rockford, IL 61101', 6336354655),
('1637468687', 'Laing', 'Jamie', 287486779, '04/09/2008', '09/24/1972', 'Female', '101 Magnolia Lane, Evanston, IL 60201', 2389388225),
('1971290432', 'Micklewicz', 'Papageno', 677258976, '02/15/2014', '05/11/1985', 'Male', '444 Sunflower Drive, Naperville, IL 60540', 6283356820),
('1572910909', 'Matejovsky', 'Michelle', 779511883, '02/01/2013', '09/08/1980', 'Female', '123 Daisy Place, Waukegan, IL 60085', 8818731789),
('6918254634', 'Sabatini', 'Mareah', 459986433, '02/28/1993', '11/16/1958', 'Female', '999 Tulip Road, Aurora, IL 60501', 2835743718),
('7521039246', 'Cass', 'Anica', 540275983, '10/26/2002', '06/20/1958', 'Female', '333 Willow Lane, Bolingbrook, IL 60440', 6073558207),
('8699777841', 'Bradburn', 'Babette', 607427769, '03/12/1998', '11/14/1950', 'Female', '678 Iris Avenue, Oak Park, IL 60301', 9603362188),
('8224044106', 'Prinnett', 'Emalee', 721429396, '09/20/2008', '04/04/1948', 'Female', '334 Camellia Court, Palatine, IL 60067', 4158232955),
('4211715445', 'Mc Elory', 'Gustave', 824611315, '06/11/2007', '02/10/1978', 'Male', '223 Violet Drive, Skokie, IL 60076', 2021334200),
('9405259113', 'Rignoldes', 'Grayce', 157288048, '07/22/1984', '05/07/1950', 'Female', '1122 Camellia Road, Arlington Heights, IL 60004', 3816987127),
('0500653666', 'Fenelon', 'Beck', 164482298, '02/22/2019', '04/13/1992', 'Male', '33445 Magnolia Avenue, Des Plaines, IL 60016', 1729665919),
('7863847907', 'Hanburry', 'Cliff', 345999938, '03/04/1993', '09/03/1961', 'Male', '7788 Cedar Drive, Decatur, IL 62521', 9505415342),
('4518562909', 'Erickssen', 'Brandy', 381784196, '03/18/1999', '08/24/1969', 'Male', '5566 Oak Road, Bloomington, IL 61701', 4829859653),
('3781706605', 'Linford', 'Ezekiel', 821173956, '11/16/2000', '05/14/1968', 'Male', '4455 Pine Street, Peoria, IL 61601', 4751147507),
('7502613455', 'Jorgesen', 'Monroe', 359300314, '07/24/1988', '04/06/1960', 'Male', '2233 Rose Street, Champaign, IL 61820', 8899113136),
('0437021416', 'Gosden', 'Emmott', 471857430, '12/19/2002', '01/28/1972', 'Male', '11223 Birch Court, Decatur, IL 62521', 4206977820),
('9207937719', 'Shreeves', 'Felicity', 663325733, '03/04/1998', '07/31/1971', 'Female', '9900 Cedar Drive, Rockford, IL 61101', 3411034854),
('2946018539', 'Yerrell', 'Maye', 161494971, '09/02/2015', '11/23/1986', 'Female', '8899 Pine Lane, Aurora, IL 60501', 2467056423),
('2261402791', 'Korfmann', 'Bartlet', 815043410, '12/22/1989', '05/28/1966', 'Male', '7788 Birch Road, Evanston, IL 60201', 7972820721),
('7204524675', 'Hunter', 'Yves', 117358724, '05/03/1979', '10/03/1951', 'Male', '6677 Willow Lane, Joliet, IL 60401', 5799336219),
('0099317990', 'Mateiko', 'Torr', 897249834, '08/05/1996', '09/13/1961', 'Male', '5566 Daisy Avenue, Naperville, IL 60540', 5946253924),
('5964724701', 'Tuison', 'Darcy', 613311406, '09/25/1977', '08/30/1949', 'Female', '4455 Orchid Road, Waukegan, IL 60085', 7883379740),
('4636658116', 'Dodsworth', 'Wainwright', 873563511, '03/10/2015', '02/09/1986', 'Male', '3344 Tulip Place, Springfield, IL 62701', 2682492933),
('5120574106', 'Gebbe', 'Vaclav', 493266416, '08/26/2002', '05/26/1945', 'Male', '2233 Maple Drive, Schaumburg, IL 60173', 7868083559),
('0899054536', 'Woollaston', 'Tabbie', 159498707, '08/06/1988', '06/30/1959', 'Male', '1122 Rosewood Lane, Champaign, IL 61820', 7591134416);


INSERT INTO assignedToNur(pID, nID)
VALUES
('5478828149', '8224044106'), ('5478828149', '9207937719'), ('2353169554', '7312243304'),
('2353169554', '7502613455'), ('2867034035', '8809364287'), ('2867034035', '4636658116'),
('1608930009', '8141746251'), ('1608930009', '2946018539'), ('1135007012', '8699777841'),
('1135007012', '2946018539'), ('7487444848', '7521039246'), ('7487444848', '2261402791'),
('9376633717', '8224044106'), ('9376633717', '0437021416'), ('8343324366', '1637468687'),
('8343324366', '3781706605'), ('3339297274', '0154784443'), ('3339297274', '0500653666'),
('1309936374', '8014003225'), ('1309936374', '7863847907'), ('0943273102', '9405259113'),
('0943273102', '5120574106'), ('6040373601', '4211715445'), ('6040373601', '0500653666'),
('7336237347', '4211715445'), ('7336237347', '0500653666'), ('5737027589', '7312243304'),
('5737027589', '0899054536'), ('9926175422', '1637468687'), ('5548366882', '8141746251'),
('5548366882', '7863847907'), ('8652992541', '1971290432'), ('8652992541', '5964724701'),
('2439361151', '8224044106'), ('2439361151', '7502613455'), ('9575986083', '2152501608'),
('9575986083', '9207937719'), ('0934341656', '8224044106'), ('0934341656', '2946018539'),
('0184960495', '8014003225'), ('0184960495', '0099317990'), ('0219096953', '0154784443'),
('0219096953', '4518562909'), ('5348686204', '7312243304'), ('5348686204', '5120574106'),
('7092577144', '9405259113'), ('0987039997', '8014003225'), ('0987039997', '7502613455'),
('9060291182', '7312243304'), ('9060291182', '7204524675'), ('1345635524', '0154784443'),
('1345635524', '7863847907'), ('5305876737', '1971290432'), ('5305876737', '2946018539'),
('9244135949', '0154784443'), ('9244135949', '5120574106'), ('4874155030', '7312243304'),
('4874155030', '8014003225'), ('4874155030', '9207937719'), ('5246007413', '7502613455'),
('0500203431', '1637468687'), ('0500203431', '7863847907'), ('0500203431', '2261402791'),
('8594054211', '1971290432'), ('6128926959', '0500653666'), ('6128926959', '3781706605'),
('0132055368', '2152501608'), ('0132055368', '4518562909'), ('0889460949', '0500653666'),
('0889460949', '0437021416'), ('0877589380', '9405259113'), ('0877589380', '0899054536'),
('3272014055', '8014003225'), ('3272014055', '5964724701'), ('3250381608', '7521039246'),
('3250381608', '0437021416'), ('3322578003', '1572910909'), ('3322578003', '0899054536'),
('1993446753', '8141746251'), ('1993446753', '7502613455'), ('5171542287', '8141746251'),
('5171542287', '2261402791'), ('3023402353', '6918254634'), ('7140976783', '1572910909'),
('7140976783', '2261402791'), ('4647884775', '1572910909'), ('4647884775', '9207937719'),
('7662072894', '4211715445'), ('7662072894', '5120574106'), ('9055660728', '8699777841'),
('9055660728', '3781706605'), ('8113174095', '8809364287'), ('8113174095', '3781706605'),
('0792077342', '8809364287'), ('0792077342', '0899054536'), ('9517512813', '4211715445'),
('9517512813', '7204524675');


INSERT INTO assignedToDoc(pID, dID)
VALUES
('5478828149', '4775744720'), ('2353169554', '2059515203'), ('2867034035', '9513444856'),
('1608930009', '5012485009'), ('1135007012', '2059515203'), ('7487444848', '0292475659'),
('9376633717', '4772535918'), ('8343324366', '5012485009'), ('3339297274', '7789964631'),
('1309936374', '3567879413'), ('0943273102', '8044068996'), ('6040373601', '0279554478'),
('7336237347', '8044068996'), ('5737027589', '1550505211'), ('9926175422', '9800443347'),
('5548366882', '2680882318'), ('8652992541', '4772535918'), ('2439361151', '3567879413'),
('9575986083', '0933876661'), ('0934341656', '0350061610'), ('0184960495', '4775744720'),
('0219096953', '3567879413'), ('5348686204', '0350061610'), ('7092577144', '0279554478'),
('0987039997', '2680882318'), ('9060291182', '7789964631'), ('1345635524', '0933876661'),
('5305876737', '3790986631'), ('9244135949', '5012485009'), ('4874155030', '8399355941'),
('5246007413', '1228121907'), ('0500203431', '1228121907'), ('8594054211', '2680882318'),
('6128926959', '0292475659'), ('0132055368', '4772535918'), ('0889460949', '7789964631'),
('0877589380', '2433573130'), ('3272014055', '1550505211'), ('3250381608', '9513444856'),
('3322578003', '0350061610'), ('1993446753', '2059515203'), ('5171542287', '8044068996'),
('3023402353', '5255868604'), ('7140976783', '9800443347'), ('4647884775', '1228121907'),
('7662072894', '2433573130'), ('9055660728', '9513444856'), ('8113174095', '0292475659'),
('0792077342', '0279554478'), ('9517512813', '4775744720');


INSERT INTO dependentOf(pID, gID, gInsuranceCo, gInsuranceNum)
VALUES
('5478828149', '8520489390', 'Hettinger Group', '6891339960'),
('2353169554', '7251298740', 'Sanford and Sons', '6857558183'),
('2867034035', '6445290620', 'Macejkovic Inc', '8545278918'),
('1608930009', '7483012498', 'King Group', '2921673665'),
('1135007012', '3285231780', 'West-Rolfson', '1526907097'),
('7487444848', '2443645274', 'Stokes LLC', '8584982'),
('9376633717', '2294796667', 'Sanford and Sons', '5286573428'),
('8343324366', '6088659734', 'Sanford and Sons', '1777314038'),
('3339297274', '9387481093', 'Russel and Sons', '6728086994'),
('1309936374', '5948730290', 'King Group', '6631240743'),
('0943273102', '3780291827', 'Hettinger Group', '9117554748'),
('6040373601', '2299841340', 'King Group', '6585379241'),
('7336237347', '3008909523', 'Gislason and Sons', '1708170677'),
('5737027589', '1742238351', 'Oberbrunner LLC', '402850793'),
('9926175422', '4832078828', 'Kihn, Rippin and Littel', '74057065'),
('5548366882', '3898341984', 'Feeney-Bergstrom', '645316121'),
('8652992541', '3487639351', 'Stoltenberg, Cormier and Wolff', '1547266287'),
('2439361151', '1025530853', 'Turner LLC', '8179605159'),
('9575986083', '9030078855', 'Sanford and Sons', '8667908061'),
('0934341656', '3542638560', 'Hettinger Group', '5729813460'),
('0184960495', '3759410618', 'King Group', '5163206265'),
('0219096953', '8520489390', 'Hettinger Group', '6891339960'),
('5348686204', '7251298740', 'Sanford and Sons', '6857558183'),
('7092577144', '6445290620', 'Macejkovic Inc', '8545278918'),
('0987039997', '7483012498', 'King Group', '2921673665'),
('9060291182', '3285231780', 'West-Rolfson', '1526907097'),
('1345635524', '2443645274', 'Stokes LLC', '8584982'),
('5305876737', '2294796667', 'Sanford and Sons', '5286573428'),
('9244135949', '6088659734', 'Sanford and Sons', '1777314038'),
('4874155030', '9387481093', 'Russel and Sons', '6728086994'),
('5246007413', '5948730290', 'King Group', '6631240743'),
('0500203431', '2299841340', 'King Group', '6585379241'),
('8594054211', '3008909523', 'Gislason and Sons', '1708170677'),
('6128926959', '1742238351', 'Oberbrunner LLC', '402850793'),
('0132055368', '3759410618', 'King Group', '5163206265'),
('0889460949', '8520489390', 'Hettinger Group', '6891339960'),
('0877589380', '7251298740', 'Sanford and Sons', '6857558183'),
('3272014055', '6088659734', 'Sanford and Sons', '1777314038'),
('3250381608', '2294796667', 'Sanford and Sons', '5286573428'),
('3322578003', '3285231780', 'West-Rolfson', '1526907097'),
('1993446753', '3008909523', 'Gislason and Sons', '1708170677'),
('5171542287', '3542638560', 'Hettinger Group', '5729813460'),
('3023402353', '3780291827', 'Hettinger Group', '9117554748'),
('7140976783', '3487639351', 'Stoltenberg, Cormier and Wolff', '1547266287'),
('4647884775', '6088659734', 'Sanford and Sons', '1777314038'),
('7662072894', '3285231780', 'West-Rolfson', '1526907097'),
('9055660728', '2294796667', 'Sanford and Sons', '5286573428'),
('8113174095', '3008909523', 'Gislason and Sons', '1708170677'),
('0792077342', '6445290620', 'Macejkovic Inc', '8545278918'),
('9517512813', '1742238351', 'Oberbrunner LLC', '402850793');


--Query 1: 
SELECT P.pID, P.pFirst, P.pLast, P.pIllness, P.pDOB, P.pAddress,
       (SELECT G.gAddress
        FROM guardian G
        WHERE G.gID = (SELECT D.gID
                        FROM dependentOf D
                        WHERE D.pID = P.pID)) AS gAddress,
       (SELECT COUNT(N.nID)
        FROM nurse N
        WHERE N.nID IN (SELECT A.nID
                        FROM assignedToNur A
                        WHERE A.pID = P.pID)) AS numberOfNurses
FROM patient P
WHERE P.pIllness = 'Pneumonia'
              AND DATE(P.pDOB) >= '01/01/2005'
               AND P.pAddress = (SELECT G.gAddress
                                FROM guardian G
                                WHERE G.gID = (SELECT D.gID
                                               FROM dependentOf D
                                                WHERE D.pID = P.pID))
GROUP BY P.pID
ORDER BY P.pFirst ASC;


--Query 2:
SELECT g.gID,  g.gLast  SUM(g.gBalance) AS TotalBalance, COUNT(d.pID) AS NumberOfDependents
FROM guardian g, dependentOf d
WHERE  g.gID = d.gID
GROUP BY g.gID, g.gLast
ORDER BY  g.gLast;


--Query 3:
SELECT D.dFirst, D.dLast,
    (SELECT COUNT(*)
        FROM assignedToDoc AD
        WHERE AD.dID = D.dID
        AND AD.pID IN (
            SELECT pID
            FROM patient P
            WHERE P.pSex = 'Female'
        )
    ) AS numFemalePatients
FROM doctor D
WHERE  (SELECT COUNT(*)
        FROM assignedToDoc AD
        WHERE AD.dID = D.dID
        AND AD.pID IN (
            SELECT pID
            FROM patient P
            WHERE P.pSex = 'Female'
        )
    ) >= 1
ORDER BY numFemalePatients ASC;


--Query 4:
SELECT N.nLast, N.nFirst, N.nID, N.nSex, A.numPatients,
(SELECT string_agg(pID, ',')
FROM assignedToNur
WHERE nID = a.nID) as listOfPatients
FROM nurse N,
(SELECT nID, count(pID) as numPatients
FROM assignedToNur
GROUP BY nID
HAVING count(pID) <= 3) A
WHERE N.nID = A.nID
ORDER BY numPatients, nLast;

