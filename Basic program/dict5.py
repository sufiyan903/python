Cricketer = {
    "VinayKumar": {102, 5},
    "Yuzvendra Chahal": {89, 10},
    "Sandeep Sharma": {95, 8},
    "Umesh Yadav": {85, 6},
    "BhuvaneswarKumar": {106, 10},
    "Basil Thampi": {70, 5}
}

# Calculate the bowling average and update the dictionary
for cricketer, stats in Cricketer.items():
    total_runs, wickets = stats
    bowling_average = total_runs / wickets
    Cricketer[cricketer] = {bowling_average}

# Sort the dictionary based on the bowling average
sorted_Cricketer = dict(sorted(Cricketer.items(), key=lambda x: x[1]))

print(sorted_Cricketer)
