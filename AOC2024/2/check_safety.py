class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.reports = []

    def parse(self):
        with open(self.filename) as f:
            for line in f:
                line = line.strip().split()
                self.reports.append([int(r) for r in line])
        
        return self.reports


class SafetyChecker:
    def __init__(self, reports):
        self.reports = reports
        self.invalid_reports = []

    def check_safety(self, reports, first_valid_stops=False):
        valid = 0
        for report in reports:
            if first_valid_stops == True and valid > 0:
                break

            last_level = None
            current_index = 0
            if report[0] - report[1] > 0:
                way = 'descending'
            else:
                way = 'ascending'

            for level in report:
                current_index += 1

                if last_level is None or abs(last_level - level) <= 3 and abs(last_level - level) >= 1:
                    if way == 'descending' and last_level is not None and last_level - level < 0:
                        self.invalid_reports.append(report)
                        break
                    elif way == 'ascending' and last_level is not None and last_level - level > 0:
                        self.invalid_reports.append(report)
                        break

                    last_level = level

                    if current_index == len(report):
                        valid += 1
                else:
                    self.invalid_reports.append(report)
                    break

        return valid
    
    def _construct_list_with_skipped_value(self, report, index):
        return report[:index] + report[index+1:]

    def _construct_all_possible_lists(self, report):
        possible_lists = []
        for report_list in range(len(report)):
            possibilities = []
            for index in range(len(report[report_list])):
                possibilities.append(self._construct_list_with_skipped_value(report[report_list], index))
            possible_lists.append(possibilities)

        return possible_lists
    
    def check_safety_with_problem_dampener(self, reports):
        dampened = 0
        dampened_reports = self._construct_all_possible_lists(reports)
        for i in dampened_reports:
            if self.check_safety(i, first_valid_stops=True) > 0:
                dampened += 1

        return dampened

if __name__ == '__main__':
    p = Parser("input.txt")
    reports = p.parse()
    
    s = SafetyChecker(reports)
    valid = s.check_safety(s.reports)
    dampened = s.check_safety_with_problem_dampener(s.invalid_reports)
    all_ok = valid + dampened
    print(f"Number of valid reports: {valid}")
    print(f"Number of valid reports with problem dampener: {dampened}")
    print(f"Total number of valid reports: {all_ok}")

