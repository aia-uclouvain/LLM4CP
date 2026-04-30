"""
Central configuration / argument parser for CP-Model-Zoo.
All entry points (app.py, run_gui.py, run_indexing.py, run_inference.py) import
config_parser() from here.
"""
import argparse
import os

# Base directory = folder that contains this file
_BASE = os.path.dirname(os.path.abspath(__file__))


def _path(*parts):
    """Return an absolute path relative to the project root."""
    return os.path.join(_BASE, *parts)


def config_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CP-Model-Zoo – Natural Language Query System for CP Models",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # ── Data paths ────────────────────────────────────────────────────────────
    parser.add_argument(
        "--mzn_path",
        default=_path("data", "input", "minizinc_source_code"),
        help="Directory containing the original MiniZinc (.mzn) model files.",
    )
    parser.add_argument(
        "--merged_mzn_source_path",
        default=_path("data", "input", "merged_mzn_source_code"),
        help="Directory containing merged MiniZinc source code (.txt) files.",
    )
    parser.add_argument(
        "--txt_path",
        default=_path("data", "input", "csplib"),
        help="Directory for generated text versions of models.",
    )
    parser.add_argument(
        "--descriptions_dir",
        default=_path("data", "output", "generated_descriptions"),
        help="Directory where generated model descriptions are stored.",
    )

    # ── Vector DB ─────────────────────────────────────────────────────────────
    parser.add_argument(
        "--storage_dir",
        default=_path("data", "vector_dbs", "code_as_text", "expert"),
        help="Directory for the LlamaIndex vector-store persistence.",
    )

    # ── Output / results ──────────────────────────────────────────────────────
    parser.add_argument(
        "--output_dir",
        default=_path("data", "output"),
        help="Directory for generated outputs.",
    )
    parser.add_argument(
        "--results_dir",
        default=_path("data", "results"),
        help="Directory for experiment results.",
    )

    # ── Runtime flags ─────────────────────────────────────────────────────────
    parser.add_argument(
        "--prod",
        action="store_true",
        default=False,
        help="Run in production mode (fixed port 9001, no auto-open browser).",
    )
    parser.add_argument(
        "--index",
        default="expert",
        choices=["code", "expert", "medium", "beginner",
                 "mediumexpert", "beginnerexpert", "beginnermedium",
                 "beginner_medium_expert"],
        help="Which pre-built index variant to load.",
    )

    return parser

