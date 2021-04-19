
# coding: utf-8

# In[620]:

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt  
import matplotlib
import numpy as np
import urllib
from scipy.stats import pearsonr
import sys
import math


# In[674]:

sys.stdout = open("logoutput.txt", "a")


# # Get command line params

# file_suffix = 'power'
# filepath_data_items = 'commondata_items_notools_powerusers.csv'
# filepath_users_items = 'powerusers_e.csv'

# In[671]:

# parameters to configure the printing the indicators files 
file_suffix =  sys.argv[1] #'tenusers'#sys.argv[1] # power #10 #sys.argv[1] 
filepath_data_items = sys.argv[2] #'commondata_tentestusers.csv'#'testdatamanual.csv'#'commondata_items_notools_weakusers_2305.csv'#sys.argv[2] 
filepath_users_items = sys.argv[3] #'userdata_2305_notoolsitemsdata.csv'#'weakusers_e_notools_2305.csv' #sys.argv[3]
sessionormonth = sys.argv[4] # 'wdtmonth'#'wdtmonth'#'session'#sys.argv[4]

#file_suffix = 'weakusers' #sys.argv[1] ''# power #10 #sys.argv[1] 
#filepath_data_items =  'commondata_items_notools_weakusers_2305.csv' #sys.argv[2]
#filepath_users_items = 'weakusers_e_notools_2305.csv' #sys.argv[3]


# # Selecting users

# In[622]:

#revContributor,editCount,lifespan,start,end,gone
users_items = pd.read_csv(filepath_users_items, usecols=[0,1,2,3,4,5])#names = ['revContributor','editCount','lifespan','start','end','gone'])


# In[623]:

# FIRST ONLY NO TOOLS 

#revContributor: int, id of the human editor
#revId: int, id of the edit (or revisions)
#revTimestamp: datetime. time when the edit was done
#year: int, extracted from revTimestamp
#month: int, extracted from revTimestamp
#day: int, extracted from revTimestamp
#revPage: int, id of the page (can be  item page or non item page)
#actionType: int, type of edit (if it's delete, add... following the list of actions I sent before)
#session: int, session computed by me
#isItem: boolean, true if the edit is of a revPage that it is an item page. For now we *always select only edits that are done on item pages, so .loc where isItem == true* 
#isTool


data_items = pd.read_csv(filepath_data_items, usecols=[0,1,2,3,4,5,6,7,8,9],parse_dates=[2]) #header=None,names = ['revContributor','revId','revTimestamp','year','month','day','revPage','actionType','session','isTool']
data_items_notools = data_items.loc[data_items['isTool'] == False] # == 0
#,dtype={'isTool': np.bool}


# In[ ]:




# # Sessions

# In[626]:

# the following code is JUST to give labels to the different Wikidata labels - it would be exactly the same to have YYYY-MM.


# In[627]:

### testing


editsgrouped =data_items_notools.groupby(by=['revContributor'])
#editsgusersession = data_items_notools.groupby(by=['revContributor','session'])

#editsgsession = data_items_notools.groupby(by=['session'])
#print(len(editsgsession.groups))



#######


# In[628]:

editsgrouped.groups


# In[629]:

def indexmonth(row):
    if row['year'] == 2012 and row['month'] == 10 :
        return 0
    if row['year'] == 2012 and row['month'] == 11 :
        return 1
    if row['year'] == 2012 and row['month'] == 12 :
        return 2
    if row['year'] == 2013 and row['month'] == 1 :
        return 3
    if row['year'] == 2013 and row['month'] == 2 :
        return 4
    if row['year'] == 2013 and row['month'] == 3 :
        return 5
    if row['year'] == 2013 and row['month'] == 4 :
        return 6
    if row['year'] == 2013 and row['month'] == 5 :
        return 7
    if row['year'] == 2013 and row['month'] == 6 :
        return 8
    if row['year'] == 2013 and row['month'] == 7 :
        return 9
    if row['year'] == 2013 and row['month'] == 8 :
        return 10
    if row['year'] == 2013 and row['month'] == 9 :
        return 11
    if row['year'] == 2013 and row['month'] == 10 :
        return 12
    if row['year'] == 2013 and row['month'] == 11 :
        return 13
    if row['year'] == 2013 and row['month'] == 12 :
        return 14
    if row['year'] == 2014 and row['month'] == 1 :
        return 15 
    if row['year'] == 2014 and row['month'] == 2 :
        return 16 
    if row['year'] == 2014 and row['month'] == 3 :
        return 17 
    if row['year'] == 2014 and row['month'] == 4 :
        return 18 
    if row['year'] == 2014 and row['month'] == 5 :
        return 19 
    if row['year'] == 2014 and row['month'] == 6 :
        return 20 
    if row['year'] == 2014 and row['month'] == 7 :
        return 21 
    if row['year'] == 2014 and row['month'] == 8 :
        return 22 
    if row['year'] == 2014 and row['month'] == 9 :
        return 23 
    if row['year'] == 2014 and row['month'] == 10 :
        return 24 
    if row['year'] == 2014 and row['month'] == 11 :
        return 25 
    if row['year'] == 2014 and row['month'] == 12 :
        return 26
    if row['year'] == 2015 and row['month'] == 1 :
        return 27 
    if row['year'] == 2015 and row['month'] == 2 :
        return 28 
    if row['year'] == 2015 and row['month'] == 3 :
        return 29 
    if row['year'] == 2015 and row['month'] == 4 :
        return 30 
    if row['year'] == 2015 and row['month'] == 5 :
        return 32 
    if row['year'] == 2015 and row['month'] == 6 :
        return 33    
    if row['year'] == 2015 and row['month'] == 7 :
        return 34 
    if row['year'] == 2015 and row['month'] == 8 :
        return 35 
    if row['year'] == 2015 and row['month'] == 9 :
        return 36 
    if row['year'] == 2015 and row['month'] == 10 :
        return 37 
    if row['year'] == 2015 and row['month'] == 11 :
        return 38 
    if row['year'] == 2015 and row['month'] == 12 :
        return 39
    if row['year'] == 2016 and row['month'] == 1 :
        return 40 
    if row['year'] == 2016 and row['month'] == 2 :
        return 41
    if row['year'] == 2016 and row['month'] == 3 :
        return 42 
    if row['year'] == 2016 and row['month'] == 4 :
        return 43 
    if row['year'] == 2016 and row['month'] == 5 :
        return 44 
    if row['year'] == 2016 and row['month'] == 6 :
        return 45    
    if row['year'] == 2016 and row['month'] == 7 :
        return 46    


# In[630]:

data_items_notools['wdtmonth'] = data_items_notools.apply(lambda row: indexmonth(row),axis=1)


# In[631]:


def slicedf(row):

    revContributor =  row.name#revContributor row.iloc[0]['revContributor'] 
    pcount = len(row.index)  #'pcount'

    groupcontributorselected = row.loc[row[sessionormonth] == sid]
    #print('pcount')
    #print(pcount)
    #print('pcountint')
    #print(pcountint)
    #print('selected slice returning:')
    #print(groupcontributorselected.head(5))
    return groupcontributorselected
    


# In[632]:

# To do the analysis of the X% of the lifestage, we consider only the edits done from the start (i.e. date of the first edit), 
# until the point where the X% of the edits were done. Therefore, we get the subset of the complete data frame, 
# where each user has done the X% of her edits.

def getRangeLifestage(sessionid):
    
    global sid
    sid = sessionid
    #print('entered getRangeLifestage')
    
    df = data_items_notools 
    result = pd.DataFrame()

    
    result = editsgrouped.apply(slicedf)
    
    
          
 
    return result
    
   
   



# # Indicators


# Productivity: volumne of edits


# In[663]:

#i1
def edits(group):

    return len(group)


# In[637]:

#i2
def editsPerItem(group):
    return pd.DataFrame(group.size())[0].mean() 


# In[664]:

#i3
def items(group):
     
    u = group.revPage.nunique()

    return u
 


# In[639]:

#i4automatically:
def timePerSession(group):
  
    # I get here all sessions grouped

    start = pd.to_datetime(group['revTimestamp'].min(),utc=True)
    end = pd.to_datetime(group['revTimestamp'].max(),utc=True)     
    
    difference = (end - start)
             
    
    return difference.total_seconds()
        
    


# In[640]:


def avgEditsPerSession(group):
    return pd.DataFrame(group.size())[0].mean()


# In[641]:


def avgSessionsPerMonth(group):
    #print(type(group['session']))
    #return group['session'].value_counts().size() # value_counts() gives the number of times each session number appears but not per group
    return group.session.nunique().mean() # unique()[0] gets the first row
   


# In[642]:


def avgTimeBetweenSessions(group):
    # group conyearmonthsession
    # the time between only one session is 0.0, there was no gap
    if (len(group) > 1):
    
        starts = pd.to_datetime(group['revTimestamp'].min(),utc=True)
        ends = pd.to_datetime(group['revTimestamp'].max(),utc=True)  

        
        startss = starts.shift(-1,axis=0)
              
        differences = startss - ends
        #print(differences.mean().total_seconds())
        
        
        #.mean().seconds will only give the seconds of the delta
        return float(differences.mean().seconds)
    else:
        
        return 0.0
            
    

    


# In[643]:

# i5
def diversityOfEditTypesInLifestage(group):
    #print(group.head(10))
    count = len(group.index)
    #print('count')
    #print(count)
    valuecounts = group.actionType.value_counts() 
    series = pd.Series()
    for i in valuecounts.index:

        prob = float(valuecounts[i]) / float(count)
        #print('prob')
        #print(prob)
        series.set_value(i,prob)
   
    # print('series')
    # print(series)
    series.reset_index()
    if series.size <= 1:
        return 0.0
    else: 
        e = 0.0
        for j in series.index:
            e -= series.ix[j] * math.log(series.ix[j],2)
        entropy = e / float(len(group)) # normalized by the # edits in that group
    return entropy 


# In[644]:


#def toolsRatioOverEdits(group):
    # groupdf = group.reset_index()
    #  countools = len(pd.DataFrame(group.loc[group['tool'] == True]).index)
    # totaleditseditor = len(group.index)
    # return (countools / totaleditseditor)


# In[690]:

# for each contribitor group this will be executed
def processContributorGroup(group):
    # input contributorgroupname
    #print('entered processContributorGroup - all indicators')
    ##print('group called:')
    #print(group.head(5))
    
    print('+++ group in process contributors+++')
    print(group)
    print('++')
   
    contributor =0
    if group.revContributor.nunique() == 1:  
        contributor_unique = group.revContributor.unique()
        contributor = int(contributor_unique[0])
    else:
        print('!! more than one contributor in the group of one contributor')
    

    resultggrouped_contyearmonth= group.groupby(['revContributor','year','month'])
    resultggrouped_contsession= group.groupby(['revContributor','session'])  
    resultggrouped_contyearmonthitems = group.groupby(['revContributor','year','month','revPage'])   
    resultggrouped_contyearmonthsession = group.groupby(['revContributor','year','month','session'])
  
    resultggrouped_contitem= group.groupby(['revContributor','revPage']) 
   
    
    # value for indicators for a concrete contributor for a particular lifestage
    #--------------------------------------------------------
   
    i1= float(edits(group))
    #print('i1')
    
  
    i2 = float(editsPerItem(resultggrouped_contitem))
    #print('i2')
   

    i3 = float(items(group))
    #print('i3')
    #--------------------------------------------------------
  
    i4 = float(timePerSession(group))
    #print('i4')
   
    i5 = float(diversityOfEditTypesInLifestage(group)) #in general in that time 
    #print('i5')
    

   

    return pd.Series([contributor,sid,i1,i2,i3,i4,i5]) 

    # for each contributor a row with all indicators and upfront the groupid (contributor id)
    
    

# In[691]:


def computeIndicators(namef,lifestagedf,sessionid):
    #print('entered computeIndicators -- main mehod')
    # it reads the file containing the edits relevant for a particular lifestage (e.g. 50%) and computes the counteditspermonth 
    # in that lifestage. Note that there can be edits of multiple years and multiple months in that set. We compute the 
    # AVG edits per month.
    

    #print(sessionids)    #lifestagedf.reset_index()
    
    
    #print('length of lifestagedf')
    #print(len(lifestagedf))
    
    #print(type(percentage))
    result = pd.DataFrame()
    #df = read_csv(name+'.csv',header=None,names=['revContributor','revId','revtimestamp','year','month','day','actiontype', 'session'])
   
    #lifestagedf.empty
    if lifestagedf.empty:
        return 0
    else:
        # create list of results and concat at the end
        # pass to the apply the contributor group, and still monthyear and session will be used for various
        lifestagedfgb = lifestagedf.groupby(['revContributor'])
      
       
        
        
        
        result = lifestagedfgb.apply(processContributorGroup) #x.name gives 'revContributor'        

        ids = pd.Series(list(lifestagedfgb.groups.keys())) #result['revContributor'] since it is grouped is in the index
  
        n = len(lifestagedfgb.groups.keys())
        
        sessions = pd.Series(sessionid for _ in range(n))
        
        resultdf = pd.DataFrame(result.values)
        

        
        resultdf.to_csv(namef+'_allindicators'+'_'+str(file_suffix)+'.csv',header=False,index=False,float_format='%11.6f')

    


# In[692]:

editsgsession = data_items_notools.groupby(by=[sessionormonth])

sessionids = set(editsgsession.groups.keys())

print(sessionids)
print(sessionids)
for sid in sessionids:
    res = getRangeLifestage(sid) #data_items_notools'+str(start)+'_'+str(end generated 01.05
    #print(len(res))
    computeIndicators('data_items_notools_indicators_'+sessionormonth+'_'+str(sid),res,sid) # now the "percentage" in the data frame is basically the upper bound in the batch
    


