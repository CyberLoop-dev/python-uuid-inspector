import unittest
from uuid_inspector import inspect

class UuidInspectorTests(unittest.TestCase):
    def test_uuid_v6_timestamp_uses_reordered_time_fields(self):
        from uuid import UUID
        from uuid_inspector import timestamp_for
        # Timestamp fields: 48 high bits + 12 low bits; version nibble is 6.
        timestamp = 0x1ED2A0000000123
        time_high = timestamp >> 12
        time_low = timestamp & 0xFFF
        value_int = (time_high << 80) | (6 << 76) | (time_low << 64) | (2 << 62) | 1
        value = UUID(int=value_int)
        self.assertEqual(value.version, 6)
        self.assertIsNotNone(timestamp_for(value))

    def test_detects_version_and_duplicates(self):
        value = "550e8400-e29b-41d4-a716-446655440000"
        items = inspect(value + "\n" + value)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["version"], 4)
        self.assertEqual(items[0]["duplicate_count"], 2)

if __name__ == "__main__":
    unittest.main()
