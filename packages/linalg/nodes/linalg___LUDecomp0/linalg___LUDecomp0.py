from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
from scipy.linalg import lu


class LUDecomp_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(LUDecomp_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        p, l, u = lu(self.input(0))
        self.set_output_val(0, p)
        self.set_output_val(1, l)
        self.set_output_val(2, u)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...

    def removing(self):
        pass
