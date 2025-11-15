# filter_nhts_columns.py
import pandas as pd
import os

# ----------------------------------------------------------------------
# 1. CONFIGURATION – change only these two lines if you want
# ----------------------------------------------------------------------
INPUT_CSV   = "vehpub.csv"      # <-- your merged CSV
OUTPUT_CSV  = "filteredvehpub.csv"    # <-- where the cleaned file goes
# ----------------------------------------------------------------------


# Columns you want to keep (exactly as they appear in the data)
REQUIRED_COLUMNS = [
    'HOUSEID',      # Household ID
    'HHFAMINC',     # Income
    'HHSIZE',       # Household size
    'LIF_CYC',      # Family life cycle
    'HHSTATE',      # Household state (if present)
    'URBAN',        # Urban indicator (alternative: URBRUR)
    'VEHID',        # Vehicle ID
    'VEHTYPE',      # Vehicle type
    'MAKE'          # Vehicle make code
]

def main():
    # ------------------------------------------------------------------
    # 2. Load the CSV
    # ------------------------------------------------------------------
    if not os.path.exists(INPUT_CSV):
        raise FileNotFoundError(f"Input file not found: {INPUT_CSV}")

    print(f"Loading {INPUT_CSV} ...")
    df = pd.read_csv(INPUT_CSV, low_memory=False)   # low_memory helps with large files

    print(f"Original columns: {len(df.columns)}")
    print(f"First few column names: {list(df.columns[:10])} ...")

    # ------------------------------------------------------------------
    # 3. Keep only existing required columns
    # ------------------------------------------------------------------
    existing_cols = [c for c in REQUIRED_COLUMNS if c in df.columns]
    missing_cols  = [c for c in REQUIRED_COLUMNS if c not in df.columns]

    if missing_cols:
        print(f"\nWarning: These requested columns are NOT in the file and will be ignored:")
        for c in missing_cols:
            print(f"   - {c}")

    df_filtered = df[existing_cols].copy()

    # ------------------------------------------------------------------
    # 4. Save the cleaned CSV
    # ------------------------------------------------------------------
    df_filtered.to_csv(OUTPUT_CSV, index=False)
    print(f"\nDone! Filtered file saved as: {OUTPUT_CSV}")
    print(f"   Kept columns ({len(existing_cols)}): {existing_cols}")

if __name__ == "__main__":
    main()