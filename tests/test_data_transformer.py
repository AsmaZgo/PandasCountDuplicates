import unittest
import pandas as pd

from processing.data_transformer import count_duplicates


class TestDataTransformer(unittest.TestCase):
    def test_count_duplicates(self):
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )
        result = count_duplicates(df_1, ['col_1', 'col_2'])

        # Expected result
        expected_samples = pd.DataFrame({
            'col_1': ['A'],
            'col_2': ['a'],
            'num_occurrences': [2]
        })
        expected_count = 1

        self.assertEqual(result['count'], expected_count)
        pd.testing.assert_frame_equal(result['samples'], expected_samples)

    def test_count_duplicates_empty_dataframe(self):
        df = pd.DataFrame(columns=['col_1', 'col_2', 'col_3', 'col_4'])
        result = count_duplicates(df, ['col_1', 'col_2'])

        # Expected result
        expected_samples = pd.DataFrame(columns=['col_1', 'col_2', 'num_occurrences'])
        expected_samples['num_occurrences'] = expected_samples['num_occurrences'].astype(int)
        expected_count = 0

        self.assertEqual(result['count'], expected_count)
        pd.testing.assert_frame_equal(result['samples'], expected_samples)

    def test_count_duplicates_non_existent_column(self):
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )

        # Check if an exception is raised for col_5
        with self.assertRaises(ValueError) as context:
            count_duplicates(df_1, ['col_1', 'col_5'])

        self.assertTrue(
            "Column 'col_5' does not exist in the dataframe! Please verify your input." in str(context.exception))

    def test_count_duplicates_col_1(self):
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )
        result = count_duplicates(df_1, ['col_1'])

        # Expected result
        expected_samples = pd.DataFrame({
            'col_1': ['A', 'B'],
            'num_occurrences': [4, 3]
        })
        expected_count = 2

        self.assertEqual(result['count'], expected_count)
        pd.testing.assert_frame_equal(result['samples'], expected_samples)

    def test_count_duplicates_col_1_col_2(self):
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )
        result = count_duplicates(df_1, ['col_1', 'col_2'])

        # Expected result
        expected_samples = pd.DataFrame({
            'col_1': ['A'],
            'col_2': ['a'],
            'num_occurrences': [2]
        })
        expected_count = 1

        self.assertEqual(result['count'], expected_count)
        pd.testing.assert_frame_equal(result['samples'], expected_samples)

    def test_count_duplicates_col_1_col_2_col_3(self):
        df_1 = pd.DataFrame(
            data=[
                ['A', 'a', 'x', 1],
                ['A', 'b', 'x', 1],
                ['A', 'c', 'x', 1],
                ['B', 'a', 'x', 1],
                ['B', 'b', 'x', 1],
                ['B', 'c', 'x', 1],
                ['A', 'a', 'y', 1],
            ],
            columns=['col_1', 'col_2', 'col_3', 'col_4']
        )
        result = count_duplicates(df_1, ['col_1', 'col_2', 'col_3'])

        # Expected result
        expected_samples = pd.DataFrame(columns=['col_1', 'col_2', 'col_3', 'num_occurrences'])
        expected_samples['num_occurrences'] = expected_samples['num_occurrences'].astype(int)
        expected_count = 0

        self.assertEqual(result['count'], expected_count)
        pd.testing.assert_frame_equal(result['samples'], expected_samples)


if __name__ == '__main__':
    unittest.main()
