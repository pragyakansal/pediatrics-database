from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

#DB Connection: create_engine(DBMS_name+driver://<username>:<password>@<hostname>/<database_name>)
engine = create_engine("postgresql+psycopg2://postgres:Pk21265003649914#@localhost:5433/postgres")

#Define Classes/Tables
class Base(DeclarativeBase):
	pass

class Patient(Base):
	__tablename__ = 'patient'
	pID: Mapped[str] = mapped_column(String(10), primary_key = True, nullable = False)
	pLast: Mapped[str] = mapped_column(String(30), nullable = False)
	pFirst: Mapped[str] = mapped_column(String(30), nullable = False)
	pSSN: Mapped[int] = mapped_column(Integer, nullable = False)
	pCreationDate: Mapped[str] = mapped_column(String(10), nullable = False)
	pDOB: Mapped[str] = mapped_column(String(10), nullable = False)
	pSex: Mapped[str] = mapped_column(String(10), nullable = False)
	pAddress: Mapped[str] = mapped_column(String(100), nullable = False)
	pLastAppt: Mapped[str] = mapped_column(String(10), nullable = False)
	pIllness: Mapped[str] = mapped_column(String(250), nullable = False)


class Guardian(Base):
	__tablename__ = 'guardian'
	gID: Mapped[str] = mapped_column(String(10), primary_key = True, nullable = False)
	gLast: Mapped[str] = mapped_column(String(30), nullable = False)
	gFirst: Mapped[str] = mapped_column(String(30), nullable = False)
	gSSN: Mapped[int] = mapped_column(Integer, nullable = False)
	gDOB: Mapped[int] = mapped_column(String (10), nullable = False)
	gSex: Mapped[str] = mapped_column(String(10), nullable = False)
	gAddress: Mapped[str] = mapped_column(String(100), nullable = False)
	gPhoneNum: Mapped[str] = mapped_column(String(10), nullable = False)
	gInsuranceCo: Mapped[str] = mapped_column(String(100), nullable = False)
	gInsuranceNum: Mapped[str] = mapped_column(String(10), nullable = False)
	gBalance: Mapped[int] = mapped_column(Integer, nullable = False)


class Doctor(Base):
	__tablename__ = 'doctor'
	dID: Mapped[str] = mapped_column(String(10), primary_key = True, nullable = False)
	dLast: Mapped[str] = mapped_column(String(30), nullable = False)
	dFirst: Mapped[str] = mapped_column(String(30), nullable = False)
	dSSN: Mapped[int] = mapped_column(Integer, nullable = False)
	dCreationDate: Mapped[str] = mapped_column(String(10), nullable = False)
	dDOB: Mapped[str] = mapped_column(String(10), nullable = False)
	dSex: Mapped[str] = mapped_column(String(10), nullable = False)
	dAddress: Mapped[str] = mapped_column(String(100), nullable = False)
	dPhoneNum: Mapped[str] = mapped_column(String(10), nullable = False)

class Nurse(Base):
	__tablename__ = 'nurse'
	nID: Mapped[str] = mapped_column(String(10), primary_key = True, nullable = False)
	nLast: Mapped[str] = mapped_column(String(30), nullable = False)
	nFirst: Mapped[str] = mapped_column(String(30), nullable = False)
	nSSN: Mapped[int] = mapped_column(Integer, nullable = False)
	nCreationDate: Mapped[str] = mapped_column(String(10), nullable = False)
	nDOB: Mapped[str] = mapped_column(String(10), nullable = False)
	nSex: Mapped[str] = mapped_column(String(10), nullable = False)
	nAddress: Mapped[str] = mapped_column(String(100), nullable = False)
	nPhoneNum: Mapped[str] = mapped_column(String(10), nullable = False)
	
class AssignedToNur(Base):
	__tablename__ = 'assignedToNur'
	pID: Mapped[str] = mapped_column(String(10), ForeignKey('patient.pID'), primary_key = True, nullable = False)
	nID: Mapped[str] = mapped_column(String(10), ForeignKey('nurse.nID'), primary_key = True, nullable=False)
	patient = relationship('Patient', back_populates = 'assigned_nurses')
	nurse = relationship('Nurse', back_populates = 'assigned_patients')
	Patient.assigned_nurses = relationship('AssignedToNur', back_populates='patient')
	Nurse.assigned_patients = relationship('AssignedToNur', back_populates='nurse')

	
class AssignedToDoc(Base):
    __tablename__ = 'assignedToDoc'
    pID: Mapped[str] = mapped_column(String(10), ForeignKey('patient.pID'), primary_key=True, nullable=False)
    dID: Mapped[str] = mapped_column(String(10), ForeignKey('doctor.dID'), nullable=False)
    assigned_doctor = relationship('Doctor', back_populates='assigned_patients')
    assigned_patients = relationship('Patient', back_populates='assigned_doctor')
    Patient.assigned_doctor = relationship('AssignedToDoc', back_populates='assigned_patients')
    Doctor.assigned_patients = relationship('AssignedToDoc', back_populates='assigned_doctor')
	
class DependentOf(Base):
	__tablename__= 'dependentOf'
	pID: Mapped[str] = mapped_column(String(10), ForeignKey('patient.pID'), primary_key = True, nullable = False)
	gID: Mapped[str] = mapped_column(String(10), ForeignKey('guardian.gID'), nullable = False)
	

#Create Tables
Base.metadata.create_all(engine)

#Insert Data

# Patient
with Session(engine) as session:
  patient1 = Patient(
	pID="5478828149",
	pLast="Krystle",
	pFirst="Carree",
	pSSN=880668772,
	pCreationDate="05/19/2011",
	pDOB="03/01/2007",
	pSex="Female",
	pAddress="123 Elm Street, Chicago, IL 60601",
	pLastAppt="9/15/2012",
	pIllness="Pneumonia")

patient2 = Patient(
	pID="2353169554",
	pLast="Wilhelmina",
	pFirst="Muhammad",
	pSSN=289612554,
	pCreationDate="07/01/2022",
	pDOB="07/12/2018",
	pSex="Male",
	pAddress="456 Maple Avenue, Springfield, IL 62701",
	pLastAppt="7/28/2022",
	pIllness="Pneumonia")

patient3 = Patient(
	pID="2867034035",
	pLast="Vania",
	pFirst="Marielle",
	pSSN=810946847,
	pCreationDate="10/26/2019",
	pDOB="03/24/2009",
	pSex="Female",
	pAddress="04 Grasskamp Trail, Chicago, IL 60626",
	pLastAppt="6/7/2020",
	pIllness="Bronchitis")

patient4 = Patient(
    pID="1608930009",
    pLast="Elsie",
    pFirst="Sayres",
    pSSN=402543798,
    pCreationDate="10/07/2020",
    pDOB="03/31/2017",
    pSex="Male",
    pAddress="101 Pine Lane, Rockford, IL 61101",
    pLastAppt="9/22/2021",
    pIllness="Meningitis")

patient5 = Patient(
    pID="1135007012",
    pLast="Elsworth",
    pFirst="Emmeline",
    pSSN=779483273,
    pCreationDate="01/19/2017",
    pDOB="04/06/2012",
    pSex="Female",
    pAddress="234 Birch Road, Aurora, IL 60501",
    pLastAppt="7/31/2019",
    pIllness="Strep throat")

patient6 = Patient(
    pID="7487444848",
    pLast="Kamilah",
    pFirst="Annabell",
    pSSN=190434601,
    pCreationDate="11/16/2015",
    pDOB="05/14/2008",
    pSex="Female",
    pAddress="567 Cedar Court, Joliet, IL 60401",
    pLastAppt="10/08/2017",
    pIllness="Strep throat")

patient7 = Patient(
    pID="9376633717",
    pLast="Redsull",
    pFirst="Sybyl",
    pSSN=458872004,
    pCreationDate="04/04/2018",
    pDOB="04/08/2016",
    pSex="Female",
    pAddress="890 Redwood Place, Naperville, IL 60540",
    pLastAppt="03/01/2020",
    pIllness="Ear infection")

patient8 = Patient(
    pID="8343324366",
    pLast="Blanko",
    pFirst="Tamera",
    pSSN=472840421,
    pCreationDate="03/31/2015",
    pDOB="09/04/2014",
    pSex="Female",
    pAddress="111 Willow Lane, Champaign, IL 61820",
    pLastAppt="09/24/2016",
    pIllness="Strep throat")

patient9 = Patient(
    pID="3339297274",
    pLast="Ronnie",
    pFirst="Arabelle",
    pSSN=436986178,
    pCreationDate="10/22/2008",
    pDOB="10/30/2005",
    pSex="Female",
    pAddress="30018 Grayhawk Plaza, Hoffman Estates, IL 60010",
    pLastAppt="03/08/2010",
    pIllness="Meningitis")

patient10 = Patient(
    pID="1309936374",
    pLast="Ortes",
    pFirst="Link",
    pSSN=113725928,
    pCreationDate="04/20/2020",
    pDOB="10/13/2004",
    pSex="Intersex",
    pAddress="333 Tulip Road, Bloomington, IL 61701",
    pLastAppt="11/16/2022",
    pIllness="Bronchitis")

patient11 = Patient(
    pID="0943273102",
    pLast="Enrique",
    pFirst="Erhart",
    pSSN=258626663,
    pCreationDate="06/13/2023",
    pDOB="04/11/2023",
    pSex="Male",
    pAddress="87634 Londonderry Crossing, Naperville, IL 60540",
    pLastAppt="7/4/2023",
    pIllness="Pneumonia")

patient12 = Patient(
    pID="6040373601",
    pLast="Dyson",
    pFirst="Fowler",
    pSSN=337648422,
    pCreationDate="06/26/2018",
    pDOB="10/09/2008",
    pSex="Male",
    pAddress="555 Daisy Avenue, Elgin, IL 60120",
    pLastAppt="11/16/2021",
    pIllness="Pneumonia")

patient13 = Patient(
    pID="7336237347",
    pLast="Burk",
    pFirst="Rodd",
    pSSN=596023469,
    pCreationDate="07/20/2016",
    pDOB="01/03/2016",
    pSex="Male",
    pAddress="666 Poplar Road, Waukegan, IL 60085",
    pLastAppt="02/04/2022",
    pIllness="Strep throat")

patient14 = Patient(
    pID="5737027589",
    pLast="Wheeler",
    pFirst="Gwyn",
    pSSN=377163080,
    pCreationDate="03/31/2018",
    pDOB="03/18/2005",
    pSex="Female",
    pAddress="3 Crowley Junction, Decatur, IL 62521",
    pLastAppt="8/26/2023",
    pIllness="Ear infection")

patient15 = Patient(
    pID="9926175422",
    pLast="Godden",
    pFirst="Reg",
    pSSN=123097541,
    pCreationDate="03/27/2007",
    pDOB="06/06/2004",
    pSex="Male",
    pAddress="888 Iris Court, Schaumburg, IL 60173",
    pLastAppt="02/08/2019",
    pIllness="Bronchitis")

patient16 = Patient(
    pID="5548366882",
    pLast="MacDearmont",
    pFirst="Ricoriki",
    pSSN=712332074,
    pCreationDate="07/22/2021",
    pDOB="07/17/2006",
    pSex="Male",
    pAddress="7539 Cordelia Place, Arlington Heights, IL 60004",
    pLastAppt="6/2/2022",
    pIllness="Meningitis")

patient17 = Patient(
    pID="8652992541",
    pLast="Idel",
    pFirst="Chrisse",
    pSSN=406111109,
    pCreationDate="04/26/2016",
    pDOB="12/04/2011",
    pSex="Male",
    pAddress="121 Magnolia Drive, Bolingbrook, IL 60440",
    pLastAppt="08/17/2019",
    pIllness="Strep throat")

patient18 = Patient(
    pID="2439361151",
    pLast="Cadany",
    pFirst="Guenevere",
    pSSN=784677467,
    pCreationDate="06/10/2018",
    pDOB="07/27/2014",
    pSex="Intersex",
    pAddress="232 Jasmine Lane, Arlington Heights, IL 60004",
    pLastAppt="06/17/2022",
    pIllness="Ear infection")

patient19 = Patient(
    pID="9575986083",
    pLast="Franchyonok",
    pFirst="Vitoria",
    pSSN=225831527,
    pCreationDate="05/31/2011",
    pDOB="01/27/2005",
    pSex="Female",
    pAddress="40 Arizona Center, Elgin, IL 60120",
    pLastAppt="04/24/2019",
    pIllness="Ear infection")

patient20 = Patient(
    pID="0934341656",
    pLast="Owlner",
    pFirst="Margarita",
    pSSN=309447807,
    pCreationDate="08/04/2014",
    pDOB="08/07/2009",
    pSex="Female",
    pAddress="004 Transport Place, Hoffman Estates, IL 60010",
    pLastAppt="02/28/2018",
    pIllness="Bronchitis")

patient21 = Patient(
    pID="0184960495",
    pLast="Maulkin",
    pFirst="Ham",
    pSSN=335142985,
    pCreationDate="10/29/2014",
    pDOB="08/20/2007",
    pSex="Male",
    pAddress="565 Orchid Place, Skokie, IL 60076",
    pLastAppt="05/18/2021",
    pIllness="Pneumonia")

patient22 = Patient(
    pID="0219096953",
    pLast="Krystle",
    pFirst="Bruce",
    pSSN=573503356,
    pCreationDate="07/24/2021",
    pDOB="12/25/2011",
    pSex="Male",
    pAddress="123 Elm Street, Chicago, IL 60601",
    pLastAppt="03/19/2022",
    pIllness="Pneumonia")

patient23 = Patient(
    pID="5348686204",
    pLast="Wilhelmina",
    pFirst="Ody",
    pSSN=574132898,
    pCreationDate="05/06/2018",
    pDOB="06/11/2005",
    pSex="Male",
    pAddress="456 Maple Avenue, Springfield, IL 62701",
    pLastAppt="04/18/2023",
    pIllness="Ear infection")

patient24 = Patient(
    pID="7092577144",
    pLast="Vania",
    pFirst="Freddy",
    pSSN=739287636,
    pCreationDate="01/11/2019",
    pDOB="07/06/2011",
    pSex="Male",
    pAddress="24740 Northland Parkway, Bloomington, IL 61701",
    pLastAppt="04/19/2020",
    pIllness="Strep throat")

patient25 = Patient(
    pID="0987039997",
    pLast="Elsie",
    pFirst="Tildie",
    pSSN=365855409,
    pCreationDate="03/31/2006",
    pDOB="09/08/2005",
    pSex="Intersex",
    pAddress="101 Pine Lane, Rockford, IL 61101",
    pLastAppt="07/20/2017",
    pIllness="Bronchitis")

patient26 = Patient(
    pID="9060291182",
    pLast="Elsworth",
    pFirst="Wayne",
    pSSN=100086560,
    pCreationDate="06/05/2021",
    pDOB="05/25/2013",
    pSex="Male",
    pAddress="234 Birch Road, Aurora, IL 60501",
    pLastAppt="07/07/2023",
    pIllness="Ear infection")

patient27 = Patient(
    pID="1345635524",
    pLast="Kamilah",
    pFirst="Donnie",
    pSSN=616587978,
    pCreationDate="02/19/2020",
    pDOB="01/10/2004",
    pSex="Female",
    pAddress="08 Bonner Street, Palatine, IL 60067",
    pLastAppt="05/19/2020",
    pIllness="Meningitis")

patient28 = Patient(
    pID="5305876737",
    pLast="Hendrik",
    pFirst="Catriona",
    pSSN=737210291,
    pCreationDate="04/07/2011",
    pDOB="02/12/2005",
    pSex="Female",
    pAddress="890 Redwood Place, Naperville, IL 60540",
    pLastAppt="07/07/2016",
    pIllness="Ear infection")

patient29 = Patient(
    pID="9244135949",
    pLast="Spear",
    pFirst="Shaylyn",
    pSSN=287744348,
    pCreationDate="09/15/2014",
    pDOB="08/18/2005",
    pSex="Female",
    pAddress="111 Willow Lane, Champaign, IL 61820",
    pLastAppt="06/27/2018",
    pIllness="Pneumonia")

patient30 = Patient(
    pID="4874155030",
    pLast="Ronnie",
    pFirst="Leyla",
    pSSN=658135785,
    pCreationDate="09/23/2009",
    pDOB="10/12/2006",
    pSex="Female",
    pAddress="89 Sunbrook Parkway, Des Plaines, IL 60016",
    pLastAppt="02/11/2021",
    pIllness="Strep throat")

patient31 = Patient(
    pID="5246007413",
    pLast="Masurel",
    pFirst="Rosaleen",
    pSSN=647529843,
    pCreationDate="01/25/2023",
    pDOB="12/30/2009",
    pSex="Female",
    pAddress="333 Tulip Road, Bloomington, IL 61701",
    pLastAppt="4/13/2023",
    pIllness="Strep throat")

patient32 = Patient(
    pID="0500203431",
    pLast="Leak",
    pFirst="Rriocard",
    pSSN=768438277,
    pCreationDate="04/25/2014",
    pDOB="09/06/2009",
    pSex="Male",
    pAddress="555 Daisy Avenue, Elgin, IL 60120",
    pLastAppt="06/13/2017",
    pIllness="Pneumonia")

patient33 = Patient(
    pID="8594054211",
    pLast="Burk",
    pFirst="Jerrylee",
    pSSN=498800658,
    pCreationDate="07/01/2016",
    pDOB="05/19/2006",
    pSex="Female",
    pAddress="666 Poplar Road, Waukegan, IL 60085",
    pLastAppt="09/04/2017",
    pIllness="Strep throat")

patient34 = Patient(
    pID="6128926959",
    pLast="Wheeler",
    pFirst="Janith",
    pSSN=628175937,
    pCreationDate="10/12/2017",
    pDOB="05/25/2009",
    pSex="Female",
    pAddress="784 Ramsey Street, Palatine, IL 60067",
    pLastAppt="11/11/2018",
    pIllness="Ear infection")

patient35 = Patient(
    pID="0132055368",
    pLast="Harries",
    pFirst="Bettine",
    pSSN=888404986,
    pCreationDate="01/27/2011",
    pDOB="11/14/2005",
    pSex="Female",
    pAddress="565 Orchid Place, Skokie, IL 60076",
    pLastAppt="08/20/2015",
    pIllness="Ear infection")

patient36 = Patient(
    pID="0889460949",
    pLast="Krystle",
    pFirst="Malvina",
    pSSN=705867340,
    pCreationDate="09/09/2021",
    pDOB="01/05/2021",
    pSex="Female",
    pAddress="123 Elm Street, Chicago, IL 60601",
    pLastAppt="06/13/2022",
    pIllness="Strep throat")

patient37 = Patient(
    pID="0877589380",
    pLast="Wilhelmina",
    pFirst="Eugine",
    pSSN=878383145,
    pCreationDate="10/14/2009",
    pDOB="10/02/2006",
    pSex="Intersex",
    pAddress="1307 Bellgrove Center, Chicago, IL 60660",
    pLastAppt="02/28/2016",
    pIllness="Bronchitis")

patient38 = Patient(
    pID="3272014055",
    pLast="Kindleysides",
    pFirst="Levin",
    pSSN=354339935,
    pCreationDate="03/30/2013",
    pDOB="08/31/2012",
    pSex="Male",
    pAddress="111 Willow Lane, Champaign, IL 61820",
    pLastAppt="12/01/2022",
    pIllness="Bronchitis")

patient39 = Patient(
    pID="3250381608",
    pLast="Ferrarese",
    pFirst="Nolana",
    pSSN=202867000,
    pCreationDate="02/16/2017",
    pDOB="11/08/2008",
    pSex="Female",
    pAddress="890 Redwood Place, Naperville, IL 60540",
    pLastAppt="08/11/2020",
    pIllness="Meningitis")

patient40 = Patient(
    pID="3322578003",
    pLast="Elsworth",
    pFirst="Corinna",
    pSSN=217236599,
    pCreationDate="12/26/2021",
    pDOB="10/20/2018",
    pSex="Female",
    pAddress="234 Birch Road, Aurora, IL 60501",
    pLastAppt="03/21/2022",
    pIllness="Pneumonia")

patient41 = Patient(
    pID="1993446753",
    pLast="Dockrill",
    pFirst="Reinhard",
    pSSN=265976489,
    pCreationDate="04/08/2012",
    pDOB="08/20/2005",
    pSex="Male",
    pAddress="404 Doe Crossing Way, Des Plaines, IL 60016",
    pLastAppt="02/10/2015",
    pIllness="Pneumonia")

patient42 = Patient(
    pID="5171542287",
    pLast="Bogays",
    pFirst="Hanson",
    pSSN=440034099,
    pCreationDate="07/24/2017",
    pDOB="06/15/2004",
    pSex="Male",
    pAddress="004 Transport Place, Hoffman Estates, IL 60010",
    pLastAppt="02/28/2019",
    pIllness="Ear infection")

patient43 = Patient(
    pID="3023402353",
    pLast="Ethersey",
    pFirst="Regan",
    pSSN=484346757,
    pCreationDate="07/18/2009",
    pDOB="03/02/2006",
    pSex="Male",
    pAddress="444 Lily Lane, Evanston, IL 60201",
    pLastAppt="09/22/2021",
    pIllness="Strep throat")

patient44 = Patient(
    pID="7140976783",
    pLast="Fancutt",
    pFirst="Gerry",
    pSSN=463183198,
    pCreationDate="12/16/2012",
    pDOB="07/29/2011",
    pSex="Female",
    pAddress="121 Magnolia Drive, Bolingbrook, IL 60440",
    pLastAppt="08/01/2020",
    pIllness="Bronchitis")

patient45 = Patient(
    pID="4647884775",
    pLast="Snare",
    pFirst="Janela",
    pSSN=124304087,
    pCreationDate="01/03/2016",
    pDOB="02/16/2010",
    pSex="Female",
    pAddress="33528 Tony Pass, Champaign, IL 61820",
    pLastAppt="11/22/2022",
    pIllness="Pneumonia")

patient46 = Patient(
    pID="7662072894",
    pLast="Aberkirder",
    pFirst="Ardisj",
    pSSN=219675186,
    pCreationDate="04/27/2022",
    pDOB="06/27/2005",
    pSex="Intersex",
    pAddress="234 Birch Road, Aurora, IL 60501",
    pLastAppt="06/05/2023",
    pIllness="Ear infection")

patient47 = Patient(
    pID="9055660728",
    pLast="Howgego",
    pFirst="Francklyn",
    pSSN=748293355,
    pCreationDate="06/27/2020",
    pDOB="10/30/2010",
    pSex="Male",
    pAddress="890 Redwood Place, Naperville, IL 60540",
    pLastAppt="01/28/2023",
    pIllness="Meningitis")

patient48 = Patient(
    pID="8113174095",
    pLast="Boggers",
    pFirst="Vassili",
    pSSN=417647968,
    pCreationDate="05/15/2020",
    pDOB="07/02/2014",
    pSex="Male",
    pAddress="666 Poplar Road, Waukegan, IL 60085",
    pLastAppt="01/24/2022",
    pIllness="Ear infection")

patient49 = Patient(
    pID="0792077342",
    pLast="Vania",
    pFirst="Jere",
    pSSN=500224791,
    pCreationDate="01/21/2023",
    pDOB="06/03/2011",
    pSex="Female",
    pAddress="789 Oak Drive, Peoria, IL 61601",
    pLastAppt="11/20/2021",
    pIllness="Strep throat")

patient50 = Patient(
    pID="9517512813",
    pLast="Wheeler",
    pFirst="Jessica",
    pSSN=551855961,
    pCreationDate="06/09/2020",
    pDOB="04/13/2004",
    pSex="Female",
    pAddress="777 Sunflower Drive, Oak Park, IL 60301",
    pLastAppt="11/17/2022",
    pIllness="Pneumonia")

session.add_all([patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8,
patient9, patient10, patient11, patient12, patient13, patient14, patient15, patient16, patient17, 
patient18, patient19, patient20, patient21, patient22, patient23, patient24, patient25, patient26,
patient27, patient28, patient29, patient30, patient31, patient32, patient33, patient34, patient35,
patient36, patient37, patient38, patient39, patient40, patient41, patient42, patient43, patient44,
patient45, patient46, patient47, patient48, patient49, patient50])
session.commit()

# Guardian
with Session(engine) as session:
	guardian1 = Guardian(
    gID="8520489390",
    gLast="Krystle",
    gFirst="Newlyn",
    gSSN=750817686,
    gDOB="06/14/1957",
    gSex="Female",
    gAddress="123 Elm Street, Chicago, IL 60601",
    gPhoneNum="3034941575",
    gInsuranceCo="Hettinger Group",
    gInsuranceNum="6891339960",
    gBalance=51666.84)

guardian2 = Guardian(
    gID="7251298740",
    gLast="Wilhelmina",
    gFirst="Standering",
    gSSN=594051136,
    gDOB="01/03/1977",
    gSex="Female",
    gAddress="456 Maple Avenue, Springfield, IL 62701",
    gPhoneNum="4618171573",
    gInsuranceCo="Sanford and Sons",
    gInsuranceNum="6857558183",
    gBalance=84567.45)

guardian3 = Guardian(
    gID="6445290620",
    gLast="Vania",
    gFirst="Nicolson",
    gSSN=769412787,
    gDOB="10/30/1980",
    gSex="Female",
    gAddress="789 Oak Drive, Peoria, IL 61601",
    gPhoneNum="3419702825",
    gInsuranceCo="Macejkovic Inc",
    gInsuranceNum="8545278918",
    gBalance=88203.48)

guardian4 = Guardian(
    gID="7483012498",
    gLast="Elsie",
    gFirst="Blacklock",
    gSSN=319616619,
    gDOB="12/10/1979",
    gSex="Female",
    gAddress="101 Pine Lane, Rockford, IL 61101",
    gPhoneNum="6479535323",
    gInsuranceCo="King Group",
    gInsuranceNum="2921673665",
    gBalance=68576.94)

guardian5 = Guardian(
    gID="3285231780",
    gLast="Elsworth",
    gFirst="Pennrington",
    gSSN=300410599,
    gDOB="11/22/1956",
    gSex="Male",
    gAddress="234 Birch Road, Aurora, IL 60501",
    gPhoneNum="6513595804",
    gInsuranceCo="West-Rolfson",
    gInsuranceNum="1526907097",
    gBalance=28278.86)

guardian6 = Guardian(
    gID="2443645274",
    gLast="Kamilah",
    gFirst="Ransom",
    gSSN="415449144",
    gDOB="03/25/1985",
    gSex="Female",
    gAddress="567 Cedar Court, Joliet, IL 60401",
    gPhoneNum="4917588501",
    gInsuranceCo="Stokes LLC",
    gInsuranceNum="8584982",
    gBalance=47155.55)

guardian7 = Guardian(
    gID="2294796667",
    gLast="Willyt",
    gFirst="Davidek",
    gSSN=499751144,
    gDOB="03/11/1986",
    gSex="Intersex",
    gAddress="890 Redwood Place, Naperville, IL 60540",
    gPhoneNum="9996224458",
    gInsuranceCo="Sanford and Sons",
    gInsuranceNum="5286573428",
    gBalance=65377.63)

guardian8 = Guardian(
    gID="6088659734",
    gLast="Ruy",
    gFirst="Bourdon",
    gSSN=317204627,
    gDOB="11/30/1964",
    gSex="Male",
    gAddress="111 Willow Lane, Champaign, IL 61820",
    gPhoneNum="8902001586",
    gInsuranceCo="Sanford and Sons",
    gInsuranceNum="1777314038",
    gBalance=69475.15)

guardian9 = Guardian(
    gID="9387481093",
    gLast="Ronnie",
    gFirst="Cham",
    gSSN=298629672,
    gDOB="Male",
    gSex="06/26/1947",
    gAddress="222 Rose Street, Decatur, IL 62521",
    gPhoneNum="3093119202",
    gInsuranceCo="Russel and Sons",
    gInsuranceNum="6728086994",
    gBalance=89725.46)

guardian10 = Guardian(
    gID="5948730290",
    gLast="Coop",
    gFirst="Oakland",
    gSSN=155279567,
    gDOB="Male",
    gSex="01/10/2003",
    gAddress="333 Tulip Road, Bloomington, IL 61701",
    gPhoneNum="4898204438",
    gInsuranceCo="King Group",
    gInsuranceNum="6631240743",
    gBalance=97270.26)

guardian11 = Guardian(
    gID="3780291827",
    gLast="Bartel",
    gFirst="Zannotti",
    gSSN=775640521,
    gDOB="Male",
    gSex="05/25/1936",
    gAddress="444 Lily Lane, Evanston, IL 60201",
    gPhoneNum="1392838015",
    gInsuranceCo="Hettinger Group",
    gInsuranceNum="9117554748",
    gBalance=86619.33)

guardian12 = Guardian(
    gID="2299841340",
    gLast="Katharina",
    gFirst="Dumini",
    gSSN=662248871,
    gDOB="Female",
    gSex="05/23/1933",
    gAddress="555 Daisy Avenue, Elgin, IL 60120",
    gPhoneNum="5059969409",
    gInsuranceCo="King Group",
    gInsuranceNum="6585379241",
    gBalance=2570.31)

guardian13 = Guardian(
    gID="3008909523",
    gLast="Burk",
    gFirst="Gorhardt",
    gSSN=115802264,
    gDOB="Male",
    gSex="04/18/1970",
    gAddress="666 Poplar Road, Waukegan, IL 60085",
    gPhoneNum="5699243872",
    gInsuranceCo="Gislason and Sons",
    gInsuranceNum="1708170677",
    gBalance=89896.33)

guardian14 = Guardian(
    gID="1742238351",
    gLast="Wheeler",
    gFirst="McGaraghan",
    gSSN=595118381,
    gDOB="Male",
    gSex="07/09/1996",
    gAddress="777 Sunflower Drive, Oak Park, IL 60301",
    gPhoneNum="6376444647",
    gInsuranceCo="Oberbrunner LLC",
    gInsuranceNum="402850793",
    gBalance=36708.67)

guardian15 = Guardian(
    gID="4832078828",
    gLast="Frasco",
    gFirst="Deverose",
    gSSN=204854710,
    gDOB="Male",
    gSex="01/03/1957",
    gAddress="888 Iris Court, Schaumburg, IL 60173",
    gPhoneNum="8435265180",
    gInsuranceCo="Kihn, Rippin and Littel",
    gInsuranceNum="74057065",
    gBalance=65317.42)

guardian16 = Guardian(
    gID="3898341984",
    gLast="Grove",
    gFirst="Dooney",
    gSSN=171953348,
    gDOB="Male",
    gSex="11/12/1994",
    gAddress="999 Violet Street, Des Plaines, IL 60016",
    gPhoneNum="8509568818",
    gInsuranceCo="Feeney-Bergstrom",
    gInsuranceNum="645316121",
    gBalance=81570.24)

guardian17 = Guardian(
    gID="3487639351",
    gLast="Barr",
    gFirst="MacShirie",
    gSSN=419030415,
    gDOB="Male",
    gSex="09/24/1938",
    gAddress="121 Magnolia Drive, Bolingbrook, IL 60440",
    gPhoneNum="4131251880",
    gInsuranceCo="Stoltenberg, Cormier and Wolff",
    gInsuranceNum="1547266287",
    gBalance=35918.82)

guardian18 = Guardian(
    gID="1025530853",
    gLast="Cedric",
    gFirst="Corsor",
    gSSN=652313710,
    gDOB="Male",
    gSex="05/02/1975",
    gAddress="232 Jasmine Lane, Arlington Heights, IL 60004",
    gPhoneNum="7353921316",
    gInsuranceCo="Turner LLC",
    gInsuranceNum="8179605159",
    gBalance=297.79)

guardian19 = Guardian(
    gID="9030078855",
    gLast="Eberto",
    gFirst="Schechter",
    gSSN=136141503,
    gDOB="Male",
    gSex="02/01/1973",
    gAddress="343 Camellia Road, Palatine, IL 60067",
    gPhoneNum="8776366732",
    gInsuranceCo="Sanford and Sons",
    gInsuranceNum="8667908061",
    gBalance=77961.15)

guardian20 = Guardian(
    gID="3542638560",
    gLast="Gaile",
    gFirst="Phillipp",
    gSSN=120714670,
    gDOB="Male",
    gSex="1/20/1967",
    gAddress="004 Transport Place, Hoffman Estates, IL 60010",
    gPhoneNum="8492361075",
    gInsuranceCo="Hettinger Group",
    gInsuranceNum="5729813460",
    gBalance=64823.13)

guardian21 = Guardian(
    gID="3759410618",
    gLast="Keelia",
    gFirst="Thomassin",
    gSSN=868415509,
    gDOB="Female",
    gSex="10/06/1943",
    gAddress="565 Orchid Place, Skokie, IL 60076",
    gPhoneNum="4981610726",
    gInsuranceCo="King Group",
    gInsuranceNum="5163206265",
    gBalance=89931.37)

session.add_all([guardian1, guardian2, guardian3, guardian4, guardian5, guardian6, guardian7, guardian8, guardian9,
guardian10, guardian11, guardian12, guardian13, guardian14, guardian15, guardian16, guardian17, guardian18, guardian19,
guardian20, guardian21])
session.commit()


# Nurse
with Session(engine) as session:
    nurse1 = Nurse(
    nID="8141746251",
    nLast="Cawston",
    nFirst="Crichton",
    nSSN=133386325,
    nCreationDate="07/14/1993",
    nDOB="09/07/1941",
    nSex="Male",
    nAddress="789 Birch Lane, Elgin, IL 60120",
    nPhoneNum="8607907498")

nurse2 = Nurse(
    nID="0154784443",
    nLast="Van de Vlies",
    nFirst="Neddie",
    nSSN=117903132,
    nCreationDate="05/02/2016",
    nDOB="08/26/1952",
    nSex="Female",
    nAddress="456 Cedar Drive, Schaumburg, IL 60173",
    nPhoneNum="3883137131")

nurse3 = Nurse(
    nID="7312243304",
    nLast="Shillington",
    nFirst="Annice",
    nSSN=607028352,
    nCreationDate="07/21/2003",
    nDOB="05/10/1976",
    nSex="Female",
    nAddress="222 Rosewood Avenue, Champaign, IL 61820",
    nPhoneNum="3511379758")

nurse4 = Nurse(
    nID="8809364287",
    nLast="Fellis",
    nFirst="Ward",
    nSSN=402910166,
    nCreationDate="06/20/2002",
    nDOB="07/27/1968",
    nSex="Male",
    nAddress="777 Maple Road, Joliet, IL 60401",
    nPhoneNum="9866889824")

nurse5 = Nurse(
    nID="2152501608",
    nLast="Maidment",
    nFirst="Heddie",
    nSSN=184403209,
    nCreationDate="02/01/1993",
    nDOB="12/01/1963",
    nSex="Female",
    nAddress="888 Orchid Court, Springfield, IL 62701",
    nPhoneNum="8901433799")

nurse6 = Nurse(
    nID="8014003225",
    nLast="Giottini",
    nFirst="Moise",
    nSSN=613896647,
    nCreationDate="10/10/2006",
    nDOB="12/06/1977",
    nSex="Male",
    nAddress="555 Poplar Street, Rockford, IL 61101",
    nPhoneNum="6336354655")

nurse7 = Nurse(
    nID="1637468687",
    nLast="Laing",
    nFirst="Jamie",
    nSSN=287486779,
    nCreationDate="04/09/2008",
    nDOB="09/24/1972",
    nSex="Female",
    nAddress="101 Magnolia Lane, Evanston, IL 60201",
    nPhoneNum="2389388225")

nurse8 = Nurse(
    nID="1971290432",
    nLast="Micklewicz",
    nFirst="Papageno",
    nSSN=677258976,
    nCreationDate="02/15/2014",
    nDOB="05/11/1985",
    nSex="Male",
    nAddress="444 Sunflower Drive, Naperville, IL 60540",
    nPhoneNum="6283356820")

nurse9 = Nurse(
    nID="1572910909",
    nLast="Matejovsky",
    nFirst="Michelle",
    nSSN=779511883,
    nCreationDate="02/01/2013",
    nDOB="09/08/1980",
    nSex="Female",
    nAddress="123 Daisy Place, Waukegan, IL 60085",
    nPhoneNum="8818731789")

nurse10 = Nurse(
    nID="6918254634",
    nLast="Sabatini",
    nFirst="Mareah",
    nSSN=459986433,
    nCreationDate="02/28/1993",
    nDOB="11/16/1958",
    nSex="Female",
    nAddress="999 Tulip Road, Aurora, IL 60501",
    nPhoneNum="2835743718")

nurse11 = Nurse(
    nID="7521039246",
    nLast="Cass",
    nFirst="Anica",
    nSSN=540275983,
    nCreationDate="10/26/2002",
    nDOB="06/20/1958",
    nSex="Female",
    nAddress="333 Willow Lane, Bolingbrook, IL 60440",
    nPhoneNum="6073558207")

nurse12 = Nurse(
    nID="8699777841",
    nLast="Bradburn",
    nFirst="Babette",
    nSSN=607427769,
    nCreationDate="03/12/1998",
    nDOB="11/14/1950",
    nSex="Female",
    nAddress="678 Iris Avenue, Oak Park, IL 60301",
    nPhoneNum="9603362188")

nurse13 = Nurse(
    nID="8224044106",
    nLast="Prinnett",
    nFirst="Emalee",
    nSSN=721429396,
    nCreationDate="09/20/2008",
    nDOB="04/04/1948",
    nSex="Female",
    nAddress="334 Camellia Court, Palatine, IL 60067",
    nPhoneNum="4158232955")

nurse14 = Nurse(
    nID="4211715445",
    nLast="Mc Elory",
    nFirst="Gustave",
    nSSN=824611315,
    nCreationDate="06/11/2007",
    nDOB="02/10/1978",
    nSex="Male",
    nAddress="223 Violet Drive, Skokie, IL 60076",
    nPhoneNum="2021334200")

nurse15 = Nurse(
    nID="9405259113",
    nLast="Rignoldes",
    nFirst="Grayce",
    nSSN=157288048,
    nCreationDate="07/22/1984",
    nDOB="05/07/1950",
    nSex="Female",
    nAddress="1122 Camellia Road, Arlington Heights, IL 60004",
    nPhoneNum="3816987127")

nurse16 = Nurse(
    nID="0500653666",
    nLast="Fenelon",
    nFirst="Beck",
    nSSN=164482298,
    nCreationDate="02/22/2019",
    nDOB="04/13/1992",
    nSex="Male",
    nAddress="33445 Magnolia Avenue, Des Plaines, IL 60016",
    nPhoneNum="1729665919")

nurse17 = Nurse(
    nID="7863847907",
    nLast="Hanburry",
    nFirst="Cliff",
    nSSN=345999938,
    nCreationDate="03/04/1993",
    nDOB="09/03/1961",
    nSex="Male",
    nAddress="7788 Cedar Drive, Decatur, IL 62521",
    nPhoneNum="9505415342")

nurse18 = Nurse(
    nID="4518562909",
    nLast="Erickssen",
    nFirst="Brandy",
    nSSN=381784196,
    nCreationDate="03/18/1999",
    nDOB="08/24/1969",
    nSex="Male",
    nAddress="5566 Oak Road, Bloomington, IL 61701",
    nPhoneNum="4829859653")

nurse19 = Nurse(
    nID="3781706605",
    nLast="Linford",
    nFirst="Ezekiel",
    nSSN=821173956,
    nCreationDate="11/16/2000",
    nDOB="05/14/1968",
    nSex="Male",
    nAddress="4455 Pine Street, Peoria, IL 61601",
    nPhoneNum="4751147507")

nurse20 = Nurse(
    nID="7502613455",
    nLast="Jorgesen",
    nFirst="Monroe",
    nSSN=359300314,
    nCreationDate="07/24/1988",
    nDOB="04/06/1960",
    nSex="Male",
    nAddress="2233 Rose Street, Champaign, IL 61820",
    nPhoneNum="8899113136")

nurse21 = Nurse(
    nID="0437021416",
    nLast="Gosden",
    nFirst="Emmott",
    nSSN=471857430,
    nCreationDate="12/19/2002",
    nDOB="01/28/1972",
    nSex="Male",
    nAddress="11223 Birch Court, Decatur, IL 62521",
    nPhoneNum="4206977820")

nurse22 = Nurse(
    nID="9207937719",
    nLast="Shreeves",
    nFirst="Felicity",
    nSSN=663325733,
    nCreationDate="03/04/1998",
    nDOB="07/31/1971",
    nSex="Female",
    nAddress="9900 Cedar Drive, Rockford, IL 61101",
    nPhoneNum="3411034854")

nurse23 = Nurse(
    nID="2946018539",
    nLast="Yerrell",
    nFirst="Maye",
    nSSN=161494971,
    nCreationDate="09/02/2015",
    nDOB="11/23/1986",
    nSex="Female",
    nAddress="8899 Pine Lane, Aurora, IL 60501",
    nPhoneNum="2467056423")

nurse24 = Nurse(
    nID="2261402791",
    nLast="Korfmann",
    nFirst="Bartlet",
    nSSN=815043410,
    nCreationDate="12/22/1989",
    nDOB="05/28/1966",
    nSex="Male",
    nAddress="7788 Birch Road, Evanston, IL 60201",
    nPhoneNum="7972820721")

nurse25 = Nurse(
    nID="7204524675",
    nLast="Hunter",
    nFirst="Yves",
    nSSN=117358724,
    nCreationDate="05/03/1979",
    nDOB="10/03/1951",
    nSex="Male",
    nAddress="6677 Willow Lane, Joliet, IL 60401",
    nPhoneNum="5799336219")

nurse26 = Nurse(
    nID="0099317990",
    nLast="Mateiko",
    nFirst="Torr",
    nSSN=897249834,
    nCreationDate="08/05/1996",
    nDOB="09/13/1961",
    nSex="Male",
    nAddress="5566 Daisy Avenue, Naperville, IL 60540",
    nPhoneNum="5946253924")

nurse27 = Nurse(
    nID="5964724701",
    nLast="Tuison",
    nFirst="Darcy",
    nSSN=613311406,
    nCreationDate="09/25/1977",
    nDOB="08/30/1949",
    nSex="Female",
    nAddress="4455 Orchid Road, Waukegan, IL 60085",
    nPhoneNum="7883379740")

nurse28 = Nurse(
    nID="4636658116",
    nLast="Dodsworth",
    nFirst="Wainwright",
    nSSN=873563511,
    nCreationDate="03/10/2015",
    nDOB="02/09/1986",
    nSex="Male",
    nAddress="3344 Tulip Place, Springfield, IL 62701",
    nPhoneNum="2682492933")

nurse29 = Nurse(
    nID="5120574106",
    nLast="Gebbe",
    nFirst="Vaclav",
    nSSN=493266416,
    nCreationDate="08/26/2002",
    nDOB="05/26/1945",
    nSex="Male",
    nAddress="2233 Maple Drive, Schaumburg, IL 60173",
    nPhoneNum="7868083559")

nurse30 = Nurse(
    nID="0899054536",
    nLast="Woollaston",
    nFirst="Tabbie",
    nSSN=159498707,
    nCreationDate="08/06/1988",
    nDOB="06/30/1959",
    nSex="Male",
    nAddress="1122 Rosewood Lane, Champaign, IL 61820",
    nPhoneNum="7591134416")
    
session.add_all([nurse1, nurse2, nurse3, nurse4, nurse5, nurse6, nurse7, nurse8, nurse9, nurse10, nurse11, nurse12,
nurse13, nurse14, nurse15, nurse16, nurse17, nurse18, nurse19, nurse20, nurse21, nurse22, nurse23, nurse24, nurse25,
nurse26, nurse27, nurse28, nurse29, nurse30])
session.commit()


# Doctor
with Session(engine) as session:

	doctor1 = Doctor(
    	dID='2433573130',
    	dLast='Brewster',
    	dFirst='Hannie',
    	dSSN=737633372,
    	dCreationDate='01/31/1998',
    	dDOB='04/29/1955',
    	dSex='Female',
    	dAddress='5085 Brickson Park Point, Chicago, IL 60601',
   		dPhoneNum="3487007747"
	)

doctor2 = Doctor(
    dID='4772535918',
    dLast='Sherlock',
    dFirst='Malanie',
    dSSN=428365612,
    dCreationDate='04/21/2003',
    dDOB='08/13/1952',
    dSex='Female',
    dAddress='60 Portage Parkway, Springfield, IL 62701',
    dPhoneNum="1605413705"
)

doctor3 = Doctor(
    dID='1550505211',
    dLast='Woodhead',
    dFirst='Jeff',
    dSSN=375677629,
    dCreationDate='01/03/2022',
    dDOB='09/06/1965',
    dSex='Male',
    dAddress='3 Graedel Road, Peoria, IL 61601',
    dPhoneNum="9626948996"
)

doctor4 = Doctor(
    dID='1228121907',
    dLast='Wrassell',
    dFirst='Dante',
    dSSN=490999123,
    dCreationDate='04/05/2014',
    dDOB='08/23/1989',
    dSex='Intersex',
    dAddress='5 Mosinee Way, Champaign, IL 61801',
    dPhoneNum="5977596025"
)

doctor5 = Doctor(
    dID='3790986631',
    dLast='Farmery',
    dFirst='Guendolen',
    dSSN=327519163,
    dCreationDate='10/13/1999',
    dDOB='05/11/1954',
    dSex='Female',
    dAddress='9753 South Crossing, Rockford, IL 61101',
    dPhoneNum="2848412538"
)
doctor6 = Doctor(
    dID='2059515203',
    dLast='Kornacki',
    dFirst='Milena',
    dSSN=641570324,
    dCreationDate='11/07/2005',
    dDOB='04/21/1956',
    dSex='Female',
    dAddress='295 Merchant Pass, Naperville, IL 60540',
    dPhoneNum="8437345485"
)

doctor7 = Doctor(
    dID='9800443347',
    dLast='Dorot',
    dFirst='Nerti',
    dSSN=592858526,
    dCreationDate='10/30/1990',
    dDOB='11/01/1964',
    dSex='Female',
    dAddress='626 Esch Crossing, Aurora, IL 60502',
    dPhoneNum="1479412914"
)

doctor8 = Doctor(
    dID='0933876661',
    dLast='Gunson',
    dFirst='Allissa',
    dSSN=788826446,
    dCreationDate='01/29/2008',
    dDOB='09/11/1980',
    dSex='Female',
    dAddress='19 Fair Oaks Way, Elgin, IL 60120',
    dPhoneNum="3922342686"
)

doctor9 = Doctor(
    dID='9513444856',
    dLast='Mepsted',
    dFirst='Fancy',
    dSSN=379337869,
    dCreationDate='03/02/2019',
    dDOB='09/12/1994',
    dSex='Female',
    dAddress='07529 Oneill Circle, Joliet, IL 60432',
    dPhoneNum="3119915649"
)

doctor10 = Doctor(
    dID='8044068996',
    dLast='Nys',
    dFirst='Bord',
    dSSN=656026935,
    dCreationDate='08/08/2023',
    dDOB='09/19/1983',
    dSex='Male',
    dAddress='41013 Elmside Trail, Peoria, IL 61601',
    dPhoneNum="2566012680"
)

doctor11= Doctor(
    dID='7789964631',
    dLast='Coon',
    dFirst='Prince',
    dSSN=781348881,
    dCreationDate='06/03/1993',
    dDOB='09/09/1959',
    dSex='Male',
    dAddress='3964 Alpine Junction, Springfield, IL 62701',
    dPhoneNum="2647699034"
)

doctor12 = Doctor(
    dID='8399355941',
    dLast='Kropach',
    dFirst='Roseanna',
    dSSN=440115178,
    dCreationDate='04/04/1996',
    dDOB='11/15/1962',
    dSex='Female',
    dAddress='5577 Mallory Terrace, Chicago, IL 60601',
    dPhoneNum="8992722118"
)

doctor13 = Doctor(
    dID='0350061610',
    dLast='Caldroni',
    dFirst='Audi',
    dSSN=610452092,
    dCreationDate='10/06/2009',
    dDOB='10/18/1951',
    dSex='Female',
    dAddress='243 Karstens Point, Rockford, IL 61101',
    dPhoneNum="1494287933"
)

doctor14 = Doctor(
    dID='4775744720',
    dLast='Baybutt',
    dFirst='Tamarah',
    dSSN=416983572,
    dCreationDate='05/05/1997',
    dDOB='03/02/1967',
    dSex='Female',
    dAddress='7176 Utah Alley, Naperville, IL 60540',
    dPhoneNum="1043354810"
)

doctor15 = Doctor(
    dID='0292475659',
    dLast='Twigger',
    dFirst='Ernst',
    dSSN=170012972,
    dCreationDate='10/08/2014',
    dDOB='08/07/1963',
    dSex='Male',
    dAddress='04116 Cardinal Way, Aurora, IL 60502',
    dPhoneNum="1583276754"
)

doctor16 = Doctor(
    dID='5012485009',
    dLast='Bushell',
    dFirst='Geordie',
    dSSN=613020115,
    dCreationDate='08/04/2018',
    dDOB='02/25/1958',
    dSex='Male',
    dAddress='82464 Rockefeller Point, Elgin, IL 60120',
    dPhoneNum="7023269059"
)

doctor17 = Doctor(
    dID='2680882318',
    dLast='Meere',
    dFirst='Darryl',
    dSSN=644948705,
    dCreationDate='06/21/2007',
    dDOB='04/24/1961',
    dSex='Male',
    dAddress='6 Norway Maple Alley, Joliet, IL 60432',
    dPhoneNum="1913324005"
)

doctor18 = Doctor(
    dID='5255868604',
    dLast='Gasticke',
    dFirst='Westley',
    dSSN=131381367,
    dCreationDate='03/10/1981',
    dDOB='04/18/1950',
    dSex='Male',
    dAddress='8584 Vernon Way, Peoria, IL 61601',
    dPhoneNum="2612489856"
)

doctor19 = Doctor(
    dID='0279554478',
    dLast='Molan',
    dFirst='Rafe',
    dSSN=690722624,
    dCreationDate='08/22/2004',
    dDOB='08/06/1956',
    dSex='Male',
    dAddress='8 Claremont Trail, Springfield, IL 62701',
    dPhoneNum="5376546617"
)

doctor20 = Doctor(
    dID='3567879413',
    dLast='Duval',
    dFirst='Decca',
    dSSN=316904838,
    dCreationDate='02/14/2021',
    dDOB='02/14/1976',
    dSex='Male',
    dAddress='6 Mallory Street, Chicago, IL 60601',
    dPhoneNum="4011307663"
)

session.add_all([doctor1, doctor2, doctor3, doctor4, doctor5, doctor6, doctor7, doctor8, doctor9, doctor10, 
doctor11, doctor12, doctor13, doctor14, doctor15, doctor16, doctor17, doctor18, doctor19, doctor20])
session.commit()


with Session(engine) as session:
	nur_assign1 = AssignedToNur(pID="5478828149", nID="8224044106")
	nur_assign2 = AssignedToNur(pID="5478828149", nID="9207937719")
	nur_assign3 = AssignedToNur(pID="2353169554", nID="7312243304")
	nur_assign4 = AssignedToNur(pID="2353169554", nID="7502613455")
	nur_assign5 = AssignedToNur(pID="2867034035", nID="8809364287")
	nur_assign6 = AssignedToNur(pID="2867034035", nID="4636658116")
	nur_assign7 = AssignedToNur(pID="1608930009", nID="8141746251")
	nur_assign8 = AssignedToNur(pID="1608930009", nID="2946018539")
	nur_assign9 = AssignedToNur(pID="1135007012", nID="8699777841")
	nur_assign10 = AssignedToNur(pID="1135007012", nID="2946018539")
	nur_assign11 = AssignedToNur(pID="7487444848", nID="7521039246")
	nur_assign12 = AssignedToNur(pID="7487444848", nID="2261402791")
	nur_assign13 = AssignedToNur(pID="9376633717", nID="8224044106")
	nur_assign14 = AssignedToNur(pID="9376633717", nID="0437021416")
	nur_assign15 = AssignedToNur(pID="8343324366", nID="1637468687")
	nur_assign16 = AssignedToNur(pID="8343324366", nID="3781706605")
	nur_assign17 = AssignedToNur(pID="3339297274", nID="0154784443")
	nur_assign18 = AssignedToNur(pID="3339297274", nID="0500653666")
	nur_assign19 = AssignedToNur(pID="1309936374", nID="8014003225")
	nur_assign20 = AssignedToNur(pID="1309936374", nID="7863847907")
	nur_assign21 = AssignedToNur(pID="0943273102", nID="9405259113")
	nur_assign22 = AssignedToNur(pID="0943273102", nID="5120574106")
	nur_assign23 = AssignedToNur(pID="6040373601", nID="4211715445")
	nur_assign24 = AssignedToNur(pID="6040373601", nID="0500653666")
	nur_assign25 = AssignedToNur(pID="7336237347", nID="4211715445")
	nur_assign26 = AssignedToNur(pID="7336237347", nID="0500653666")
	nur_assign27 = AssignedToNur(pID="5737027589", nID="7312243304")
	nur_assign28 = AssignedToNur(pID="5737027589", nID="0899054536")
	nur_assign29 = AssignedToNur(pID="9926175422", nID="1637468687")
	nur_assign30 = AssignedToNur(pID="5548366882", nID="8141746251")
	nur_assign31 = AssignedToNur(pID="5548366882", nID="7863847907")
	nur_assign32 = AssignedToNur(pID="8652992541", nID="1971290432")
	nur_assign33 = AssignedToNur(pID="8652992541", nID="5964724701")
	nur_assign34 = AssignedToNur(pID="2439361151", nID="8224044106")
	nur_assign35 = AssignedToNur(pID="2439361151", nID="7502613455")
	nur_assign36 = AssignedToNur(pID="9575986083", nID="2152501608")
	nur_assign37 = AssignedToNur(pID="9575986083", nID="9207937719")
	nur_assign38 = AssignedToNur(pID="0934341656", nID="8224044106")
	nur_assign39 = AssignedToNur(pID="0934341656", nID="2946018539")
	nur_assign40 = AssignedToNur(pID="0184960495", nID="8014003225")
	nur_assign41 = AssignedToNur(pID="0184960495", nID="0099317990")
	nur_assign42 = AssignedToNur(pID="0219096953", nID="0154784443")
	nur_assign43 = AssignedToNur(pID="0219096953", nID="4518562909")
	nur_assign44 = AssignedToNur(pID="5348686204", nID="7312243304")
	nur_assign45 = AssignedToNur(pID="5348686204", nID="5120574106")
	nur_assign46 = AssignedToNur(pID="7092577144", nID="9405259113")
	nur_assign47 = AssignedToNur(pID="0987039997", nID="8014003225")
	nur_assign48 = AssignedToNur(pID="0987039997", nID="7502613455")
	nur_assign49 = AssignedToNur(pID="9060291182", nID="7312243304")
	nur_assign50 = AssignedToNur(pID="9060291182", nID="7204524675")
	nur_assign51 = AssignedToNur(pID="1345635524", nID="0154784443")
	nur_assign52 = AssignedToNur(pID="1345635524", nID="7863847907")
	nur_assign53 = AssignedToNur(pID="5305876737", nID="1971290432")
	nur_assign54 = AssignedToNur(pID="5305876737", nID="2946018539")
	nur_assign55 = AssignedToNur(pID="9244135949", nID="0154784443")
	nur_assign56 = AssignedToNur(pID="9244135949", nID="5120574106")
	nur_assign57 = AssignedToNur(pID="4874155030", nID="7312243304")
	nur_assign58 = AssignedToNur(pID="4874155030", nID="8014003225")
	nur_assign59 = AssignedToNur(pID="4874155030", nID="9207937719")
	nur_assign60 = AssignedToNur(pID="5246007413", nID="7502613455")
	nur_assign61 = AssignedToNur(pID="0500203431", nID="1637468687")
	nur_assign62 = AssignedToNur(pID="0500203431", nID="7863847907")
	nur_assign63 = AssignedToNur(pID="0500203431", nID="2261402791")
	nur_assign64 = AssignedToNur(pID="8594054211", nID="1971290432")
	nur_assign65 = AssignedToNur(pID="6128926959", nID="0500653666")
	nur_assign66 = AssignedToNur(pID="6128926959", nID="3781706605")
	nur_assign67 = AssignedToNur(pID="0132055368", nID="2152501608")
	nur_assign68 = AssignedToNur(pID="0132055368", nID="4518562909")
	nur_assign69 = AssignedToNur(pID="0889460949", nID="0500653666")
	nur_assign70 = AssignedToNur(pID="0889460949", nID="0437021416")
	nur_assign71 = AssignedToNur(pID="0877589380", nID="9405259113")
	nur_assign72 = AssignedToNur(pID="0877589380", nID="0899054536")
	nur_assign73 = AssignedToNur(pID="3272014055", nID="8014003225")
	nur_assign74 = AssignedToNur(pID="3272014055", nID="5964724701")
	nur_assign75 = AssignedToNur(pID="3250381608", nID="7521039246")
	nur_assign76 = AssignedToNur(pID="3250381608", nID="0437021416")
	nur_assign77 = AssignedToNur(pID="3322578003", nID="1572910909")
	nur_assign78 = AssignedToNur(pID="3322578003", nID="0899054536")
	nur_assign79 = AssignedToNur(pID="1993446753", nID="8141746251")
	nur_assign80 = AssignedToNur(pID="1993446753", nID="7502613455")
	nur_assign81 = AssignedToNur(pID="5171542287", nID="8141746251")
	nur_assign82 = AssignedToNur(pID="5171542287", nID="2261402791")
	nur_assign83 = AssignedToNur(pID="3023402353", nID="6918254634")
	nur_assign84 = AssignedToNur(pID="7140976783", nID="1572910909")
	nur_assign85 = AssignedToNur(pID="7140976783", nID="2261402791")
	nur_assign86 = AssignedToNur(pID="4647884775", nID="1572910909")
	nur_assign87 = AssignedToNur(pID="4647884775", nID="9207937719")
	nur_assign88 = AssignedToNur(pID="7662072894", nID="4211715445")
	nur_assign89 = AssignedToNur(pID="7662072894", nID="5120574106")
	nur_assign90 = AssignedToNur(pID="9055660728", nID="8699777841")
	nur_assign91 = AssignedToNur(pID="9055660728", nID="3781706605")
	nur_assign92 = AssignedToNur(pID="8113174095", nID="8809364287")
	nur_assign93 = AssignedToNur(pID="8113174095", nID="3781706605")
	nur_assign94 = AssignedToNur(pID="0792077342", nID="8809364287")
	nur_assign95 = AssignedToNur(pID="0792077342", nID="0899054536")
	nur_assign96 = AssignedToNur(pID="9517512813", nID="4211715445")
	nur_assign97 = AssignedToNur(pID="9517512813", nID="7204524675")
	

session.add_all([nur_assign1, nur_assign2, nur_assign3, nur_assign4, nur_assign5, 
                        nur_assign6, nur_assign7, nur_assign8, nur_assign9, nur_assign10, 
                        nur_assign11, nur_assign12, nur_assign13, nur_assign14, nur_assign15, 
                        nur_assign16, nur_assign17, nur_assign18, nur_assign19, nur_assign20, 
                        nur_assign21, nur_assign22, nur_assign23, nur_assign24, nur_assign25, 
                        nur_assign26, nur_assign27, nur_assign28, nur_assign29, nur_assign30, 
                        nur_assign31, nur_assign32, nur_assign33, nur_assign34, nur_assign35, 
                        nur_assign36, nur_assign37, nur_assign38, nur_assign39, nur_assign40,
                        nur_assign41, nur_assign42, nur_assign43, nur_assign44, nur_assign45, 
                        nur_assign46, nur_assign47, nur_assign48, nur_assign49, nur_assign50,
                        nur_assign51, nur_assign52, nur_assign53, nur_assign54, nur_assign55, 
                        nur_assign56, nur_assign57, nur_assign58, nur_assign59, nur_assign60,
                        nur_assign61, nur_assign62, nur_assign63, nur_assign64, nur_assign65, 
                        nur_assign66, nur_assign67, nur_assign68, nur_assign69, nur_assign70,
                        nur_assign71, nur_assign72, nur_assign73, nur_assign74, nur_assign75, 
                        nur_assign76, nur_assign77, nur_assign78, nur_assign79, nur_assign80,
                        nur_assign81, nur_assign82, nur_assign83, nur_assign84, nur_assign85, 
                        nur_assign86, nur_assign87, nur_assign88, nur_assign89, nur_assign90,
                        nur_assign91, nur_assign92, nur_assign93, nur_assign94, nur_assign95, 
                        nur_assign96, nur_assign97])
session.commit()


# AssignedToDoc
with Session(engine) as session:
	doc_assign1 = AssignedToDoc(pID="5478828149", dID="4775744720")
	doc_assign2 = AssignedToDoc(pID="2353169554", dID="2059515203")
	doc_assign3 = AssignedToDoc(pID="2867034035", dID="9513444856")
	doc_assign4 = AssignedToDoc(pID="1608930009", dID="5012485009")
	doc_assign5 = AssignedToDoc(pID="1135007012", dID="2059515203")
	doc_assign6 = AssignedToDoc(pID="7487444848", dID="0292475659")
	doc_assign7 = AssignedToDoc(pID="9376633717", dID="4772535918")
	doc_assign8 = AssignedToDoc(pID="8343324366", dID="5012485009")
	doc_assign9 = AssignedToDoc(pID="3339297274", dID="7789964631")
	doc_assign10 = AssignedToDoc(pID="1309936374", dID="3567879413")
	doc_assign11 = AssignedToDoc(pID="0943273102", dID="8044068996")
	doc_assign12 = AssignedToDoc(pID="6040373601", dID="0279554478")
	doc_assign13 = AssignedToDoc(pID="7336237347", dID="8044068996")
	doc_assign14 = AssignedToDoc(pID="5737027589", dID="1550505211")
	doc_assign15 = AssignedToDoc(pID="9926175422", dID="9800443347")
	doc_assign16 = AssignedToDoc(pID="5548366882", dID="2680882318")
	doc_assign17 = AssignedToDoc(pID="8652992541", dID="4772535918")
	doc_assign18 = AssignedToDoc(pID="2439361151", dID="3567879413")
	doc_assign19 = AssignedToDoc(pID="9575986083", dID="0933876661")
	doc_assign20 = AssignedToDoc(pID="0934341656", dID="0350061610")
	doc_assign21 = AssignedToDoc(pID="0184960495", dID="4775744720")
	doc_assign22 = AssignedToDoc(pID="0219096953", dID="3567879413")
	doc_assign23 = AssignedToDoc(pID="5348686204", dID="0350061610")
	doc_assign24 = AssignedToDoc(pID="7092577144", dID="0279554478")
	doc_assign25 = AssignedToDoc(pID="0987039997", dID="2680882318")
	doc_assign26 = AssignedToDoc(pID="9060291182", dID="7789964631")
	doc_assign27 = AssignedToDoc(pID="1345635524", dID="0933876661")
	doc_assign28 = AssignedToDoc(pID="5305876737", dID="3790986631")
	doc_assign29 = AssignedToDoc(pID="9244135949", dID="5012485009")
	doc_assign30 = AssignedToDoc(pID="4874155030", dID="8399355941")
	doc_assign31 = AssignedToDoc(pID="5246007413", dID="1228121907")
	doc_assign32 = AssignedToDoc(pID="0500203431", dID="1228121907")
	doc_assign33 = AssignedToDoc(pID="8594054211", dID="2680882318")
	doc_assign34 = AssignedToDoc(pID="6128926959", dID="0292475659")
	doc_assign35 = AssignedToDoc(pID="0132055368", dID="4772535918")
	doc_assign36 = AssignedToDoc(pID="0889460949", dID="7789964631")
	doc_assign37 = AssignedToDoc(pID="0877589380", dID="2433573130")
	doc_assign38 = AssignedToDoc(pID="3272014055", dID="1550505211")
	doc_assign39 = AssignedToDoc(pID="3250381608", dID="9513444856")
	doc_assign40 = AssignedToDoc(pID="3322578003", dID="0350061610")
	doc_assign41 = AssignedToDoc(pID="1993446753", dID="2059515203")
	doc_assign42 = AssignedToDoc(pID="5171542287", dID="8044068996")
	doc_assign43 = AssignedToDoc(pID="3023402353", dID="5255868604")
	doc_assign44 = AssignedToDoc(pID="7140976783", dID="9800443347")
	doc_assign45 = AssignedToDoc(pID="4647884775", dID="1228121907")
	doc_assign46 = AssignedToDoc(pID="7662072894", dID="2433573130")
	doc_assign47 = AssignedToDoc(pID="9055660728", dID="9513444856")
	doc_assign48 = AssignedToDoc(pID="8113174095", dID="0292475659")
	doc_assign49 = AssignedToDoc(pID="0792077342", dID="0279554478")
	doc_assign50 = AssignedToDoc(pID="9517512813", dID="4775744720")

session.add_all([doc_assign1, doc_assign2, doc_assign3, doc_assign4, doc_assign5,
                        doc_assign6, doc_assign7, doc_assign8, doc_assign9, doc_assign10,
                        doc_assign11, doc_assign12, doc_assign13, doc_assign14, doc_assign15,
                        doc_assign16, doc_assign17, doc_assign18, doc_assign19, doc_assign20,
                        doc_assign21, doc_assign22, doc_assign23, doc_assign24, doc_assign25,
                        doc_assign26, doc_assign27, doc_assign28, doc_assign29, doc_assign30,
                        doc_assign31, doc_assign32, doc_assign33, doc_assign34, doc_assign35,
                        doc_assign36, doc_assign37, doc_assign38, doc_assign39, doc_assign40,
                        doc_assign41, doc_assign42, doc_assign43, doc_assign44, doc_assign45,
                        doc_assign46, doc_assign47, doc_assign48, doc_assign49, doc_assign50])
session.commit()
	

# DependentOf
with Session(engine) as session:
	dependentOf1 = DependentOf(pID='5478828149', gID='8520489390')
	dependentOf2 = DependentOf(pID='2353169554', gID='7251298740')
	dependentOf3 = DependentOf(pID='2867034035', gID='6445290620')
	dependentOf4 = DependentOf(pID='1608930009', gID='7483012498')
	dependentOf5 = DependentOf(pID='1135007012', gID='3285231780')
	dependentOf6 = DependentOf(pID='7487444848', gID='2443645274')
	dependentOf7 = DependentOf(pID='9376633717', gID='2294796667')
	dependentOf8 = DependentOf(pID='8343324366', gID='6088659734')
	dependentOf9 = DependentOf(pID='3339297274', gID='9387481093')
	dependentOf10 = DependentOf(pID='1309936374', gID='5948730290')
	dependentOf11 = DependentOf(pID='0943273102', gID='3780291827')
	dependentOf12 = DependentOf(pID='6040373601', gID='2299841340')
	dependentOf13 = DependentOf(pID='7336237347', gID='3008909523')
	dependentOf14 = DependentOf(pID='5737027589', gID='1742238351')
	dependentOf15 = DependentOf(pID='9926175422', gID='4832078828')
	dependentOf16 = DependentOf(pID='5548366882', gID='3898341984')
	dependentOf17 = DependentOf(pID='8652992541', gID='3487639351')
	dependentOf18 = DependentOf(pID='2439361151', gID='1025530853')
	dependentOf19 = DependentOf(pID='9575986083', gID='9030078855')
	dependentOf20 = DependentOf(pID='0934341656', gID='3542638560')
	dependentOf21 = DependentOf(pID='0184960495', gID='3759410618')
	dependentOf22 = DependentOf(pID='0219096953', gID='8520489390')
	dependentOf23 = DependentOf(pID='5348686204', gID='7251298740')
	dependentOf24 = DependentOf(pID='7092577144', gID='6445290620')
	dependentOf25 = DependentOf(pID='0987039997', gID='7483012498')
	dependentOf26 = DependentOf(pID='9060291182', gID='3285231780')
	dependentOf27 = DependentOf(pID='1345635524', gID='2443645274')
	dependentOf28 = DependentOf(pID='5305876737', gID='2294796667')
	dependentOf29 = DependentOf(pID='9244135949', gID='6088659734')
	dependentOf30 = DependentOf(pID='4874155030', gID='9387481093')
	dependentOf31 = DependentOf(pID='5246007413', gID='5948730290')
	dependentOf32 = DependentOf(pID='0500203431', gID='2299841340')
	dependentOf33 = DependentOf(pID='8594054211', gID='3008909523')
	dependentOf34 = DependentOf(pID='6128926959', gID='1742238351')
	dependentOf35 = DependentOf(pID='0132055368', gID='3759410618')
	dependentOf36 = DependentOf(pID='0889460949', gID='8520489390')
	dependentOf37 = DependentOf(pID='0877589380', gID='7251298740')
	dependentOf38 = DependentOf(pID='3272014055', gID='6088659734')
	dependentOf39 = DependentOf(pID='3250381608', gID='2294796667')
	dependentOf40 = DependentOf(pID='3322578003', gID='3285231780')
	dependentOf41 = DependentOf(pID='1993446753', gID='3008909523')
	dependentOf42 = DependentOf(pID='5171542287', gID='3542638560')
	dependentOf43 = DependentOf(pID='3023402353', gID='3780291827')
	dependentOf44 = DependentOf(pID='7140976783', gID='3487639351')
	dependentOf45 = DependentOf(pID='4647884775', gID='6088659734')
	dependentOf46 = DependentOf(pID='7662072894', gID='3285231780')
	dependentOf47 = DependentOf(pID='9055660728', gID='2294796667')
	dependentOf48 = DependentOf(pID='8113174095', gID='3008909523')
	dependentOf49 = DependentOf(pID='0792077342', gID='6445290620')
	dependentOf50 = DependentOf(pID='9517512813', gID='1742238351')


	

session.add_all([dependentOf1, dependentOf2, dependentOf3, dependentOf4, dependentOf5,
                     dependentOf6, dependentOf7, dependentOf8, dependentOf9, dependentOf10,
                     dependentOf11, dependentOf12, dependentOf13, dependentOf14, dependentOf15,
                     dependentOf16, dependentOf17, dependentOf18, dependentOf19, dependentOf20,
                     dependentOf21, dependentOf22, dependentOf23, dependentOf24, dependentOf25,
                     dependentOf26, dependentOf27, dependentOf28, dependentOf29, dependentOf30,
                     dependentOf31, dependentOf32, dependentOf33, dependentOf34, dependentOf35,
                     dependentOf36, dependentOf37, dependentOf38, dependentOf39, dependentOf40,
                     dependentOf41, dependentOf42, dependentOf43, dependentOf44, dependentOf45,
                     dependentOf46, dependentOf47, dependentOf48, dependentOf49, dependentOf50])
session.commit()


# Simple Queries
session = Session(engine)

print("\n--------------------")
print("\n## Query 1 (Pragya) ##\n")

result = (
    session.query(Patient)
    .join(DependentOf, Patient.pID == DependentOf.pID)
    .join(Guardian, DependentOf.gID == Guardian.gID)
    .filter(Patient.pIllness == 'Pneumonia')
    .order_by(Patient.pFirst, Patient.pLast)
    .all()
)

if not result:
    print("No patients with Pneumonia found.")
else:
    for patient in result:
        print(
            f"pID: {patient.pID}\n"
            f"First Name: {patient.pFirst}\n"
            f"Last Name: {patient.pLast}\n"
            f"Illness: {patient.pIllness}\n"
            f"Patient Address: {patient.pAddress}\n\n"
        )

print("--------------------")
print("\n## Query 2 (Arub) ##\n")

print("\n--------------------")
print("\n## Query 3 (Rihab) ##\n")
result = (
    session.query(Doctor.dFirst, Doctor.dLast, func.count(AssignedToDoc.pID).label('numFemalePatients'))
    .join(AssignedToDoc, Doctor.dID == AssignedToDoc.dID)
    .join(Patient, AssignedToDoc.pID == Patient.pID)
    .filter(Patient.pSex == 'Female')
    .group_by(Doctor.dFirst, Doctor.dLast)
    .having(func.count(AssignedToDoc.pID) >= 1)
    .order_by('numFemalePatients')
    .all()
)
for doctor in result:
    print(f"Last Name: {doctor.dLast}\n"
    f"First Name: {doctor.dFirst}\n"
    f"Number of Female Patients: {doctor.numFemalePatients}\n"
    f"\n")

    
print("\n--------------------")
print("\n## Query 4 (Kayla) ##\n")
result = (
    session.query(Nurse.nID, Nurse.nLast, Nurse.nFirst, Nurse.nSex, func.count(AssignedToNur.pID).label("numPatients"))
    .filter(Nurse.nSex == "Female")
    .join(AssignedToNur, Nurse.nID == AssignedToNur.nID)
    .group_by(Nurse.nID)
    .having(func.count(AssignedToNur.pID) <= 3)
    .order_by(Nurse.nLast)
    .all()
)
print("List of nurses and the number of patients they have:\n")
for nurse in result:
    print(
        f"nID: {nurse.nID}\n"
        f"Last Name: {nurse.nLast}\n"
        f"First Name: {nurse.nFirst}\n"
        f"Sex: {nurse.nSex}\n"
        f"Number of Patients: {nurse.numPatients}\n\n"
    )
print("--------------------")



