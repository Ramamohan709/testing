import unittest

from app import health_payload


class HealthPayloadTests(unittest.TestCase):
    def test_health_payload_reports_healthy_status(self):
        self.assertEqual(
            health_payload(),
            {"status": "healthy", "service": "devops-practice"},
        )


if __name__ == "__main__":
    unittest.main()
