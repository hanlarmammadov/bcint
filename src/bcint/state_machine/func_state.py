from src.bcint.state_machine.flow_interruption import FlowInterruption


class FuncState:

    def __init__(self, num_of_ins: int):
        self.curr_index = -1
        self.jump_index = -1
        self.num_of_ins = num_of_ins
        self.flow_interruption = FlowInterruption.NONE
        self.returned_value = None

    def __repr__(self):
        return "ind: {index} jmp: {jump} len: {len} intr: {flow_intr} ret: {ret}" \
            .format(index=self.curr_index,
                    jump=self.jump_index,
                    len=self.num_of_ins,
                    flow_intr=self.flow_interruption,
                    ret=self.returned_value)

    def __str__(self):
        return self.__repr__()
