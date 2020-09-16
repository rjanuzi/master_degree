from dataset.local import (make_train_generator, NEW_WIDTH, NEW_HEIGHT)
from models.basic_cnn import BasicCNN

BATCH_SIZE = 2000

def train(model):
    total_imgs = 0
    loops = 0

    # The batch generator returns pairs of (imgs, target)
    for X, y in make_train_generator(batch_size=BATCH_SIZE):
        total_imgs += len(X)
        loops += 1
        print(total_imgs, loops)
        
        model.fit(X, y, epochs=30)

def test(model):
    raise Exception('Not implemented yet')

def save_model(model):
    raise Exception('Not implemented yet')

train(BasicCNN((NEW_WIDTH, NEW_HEIGHT, 3), 1))
