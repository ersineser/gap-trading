import datetime

BASE_URL = "https://paper-api.alpaca.markets"
API_KEY = ""
SECRET_KEY = ""

QQQ_SYMBOLS = [
    'AMD','ADBE','ABNB','ALGN','AMZN','AMGN','AEP','ADI','ANSS','AAPL','AMAT','ASML','TEAM','ADSK','ATVI','ADP','AZN','AVGO','BIDU','BIIB','BMRN','BKNG','CDNS','CHTR','CPRT','CRWD','CTAS','CSCO','CMCSA','COST','CSX','CTSH','DDOG','DOCU',
    'DXCM','DLTR','EA','EBAY','EXC','FAST','FB','FISV','FTNT','GILD','GOOG','GOOGL','HON','ILMN','INTC','INTU','ISRG','MRVL','IDXX','JD','KDP','KLAC','KHC','LRCX','LCID','LULU','MELI','MAR','MTCH','MCHP','MDLZ','MRNA','MNST','MSFT',
    'MU','NFLX','NTES','NVDA','NXPI','OKTA','ODFL','ORLY','PCAR','PANW','PAYX','PDD','PYPL','PEP','QCOM','REGN','ROST','SIRI','SGEN','SPLK','SWKS','SBUX','SNPS','TSLA','TXN','TMUS','VRSN','VRSK','VRTX','WBA','WDAY','XEL','ZM','ZS'
]

IWM_SYMBOLS = [
    'OVV','CAR','AR','AMC','CHK','BJ','THC','EGP','SWN','TTEK','WSC','M','PFGC','RRC','KBR','PDCE','STAG','LSCC','SWAV','INSP','IIVI','GTLS','SYNA','MTDR','RPD','MUR','SSB','EME','ASGN','IRT','SGMS','TXRH','HALO','SAIL','BHVN','SWX','HQY','WCC','EXPO','XTSLA','TRNO','TENB','MUSA','FFIN','SAIA','CMC','NSA','VRNS','GBCI','RHP','OMCL','CHX','AQUA','ROLL','SIGI','VLY','ROG','CCMP','VG','SLAB','LHCG','BKH','HP','AMN','HELE','BIPC','ADC','POWI','QLYS','KNSL','IRDM','TGNA',
    'MIME','BXMT','ITCI','KRG','POR','EXLS','SM','SSD','CADE','OPCH','ESNT','WK','ONB','NOVT','OGS','MMS','ARWR','UBSI','ALKS','LIVN','SPSC','UFPI','CROX','MEDP','NJR','RLI','ENV','ENSG','CNX','BOX','MSTR','HLI','HWC','SFBS','AVNT','CNMD','CWST','ATKR','BCPC','ZD','HGV','SIG','UMBF','TRTN','FLR','LTHM','ZWS','GATX','IIPR','LNTH','IRTC','PNM','PECO','APLS','SMTC','APG','RDN','OUT','HR','NTLA','SR','MATX','TNET','FOXF','ORA','BPMC','CBT','HRI','APLE','DOC','SAFM','GT','WD',
    'AIT','BL','CARG','ATI','SMPL','ABG','DEN','FELE','FUL','MGY','NSP','WTS','SEAS','BKU','CRC','LXP','CBU','FN','INDB','SI','SFM','EBC','DBRG','KFY','HL','MP','PRFT','EYE','NSIT','SXT','PCH','VRNT','HOMB','MMSI','BNL','SJI','JBT','PZZA','ONTO','SUM','VIAV','SHOO','REZI','PTEN','APPS','BECN','ACIW','ABM','ETRN','ADNT','ALE','WHD','AEL','PSB','ASB','SONO','BE','MXL','TMHC','DIOD','SPT','HASI','KOS','NWE','PCRX','TWNK','AMBA','PEB','CATY','PPBI','ASO','WLL','UCBI','CVBF',
    'WING','RCM','SFNC','OFC','NARI','ESGR','QTWO','EPRT','AVA','BCO','NEOG','FIBK','KLIC','AJRD','FIX','MLI','ARVN','CNO','TRUP','CELH','AWR','WBT','HI','MTH','STAA','NUVA','MAC','OMI','SITM','PTCT','FCFS','FHI','CYTK','FATE','MGEE','INSM','TCBI','BCC','LANC','EQC','AXNX','OAS','ENS','AEIS','KRTX','CBRL','GPI','MC','CPE','RMBS','FORM','SITC','CVLT','CWT','BOOT','ARNC','AUB','ALRM','HAE','PDCO','SBRA','KW','SKY','ABCB','PBF','MAXR','COOP','BLKB','CCOI','PGNY','CWEN','BRBR',
    'FOCS','GKOS','ITGR','BTU','REGI','MDRX','ALTR','WSFS','CIVI','LCII','DY','IBTX','KBH','PD','ACA','ATRC','VC','AEO','SEM','PBH','UNIT','NAVI','FULT','ELY','MTSI','CWK','SHO','FBP','WDFC','UNF','AIN','OTTR','DOCN','ACAD','HLNE','NVRO','MOGA','DNLI','GLNG','RRR','UNFI','BMI','NGVT','DORM','FWRD','YELP','SANM','TEX','ALGT','EPAY','SAVE','ABR','UPWK','MLKN','EVTC','ARCH','IGT','COLB','TRN','SHAK','VSH','MTOR','CIM','GHC','RAMP','AX','MNTV','NUS','EVH','NHI','FRME','ASAN',
    'HLIO','DAN','AIMC','KMT','WLY','CPK','ROIC','RLJ','KTOS','AVAV','THRM','IBOC','JJSF','WERN','IOSP','NTCT','FCPT','TROX','COKE','TWST','CVCO','CMP','TPH','PRMW','VRRM','BEAM','KWR','APAM','CALM','OCDX','UE','NMRK','ITRI','IHRT','MANT','BDC','PLXS','KAI','KTB','XHR','CSTM','USD','AAON','CALX','WIRE','BDN','MED','PRGS','MDC','WRE','FOLD','TELL','WAFD','GMS','CNS','BRC','PLAY','CNNE','PIPR','GBT','MTX','WSBC','APPF','SCL','DRH','MSGE','APPN','HUBG','MGRC',
    'PDM','FBC','CSGS','CBZ','ODP','OM','KAR','FFBC','ENR','VSTO','GCP','RUSHA','CRS','VRTV','FSS','ANF','OI','RLAY','MARA','NPO','LGIH','CORT','AAWW','TOWN','EBS','AMKR','SASR','EPC','SMCI','SPXC','TSE','MWA','EAF','FSR','RVLV','NXRT','PSMT','HTLF','TTGT','JELD','SGRY','BLMN','HCC','IBP','PGRE','NEX','FCEL','PRAA','JOE','ATSG','JACK','ACLS','SSTK','TDS','GNW','TBK','ARI','LKFN','AKR','IDCC','SBCF','TRMK','CNK','VGR','WOR','WWW','HOPE','MYGN','WGO','ISEE','DOOR',
    'ARCB','BCRX','NG','RNST','SKT','HTH','NKLA','ICFI','AAT','URBN','BGS','BANR','MD','STRA','NTB','TVTX','THS','DDD','PRK','EGBN','ANDE','INT','FOE','IRWD','SBH','PING','DEA','MTRN','GTN','AIR','AMRC','VBTX','FLYW','CENTA','SJW','XPER','VCEL','B','RCII','NOG','TGH','CAKE','PFS','KN','LILAK','CDNA','MEI','SPWR','NVEE','TWO','HMN','NMIH','CVET','POLY','EFSC','ESE','TGI','DK','OSTK','CSWI','CXW','EVRI','EAT','DDS','NOVA','COUR','LPSN','ALEX','CTRE','LNN','GEF','CEIX','BBBY',
    'CDEV','PRG','LPRO','MSEX','MFA','VCYT','LOB','AMEH','KALU','NWBI','LBRT','ETWO','RIOT','HNI','CCS','CRK','SILK','NWN','CDLX','LGFB','CLDX','GNL','MNRO','GDOT','RLGY','UCTT','WABC','PJT','VRTS','ZUO','LGND','CRVL','MPLN','SCHN','AVNS','RDFN','NBTB','SLCA','OII','ECOL','OXM','UEC','SKYW','MGNI','BANF','XNCR','ATGE','IPAR','EXTR','CASH','MYRG','TTEC','KFRC','PFSI','ECPG','GVA','SVC','UUUU','ASIX','TTMI','SWTX','CUBI','PLUS','PLMR','TPTX','KRYS','MODV','NNI','VRE','LRN','GOLF',
    'ENVA','AMPH','RVMD','PRIM','PMT','PACB','FBK','ENTA','SUPN','ANAT','INFN','LTC','LC','FBNC','CSR','TVTY','PUMP','GBX','UVV','STC','IRBT','AGIO','TRS','CYH','ADUS','VIR','CFFN','PATK','RCUS','MEG','IMKTA','FROG','SYBT','TBBK','VICR','LADR','NBR','PRA','ALG','PHR','FCF','DOMO','ILPT','WMK','TNC','NEO','USPH','BKD','HSKA','OSIS','ROCK','SDGR','CNR','CENX','HEES','OFG','GIII','GOGO','AROC','SFL','SKIN','CERE','MGPI','SAFT','CRNC','BUSE','PRLB','AVID','LAND','ARGO','APTS','STEP',
    'CDE','OPK','STAR','ESRT','SPTN','COHU','KYMR','MHO','BHLB','RPAY','DRQ','DNOW','DCOM','EPAC','RILY','PRTA','CYRX','SNEX','DLX','EGHT','SBSI','HCSG','RGR','FLGT','BGCP','MMI','TEN','RVNC','PRO','TREE','NVTA','HCAT','ELF','UIS','NYMT','DIN','DNUT','MLAB','SGH','VECO','CNOB','OPI','LZB','MNRL','KAMN','FFWM','NBHC','MCRI','GSHD','RGNX','GTY','HRMY','PRVA','NXGN','CHCO','HURN','SXI','EIG','CCO','CUTR','BIG','ARRY','CWH','BRKL','ONEM','AMCX','SNBR','WOW','NCBS','APOG','OCFC','VIVO',
    'LAUR','TCBK','FRG','BRP','EVOP','CCXI','BBIO','IPI','AXSM','TMP','AZZ','FRO','RPT','GPRO','SBGI','STEM','NTUS','IMGN','CTS','AHCO','CDMO','GPRE','CLNE','PFC','CWENA','TMST','DVAX','CHEF','MBUU','CMPR','STNG','CMCO','FIZZ','CRNX','SHEN','EDIT','SHYF','UMH','SSP','ROAD','MRC','FA','BANC','BRMK','CDXS','MCB','RWT','STBA','AGM','EXPI','LBAI','BALY','PSN','AIV','LPI','BCOR','SCHL','EB','KURA','ATRI','BKE','INN','CTKB','TBI','GCO','TSC','SCS','XMTR','AOSL','SAFE','PGTI','HA','KROS',
    'RC','PCVX','MODN','SAH','GES','CHCT','NSTG','MRTN','PI','BIGC','OBNK','INSW','RDNT','GABC','OEC','BATRK','AVYA','PAR','USNA','MGI','TUP','MATW','QCRH','SATS','GFF','CNDT','GMRE','PLAB','RADI','TGTX','DBI','CCSI','TDW','ATRS','XENT','AHH','AMSF','GDEN','ASTE','NHC','FDP','DFIN','SUMO','GLDD','FGEN','LGFA','RXDX','UTZ','NTST','NUVB','MDGL','ZNTL','SMP','CVI','ANGO','HSC','HZO','SNCY','ATEC','GEVO','WASH','FSBC','HEAR','AKRO','URG',
    'KRNY','JRVR','DHT','EBIX','LMAT','RETA','EFC','MNKD','CLBK','HBNC','ADTN','XPRO','CARS','CAL','HFWA','CMRE','BLNK','PTGX','SCSC','WRLD','CSII','SAVA','XPEL','AORT','ALHC','TWOU','ICHR','IMAX','HMST','WETF','ERII','RES','SFIX','SWM','BHE','ACRS','FARO','SNDX','PEBO','GOOD','AXL','CPRX','CERS','VERU','GNK','SXC','DENN','CEVA','GEO','ABTX','VREX','LYEL','BRY','ARKO','CSV','AGYS','HWKN','VTOL','ROCC','MYE','UVSP','SRCE','ATEN','ZUMZ','PLYM','PRDO','UTL','SPNS','INVA','AMTB','GSAT',
    'NPTN','AMRK','HLIT','PLOW','HLX','QTRX','SLP','DM','HSII','MORF','AMWD','AMRS','GRC','WINA','TILE','TWI','BSIG','IIIN','LUNG','UHT','JBSS','PLCE','KELYA','FUBO','YEXT','RXRX','CAC','CCRN','SENS','RUTH','TALO','VVI','AVXL','STRL','BRSP','LFST','ARLO','SIBN','HAFC','ACCO','FBMS','PFBC','ACCD','PARR','HONE','CFB','PDFS','HTBK','ACEL','RYI','PWSC','SWBI','SP','KIDS','AVD','CTBI','DGII','AAN','CHRS','HNGR','CIO','ATRA','TRTX','KREF','ACRE','GDYN','WNC','RNA','NX','CPF','CLFD','AMWL',
    'BJRI','VERV','NAPA','LLNW','CVGW','FFIC','CHS','ARR','BAND','BY','ALEC','PACK','OPRX','IMXI','CLDT','DHC','CCF','BTRS','HIBB','ATEX','SANA','NP','FMBH','NTGR','ENDP','LASR','COWN','LOVE','BFS','PGC','ECVT','RLMD','ETD','BXC','ITOS','GSBC','COLL','INO','OFIX','FORR','KDNY','TCX','MBI','EGLE','MOV','NFBK','UFCS','CLAR','WSR','MSBI','PBI','SPNT','VNDA','DCO','GRBK','CRAI','SGMO','PETQ','GCI','HTLD','AMSWA','LTH','ALBO','QUOT','SRDX','TMDX','RICK','TRST','BV','ASPN','TMCI','EGRX',
    'CNXN','CASS','CARA','CATC','CBTX','IVR','SCVL','MBWM','MITK','IIIV','GPMT','HCKT','BNGO','RXT','AGX','OSW','TRNS','NWLI','SRNE','ARQT','BBSI','RGP','HAYN','ALX','REAL','NSSC','DX','SWIM','MVIS','DHIL','KOP','RCKT','FC','WW','KZR','FSP','TR','BMRC','QNST','UBA','INGN','PTLO','YORW','BFLY','GLT','VXRT','CRSR','OSPN','NRC','ALLO','TBPH','BOOM','GOEV','REPL','WTTR','FOSL','MDXG','THFF','CRGY','ARCT','ERAS','WKHS','THR','TA','MXCT','CHUY','FMNB','CRMT','SRI','GOSS','OUST','INBX','HIFS',
    'CSTL','REX','TTI','VVNT','PCT','AGEN','TITN','ORGO','KPTI','PETS','ALTO','AGTI','LAW','HRTX','HSTM','UFPT','OCGN','OLP','NGM','BOC','FISI','RMAX','GRPN','DOUG','MGNX','HYFM','OSUR','TIL','BFC','AVO','DNMR','MTW','AFMD','RIGL','LIND','LILA','TTCF','VRAY','HTBI','LPG','BLX','MOFG','JYNT','RMR','LXFR','FNKO','SPWH','CPSI','FCBC','WTI','BFST','IBCP','MSFUT','DXPE','TPIC','UPLD','BHG','CARE','CNSL','FPI','CCB','MCFT','BZH','HCCI','STGW','USM','OIS','IDT','BW','ECOM','CLW','TPB','RBCAA',
    'EBF','CIR','GERN','PNTG','CTOS','VERI','FBRT','FLIC','ATNI','YMAB','PAYA','IAS','VEC','EQBK','CSTR','SEER','AROW','NAT','ESTE','CENT','MCBS','SRG','HVT','LQDT','HYLN','CCNE','KE','ANAB','VSEC','PRTY','WTBA','GRWG','RAPT','PTVE','MVBF','OSBC','INBK','MBIN','WSBF','JOUT','PMVP','CTT','TPC','ADV','BHB','MOD','REVG','ICPT','BASE','STER','ABSI','ULCC','NOTV','NRIX','AMK','AMRX','EWCZ','ALRS','GCMG','BVH','AVIR','LL','DBD','GIC','APEI','MCS','AMNB','RAD','TNK','FRPH','MCRB','IDEX','AMBC',
    'PRCH','CRBU','ACET','SOVO','MASS','PAHC','AEVA','ORC','FLWS','DCPH','ZEUS','BLFY','ONTF','NPK','OFLX','MPB','VPG','TRC','RIDE','CMTL','UEIC','CZNC','ARTNA','SFST','TCMD','MGTX','POWW','EVCM','UVE','CTO','INDT','RM','MLNK','FDMT','CLSK','ATHA','HCI','NR','KRO','BWB','CCCC','HNST','TLS','RDUS','TRUE','DSGN','EZPW','RYTM','TSVT','RSI','ALKT','GLUE','ONEW','ESMT',    'BNFT','CONN','VITL','VERA','STRO','ARIS','COGT','BCOV','CNTY','FOR','TNYA','MRSN','KBAL','MPAA','EVER','EWTX','UTMD',
    'GEFB','SOI','EOLS','SMBC','STOK','FULC','AERI','PRTS','PFIS','SMBK','DMRC','BVS','BSRR','CMRX','ANIP','RBB','EBTC','CCBG','FRST','IMGO','HRT','IDYA','SPNE','XXII','SIGA','EVC','DJCO','LEU','RYAM','CIVB','SENEA','AUD','INTA','IBRX','AMTX','ANIK','IESC','MAX','PLBY','PRVB','HY','BGFV','IEA','DSKE','FXLV','KNSA','ARAY','BHR','TG','FLL','PRPL','VUZI','OPY','AMOT','GBIO','CTLP','MNMD','HBCP','RUSHB','SG','APPH','WLDN','CATO','BLBD','HT','FLMN','KALV','OOMA','MLR','NESR','FNLC','OCUL',
    'PHAT','EYPT','FREE','OPRT','SPFI','SRRK','VTGN','GNTY','SMMF','MMAT','PRAX','DICE','VSTM','SB','ATRO','CGEM','AXGN','BLUE','SLQT','BLI','FMTX','PRCT','NWPX','OMER','VBIV','KODK','IRMD','TIPT','INSG','BATRA','GTHX','ALXO','INVE','RCKY','FF','CURO','RMNI','AKTS','MRNS','BTAI','DYN','BRBS','SCU','BRT','ESPR','HOV','DMTK','ENFN','TCS','AMAL','FHTX','AVNW','LNDC','XPOF','CRDO','NRIM','SSTI','CTRN','PSNL','AXTI','PCSB','SNPO','KRUS','ITIC','CLVS','RRBI','LE','YELL','REPX','CSTE','LAB',
    'CVGI','NVEC','PVBC','GNOG','USLM','ORRF','MCBC','PKE','ORMP','TK','ABUS','AVDX','KNTK','ATLC','ICVX','RRGB','ASLE','RLGT','JANX','UFI','PCYO','PSTL','EGAN','AFCG','KNTE','JNCE','DAWN','GNUS','OMIC','FRBA','EHTH','FSBW','GHL','CVLG','KOD','RBBN','KRON','ACTG','OB','HBIO','ALTG','AJX','INST','ATOM','LBC','NDLS','COOK','FRBK','GATO','LMNR','THRY','DZSI','NATR','EIGR','LOCO','HOFT','CAMP','CINC','STKS','NUVL','CIA','ALT','TLYS','GWRS','LUNA','VLGEA','PTSI','AOUT','RXST','CBAY','SGC',
    'HFFG','VMD','OTLK','CLPT','IMVT','WEBR','DGICA','CBNK','PLPC','BEEM','ALDX','CASA','SGHT','POWL','QMCO','XL','VRA','AMSC','CCRD','ADGI','BLFS','SCOR','CMBM','IPSC','GAN','FDBC','GLRE','MTRX','NGVC','VATE','OCN','RCEL','CRMD','LAWS','RLYB','HBT','VKTX','ATCX','LCUT','AGS','ZYXI','ALLK','AVTE','HRTG','BSET','MHLD','ZY','PLRX','HPK','BNED','APYX','TALS','VIEW','UDMY','ALVR','VLDR','LCTX','IKNA','SMSI','FNA','STXS','PGEN','LEGH','IMUX','IGMS','TARS','CECE','NCMI','ATER','LXRX','DLTH',
    'XOMA','LAZY','SPPI','TH','CTXR','AOMR','DIBS','AHT','BBCP','VOXX','MESA','NODK','SPRO','CTMX','INFU','VTYX','ODC','CDRE','ULH','URGN','GRTS','ESCA','CUE','BYRN','NATH','KOPN','DAKT','EAR','AKYA','FTCI','LTRPA','FLXS','EMKR','VAPO','NGMS','CRDA','KMPH','SCWX','ATOS','JOAN','DTIL','RELY','FWRG','AMTI','XBIT','REKR','IMRX','GBL','PZN','ASXC','AVAH','FRGI','ORIC','KIRK','INNV','TSHA','MG','PBFS','EOSE','EVI','RMO','KVHI','THRX','NKTX','CPS','FUV','CLPR','ITI','CVM','NLS','BH','VIRX',
    'NNBR','RENT','OMGA','DS','AQB','CTSO','SFT','ABOS','PPTA','VHC','TKNO','TSAT','MILE','NMTR','VOR','HGEN','CURV','PRTK','GRPH','TYRA','MPX','CRIS','PLM','HLTH','PKOH','DRRX','CDXC','EPZM','TXMD','VALU','ATHX','HOWL','SIEN','AMLX','ACLX','VIA','WLFC','MBII','GTYH','PASG','PSTX','ADVM','TNXP','SESN','VRCA','TRHC','HQI','STTK','COCO','PBYI','MIRM','ALPN','IBEX','USX','KRT','LSEA','AKUS','TCRT','OYST','CRTX','FIXX','CNVY','AKBA','TIG','SQZ','WLLAW','MTEM','VHI','DTC','STON','SELB','VEL',
    'HBB','SURF','RPID','OLMA','DRIO','FBIO','REFI','INFI','MEC','DSP','LOTZ','PAVM','BMEA','EEX','AGLE','STIM','KLTR','WVE','BDTX','TCRR','FLNT','RUBY','ANNX','SEEL','IBIO','OCX','ICAD','XGN','HMTV','RVP','CELC','USER','EVLO','FORA','SRT','AMPE','ARDX','AURA','BCEL','SMED','GLSI','SBTX','RGS','TAST','AWH','AC','TRVN','UIHC','UAVS','NL','CURI','INZY','AIP','GBOX','BCAB','RAIN','PRLD','CRDF','MBIO','CDAK','TRDA','NBEV','ATNX','FREQ','EBET','SKYT','MEIP','ELYM','NPCE','FOA','HARP','CLNN',
    'MGTA','SLDB','QTNT','PRTH','SYRS','NEXI','REV','CSSE','HOFV','TISI','NLTX','BOLT','IVC','ONCT','SMMT','PLSE','BYSI','LVO','CDZI','FTHM','KALA','TCBX','GTBP','BTX','AVRO','ESGC','SNSE','ADN','CVRX','ZVIA','CIX','ZGNX','AIRS','VINC','ANGN','ADRO','IMPL','APLT','AXDX','VIGL','GMTX','SDIG','AVTX','MDVL','HOOK','TERN','DNAY','WLLBW','ALGS','XLO','HYRE','AKA','CYT','ETNB','ONCR','FNCH','PYXS','HMPT','PRTG','RFL','SGTX','NH','SPRB','FBRX','AFIB','BDSX','TLIS','LSF','RPHM','OTRK','GNLN','SERA',
    'DMS','LVLU','LABP','ISO','PDLI','GTXI','KLDO'
]

MOVING_AVERAGE_DAYS = 3
TODAY = datetime.date.today()
START_DATE = TODAY - datetime.timedelta(days=MOVING_AVERAGE_DAYS)

ORDER_DOLLAR_SIZE = 5000