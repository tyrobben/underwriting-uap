# tests/test_classifier_prompt.py
import json
import re
import pathlib
import yaml

PROMPT   = pathlib.Path("prompts/classifier.yaml")
EXAMPLE  = pathlib.Path("prompts/examples/cls_good.md")

REQ_KEYS = {
    "naics",
    "sic",
    "am_best_class",
    "iso_gl",
    "vehicle_types",
    "appetite_flag",
    "citations",
}


def test_schema_keys():
    prompt = yaml.safe_load(PROMPT.read_text())
    schema_keys = set(prompt["output_schema"].keys())
    missing = REQ_KEYS - schema_keys
    assert not missing, f"schema missing keys: {missing}"


def test_list_fields_in_example():
    md = EXAMPLE.read_text()
    # grab the first {...} block – dot-all (= re.S) so new-lines are included
    match = re.search(r"\{[^\}]*\}", md, flags=re.S)
    assert match, "No JSON block found in cls_good.md"
    example = json.loads(match.group(0))

    for field in ("naics", "sic", "iso_gl", "vehicle_types", "citations"):
        assert isinstance(
            example[field], list
        ), f"{field} should be a list in example json"