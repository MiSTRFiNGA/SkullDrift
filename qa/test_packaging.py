"""Skull Drift packaging QA — run after python build.py."""
from __future__ import annotations
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
MB = 1024 * 1024


class TestSkullDriftPackaging(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cg = DIST / "skulldrift-crazygames.zip"
        cls.poki = DIST / "skulldrift-poki.zip"
        if not cls.cg.is_file() or not cls.poki.is_file():
            raise unittest.SkipTest("dist zips missing — run python build.py first")

    def test_sizes(self):
        for p in (self.cg, self.poki):
            size = p.stat().st_size
            print(p.name, size)
            self.assertLessEqual(size, 50 * MB)
            self.assertLessEqual(size, 20 * MB)

    def test_index_and_relative(self):
        for p in (self.cg, self.poki):
            with zipfile.ZipFile(p) as zf:
                names = zf.namelist()
                self.assertIn("index.html", names)
                for n in names:
                    self.assertFalse(n.startswith("/") or n.startswith("\\"))
                    self.assertNotIn("..", n.split("/"))
