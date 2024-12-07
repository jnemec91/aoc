import unittest
import bridge_repair

class TestBridgeRepair(unittest.TestCase):
    def test_evaluate(self):
        bridge = bridge_repair.BridgeRepair([])
        self.assertEqual(bridge._evaluate('1+2*3'), 9)
        self.assertEqual(bridge._evaluate('1*2+3'), 5)
        self.assertEqual(bridge._evaluate('1+2+3'), 6)
        self.assertEqual(bridge._evaluate('1*2*3'), 6)
        self.assertEqual(bridge._evaluate('1||2||3'), 123)
        self.assertEqual(bridge._evaluate('1+2||3'), 33)
        self.assertEqual(bridge._evaluate('1||2+3'), 15)
    
    def test_get_all_possible_strings(self):
        bridge = bridge_repair.BridgeRepair([])
        self.assertEqual(bridge._get_all_possible_strings(['1', '2', '3']), ['1+2+3', '1+2*3', '1*2+3', '1*2*3'])
        self.assertEqual(bridge._get_all_possible_strings(['1', '2', '3'], part_two=True),
                         ['1+2+3', '1+2*3', '1+2||3', '1*2+3', '1*2*3', '1*2||3', '1||2+3', '1||2*3', '1||2||3'])   

    def test_repair(self):
        data = [('6', ['1', '2', '3']), ('26', ['2', '3', '4'])]
        bridge = bridge_repair.BridgeRepair(data)
        self.assertEqual(bridge.repair(), 6)
    
    def test_repair_part_two(self):
        data = [('6', ['1', '2', '3']), ('27', ['2', '3', '4'])]
        bridge = bridge_repair.BridgeRepair(data)
        self.assertEqual(bridge.repair(part_two=True), 33)

if __name__ == '__main__':
    unittest.main()