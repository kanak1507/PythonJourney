
sample_dict = {}

dict_functions = [func for func in dir(sample_dict) if not func.startswith("__")]

print("--- Clean List of Dictionary Methods ---")
for func in dict_functions:
    print(f"- {func}()")

print("\n--- Summary Table of All 11 Dictionary Methods ---")

demo = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(f"Original Dictionary: {demo}")
print(f"keys():             {list(demo.keys())}")
print(f"values():           {list(demo.values())}")
print(f"items():            {list(demo.items())}")
print(f"get('brand'):       {demo.get('brand')}")
