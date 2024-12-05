import unittest
import printer_fix


class TestParser(unittest.TestCase):
    def test_parser(self):
        parser = printer_fix.Parser("test_input.txt")
        self.assertIsInstance(parser.parse(), tuple)
        self.assertIsInstance(parser.parse()[0], list)
        self.assertIsInstance(parser.parse()[1], list)
        self.assertEqual(parser.parse()[0],['47|53', '97|13', '97|61', '97|47', '75|29', '61|13', '75|53', '29|13', '97|29', '53|29', '61|53', '97|53', '61|29', '47|13', '75|47', '97|75', '47|61', '75|61', '47|29', '75|13'])
        self.assertEqual(parser.parse()[1],['75,47,61,53,29', '97,61,53,29,13', '75,29,13', '75,97,47,61,53', '61,13,29', '97,13,75,29,47'])


class TestUpdateRule(unittest.TestCase):
    def test_update_rule(self):
        rule = printer_fix.UpdateRule("1|2")
        self.assertIsInstance(rule.before, int)
        self.assertIsInstance(rule.after, int)
        self.assertEqual(rule.before, 1)
        self.assertEqual(rule.after, 2)
    

class TestManual(unittest.TestCase):
    def test_manual(self):
        manual = printer_fix.Manual("1,2,3,4,5")
        self.assertIsInstance(manual.pages, list)
        self.assertEqual(manual.pages, [1,2,3,4,5])
    

class TestPrinterFix(unittest.TestCase):
    def setUp(self):
        parser = printer_fix.Parser("test_input.txt")
        self.printer_fix = printer_fix.PrinterFix(parser.parse())
    
    def test_parse_data(self):
        self.assertIsInstance(self.printer_fix.rules, list)
        self.assertIsInstance(self.printer_fix.updates, list)
        self.assertEqual(len(self.printer_fix.rules), 20)
        self.assertEqual(len(self.printer_fix.updates), 6)
    
    def test_check_rules(self):
        self.assertEqual(self.printer_fix.check_rules(), 143)
    
    def test_fix_ordering(self):
        self.printer_fix.check_rules()
        self.assertEqual(self.printer_fix.fix_ordering(), 123)


if __name__ == "__main__":
    unittest.main()