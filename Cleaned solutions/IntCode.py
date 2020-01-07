import 

class IntCoder:
    def __init__(self, intcode):
        self.intcode = intcode
        self.reset()
    
    def reset(self):
        self.work_intcode = {idx:val for idx, val in enumerate(self.intcode)} 
        self.output = []
        self.mem = {}
        
    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            return cls([int(x) for x in file.read().split(',')])
    
    @classmethod
    def test_txt(cls, text, calc, **input_dict):
        test_intcode = cls([int(x) for x in text.split(',')])
        test_intcode.intcodeRead(calc, outmode = 0, **input_dict)
    
    def mode_manage(self, num, mode):
        if mode == 0:
            return self.work_intcode.get(num, 0)
        elif mode == 1:
            return num
        elif mode == 2:
            return self.work_intcode.get(self.mem['relbase'] + num, 0)
    
    def spec_mode_manage(self, num, mode):
        if mode == 0 or mode == 1:
            return num
        elif mode == 2:
            return self.mem['relbase'] + num
                
    def instr_manage(self, selfmem):      
        current_idx =  selfmem['current_idx']
        
        instr_str = str(self.work_intcode.get(current_idx, 0))
        params = {x:int(y) for x, y in enumerate(reversed(instr_str[:len(instr_str)-2]))}
        opcode = instr_str[len(instr_str)-2:]
        
        
#         print(instr_str, opcode)
        if int(opcode) == 1:
            param_a = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            param_b = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            output_loc = self.spec_mode_manage(self.work_intcode.get(current_idx + 3, 0), params.get(2, 0))
            
            self.work_intcode[output_loc] = param_a + param_b
            
            current_idx += 4
            
        elif int(opcode) == 2:
            param_a = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            param_b = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            output_loc = self.spec_mode_manage(self.work_intcode.get(current_idx + 3, 0), params.get(2, 0))
            
            self.work_intcode[output_loc] = param_a * param_b
            
            current_idx += 4

        elif int(opcode) == 3: 
            try:
                move_num = self.spec_mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0)) 
                selfmem['inputs'][selfmem['input_idx']]
                self.work_intcode[move_num] = selfmem['inputs'][selfmem['input_idx']]
                
                selfmem['input_idx'] += 1
                current_idx += 2
                
            except IndexError:
#                 print('HALT COMMAND')
                selfmem['midhalt'] = 1
        
        elif int(opcode) == 4:
            val_output = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            self.output.append(val_output)
            
            current_idx += 2
        
        elif int(opcode) == 5:
            check = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            
            if check != 0:
                current_idx = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            else:
                current_idx += 3
        
        elif int(opcode) == 6:
            check = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            
            if check == 0:
                current_idx = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            else:
                current_idx += 3
        
        elif int(opcode) == 7:
            param_a = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            param_b = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            output_loc = self.spec_mode_manage(self.work_intcode.get(current_idx + 3, 0), params.get(2, 0))
            
            if param_a < param_b:
                self.work_intcode[output_loc] = 1
            else:
                self.work_intcode[output_loc] = 0
            
            current_idx += 4
        
        elif int(opcode) == 8:
            param_a = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            param_b = self.mode_manage(self.work_intcode.get(current_idx + 2, 0), params.get(1, 0))
            output_loc = self.spec_mode_manage(self.work_intcode.get(current_idx + 3, 0), params.get(2, 0))
            
            if param_a == param_b:
                self.work_intcode[output_loc] = 1
            else:
                self.work_intcode[output_loc] = 0
                
            current_idx += 4
        
        elif int(opcode) == 9:
            rel_adj = self.mode_manage(self.work_intcode.get(current_idx + 1, 0), params.get(0, 0))
            
            selfmem['relbase'] += rel_adj
                
            current_idx += 2
        
        return current_idx
       
    def intcodeRead(self, outmode = 1, **input_dict):
        current_idx = 0
        
        if self.mem == {}:
            self.mem = input_dict
            self.mem['input_idx'] = 0
            self.mem['midhalt'] = None
            self.mem['current_idx'] = 0
            self.mem['relbase'] = 0
            
            if isinstance(self.mem.get('inputs',0), int):
                self.mem['inputs'] = [self.mem.get('inputs',0)]
        else:
            self.mem['inputs'] = input_dict['inputs']
            self.mem['midhalt'] = 0
        
        while self.work_intcode.get(self.mem['current_idx'], 0) != 99 and self.mem['midhalt'] != 1:
            self.mem['current_idx'] = self.instr_manage(self.mem)

        reconstituted = [self.work_intcode.get(x, 0) for x in range(max(self.work_intcode)+1)]
        
        if outmode == 1:
            return reconstituted, self.output
        elif outmode == 'output_only':
            return self.output
        elif outmode == 'last_out':
            return self.output[-1]
        else:
#             print(reconstituted, self.output, self.mem.get('inputs'))
            print(self.mem.get('inputs'), self.output)