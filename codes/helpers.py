def icd_chapter_section(condition_code):
    try:
        icd_section = int(condition_code.split('.')[0])
    except:
        return 0, 0
    if icd_section >= 1 and icd_section <= 139:
        chapter = 1
    elif icd_section >= 140 and icd_section <= 239:
        chapter = 2
    elif icd_section >= 240 and icd_section <= 279:
        chapter = 3
    elif icd_section >= 280 and icd_section <= 289:
        chapter = 4
    elif icd_section >= 290 and icd_section <= 319:
        chapter = 5
    elif icd_section >= 320 and icd_section <= 389:
        chapter = 6
    elif icd_section >= 390 and icd_section <= 459:
        chapter = 7
    elif icd_section >= 460 and icd_section <= 519:
        chapter = 8
    elif icd_section >= 520 and icd_section <= 579:
        chapter = 9
    elif icd_section >= 580 and icd_section <= 629:
        chapter = 10
    elif icd_section >= 630 and icd_section <= 679:
        chapter = 11
    elif icd_section >= 680 and icd_section <= 709:
        chapter = 12
    elif icd_section >= 710 and icd_section <= 739:
        chapter = 13
    elif icd_section >= 740 and icd_section <= 759:
        chapter = 14
    elif icd_section >= 760 and icd_section <= 779:
        chapter = 15
    elif icd_section >= 780 and icd_section <= 799:
        chapter = 16
    elif icd_section >= 800 and icd_section <= 999:
        chapter = 17
    # 1. Infectious And Parasitic Diseases
    if icd_section >= 1 and icd_section <= 9:
        section = 1
    elif icd_section >= 10 and icd_section <= 18:
        section = 2
    elif icd_section >= 20 and icd_section <= 27:
        section = 3
    elif icd_section >= 30 and icd_section <= 41:
        section = 4
    elif icd_section >= 42 and icd_section <= 44:
        section = 5
    elif icd_section >= 45 and icd_section <= 49:
        section = 6
    elif icd_section >= 50 and icd_section <= 59:
        section = 7
    elif icd_section >= 60 and icd_section <= 66:
        section = 8
    elif icd_section >= 70 and icd_section <= 79:
        section = 9
    elif icd_section >= 80 and icd_section <= 88:
        section = 10
    elif icd_section >= 90 and icd_section <= 99:
        section = 11
    elif icd_section >= 100 and icd_section <= 104:
        section = 12
    elif icd_section >= 110 and icd_section <= 118:
        section = 13
    elif icd_section >= 120 and icd_section <= 129:
        section = 14
    elif icd_section >= 130 and icd_section <= 136:
        section = 15
    elif icd_section >= 137 and icd_section <= 139:
        section = 16
    # 2. Neoplasms
    elif icd_section >= 140 and icd_section <= 149:
        section = 17
    elif icd_section >= 150 and icd_section <= 159:
        section = 18
    elif icd_section >= 160 and icd_section <= 165:
        section = 19
    elif icd_section >= 170 and icd_section <= 176:
        section = 20
    elif icd_section >= 179 and icd_section <= 189:
        section = 21
    elif icd_section >= 190 and icd_section <= 199:
        section = 22
    elif icd_section >= 200 and icd_section <= 209:
        section = 23
    elif icd_section >= 210 and icd_section <= 229:
        section = 24
    elif icd_section >= 230 and icd_section <= 234:
        section = 25
    elif icd_section >= 235 and icd_section <= 238:
        section = 26
    elif icd_section >= 239 and icd_section <= 239:
        section = 27
    # 3. endocrine, nutritional and metabolic diseases, and immunity disorders
    elif icd_section >= 240 and icd_section <= 246:
        section = 28
    elif icd_section >= 249 and icd_section <= 259:
        section = 29
    elif icd_section >= 260 and icd_section <= 269:
        section = 30
    elif icd_section >= 270 and icd_section <= 279:
        section = 31
    # 4. Diseases Of The Blood And Blood-Forming Organs
    elif icd_section >= 280 and icd_section <= 289:
        section = 32
    # 5. Mental disorder
    elif icd_section >= 290 and icd_section <= 294:
        section = 33
    elif icd_section >= 295 and icd_section <= 299:
        section = 34
    elif icd_section >= 300 and icd_section <= 316:
        section = 35
    elif icd_section >= 317 and icd_section <= 319:
        section = 36
    # 6. Diseases Of The Nervous System And Sense Organs
    elif icd_section >= 320 and icd_section <= 327:
        section = 37
    elif icd_section >= 330 and icd_section <= 337:
        section = 38
    elif icd_section >= 338 and icd_section <= 338:
        section = 39
    elif icd_section >= 339 and icd_section <= 339:
        section = 40
    elif icd_section >= 340 and icd_section <= 349:
        section = 41
    elif icd_section >= 350 and icd_section <= 359:
        section = 42
    elif icd_section >= 360 and icd_section <= 379:
        section = 43
    elif icd_section >= 380 and icd_section <= 389:
        section = 44
    # 7. Diseases Of The Circulatory System
    elif icd_section >= 390 and icd_section <= 392:
        section = 45
    elif icd_section >= 393 and icd_section <= 398:
        section = 46
    elif icd_section >= 401 and icd_section <= 405:
        section = 47
    elif icd_section >= 410 and icd_section <= 414:
        section = 48
    elif icd_section >= 415 and icd_section <= 417:
        section = 49
    elif icd_section >= 420 and icd_section <= 429:
        section = 50
    elif icd_section >= 430 and icd_section <= 438:
        section = 51
    elif icd_section >= 440 and icd_section <= 449:
        section = 52
    elif icd_section >= 451 and icd_section <= 459:
        section = 53
    # 8. Diseases Of The Respiratory System
    elif icd_section >= 460 and icd_section <= 466:
        section = 54
    elif icd_section >= 470 and icd_section <= 478:
        section = 55
    elif icd_section >= 480 and icd_section <= 488:
        section = 56
    elif icd_section >= 490 and icd_section <= 496:
        section = 57
    elif icd_section >= 500 and icd_section <= 508:
        section = 58
    elif icd_section >= 510 and icd_section <= 519:
        section = 59
    # 9. Diseases Of The Digestive System
    elif icd_section >= 520 and icd_section <= 529:
        section = 60
    elif icd_section >= 530 and icd_section <= 539:
        section = 61
    elif icd_section >= 540 and icd_section <= 543:
        section = 62
    elif icd_section >= 550 and icd_section <= 553:
        section = 63
    elif icd_section >= 555 and icd_section <= 558:
        section = 64
    elif icd_section >= 560 and icd_section <= 569:
        section = 65
    elif icd_section >= 570 and icd_section <= 579:
        section = 66
    # 10. Diseases Of The Genitourinary System
    elif icd_section >= 580 and icd_section <= 589:
        section = 67
    elif icd_section >= 590 and icd_section <= 599:
        section = 68
    elif icd_section >= 600 and icd_section <= 608:
        section = 69
    elif icd_section >= 610 and icd_section <= 612:
        section = 70
    elif icd_section >= 614 and icd_section <= 616:
        section = 71
    elif icd_section >= 617 and icd_section <= 629:
        section = 72
    # 11. Complications Of Pregnancy, Childbirth, And The Puerperium
    elif icd_section >= 630 and icd_section <= 639:
        section = 73
    elif icd_section >= 640 and icd_section <= 649:
        section = 74
    elif icd_section >= 650 and icd_section <= 659:
        section = 75
    elif icd_section >= 660 and icd_section <= 669:
        section = 76
    elif icd_section >= 670 and icd_section <= 677:
        section = 77
    elif icd_section >= 678 and icd_section <= 679:
        section = 78
    # 12. Diseases Of The Skin And Subcutaneous Tissue
    elif icd_section >= 680 and icd_section <= 686:
        section = 79
    elif icd_section >= 690 and icd_section <= 698:
        section = 80
    elif icd_section >= 700 and icd_section <= 709:
        section = 81
    # 13. Diseases Of The Musculoskeletal System And Connective Tissue
    elif icd_section >= 710 and icd_section <= 719:
        section = 82
    elif icd_section >= 720 and icd_section <= 724:
        section = 83
    elif icd_section >= 725 and icd_section <= 729:
        section = 84
    elif icd_section >= 730 and icd_section <= 739:
        section = 85
    # 14. Congenital Anomalies
    elif icd_section >= 740 and icd_section <= 759:
        section = 86
    # 15. Certain Conditions Originating In The Perinatal Period
    elif icd_section >= 760 and icd_section <= 763:
        section = 87
    elif icd_section >= 764 and icd_section <= 779:
        section = 88
    # 16. Symptoms, Signs, And Ill-Defined Conditions
    elif icd_section >= 780 and icd_section <= 804:
        section = 89
    elif icd_section >= 790 and icd_section <= 809:
        section = 90
    elif icd_section >= 797 and icd_section <= 819:
        section = 91
    # 17. Injury And Poisoning
    elif icd_section >= 800 and icd_section <= 804:
        section = 92
    elif icd_section >= 805 and icd_section <= 809:
        section = 93
    elif icd_section >= 810 and icd_section <= 819:
        section = 94
    elif icd_section >= 820 and icd_section <= 829:
        section = 95
    elif icd_section >= 830 and icd_section <= 839:
        section = 96
    elif icd_section >= 840 and icd_section <= 848:
        section = 94
    elif icd_section >= 850 and icd_section <= 854:
        section = 98
    elif icd_section >= 860 and icd_section <= 869:
        section = 99
    elif icd_section >= 870 and icd_section <= 879:
        section = 100
    elif icd_section >= 880 and icd_section <= 887:
        section = 101
    elif icd_section >= 890 and icd_section <= 897:
        section = 102
    elif icd_section >= 900 and icd_section <= 904:
        section = 103
    elif icd_section >= 905 and icd_section <= 909:
        section = 104
    elif icd_section >= 910 and icd_section <= 919:
        section = 105
    elif icd_section >= 920 and icd_section <= 924:
        section = 106
    elif icd_section >= 925 and icd_section <= 929:
        section = 107
    elif icd_section >= 930 and icd_section <= 939:
        section = 108
    elif icd_section >= 940 and icd_section <= 949:
        section = 109
    elif icd_section >= 950 and icd_section <= 957:
        section = 110
    elif icd_section >= 958 and icd_section <= 959:
        section = 111
    elif icd_section >= 960 and icd_section <= 979:
        section = 112
    elif icd_section >= 980 and icd_section <= 989:
        section = 113
    elif icd_section >= 990 and icd_section <= 995:
        section = 114
    elif icd_section >= 996 and icd_section <= 999:
        section = 115
    return chapter, section
    
def cause_of_death_disease(condition_code):
    section_str = condition_code.split('.')[0]
    try:
        icd_num = float(condition_code)
    except:
        return -1
    if int(icd_num) == 11 or int(icd_num) == 12:
        return 0 # Respiratory tuberculosis
    if int(icd_num) == 33:
        return 1 # Pertussis
    if icd_num in [34, 35] or icd_num == 41.09:
        return 2 # Streptococcal sore throat, scarlatina, and erysipelas
    if int(icd_num) == 38:
        return 3 # Sepsis
    if int(icd_num) == 55:
        return 4 # Measles
    if int(icd_num) == 45:
        return 5 # Acute poliomyelitis
    if int(icd_num) == 71:
        return 6 # Rabbies
    if int(icd_num) == 70:
        return 7 # Viral hepatitis
    if int(icd_num) == 150:
        return 8 # Malignant neoplasm of esophagus
    if int(icd_num) == 151:
        return 9 # Malignant neoplasm of stomach
    if int(icd_num) == 152:
        return 10 # Malignant neoplasm of small intestine
    if int(icd_num) in [153, 154]:
        return 11 # Malignant neoplasm of colon, rectum and anus
    if int(icd_num) in [155, 156]:
        return 12 # Malignant neoplasm of liver and intrahepatic bile ducts
    if int(icd_num) == 157:
        return 13 # Malignant neoplasm of pancreas
    if int(icd_num) == 161:
        return 14 # Malignant neoplasm of larynx
    if int(icd_num) in [162, 163]:
        return 15 # Malignant neoplasm of trachea, bronchus and lung
    if int(icd_num) in [172, 173]:
        return 16 # Malignant neoplasm of skin
    if int(icd_num) == 174:
        return 17 # Malignant neoplasm of breast
    if int(icd_num) in [179, 180, 181, 182]:
        return 18 # Malignant neoplasm of cervix uteri
    if int(icd_num) == 183:
        return 19 # Malignant neoplasm of ovary
    if int(icd_num) == 185:
        return 20 # Malignant neoplasm of prostate
    if int(icd_num) == 189:
        return 21 # Malignant neoplasm of kidney and renal pelvis
    if int(icd_num) == 188:
        return 22 # Malignant neoplasm of bladder
    if int(icd_num) in [191, 192]:
        return 23 # Malignant neoplasm of meninges, brain and other parts of central nervous system
    if int(icd_num) in [200, 201, 202, 203]:
        return 24 # Malignant neoplasm of lymphoid, hematopoietic and related tissue
    if int(icd_num) in [249, 250]:
        return 25 # Diabetes mellitus
    if int(icd_num) in [47, 320, 321, 322]:
        return 26 # Meningitis
    if int(icd_num) == 332:
        return 27 # Parkinson disease
    if int(icd_num) == 294:
        return 28 # Alzheimer disease
    if icd_num >= 402.1 and icd_num < 402.2:
        return 29 # Benign hypertensive heart disease
    if icd_num == 402.01:
        return 30 # Malignant hypertensive heart disease with heart failure
    if icd_num == 402.00:
        return 31 # Malignant hypertensive heart disease without heart failure
    if icd_num == 403.91:
        return 32 # Hypertensive renal disease with renal failure
    if icd_num == 403.93:
        return 33 # Hypertensive heart and renal disease with (congestive) heart failure
    if int(icd_num) == 410:
        return 34 # Acute myocardial infarction
    if int(icd_num) == 434:
        return 35 # Cerebral infarction
    if icd_num == 493.92:
        return 36 # Acute exacerbation of asthma
    if int(icd_num) == 493:
        return 37 # Asthma
    if int(icd_num) in [490, 491]:
        return 38 # Bronchitis
    if int(icd_num) in [492, 518, 998, 958]:
        return 39 # Emphysema
    if int(icd_num) == 584:
        return 40 # Renal failure
    if int(icd_num) == 580:
        return 41 # Acute glomerulonephritis and nephrotic syndrome
    if icd_num == 494.1:
        return 42 # Acute exacerbation of bronchiectasis
    if icd_num == 491.21:
        return 43 # Acute exacerbation of chronic obstructive airways disease
    return -1
    
def other_icd9(condition_code):
    section_str = condition_code.split('.')[0]
    if len(section_str) == 0: return -1
    if section_str[0] == 'V':
        if int(section_str[1:]) == 9:
            return 0 # personal history of cancer
        if int(section_str[1:]) == 10:
            return 1 # personal history of cancer
        if int(section_str[1:]) == 16:
            return 2 # family history of cancer
        if int(section_str[1:]) == 46:
            return 3 # dependence on machines and devices
        if float(condition_code[1:]) >= 58.1 and float(condition_code[1:]) < 58.2:
            return 4 # Encounter for antineoplastic chemotherapy and immunotherapy
        if float(condition_code[1:]) == 58.69:
            return 5 # High-risk medications
        if int(section_str[1:]) == 59:
            return 6 # Donors
        if float(condition_code[1:]) == 87.46:
            return 7 # History of immunosuppressive therapy
        if float(condition_code[1:]) == 87.43:
            return 8 # History of estrogen therapy
        if float(condition_code[1:]) >= 62.1 and float(condition_code[1:]) < 62.2 or int(section_str[1:]) == 87:
            return 9 # Personal exposures and history presenting hazards to health
        if float(condition_code[1:]) == 49.83:
            return 10 # On waiting list for organ transplant

        if int(section_str[1:]) >= 1 and int(section_str[1:]) <= 9:
            return 11 # Persons With Potential Health Hazards Related To Communicable Diseases
        if int(section_str[1:]) >= 10 and int(section_str[1:]) <= 19:
            return 12 # Persons With Potential Health Hazards Related To Personal And Family History
        if int(section_str[1:]) >= 20 and int(section_str[1:]) <= 29:
            return 13 # Persons Encountering Health Services In Circumstances Related To Reproduction And Development
        if int(section_str[1:]) >= 30 and int(section_str[1:]) <= 39:
            return 14 # Liveborn Infants According To Type Of Birth
        if int(section_str[1:]) >= 40 and int(section_str[1:]) <= 49:
            return 15 # Persons With A Condition Influencing Their Health Status
        if int(section_str[1:]) >= 50 and int(section_str[1:]) <= 59:
            return 16 # Persons Encountering Health Services For Specific Procedures And Aftercare
        if int(section_str[1:]) >= 60 and int(section_str[1:]) <= 69:
            return 17 # Persons Encountering Health Services In Other Circumstances
        if int(section_str[1:]) >= 70 and int(section_str[1:]) <= 82:
            return 18 # Persons Without Reported Diagnosis Encountered During Examination And Investigation Of Individuals And Populations
        if int(section_str[1:]) >= 83 and int(section_str[1:]) <= 84:
            return 19 # Genetics
        if int(section_str[1:]) == 86 and float(condition_code[1:]) == 86:
            return 20 # Estrogen Receptor Status +
        if int(section_str[1:]) == 86 and float(condition_code[1:]) == 86.1:
            return 21 # Estrogen Receptor Status -
        if int(section_str[1:]) == 87:
            return 22 # Other Specified Personal Exposures And History Presenting Hazards To Health
        if int(section_str[1:]) == 88:
            return 23 # Acquired Absence Of Other Organs And Tissue
        if int(section_str[1:]) == 89:
            return 24 # Other Suspected Conditions Not Found
        if int(section_str[1:]) == 90:
            return 25 # Retained Foreign Body
        if int(section_str[1:]) == 91:
            return 26 # Multiple Gestation Placenta Status
    
    if section_str[0] == 'E':
        if int(section_str[1:]) >= 800 and int(section_str[1:]) < 850:
            return 25 # Traffic Accidents
        if int(section_str[1:]) >= 850 and int(section_str[1:]) < 870:
            return 26 # Accidental Poisoning
        if int(section_str[1:]) >= 870 and int(section_str[1:]) < 880:
            return 27 # Misadventures To Patients During Surgical And Medical Care       
        if int(section_str[1:]) >= 880 and int(section_str[1:]) < 929:
            return 28 # Accidents
        if int(section_str[1:]) == 929:
            return 29 # Late Effects Of Accidental Injury
        if int(section_str[1:]) >= 930 and int(section_str[1:]) < 950:
            return 30 # Adverse Effects In Therapeutic Use
        if int(section_str[1:]) >= 950 and int(section_str[1:]) < 960:
            return 31 # Suicide And Self-Inflicted Injury
        if int(section_str[1:]) >= 960 and int(section_str[1:]) < 970:
            return 32 # Homicide       
    return -1
    
def proc_cpt4(proc_code):
    try:
        num_proc = int(proc_code)
    except:
        return 30
    if num_proc>=100 and num_proc<2000:
        return 0 # Anesthesia
    if num_proc>=10004 and num_proc<=10021:
        return 1 # Fine Needle Aspiration Biopsy Procedures
    if num_proc>=10030 and num_proc<=19499:
        return 2 # Surgical Procedures on the Integumentary System
    if num_proc>=20100 and num_proc<=29999:
        return 3 # Surgical Procedures on the Musculoskeletal System
    if num_proc>=30000 and num_proc<=32999:
        return 4 # Surgical Procedures on the Respiratory System
    if num_proc>=33016 and num_proc<=37799:
        return 5 # Surgical Procedures on the Cardiovascular System
    if num_proc>=39000 and num_proc<=39599:
        return 6 # Surgical Procedures on the Mediastinum and Diaphragm
    if num_proc>=38100 and num_proc<=38999:
        return 7 # Surgical Procedures on the Hemic and Lymphatic Systems
    if num_proc>=40490 and num_proc<=49999:
        return 8 # Surgical Procedures on the Digestive System
    if num_proc>=50010 and num_proc<=53899:
        return 9 # Surgical Procedures on the Urinary System
    if num_proc>=54000 and num_proc<=55899:
        return 10 # Surgical Procedures on the Male Genital System
    if num_proc==55920:
        return 11 # Reproductive System Procedures
    if num_proc>=55970 and num_proc<=55980:
        return 12 # Intersex Surgery
    if num_proc>=56405 and num_proc<=58999:
        return 13 # Surgical Procedures on the Female Genital System
    if num_proc>=59000 and num_proc<=59899:
        return 14 # Surgical Procedures for Maternity Care and Delivery
    if num_proc>=60000 and num_proc<=60699:
        return 15 # Surgical Procedures on the Endocrine System
    if num_proc>=61000 and num_proc<=64999:
        return 16 # Surgical Procedures on the Nervous System
    if num_proc>=65091 and num_proc<=68899:
        return 17 # Surgical Procedures on the Eye and Ocular Adnexa
    if num_proc>=69000 and num_proc<=69979:
        return 18 # Surgical Procedures on the Auditory System
    if num_proc==69990:
        return 19 # Operating Microscope Procedures
    if num_proc>=70010 and num_proc<=76499:
        return 20 # Diagnostic Radiology (Diagnostic Imaging) Procedures
    if num_proc>=76506 and num_proc<=76999:
        return 21 # Diagnostic Ultrasound Procedures
    if num_proc>=77001 and num_proc<=77022:
        return 22 # Radiologic Guidance
    if num_proc>=77046 and num_proc<=77067:
        return 23 # Breast, Mammography
    if num_proc>=77071 and num_proc<=77086:
        return 24 # Bone/Joint Studies
    if num_proc>=77261 and num_proc<=77799:
        return 25 # Radiation Oncology Treatment
    if num_proc>=78012 and num_proc<=79999:
        return 26 # Nuclear Medicine Procedures
    if num_proc>=80047 and num_proc<=89398:
        return 27 # Pathology and Laboratory Procedures
    if num_proc>=90281 and num_proc<=99756:
        return 28 # Medicine Services and Procedures
    if num_proc>=99201 and num_proc<=99499:
        return 29 # Evaluation and Management Services
    return 30
