from corruptpm.validate import validate_project
from tests.conftest import ROOT


def test_shacl_validation_passes_for_valid_examples() -> None:
    result = validate_project(root=ROOT, include_examples=True)
    assert result.conforms, result.report_text

