import json, re, pathlib, yaml

PROMPT  = pathlib.Path("prompts/classifier.yaml")
EXAMPLE = pathlib.Path("prompts/examples/cls_good.md")

# ---------- Test 1: schema must include required keys ----------
def test_schema_keys():
    required = {
        "naics", "sic", "am_best_class",
        "iso_gl", "vehicle_types",
        "appetite_flag", "citations",
    }
    schema = yaml.safe_load(PROMPT.read_text())["output_schema"]
    missing = required - set(schema)
    assert not missing, f"schema missing keys: {missing}"

# ---------- Test 2: sample JSON must have list fields ----------
def test_list_fields_in_example():
    md = EXAMPLE.read_text()
    block = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", md, re.S)
    assert block, "fenced JSON block not found in cls_good.md"

    example = json.loads(block.group(1))
    for field in ("naics", "sic", "iso_gl", "vehicle_types", "citations"):
        assert isinstance(example[field], list), f"{field} should be a list"
