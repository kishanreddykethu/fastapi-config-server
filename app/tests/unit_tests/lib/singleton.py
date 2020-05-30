import unittest
import threading

from app.lib.singleton import SingletonMetaClass


def instantiate(cls, instance_ids: list):
    instance = cls()
    instance_ids.append(id(instance))


class TestSingletonObject(object, metaclass=SingletonMetaClass):
    """
    A simple object for testing the SingletonMetaClass library class.
    """
    def __init__(self, *args, **kwargs):
        pass


class TestSingletonMeta(unittest.TestCase):
    def test_instance(self):
        threads = 2
        jobs = []

        instance_ids = []
        for i in range(threads):
            thread = threading.Thread(target=instantiate(TestSingletonObject, instance_ids))
            jobs.append(thread)

        for job in jobs:
            job.start()

        for job in jobs:
            job.join()

        self.assertEqual(instance_ids[0], instance_ids[1])


if __name__ == '__main__':
    unittest.main()
