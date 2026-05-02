SEED_NUM = 8
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "BRUNO MARS"
LOCAL_HAZARD = "FLOOD"
CONTROL_NUM = max(3, SEED_NUM)
from collections import defaultdict, Counter

# Step 1: Base stream
stream = [
    ("TUP Manila", "BSECE"), 
    ("TUP Taguig", f"BSME_v{CONTROL_NUM}"), 
    ("TUP Manila", f"BSME_v{CONTROL_NUM}"), 
    ("TUP Manila", "BSECE"), 
    ("TUP Visayas", STUDENT_MAJOR), 
    ("TUP Taguig", "BSECE"), 
    ("TUP Manila", "BSECE")
]

# Step 2: Add (CONTROL_NUM + 3) = 7 entries
stream.extend([
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", "BSEE"),
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", "BSIT"),
    ("TUP Manila", "BSME_v4"),
    ("TUP Taguig", "BSECE"),
    ("TUP Manila", "BSECE")
])

# Step 3: Aggregate
campus_data = defaultdict(list)

for campus, program in stream:
    campus_data[campus].append(program)

# Step 4: Count frequencies
manila_counter = Counter(campus_data["TUP Manila"])

# Step 5: Get most common
top_program = manila_counter.most_common(1)


# Output
print("CONTROL_NUM:", CONTROL_NUM)
print("Expanded Stream Length:", len(stream))
print("Manila Data:", campus_data["TUP Manila"])
print("Top Program:", top_program)

print("Total Applications Processed for TUP Manila:", len(campus_data["TUP Manila"]))

top = manila_counter.most_common(1)[0]

print("Top Requested Program at TUP Manila:", top[0])
print("Exact Frequency of Top Program:", top[1])
