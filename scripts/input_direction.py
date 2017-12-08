import time
import random
import pickle
def input_read(buttons, controller = 0):
    global running
    input_value = open('../scripts/input_'+str(controller)+'.txt', 'r').read()
    if 'exit' in input_value.lower():
        running = False
    buttons[str(controller)].x_axis = int(input_value.strip())
    return buttons

def random_file(controller = 0):
    global running
    file_write = open('../scripts/input_'+str(controller)+'.txt', 'w')
    file_write.write(str(random.randint(-100, 100)))
    file_write.close()
    return 1

def move_data(k, dict_values):
    folder = '/home/adrian/.local/share/mupen64plus/screenshot/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                print folder+'/'+str(k)+'/'+file_path.split('/')[-1]
                os.rename(file_path, folder+str(k)+'/'+file_path.split('/')[-1])
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    pickle.dump(dict_values, open(folder+str(k)+'/'+'data.pkl', 'w'))
debug.buttons_override(reset=True)
buttons = {}
buttons['0'] = debug.buttons_override_struct_last(controller=0)
buttons['1'] = debug.buttons_override_struct_last(controller=1)

buttons['0'].a_button = 1
buttons['1'].a_button = 1
running = True
core.state_load()
time.sleep(0.5)
core.state_set_slot(1)
n_trees = 1
import os, shutil
folder = '/home/adrian/.local/share/mupen64plus/screenshot/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

folder = '/home/adrian/.local/share/mupen64plus/screenshot/0/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
        
n_screenshot = 0
core.pause()
random_file(0)
random_file(1)
while running == True:
    ## Negative and positive values accepted. Need to check range of values (probably -128, 128)
    core.state_save()
    for k in range(n_trees):
        dict_values = {}
        dict_values[0] = []
        dict_values[1] = []
        for i in range(30):
            n_screenshot += 1
            input_read(buttons, 0)
            input_read(buttons, 1)
            dict_values[0].append(buttons['0'].x_axis)
            dict_values[1].append(buttons['1'].x_axis)
            debug.buttons_override_struct(buttons['0'], 0)
            debug.buttons_override_struct(buttons['1'], 1)
            print(len(os.listdir(folder)))
            core.take_next_screenshot()
            time.sleep(0.2)
            core.advance_frame()
        move_data(k, dict_values)
        core.state_set_slot(2)
        time.sleep(0.2)
        core.state_save()
        time.sleep(0.2)
        core.state_set_slot(1)
        time.sleep(0.2)
        if n_screenshot > 950:
            core.resume()
            time.sleep(3)
            core.reset()
            time.sleep(5)
            core.state_set_slot(1)
            time.sleep(0.2)
            n_screenshot = 0
        core.state_load()
        time.sleep(0.2)
        random_file(0)
        random_file(1)
    core.state_set_slot(2)
    time.sleep(0.5)
    core.state_load()
    time.sleep(0.5)
    core.state_set_slot(1)
    time.sleep(0.5)
debug.buttons_override_disable()
