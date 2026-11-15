import argparse, os, random, yaml, pandas as pd
from faker import Faker

fake = Faker(); Faker.seed(42); random.seed(42)   # same "random" data every run

def make_value(spec, keys):
    """Make one fake value for a column, based on the recipe card."""
    if "ref" in spec:                         # link to a row in another table
        table, _ = spec["ref"].split(".")
        return random.choice(keys[table])
    if "choices" in spec:                     # pick from a list
        return random.choice(spec["choices"])
    if "min" in spec:                         # random number in a range
        return round(random.uniform(spec["min"], spec["max"]), 2)
    return getattr(fake, spec["fake"])()      # e.g. fake.name(), fake.city()

def add_dirty_data(df, pk, date_cols):
    """Add mistakes on purpose, like real-world data."""
    df = pd.concat([df, df.sample(frac=0.02, random_state=1)], ignore_index=True).astype(object)  # 2% duplicate rows
    df.loc[df.sample(frac=0.01, random_state=2).index, pk] = None                               # 1% missing IDs
    for c in date_cols:
        df.loc[df.sample(frac=0.01, random_state=3).index, c] = "2025-13-45"                    # 1% impossible dates
    return df

def main(industry):
    cfg = yaml.safe_load(open(f"config/{industry}.yaml"))
    os.makedirs("data", exist_ok=True)
    keys = {}                                 # remembers IDs so other tables can link to them
    for name, t in cfg["tables"].items():
        df = pd.DataFrame([{c: make_value(s, keys) for c, s in t["columns"].items()}
                           for _ in range(t["rows"])])
        keys[name] = df[t["primary_key"]].tolist()
        date_cols = [c for c, s in t["columns"].items() if s["type"] == "DATE"]
        dirty = add_dirty_data(df, t["primary_key"], date_cols)
        dirty.to_csv(f"data/{industry}_{name}.csv", index=False)
        print(f"{name}: {len(df)} rows + {len(dirty) - len(df)} duplicates, with errors added")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--industry", required=True)
    main(p.parse_args().industry)