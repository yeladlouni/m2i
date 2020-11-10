employees = [
    '200;Jennifer;Whalen;JWHALEN;515.123.4444;17/09/03;AD_ASST;4400;;101;10',
    '201;Michael;Hartstein;MHARTSTE;515.123.5555;17/02/04;MK_MAN;13000;;100;20',
    '202;Pat;Fay;PFAY;603.123.6666;17/08/05;MK_REP;6000;;201;20',
    '114;Den;Raphaely;DRAPHEAL;515.127.4561;07/12/02;PU_MAN;11000;;100;30',
    '115;Alexander;Khoo;AKHOO;515.127.4562;18/05/03;PU_CLERK;3100;;114;30',
    '116;Shelli;Baida;SBAIDA;515.127.4563;24/12/05;PU_CLERK;2900;;114;30',
    '117;Sigal;Tobias;STOBIAS;515.127.4564;24/07/05;PU_CLERK;2800;;114;30',
    '118;Guy;Himuro;GHIMURO;515.127.4565;15/11/06;PU_CLERK;2600;;114;30',
    '119;Karen;Colmenares;KCOLMENA;515.127.4566;10/08/07;PU_CLERK;2500;;114;30',
    '203;Susan;Mavris;SMAVRIS;515.123.7777;07/06/02;HR_REP;6500;;101;40',
    '120;Matthew;Weiss;MWEISS;650.123.1234;18/07/04;ST_MAN;8000;;100;50',
    '121;Adam;Fripp;AFRIPP;650.123.2234;10/04/05;ST_MAN;8200;;100;50',
    '122;Payam;Kaufling;PKAUFLIN;650.123.3234;01/05/03;ST_MAN;7900;;100;50',
    '123;Shanta;Vollman;SVOLLMAN;650.123.4234;10/10/05;ST_MAN;6500;;100;50',
    '124;Kevin;Mourgos;KMOURGOS;650.123.5234;16/11/07;ST_MAN;5800;;100;50',
    '125;Julia;Nayer;JNAYER;650.124.1214;16/07/05;ST_CLERK;3200;;120;50',
    '126;Irene;Mikkilineni;IMIKKILI;650.124.1224;28/09/06;ST_CLERK;2700;;120;50',
    '127;James;Landry;JLANDRY;650.124.1334;14/01/07;ST_CLERK;2400;;120;50',
    '128;Steven;Markle;SMARKLE;650.124.1434;08/03/08;ST_CLERK;2200;;120;50',
    '129;Laura;Bissot;LBISSOT;650.124.5234;20/08/05;ST_CLERK;3300;;121;50',
    '130;Mozhe;Atkinson;MATKINSO;650.124.6234;30/10/05;ST_CLERK;2800;;121;50',
    '131;James;Marlow;JAMRLOW;650.124.7234;16/02/05;ST_CLERK;2500;;121;50',
    '132;TJ;Olson;TJOLSON;650.124.8234;10/04/07;ST_CLERK;2100;;121;50',
    '133;Jason;Mallin;JMALLIN;650.127.1934;14/06/04;ST_CLERK;3300;;122;50',
    '134;Michael;Rogers;MROGERS;650.127.1834;26/08/06;ST_CLERK;2900;;122;50',
    '135;Ki;Gee;KGEE;650.127.1734;12/12/07;ST_CLERK;2400;;122;50',
    '136;Hazel;Philtanker;HPHILTAN;650.127.1634;06/02/08;ST_CLERK;2200;;122;50',
    '137;Renske;Ladwig;RLADWIG;650.121.1234;14/07/03;ST_CLERK;3600;;123;50',
    '138;Stephen;Stiles;SSTILES;650.121.2034;26/10/05;ST_CLERK;3200;;123;50',
    '139;John;Seo;JSEO;650.121.2019;12/02/06;ST_CLERK;2700;;123;50',
    '140;Joshua;Patel;JPATEL;650.121.1834;06/04/06;ST_CLERK;2500;;123;50',
    '141;Trenna;Rajs;TRAJS;650.121.8009;17/10/03;ST_CLERK;3500;;124;50',
    '142;Curtis;Davies;CDAVIES;650.121.2994;29/01/05;ST_CLERK;3100;;124;50',
    '143;Randall;Matos;RMATOS;650.121.2874;15/03/06;ST_CLERK;2600;;124;50',
    '144;Peter;Vargas;PVARGAS;650.121.2004;09/07/06;ST_CLERK;2500;;124;50',
    '180;Winston;Taylor;WTAYLOR;650.507.9876;24/01/06;SH_CLERK;3200;;120;50',
    '181;Jean;Fleaur;JFLEAUR;650.507.9877;23/02/06;SH_CLERK;3100;;120;50',
    '182;Martha;Sullivan;MSULLIVA;650.507.9878;21/06/07;SH_CLERK;2500;;120;50',
    '183;Girard;Geoni;GGEONI;650.507.9879;03/02/08;SH_CLERK;2800;;120;50',
    '184;Nandita;Sarchand;NSARCHAN;650.509.1876;27/01/04;SH_CLERK;4200;;121;50',
    '185;Alexis;Bull;ABULL;650.509.2876;20/02/05;SH_CLERK;4100;;121;50',
    '186;Julia;Dellinger;JDELLING;650.509.3876;24/06/06;SH_CLERK;3400;;121;50',
    '187;Anthony;Cabrio;ACABRIO;650.509.4876;07/02/07;SH_CLERK;3000;;121;50',
    '188;Kelly;Chung;KCHUNG;650.505.1876;14/06/05;SH_CLERK;3800;;122;50',
    '189;Jennifer;Dilly;JDILLY;650.505.2876;13/08/05;SH_CLERK;3600;;122;50',
    '190;Timothy;Gates;TGATES;650.505.3876;11/07/06;SH_CLERK;2900;;122;50',
    '191;Randall;Perkins;RPERKINS;650.505.4876;19/12/07;SH_CLERK;2500;;122;50',
    '192;Sarah;Bell;SBELL;650.501.1876;04/02/04;SH_CLERK;4000;;123;50',
    '193;Britney;Everett;BEVERETT;650.501.2876;03/03/05;SH_CLERK;3900;;123;50',
    '194;Samuel;McCain;SMCCAIN;650.501.3876;01/07/06;SH_CLERK;3200;;123;50',
    '195;Vance;Jones;VJONES;650.501.4876;17/03/07;SH_CLERK;2800;;123;50',
    '196;Alana;Walsh;AWALSH;650.507.9811;24/04/06;SH_CLERK;3100;;124;50',
    '197;Kevin;Feeney;KFEENEY;650.507.9822;23/05/06;SH_CLERK;3000;;124;50',
    '198;Donald;OConnell;DOCONNEL;650.507.9833;21/06/07;SH_CLERK;2600;;124;50',
    '199;Douglas;Grant;DGRANT;650.507.9844;13/01/08;SH_CLERK;2600;;124;50',
    '103;Alexander;Hunold;AHUNOLD;590.423.4567;03/01/06;IT_PROG;9000;;102;60',
    '104;Bruce;Ernst;BERNST;590.423.4568;21/05/07;IT_PROG;6000;;103;60',
    '105;David;Austin;DAUSTIN;590.423.4569;25/06/05;IT_PROG;4800;;103;60',
    '106;Valli;Pataballa;VPATABAL;590.423.4560;05/02/06;IT_PROG;4800;;103;60',
    '107;Diana;Lorentz;DLORENTZ;590.423.5567;07/02/07;IT_PROG;4200;;103;60',
    '204;Hermann;Baer;HBAER;515.123.8888;07/06/02;PR_REP;10000;;101;70',
    '145;John;Russell;JRUSSEL;011.44.1344.429268;01/10/04;SA_MAN;14000;0,4;100;80',
    '146;Karen;Partners;KPARTNER;011.44.1344.467268;05/01/05;SA_MAN;13500;0,3;100;80',
    '147;Alberto;Errazuriz;AERRAZUR;011.44.1344.429278;10/03/05;SA_MAN;12000;0,3;100;80',
    '148;Gerald;Cambrault;GCAMBRAU;011.44.1344.619268;15/10/07;SA_MAN;11000;0,3;100;80',
    '149;Eleni;Zlotkey;EZLOTKEY;011.44.1344.429018;29/01/08;SA_MAN;10500;0,2;100;80',
    '150;Peter;Tucker;PTUCKER;011.44.1344.129268;30/01/05;SA_REP;10000;0,3;145;80',
    '151;David;Bernstein;DBERNSTE;011.44.1344.345268;24/03/05;SA_REP;9500;0,25;145;80',
    '152;Peter;Hall;PHALL;011.44.1344.478968;20/08/05;SA_REP;9000;0,25;145;80',
    '153;Christopher;Olsen;COLSEN;011.44.1344.498718;30/03/06;SA_REP;8000;0,2;145;80',
    '154;Nanette;Cambrault;NCAMBRAU;011.44.1344.987668;09/12/06;SA_REP;7500;0,2;145;80',
    '155;Oliver;Tuvault;OTUVAULT;011.44.1344.486508;23/11/07;SA_REP;7000;0,15;145;80',
    '156;Janette;King;JKING;011.44.1345.429268;30/01/04;SA_REP;10000;0,35;146;80',
    '157;Patrick;Sully;PSULLY;011.44.1345.929268;04/03/04;SA_REP;9500;0,35;146;80',
    '158;Allan;McEwen;AMCEWEN;011.44.1345.829268;01/08/04;SA_REP;9000;0,35;146;80',
    '159;Lindsey;Smith;LSMITH;011.44.1345.729268;10/03/05;SA_REP;8000;0,3;146;80',
    '160;Louise;Doran;LDORAN;011.44.1345.629268;15/12/05;SA_REP;7500;0,3;146;80',
    '161;Sarath;Sewall;SSEWALL;011.44.1345.529268;03/11/06;SA_REP;7000;0,25;146;80',
    '162;Clara;Vishney;CVISHNEY;011.44.1346.129268;11/11/05;SA_REP;10500;0,25;147;80',
    '163;Danielle;Greene;DGREENE;011.44.1346.229268;19/03/07;SA_REP;9500;0,15;147;80',
    '164;Mattea;Marvins;MMARVINS;011.44.1346.329268;24/01/08;SA_REP;7200;0,1;147;80',
    '165;David;Lee;DLEE;011.44.1346.529268;23/02/08;SA_REP;6800;0,1;147;80',
    '166;Sundar;Ande;SANDE;011.44.1346.629268;24/03/08;SA_REP;6400;0,1;147;80',
    '167;Amit;Banda;ABANDA;011.44.1346.729268;21/04/08;SA_REP;6200;0,1;147;80',
    '168;Lisa;Ozer;LOZER;011.44.1343.929268;11/03/05;SA_REP;11500;0,25;148;80',
    '169;Harrison;Bloom;HBLOOM;011.44.1343.829268;23/03/06;SA_REP;10000;0,2;148;80',
    '170;Tayler;Fox;TFOX;011.44.1343.729268;24/01/06;SA_REP;9600;0,2;148;80',
    '171;William;Smith;WSMITH;011.44.1343.629268;23/02/07;SA_REP;7400;0,15;148;80',
    '172;Elizabeth;Bates;EBATES;011.44.1343.529268;24/03/07;SA_REP;7300;0,15;148;80',
    '173;Sundita;Kumar;SKUMAR;011.44.1343.329268;21/04/08;SA_REP;6100;0,1;148;80',
    '174;Ellen;Abel;EABEL;011.44.1644.429267;11/05/04;SA_REP;11000;0,3;149;80',
    '175;Alyssa;Hutton;AHUTTON;011.44.1644.429266;19/03/05;SA_REP;8800;0,25;149;80',
    '176;Jonathon;Taylor;JTAYLOR;011.44.1644.429265;24/03/06;SA_REP;8600;0,2;149;80',
    '177;Jack;Livingston;JLIVINGS;011.44.1644.429264;23/04/06;SA_REP;8400;0,2;149;80',
    '179;Charles;Johnson;CJOHNSON;011.44.1644.429262;04/01/08;SA_REP;6200;0,1;149;80',
    '100;Steven;King;SKING;515.123.4567;17/06/03;AD_PRES;24000;;;90',
    '101;Neena;Kochhar;NKOCHHAR;515.123.4568;21/09/05;AD_VP;17000;;100;90',
    '102;Lex;De Haan;LDEHAAN;515.123.4569;13/01/01;AD_VP;17000;;100;90',
    '108;Nancy;Greenberg;NGREENBE;515.124.4569;17/08/02;FI_MGR;12008;;101;100',
    '109;Daniel;Faviet;DFAVIET;515.124.4169;16/08/02;FI_ACCOUNT;9000;;108;100',
    '110;John;Chen;JCHEN;515.124.4269;28/09/05;FI_ACCOUNT;8200;;108;100',
    '111;Ismael;Sciarra;ISCIARRA;515.124.4369;30/09/05;FI_ACCOUNT;7700;;108;100',
    '112;Jose Manuel;Urman;JMURMAN;515.124.4469;07/03/06;FI_ACCOUNT;7800;;108;100',
    '113;Luis;Popp;LPOPP;515.124.4567;07/12/07;FI_ACCOUNT;6900;;108;100',
    '205;Shelley;Higgins;SHIGGINS;515.123.8080;07/06/02;AC_MGR;12008;;101;110',
    '206;William;Gietz;WGIETZ;515.123.8181;07/06/02;AC_ACCOUNT;8300;;205;110',
    '178;Kimberely;Grant;KGRANT;011.44.1644.429263;24/05/07;SA_REP;7000;0,15;149;'
]

departments = [
    '10;Administration;200;1700',
    '20;Marketing;201;1800',
    '30;Purchasing;114;1700',
    '40;Human Resources;203;2400',
    '50;Shipping;121;1500',
    '60;IT;103;1400',
    '70;Public Relations;204;2700',
    '80;Sales;145;2500',
    '90;Executive;100;1700',
    '100;Finance;108;1700',
    '110;Accounting;205;1700',
    '120;Treasury;;1700',
    '130;Corporate Tax;;1700',
    '140;Control And Credit;;1700',
    '150;Shareholder Services;;1700',
    '160;Benefits;;1700',
    '170;Manufacturing;;1700',
    '180;Construction;;1700',
    '190;Contracting;;1700',
    '200;Operations;;1700',
    '210;IT Support;;1700',
    '220;NOC;;1700',
    '230;IT Helpdesk;;1700',
    '240;Government Sales;;1700',
    '250;Retail Sales;;1700',
    '260;Recruiting;;1700',
    '270;Payroll;;1700'
]


# Renvoyer la liste des employés dont le job_id est 'SA_REP'
# Solution en utilisant les listes de compréhensions ==> One-liner

sales_representatives = [employee.split(';')[1] + ' ' + employee.split(';')[2] for employee in employees
                         if employee.split(';')[6] == 'SA_REP']

print(sales_representatives)

# Convertir la liste des employés en une liste de dictionnaires avec les différentes informations de l'employé

employees_list = [{'EMPLOYEE_ID': e.split(';')[0], 'FIRST_NAME': e.split(';')[1], 'LAST_NAME': e.split(';')[2],
                   'EMAIL': e.split(';')[3], 'PHONE_NUMBER': e.split(';')[4], 'HIRE_DATE': e.split(';')[5],
                   'JOB_ID': e.split(';')[6], 'SALARY': float(e.split(';')[7]), 'COMMISSION_PCT': e.split(';')[8],
                   'MANAGER_ID': e.split(';')[9], 'DEPARTMENT_ID': e.split(';')[10]} for e in employees]

print(employees_list)

# Total des salaires

total_salaries = sum([e['SALARY'] for e in employees_list])

print(f"Le total des salaires est: {total_salaries}")

# Afin de retirer les doublons depuis une liste, on peut la convertir vers un ensemble "set"

duplicated_list = ['Audi', 'Merceded', 'Audi', 'Audi']

print(set(duplicated_list))

# Afficher le total des salaires par département sous forme d'une liste de dictionnaires

# Vanilla python : pure python ==> sans utiliser aucun package (pandas, itertools....)

department_names = {int(d.split(';')[0]):d.split(';')[1] for d in departments}

salaries_per_department = {}

for e in employees_list:
    if e['DEPARTMENT_ID'] != '':
        department_id = int(e['DEPARTMENT_ID'])
        department_name = department_names[department_id]
    else:
        department_name = 'NA'

    salaries_per_department[department_name] = salaries_per_department.get(department_name, 0) + e['SALARY']
    print(salaries_per_department)

print(salaries_per_department)



