# 3.2.2: Run a Python file in the command line or VS Code
print("Hello World!")

# 3.2.4: Preform Calculations
## Mathemantical Expression
print(5+2*3)
print(8//5-3)
print(8+22*2-4)
print(16-3/2+7-1)
print(3**3%5)
print(5+9*3/2-4)

## Grouping with Parantheses Mathematical Expression
print((5+2)*3)
print((8//5)-3)
print(8+(22*(2-4)))
print(16-3/(2-7)-1)

## Compare 
print(5+(9*3/2-4))
print(5+(9*3/(2-4)))

# 3.2.5: Create and add to List
## Data Structures: Lists
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)

print(counties[0])

print(counties[2])
print(counties[-1])
print(len(counties))

print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])

## Add Item to A List
counties.append("El Paso")
counties.insert(2, "El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

## Change an Element in a List
counties[2] = "El Paso"
print(counties)

# 3.2.7: Create and add keys and values to a dictionary
## Data Structures: Dictionaries 

counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

print(len(counties_dict))
counties_dict.items()
counties_dict.keys()
counties_dict.values()

counties_dict.get("Denver")
counties_dict['Arapahoe']
counties_dict["Arapahoe"]

## List of Dictionaries

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_votes": 463353})
voting_data.append({"county": "Jefferson", "registered_votes": 432438})
print(voting_data)

# 3.2.8: Decision Statements
## How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
## Total votes in the election 
total_votes = int(input("What is the total votes in the election?"))
## Calculate the percentage of votes you received 
percentage_votes = (my_votes/total_votes)*100
print("I received" + str(percentage_votes)+ "% of the total votes.")

# If Statements
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


## What is the score?
score = int(input("What is your test score?"))
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is a F.')

# 3.2.9: Membership and Logical Operators
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# 3.2.10: Repetetion Statements
x = 0
while x<=5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "regitered_voters": 432438}]
            
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
    
for county_dict in voting_data:
    print(county_dict['county'])

# 3.2.11: Printing Formats
my_votes= int(input("How many votes did you get the electon?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes / total_votes) * 100
print("I received" + str(percentage_votes)+ "% of the total votes.")

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100} % of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered_voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f" You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes/ total_votes * 100}% of the total votes.")
print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
