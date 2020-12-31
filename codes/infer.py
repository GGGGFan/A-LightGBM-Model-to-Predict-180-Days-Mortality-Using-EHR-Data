import sqlite3
import csv
import gc
import numpy as np
import pandas as pd
from dateutil import parser
from scipy import sparse
import lightgbm as lgb
from helpers import *

evl_path = '/infer/'
db_path = 'dream_challenge_3.sqlite3'
measurement_list = [3024561, 3025313, 3002069, 3036955, 3018910, 3020990,
                   3015632, 3021447, 3027946, 3007696, 3021513, 3003932,
                   3028193, 3024128, 3027597, 4154790, 4152194, 3004295,
                   3010156, 3035569, 3018405, 3024929, 3021706, 3027801,
                   3000483, 3010300, 3004501, 3034962, 3011424, 3030260,
                   3028653, 3000963, 3002173, 3022493, 3004119, 3045807,
                   3000185, 3002400, 3021044, 3023103, 3000593, 3037556,
                   3007144, 3008342, 3013650, 3014502, 40765040,3016502,
                   3020630, 3029872, 3037121, 3005029, 4239408, 3019550,
                   3009596, 3009966, 3027114, 3007070, 3007352, 3015232,
                   3006906, 3013784, 3021119, 3034244, 3000637, 3022192,
                   3005770, 3016723, 3017250, 3016662, 3051825, 3004239,
                   44783982]

class OmopParser_predict(object):

    def __init__(self):
        self.name = 'omop_assembler'

    def build_database(self):
        # connect to database
        con = sqlite3.connect(db_path)
        # build table person
        query = """
                CREATE TABLE person_evl
                (
                    person_id INT,
                    gender_concept_id INT,
                    year_of_birth INT,
                    ethnicity_concept_id INT
                )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'person.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['person_id', 'gender_concept_id', 'year_of_birth', 'ethnicity_concept_id']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO person_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        con.commit()
        con.close()
        print('Table person built')

        # Table condition
        con = sqlite3.connect(db_path)
        query = """
                CREATE TABLE condition_evl
                (
                    condition_occurrence_id INT NOT NULL,
                    person_id INT,
                    condition_concept_id INT,
                    condition_start_date CHAR(14),
                    condition_end_date CHAR(14),
                    condition_type_concept_id INT,
                    visit_occurrence_id INT,
                    condition_source_concept_id INT
                )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'condition_occurrence.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['condition_occurrence_id', 'person_id', 'condition_concept_id', \
                                           'condition_start_date', 'condition_end_date', 'condition_type_concept_id',\
                                           'visit_occurrence_id', 'condition_source_concept_id']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO condition_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        con.commit()
        con.close()
        print('Table condition built')

        # TABLE visit
        con = sqlite3.connect(db_path)
        query = """
            CREATE TABLE visit_evl
            (
                visit_occurrence_id INT,
                person_id INT,
                visit_concept_id INT,
                visit_start_date VARCHAR(14),
                visit_end_date VARCHAR(14),
                visit_type_concept_id INT,
                provider_id INT,
                care_site_id INT,
                visit_source_concept_id INT
            )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'visit_occurrence.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['visit_occurrence_id', 'person_id', 'visit_concept_id', \
                                           'visit_start_date', 'visit_end_date', 'visit_type_concept_id',\
                                           'provider_id', 'care_site_id', 'visit_source_concept_id']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO visit_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        con.commit()
        con.close()
        print('Table visit built')

        # Table drug
        con = sqlite3.connect(db_path)
        query = """
                CREATE TABLE drug_evl
                (
                    drug_exposure_id INT,
                    person_id INT,
                    drug_concept_id INT,
                    drug_exposure_start_date VARCHAR(14),
                    drug_exposure_end_date VARCHAR(14),
                    quantity INT
                )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'drug_exposure.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['drug_exposure_id', 'person_id', 'drug_concept_id', \
                                           'drug_exposure_start_date', 'drug_exposure_end_date', 'quantity']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO drug_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        con.commit()
        con.close()
        print('Table drug built')

        # TABLE measurement
        con = sqlite3.connect(db_path)
        query = """
                CREATE TABLE measurement_evl
                (
                    measurement_date CHAR(10),
                    person_id INT,
                    value_as_number DECIMAL(11,4),
                    measurement_concept_id INT
                )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'measurement.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['measurement_date', 'person_id',
                                           'value_as_number', 'measurement_concept_id']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                try:
                    msm_id = float(field[name.index('measurement_concept_id')])
                    if msm_id in measurement_list:
                        c.execute("INSERT INTO measurement_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
                except:
                    pass
        con.commit()
        con.close()

        # TABLE procedure
        conn = sqlite3.connect(db_path)
        query = """
            CREATE TABLE procedure_evl
            (
                person_id INT,
                procedure_concept_id INT,
                procedure_date VARCHAR(14)
            )
                """
        c = conn.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'procedure_occurrence.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['person_id', 'procedure_concept_id', 'procedure_date']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO procedure_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        conn.commit()
        conn.close()

        # build table observation
        con = sqlite3.connect(db_path)
        query = """
                CREATE TABLE observation_evl
                (
                    person_id INT,
                    observation_date CHAR(14),
                    observation_concept_id INT
                )
                """
        c = con.cursor()
        c.execute(query)
        # load data from csv files
        with open(evl_path + 'observation.csv') as f:
            reader = csv.reader(f)
            name = next(reader, None)
            idx = [name.index(c) for c in ['person_id', 'observation_date', 'observation_concept_id']]
            question_marks = str((query.count('\n')-4)*'?,')[:-1]
            for field in reader:
                c.execute("INSERT INTO observation_evl VALUES"+'('+question_marks+')', [field[i] for i in idx])
        con.commit()
        con.close()

        # TABLE last_visit
        con = sqlite3.connect(db_path)
        query = """
                create table last_date_evl as

                    with t1 as (
                    select person_id, condition_start_date as date from condition_evl
                    union
                    select person_id, drug_exposure_start_date as date from drug_evl
                    union
                    select person_id, measurement_date as date from measurement_evl
                    union
                    select person_id, max(visit_start_date, visit_end_date) as date from visit_evl
                    union
                    select person_id, procedure_date as date from procedure_evl
                    )

                    select person_id, max(t1.date) as last_visit
                    from t1
                    group by person_id

                """
        c = con.cursor()
        c.execute(query)
        con.commit()
        con.close()
        print('Table last_date built')

    def predict(self):
        # patient dict
        con = sqlite3.connect(db_path)
        query = """
                select distinct person_id
                from person_evl
                """

        df_person = pd.read_sql_query(query, con)
        con.commit()
        con.close()
        ary_person = df_person.person_id.values
        person_index = {ary_person[i]:i for i in range(ary_person.shape[0])}

        # add diagnosis to features
        ary_person_icd9_section = np.zeros([len(person_index), 116*5], dtype=np.uint16)
        ary_person_cod = np.zeros([len(person_index), 44*5], dtype=np.uint16)
        ary_person_ob = np.zeros([len(person_index), 34], dtype=np.uint16)
        con = sqlite3.connect(db_path)
        query = """
                select cd.person_id, cd.condition_concept_id,
                case when cc.vocabulary_id = 'ICD9CM' then cc.concept_code else ci.icd9cm end as icd9,
                JulianDay(lv.last_visit) - JulianDay(cd.condition_start_date) to_last_visit
                from condition_evl cd, last_date_evl lv
                left outer join concept_icd9 ci
                on cd.condition_concept_id = ci.concept_id
                left outer join concept cc
                on cd.condition_source_concept_id == cc.concept_id
                where cd.person_id = lv.person_id
                """
        c = con.cursor()
        c.execute(query)
        count, err_1 = 0, 0
        icd9_chapters = []
        icd9_sections = []
        for row in c:
            if row[1] == '': continue
            count += 1
            # assign time_chunk: 1 week -> 0; 1 month -> 1; 3 month -> 2: ...
            days_to_last = row[3]
            time_chunk = 4
            if days_to_last <= 7:
                time_chunk = 0
            elif days_to_last <= 30:
                time_chunk = 1
            elif days_to_last <= 90:
                time_chunk = 2
            elif days_to_last <= 180:
                time_chunk = 3
            # find icd9 section
            _, section = icd_chapter_section(str(row[2]))
            # if disease is a candidate of death
            idx_cod = cause_of_death_disease(str(row[2]))
            if idx_cod != -1:
                ary_person_cod[person_index[row[0]], time_chunk*44+idx_cod] += 1
            # add observation
            idx_ob = other_icd9(str(row[2]))
            if idx_ob != -1:
                ary_person_ob[person_index[row[0]], idx_ob] = 1
            # add to icd9 section
            ary_person_icd9_section[person_index[row[0]], time_chunk*116+section] += 1
        con.commit()
        con.close()
        print('Diagnosis added')

        # add observation to features
        con = sqlite3.connect(db_path)
        query = """
                select ob.person_id, ci.icd9cm
                from observation_evl ob, concept_icd9 ci
                where ci.concept_id = ob.observation_concept_id
                """
        c = con.cursor()
        c.execute(query)
        count = 0
        for row in c:
            count += 1
            if row[1] == '':
                ary_person_ob[person_index[row[0]], 33] += 1
            idx_ob = other_icd9(str(row[1]))
            if idx_ob != -1:
                ary_person_ob[person_index[row[0]], idx_ob] = 1
        con.commit()
        con.close()
        print('Observation added')

        # map drug id to atc code
        con = sqlite3.connect(db_path)
        c = con.cursor()
        c.execute('select distinct concept_code from drug_atc')
        lst_atc = []
        for r in c:
            lst_atc.append(r[0])
        con.commit()
        con.close()
        # add drug to features
        ary_person_drug_atc = np.zeros([len(person_index), 268*5], dtype=np.uint16)
        con = sqlite3.connect(db_path)
        query = """
                select d.person_id, d.drug_concept_id, a.concept_code,
                JulianDay(lv.last_visit) - JulianDay(d.drug_exposure_start_date) to_last_visit
                from drug_evl d, drug_atc a, last_date_evl lv
                where a.descendant_concept_id == d.drug_concept_id
                and d.person_id = lv.person_id
                """
        c = con.cursor()
        c.execute(query)
        count, err = 0, 0
        icd9_chapters = []
        icd9_sections = []
        for row in c:
            count+=1
            days_to_last = row[3]
            if days_to_last <= 7:
                time_chunk = 0
            elif days_to_last <= 30:
                time_chunk = 1
            elif days_to_last <= 90:
                time_chunk = 2
            elif days_to_last <= 180:
                time_chunk = 3
            else:
                time_chunk = 4
            ary_person_drug_atc[person_index[row[0]], time_chunk*268+lst_atc.index(row[2])] += 1
        con.commit()
        con.close()
        print('Drug added')

        # build matrix for demographics
        ary_person_demo = np.zeros([len(person_index), 5])-1
        con = sqlite3.connect(db_path)
        query = """
                select p.person_id, p.gender_concept_id, p.year_of_birth, t.last_visit,
                p.ethnicity_concept_id, t.visit_concept_id
                from person_evl p,(
                select person_id, max(visit_start_date) as last_visit, visit_concept_id
                from visit_evl
                group by person_id
                ) as t
                where p.person_id = t.person_id
                """
        c = con.cursor()
        c.execute(query)
        count, age_err = 0, 0
        for row in c:
            # gender
            if row[1] == 8507:
                ary_person_demo[person_index[row[0]], 0] = 0
            elif row[1] == 8532:
                ary_person_demo[person_index[row[0]], 0] = 1
            # ethnicity
            if row[4] == 8515:
                ary_person_demo[person_index[row[0]], 2] = 0
            elif row[4] == 8516:
                ary_person_demo[person_index[row[0]], 2] = 1
            elif row[4] == 8527:
                ary_person_demo[person_index[row[0]], 2] = 2
            elif row[4] == 8552:
                ary_person_demo[person_index[row[0]], 2] = 3
            elif row[4] == 8557:
                ary_person_demo[person_index[row[0]], 2] = 4
            elif row[4] == 8657:
                ary_person_demo[person_index[row[0]], 2] = 5
            try:
                ary_person_demo[person_index[row[0]], 1] = int(parser.parse(row[3]).year) - int(row[2]) #age
            except:
                age_err += 1
            ary_person_demo[person_index[row[0]], 3] = row[5] # last visit type
            ary_person_demo[person_index[row[0]], 4] = int(parser.parse(row[3]).year) # last visit_year
            count += 1
        con.commit()
        con.close()
        print('Demographics added')

        # add measurement to features
        ary_person_measure = np.zeros([len(person_index), 127], dtype=np.float16)-1
        con = sqlite3.connect(db_path)
        query = open("measurement_evl_query.txt", "r").read()
        c = con.cursor()
        c.execute(query)
        count = 0
        for row in c:
            for i in range(1,len(row)):
                if row[i] is not None and row[i] is not '':
                    try:
                        ary_person_measure[person_index[row[0]], i-1] = row[i]
                    except:
                        pass
            count += 1
        con.commit()
        con.close()
        print('Measurement added')

        # add procedure to features
        ary_person_proc = np.zeros([len(person_index), 31*5], dtype=np.uint16)
        con = sqlite3.connect(db_path)
        query = """
                select p.person_id,c.concept_code,
                JulianDay(lv.last_visit) - JulianDay(p.procedure_date) to_last_visit
                from procedure_evl p, cpt4 c, last_date_evl lv
                where p.procedure_concept_id = c.concept_id
                and lv.person_id = p.person_id
                """
        c = con.cursor()
        c.execute(query)
        count = 0
        for row in c:
            count += 1
            # assign time_chunk: 1 week -> 0; 1 month -> 1; 3 month -> 2: ...
            days_to_last = row[2]
            time_chunk = 4
            if days_to_last <= 7:
                time_chunk = 0
            elif days_to_last <= 30:
                time_chunk = 1
            elif days_to_last <= 90:
                time_chunk = 2
            elif days_to_last <= 180:
                time_chunk = 3
            # add to array
            cpt = proc_cpt4(str(row[1]))
            ary_person_proc[person_index[row[0]], time_chunk*31+cpt] += 1
        con.commit()
        con.close()
        print("Procedure added!")

        # build evaluation array
        evl_sparse = sparse.csr_matrix(ary_person_measure)
        del ary_person_measure
        sparse_dgx = sparse.csr_matrix(ary_person_icd9_section)
        sparse_drug = sparse.csr_matrix(ary_person_drug_atc)
        sparse_demo = sparse.csr_matrix(ary_person_demo)
        sparse_cod = sparse.csr_matrix(ary_person_cod)
        sparse_ob = sparse.csr_matrix(ary_person_ob)
        sparse_proc = sparse.csr_matrix(ary_person_proc)
        del ary_person_demo, ary_person_drug_atc, ary_person_icd9_section, ary_person_cod, ary_person_ob, ary_person_proc
        gc.collect()
        evl_sparse = sparse.hstack((evl_sparse, sparse_dgx, sparse_demo, sparse_drug, sparse_cod, sparse_ob, sparse_proc),
                                   format='csr')
        del sparse_demo, sparse_drug, sparse_dgx, sparse_ob, sparse_cod, sparse_proc
        gc.collect()

        # load model and predict
        lgb_model = lgb.Booster(model_file='/model/model.txt')
        output = pd.DataFrame(lgb_model.predict(evl_sparse.astype('float32')),columns=['score'])
        output_prob = pd.concat([df_person.person_id,output],axis=1)
        output_prob.to_csv('/output/predictions.csv', index = False)

if __name__ == '__main__':
    print('This is the final model!')
    op = OmopParser_predict()
    op.build_database()
    op.predict()
