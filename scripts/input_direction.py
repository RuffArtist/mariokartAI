import time

debug.buttons_override(reset=True)
buttons = debug.buttons_override_struct_last(controller=0)
buttons.a_button = 1
running = True
while running == True:
    try:
        ## Negative and positive values accepted. Need to check range of values (probably -32768, 32767)
        input_value = open('/media/adrian/Storage/Dropbox/codes/scripts_m64py/input.txt', 'r').read()
        if 'exit' in input_value.lower():
            running = False
            break
        print input_value.strip()
        buttons.x_axis = int(input_value.strip())
        print buttons.x_axis
        debug.buttons_override_struct(buttons)
        time.sleep(1)
    except:
        continue
    
debug.buttons_override_disable()
