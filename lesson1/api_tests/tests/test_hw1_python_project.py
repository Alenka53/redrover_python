import pytest

from lesson1.api_tests.case.pom.case import create_case
from lesson1.api_tests.case.models.case import Case, Case1
from lesson1.api_tests.case.data.case import create_case_dict, create_case_dict1


@pytest.mark.xfail(reason="Not enough data (priority is lost)")
def test_create_case1():
    response = create_case(Case1(**create_case_dict1).model_dump())
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(Case1(**create_case_dict1).model_dump())
    response.schema_should_be_eq(Case1(**create_case_dict1).model_json_schema())

