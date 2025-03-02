from TM import *

config = load_configuration("tm_conf.json")
test_cases = ["1", "11", "111", "1111"]
analyze_execution(config, test_cases)
