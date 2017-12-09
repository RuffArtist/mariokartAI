import cv2
import numpy as np

def prepare_image(path):

    def find_area_box_players():
        positions_red = []
        positions_green = []
        colors_red = []
        colors_green = []
        positions_red_box = []
        positions_green_box = []
        previous_red = False
        previous_green = False
        max_color_red = 0
        max_color_green = 0
        for i in xrange(shape[1]):
            color_col = im_rewards[:,i,:]
            b = sum([color_col[idx_col, 0] for idx_col in xrange(im_rewards.shape[0])])/im_rewards.shape[0]
            g = sum([color_col[idx_col, 1] for idx_col in xrange(im_rewards.shape[0])])/im_rewards.shape[0]
            r = sum([color_col[idx_col, 2] for idx_col in xrange(im_rewards.shape[0])])/im_rewards.shape[0]

            if (r > g*20) and (r > b*20):
                if previous_red == True:
                    if max_color_red < r:
                        max_color_red = r
                        positions_red[len(positions_red)-1] = i
                        colors_red[len(colors_red)-1] = r
                else:
                    max_color_red = r
                    previous_red = True
                    positions_red.append(i)
                    colors_red.append(r)
            else:
                previous_red = False

            if (g > r*20) and (g > b*20):
                if previous_green == True:
                    if max_color_green < g:
                        max_color_green = g
                        positions_green[len(positions_green)-1] = i
                        colors_green[len(colors_green)-1] = g
                else:
                    max_color_green = g
                    previous_green = True
                    positions_green.append(i)
                    colors_green.append(g)
            else:
                previous_green = False

        if len(positions_red) > 2 or len(positions_green) > 2:
            if len(positions_red) > 0:
                positions_red_box.append(min(positions_red))
                positions_red_box.append(max(positions_red))
                print 'Position red box: '
                print positions_red_box
            if len(positions_green) > 0:
                positions_green_box.append(min(positions_green))
                positions_green_box.append(max(positions_green))
                print 'Position green box: '
                print positions_green_box

        elif len(positions_red) == 0 and len(positions_green) == 0:
            print 'No positions at all . . . . . . .'

        else:
            positions_red_box = positions_red
            positions_green_box = positions_green
            print 'Position red box: '
            print positions_red_box
            print 'Position green box: '
            print positions_green_box

        return positions_red_box, positions_green_box

    im = cv2.imread(path)
    shape = im.shape
    if shape[0]%2 != 0:
        im = im[0:shape[0]-1,:,:]
        shape = im.shape
    factor = 360.0/shape[0]
    im = cv2.resize(im, None, fx= factor , fy=factor , interpolation=cv2.INTER_CUBIC)
    shape = im.shape
    im_1 = im[0:shape[0]/2,:,:]
    im_2 = im[shape[0]/2:shape[0],:,:]
    im_rewards = im[shape[0] / 2 -1 :shape[0] /2 + 3 , :, :]

    positions_red_box, positions_green_box = find_area_box_players()

    return im_1, im_2, positions_red_box, positions_green_box


if __name__ == '__main__':
    path = 'mariokart64-544.png'
    prepare_image(path)