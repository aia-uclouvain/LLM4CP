import os
import re

# Root folder
root = "Problems"

# Allowed extensions
allowed_exts = {".essence", ".py", ".mzn", ".pi", ".pl", ".eprime", ".cpp",
                ".epl", ".cs", ".lp4", ".mod", ".xcsp", ".java", ".c", ".cc", ".co", ".scala"}

# Track ignored extensions globally
ignored_exts = set()

# Walk through each probxxx folder
for prob_folder in sorted(os.listdir(root)):
    prob_path = os.path.join(root, prob_folder)
    if not os.path.isdir(prob_path):
        continue

    spec_file = os.path.join(prob_path, "specification.md")
    if not os.path.exists(spec_file):
        continue

    # --- Step 1: get the title
    with open(spec_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("Title:"):
                title = line.split(":", 1)[1].strip()
                break
        else:
            continue  # no Title found

    # format title
    title_clean = title.lower().replace(" ", "_")

    # --- Step 2: process models folder
    models_dir = os.path.join(prob_path, "models")
    if not os.path.isdir(models_dir):
        continue

    # Output file at same level as Problems
    out_file = os.path.join(os.path.dirname(root), f"{title_clean}.txt")

    model_files = [f for f in os.listdir(models_dir)
                   if os.path.isfile(os.path.join(models_dir, f))]

    with open(out_file, "w", encoding="utf-8") as out:
        counter = 1
        for mf in model_files:
            ext = os.path.splitext(mf)[1]
            if ext in allowed_exts:
                out.write(f"{counter}) IMPLEMENTATION IN {ext}\n")
                with open(os.path.join(models_dir, mf), "r", encoding="utf-8", errors="ignore") as infile:
                    out.write(infile.read())
                out.write("\n\n")
                counter += 1
            else:
                ignored_exts.add(ext)

# --- Step 3: print ignored extensions once globally
print("Ignored extensions:", ignored_exts)
