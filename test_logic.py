import unittest

def add_task(tasks, new_task):
    if not new_task:
        return False
    tasks.append(new_task)
    return True

class TestSmartManager(unittest.TestCase):
    def test_add_task_success(self):
        tasks = []
        result = add_task(tasks, "Лабораторияны бүтүрүү")
        self.assertTrue(result)
        self.assertEqual(len(tasks), 1)

    def test_add_task_empty(self):
        tasks = []
        result = add_task(tasks, "")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
