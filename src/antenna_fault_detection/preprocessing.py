"""Dataset preparation used by the antenna fault detection analysis."""

from __future__ import annotations

import numpy as np
import pandas as pd


COLUMN_RENAME_MAP = {
    "Z_Real (Ohms)": "Z_Real",
    "Z_Imag (Ohms)": "Z_Imag",
    "S11 (dB)": "S11",
    "Gain (dBi)": "Gain",
    "Eff (%)": "Eff",
    "BW (MHz)": "BW",
}


def rename_measurement_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with the notebook's canonical measurement names."""
    return data.rename(columns=COLUMN_RENAME_MAP).copy()


def engineer_features(data: pd.DataFrame) -> pd.DataFrame:
    """Add impedance, gain, and resonance features to an antenna dataset."""
    required = {"Z_Real", "Z_Imag", "Gain", "Eff", "BW"}
    missing = required.difference(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Missing required measurement columns: {missing_columns}")

    result = data.copy()
    result["Z_magnitude"] = np.hypot(result["Z_Real"], result["Z_Imag"])
    result["Z_phase_deg"] = np.degrees(np.arctan2(result["Z_Imag"], result["Z_Real"]))
    result["gain_over_eff"] = result["Gain"] / (result["Eff"] + 1e-8)
    result["conductance"] = result["Z_Real"] / (result["Z_magnitude"] ** 2 + 1e-12)
    result["susceptance"] = result["Z_Imag"] / (result["Z_magnitude"] ** 2 + 1e-12)
    result["Q_factor"] = result["Gain"] / (result["BW"] + 1e-6)
    result["resonance_quality"] = 1 / (np.abs(result["Z_phase_deg"]) + 1e-6)
    return result