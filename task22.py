def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result = {}
    for student in students:
        result.setdefault(student['group'],[]).append(student['name'])
    return result

students = [
    {
        'name':'daler',
        'group':'sn2'
    },
    {
        'name':'samandar',
        'group':'sn2'
    },
    {
        'name':'sharif',
        'group':'sn4'
    },
    {
        'name':'azizbek',
        'group':'sn4'
    }
]

print(group_students(students))