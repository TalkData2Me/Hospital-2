
import pandas as pd
import os
import numpy as np

cleaveland = pd.read_csv(os.path.join('.','data','processed.cleveland.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
hungarian = pd.read_csv(os.path.join('.','data','reprocessed.hungarian.data'),sep=' ',names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
switzerland = pd.read_csv(os.path.join('.','data','processed.switzerland.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
va = pd.read_csv(os.path.join('.','data','processed.va.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])


for location in ['cleaveland','hungarian','switzerland','va']:
    cleaveland[location]=0
    hungarian[location]=0
    switzerland[location]=0
    va[location]=0

cleaveland['cleaveland']=1
hungarian['hungarian']=1
switzerland['switzerland']=1
va['va']=1

processedData = pd.concat([cleaveland,hungarian,switzerland,va])

processedData['chol'] = processedData.apply(lambda x: x.chol if x.chol > 0 else np.nan, axis=1)
processedData['pain'] = processedData.apply(lambda x: 0 if x.cp == 4 else 1, axis=1)
processedData['restecg_normal'] = processedData.apply(lambda x: 1 if x.restecg == 0 else 0, axis=1)
processedData['restecg_sttabnormal'] = processedData.apply(lambda x: 1 if x.restecg == 1 else 0, axis=1)
processedData['restecg_venthypertrophy'] = processedData.apply(lambda x: 1 if x.restecg == 2 else 0, axis=1)
processedData['slope_upsloping'] = processedData.apply(lambda x: 1 if x.slope == 1 else 0, axis=1)
processedData['slope_flat'] = processedData.apply(lambda x: 1 if x.slope == 2 else 0, axis=1)
processedData['slope_downsloping'] = processedData.apply(lambda x: 1 if x.slope == 3 else 0, axis=1)
processedData['thal_normal'] = processedData.apply(lambda x: 1 if x.thal == 3 else 0, axis=1)
processedData['thal_fixed'] = processedData.apply(lambda x: 1 if x.thal == 6 else 0, axis=1)
processedData['thal_reversible'] = processedData.apply(lambda x: 1 if x.thal == 7 else 0, axis=1)
processedData['heart_disease'] = processedData.apply(lambda x: 0 if x.thal == 0 else 1, axis=1)
