import os
import cv2

def build_data():
    card_list = os.listdir('all_cards/')
    card_list.sort()

    cards_data = []

    for card in card_list:
        aux = card
        s = 'train_cards/cards/' + aux[:-4]
        print(s)
        try:
            os.mkdir(s)
        except:
            print('Folder exists')

        img = cv2.imread('all_cards/' + card, cv2.IMREAD_UNCHANGED)

        s = 'train_cards/cards/' + card[:-4] + '/' + card
        # print(s)
        cv2.imwrite(s, img)
        cards_data.append(img)

build_data()
