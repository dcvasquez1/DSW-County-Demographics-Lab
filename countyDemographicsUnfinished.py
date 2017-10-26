import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first=counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first=c["County"]
    return first
    
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    under_18=counties[0]["Age"]["Percent Under 18 Years"]
    countyName=counties[0]["County"]
    stateName=counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > under_18:
            under_18=c["Age"]["Percent Under 18 Years"]
            countyName=c["County"]
            stateName=c["State"]
    answer=countyName + ", " + stateName
    return answer
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    under_18=counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > under_18:
            under_18=c["Age"]["Percent Under 18 Years"]
    return under_18
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    under_18=counties[0]["Age"]["Percent Under 18 Years"]
    countyName=counties[0]["County"]
    stateName=counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > under_18:
            under_18=c["Age"]["Percent Under 18 Years"]
            countyName=c["County"]
            stateName=c["State"]
    answer=countyName + ", " + stateName + " " + str(under_18) + "%"
    return answer
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    stateDict = dict()
    stateName=counties[0]["State"]
    stateNum=0
    for c in counties:
        if c["State"]==stateName:
            stateNum+=1
            stateDict[stateName]=stateNum
        else:
            stateNum=1
            stateName=c["State"]
            stateDict[stateName]=stateNum
            
    #Find the state in the dictionary with the most counties
    state=counties[0]["State"]
    maxNumCounties=0
    for s in stateDict:
        if stateDict[s]>maxNumCounties:
            state=s
            maxNumCounties=stateDict[state]
    
    #Return the state with the most counties
    return state
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    under_18=counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        under_18+=c["Age"]["Percent Under 18 Years"]
    return "The average percentage of people under 18 across the US is " + str(round(under_18/len(counties), 2)) + "%"
    
if __name__ == '__main__':
    main()
