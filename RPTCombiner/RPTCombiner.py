import csv
from pathlib import Path

def combine_rpt(
    input_dir,
    output_file,
    pattern="*.rpt",
    extra_col_name="source_file",
    encoding="utf-8"
):
    input_dir = Path(input_dir)
    files = sorted(input_dir.glob(pattern))
    if not files:
        print(f"No files found in {input_dir} matching {pattern}")
        return

    # Use header of first file as reference
    with files[0].open("r", encoding=encoding, newline="") as f:
        reader = csv.reader(f)
        master_header = next(reader)

    total_rows = 0
    with open(output_file, "w", encoding=encoding, newline="") as out_f:
        writer = csv.writer(out_f)
        writer.writerow(master_header + [extra_col_name])  # write header once

        for file in files:
            with file.open("r", encoding=encoding, newline="") as in_f:
                reader = csv.reader(in_f)
                header = next(reader)  # skip header line

                if header != master_header:
                    print(f"[warn] Header mismatch in {file.name}, skipping.")
                    continue

                for row in reader:
                    writer.writerow(row + [file.name])
                    total_rows += 1

            print(f"[info] Processed {file.name}, total rows: {total_rows}")

    print(f"[done] Combined {len(files)} files → {output_file}")
    print(f"[done] Total rows written: {total_rows}")

# Example call from inside Python:
combine_rpt(
    input_dir=r"condensed",
    output_file=r"condensed\combined.csv"
)
