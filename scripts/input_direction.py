import time
import random
import pickle
import getpass
import os, shutil
## We import the function to get the position from screenshot
from prepare_data.prepare_data import *


## Several functions, need to put in several files


def clean_folder(folder):
    ## This function erases all files in folder (only files 
    ## on main directory, not folders nor subfiles)
    ## To erase subfiles add           
    ## elif os.path.isdir(file_path): shutil.rmtree(file_path)

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def input_read(buttons, controller = 0):
    ## Reads file of input of corresponding controller
    global running
    input_value = open('../scripts/input_'+str(controller)+'.txt', 'r').read()
    if 'exit' in input_value.lower():
        running = False
    buttons[str(controller)].x_axis = int(input_value.strip())
    return buttons

def random_file(controller = 0):
    ## Generates a random value for the controller
    global running
    file_write = open('../scripts/input_'+str(controller)+'.txt', 'w')
    file_write.write(str(random.randint(-100, 100)))
    file_write.close()
    return 1

def move_data(k, dict_values):
    ## After a rollout, saves all screenshots in a folder, 
    ## along with the commands read
    folder = '/home/'+user+'/.local/share/mupen64plus/screenshot/'
    if not os.path.exists(folder+str(k)):
        os.makedirs(folder+str(k))
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.rename(file_path, folder+str(k)+'/'+file_path.split('/')[-1])
        except Exception as e:
            print(e)
    pickle.dump(dict_values, open(folder+str(k)+'/'+'data.pkl', 'w'))


def clean_positions(p1, p2):
    if len(p1) == 0:
        p1 = p2[:]
    elif len(p2) == 0:
        p2 = p1[:]
    if len(p1) > 0:
        p1 = p1[0]
    if len(p2) > 0:
        p2 = p2[0]
    return p1, p2
        

def check_position_last(tree):
    folder = '/home/'+user+'/.local/share/mupen64plus/screenshot/'
    final = sorted(os.listdir(folder))[-1]
    _, _, final_p1, final_p2 = prepare_image(folder+final)
    final_p1, final_p2 = clean_positions(final_p1, final_p2)
    return final_p1, final_p2


def check_position_tree(tree):
    folder = '/home/'+user+'/.local/share/mupen64plus/screenshot/'+str(tree)+'/'
    initial = sorted(os.listdir(folder))[1]
    _, _, initial_p1, initial_p2 = prepare_image(folder+initial)
    final = sorted(os.listdir(folder))[-1]
    _, _, final_p1, final_p2 = prepare_image(folder+final)
    initial_p1, initial_p2 = clean_positions(initial_p1, initial_p2)
    final_p1, final_p2 = clean_positions(final_p1, final_p2)
    return final_p1 - initial_p1, final_p2 - initial_p2

## Get user for path purposes
user = getpass.getuser()

## Get buttons struct for each controller
debug.buttons_override(reset=True)
buttons = {}
buttons['0'] = debug.buttons_override_struct_last(controller=0)
buttons['1'] = debug.buttons_override_struct_last(controller=1)

## Assume acceleration all the time
buttons['0'].a_button = 1
buttons['1'].a_button = 1

## Number of rollouts
n_trees = 5

## Clean folders of screenshots
clean_folder('/home/'+user+'/.local/share/mupen64plus/screenshot/')
for i in range(n_trees):
    folder = '/home/'+user+'/.local/share/mupen64plus/screenshot/'+str(i)
    if os.path.isdir(folder):
        clean_folder(folder)

## Load state of race
core.state_load()
time.sleep(0.5)
## Change saving slot to preserve beginning of race
core.state_set_slot(1)

## Pause game to read frame by frame
core.pause()
## Initialize file with random value
random_file(0)
random_file(1)
## Counter of screenshots, the emulator only lets us save up to 1000, needs to be reset
n_screenshot = 0
## Initialize running var for the while loop
running = True
n_trees = 1
while running == True:
    ## Negative and positive values accepted. 
    ## Need to check range of values (probably -128, 128)
    ## Save state before rollout
    core.state_save()
    ## Deploy trees 
    max_reward = -1000
    for k in range(n_trees):
        dict_values = {}
        dict_values[0] = []
        dict_values[1] = []
        ## 30 frames per tree
        core.take_next_screenshot()
        time.sleep(0.2)
        core.advance_frame()
        for i in range(200):
            n_screenshot += 1
            input_read(buttons, 0)
            input_read(buttons, 1)
            dict_values[0].append(buttons['0'].x_axis)
            dict_values[1].append(buttons['1'].x_axis)
            debug.buttons_override_struct(buttons['0'], 0)
            debug.buttons_override_struct(buttons['1'], 1)
            # core.take_next_screenshot()
            time.sleep(0.01)
            core.advance_frame()
        core.take_next_screenshot()
        time.sleep(0.2)
        core.advance_frame()
        move_data(k, dict_values)
        try:
            reward_p1, reward_p2 = check_position_tree(k)
        except:
            reward_p1 = 0
        clean_folder('/home/'+user+'/.local/share/mupen64plus/screenshot/'+str(k))
        print max_reward, reward_p1
        if reward_p1 > max_reward:
            max_reward = reward_p1
            core.state_set_slot(2)
            time.sleep(0.2)
            core.state_save()
            time.sleep(0.4)
            core.advance_frame()
        core.state_set_slot(1)
        time.sleep(0.2)
        core.state_load()
        time.sleep(0.2)
        random_file(0)
        random_file(1)
    if reward_p1 != 0 or reward_p2 !=0:
        n_trees = 5
    ## Create exit.txt file to exit while loop
    if os.path.isfile('../scripts/exit.txt'):
        os.unlink('../scripts/exit.txt')
        running = False
    core.state_set_slot(2)
    time.sleep(0.2)
    core.state_load()
    time.sleep(0.2)
    core.state_set_slot(1)
    time.sleep(0.2)
debug.buttons_override_disable()
