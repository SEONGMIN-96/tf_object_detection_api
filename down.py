BASE_URL = 'http://download.tensorflow.org/models/object_detection/' 
MODEL_NAME = 'faster_rcnn_resnet50_coco_2018_01_28'                 
MODEL_FILE = MODEL_NAME + '.tar.gz'                         
                                                           
 
DOWNLOAD_URL = BASE_URL + MODEL_FILE
DOWNLOAD_PATH = './pretrained_model'
 
import os
if not os.path.isdir(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)
    
import six.moves.urllib as urllib
 
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'ballentain')
opener.retrieve(DOWNLOAD_URL, filename = DOWNLOAD_PATH + '/' + MODEL_FILE)
print('모델 다운로드 완료...')
 
 
import tarfile
tar_file = tarfile.open(DOWNLOAD_PATH + '/' + MODEL_FILE)                                               
tar_file.extractall(DOWNLOAD_PATH)
 
print('압축 해제 완료...')