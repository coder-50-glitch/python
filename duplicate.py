std_data={'id1':
    {'Name':['SARA'], 
    'class':['VI'],
    'subject_intigration':['eng, Math, Comp']
    },
'id2':
    {'Name':['DAVID'], 
    'class':['V'],
    'subject_intigration':['eng, Math, Comp']

    },
'id3':
    {'Name':['Tara'], 
    'class':['VI'],
    'subject_intigration':['eng, Math, Comp']
    },
'id4':
    {'Name':['SARA'], 
    'class':['IV'],
    'subject_intigration':['eng, Math, Comp']
    },
}
res={}
for key,values in std_data.items():
    if values not in res.values():
        res[key]=values
print(res)