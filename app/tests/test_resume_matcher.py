from analysis.resume_matcher import get_resume_and_jd

resume, jd = get_resume_and_jd("Amazon")

print("RESUME")
print("=" * 50)

for doc in resume["documents"]:
    print(doc[:200])
    print()

print("\nJOB DESCRIPTION")
print("=" * 50)

for doc in jd["documents"]:
    print(doc[:200])
    print()