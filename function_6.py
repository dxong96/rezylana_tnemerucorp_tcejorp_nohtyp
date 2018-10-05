import data_holder

def agencyamt(category):
    '''search parametres go here'''

    technology = ['Technology', 'Media', 'Communications']
    transport = ['Transport']
    government = ['Prime Minister', 'Parliament']
    law = ['Attorney', 'Law', 'Judiciary']
    publicService = ['Social', 'Fund', 'Culture', 'Family', 'Energy', 'Intellectual', 'Manpower', 'Arts', 'National',
                     'Parks', 'Utilities', 'Workforce', 'Tote', 'Labor']
    finance = ['Accounting', 'Auditor', 'Commission','Project', 'Casino', 'Economic', 'Finance', 'Enterprise', 'Revenue'
        , 'Trade']
    clubs = ['Aviation', 'Istana', 'Corporation', 'Islam', 'Heritage', 'Library', 'Productivity', 'Rehabilitative',
             'Sports']
    health = ['Food', 'Health']
    housing = ['Estate', 'Housing', 'Redevelopment', 'Land']
    maritime = ['Maritime']
    education = ['Education', 'Polytechnic', 'College', 'Examinations', 'School', 'Institute', 'University', 'Science',
                 'SkillsFuture']
    defence = ['Defence']


    '''storing lists go here'''

    technologyList = []
    transportList = []
    governmentList = []
    financeList = []
    clubsList = []
    maritimeList = []
    educationList = []
    lawList = []
    healthList = []
    housingList = []
    defenceList = []
    publicServiceList = []
    agency_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'agency')

    agency_to_awarded_amt = {}
    # convert the list of procurement to awarded amount
    for agency in agency_to_procurements:
        agency_to_awarded_amt[agency] = sum([p.awarded_amt for p in agency_to_procurements[agency]])

        if has_any_word_in_sentence(agency, law):
            lawList.append(agency_to_awarded_amt[agency])
        elif has_any_word_in_sentence(agency, defence):
            defenceList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, publicService):
            publicServiceList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, technology):
            technologyList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, transport):
            transportList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, government):
            governmentList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, finance):
            financeList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, clubs):
            clubsList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, maritime):
            maritimeList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, education):
            educationList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, health):
            healthList.append(agency_to_awarded_amt[agency])
        elif  has_any_word_in_sentence(agency, housing):
            housingList.append(agency_to_awarded_amt[agency])

    if category == 'Law':
        totalspend = sum(lawList)
        return totalspend
    elif category == 'Defence':
        totalspend = sum(defenceList)
        return totalspend
    elif category == 'Public Service':
        totalspend = sum(publicServiceList)
        return totalspend
    elif category == 'Technology':
        totalspend = sum(technologyList)
        return totalspend
    elif category == 'Transport':
        totalspend = sum(transportList)
        return totalspend
    elif category == 'Government':
        totalspend = sum(governmentList)
        return totalspend
    elif category == 'Finance':
        totalspend = sum(financeList)
        return totalspend
    elif category == 'Clubs':
        totalspend = sum(clubsList)
        return totalspend
    elif category == 'Maritime':
        totalspend = sum(maritimeList)
        return totalspend
    elif category == 'Education':
        totalspend = sum(educationList)
        return totalspend
    elif category == 'Health':
        totalspend = sum(healthList)
        return totalspend
    elif category == 'Housing':
        totalspend = sum(housingList)
        print totalspend
        return totalspend

def function_6(category):
    result = agencyamt(category)
    return 'Amount spent for %s is: %f' % (category, result)


def has_any_word_in_sentence(sentence, words):
    for word in words:
        if word in sentence:
            return True
    return False




