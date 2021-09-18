from src.bcint.state_machine.flow_interruption import FlowInterruption


class FuncState:

    def __init__(self, num_of_ins: int):
        self.curr_index = -1
        self.jump_index = -1
        self.num_of_ins = num_of_ins
        self.flow_interruption = FlowInterruption.NONE
        self.returned_value = None
