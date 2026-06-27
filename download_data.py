from supabase import create_client
import os

SUPABASE_URL = "https://wvhgrlaxoihijgutoxyp.supabase.co"
SUPABASE_KEY = "your_key_here"  # ใส่ key จริงครับ
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

LABELS = ["raw", "ripe", "overripe"]

for label in LABELS:
    os.makedirs(f"data/{label}", exist_ok=True)
    files = supabase.storage.from_("audio-feedback").list(label)
    for f in files:
        filename = f["name"]
        data = supabase.storage.from_("audio-feedback").download(f"{label}/{filename}")
        with open(f"data/{label}/{filename}", "wb") as out:
            out.write(data)
        print(f"Downloaded: {label}/{filename}")

print("Done!")
