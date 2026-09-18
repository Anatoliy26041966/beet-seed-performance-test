import csv
import json
import subprocess

def fetch_classroom_courses():
    print("Отримання активних курсів з Google Classroom...")
    cmd = "gam print courses states ACTIVE fields id,name,section,alternateLink"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    courses = []
    lines = result.stdout.strip().split("\n")
    if len(lines) > 1:
        reader = csv.DictReader(lines)
        for row in reader:
            courses.append({
                "id": row.get("id", ""),
                "name": row.get("name", ""),
                "section": row.get("section", ""),
                "link": row.get("alternateLink", "")
            })
            
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
        
    print(f"Успішно збережено {len(courses)} курсів у courses.json (без кодів приєднання).")

if __name__ == "__main__":
    fetch_classroom_courses()
