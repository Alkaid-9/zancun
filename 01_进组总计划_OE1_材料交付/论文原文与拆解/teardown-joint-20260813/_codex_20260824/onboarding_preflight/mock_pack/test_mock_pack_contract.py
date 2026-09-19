import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E1 = ROOT / "questions_E1.md"
E2 = ROOT / "questions_E2.md"
RUBRIC = ROOT / "rubric.tsv"
REPORT = ROOT / "REPORT.md"


def question_ids(path: Path, prefix: str) -> set[str]:
    pattern = re.compile(rf"^### ({prefix}-\d+)\b", re.MULTILINE)
    return set(pattern.findall(path.read_text(encoding="utf-8")))


class MockPackContractTests(unittest.TestCase):
    def test_question_and_rubric_counts_are_explicit(self):
        e1_ids = question_ids(E1, "E1")
        e2_ids = question_ids(E2, "E2")
        rows = [
            line.split("\t")
            for line in RUBRIC.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("rubric_id")
        ]
        e1_rows = [row for row in rows if row[1] == "E1"]
        e2_rows = [row for row in rows if row[1] == "E2"]
        self.assertEqual(len(e1_ids), 10)
        self.assertEqual(len(e2_ids), 13)
        self.assertEqual(len(e1_rows), 10)
        self.assertEqual(len(e2_rows), 12)
        self.assertIn("满分 24", REPORT.read_text(encoding="utf-8"))
        self.assertIn("18/24", REPORT.read_text(encoding="utf-8"))

    def test_rubric_question_references_exist(self):
        e1_ids = question_ids(E1, "E1")
        e2_ids = question_ids(E2, "E2")
        for line in RUBRIC.read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("rubric_id"):
                continue
            fields = line.split("\t")
            stage = fields[1]
            references = re.findall(r"E[12]-\d+", fields[2])
            valid = e1_ids if stage == "E1" else e2_ids
            self.assertTrue(set(references) <= valid, line)

    def test_e2_gate_matches_twelve_two_point_items(self):
        rows = [
            line.split("\t")
            for line in RUBRIC.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("rubric_id") and "\tE2\t" in line
        ]
        self.assertEqual(len(rows) * 2, 24)
        gate_rules = [row[-1] for row in rows if "总分>=" in row[-1]]
        self.assertEqual(gate_rules, ["E2总分>=18/24且关键项无0"])
        self.assertNotIn("18/26", "\n".join(row[-1] for row in rows))


if __name__ == "__main__":
    unittest.main()
