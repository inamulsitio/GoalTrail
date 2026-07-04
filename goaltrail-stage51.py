# === Stage 51: Add unit tests for search and filter behavior ===
# Project: GoalTrail
from unittest.mock import patch, MagicMock
import pytest
from goal_tracker.core.search_filter import SearchFilter

class TestSearchFilter:
    @patch('goal_tracker.core.storage.Storage')
    def test_search_by_keyword(self, mock_storage):
        mock_storage.get_all_entries.return_value = [
            {'id': 1, 'content': 'Buy groceries', 'tags': ['shopping']},
            {'id': 2, 'content': 'Read book', 'tags': ['learning']}
        ]
        filter_obj = SearchFilter(mock_storage)
        results = filter_obj.search('groceries')
        assert len(results) == 1
        assert results[0]['id'] == 1

    @patch('goal_tracker.core.storage.Storage')
    def test_filter_by_tag(self, mock_storage):
        mock_storage.get_all_entries.return_value = [
            {'id': 1, 'content': 'Task A', 'tags': ['work', 'urgent']},
            {'id': 2, 'content': 'Task B', 'tags': ['personal']}
        ]
        filter_obj = SearchFilter(mock_storage)
        results = filter_obj.filter_by_tag('work')
        assert len(results) == 1
        assert results[0]['id'] == 1

    @patch('goal_tracker.core.storage.Storage')
    def test_filter_combined(self, mock_storage):
        mock_storage.get_all_entries.return_value = [
            {'id': 1, 'content': 'Fix bug', 'tags': ['dev'], 'status': 'open'},
            {'id': 2, 'content': 'Write doc', 'tags': ['dev'], 'status': 'done'}
        ]
        filter_obj = SearchFilter(mock_storage)
        results = filter_obj.search('bug').filter_by_tag('dev').filter_status('open')
        assert len(results) == 1
