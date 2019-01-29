states = {
    "CA": "California",
    "VA": "Virgina",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045  # 39,557,045
    },
    "VA": {
        "NAME": "Virgina",
        "POPULATION": 8500000  # 8,500,000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718   # 6,042,718
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,032,392
    }
}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045,   # 39,557,045
        "CITIES": [
            "Fresno"
            "San Francisco"
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virgina",
        "POPULATION": 8500000, # 8,500,000
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexadria"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,   # 6,042,718
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,  # 1,057,315
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392,  # 3,032,392
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}
print(complex_dictionary["RI"]["CITIES"][2])