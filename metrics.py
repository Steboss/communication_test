import json, random

print("Hello")
metrics = {"tflops_per_sec": round(random.uniform(10,20),2)}
print(f"tflops_per_sec: {metrics['tflops_per_sec']}")
with open('metrics.json', 'w') as ifile:
    json.dump(metrics, ifile)
