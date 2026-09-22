# Data

Place the input file at `data/antenna_dataset.csv`.

The notebook expects these columns:

- `Z_Real (Ohms)`
- `Z_Imag (Ohms)`
- `S11 (dB)`
- `VSWR`
- `Gain (dBi)`
- `Eff (%)`
- `BW (MHz)`
- `Status`
- `Fault_Type`

The preprocessing step normalizes the measurement names to `Z_Real`, `Z_Imag`, `S11`, `Gain`, `Eff`, and `BW`. `Fault_Type` is the classification target; `Status` is retained for exploratory plots.

Do not commit private or licensed datasets. The CSV pattern is ignored by Git by default.