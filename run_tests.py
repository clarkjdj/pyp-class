import unittest
import os
import sys

try:
    from tempfile import TemporaryDirectory
except ImportError:
    import tempfile
    import shutil

    class TemporaryDirectory(object):
        def __enter__(self):
            self.dir_name = tempfile.mkdtemp()
            return self.dir_name

        def __exit__(self, exc_type, exc_value, traceback):
            shutil.rmtree(self.dir_name)

from nose.core import TestProgram
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


import pytoml as toml

CODE_TYPE = 'code'
SOLUTIONS_RELATIVE_PATH = 'solutions'
TESTS_FILE_NAME = 'tests.py'


class InvalidLessonException(Exception):
    pass


class Lesson(object):
    def __init__(self, uuid, path):
        self.uuid = uuid
        self.path = path
        self.__test_data = None

    @property
    def test_data(self):
        if not self.__test_data:
            self.__test_data = read_lesson_tests(self.path)

        return self.__test_data


class Solution(object):
    def __init__(self, lesson, path):
        self.lesson = lesson
        self.path = path


def read_lesson_tests(lesson_path):
    tests_path = lesson_path / TESTS_FILE_NAME
    with tests_path.open('r') as tests_f:
        return tests_f.read()


def iter_code_lessons(path='.', unit_glob='unit-*',
                      lesson_glob='lesson-*', rmotr_toml_name='.rmotr'):
    p = Path(path)

    for unit in p.glob(unit_glob):
        for lesson_path in unit.glob(lesson_glob):
            rmotr_toml = lesson_path / rmotr_toml_name
            if not rmotr_toml.exists():
                raise InvalidLessonException(
                    ("Lessons must contain a .rmotr file. "
                     "Lesson {} doesn't contain any").format(lesson_path.name))

            with rmotr_toml.open() as rmotr_f:
                lesson_data = toml.load(rmotr_f)
                if lesson_data['type']:
                    yield Lesson(uuid=lesson_data['uuid'],
                                 path=lesson_path)


def iter_lesson_solutions(lesson):
    solutions_path = (lesson.path / SOLUTIONS_RELATIVE_PATH)
    if solutions_path.exists():
        for solution_path in solutions_path.glob('*.py'):
            yield Solution(lesson=lesson, path=solution_path)


def write_solution_test_file(_dir, solution):
    abs_path = os.path.abspath(_dir)
    test_file_name = os.path.join(abs_path, 'test_' + solution.path.name)
    with open(test_file_name, 'w') as test_f, solution.path.open('r') as solution_f:
        test_f.write(solution_f.read())
        test_f.write(solution.lesson.test_data)


def test_lessons_solutions(exit=True):
    with TemporaryDirectory() as temp_dir:
        abs_path = os.path.abspath(temp_dir)
        for lesson in iter_code_lessons():
            for solution in iter_lesson_solutions(lesson):
                write_solution_test_file(temp_dir, solution)

        suite = unittest.TestLoader().discover(abs_path)
        program = TestProgram(suite=suite, exit=False)

        if exit:
            sys.exit(int(not program.success))

        return program


main = test_lessons_solutions

if __name__ == '__main__':
    main()
