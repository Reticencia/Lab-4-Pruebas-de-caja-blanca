import process_grades
import pytest

@pytest.mark.parametrize(
        'student, expected',
        [
            (
                [{'name' : 'Ana', 'grades' : [55,55,55]}], 'is in recovery'
            )
        ]
)


@pytest.mark.wip
def test_process_grade_recovery(student,expected, capsys):
    result = process_grades.process_grades(student)
    captured = capsys.readouterr()
    assert expected in captured.out

@pytest.mark.parametrize(
        'student, expected',
        [
            (
                [{'name' : 'Ana', 'grades' : [80,80,80]}], ['Ana']
            )
        ]
)

@pytest.mark.wip
def test_process_grade_pass(student,expected):
    result = process_grades.process_grades(student)

    assert result ['passed'] == expected

@pytest.mark.parametrize(
        'student, expected',
        [
            (
                [{'name' : 'Ana', 'grades' : [40,40,40]}], ['Ana']
            )
        ]
)

@pytest.mark.wip
def test_process_grade_fail(student,expected):
    result = process_grades.process_grades(student)

    assert result ['failed'] == expected