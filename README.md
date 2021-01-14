# A-LightGBM-Model-to-Predict-180-Days-Mortality-Using-EHR-Data

#### Jifan Gao<sup>1,2</sup>, Guanhua Chen<sup>1,2</sup>
<sup>1</sup> Department of Biostatistics and Medical Informatics, University of Wisconsin-Madison, Madison, Wisconsin, USA
<sup>2</sup> Contact: J.G. (jifan.gao@wisc.edu), G.C. (gchen25@wisc.edu)


>### Abstract
> We build a mortality risk prediction model based on LightGBM, with a dimensional reduction strategy tailored for sparse and longitudinal EHR data. 

## Background/Introduction
The aim of the EHR DREAM Challenge is to predict the mortality status of patients within 180 days of their last visit using their EHR data. The data collected spans 10 years from 2009 to 2019 and contains up to hundreds of thousands of unique concepts for millions of patients. For the feature generation/extraction part, we map each of these concepts to a category in medical terminology vocabularies (mega concepts) which have a limited number of cardinalities to reduce the dimensionality of the features. These mega concepts include ICD-9 (International Statistical Classification of Diseases 9th Revision), ATC (Anatomical Therapeutic Chemical), and CPT (Current Procedural Terminology). For the model part, we use LightGBM, a novel type of Gradient Boosting Decision Tree algorithm, proposed by Guolin Ke et al. in 2016 [1].  In this project, we train and tune a LightGBM to predict the mortality risk of each patient by using mega concepts as input features.

## Methods
### Feature Generation
We map each event in clinical findings (including diagnosis and symptoms), drug exposure, and procedure occurrence to medical terminology in ICD-9, ATC, and CPT, respectively. Such mapping information is available to download from the [OHDSI](http://athena.ohdsi.org/search-terms/terms) and [NIH](https://www.nlm.nih.gov/research/umls/mapping_projects/icd9cm_to_snomedct.html) websites. For clinical findings, their concept IDs are first mapped to an ICD-9 code and then mapped to the corresponding ICD-9 subgroup. For drug exposure, the drug IDs are first mapped to an ATC code and then mapped to the corresponding ATC pharmacological subgroup. For procedure occurrence, the procedure occurrence IDs are first mapped to a CPT code and then mapped to the corresponding CPT subgroup. For each patient, we count the occurrence of each of the ICD-9/ATC/CPT subgroups. In addition, we also count the ICD-9 codes of diseases that cause most deaths according to reports from the CDC (Center for Disease Control and Prevention) [3]. Such strategies lead to 459 features/mega concepts. 
<br/> 
To take into account the longitudinal data information in the EHR, we create five time frames with various lengths and summarize the occurrence of events within each time frame. Hence, there are five sets of these 459 mega concepts, one for each time frame. We also compute means and most recent values of selected measurements [4]. Combining these features with other time-invariant information such as demographics, lifestyle, and disease history, a total of 2460 features are generated through this process. See Figure 1 for illustration.
<br/> <br/> 
![](https://github.com/GGGGFan/A-LightGBM-Model-to-Predict-180-Days-Mortality-Using-EHR-Data/blob/main/images/ehr_1.png)
<br/>
### Missing label imputation
As is described in the [Challenge Website](https://www.synapse.org/#!Synapse:syn18405991/wiki/595494), some of the patients’ mortality status (label) is missing in the training data. Hence, there is a need to impute the missing labels. Among all strategies we have tried,  the model produces the best AUROC results when all of these missing labels are set to be negative.
### Sample Reweighting
To take into account the potential time trend of mortality among patients in the EHR, we encourage our model to perform well for more recent patients. In particular, patients whose last visits are closer to the current date will be assigned a larger weight in the training process, whereas patients whose last visits are earlier will be assigned a smaller weight. The pseudo-labeled patients have weights of 1. The weights for those who are guaranteed to have a true label are computed as below:
<br/>
![](https://github.com/GGGGFan/A-LightGBM-Model-to-Predict-180-Days-Mortality-Using-EHR-Data/blob/main/images/ehr_2.png)
<br/>
Note that patients, whose last visit is before 2018-09-01 12:00 am, are guaranteed to have a true label. *JulianDay(some DateTime)* returns the DateTime as a Julian Day, which is convenient for computation of DateTime in YYYY-MM-DD Time format.
### Training/Validation Split
In order to validate the model’s “future-proof” ability, we order the labeled patients by their last visit date from recent to early and use the top 15% of patients for validation.
### Model Tuning
We use Optuna [2] to enable automatic hyper-parameter tuning. AUROC is used as the stop criteria.
## Discussion
We build a mortality risk prediction model based on LightGBM, with a dimensional reduction strategy tailored for sparse and longitudinal EHR data. The model achieves the highest AUROC and AUPR on the validation data, which are 0.9470 and 0.4779, respectively.<br/>
Although our ontology-rollup strategy may lose variations of concepts within a group, the AUROC and AUPR results indicate that the overarching concepts can be represented by such a strategy. Compared with our latest model in the Leaderboard Phase, we add measurement features to our final model in the Validation Phase. Considering that the final model achieves highest AUROC and AUPR with the validation data, it is reasonable to believe our strategy of ontology-rollup, time binning and sample reweighting could potentially handle the data drift between the EHR datasets in the Leaderboard Phase and the Validation Phase. The importance of measurement features reflects that taking vital signs and lab results into more consideration may help to improve the performance of mortality risk prediction models.
## References
[1] Ke G, Meng Q, Finley T, et al. Lightgbm: A highly efficient gradient boosting decision tree[C]//Advances in neural information processing systems. 2017: 3146-3154.<br/>
[2] Akiba T, Sano S, Yanase T, et al. Optuna: A next-generation hyperparameter optimization framework[C]//Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2019: 2623-2631.<br/>
[3] Kochanek K D, Murphy S L, Xu J, et al. Deaths: final data for 2017[J]. 2019.<br/>
[4] Blodgett J M, Theou O, Howlett S E, et al. A frailty index from common clinical and laboratory tests predicts increased risk of death across the life course[J]. GeroScience, 2017, 39(4): 447-455.<br/>
## Author Contributions
J.G. and G.C. designed the model and wrote the paper. J.G. implemented the code and conducted the analysis.
