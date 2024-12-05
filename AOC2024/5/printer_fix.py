class Parser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        with open(self.file) as f:
            text = f.read()
            text = text.splitlines()
               
            for i in range(len(text)):
                if text[i] == '':
                    page_ordering_rules = text[:i-1]
                    page_updates = text[i+1:]
                    break
        
        return page_ordering_rules, page_updates


class UpdateRule:
    def __init__(self, rule_txt):
        self.rule_txt = rule_txt
        self.before = int(self._parse_rule()[0])
        self.after = int(self._parse_rule()[1])

    def _parse_rule(self):
        rule = self.rule_txt.split('|')
        return rule


class Manual:
    def __init__(self, update):
        self.update = update
        self.pages = self._parse_pages()

    def _parse_pages(self):
        update = self.update.split(',')
        pages = []
        for i in  update:
            pages.append(int(i))
        
        return pages


class PrinterFix:
    def  __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.rules = []
        self.updates = []
        self.incorect_order = []
        self.correct_order_middle_pages_add_up = 0
        self.fixed_order_middle_pages_add_up = 0
        self._parse_data()
        
    def _parse_data(self):
        for i in self.parsed_data[0]:
            self.rules.append(UpdateRule(i))
        
        for i in self.parsed_data[1]:
            self.updates.append(Manual(i))
    
    def check_rules(self):
        for update in self.updates:
            for rc,rule in enumerate(self.rules):
                if rule.before in update.pages:
                    try:
                        index_before = update.pages.index(rule.before)
                        index_after = update.pages.index(rule.after)
                        if index_before > index_after:
                            self.incorect_order.append(update.pages)
                            break
                    except ValueError:
                        pass
                if rc == len(self.rules) - 1:
                    self.correct_order_middle_pages_add_up += update.pages[len(update.pages) // 2]
            
        return self.correct_order_middle_pages_add_up

    def fix_ordering(self):
        for update in self.incorect_order:
            incorrect = True
            while incorrect:
                for rc, rule in enumerate(self.rules):
                    if rule.before in update:
                        try:
                            index_before = update.index(rule.before)
                            index_after = update.index(rule.after)
                            if index_before > index_after:
                                update[index_before], update[index_after] = update[index_after], update[index_before]
                                break
                        except ValueError:
                            pass
                    if rc == len(self.rules) - 1:
                        incorrect = False

            self.fixed_order_middle_pages_add_up += update[len(update) // 2]

        return self.fixed_order_middle_pages_add_up

if __name__ == "__main__":
    parser = Parser("input.txt")
    printer_fix = PrinterFix(parser.parse())
    print(f'Add up of middle page numbers from all correct manuals is: {printer_fix.check_rules()}')
    print(f'Add up of middle page numbers from all fixed manuals is: {printer_fix.fix_ordering()}')



